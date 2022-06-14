from flask import Flask, request, render_template
import random

app = Flask(__name__)

temperaturedata = [
    "25", "10", "15", "2", "5", "72", "1", "-9", "2", "14", "12", "8"

]
winddata = [

    6, 8, 7, 3, 12, 45, 0, 9, 1, 11

]
directiondata = [

    58, 0, 180, 23, 360, 122, 10, 19

]


@app.route('/temperature', methods=['POST'])
def weather():
    location = request.form['location']
    wind = random.choice(winddata)
    direction = random.choice(directiondata)
    return render_template('temperature.html', temp=random.choice(temperaturedata), wind=wind, direction=direction, location=location)


@app.route('/wind', methods=['POST', 'GET'])
def wind():
    location = request.form.get("location")
    wind = random.choice(winddata)
    direction = random.choice(directiondata)
    return render_template('wind.html', wind=wind, direction=direction, location=location)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
