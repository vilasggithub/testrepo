from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def retrieve():
    return render_template('myForm.html')


@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == "POST":
        city = request.form['city']
        # res = requests.get(
        #    "http://api.wunderground.com/api/7c1c38b610841bda/conditions/q/PA/Philadelphia.json")
        res = requests.get(
            "http://api.wunderground.com/api/7c1c38b610841bda/conditions/q/PA/" + city + ".json")
        weather = res.json()  # Get the json data
        city = weather['current_observation']['display_location']['full']
        temp = weather['current_observation']['temp_f']
        weather_cond = weather['current_observation']['weather']
        humidity = weather['current_observation']['relative_humidity']
        data = {"city": city, "temp": temp, "weather_cond": weather_cond, "humidity": humidity}
        return render_template('weather.html', data=data)
        # return render_template('weather.html', city=city, temp=temp, weather_cond=weather_cond, humidity=humidity)


if __name__ == '__main__':
    app.run(debug=True)
