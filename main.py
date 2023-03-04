from flask import Flask


app = Flask(__name__)


@app.route('/')
def index_page():
    return 'Hello!'


@app.route('/profile/<uid>')
def profile_page(uid):
    return f'User <h3>{uid}</h3> profile'


@app.route('/profile/<uid>/feed/')
def feed_page(uid):
    return f'User <h3>{uid}</h3> feed'


@app.route('/messages/')
def messages():
    return 'User\'s messages'


app.run()
