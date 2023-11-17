from config.db_config import db

class Passenger(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Pclass = db.Column(db.Integer)
    Age = db.Column(db.Float)
    SibSp = db.Column(db.Integer)
    Parch = db.Column(db.Integer)
    Fare = db.Column(db.Float)
    Survived = db.Column(db.Integer)

def get_all_data():
    return Passenger.query.all()