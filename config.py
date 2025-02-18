import os
basedir = os.path.abspath(os.path.dirname(__name__))
class Config:
    """
    set config variables for our flask app
    """
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS= False
    
    MAIL_SERVER = 'mail.smtp2go.com'
    MAIL_PORT = 2525
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'SDA Nutrition'  # Replace with your actual email
    MAIL_PASSWORD = 'w4o9BlXfNSV7KTio'  # Replace with your actual password
    MAIL_DEFAULT_SENDER = 'sdanutrition@nutritionsda.com'  # Replace with your email
    # CELERY_BROKER_URL = 'redis://red-cuptcji3esus738ikfr0:6379'
    # CELERY_RESULT_BACKEND = 'redis://red-cuptcji3esus738ikfr0:6379'
# Explanation:
# - This config class stores the settings used by Flask to connect to the email server.
# - We define the email server 

#Config file
# this keeps sensitive settings seperate from app the main code. 
# Makes it easier to update setting without modifying  the apps core logic.

# if your email credentials or settings change, you can update this one file
# instead of digging through the entire code base