from functools import wraps
from flask import redirect, session, url_for, flash, request

def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to see the content.')
            return redirect(url_for('login', next=request.path))
        return view(*args, **kwargs)
    return wrapped
