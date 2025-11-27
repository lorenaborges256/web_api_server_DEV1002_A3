from main import db
from flask import Blueprint
from models.products import Product
from models.suppliers import Supplier
from models.categories import Category
from models.product_supplier import Product_Supplier

db_commands = Blueprint("db", __name__)

# create app's cli command named create, then run it in the terminal as "flask db create", 
# it will invoke create_db function
@db_commands .cli.command("create")
def create_db():
    db.create_all()
    print("Tables created")

@db_commands .cli.command("seed")
def seed_db():
    #Category object/table
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
    
    #Product object/table
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

    # Supplier object/table
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
    # product_supplier junction table
    product_supplier1 = Product_Supplier(
        product=product1,
        supplier=supplier2,
        supply_price=5.00,
        last_supplied_date="2024-01-15"
    )
    db.session.add(product_supplier1)

    product_supplier2 = Product_Supplier(
        product=product2,
        supplier=supplier1,
        supply_price=2.00,
        last_supplied_date="2024-01-20"
    )
    db.session.add(product_supplier2)

    # commit ALL changes
    db.session.commit()
    print("Table seeded")

@db_commands .cli.command("drop")
def drop_db():
    # Drop junction table first
    Product_Supplier.__table__.drop(db.engine)
    Supplier.__table__.drop(db.engine)
    Product.__table__.drop(db.engine)
    Category.__table__.drop(db.engine)
    print("Tables dropped")
