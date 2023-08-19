from flask import Flask, render_template, request
import openweathermap

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    if request.method == "POST":
        location = request.form.get("location")
        weather_data = openweathermap.get_weather_data(location)
    return render_template("index.html", weather_data=weather_data)

if __name__ == "__main__":
    app.run(debug=True)
