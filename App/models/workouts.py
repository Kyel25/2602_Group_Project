from App.database import db

class Workouts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String, nullable=True)
    body_part = db.Column(db.String(80), nullable=False)
    equipment = db.Column(db.String(80), nullable=False)
    level = db.Column(db.String(40), nullable=False)
    rating = db.Column(db.String(80), nullable=True)
    rating_desc = db.Column(db.String(120), nullable=True)
    # routine_id = db.Column(db.Integer, db.ForeignKey('routine.id'), nullable=False)

    def __init__(self, title, description, body_part, equipment, level, rating, rating_desc):
        self.title = title
        self.description = description
        self.body_part = body_part
        self.equipment = equipment
        self.level = level
        self.rating = rating
        self.rating_desc = rating_desc