from flask_1.constants import POSTS
from flask_1.users2 import get_users_comp
from flask_1.models import User, Post
from flask_1.forms import RegistrationForm, LoginForm
from flask import render_template, url_for, flash, redirect
from flask_1 import app


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=POSTS)


@app.route('/about')
def about():
    return render_template('about2.html', title='About')


@app.route('/users')
def users():
    users_py = get_users_comp()
    return render_template('users.html', title='Users', users=users_py)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. PLease check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
