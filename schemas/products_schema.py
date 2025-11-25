from main import ma
from marshmallow import fields

# create the Product Schema with Marshmallow, it will provide the serialization needed for converting the data into JSON
class ProductSchema(ma.Schema):
    # Fields to expose
    product_id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    quantity = fields.Int()
    unit_price = fields.Int()
    class Meta:
        # Fields to expose
        fields = ("product_id", "name", "description", "quantity", "unit_price")

# single competition schema, when one competition needs to be retrieved
product_schema = ProductSchema()
# multiple competition schema, when many competitions need to be retrieved
products_schema = ProductSchema(many=True)