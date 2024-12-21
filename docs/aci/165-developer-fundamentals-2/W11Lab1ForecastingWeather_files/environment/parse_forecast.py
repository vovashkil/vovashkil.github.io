# Import the requests library
import requests

# Create a variable called "url" and set it to the site for the API.
url = 'http://localhost:8000/weather'

# Create a dictionary called params and set the key value pairs(<city>:<city name>, <forecast>:<forecast length>)
params = {
    'city': 'New York',
    'forecast': '5day'
}

# Create a variable for the response. Use the request.get method and pass the URL and params
response = requests.get(url, params=params)

# If the response.status_code is 200 (successful) then return the weather data from the app in JSON format
if response.status_code == 200:
    # Assuming the API returns JSON data
    weather_data = response.json()
    day_2_info = next(item for item in weather_data if item['day'] == 'Day 2')

    print('\nThe weather for the day after tomorrow is forecasted as:\n')
    print('Hi Temp:', day_2_info['temperature']['max'])
    print('Lo Temp:', day_2_info['temperature']['min'])
    print('Weather Conditions:', day_2_info['weather'])
    print('Winds:', day_2_info['wind']['direction'], 'at', day_2_info['wind']['speed'], 'mph')
else:
    # If the response.status_code is not 200 the return the status_code.
    print('Failed to retrieve weather data. Status code:', response.status_code)