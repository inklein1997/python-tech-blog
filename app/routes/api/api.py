from flask import Blueprint, request, jsonify, session, redirect
from app.models import Users, Comments, Posts
from app.db import get_db
import sys

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/users/signup', methods=['POST'])
def signup():
  db = get_db()
  data = request.get_json()
  
  try:
    newUser = Users(
        user = data['user'],
        password = data['password']
    )
    
    db.add(newUser)
    db.commit()
  except:
    return jsonify(message='Signup failed'), 500

  session.clear()
  session['user_id'] = newUser.id
  session['username'] = newUser.user
  session['loggedIn'] = True
  return jsonify(id = newUser.id)

@bp.route('/users/login', methods=['POST'])
def login():
  data = request.get_json()
  db = get_db()
  
  try:
    user = db.query(Users).filter(Users.user == data['user']).one()
    if user.verify_password(data['password']) == False:
      return jsonify(message = 'Incorrect credentials'), 400
    session.clear()
    session['user_id'] = user.id
    session['username'] = user.user
    session['loggedIn'] = True
    return jsonify(id = user.id)
  except:
    print(sys.exc_info()[0])
    return jsonify(message = 'Incorrect credentials'), 400

@bp.route('/users/logout', methods=['POST'])
def logout():
  # remove session variables
  session.clear()
  return '', 204

@bp.route('/comments', methods=['POST'])
def comment():
  data = request.get_json()
  db = get_db()
  try:
  # create a new comment
    newComment = Comments(
    content = data['content'],
    post_id = data['post_id'],
    user_id = session.get('user_id')
  )

    db.add(newComment)
    db.commit()
  except:
    print(sys.exc_info()[0])

    db.rollback()
    return jsonify(message = 'Comment failed'), 500
  return jsonify(id = newComment.id)

@bp.route('/posts', methods=['POST'])
def create():
  data = request.get_json()
  db = get_db()

  try:
    # create a new post
    newPost = Posts(
      title = data['title'],
      description = data['description'],
      user_id = session.get('user_id')
    )

    db.add(newPost)
    db.commit()
  except:
    print(sys.exc_info()[0])

    db.rollback()
    return jsonify(message = 'Post failed'), 500

  return jsonify(id = newPost.id)

@bp.route('/posts/<id>', methods=['PUT'])
def update(id):
  data = request.get_json()
  db = get_db()

  try:
    # retrieve post and update title property
    post = db.query(Posts).filter(Posts.id == id).one()
    post.title = data['title']
    post.description = data['description']
    db.commit()
  except:
    print(sys.exc_info()[0])

    db.rollback()
    return jsonify(message = 'Post not found'), 404

  return '', 204

@bp.route('/posts/<id>', methods=['DELETE'])
def delete(id):
  db = get_db()

  try:
    # delete post from db
    db.delete(db.query(Posts).filter(Posts.id == id).one())
    db.commit()
  except:
    print(sys.exc_info()[0])

    db.rollback()
    return jsonify(message = 'Post not found'), 404

  return '', 204


