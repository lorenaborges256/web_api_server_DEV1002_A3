from main import ma
from marshmallow import fields

# create the Category Schema with Marshmallow, it will provide the serialization needed for converting the data into JSON
class CategorySchema(ma.Schema):
    # Fields to expose
    category_id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    products = fields.Nested("ProductSchema", many=True, only=["name", "unit_price"])
    class Meta:
        # Fields to expose
        fields = ("category_id", "name", "description", "products")

# single category schema, when one category needs to be retrieved
category_schema = CategorySchema()
# multiple category schema, when many categories need to be retrieved
categories_schema = CategorySchema(many=True)