from flask import Blueprint, render_template
from app.models import Posts
from app.db import get_db

bp = Blueprint('home', __name__, url_prefix="/")

@bp.route('/')
def index():
    db= get_db()
    posts = db.query(Posts).order_by(Posts.created_at.desc()).all()
    
    return render_template('homepage.html', posts=posts)