import requests

def get_weather_data(location):
    api_key = "cce9476429eecfcc37e5b6385ac814c9"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    if response.status_code != 200:
        error_message = data.get("message", "Unknown error")
        raise Exception(f"API request failed with status code {response.status_code}: {error_message}")
    return data
