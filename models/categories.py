from main import db

class Category(db.Model):
    # define the table name for the db
    __tablename__= "categories"
    # Set the primary key, we need to define that each attribute is also a column in the db table, remember "db" is the object we created in the previous step.
    category_id = db.Column(db.Integer,primary_key=True)
    # Add the rest of the attributes. 
    name = db.Column(db.String(), unique=True, nullable=False)
    description = db.Column(db.String())
    products = db.relationship(
        "Product",
        back_populates="category",
        cascade="all, delete"
    )