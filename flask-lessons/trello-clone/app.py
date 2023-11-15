from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://trello_dev:nahui@localhost:5432/trello'

db = SQLAlchemy(app)

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.text())
    date_created = db.Column(db.Date())


@app.cli.command('db_create')
def db_create():
    db.create_all()
    print('Created tables')


@app.route('/')
def index():
    return 'Hello world!'

