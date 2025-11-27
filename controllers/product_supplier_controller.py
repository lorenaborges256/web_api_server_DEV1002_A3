from flask import Blueprint, jsonify, request
from main import db
from models.product_supplier import Product_Supplier
from models.products import Product
from models.suppliers import Supplier
from schemas.product_supplier_schema import products_suppliers_schema, product_supplier_schema


products_suppliers = Blueprint('product_supplier', __name__, url_prefix="/product_supplier")

# GET products_suppliers list
@products_suppliers.route("/", methods=["GET"])
def get_product_supplier():
    # get all the products_suppliers from the database table
    stmt = db.select(Product_Supplier)
    products_suppliers_list = db.session.scalars(stmt)
    # Convert the sproducts_suppliers from the database into a JSON format and store them in result
    result = products_suppliers_schema.dump(products_suppliers_list)
    # return the data in JSON format
    return jsonify(result)

# GET suppliers for a given product_id
@products_suppliers.route("/<int:product_id>", methods=["GET"])
def get_suppliers_by_product(product_id):
    # Query all product-supplier links for this product_id
    stmt = db.select(Product_Supplier).where(Product_Supplier.product_id == product_id)
    products_suppliers = db.session.scalars(stmt).all()

    if not products_suppliers:
        return jsonify({"error": "No suppliers found for this product"}), 404

    # Serialize the results
    result = products_suppliers_schema.dump(products_suppliers)
    return jsonify(result), 200

# GET products for a given supplier_id
@products_suppliers.route("/supplier/<int:supplier_id>", methods=["GET"])
def get_products_by_supplier(supplier_id):
    # Query all product-supplier links for this supplier_id
    stmt = db.select(Product_Supplier).where(Product_Supplier.supplier_id == supplier_id)
    suppliers_products = db.session.scalars(stmt).all()

    if not suppliers_products:
        return jsonify({"error": "No Products found for this Supplier"}), 404

    # Serialize the results
    result = products_suppliers_schema.dump(suppliers_products)
    return jsonify(result), 200


# POST create a new product-supplier link
@products_suppliers.route("/", methods=["POST"])
def create_product_supplier():
    data = request.json

    # Validate required fields
    required_fields = ["product_id", "supplier_id", "supply_price", "last_supplied_date"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    # Check if product exists
    product = Product.query.get(data["product_id"])
    if not product:
        return jsonify({"error": "Product not found"}), 404

    # Check if supplier exists
    supplier = Supplier.query.get(data["supplier_id"])
    if not supplier:
        return jsonify({"error": "Supplier not found"}), 404

    # Check if link already exists
    existing_link = Product_Supplier.query.get((data["product_id"], data["supplier_id"]))
    if existing_link:
        return jsonify({"error": "This product-supplier link already exists"}), 400

    # Create new record
    new_link = Product_Supplier(
        product_id=data["product_id"],
        supplier_id=data["supplier_id"],
        supply_price=data["supply_price"],
        last_supplied_date=data["last_supplied_date"]
    )

    db.session.add(new_link)
    db.session.commit()

    return jsonify(product_supplier_schema.dump(new_link)), 201


# PUT update last_supplied_date for a product-supplier link
@products_suppliers.route("/<int:product_id>/<int:supplier_id>", methods=["PUT"])
def update_last_supplied_date(product_id, supplier_id):
    # Find the product-supplier record by composite key
    record = Product_Supplier.query.get((product_id, supplier_id))
    if not record:
        return jsonify({"error": "Product-Supplier link not found"}), 404

    # Get new date from request body
    data = request.json
   # Update supply_price if provided
    if "supply_price" in data:
        record.supply_price = data["supply_price"]

    # Update last_supplied_date if provided
    if "last_supplied_date" in data:
        record.last_supplied_date = data["last_supplied_date"]

    # If neither field is provided, return error
    if "supply_price" not in data and "last_supplied_date" not in data:
        return jsonify({"error": "No updatable fields provided"}), 400

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

    return jsonify(product_supplier_schema.dump(record)), 200

