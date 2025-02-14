# if using run.py file for shell context processor - change your FLASK_APP .env variable to run.py
# we may have to change a config variable to get this to work

from app import create_app
from app.models import db, Program
from flask_cors import CORS

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

# @app.shell_context_processor
# def shell_context():
#     return{'db': db, "Program": Program}