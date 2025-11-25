from main import ma
from marshmallow import fields

# create the Suppliers Schema with Marshmallow, it will provide the serialization needed for converting the data into JSON
class SupplierSchema(ma.Schema):
    # Fields to expose
    supplier_id = fields.Int()
    name = fields.Str()
    contact_email = fields.Str()
    phone_number = fields.Str()
    class Meta:
        # Fields to expose
        fields = ("supplier_id", "name", "contact_email", "phone_number")

# single competition schema, when one competition needs to be retrieved
supplier_schema = SupplierSchema()
# multiple competition schema, when many competitions need to be retrieved
suppliers_schema = SupplierSchema(many=True)