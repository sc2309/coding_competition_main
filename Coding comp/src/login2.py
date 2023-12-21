from flask import Blueprint, render_template, request
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

login2 = Blueprint('login2', __name__)

@login2.route('/login2', methods=['GET', 'POST'])
def index():
    email = request.form.get('email')
    passw = request.form.get('pass')
    # Call the function with the ID you want to fetch
    hashed_password2 = passw
    conn = sqlite3.connect('signUp.db')
    cursor = conn.cursor()
    # Using a parameterized query to avoid SQL injection
    cursor.execute("SELECT hashed_password FROM signUp_table WHERE email = ?", (email,))
    #checking_pass = "[('" + hashed_password2 + "',)]"
    checking_pass = hashed_password2
    ogPassword = cursor.fetchall()
    print ('the password is',ogPassword)
    print ('the password2 is',checking_pass)
    conn.close()
    if ogPassword == checking_pass:
        print('Login successful!')
    else:
        pass
    return render_template('login2.html')