import os
from flask import Flask, render_template, request, redirect, url_for
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
    return render_template('base.html')

@app.route('/support/')
def guide():
    return render_template('support.html')

@app.route('/pricing/')
def pricing():
    return render_template('pricing.html')

@app.route('/guide/')
def guide():
    return render_template('guide.html')

@app.route('/login/')
def guide():
    return render_template('login.html')

@app.route('/register/')
def guide():
    return render_template('register.html')

@app.route('/overlay/<int:group_id>/')
def guide(group_id):
    return render_template('overlay.html', group_id=group_id)

@app.route('/profile/')
def guide():
    return render_template('profile.html')

@app.route('/groups/')
def groups():
    db_con = db.get_db_con()
    groups = db_con.execute("SELECT id, name FROM groups").fetchall()
    return render_template("groups.html", groups=groups)

@app.route('/group/<int:group_id>/')
def group(group_id):
    return render_template('group.html', group_id=group_id)

@app.route('/create_group/', methods=['GET', 'POST'])
def create_group():
    if request.method == 'POST':
        # Handle group creation logic here
        return redirect(url_for('groups'))
    return render_template('create_group.html')



@app.route('/insert/sample/')
def run_insert_sample():
    db.insert_sample()
    return "Sample data inserted."