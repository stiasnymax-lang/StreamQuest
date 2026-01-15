import os
from flask import Flask, render_template, redirect, url_for, request, abort, flash
import db

app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'data.sqlite'),
)

app.cli.add_command(db.init_db)
app.teardown_appcontext(db.close_db_con)


@app.route('/')
def index():
    return render_template('index.html')


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


# -------- Auth (placeholder) --------

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Dein Form muss name="username" / name="password" haben
        username = request.form['username']
        password = request.form['password']

        # TODO: hier später DB-Check + session['user_id'] setzen
        return redirect(url_for('index'))

    return render_template('login.html')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # TODO: user speichern (inkl. email) + passwort hashen
        return redirect(url_for('login'))

    return render_template('register.html')


# -------- Profile --------

@app.route('/profile/')
def profile():
    db_con = db.get_db_con()

    # TODO: später aus session holen statt hart 1
    user = db_con.execute(
        "SELECT id, username, email, abonoment FROM users WHERE id = ?",
        (1,)
    ).fetchone()

    if user is None:
        abort(404)

    return render_template('profile.html', user=user)


# -------- Groups --------

@app.route('/groups/')
def groups():
    db_con = db.get_db_con()
    groups = db_con.execute(
        "SELECT id, name FROM groups ORDER BY name"
    ).fetchall()
    return render_template('groups.html', groups=groups)


@app.route('/group/<int:group_id>/')
def group(group_id):
    db_con = db.get_db_con()

    group_row = db_con.execute(
        "SELECT id, name, owner_id, challenge_id FROM groups WHERE id = ?",
        (group_id,)
    ).fetchone()
    if group_row is None:
        abort(404)

    owner = db_con.execute(
        "SELECT id, username, abonoment FROM users WHERE id = ?",
        (group_row["owner_id"],)
    ).fetchone()

    challenge = None
    if group_row["challenge_id"] is not None:
        challenge = db_con.execute(
            """
            SELECT id, title, description, difficulty, game_name, time_needed
            FROM challenges
            WHERE id = ?
            """,
            (group_row["challenge_id"],)
        ).fetchone()

    group_members = db_con.execute(
        """
        SELECT u.id, u.username, u.abonoment
        FROM users u
        JOIN group_members gm ON gm.user_id = u.id
        WHERE gm.group_id = ?
        ORDER BY u.username
        """,
        (group_id,)
    ).fetchall()

    return render_template(
        'group.html',
        group=group_row,
        owner=owner,
        challenge=challenge,
        group_members=group_members
    )


@app.route('/create_group/', methods=['GET', 'POST'])
def create_group():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form.get('password', 'devpass')

        db_con = db.get_db_con()

        # TODO: owner_id später aus session holen
        db_con.execute(
            "INSERT INTO groups (name, password, owner_id) VALUES (?, ?, ?)",
            (name, password, 1)
        )
        db_con.commit()   

        return redirect(url_for('groups'))

    return render_template('create_group.html')


@app.route('/insert/sample/')
def run_insert_sample():
    db.insert_sample()
    return "Sample data inserted."
