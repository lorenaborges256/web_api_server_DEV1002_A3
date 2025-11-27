from main import db

class Product_Supplier(db.Model):
    # define the table name for the db
    __tablename__= "product_suppliers"
    # Set the primary key, we need to define that each attribute is also a column in the db table, remember "db" is the object we created in the previous step.
    product_id = db.Column(db.Integer, db.ForeignKey("products.product_id"), primary_key=True, nullable=False)
    supplier_id = db.Column(db.Integer, db.ForeignKey("suppliers.supplier_id"), primary_key=True, nullable=False)
    # Add the rest of the attributes. 
    supply_price = db.Column(db.Numeric(10, 2))
    last_supplied_date = db.Column(db.DateTime())
    product = db.relationship(
        "Product",
        back_populates="product_suppliers",
    )
    supplier = db.relationship(
        "Supplier",
        back_populates="product_suppliers",
    )