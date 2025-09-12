from flask_restx import inputs
from src.ext import api
from flask_restx import reqparse, fields

person_ns = api.namespace("person", description="უზერები")

del_parser = reqparse.RequestParser()
del_parser.add_argument("id", type=int, required=True)

post_parser = reqparse.RequestParser()
post_parser.add_argument("name", type=str, required=True, location="json")
post_parser.add_argument("surname", type=str, required=True, location="json")
post_parser.add_argument("birthday", type=inputs.date_from_iso8601, required=True, location="json")

person_model = api.model("Person", {
    "id": fields.Integer,
    "name": fields.String,
    "surname": fields.String,
    "birthday": fields.DateTime
})