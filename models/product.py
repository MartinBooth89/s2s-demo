from db import db

class ProductModel(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String, unique=True, nullable=False)
    attributes = db.Column(db.String, unique=False, nullable=False)
