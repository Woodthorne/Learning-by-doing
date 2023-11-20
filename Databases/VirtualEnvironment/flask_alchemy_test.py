from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask('__name__')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:password@localhost/hockeybasen'
db = SQLAlchemy(app)

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    namn = db.Column(db.String(80), unique=False, nullable=False)
    city = db.Column(db.String(80), unique=False, nullable=False)
    players = db.relationship('Player', backref='team', lazy=True)

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    namn = db.Column(db.String(80), unique=False, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=False)
    jersey = db.Column(db.Integer, unique=False, nullable=False)
    team_id=db.Column(db.Integer, db.ForeignKey('team.id'),nullable=False)

with app.app_context():
    db.create_all()

    for num in range(100):
        team = Team()
        team.namn = f'Lag #{num}'
        team.city = 'Västerås'
        db.session.add(team)
    db.session.commit()

    for team in Team.query.all():
        print(f'{team.id} {team.namn} {team.city}')