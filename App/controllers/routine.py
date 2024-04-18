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
    routine = Routines.query.filter_by(id=id).first()
    if routine:
        return routine
    else:
        return None

def update_routine(id, new_name):
    routine = Routines.query.get(id)
    if routine and new_name is not None:
        routine.name = new_name
        db.session.commit()

