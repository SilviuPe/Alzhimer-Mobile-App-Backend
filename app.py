from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return {'message':"Hello"}, 200


@app.route('/cognitive-support/dashboard')
def dashboard():
    # API_KEY = '255a2a2498d31a425a439aa0ff887a87'
    # CITY = "Galati"
    # URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    # print(URL)
    # response = requests.get(URL)
    # data = response.json()

    
    # if response.status_code == 200:
    #     temp = data['main']['temp']
    #     weather = data['weather'][0]['description']

    #     return { "temp" : temp, "weather" : weather}, 200

    # else:
    #     return {"Error": f"{data.get('message', 'Failed to retrieve data')}"}, 400

    return {
        'temp' : 20,
        'location': 'Bucharest'
    }, 200
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)