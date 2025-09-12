from flask_restx import Resource

from src.endpoints.product import product_ns, product_model, post_parser, del_parser
from src.models import Product

@product_ns.route("/")
class ProductApi(Resource):

    @product_ns.marshal_with(product_model)
    def get(self):
        products = Product.query.all()
        return products

    @product_ns.doc(parser=post_parser)
    def post(self):
        args = post_parser.parse_args()
        product = Product(name=args["name"], author=args["author"], price=args["price"])
        product.create()
        return product.id, 200

    @product_ns.doc(parser=del_parser)
    def delete(self):
        args = del_parser.parse_args()

        product = Product.query.get(args["id"])
        if not product:
            return "Not Found", 404
        
        product.delete()
        product.save()
        return "Success", 200