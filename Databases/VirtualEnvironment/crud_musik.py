import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask('__name__')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:password@localhost/Musik'
db = SQLAlchemy(app)

class Artist(db.Model):
    artist_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), unique = False, nullable = False)
    birth_year = db.Column(db.Integer, unique = False, nullable = False)
    song = db.relationship('Song', backref = 'artist_id', lazy = True)

class Song(db.Model):
    song_id = db.Column(db.Integer, primary_key = True)
    artist = db.Column(db.Integer, db.ForeignKey('artist.artist_id'), nullable = False)
    name = db.Column(db.String(30), unique = False, nullable = False)
    runtime = db.Column(db.Integer, unique = False, nullable = False)
    tracklist = db.relationship('Tracklist', backref = 'song_id', lazy = True)

class Album(db.Model):
    album_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), unique = False, nullable = False)
    release_year = db.Column(db.Integer, unique = False, nullable = False)
    tracklist = db.relationship('Tracklist', backref = 'album_id', lazy = True)

class Tracklist(db.Model):
    album = db.Column(db.Integer, db.ForeignKey('album.album_id'), primary_key = True)
    song = db.Column(db.Integer, db.ForeignKey('song.song_id'), primary_key = True)

def run():
    with app.app_context():
        db.create_all()

        while True:
            os.system('cls')
            print('1. Add artist')
            print('2. Add song')
            print('3. Add album')
            print('0. Quit')
            opt = input('>>> ')
            if opt == '0':
                quit()
            elif opt == '1':
                artist = Artist()
                artist.name = input('Name the artist: ')
                artist.birth_year = int(input('Input date of birth: '))
                db.session.add(artist)
                db.session.commit()
            elif opt == '2':
                for artist in Artist.query.all():
                    print(f'{artist.artist_id}. {artist.name}')
                opt = int(input('Choose artist by number: '))
                try:
                    artist = Artist.query.filter_by(artist_id = opt).first()
                    song = Song()
                    song.artist = artist.artist_id
                    song.name = input('Name of song: ')
                    runtime = input('Length of song (m:s): ')
                    song.runtime = int(runtime.split(':')[-1]) + int(runtime.split(':')[-2]) * 60
                    db.session.add(song)
                    db.session.commit()
                except:
                    print('No artist with that id.')
            elif opt == '3':
                album = Album()
                album.name = input('Name the album: ')
                album.release_year = int(input('Input year of release: '))
                db.session.add(album)
                db.session.commit()

if __name__ == '__main__':
    run()

## TODO:    Add album (https://en.wikipedia.org/wiki/Hounds_of_Love)
##          Add tracklist