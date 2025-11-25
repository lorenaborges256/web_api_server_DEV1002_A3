from flask import Blueprint, jsonify, request, abort
from main import db
from models.products import Product
from schemas.products_schema import product_schema, products_schema

products = Blueprint('products', __name__, url_prefix="/products")

# The GET routes endpoint
@products.route("/", methods=["GET"])
def get_products():
    # get all the products from the database table
    stmt = db.select(Product)
    products_list = db.session.scalars(stmt)
    # Convert the products from the database into a JSON format and store them in result
    result = products_schema.dump(products_list)
    # return the data in JSON format
    return jsonify(result)

# The POST route endpoint
@products.route("/", methods=["POST"])
def create_product():
    # Create a new product
    product_fields = product_schema.load(request.json)
    new_product = Product()
    new_product.name = product_fields["name"]
    new_product.description = product_fields["description"]
    new_product.quantity = product_fields["quantity"]
    new_product.unit_price = product_fields["unit_price"]
    # add to the database and commit
    db.session.add(new_product)
    db.session.commit()
    # return the competition in the response
    return jsonify(product_schema.dump(new_product))


# The DELETE route endpoint
@products.route("/<int:id>/", methods=["DELETE"])
def delete_product(product_id):
    # find the product
    stmt = db.select(Product).filter_by(product_id=product_id)
    product = db.session.scalar(stmt)
    # return an error if the product doesn't exist
    if not product:
        return abort(400, description= "Product doesn't exist")
    # Delete the product from the database and commit
    db.session.delete(product)
    db.session.commit()
    # return the product in the response
    return jsonify(product_schema.dump(product))