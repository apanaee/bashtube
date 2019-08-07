from bashtube import db


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    role = db.Column(db.CHAR, nullable=False, unique=False)  # M - member,A - admin

    def __repr__(self):
        return f'({Users.id}>) <{Users.name}>'
