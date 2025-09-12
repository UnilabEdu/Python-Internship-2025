from flask_restx import Resource
from flask_jwt_extended import jwt_required

from src.endpoints.person import person_ns, person_model, post_parser, del_parser
from src.models import Person

@person_ns.route("/")
class PersonApi(Resource):

    @jwt_required()
    @person_ns.doc(security="JsonWebToken")
    @person_ns.marshal_with(person_model)
    def get(self):
        persons = Person.query.all()
        return persons

    @jwt_required()
    @person_ns.doc(security="JsonWebToken")
    @person_ns.doc(parser=post_parser)
    def post(self):
        args = post_parser.parse_args()
        person = Person(name=args["name"], surname=args["surname"], birthday=args["birthday"])
        person.create()
        return person.id, 200

    @person_ns.doc(parser=del_parser)
    def delete(self):
        args = del_parser.parse_args()

        person = Person.query.get(args["id"])
        person.delete()
        person.save()
        return "Success", 200