from flask import Blueprint, render_template

sports = Blueprint('sports', __name__)

@sports.route('/sports')
def index():
    return render_template('sports.html')