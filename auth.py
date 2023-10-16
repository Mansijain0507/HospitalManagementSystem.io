from flask import Blueprint, render_template, redirect, url_for, request, flash
# from werkzeug.security import generate_password_hash, check_password_hash
from models import User  # type: ignore
from flask_login import login_user, logout_user, login_required, current_user
from __init__ import db
import re


auth = Blueprint('auth', __name__)
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False
        if (len(email) == 0 or len(password) == 0):
            flash("Please enter all your details.")
            return redirect(url_for('auth.login'))

        user = User.query.filter_by(email=email).first()

        if not user:
            flash('Please sign up before!')
            # error = 'Please sign up before!'
            return redirect(url_for('auth.signup'))
        elif not (user.password, password):
            # error = 'Please Check your login details and try again.'
            flash('Please check your login details and try again.')
            return redirect(url_for('auth.login'))
        else:

            login_user(user, remember=remember)
            flash('You are successfully login to your profile')
            id = current_user.id
            if id == 1:
                return redirect(url_for('main.admin'))
            else:
                return redirect(url_for('main.profile'))


@auth.route('/signup', methods=['GET', 'POST'])
def signup():

    if request.method == 'GET':
        return render_template('signup.html')
    else:
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        if not (re.fullmatch(regex, email)):
            flash("Invalid email")
            return redirect(url_for('auth.signup'))

        if (len(email) == 0 or len(name) == 0 or len(password) == 0):
            flash("Please enter all your details.")
            return redirect(url_for('auth.signup'))
        else:
            user = User.query.filter_by(email=email).first()
            if user:
                flash('Email address already exists')
                return redirect(url_for('auth.signup'))

            new_user = User(email=email, name=name, password=password)

            db.session.add(new_user)
            db.session.commit()
        return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
