from flask import Flask
from config import Config  # <-- Add this import statement
from flask_mail import Mail
from flask_cors import CORS
from .api.routes2 import api
from .payments.routesstripe import payments
# import blueprints
from flask_sqlalchemy import SQLAlchemy
from celery import Celery

from .models import db
from flask_migrate import Migrate

mail = Mail()

#Application factory function
def create_app():
    app = Flask(__name__) # initialize the Flask app

    # Load configuration settings
    app.config.from_object(Config)

    #initialize celery with Flask config
    # celery = make_celery(app)

    #Initialize mail with app
    mail.init_app(app)

    CORS(app, origins="https://sda-nutrition.web.app")
    # CORS(app, origins="http://localhost:3000")

    # CORS(app, supports_credentials=True, 
    #      resources={r"/*": {"origins": "http://localhost:3000", 
    #                         "allow_headers": ["Content-Type", "Authorization"], 
    #                         "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
    #                        }})

    # You can import the routes after the app has been created to avoid circular imports

    from .routes import routes 
    app.register_blueprint(routes)

    return app

# def make_celery(app):
#     """Create a Celery instance using Flask app context."""
#     celery = Celery(
#         app.import_name,
#         backend=app.config['CELERY_RESULT_BACKEND'],
#         broker = app.config['CELERY_BROKER_URL']
#     )
#     celery.conf.update(app.config)

#     return celery



# app = Flask(__name__)
# CORS(app, origins=['*'])

# app.config.from_object(Config)

# app.config['MAIL_SERVER'] = 'smtp.gmail.com' # SMTP server for Gmail
# app.config['MAIL_PORT'] = 587 # Port for TLS (secure email sending)
# app.config['MAIL_USE_TLS'] = True # Enable TLS encryption
# app.config['MAIL_USERNAME'] = 'your_email@gmail.com' # Your email address
# app.config['MAIL_PASSWORD'] = 'your_email_password' # Your email password
# app.config['MAIL_DEFAULT_SENDER'] = 'your_email@gmail.com' #Default sender address

# app.register_blueprint(api)
# app.register_blueprint(payments)

# db.init_app(app)
# migrate = Migrate(app, db)
# from . import routes

