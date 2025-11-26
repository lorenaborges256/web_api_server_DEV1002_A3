from flask import Blueprint, jsonify, request
from main import db
from models.categories import Category
from schemas.categories_schema import category_schema, categories_schema

categories = Blueprint('categories', __name__, url_prefix="/categories")

# GET categories list
@categories.route("/", methods=["GET"])
def get_categories():
    # get all the categories from the database table
    stmt = db.select(Category)
    categories_list = db.session.scalars(stmt)
    # Convert the categories from the database into a JSON format and store them in result
    result = categories_schema.dump(categories_list)
    # return the data in JSON format
    return jsonify(result)

# GET one category by category_id
@categories.route("/<int:category_id>/", methods=["GET"])
def get_category(category_id):
    stmt = db.select(Category).filter_by(category_id=category_id)
    category = db.session.scalar(stmt)
    #return an error if the category doesn't exist
    if not category:
        return jsonify({"error": "Category does not exist"}), 400
    # Convert the category from the database into a JSON format and store them in result
    result = category_schema.dump(category)
    # return the data in JSON format
    return jsonify(result)

# POST new category
@categories.route("/", methods=["POST"])
def create_category():
    # Create a new category
    category_fields = category_schema.load(request.json)
    new_category = Category()
    new_category.name = category_fields["name"]
    new_category.description = category_fields["description"]
    # add to the database and commit
    db.session.add(new_category)
    db.session.commit()
    # return the category in the response
    return jsonify(category_schema.dump(new_category))

# DELETE category by category_id
@categories.route("/<int:category_id>/", methods=["DELETE"])
def delete_category(category_id):
    # find the category
    stmt = db.select(Category).filter_by(category_id=category_id)
    category = db.session.scalar(stmt)
    # return an error if the category doesn't exist
    if not category:
        return jsonify({"error": "Category does not exist"}), 400
    # Delete the Category from the database and commit
    db.session.delete(category)
    db.session.commit()
    # return the Category in the response
    return jsonify(category_schema.dump(category))

# PUT update category by category_id
@categories.route("/<int:category_id>/", methods=["PUT"])
def update_category(category_id):
    # find the category
    stmt = db.select(Category).filter_by(category_id=category_id)
    category = db.session.scalar(stmt)

    # return an error if the category doesn't exist
    if not category:
        return jsonify({"error": "Category does not exist"}), 400
    # Load the category details from the request
    category_fields = category_schema.load(request.json)
    # update the category details with the given values
    category.name = category_fields["name"]
    category.description = category_fields["description"]
    # commit the changes to the database
    db.session.commit()
    # return the updated category in the response
    return jsonify(category_schema.dump(category))