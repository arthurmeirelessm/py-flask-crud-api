from flask import Blueprint

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return "Home"

@routes.route('/main')
def main():
    return "Main"
