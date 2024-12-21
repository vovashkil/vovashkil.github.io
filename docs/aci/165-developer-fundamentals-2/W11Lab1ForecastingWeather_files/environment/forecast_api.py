from flask import Flask, jsonify, request
import random

app = Flask(__name__)

#Mock data for different cities forecasts
weather_data = {
    'New York': {
        'current': {
            'temperature': 68,
            'condition': 'Sunny'
        },
        '5day': [
            {
                'day': "Day 1",
                'temperature': {
                    'min': 50,
                    'max': 68
                },
                'weather': 'Partly Cloudy',
                'humidity': 65,
                'wind': {
                    'speed': 10,
                    'direction': 'NE'
                }
            },
            {
                'day': "Day 2",
                'temperature': {
                    'min': 60,
                    'max': 76
                },
                'weather': 'Sunny',
                'humidity': 60,
                'wind': {
                    'speed': 12,
                    'direction': 'E'
                }
            },
            {
                'day': "Day 3",
                'temperature': {
                    'min': 58,
                    'max': 78
                },
                'weather': 'Clear',
                'humidity': 55,
                'wind': {
                    'speed': 15,
                    'direction': 'SE'
                }
            },
            {
                'day': "Day 4",
                'temperature': {
                    'min': 48,
                    'max': 58
                },
                'weather': 'Partly Cloudy',
                'humidity': 50,
                'wind': {
                    'speed': 14,
                    'direction': 'S'
                }
            },
            {
                'day': "Day 5",
                'temperature': {
                    'min': 56,
                    'max': 73
                },
                'weather': 'Mostly Sunny',
                'humidity': 45,
                'wind': {
                    'speed': 18,
                    'direction': 'SW'
                }
            },
            ]
    },
    'Atlanta': {
        'current': {
            'temperature': 74,
            'condition': 'Sunny'
        },
        '5day': [
            {
                'day': "Day 1",
                'temperature': {
                    'min': 66,
                    'max': 78
                },
                'weather': 'Sunny',
                'humidity': 70,
                'wind': {
                    'speed': 12,
                    'direction': 'NE'
                }
            },
            {
                'day': "Day 2",
                'temperature': {
                    'min': 67,
                    'max': 80
                },
                'weather': 'Sunny',
                'humidity': 70,
                'wind': {
                    'speed': 10,
                    'direction': 'NE'
                }
            },
            {
                'day': "Day 3",
                'temperature': {
                    'min': 70,
                    'max': 85
                },
                'weather': 'Partly Cloudy',
                'humidity': 70,
                'wind': {
                    'speed': 5,
                    'direction': 'SW'
                }
            },
            {
                'day': "Day 4",
                'temperature': {
                    'min': 65,
                    'max': 72
                },
                'weather': 'Rain Showers',
                'humidity': 50,
                'wind': {
                    'speed': 7,
                    'direction': 'S'
                }
            },
            {
                'day': "Day 5",
                'temperature': {
                    'min': 68,
                    'max': 73
                },
                'weather': 'Mostly Sunny',
                'humidity': 61,
                'wind': {
                    'speed': 9,
                    'direction': 'SE'
                }
            },
            ]
    },
    'Houston': {
        'current': {
            'temperature': 89,
            'condition': 'Sunny'
        },
        '5day': [
            {
                'day': "Day 1",
                'temperature': {
                    'min': 72,
                    'max': 88
                },
                'weather': 'Mostly Cloudy',
                'humidity': 43,
                'wind': {
                    'speed': 10,
                    'direction': 'W'
                }
            },
            {
                'day': "Day 2",
                'temperature': {
                    'min': 75,
                    'max': 90
                },
                'weather': 'Partly Sunny',
                'humidity': 40,
                'wind': {
                    'speed': 6,
                    'direction': 'SW'
                }
            },
            {
                'day': "Day 3",
                'temperature': {
                    'min': 70,
                    'max': 86
                },
                'weather': 'Scattered Clouds',
                'humidity': 35,
                'wind': {
                    'speed': 15,
                    'direction': 'SE'
                }
            },
            {
                'day': "Day 4",
                'temperature': {
                    'min': 71,
                    'max': 90
                },
                'weather': 'Sunny',
                'humidity': 34,
                'wind': {
                    'speed': 12,
                    'direction': 'S'
                }
            },
            {
                'day': "Day 5",
                'temperature': {
                    'min': 70,
                    'max': 87
                },
                'weather': 'Mostly Sunny',
                'humidity': 32,
                'wind': {
                    'speed': 13,
                    'direction': 'SW'
                }
            },
            ]
    }
}

@app.route('/weather', methods=['GET'])


def get_weather():
    city = request.args.get('city')
    
    if request.args.get('forecast'):
        forecast = request.args.get('forecast')
    else: 
        forecast = 'current'
        
    if city in weather_data and forecast in weather_data[city]:
        return jsonify(weather_data[city][forecast])
    else:
        return jsonify({'error': 'Invalid Parameters'}), 404
        
if __name__ == '__main__':
    app.run(port=8000)