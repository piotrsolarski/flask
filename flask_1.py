from flask import Flask, render_template, url_for
from constants import POSTS, USERS
from users2 import get_transformed_users

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=POSTS)


@app.route('/about')
def about():
    return render_template('about2.html', title='About')


@app.route('/users')
def users():
    users_py = get_transformed_users()
    return render_template('users.html', title='Users', users=users_py)


if __name__ == '__main__':
    app.run(debug=True)
