from flask import Blueprint, jsonify, request
from main import db
from models.products import Product
from models.categories import Category
from schemas.products_schema import product_schema, products_schema

products = Blueprint('products', __name__, url_prefix="/products")

# GET products list
@products.route("/", methods=["GET"])
def get_products():
    # get all the products from the database table
    stmt = db.select(Product)
    products_list = db.session.scalars(stmt)
    # Convert the products from the database into a JSON format and store them in result
    result = products_schema.dump(products_list)
    # return the data in JSON format
    return jsonify(result)

# GET one product by product_id
@products.route("/<int:product_id>/", methods=["GET"])
def get_product(product_id):
    stmt = db.select(Product).filter_by(product_id=product_id)
    product = db.session.scalar(stmt)
    #return an error if the product doesn't exist
    if not product:
        return jsonify({"error": "Product does not exist"}), 400
    # Convert the product from the database into a JSON format and store them in result
    result = product_schema.dump(product)
    # return the data in JSON format
    return jsonify(result)


# POST new product
@products.route("/", methods=["POST"])
def create_product():
    # Create a new product
    product_fields = product_schema.load(request.json)

    # Check if category exists
    category = Category.query.get(product_fields["category_id"])
    if not category:
        return jsonify({"error": "Category ID does not exist"}), 400

    new_product = Product()
    new_product.name = product_fields["name"]
    new_product.description = product_fields["description"]
    new_product.quantity = product_fields["quantity"]
    new_product.unit_price = product_fields["unit_price"]
    new_product.category_id = product_fields["category_id"]
    # add to the database and commit
    db.session.add(new_product)
    db.session.commit()
    # return the competition in the response
    return jsonify(product_schema.dump(new_product))


# DELETE product by product_id
@products.route("/<int:product_id>/", methods=["DELETE"])
def delete_product(product_id):
    # find the product
    stmt = db.select(Product).filter_by(product_id=product_id)
    product = db.session.scalar(stmt)
    # return an error if the product doesn't exist
    if not product:
        return jsonify({"error": "Product does not exist"}), 400
    
    # Delete the product from the database and commit
    db.session.delete(product)
    db.session.commit()
    # return the product in the response
    return jsonify(product_schema.dump(product))

# PUT update product by product_id
@products.route("/<int:product_id>/", methods=["PUT"])
def update_product(product_id):
    # Create a new product
    product_fields = product_schema.load(request.json)

    # find the product
    stmt = db.select(Product).filter_by(product_id=product_id)
    product = db.session.scalar(stmt)

    # return an error if the product doesn't exist
    if not product:
        return jsonify({"error": "Product does not exist"}), 400
    
    # update the product details with the given values
    product.name = product_fields["name"]
    product.description = product_fields["description"]
    product.quantity = product_fields["quantity"]
    product.unit_prie = product_fields["unit_price"]
    product.category_id = product_fields["category_id"]
    # add to the database and commit
    db.session.commit()
    #return the product in the response
    return jsonify(product_schema.dump(product))