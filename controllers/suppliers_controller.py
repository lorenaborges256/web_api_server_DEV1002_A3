from flask import Blueprint, jsonify, request, abort
from main import db
from models.suppliers import Supplier
from schemas.suppliers_schema import supplier_schema, suppliers_schema

suppliers = Blueprint('participants', __name__, url_prefix="/suppliers")

# GET suppliers list
@suppliers.route("/", methods=["GET"])
def get_suppliers():
    # get all the suppliers from the database table
    stmt = db.select(Supplier)
    suppliers_list = db.session.scalars(stmt)
    # Convert the suppliers from the database into a JSON format and store them in result
    result = suppliers_schema.dump(suppliers_list)
    # return the data in JSON format
    return jsonify(result)

# GET one supplier by supplier_id
@suppliers.route("/<int:supplier_id>/", methods=["GET"])
def get_supplier(supplier_id):
    stmt = db.select(Supplier).filter_by(supplier_id=supplier_id)
    supplier = db.session.scalar(stmt)
    #return an error if the supplier doesn't exist
    if not supplier:
        return abort(400, description= "supplier does not exist")
    # Convert the supplier from the database into a JSON format and store them in result
    result = supplier_schema.dump(supplier)
    # return the data in JSON format
    return jsonify(result)

# POST new supplier
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


# DELETE supplier by supplier_id
@suppliers.route("/<int:supplier_id>/", methods=["DELETE"])
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

# PUT update supplier by supplier_id
@suppliers.route("/<int:supplier_id>/", methods=["PUT"])
def update_supplier(supplier_id):
    # Create a new supplier
    supplier_fields = supplier_schema.load(request.json)

    # find the supplier
    stmt = db.select(Supplier).filter_by(supplier_id=supplier_id)
    supplier = db.session.scalar(stmt)

    # return an error if the supplier doesn't exist
    if not supplier:
        return abort(400, description= "Supplier does not exist")
    # update the supplier details with the given values
    supplier.name = supplier_fields["name"]
    supplier.contact_email = supplier_fields["contact_email"]
    supplier.phone_number = supplier_fields["phone_number"]
    # add to the database and commit
    db.session.commit()
    #return the supplier in the response
    return jsonify(supplier_schema.dump(supplier))