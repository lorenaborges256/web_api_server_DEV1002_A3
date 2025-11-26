from main import db
from flask import Blueprint
from models.products import Product
from models.suppliers import Supplier
from models.categories import Category

db_commands = Blueprint("db", __name__)

# create app's cli command named create, then run it in the terminal as "flask db create", 
# it will invoke create_db function
@db_commands .cli.command("create")
def create_db():
    db.create_all()
    print("Tables created")

@db_commands .cli.command("seed")
def seed_db():
        #create the Category object
    category1 = Category(
        name="shampoo",
        description="product to clean hair"
    )
    db.session.add(category1)

    category2 = Category(
        name="conditioner",
        description="product to soften hair"
    )
    db.session.add(category2)
        # commit the changes
    db.session.commit()
    
    # create the Product object
    product1 = Product(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        name="Aloe Vera Super Shampoo",
        description="Shampoo made from organic Aloe Vera for healthy hair",
        quantity=10,
        unit_price=3,
        category_id=category1.category_id
    )
    # Add the object as a new row to the table
    db.session.add(product1)

    product2 = Product(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        name="Aloe Vera Super Conditioner",
        description="Conditioner made from organic Aloe Vera for healthy hair",
        quantity= 8,
        unit_price=2.5,
        category_id=category2.category_id
    )
    # Add the object as a new row to the table
    db.session.add(product2)

    # create the Supplier object
    supplier1 = Supplier(
        name="Supplier 1",
        contact_email="email1@email.com",
        phone_number="0412345678"
    )
    db.session.add(supplier1)

    supplier2 = Supplier(
        name="Supplier 2",
        contact_email="email2@email.com",
        phone_number="0412345678"
    )
    db.session.add(supplier2)



    # commit the changes
    db.session.commit()
    print("Table seeded")

@db_commands .cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables dropped")