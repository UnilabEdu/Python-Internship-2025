from flask_restx import Resource
from flask_jwt_extended import create_access_token, create_refresh_token

from src.ext import api
from src.models import User
from src.endpoints.auth import auth_ns, login_parser

@auth_ns.route("/login")
class LoginApi(Resource):

    @auth_ns.doc(parser=login_parser)
    def post(self):
        args = login_parser.parse_args()
        user = User.query.filter_by(username=args["username"]).first()
        if not user:
            return "მომხმარებელი ვერ მოიძებნა", 404

        if user.check_password(args["password"]):
            access_token = create_access_token(identity=user)
            refresh_token = create_refresh_token(identity=user)

            response = {
                "access_token": access_token,
                "refresh_token": refresh_token
            }
            return response
        else:
            return "მონაცემები არ არის სწორი", 400