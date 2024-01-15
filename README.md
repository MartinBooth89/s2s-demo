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

4. Initialise Sqlite database by running:

```
python init_db.py
```

5. Finally, run the API:

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

## Endpoints

```
GET /products
```

```
POST /products
```
