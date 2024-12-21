# Forecasting the Weather with an API

## Lab overview

This lab gives hands on experience of using Python to request data from an API. You learn how to use the Python requests library to query a remote API.

You focus on retrieving data using the GET method from this module and retrieve weather information in a JSON format. It is important to understand, that in real-world situations, every API is different and could use different data formats.

Objectives
By the end of this lab, you should be able to do the following:

Learn how to import and use the Python Requests library.
Query a remote API.
Specify the appropriate parameters for a request and pass that to an API.
Store, parse and utilize the data that is returned from the API.
Technical knowledge prerequisites
This hands-on lab assumes that you have completed the Developer Fundamentals 1 (DF1) course and the associated labs.

Duration
This lab requires approximately 60 minutes to complete.

Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Expected output: A sample output that you can use to verify the output of a command or edited file
 Command: A command that you must run
 Hint: A hint to a question or challenge
 Task complete: A conclusion or summary point in the lab
 Note: A hint, tip, or important guidance
Start lab
To launch the lab, at the top of the page, choose Start lab.

 Caution: You must wait for the provisioned AWS services to be ready before you can continue.

To open the lab, choose Open Console .

You are automatically signed in to the AWS Management Console in a new web browser tab.

 Warning: Do not change the Region unless instructed.

Common sign-in errors
Error: Choosing Start Lab has no effect
In some cases, certain pop-up or script blocker web browser extensions might prevent the Start Lab button from working as intended. If you experience an issue starting the lab:

Add the lab domain name to your pop-up or script blocker’s allow list or turn it off.
Refresh the page and try again.
AWS services used in this lab
AWS Cloud9
AWS Cloud9 is a cloud-based IDE that offers a rich code-editing experience with support for several programming languages and runtime debuggers, and a built-in terminal. It contains a collection of tools that you use to code, build, run, test, and debug software, and helps you release software to the cloud.

Task 1: Establishing the development environment
In this task, you connect to the AWS Cloud9 IDE.

In the Lab Information navigation pane, copy the Cloud9Environment value, and paste it into a new web browser tab.

 Expected output: A new browser tab opens and displays the AWS Cloud9 IDE.

Choose X next to Welcome to close the Welcome window.

Cloud9 navigation menu is displayed on the left side to perform operation with files such as creating New, Save etc.

Cloud9 Terminal Session window is displayed at the bottom with a $ prompt. You use this window to run commands in the lab.

 Task complete: You have successfully connected to the AWS Cloud9 IDE.

Task 2: Retrieve the current weather for a specific location
In this task, you retrieve the current weather conditions for a specific location by sending a GET request to a remote API.

To start, you test the API using command line.

 Command: To test the API using the command line, run the following code in the terminal window:

curl "http://localhost:8000/weather?city=Atlanta"
 Expected output:



{"condition":"Sunny","temperature":74}
 Additional information: When you run the above command it sends a GET request to the API which resides at the url http://localhost:8000/weather. The command also passes a parameter named city to retrieve the expected response. If the city name mentioned is invalid or not found in the API, the request will fail with HTTP/1.1 404 NOT FOUND error.

From the navigation pane of the IDE, choose the request_current.py file.

In the request_current.py file, Replace INSERT_URL_HERE placeholder value with http://localhost:8000/weather.

In the request_current.py file, Replace INSERT_CITY_HERE placeholder value with Atlanta.

To see how the request_current.py file looks after replacing these placeholder values, expand this section.
From the File menu, choose Save.

 Command: Run the following command in the bash terminal:


python request_current.py
 Expected output:



Weather data for Atlanta :

 {'condition': 'Sunny', 'temperature': 74}
When you run the python script it sends a GET request to the API, similar to the curl command you performed in step 5.

 Task complete: You have successfully retrieved the current weather conditions for a specific location by sending a GET request to a remote API.

Task 3: Request a 5-day forecast for a location
In this task, you perform an API request to include an additional parameter that should return a 5-day forecast, rather than just the current weather conditions.

From the navigation pane of the IDE, choose the request_5day.py file.

In the request_5day.py file, Replace INSERT_URL_HERE placeholder value with http://localhost:8000/weather.

In the request_5day.py file, Replace INSERT_CITY_HERE placeholder value with Houston.

In the request_5day.py file, Replace INSERT_FORECAST_HERE placeholder value with 5day.

Expand this link to see how the request_5day.py file looks after replacing the above placeholder values.
From the File menu, choose Save.

 Command: To run the code, enter the following command in the bash terminal:


python request_5day.py
 Expected output:



5 day forecast for Houston :

 [{'day': 'Day 1', 'humidity': 43, 'temperature': {'max': 88, 'min': 72}, 'weather': 'Mostly Cloudy', 'wind': {'direction': 'W', 'speed': 10}}, {'day': 'Day 2', 'humidity': 40, 'temperature': {'max': 90, 'min': 75}, 'weather': 'Partly Sunny', 'wind': {'direction': 'SW', 'speed': 6}}, {'day': 'Day 3', 'humidity': 35, 'temperature': {'max': 86, 'min': 70}, 'weather': 'Scattered Clouds', 'wind': {'direction': 'SE', 'speed': 15}}, {'day': 'Day 4', 'humidity': 34, 'temperature': {'max': 90, 'min': 71}, 'weather': 'Sunny', 'wind': {'direction': 'S', 'speed': 12}}, {'day': 'Day 5', 'humidity': 32, 'temperature': {'max': 87, 'min': 70}, 'weather': 'Mostly Sunny', 'wind': {'direction': 'SW', 'speed': 13}}]
 Task complete: You have successfully retrieved 5 day weather conditions for a specific location by sending a GET request to a remote API.

Task 4: Parsing the weather forecast to only display the weather for a specific day
In this task, you request a 5-day forecast, and parse the returned JSON response so that it will only show the weather conditions that are being forecasted for the day after tomorrow.

From the navigation pane of the IDE, choose the parse_forecast.py file.

In the parse_forecast.py file, Replace INSERT_URL_HERE placeholder value with http://localhost:8000/weather.

In the parse_forecast.py file, Replace INSERT_CITY_HERE placeholder value with New York.

In the parse_forecast.py file, Replace INSERT_FORECAST_HERE placeholder value with 5day.

Expand this link to see how the parse_forecast.py file looks like after replacing the above placeholder values.
 Additional information: Observe that this code has some additional steps to work with the response from the API. The API response is loaded into the dictionary weather_data. The weather_data is then searched for the Day 2 entry and then the information for day 2 is printed.

From the File menu, choose Save.

 Command: To run the code, enter the following command in the bash terminal:


python parse_forecast.py
 Expected output:



The weather for the day after tomorrow is forecasted as:

Hi Temp: 76
Lo Temp: 60
Weather Conditions: Sunny
Winds: E at 12 mph
 Task complete: You have successfully parsed the returned JSON response so that it will only show the weather conditions that are being forecasted for the day after tomorrow.

Challenge Task
In this challenge task, you create a new Python file that loops through the results of each day and prints whether it is a beach day or not.

From the navigation pane of the IDE, choose the beach_day.py file.
This file is provided to you as a skeleton to start your challenge task. The file contains the url and parameters required to build this python file.

 Hint: The file has some comments and hints which can help you complete this task, also refer to previous tasks for more help.

If you find yourself struggling with the challenge and need assistance to make progress, expand this link for a complete solution of this challenge.

Challenge Solution
 Task complete: You have successfully completed the challenge task.

Conclusion
You have successfully done the following:

Learned how to import and use the Python Requests library.
Queried a remote API.
Specified and passed an API the appropriate parameters for a request.
Stored, parsed and utilized the data that is returned from the API.
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End lab and then confirm that you want to end your lab.

For more information about AWS Training and Certification, see https://aws.amazon.com/training/.

Your feedback is welcome and appreciated.
If you would like to share any feedback, suggestions, or corrections, please provide the details in our AWS Training and Certification Contact Form.