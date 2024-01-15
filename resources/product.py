from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
import json
from db import db
from models import ProductModel
from schemas import GetProductSchema, ProductSchema

blueprint = Blueprint("product", __name__, description="Product operations")

def map_db_product_to_api(product):
  return { "id": product.id, "sku": product.sku, "attributes": json.loads(product.attributes) }

@blueprint.route("/products")
class Product(MethodView):
  @blueprint.response(200, GetProductSchema(many=True))
  def get(self):
    return map(map_db_product_to_api, ProductModel.query.all())

  @blueprint.response(201, GetProductSchema)
  @blueprint.arguments(ProductSchema)
  def post(self, product_data):
    # find existing product, if any
    product = ProductModel.query.filter(ProductModel.sku == product_data["sku"]).first()

    # stringify attributes field
    attributes = json.dumps({} if 'attributes' not in product_data else product_data['attributes'])
  
    if product:
      # update if existing
      product.attributes = attributes
    else:
      # create if new
      product = ProductModel(sku=product_data["sku"], attributes=attributes)

    try:
      db.session.add(product)
      db.session.commit()
    except SQLAlchemyError as e:
      abort(500, message=f"Error adding/updating product.")

    return map_db_product_to_api(product)