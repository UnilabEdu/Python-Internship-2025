from src.ext import api
from flask_restx import reqparse, fields

product_ns = api.namespace("product", description="პროდუქტები")

del_parser = reqparse.RequestParser()
del_parser.add_argument("id", type=int, required=True)

post_parser = reqparse.RequestParser()
post_parser.add_argument("name", type=str, required=True, location="json")
post_parser.add_argument("author", type=str, required=True, location="json")
post_parser.add_argument("price", type=float, required=True, location="json")

product_model = api.model("Product", {
    "id": fields.Integer,
    "name": fields.String,
    "author": fields.String,
    "price": fields.Float,
    "image": fields.String
})