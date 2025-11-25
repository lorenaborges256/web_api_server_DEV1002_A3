from main import ma

# create the Suppliers Schema with Marshmallow, it will provide the serialization needed for converting the data into JSON
class SupplierSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("supplier_id", "name", "contact_email", "phone_number")

# single competition schema, when one competition needs to be retrieved
supplier_schema = SupplierSchema()
# multiple competition schema, when many competitions need to be retrieved
suppliers_schema = SupplierSchema(many=True)