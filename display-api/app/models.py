from app import db


class Rapper(db.Model):
    __tablename__ = 'rappers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    birth_date = db.Column(db.String(255))

    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

    def __repr__(self):
        return 'Your Rapper name is    %r   Your best album was released in   %r ' % (self.name, self.birth_date)
