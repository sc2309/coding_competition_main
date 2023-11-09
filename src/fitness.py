from flask import Blueprint, render_template

fitness = Blueprint('fitness', __name__)

@fitness.route('/fitness')
def index():
    return render_template('fitness.html')