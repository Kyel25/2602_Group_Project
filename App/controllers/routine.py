from App.models import Workouts, Routines
from App.database import db

def create_routine(name):
    newroutine = routines(name=name)
    db.session.add(newroutine)
    db.session.commit()
    return newroutine

def list_all_routines():
    routines = Routines.query.all()
    return routines

def get_routine_by_id(id):
    routine = routines.query.filter_by(id=id).first()
    if routine:
        return routine
    else:
        return None



