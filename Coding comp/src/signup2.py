from flask import Blueprint, render_template, request
import sqlite3

signup2 = Blueprint('signup2', __name__)

@signup2.route('/signup2', methods=['GET', 'POST'])
def index():
    firstname = request.form.get('first_name')
    lastname = request.form.get('last_name')
    number = request.form.get('number')
    email = request.form.get('email')
    password = str(request.form.get('UserPassword'))
    re_password = request.form.get('confirm_password')
    print('password is',password)
    if password != re_password:
        print("password dosen't match")
    
    conn = sqlite3.connect('signUp.db')
    cursor = conn.cursor()

    # Define the table schema if it doesn't exist, including the hashed_password column
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS signUp_table (
            id INTEGER PRIMARY KEY,
            firstname TEXT,
            lastname TEXT,
            number TEXT,
            email TEXT,
            password TEXT
        )
    ''')

    # Commit changes to the database
    conn.commit()

    # Check the table schema
    cursor.execute("PRAGMA table_info('signUp_table')")
    table_info = cursor.fetchall()
    print(table_info)  # Print the table schema info

    # Check if 'hashed_password' column exists in the table schema
    #column_exists = any(column[1] == 'hashed_password' for column in table_info)

    ## If 'hashed_password' column not present, alter the table to add it
    #if not column_exists:
    #    cursor.execute('ALTER TABLE signUp_table ADD COLUMN hashed_password TEXT')
    #    conn.commit()
    #    print("Column 'hashed_password' added to the table")

    # Insert data into the table
    cursor.execute('''
        INSERT INTO signUp_table (firstname, lastname, number, email, hashed_password) 
        VALUES (?, ?, ?, ?, ?)
    ''', (firstname, lastname, number, email, password))
    conn.commit()
    
    # Fetch and display data
    cursor.execute('SELECT * FROM signUp_table')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    cursor.close()
    conn.close()
    
    return render_template('signup2.html')
