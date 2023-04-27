from flask import Blueprint, render_template
from app.models import Post
from app.db import get_db

# import function blueprint
bp = Blueprint('home', __name__, url_prefix='/')

# define function index


@bp.route('/')
def index():
    # get all posts
    db = get_db()
    posts = db.query(Post).order_by(Post.created_at.desc()).all()

    return render_template(
        'homepage.html',
        posts=posts
    )

# define function login
# @bp.route is a decorator whatever function returns it becomes a response


@bp.route('/login')
def login():
    return render_template('login.html')


@bp.route('/post/<id>')
def single(id):
    return render_template('single-post.html')
