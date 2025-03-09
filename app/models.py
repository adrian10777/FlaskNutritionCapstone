# import sqlalchemy to create our instance of our ORM (translator between python and SQL)
from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4
from secrets import token_hex

# create the instance of SQLAlchemy obj
db = SQLAlchemy() #<- mediator btwn models(user bluepint/user obj) and backbone of our app init.py


class Program(db.Model):
    id = db.Column(db.String, primary_key=True)
    program_name = db.Column(db.String(150), nullable=False)
    program_cost = db.Column(db.String(150), nullable=False, default='$0')
    apitoken = db.Column(db.String(32), nullable=True, default=None)
    
    def __init__(self, program_name='', program_cost=''):
        self.program_name = program_name
        self.program_cost = program_cost
        self.id = str(uuid4()) # generate id in some manner 
        self.apitoken = token_hex(32)

    def to_dict(self):
        return {'id': self.id,
                'program_name': self.program_name,
                'program_cost': self.program_cost
    }

    def from_dict(self, dict):
        self.program_cost = dict['program_cost']
        if dict.get['program_name']:
            self.program_name = dict['program_name']
        else:
            self.program_name = ''

        # id which only should be made for creation not updating
        if not self.id:
            self.id = str(uuid4())
        
        #originally optional values if doing these go to week 6 day 4