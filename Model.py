# Flask Import
from marshmallow import fields, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()  # Object to serialization/deserialization
db = SQLAlchemy()  # Object to database


class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), unique=True, nullable=False)
    content = db.Column(db.String(1500), unique=False, nullable=True)

    def __init__(self, title):
        self.title = title


# Serialization/Deserialization
class BlogSchema(ma.ModelSchema):
    class Meta:
        model = Blog

