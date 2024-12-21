# Import the requests library
import requests

# Create a variable called "url" and set it to the site for the API.
url = 'http://localhost:8000/weather'

# Create a dictionary called params and set the key value pairs(<city>:<city name>, <forecast>:<forecast length>)
params = {
    'city': 'Houston',
    'forecast': '5day'
}

# Create a variable for the response. Use the request.get method and pass the URL and params
response = requests.get(url, params=params)

# If the response.status_code is 200 (successful) then return the weather data from the app in JSON format
if response.status_code == 200:
    # Assuming the API returns JSON Data
    weather_data = response.json()
    print('\n5 day forecast for', params['city'], ':\n\n', weather_data)
else:
    # If the response.status_code is not 200 (successful) then return the status_code
    print('Failed to retrieve weather data. Status code:', response.status_code)
