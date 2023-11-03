





#                         THIS IS A DEMO FILE AND WILL BE USED IN DIET.PY











from flask import Flask, render_template

app = Flask(__name__)

# List of items
x = ['dal', 'rice', 'sabzi', 'roti']
# Variable to keep track of the current item index
current_index = 0

# Function to get the next item from the list
def get_next_item():
    global current_index
    item = x[current_index]
    current_index = (current_index + 1) % len(x)
    return item

# Route that renders an HTML template with the next item from the list
@app.route('/')
def index():
    next_item = get_next_item()
    return render_template('test.html', next_item=next_item)

if __name__ == '__main__':
    app.run(debug=True)
