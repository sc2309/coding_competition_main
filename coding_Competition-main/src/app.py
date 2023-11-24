from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import secrets
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # This suppresses a warning
app.config['SECRET_KEY'] = secrets.token_hex(16)  # 16 bytes gives a 32-character hex string

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Create tables
db.create_all()
@app.route('/')
def index():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']

        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()

        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
