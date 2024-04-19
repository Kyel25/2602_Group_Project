from App.database import db

class Workouts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    type = db.Column(db.String(80), nullable=True)
    description = db.Column(db.String, nullable=True)
    bodypart = db.Column(db.String(80), nullable=False)
    equipment = db.Column(db.String(80), nullable=False)
    level = db.Column(db.String(40), nullable=False)
    rating = db.Column(db.String(80), nullable=True)
    rating_desc = db.Column(db.String(120), nullable=True)
    routine_id = db.Column(db.Integer, db.ForeignKey('routines.id'), nullable=True)

    def init(self, title, description, type, bodypart, equipment, level, rating, rating_desc, routine_id):
        self.title = title
        self.description = description
        self.type = type
        self.body_part = body_part
        self.equipment = equipment
        self.level = level
        self.rating = rating
        self.rating_desc = rating_desc
        self.routine_id = routine_id

    def get_json(self):
        return{
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'type': self.type,
            'body part': self.body_part,
            'equipment': self.equipment,
            'level': self.level,
            'rating': self.rating,
            'rating_desc': self.rating_desc,
            'routine_id': self.routine_id
        }