from App.models import Workouts, Routines
from App.database import db

def create_routine(name):
    newroutine = Routine(name=name)
    db.session.add(newroutine)
    db.session.commit()
    return newroutine

def get_routine_by_id(id):
    routine = Routine.query.filter_by(id=id).first()
    if routine:
        return routine
    else:
        return None


