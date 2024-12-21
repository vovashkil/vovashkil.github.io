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

# if the response.status_code is 200 (successful) then return the weather data from the app in JSON format
if response.status_code == 200:
    # Assuming the API returns JSON Data
    weather_data = response.json()
    
    # Loop through the return from the API and for each day print if it is a beach day(that is, contains 'Sunny'), else print if it is not a suitable day
    for day in weather_data:
        if 'Sunny' in day['weather']:
            print(day['day'], 'is a beach day. Enjoy the sun!')
        else:
            print(day['day'], 'is not suitable for the beach.')
else:
    # If the response.status_code is not 200 (successful) then return the status_code
    print('Failed to retrieve weather data. Status code:', response.status_code)