from flask import Flask, render_template, url_for
from constants import POSTS, USERS

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
    return render_template('users.html', title='Users', users=USERS)


if __name__ == '__main__':
    app.run(debug=True)
