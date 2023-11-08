from flask import Blueprint, render_template

sports = Blueprint('signup', __name__)

@sports.route('/signup')
def index():
    return render_template('signup.html')