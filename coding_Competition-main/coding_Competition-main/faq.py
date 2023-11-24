from flask import Blueprint, render_template

faq = Blueprint('faq', __name__)

@faq.route('/home')
def index():
    return render_template('faq.html')