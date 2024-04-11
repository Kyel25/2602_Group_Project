import csv
from App.models import Workouts
from App.database import db

def parse_workouts():
    with open('/workspace/2602_Group_Project/megaGymDataset.csv', encoding='unicode_escape') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        for row in reader:
            workout = Workouts(title=row['Title'],
                description = row['Desc'],
                body_part = row['BodyPart'],
                equipment = row['Equipment'],
                level = row['Level'],
                rating = row['Rating'],
                rating_desc = row['RatingDesc'])
            db.session.add(workout)
        db.session.commit()