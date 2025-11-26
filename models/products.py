from main import db
from sqlalchemy import Numeric


class Product(db.Model):
    # define the table name for the db
    __tablename__= "products"
    # Set the primary key, we need to define that each attribute is also a column in the db table, remember "db" is the object we created in the previous step.
    product_id = db.Column(db.Integer,primary_key=True)
    # Add the rest of the attributes. 
    name = db.Column(db.String())
    description = db.Column(db.String())
    quantity = db.Column(db.Integer())
    unit_price = db.Column(Numeric(10, 2))
    category_id = db.Column(db.Integer, db.ForeignKey("categories.category_id"), nullable=False)
    category = db.relationship(
        "Category", 
        back_populates="products"
    )