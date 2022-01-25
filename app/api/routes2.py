from flask import Blueprint, jsonify, request
from app.models import Program, db
from .apihelpers import token_required

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/')
def test():
    return{'datadatadata': 'ooh look at this fancy data'}

@api.route('/programs', methods=['GET'])
def programs():
    """
    [GET] route returns json data on all players in our db
    """
    
    return jsonify([program.to_dict() for program in Program.query.all()])

@api.route('/program/<int:program_cost>', methods=['GET'])
def get_cost(cost):
    """
    [GET] /api/program/<int:program_cost>
    returns all programs with that program_cost
    or none if no programs have that program_cost
    """
    programs = Program.query.filter_by(program_cost=cost).all()
    if not programs:
        return jsonify({cost: None})
    return jsonify([x.to_dict() for x in programs])

@api.route('/<string:name>', methods=['GET'])
def get_name(name):
    """
    [GET /api/name]
    returns all programs on the applicable name
    """
    name = name.replace('_',' ').title()
    programs = Program.query.filter_by(first_name=name).all()
    if not programs:
        return jsonify({name: None})
    return jsonify([x.to_dict() for x in programs])

@api.route('/createprogram', methods=['POST'])
@token_required
def createprogram():
    """
    [POST] /api/createprogram
    accepts JSON date for the creation of program in the following format:
    {
        'program_name': <str>,
        'program_cost': <str> optional default '$0m'
    }
    checks if program of the same program_name and program_Cost exists in db
    Create the player in our database with a UUID
    Return a dict representation of that program in our db
    """
    data = request.get_json() # grabs json data sent in the API POST request
    print(data)

    '''
    # fill program name if not present
    if not data.get('program_name'):
        data['program_name'] = ''

    #check if program of same cost and name exists already
        checks = Program.query.filter_by(program_name=data['program_name']).all()
        if checks:
            for p in checks:
                if p.program_name == data['program_name'] and p.program_cost == data['program_cost']:
                    return jsonify({'Create Program rejected': 'Program already exists'})
    #if not - create program objext and save to db
    newprogram = Program()
    newprogram.from_dict(data)
    db.session.add(newprogram)
    db.session.commit()
    return jsonify({'created': newprogram.to_dict()})

    #update route  - allows u to update players info
    @api.route('/update/<string:id>', methods=['PUT']) #PUT used for updating existing players - just like POST put can accept input
    @token_required
    def updateprogram(id):
    """
    [PUT] /api/update/<str:id>
    Accept a dict of all program attributes u wish to change - all K/V pairs are optional
    This route will work for changing every or just 1 piece of a player's information
    day 4 5:00
    """
    data = request.get_json() # grabs json data sent in the API POST request
    print(data)

    # when it comes to updating player info we already made method to do this, we prob just have to change it a bit
    # get player obj for this player id
    program = Program.query.get(id)
    if not program:
        return jsonify('update failed': 'No program with that ID')
    program.from_dict(data)
    print(program.to_dict())
    db.session.commit()
    return jsonify({'updated': program.to_dict()})

    #delete route - allows u to delete program info
    @api.route('/delete/<string:id>', methods=['DELETE'])
    @token_required
    def deleteprogram(id):
        # check if program of that id exists in db
        p = Program.query.get(id)
        if not p: #  if they do delete if they dont, tell the user
            return jsonify({'Delete failed':'No player of that Id exists in the database'})
        # implied else that program does exist, no need to put is if, if statement is true it returns(ends function) function so it never hits the code
        db.session.delete(p)
        db.session.commit()
        return jsonify({'Deleted':p.to_dict()})


'''


  