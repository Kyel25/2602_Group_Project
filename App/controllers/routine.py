from App.models import workouts, routines
from App.models.user import get_user_by_username
from App.database import db

def create_routine(name):
    newroutine = routines(name=name)
    db.session.add(newroutine)
    db.session.commit()
    return newroutine

def get_routine_by_id(id):
    routine = routines.query.filter_by(id=id).first()
    if routine:
        return routine
    else:
        return None


def create_routine_and_add_to_user(username, routine_name):
    # Get the user by username
    user = get_user_by_username(username)
    if user:
        # Create the routine
        new_routine = create_routine(routine_name)
        if new_routine:
            # Associate the routine with the user
            new_routine.user_id = user.id
            db.session.commit()
            return "Routine '{}' added to user '{}' successfully.".format(routine_name, username)
        else:
            return "Failed to create the routine."
    else:
        return "User '{}' not found.".format(username)

