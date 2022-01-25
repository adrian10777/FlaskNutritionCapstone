# if using run.py file for shell context processor - change your FLASK_APP .env variable to run.py
# we may have to change a config variable to get this to work

from app import app
from app.models import db, Program

@app.shell_context_processor
def shell_context():
    return{'db': db, "Program": Program}