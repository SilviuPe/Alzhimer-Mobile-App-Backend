from flask import Flask, request
import requests

from cognitive_support import get_activity_message
from therapy_and_recreation import create_puzzle
from accessibility_and_medical import translate_text_live

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






@app.route('/accessibility-and-medical/live-translation-assistant', methods=['POST'])
def translate_live():

    query = request.json['query']
    src = request.json['src']
    dest = request.json['dest']

    try:

        translation = translate_text_live(query,src,dest)

        return translation, 200

    except Exception as error:

        return {
            'error' : str(error)
        }, 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
