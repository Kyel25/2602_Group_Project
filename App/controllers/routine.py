from App.models import Workouts, Routines
from App.database import db

def create_routine(name, id):
    newroutine = Routines(name=name)
    newroutine.user_id = id
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

def add_workout_to_routine(workout_num, routine_id, workout_id):
    if routine_id and workout_id and workout_num is not None:
        routine = Routines.query.filter_by(id = routine_id).first()
        workout = Workouts.query.filter_by(id = workout_id).first()
        if routine and workout is not None:
            if workout_num == "1":
                add_workout = routine.work_1 = workout.title
            elif workout_num == "2":
                add_workout = routine.work_2 = workout.title
            elif workout_num == "3":
                add_workout = routine.work_3 = workout.title
            elif workout_num == "4":
                add_workout = routine.work_4 = workout.title
            elif workout_num == "5":
                add_workout = routine.work_5 = workout.title
            elif workout_num == "6":
                add_workout = routine.work_6 = workout.title
            elif workout_num == "7":
                add_workout = routine.work_7 = workout.title
            elif workout_num == "8":
                add_workout = routine.work_8 = workout.title
            elif workout_num == "9":
                add_workout = routine.work_9 = workout.title
            else:
                add_workout = routine.work_10 = workout.title
            db.session.commit()
        else:
            return None
    else:
        return 6

