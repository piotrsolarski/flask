from flask import Flask, render_template, url_for

from constants import POSTS
from forms import RegistrationForm, LoginForm
from users2 import get_users_comp

app = Flask(__name__)

app.config['SECRET_KEY'] = 'f8824c95c795fc09db2c87f8aea49692'


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


@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
