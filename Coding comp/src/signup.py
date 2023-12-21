from flask import Blueprint, render_template

signup = Blueprint('signup', __name__)

@signup.route('/signup')
def index():
    return render_template('signup.html')