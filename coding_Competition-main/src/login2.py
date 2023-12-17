from flask import Blueprint, render_template, request
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import hashlib

login2 = Blueprint('login2', __name__)

def compare_hashes(hash1, hash2):
    # Compare two hashes
    return hash1 == hash2

@login2.route('/login2', methods=['GET', 'POST'])
def index():
    email = request.form.get('email')
    passw = request.form.get('pass')
    # Call the function with the ID you want to fetch
    hashed_password2 = hashlib.sha256(passw.encode()).hexdigest()
    conn = sqlite3.connect('signUp.db')
    cursor = conn.cursor()
    # Using a parameterized query to avoid SQL injection
    cursor.execute("SELECT hashed_password FROM signUp_table WHERE email = ?", (email,))
    #checking_pass = '[(\'' + hashed_password2 + '\',)]'
    ogPassword = cursor.fetchall()
    #print ('the password is',ogPassword)
    conn.close()
    con = True
    if con:
        if check_password_hash(ogPassword, hashed_password2):
            print('Login successful!')
            return render_template('login2.html')
        else:
            return render_template('index.html')
    else:
        print('email dosen\'t exists')
    return render_template('index.html')