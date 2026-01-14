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

@app.route('/support/')
def support():
    return render_template('support.html')

@app.route('/pricing/')
def pricing():
    return render_template('pricing.html')

@app.route('/guide/')
def guide():
    return render_template('guide.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return redirect(url_for('login'))    
    return render_template('register.html')
 
@app.route('/profile/')
def profile():
    db_con = db.get_db_con()
    user = db_con.execute("SELECT id, username FROM users WHERE id = ?", (1,)).fetchone()
    return render_template('profile.html', user=user)

@app.route('/groups/')
def groups():
    db_con = db.get_db_con()
    groups = db_con.execute("SELECT id, name FROM groups ORDER BY name").fetchall()
    return render_template('groups.html', groups=groups)

@app.route('/group/<int:group_id>/')
def group(group_id):
    db_con = db.get_db_con()

    group_row = db_con.execute(
        "SELECT id, name FROM groups WHERE id = ?",
        (group_id,)
    ).fetchone()
    if group_row is None:
        abort(404)

    group_members = db_con.execute(
        """
        SELECT u.id, u.username
        FROM users u
        JOIN group_members gm ON gm.user_id = u.id
        WHERE gm.group_id = ?
        ORDER BY u.username
        """,
        (group_id,)
    ).fetchall()

    return render_template('group.html', group=group_row, group_members=group_members)

@app.route('/create_group/', methods=['GET', 'POST'])
def create_group():
    if request.method == 'POST':
        name = request.form['name']

        db_con = db.get_db_con()
        # Achtung: muss zu deinem Schema passen!
        # Wenn groups owner_id/password NOT NULL hat, musst du die mit angeben.
        db_con.execute(
            "INSERT INTO groups (name, password, owner_id) VALUES (?, ?, ?)",
            (name, "devpass", 1)
        )
        db_con.commit()

        return redirect(url_for('groups'))

    return render_template('create_group.html')

@app.route('/insert/sample/')
def run_insert_sample():
    db.insert_sample()
    return "Sample data inserted."
