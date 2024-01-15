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

5. You can now navigate to the Swagger UI page to get more information on the available API endpoints at http://127.0.0.1:5000/swagger-ui

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
