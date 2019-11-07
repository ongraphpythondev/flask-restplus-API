from flask import request
from flask_restplus import Resource
from Model import db, Blog, BlogSchema

blogs_schemas = BlogSchema(many=True)
blogs_schema = BlogSchema()


class BlogResources(Resource):
    def get(self):
        blogs = Blog.query.all()
        blogs = blogs_schemas.dump(blogs)
        return {'status': 'success', 'data': blogs}, 200

    def post(self):
        json_data = request.get_json(force=True)
        data = blogs_schema.load(json_data)
        blog = Blog.query.filter_by(name=data['title']).first()
        if blog:
            return {'message': 'Title already exists'}, 400
        blog = Blog(name=json_data['title'], content=json_data['content'])
        db.session.add(blog)
        db.session.commit()
        result = blogs_schema.dump(blog)
        return { "status": 'success', 'data': result }, 201


class BlogResource(Resource):
    def get(self, id):
        blog = Blog.query.filter_by(id=id)
        if blog.count() > 0:
            blog = blogs_schema.dump(blog)
            return {'status': 'success', 'data': blog}, 200
        else:
            return {'message': 'Blog does not exist'}, 400

    def put(self, id):
        json_data = request.get_json(force=True)
        data = blogs_schema.load(json_data)
        blog = Blog.query.filter_by(id=id)
        if blog.count() > 0:
            blog = category.first()
            blog.title = data['title']
            blog.content = data['content']
            db.session.commit()
            result = blogs_schema.dump(blog)
            return { "status": 'success', 'data': result }, 200
        else:
            return {'message': 'Blog does not exist'}, 400

    def delete(self, id):
        blog = Blog.query.filter_by(id=id)
        if blog.count() > 0:
            blog.delete()
            db.session.commit()
            return {'status': 'success'}, 200
        else:
            return {'message': 'Blog does not exist'}, 400