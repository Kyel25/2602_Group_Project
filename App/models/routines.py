from App.database import db

class Routines(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    work_1 = db.Column(db.Integer, db.ForeignKey("workouts.id"), nullable=True, unique=True)
    work_2 = db.Column(db.Integer, db.ForeignKey("workouts.id"), nullable=True, unique=True)
    work_3 = db.Column(db.Integer, db.ForeignKey("workouts.id"), nullable=True, unique=True)
    work_4 = db.Column(db.Integer, db.ForeignKey("workouts.id"), nullable=True, unique=True)
    work_5 = db.Column(db.Integer, db.ForeignKey("workouts.id"), nullable=True, unique=True)
    work_6 = db.Column(db.Integer, db.ForeignKey("workouts.id"), nullable=True, unique=True)
    work_7 = db.Column(db.Integer, db.ForeignKey("workouts.id"), nullable=True, unique=True)
    work_8 = db.Column(db.Integer, db.ForeignKey("workouts.id"), nullable=True, unique=True)
    work_9 = db.Column(db.Integer, db.ForeignKey("workouts.id"), nullable=True, unique=True)
    work_10 = db.Column(db.Integer, db.ForeignKey("workouts.id"), nullable=True, unique=True)

    def __init__(self, name):
        self.name = name
        