from marshmallow import fields
from main import ma

# create the product_supplier Schema with Marshmallow, it will provide the serialization needed for converting the data into JSON
class ProductSupplierSchema(ma.Schema):
    ordered = True    
    product =  fields.Nested("ProductSchema", only=["name"])
    supplier =  fields.Nested("SupplierSchema", only=["name"])
    product_id = fields.Int()
    supplier_id = fields.Int()
    supply_price = fields.Decimal(as_string=True, places=2)
    last_supplied_date = fields.DateTime()

    class Meta:
        # Fields to expose
        fields = ("product_id", "product", "supplier_id", "supplier", "supply_price", "last_supplied_date")

# single product and supplier schema
product_supplier_schema = ProductSupplierSchema()
# multiple products and suppliers schema
products_suppliers_schema = ProductSupplierSchema(many=True)