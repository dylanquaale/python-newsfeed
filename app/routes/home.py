from flask import Blueprint, render_template

## import function blueprint
bp = Blueprint('home', __name__, url_prefix='/')

## define function index
@bp.route('/')
def index():
  return render_template('homepage.html')

## define function login 
## @bp.route is a decorator whatever function returns it becomes a response 
@bp.route('/login')
def login():
  return render_template('login.html')