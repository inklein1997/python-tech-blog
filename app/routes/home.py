from flask import Blueprint, render_template
from app.models import Posts, Comments, Users
from app.db import get_db

bp = Blueprint('home', __name__, url_prefix="/")

@bp.route('/')
def index():
    db = get_db()
    posts = db.query(Posts).order_by(Posts.created_at.desc()).all()
    return render_template('homepage.html', posts=posts)

@bp.route('login/')
def login():
    return render_template('login.html')

@bp.route('signup/')
def signup():
    return render_template('signup.html')

@bp.route('dashboard/')
def dashboard():
    db = get_db()
    posts = db.query(Posts).where(Posts.user_id == 1).order_by(Posts.created_at.desc())
    return render_template('dashboard.html', posts=posts)

@bp.route('thread/<id>/')
def singlePost(id):
    db = get_db()
    post = db.query(Posts).filter(Posts.id == id).one()    
    comments = db.query(Comments).filter(Comments.post_id == post.id)
    return render_template('thread.html', post=post, comments=comments)

@bp.route('newpost/')
def newpost():
    render_template('newpost.html')
    
@bp.route('editpost/<id>')
def editpost(id):
    db=get_db()
    post = db.query(Posts).filter(Posts.id == id).one()
    print(post)
    return render_template('editpost.html', post=post)

@bp.route('logout/')
def logout():
    return