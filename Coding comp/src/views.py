from flask import Blueprint, render_template

views = Blueprint('views', __name__)

challenges = ['challenge: do 50 push ups','challenge: do 100 push ups','challenge: do 30 sit ups','challenge: do 50 squats','challenge: 50 sit ups','challenges: do 30 pull ups','challenge: do 50 pull ups']
current_index = 0

def new_diet(x):
    global current_index
    item = x[current_index]
    current_index = (current_index + 1) % len(x)
    return item

@views.route('/')
def index():
    next_challenge=new_diet(challenges)
    return render_template('index.html', next_challenge=next_challenge)