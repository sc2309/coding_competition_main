from flask import Blueprint, render_template

diet = Blueprint('diet', __name__)

@diet.route('/diet')
def index():
    return render_template('daily_diet.html')