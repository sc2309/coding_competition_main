from flask import Blueprint, render_template

sports = Blueprint('fitness', __name__)

@sports.route('/fitness')
def index():
    return render_template('fitness.html')