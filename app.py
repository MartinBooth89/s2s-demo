from flask import Flask, request, g
from db import get_db
import json

app = Flask(__name__)

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.get('/products')
def get_products():
  return get_db().execute('SELECT * FROM products').fetchall(), 200

@app.post('/products')
def create_or_update_product():
  try:
    product = request.get_json()

    db_product = { 'sku': product['sku'], 'attributes': json.dumps(product['attributes'])}
    db = get_db()

    db.execute('INSERT INTO products (sku, attributes) VALUES (?, ?) ON CONFLICT(sku) DO UPDATE SET attributes = ?', (db_product['sku'], db_product['attributes'], db_product['attributes']))

    result = db.execute('SELECT id, sku, attributes FROM products WHERE sku LIKE ?', (db_product['sku'],)).fetchone()
    db.commit()
    
    return result, 200
  except Exception as error:
    print(error)
     
  return {}, 500