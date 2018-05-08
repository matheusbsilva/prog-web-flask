from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
import shelve

app = Flask(__name__)


class User:
    def __init__(self, username, description):
        self.username = username
        self.description = description
        self.likes = 0

    def save(self):
        if self.username is not None:
            with shelve.open("users") as db:
                users = db.get('users', [])
                users.append({'user': self.username, 'description': self.description})
                db['users'] = users

    def all(self):
        users = shelve.open("users")
        users = users['users']
        return users


@app.route('/')
def hello_world():
    return render_template('app.html')


@app.route('/register', methods=['POST', 'GET'])
def register_perfil():
    if request.method == 'POST':
        user = User(username=request.form['username'], description=request.form['description'])
        user.save()
        return redirect(url_for('hello_world'))
    if request.method == 'GET':
        return render_template('register.html')


@app.route('/match')
def match_love():
    users = 



