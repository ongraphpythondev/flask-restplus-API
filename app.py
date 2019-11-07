# Flask Import
from flask import Blueprint
from flask_restplus import Api
# Project Import
from resources.Blog import BlogResources, BlogResource

# App Initialization
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Routes
api.add_resource(BlogResources, '/blog/', methods=['GET', 'POST'])
api.add_resource(BlogResource, '/blog/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
