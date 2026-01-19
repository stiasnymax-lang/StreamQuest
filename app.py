import os
from flask import Flask, render_template, redirect, session, url_for, request, abort, flash
import db, forms

app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'data.sqlite'),
)

app.cli.add_command(db.init_db)
app.teardown_appcontext(db.close_db_con)


@app.route('/')
def index():
    form = forms.ProfileForm()
    form.user_id.data = session['user_id']
    return render_template('index.html')

@app.route('/overlay/<int:group_id>/')
def overlay(group_id):
    logincheck()

    db_con = db.get_db_con()
    group_row = db_con.execute(
        "SELECT id, name FROM groups WHERE id = ?",
        (group_id,)
    ).fetchone()
    if group_row is None:
        abort(404) 

    active_challenge = db_con.execute("""
        SELECT c.*, gc.status
        FROM group_challenges gc
        JOIN challenges c ON c.id = gc.challenge_id
        WHERE gc.group_id = ? AND gc.status = 'active'
        ORDER BY gc.started_at DESC, gc.assigned_at DESC
        LIMIT 1
    """, (group_id,)).fetchone()

    done_challenges = db_con.execute("""
        SELECT c.*, gc.status
        FROM group_challenges gc
        JOIN challenges c ON c.id = gc.challenge_id
        WHERE gc.group_id = ? AND gc.status = 'done'
        ORDER BY gc.assigned_at DESC
    """, (group_id,)).fetchall()

    queued_challenges = db_con.execute("""
        SELECT c.*, gc.status
        FROM group_challenges gc
        JOIN challenges c ON c.id = gc.challenge_id
        WHERE gc.group_id = ? AND gc.status = 'queued'
        ORDER BY gc.assigned_at DESC
    """, (group_id,)).fetchall()

    return render_template(
        'overlay.html',
        group_name=group_row['name'],
        active_challenge=active_challenge,
        queued_challenges=queued_challenges,
        done_challenges=done_challenges
        )

# -------- Challenges --------

@app.route('/challenges/')
def challenges():
    db_con = db.get_db_con()
    challenges = db_con.execute(
        "SELECT id, title, difficulty, game_name, time_needed FROM challenges ORDER BY title"
    ).fetchall()
    return render_template('challenges.html', challenges=challenges)


@app.route('/challenge/<int:challenge_id>/')
def challenge(challenge_id):
    db_con = db.get_db_con()

    challenge_row = db_con.execute(
        """
        SELECT id, title, description, difficulty, game_name, time_needed
        FROM challenges
        WHERE id = ?
        """,
        (challenge_id,) 
    ).fetchone() 

    if challenge_row is None:
        abort(404)

    return render_template('challenge.html', challenge=challenge_row)


# -------- Static pages --------

@app.route('/support/')
def support():
    return render_template('support.html')


@app.route('/pricing/')
def pricing():
    return render_template('pricing.html')


@app.route('/guide/')
def guide():
    return render_template('guide.html')


# -------- Authentication --------

@app.route('/login/', methods=['GET', 'POST'])
def login():
    db_con = db.get_db_con()
    form = forms.LoginForm()

    if request.method == 'GET':
        sql_query = "SELECT id, username FROM users ORDER BY username"
        users = db_con.execute(sql_query).fetchall()
        return render_template('login.html', form=form, users=users)
    else:  # POST
        if form.validate():
            username = form.username.data
            password = form.password.data

            user = db_con.execute(
                "SELECT id, password FROM users WHERE username = ?",
                (username,)
            ).fetchone()
            if user and password == user['password']:
                session['user_id'] = user['id']
                flash('Login successful.', 'success')
                return redirect(url_for('index'))
            else: 
                flash('Invalid username or password.', 'error')
        else:   
            flash("Please fill out the form correctly.", 'error')
    return render_template('login.html', form=form)


@app.route('/register/', methods=['GET', 'POST'])
def register():

    db_con = db.get_db_con()
    form = forms.RegisterForm()

    if request.method == 'GET':
        sql_query = "SELECT * FROM users ORDER BY id"
        users = db_con.execute(sql_query).fetchall()
        return render_template('register.html', form=form, users=users)
    else:  # POST
        if form.validate():
            sql_query = "INSERT INTO users (username, password, email) VALUES (?, ?, ?);"
            username = form.username.data
            password = form.password.data
            email = form.email.data
            db_con.execute(sql_query, (username, password, email))
            db_con.commit()
            flash('Registration successful. Please log in.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Error in registration form. Please check the input fields.', 'error')
    return render_template('register.html', form=form)



# -------- Profile --------

@app.route('/profile/')
def profile():
    logincheck()

    db_con = db.get_db_con()
    user_id = session['user_id']

    user = db_con.execute(
        "SELECT id, username, email, abonoment FROM users WHERE id = ?",
        (user_id,)
    ).fetchone()

    return render_template('profile.html', user=user)


# -------- Groups --------

@app.route('/groups/')
def groups():
    db_con = db.get_db_con()
        #search functionality
    g = request.args.get("g", "").strip().lower()

    groups = db_con.execute(
        "SELECT id, name FROM groups WHERE lower(name) LIKE ? ORDER BY name", (f"%{g}%",)
    ).fetchall()
    return render_template('groups.html', groups=groups, g=g)

@app.route('/join/<int:group_id>/')
def join_group(group_id):
    logincheck()
    db_con = db.get_db_con()
    form = forms.JoinGroupForm()
    user_id = session['user_id']

    # Hole Gruppeninfo (inkl. password und owner_id)
    group_row = db_con.execute(
        "SELECT id, name, password, owner_id FROM groups WHERE id = ?",
        (group_id,)
    ).fetchone()
    if group_row is None:
        abort(404)
    
    # Prüfe, ob User bereits Mitglied ist
    existing_member = db_con.execute(
        "SELECT 1 FROM group_members WHERE user_id = ? AND group_id = ?",
        (user_id, group_id)
    ).fetchone()
    if existing_member:
        flash('You are already a member of this group.', 'info')
        return redirect(url_for('group', group_id=group_id))
    
    # Füge User als Mitglied hinzu und Prüfe Passwort
    if request.method == 'GET':
        return render_template('join_group.html', form=form, group=group_row)
    else:  # POST
        if form.validate():
            if form.password.data == group_row['password']:
                # Füge User zur Gruppe hinzu
                db_con.execute(
                    "INSERT INTO group_members (owner_id, user_id, group_id) VALUES (?, ?, ?)",
                    (group_row['owner_id'], user_id, group_id)
                )
                db_con.commit()
                flash('Successfully joined the group!', 'success')
                return redirect(url_for('group', group_id=group_id))
            else:
                flash('Invalid group password.', 'error')
        else:
            flash('Please enter the group password.', 'error')
        return render_template('join_group.html', form=form, group=group_row)

@app.route('/group/<int:group_id>/', methods=["GET", "POST"])
def group(group_id):
    logincheck()
    
    db_con = db.get_db_con()
    user_id = session['user_id']
    form = forms.GroupForm()
    
    # Prüfe, ob User Mitglied oder Owner ist
    is_member = db_con.execute(
        "SELECT 1 FROM group_members WHERE user_id = ? AND group_id = ?",
        (user_id, group_id)
    ).fetchone()

    group_row = db_con.execute(
        "SELECT id, owner_id, name FROM groups WHERE id = ?",
        (group_id,)
    ).fetchone()
    if group_row is None:
        abort(404)
    
    owner = db_con.execute(
        "SELECT id, username FROM users WHERE id = ?",
        (group_row["owner_id"],)
    ).fetchone()

    group_members = db_con.execute("""
        SELECT u.id, u.username, owner_id
        FROM group_members gm 
        JOIN users u ON u.id = gm.user_id
        WHERE u.id != owner_id AND gm.group_id = ?
    """, (group_id,)).fetchall()

    active_challenge = db_con.execute("""
        SELECT c.*, gc.status
        FROM group_challenges gc
        JOIN challenges c ON c.id = gc.challenge_id
        WHERE gc.group_id = ? AND gc.status = 'active'
        ORDER BY gc.started_at DESC, gc.assigned_at DESC
        LIMIT 1
    """, (group_id,)).fetchone()

    done_challenges = db_con.execute("""
        SELECT c.*, gc.status
        FROM group_challenges gc
        JOIN challenges c ON c.id = gc.challenge_id
        WHERE gc.group_id = ? AND gc.status = 'done'
        ORDER BY gc.assigned_at DESC
    """, (group_id,)).fetchall()

    queued_challenges = db_con.execute("""
        SELECT c.*, gc.status
        FROM group_challenges gc
        JOIN challenges c ON c.id = gc.challenge_id
        WHERE gc.group_id = ? AND gc.status = 'queued'
        ORDER BY gc.assigned_at DESC
    """, (group_id,)).fetchall()

    #search functionality
    q = request.args.get("q", "").strip().lower()

    challenges = db_con.execute("""
        SELECT id, title
        FROM challenges
        WHERE title LIKE ? AND id NOT IN (
            SELECT challenge_id FROM group_challenges WHERE group_id = ?
        );
    """, (f"%{q}%", group_id)).fetchall()


    if request.method == 'GET':
        return render_template(
            "group.html",
            group=group_row,
            owner=owner,
            group_members=group_members,
            active_challenge=active_challenge,
            done_challenges=done_challenges,
            queued_challenges=queued_challenges, 
            is_member=is_member,
            challenges=challenges,
            q=q,
            form=form
        )
    else: #request.method == 'POST'
        
        if form.validate_on_submit():
            if form.add_challenge.data:
                sql_query = """
                    INSERT OR IGNORE INTO group_challenges (group_id, challenge_id)
                    VALUES (?, ?);
                """
                db_con.execute(sql_query, [form.group_id.data, form.challenge_id.data])
                db_con.commit()
                flash('Challenge has been added', 'success')
            if form.delete_challenge.data:
                sql_query = """
                    DELETE FROM group_challenges
                    WHERE group_id = ? AND challenge_id = ?;
                """
                db_con.execute(sql_query, [form.group_id.data, form.challenge_id.data])
                db_con.commit()
                flash('Challenge has been deleted', 'success')
            return redirect(url_for('group', group_id=group_id))



# -------- Create Group ---------

@app.route('/create_group/', methods=['GET', 'POST'])
def create_group():

    logincheck()
    
    db_con = db.get_db_con()
    form = forms.CreateGroupForm()

    form.user_id.data = session.get('user_id') 

    if request.method == 'GET':
        return render_template('create_group.html', form=form)
    
    else: #request.method == 'POST'
        if form.validate():
            sql_query = 'INSERT INTO groups (name, password, owner_id) VALUES (?, ?, ?);'
            db_con.execute(sql_query, [form.name.data, form.password.data, form.user_id.data])  
            db_con.commit()
            flash('Group has been created.', 'success') 
        else: 
            flash('Error creating group. Please check the input fields.', 'error') 
        return redirect(url_for('groups')) # groups fürs debugging --> /group/<int:group_id>/ direkt zur erstellten
        

@app.route('/insert/sample/')
def run_insert_sample():
    db.insert_sample() 
    return "Sample data inserted."

def logincheck():
    if 'user_id' not in session:
        flash('Please log in to see the content.')
        return redirect(url_for('login'))
