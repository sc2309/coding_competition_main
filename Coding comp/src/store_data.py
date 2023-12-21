from flask import Blueprint, render_template, request

store_data = Blueprint('store_data', __name__)

@store_data.route('/store_data', methods=['GET', 'POST'])
def index():
    feedback = request.form.get('feedback')
    file_name = 'feedback.txt'
    with open(file_name, "a") as file:
        file.write("\n" + feedback)
    return render_template('feedback.html')