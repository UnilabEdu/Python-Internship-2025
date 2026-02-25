from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask_restx import Resource

from src import User
from src.endpoints.auth import auth_ns, refresh_parser

@auth_ns.route("/refresh_token")
class AccessTokenRefreshApi(Resource):

    @auth_ns.doc(parser=refresh_parser)
    @jwt_required(refresh=True, locations=["query_string"])
    def post(self):
        client = get_jwt_identity()
        user = User.query.filter_by(username=client).first()

        access_token = create_access_token(identity=user)
        response = {
            "access_token": access_token
        }
        return response