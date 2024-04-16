import csv
from App.models import Workouts
from App.database import db

def parse_workouts():
    with open('/workspace/2602_Group_Project/megaGymDataset.csv', encoding='unicode_escape') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        for row in reader:
            workout = Workouts(title=row['Title'],
                description = row['Desc'],
                type_ = row['Type'],
                body_part = row['BodyPart'],
                equipment = row['Equipment'],
                level = row['Level'],
                rating = row['Rating'],
                rating_desc = row['RatingDesc'])
            db.session.add(workout)
        db.session.commit()

def list_all_workouts():
    workouts = Workouts.query.all()
    return workouts

def list_workouts_by_type(type):
    workouts_by_type = Workouts.query.filter_by(type=type).all()
    return workouts_by_type

def list_workouts_by_body_part(body_part):
    workouts_by_type = Workouts.query.filter_by(body_part=body_part).all()
    return list_workouts_by_body_part

def list_workouts_by_level(level):
    workouts_by_type = Workouts.query.filter_by(level=level).all()
    return list_workouts_by_level

def list_all_workouts_json():
    workouts = Workouts.query.all()
    if not workouts:
        return []
    workouts = [Workouts.get_json() for workout in workouts]
    return workouts


    
