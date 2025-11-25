from flask import Blueprint, jsonify, request, abort
from main import db
from models.suppliers import Supplier
from schemas.suppliers_schema import supplier_schema, suppliers_schema

suppliers = Blueprint('participants', __name__, url_prefix="/suppliers")

# The GET routes endpoint
@suppliers.route("/", methods=["GET"])
def get_suppliers():
    # get all the suppliers from the database table
    stmt = db.select(Supplier)
    suppliers_list = db.session.scalars(stmt)
    # Convert the suppliers from the database into a JSON format and store them in result
    result = suppliers_schema.dump(suppliers_list)
    # return the data in JSON format
    return jsonify(result)

# The POST route endpoint
@suppliers.route("/", methods=["POST"])
def create_supplier():
    # Create a new supplier
    supplier_fields = supplier_schema.load(request.json)
    new_supplier = Supplier()
    new_supplier.name = supplier_fields["name"]
    new_supplier.contact_email = supplier_fields["contact_email"]
    new_supplier.phone_number = supplier_fields["phone_number"]
    # add to the database and commit
    db.session.add(new_supplier)
    db.session.commit()
    # return the supplier in the response
    return jsonify(supplier_schema.dump(new_supplier))


# The DELETE route endpoint
@suppliers.route("/<int:id>/", methods=["DELETE"])
def delete_supplier(supplier_id):
    # find the supplier
    stmt = db.select(Supplier).filter_by(supplier_id=supplier_id)
    supplier = db.session.scalar(stmt)
    # return an error if the supplier doesn't exist
    if not supplier:
        return abort(400, description= "Supplier doesn't exist")
    # Delete the Supplier from the database and commit
    db.session.delete(supplier)
    db.session.commit()
    # return the Supplier in the response
    return jsonify(supplier_schema.dump(supplier))