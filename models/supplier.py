from main import db

class Supplier(db.Model):
    __tablename__ = "suppliers"

    supplier_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    contact_email = db.Column(db.String(), nullable=False)
    phone_number = db.Column(db.String(), nullable=False)