from App.database import db

class Routines(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    workouts = db.relationship('Workouts', backref='routine', lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    work_1 = db.Column(db.Integer, nullable=True, unique=False)
    work_2 = db.Column(db.Integer, nullable=True, unique=False)
    work_3 = db.Column(db.Integer, nullable=True, unique=False)
    work_4 = db.Column(db.Integer, nullable=True, unique=False)
    work_5 = db.Column(db.Integer, nullable=True, unique=False)
    work_6 = db.Column(db.Integer, nullable=True, unique=False)
    work_7 = db.Column(db.Integer, nullable=True, unique=False)
    work_8 = db.Column(db.Integer, nullable=True, unique=False)
    work_9 = db.Column(db.Integer, nullable=True, unique=False)
    work_10 = db.Column(db.Integer, nullable=True, unique=False)
    work_1_description = db.Column(db.Text, nullable=True)
    work_2_description = db.Column(db.Text, nullable=True)
    work_3_description = db.Column(db.Text, nullable=True)
    work_4_description = db.Column(db.Text, nullable=True)
    work_5_description = db.Column(db.Text, nullable=True)
    work_6_description = db.Column(db.Text, nullable=True)
    work_7_description = db.Column(db.Text, nullable=True)
    work_8_description = db.Column(db.Text, nullable=True)
    work_9_description = db.Column(db.Text, nullable=True)
    work_10_description = db.Column(db.Text, nullable=True)

    def __init__(self, name):
        self.name = name
        