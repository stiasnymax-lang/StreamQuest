
from flask import redirect, session, url_for, flash

def logincheck():
    if 'user_id' not in session:
        flash('Please log in to see the content.')
        return redirect(url_for('login'))