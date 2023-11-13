from flask import Flask, render_template, Blueprint

# Create a Flask instance
app = Flask(__name__)

# Define the blueprint
routines = Blueprint('routines', __name__)

# Register a route inside the blueprint
@routines.route('/routine')
def index():
    return render_template('routine.html')

