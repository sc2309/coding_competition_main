from flask import Blueprint, render_template

sports = Blueprint('login', __name__)

@sports.route('/login')
def index():
    return render_template('login.html')