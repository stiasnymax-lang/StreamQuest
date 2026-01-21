import os
from flask import Flask, render_template, redirect, session, url_for, request, abort, flash, jsonify

def logincheck():
    if 'user_id' not in session:
        flash('Please log in to see the content.')
        return redirect(url_for('login'))