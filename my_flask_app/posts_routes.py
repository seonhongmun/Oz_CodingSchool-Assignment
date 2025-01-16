from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
from db import db, Posts
from datetime import datetime

time = datetime.now()
Post_blp = Blueprint('Posts', 'posts', description='Operations on users', url_prefix='/post')

@Post_blp.route('/')
class PostList(MethodView):  #게시글 조회
    def get(self):
        posts = Posts.query.all()
        post_data = [{"id":post.id, 
                    "title": post.title,
                    "content": post.content,
                    "created_at":post.created_at} for post in posts]
        return jsonify(post_data)

    def post(self):   # 게시글 생성
        post_data = request.json
        new_post = Posts(title=post_data['title'], content=post_data['content'], created_at=[time])
        db.session.add(new_post)
        db.session.commit()
        return jsonify({"message": "Create Post Complete"}), 201

@Post_blp.route('/<int:id>')
class Users(MethodView):
    def get(self, user_id):
        posts = Posts.query.get_or_404(user_id)
        return {"name": posts.name, 'email': posts.email}

    def put(self, user_id):
        user = User.query.get_or_404(user_id)
        user_data = request.json

        user.name = user_data['name']
        user.email = user_data['email']

        db.session.commit()
        return {"message": "User updated"}

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted"}