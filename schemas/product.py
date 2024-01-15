from marshmallow import Schema, fields

class ProductSchema(Schema):
  sku = fields.Str(required=True)
  attributes = fields.Raw()

class GetProductSchema(ProductSchema):
  id = fields.Integer(dump_only=True)