from flask import Blueprint, render_template, session, redirect
from app.models import Posts, Comments, Users
from app.db import get_db

bp = Blueprint('home', __name__, url_prefix="/")

@bp.route('/')
def index():
    db = get_db()
    posts = db.query(Posts).order_by(Posts.created_at.desc()).all()
    return render_template('homepage.html', posts=posts, loggedIn=session.get('loggedIn'), user_id=session.get('user_id'), username=session.get('username'))

@bp.route('login/')
def login():
  if session.get('loggedIn') is None:
    return render_template('login.html')
  return redirect('/dashboard', loggedIn=session.get('loggedIn'), user_id=session.get('user_id'), username=session.get('username'))

@bp.route('signup/')
def signup():
  if session.get('loggedIn') is None:
    return render_template('signup.html')
  return redirect('/dashboard', loggedIn=session.get('loggedIn'), user_id=session.get('user_id'), username=session.get('username'))

@bp.route('dashboard/')
def dashboard():
    if session.get('loggedIn') is None:
      return redirect('/login')
    else:
      db = get_db()
      posts = db.query(Posts).where(Posts.user_id == session.get("user_id")).order_by(Posts.created_at.desc())
      return render_template('dashboard.html', posts=posts, loggedIn=session.get('loggedIn'), user_id=session.get('user_id'), username=session.get('username'))

@bp.route('thread/<id>/')
def singlePost(id):
    db = get_db()
    post = db.query(Posts).filter(Posts.id == id).one()    
    comments = db.query(Comments).filter(Comments.post_id == post.id)
    return render_template('thread.html', post=post, comments=comments, loggedIn=session.get('loggedIn'), user_id=session.get('user_id'), username=session.get('username'))

@bp.route('newpost/')
def newpost():
    return render_template('newpost.html', loggedIn=session.get('loggedIn'), user_id=session.get('user_id'), username=session.get('username'))
    
@bp.route('editpost/<id>')
def editpost(id):
    db=get_db()
    post = db.query(Posts).filter(Posts.id == id).one()
    print(post)
    return render_template('editpost.html', post=post, loggedIn=session.get('loggedIn'), user_id=session.get('user_id'), username=session.get('username'))

@bp.route('logout/')
def logout():
    session.clear()
    return redirect('/')