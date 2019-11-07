# Flask Restful API using flask-restplus with flask-marshmallow and flask-sqlalchemy(Create, Read, Update, Delete)

A flask APIs demo project to CRUD operations using flask-marshmallow to serialization/deserialization, flask-restplus to better API response and flask-SQLAlchemy to database operations.
Flask-Restplus provide better APIs response with swagger documentation.

## Prerequisites:

You will need the following programmes properly installed on your computer.

* [Python](https://www.python.org/) 3.7+

* Virtual Environment

To install virtual environment on your system use:

apt-get install python3-venv

## Installation and Running :

```bash
git clone https://github.com/ongraphpythondev/flask-restplus-API.git

cd flask-restplus-API

python3 -m venv venv

source venv/bin/activate

# install required packages for the project to run
pip install -r requirements.txt

python migrate db upgrade
python run.py
```


