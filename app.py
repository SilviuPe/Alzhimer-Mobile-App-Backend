from flask import Flask
import requests

from cognitive_support import get_activity_message
from therapy_and_recreation import create_puzzle

app = Flask(__name__)

@app.route('/')
def home():
    return {'message':"Hello"}, 200


@app.route('/cognitive-support/dashboard')
def dashboard():
    return {
        'temp' : 20,
        'location': 'Bucharest'
    }, 200
    

@app.route('/cognitive-support/ai-check-in')
def ai_check_in():
    return {}, 200

@app.route('/cognitive-support/digital-storybook')
def digital_storybook():
    return {}, 200

@app.route('/cognitive-support/locked-down-mode')
def locked_down_mode():
    return {}, 200

@app.route('/cognitive-support/what-am-i-doing')
def waid():

    message = get_activity_message()

    return {'message': message}, 200


@app.route('/therapy-and-recreation/puzzle-coach')
def puzzle_therapy():
    
    game = create_puzzle()

    return game, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
