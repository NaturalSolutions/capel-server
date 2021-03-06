from flask import Blueprint, jsonify

from model import TypeDive
from . import users
from api import divesites, dives, permits, users, boats, offenses

api = Blueprint('api', __name__)

def init_app(app):
    app.register_blueprint(users.users)
    app.register_blueprint(divesites.divesites)
    app.register_blueprint(permits.permits)
    app.register_blueprint(boats.boats)
    app.register_blueprint(offenses.offenses)
    permits.init_app(app)
    app.register_blueprint(dives.dives)


@api.route('/api/dives/typedives')
def getTypeDives():
    typeDives = TypeDive.query.all()
    typeDivesJsn = []
    for typeDive in typeDives:
        typeDivesJsn.append(typeDive.json())
    return jsonify(typeDivesJsn)


