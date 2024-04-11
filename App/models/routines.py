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

    def __init__(self, name, work_1, work_2, work_3, work_4, work_5, work_6, work_7, work_8, work_9, work_10):
        self.name = name
        self.work_1 = work_1
        self.work_2 = work_2
        self.work_3 = work_3
        self.work_4 = work_4
        self.work_5 = work_5
        self.work_6 = work_6
        self.work_7 = work_7
        self.work_8 = work_8
        self.work_9 = work_9
        self.work_10 = work_10
        