from App.models import Workouts, Routines
from App.database import db

def create_routine(name):
    newroutine = Routines(name=name)
    db.session.add(newroutine)
    db.session.commit()
    return newroutine

def delete_routine(id):
    routine = Routines.query.get(id)
    db.session.delete(routine)
    db.session.commit()
    return None

def list_all_routines():
    routines = Routines.query.all()
    return routines

def get_routine_by_id(id):
    routine = routines.query.filter_by(id=id).first()
    if routine:
        return routine
    else:
        return None



