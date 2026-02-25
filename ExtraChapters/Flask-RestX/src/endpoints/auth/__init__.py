from src.ext import api

from flask_restx import reqparse

auth_ns = api.namespace("Auth", description="ავტორიზაცია")

login_parser = reqparse.RequestParser()
login_parser.add_argument("username", type=str, required=True)
login_parser.add_argument("password", type=str, required=True)

refresh_parser = reqparse.RequestParser()
refresh_parser.add_argument("jwt", location="args", required=True)