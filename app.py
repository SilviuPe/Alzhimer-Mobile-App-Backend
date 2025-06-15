from flask import Flask, request
from flask_cors import CORS
import requests

from cognitive_support import get_activity_message, generate_questions
from therapy_and_recreation import create_puzzle
from accessibility_and_medical import translate_text_live
from safety_and_communication import reminders

from home import get_random_images

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return {'message':"Hello"}, 200



@app.route('/cognitive-support/dashboard')
def dashboard():
    return {
        'temp' : 20,
        'location': 'Bucharest'
    }, 200

@app.route('/cognitive-support/ai-check')
def ai_check():

    questions = generate_questions(3)

    return questions, 200

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








@app.route('/safety_and_communication/caregiver-portal')
def get_reminders():

    reminders_list = reminders()

    return reminders_list, 200





@app.route('/therapy-and-recreation/puzzle-coach')
def puzzle_therapy():
    
    game = create_puzzle()

    return game, 200






@app.route('/home/image-flasback')
def get_images_url():

    images_list = get_random_images()

    return {
        'images' : {
            'image_1' : images_list[0],
            'image_2' : images_list[1]
        },
        'date' : images_list[2]
    }, 200





@app.route('/accessibility-and-medical/live-translation-assistant', methods=['POST'])
def translate_live():

    query = request.json['query']
    src = request.json['src']
    dest = request.json['dest']

    try:

        translation = translate_text_live(query,src,dest)
        print(translation)
        return translation, 200

    except Exception as error:

        return {
            'error' : str(error)
        }, 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
