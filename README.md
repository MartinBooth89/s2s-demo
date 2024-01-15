# s2s-demo

A simple store REST API written in Flask.

## Local setup

Prerequisites: Python3

To set up and run the API locally:

1. Clone the repo to your local machine:

```
git clone https://github.com/MartinBooth89/s2s-demo.git
```

2. `cd` into the s2s-demo directory and run the following to create and source a virtual Python environment:

```
python -m venv .venv
source .venv/bin/activate
```

3. Install project dependencies by running:

```
pip install -r requirements.txt
```

4. Finally, run the API:

```
flask run
```

You should now see output similar to the following:

```
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

5. You can now navigate to the Swagger UI page to get more information on the available API endpoints locally at http://127.0.0.1:5000/swagger-ui

## Endpoints

### GET /products

Try this out using Curl:

```
curl -X GET  http://127.0.0.1:5000/products
```

Output:

```
[
  {
    "attributes": {
      "price": 12.34
    },
    "id": 1,
    "sku": "SKU1432348"
  },
  ...
]
```

### POST /products

Try this out using Curl:

```
curl -X POST  http://127.0.0.1:5000/products -H "Content-Type: application/json" -d '{"sku": "SKU0001", "attributes": {"price": 12.34}}'
```

Output:

```
{
  "attributes": {
    "price": 12.34
  },
  "id": 4,
  "sku": "SKU0001"
}
```

## 3rd party packages

The following 3rd party packages are used by this REST API:

- [Flask](https://flask.palletsprojects.com/en/3.0.x/) - Python REST API framework that simplifies developing route based REST APIs.
- [Flask-Smorest & Marshmallow](https://flask-smorest.readthedocs.io/en/latest/) - Adds Marshmallow features on top of Flask to allow defining how API requests and responses are processed and validated in a declarative manner. It also supports generating a Swagger API spec from available API endpoints and model declarations, which can be viewed using Swagger UI. This allows the code to be self documenting, making the API easier to understand and use without duplicating effort.
- [Sqlite](https://docs.python.org/3/library/sqlite3.html) - Lightweight file-based database. This is especially suitable for this API since there is currently only a single table with a very basic structure. Sqlite doesn't enforce referential integrity, which only becomes a concern when the database has multiple interrelated tables. If more tables are introduced in the future, it may become necessary to migrate to a DBMS like MySQL or PostgreSQL.
- [Flask-SqlAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/) - Flask extension that adds SqlAlchemy ORM (Object Relational Model) functionality that simplifies interaction between the Flask app and databases. SqlAlchemy abstracts the database details away from the Flask app, allowing the code to connect to different types of databases using a shared interface. This can help simplify the process of migrating to a different DBMS down the line. It also allows the Flask app to query and write to the database using Python statements and objects. This avoids having to include raw SQL in your code, making the code easier to test, debug and maintain. This also helps prevent security risks such as SQL injection since queries are always parameterised.

## Considerations

This is a very simple REST API. Yet, there are some things to consider regarding performance and scaling:

- Since the 'attributes' field can contain any type of object with potentially multiple levels, it makes sense to store it as a JSON string in the database. This allows the database to store semi-structured data.
- Instead of having separate insert and update endpoints, a shared upsert endpoint is used to ensure these operations are idempotent. This means that a request can be made multiple times with the same outcome each time. This promotes higher data throughput as clients do not need to check if a product exists before deciding whether to make an insert or update request. It also helps prevent the API / clients from having to handle potential duplication errors.
- The API currently only has a single resource type, products. However, to make way for potential future expansion, it helps having already maintaining separate database models, API schemas and resources for each resource type.
- Since the data model is currently very simple, Sqlite makes for a suitable choice of database. However, if the data model is to expand and become more complex, it could be worth considering the user of more sophisticated DBMSs with potentially better performance, security and control.
- Adding/updating products is an atomic operation. This helps prevent different requests from interfering with each other. It also means that if an error occurs during an add/update operation, the operation is rolled back completely, instead leaving the data in an inconsistent state.

## References

This project is part of my journey learning to write REST APIs using Python and Flask. As such, the code is heavily influenced by the code in this [course](https://github.com/tecladocode/rest-apis-flask-python/tree/master) by Jose Salvatierra.
