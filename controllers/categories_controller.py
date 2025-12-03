from flask import Blueprint, jsonify, request
from main import db
from sqlalchemy.exc import IntegrityError
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
    category_fields = category_schema.load(request.json)
    
    # Pre-check for duplicate name
    existing = db.session.scalar(
        db.select(Category).filter_by(name=category_fields["name"])
    )
    if existing:
        return jsonify({"error": "Category name already exists"}), 400

    new_category = Category(
        name=category_fields["name"],
        description=category_fields["description"]
    )
    db.session.add(new_category)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Category name must be unique"}), 400
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

    # Pre-check for duplicate name (excluding the current category itself)
    existing = db.session.scalar(
        db.select(Category).filter_by(name=category_fields["name"])
    )
    if existing and existing.category_id != category_id:
        return jsonify({"error": "Category name already exists"}), 400

    # update the category details with the given values
    category.name = category_fields["name"]
    category.description = category_fields["description"]
    # commit the changes to the database
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Category name must be unique"}), 400

    # return the updated category in the response
    return jsonify(category_schema.dump(category))