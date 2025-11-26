from main import ma
from marshmallow import fields

# create the Product Schema with Marshmallow, it will provide the serialization needed for converting the data into JSON
class ProductSchema(ma.Schema):
    # Fields to expose
    product_id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    quantity = fields.Int()
    unit_price = fields.Decimal(as_string=True, places=2)
    category_id = fields.Int()

    class Meta:
        # Fields to expose
        fields = ("product_id", "name", "description", "quantity", "unit_price", "category_id")

# single Product schema, when one Product needs to be retrieved
product_schema = ProductSchema()
# multiple Product schema, when many Product need to be retrieved
products_schema = ProductSchema(many=True)