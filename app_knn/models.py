from config.db_config import db

class Flower(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sepal_length = db.Column(db.Float)
    sepal_width = db.Column(db.Float)
    petal_length = db.Column(db.Float)
    petal_width = db.Column(db.Float)
    species = db.Column(db.String(50))


def get_all_data():
    return Flower.query.all()