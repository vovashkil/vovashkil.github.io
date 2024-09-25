###### back to AWS Cloud Institute repo's root [aci.md](../aci.md)
###### back to repo's main [README.md](../../../README.md)
# AWS Cloud Institute
## Developer Fundamentals 1
### Week 1: Python 1 - Python Overview
### Week 2: Python 1 - Data Structures and Iterables
### Week 3: Python 1 - Functions
### Week 4: Python 1 - Classes and Objects

#### Classes
The terms **class** and **type** are practically synonymous in Python. In practice, people use the term **type** to refer to Python’s **built-in types like lists**, and **class** to refer to **user-defined types**.

The constructor method belongs to a group called **dunder** methods.

#### Dunder methods
Special methods that start and end with double underscores (__).

They provide functionality that isn't available through regular methods.

#### Some of the reasons to use classes and objects in programming
##### Better organization
You can use classes to organize your code into logical and reusable blocks. You can establish relationships among objects and represent the behaviors and properties of the specific objects that you want to model in your code.

##### Code reusability
After you have defined a class, you can create objects from it without having to rewrite any of the universal characteristics or tools that define the class. In this case, you will generate an object to represent each employee in the system. By creating a class, you can easily generate new employee objects with unique details in a single line of code.

##### Easier code maintenance
Classes provide a way to break down complex systems into smaller, more manageable modular units. You can change and test code at the modular level and quickly target errors and necessary corrections. When you find a bug in your application, you can target your fixes to the affected classes without affecting the broader system you've created.

#### Defining **class** attributes
The following syntax creates an Employee class, with a class attribute named status. Each employee object created from this class will include this attribute. 

```
class Employee:
    status = "active"
```

#### Defining instance attributes
The constructor is created with one of the special dunder methods (__init__). The __init__ function builds your object. It is called automatically when an object of a class is created, and it assigns the starting attributes and methods that make up your object.

```
    def __init__(self):
        # initial values
```

When a class is instantiated, the __init__ function runs and assigns the values passed in as arguments to the attributes named in the class definition.

Your classes can include a mix of **class** and **instance** attributes.

#### Defining instance methods
Instance methods are functions that are bound to the instance of a class.

The following code creates a post method for each employee. A line has been added to the __init__ function to initialize an empty list on creation of an object. The post method takes the content passed in when the post method is called and adds it to the employee's list of posts.

```
class Employee:
    employee_count = 0
    
    def __init__(self, name, email, hire_date):
        self.name = name
        self.email = email
        self.hire_date = hire_date
        Employee.employee_count += 1
        
        self.posts = [] #initiates list to hold user posts
        
    def post(self, content):
        new_post = content
        self.posts.append(new_post) 
```

#### Week 4 Assessment
##### A game developer has created a function to randomly scramble the letters of a word or phrase. This will be used in several games, and more functions that manipulate text and change the way the words are printed by default will be developed later. What is one way the developer can make their code easy to reuse, maintain, and extend without recreating existing functionality?
* `Create a subclass of the built-in str class and add the function as a method.`. This will add the function as a method to a new string subclass while maintaining all of the methods and attributes of the built-in class. The new functions can be added as additional methods. Methods of the string class, such as the way objects are printed, can be overridden in the subclass.

The other options are incorrect because of the following:
* `Add the function definition to the built-in str class.` You cannot directly change a built-in class.
* `Create a new data type by copying all of the attributes of the str class and add the function as a method`. This will not inherit the methods and attributes of the str class.
* `Create a new empty class and add the function as a method`. It is not necessary to create a new string type when inheritance will automatically include these.

##### A developer is troubleshooting their code. How could they print a dictionary object containing the changeable attributes of the object named p1?
```
class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

p1 = Person('John Smith', 44, 'US')
```
* `print(vars(p1))`. The `vars()` function output all of the changeable attributes of an object.

Incorrect options:
* print(repr(p1))
* print(p1)
* print(object(p1))

##### What is the advantage of using the super() function to access the methods and attributes of a parent class?
* The name of the parent element isn't needed when accessing its methods and attributes.

Incorrect answers:
* It returns a new class containing a superset of the methods and attributes of both classes.
* The attributes and methods of the parent class are invoked at a higher priority.
* The methods and attributes of the child class are added to the parent class without modifying the parent.

### Week 5: Python 1 - Libraries and Modules
### Week 6: Python 1 - Files and File Handling
#### open() function to open file

##### Modes for open()

| Method | Description |
| ------ | ----------- |
| Read "r" | Default value. Use this method for reading the contents of an existing file. If the file does not exist, Python displays an error. |
| Append "a" | Use this method to add data to an existing file. If the file does not exist, Python creates a new one. |
| Write "w" | Use this method to write data into a file. If the file exists, Python will overwrite it. If the file does not exist, Python will create a new one. |
| Create "x" | Use this method to create a new file. If the file already exists, Python displays an error. |

By default, Python uses "t" (text mode) for text-based file handling. You can also use "b" (binary mode) for handling binary files, such as images.

**Because "r" for read and "t" for text are the default values, you do not need to specify them for your code to run successfully. However, including them can make your code more explicit and easier to understand for others who may read it.**

#### Creating and writing files

```
# Create a file and write a welcome message to it.
f = open("welcome.txt", "w")
f.write("Hello! Welcome to the Python 1 module. This file is for testing purposes. Hope you are enjoying this module so far.")

# Open the file and print its contents.
f = open("welcome.txt", "r")
print(f.read())
f.close()
```

#### Opening and reading files
When using the open() function to open a file, you need to include the name of the file you want to open. By default, Python looks for the file you are referencing in the directory where the program that you are running is stored. If the file resides in a different location, you need to specify its file path, as in the following example.

```
f = open("D:\\appfiles\welcome.txt", "r")
print(f.read())
```

Without arguments, the read() method reads the entire content of your file. With a size argument, the read() method reads a specific number of bytes from the file. 

```
f = open("welcome.txt", "r")
print(f.read(5))
```

#### Deleting files
```
import os
os.remove("welcome.txt")
```

Check existence before deleting
```
import os
if os.path.exists("welcome.txt"):
  os.remove("welcome.txt")
else:
  print("The file does not exist")
```

#### Working with JSON and Python
##### Mapping

| Python | JSON |
| ------ | ---- |
| dict | object |
| list, tuple | array |
| str | string |
| int, float | number |
| True | true |
| False | false |
| None | null |

#### json.loads() and json.dumps()
* json.dump() encodes a Python object as JSON and writes it to a file.
* json.dumps() encodes a Python object as a JSON-formatted string.
* json.load() decodes JSON data from a file and returns a Python object.
* json.loads() decodes a JSON-formatted string into a Python object.

#### Converting from JSON to Python
In this example, you use json.loads() to convert a JSON-formatted string into a Python object. 

```
# Import the JSON module
import json

# Define a JSON-formatted string.
x =  '{ "name":"John", "lastname":"Stiles", "city":"Seattle"}'

# Convert the JSON string into a Python object.
y = json.loads(x)

# Print the value of 'city'.
print(y["city"])
```

#### Using json.load()
json.load() reads JSON data from a file and convert it into Python. 

#### Convert from Python to JSON
You can convert Python objects of the following types into JSON:
* dict
* list
* tuple
* string
* int
* float
* True
* False
* None

json.dumps() method converts the dictionary into a JSON-formatted string

```
import json

# Define a dictionary with three key-value pairs.
x = {
  "dog": "Jack",
  "breed": "Golden Retriever",
  "city": "Albuquerque"
}

# Convert dictionary into a JSON string using json.dumps().
y = json.dumps(x)

# Print output.
print(y)
```

**Use the indent parameter to define the number of indents.**

```
json.dumps(x, indent=4)
```

**Use the separators parameter to change the default separator.**

```
json.dumps(x, indent=4, separators=(". ", " = "))
```

```
{
    "dog" = "Jack". 
    "breed" = "Golden Retriever". 
    "city" = "Albuquerque"
}
```

#### Looping over dictionaries and JSON
You can use the json module to loop over dictionaries represented as JSON objects. In this example, you define a JSON string called x. You then use the json.loads() method to parse the JSON data into a Python dictionary called py_dict. Finally, you use a for loop to iterate through the Python dictionary and print out each value pair.

```
# Import the JSON module
import json

# Define JSON string
x = '{"name": "John", "lastname": "Stiles", "city": "Seattle"}'

# Parse JSON data into a Python dictionary
py_dict = json.loads(x)

# Loop through the Python dictionary
for key, value in py_dict.items():
    print(key, ":", value)
```

#### Using input validation
You can use a JSON schema to perform input validation in Python. A JSON schema is a JSON document that allows you to validate JSON documents. JSON schemas are a way to define the expected structure, data types, and validation rules for JSON data.

To use a JSON schema for input validation in Python, use the jsonschema library. It is an implementation of the JSON Schema specification for Python.

**You install jsonschema using the following command: pip install jsonschema.**

```
import jsonschema
import json
# Define a JSON schema.
schema = {
    "type": "object",
    "properties": {
        "firstname": {"type": "string"},
        "lastname" : {"type": "string"},
        "age": {"type": "integer"}
    },
    "required": ["firstname", "lastname", "age"]
}
# Validate a JSON document against the schema.
document = {
    "firstname": "John",
    "lastname": "Stiles",
    "age": 28
}
try:
    jsonschema.validate(document, schema)
except jsonschema.exceptions.ValidationError as x:
    print(x)
```

### Week 7: Python 1 - Logging and Error Handling
#### Logging in Python
For Python, a logging module is included in the standard library. 

The **print** function is a general purpose tool, while **logging** is a specialized one. In general, when you're working with Python's standard library, you can assume that a tool specifically designed for a particular task is more efficient than a general purpose workaround.

#### Logging importance
##### Debugging and troubleshooting
Logging can help you flag and investigate bugs in your code. Logs provide historical context for events, so developers can study log files to locate and resolve bugs. They also use tools like log analyzers to automate the processing of log files.  

##### Monitoring and performance analysis
Logging provides monitoring and performance analysis by capturing data about an application's behavior over time. Developers can include logs that measure efficiency of running code. They can use those logs to detect weak performance and resolve inefficiencies.

##### Security and compliance
Logs can be used to identify and fix security vulnerabilities in application code, as well as ensure that security policies are being followed. Regular reviews of audit logs can help organizations identify and improve weaknesses in their systems.

#### Error handling in Python
Error handling refers to the process of anticipating, detecting, responding to and recovering from errors that occur when an application runs. It is an essential part of software development, typically used in conjunction with logging. 

When you anticipate where errors might occur, error handling provides a way to resolve or work around the problems without stopping your program or losing data. Without proper error handling, software can fail in unpredictable ways, leading to data loss and security vulnerabilities.

#### The logging module
The logging module is included with the Python standard library.

#### Keeping logs

##### The basicConfig method
```
logging.basicConfig(filename="example.log", level=logging.DEBUG)
```

#### Formatting messages
```
logging.basicConfig(filename="example.log", 
                    format="%(asctime)s %(levelname)s %(message)s", 
                    level=logging.DEBUG)
```

#### Errors and exceptions

#### Types of errors
##### Syntax errors
A syntax error occurs when the Python interpreter cannot parse the code. Common reasons for syntax errors include: unclosed quotation marks or parentheses, missing punctuation at the beginning of a code block, or unexpected indentation. 

Python error messages usually point programmers directly to the error-causing code.

##### Runtime errors
Generally speaking, a runtime error occurs when a program is running and an unexpected condition or value prevents it from continuing. When a program stops due to a runtime error, people often say that the program has crashed.

##### Logical errors
A logical error won't interrupt the flow of a running program, but it will produce an incorrect or unexpected result. These are frequently caused by the incorrect use of a tool, method, or function. Or, a logical error could reflect a misunderstanding of the problem the program is trying to solve.

#### Handling exceptions
```
integer = 50
string = "The number is "

try: 
    expression = string + integer
except:
    print ("Exception occurred")
    expression = string + str(integer) 

print (expression)
```

```
def add_numbers(x, y):
    """Adds two numbers and returns the sum"""
    try: 
        return x + y
    except: 
        return (f"Cannot add {type(x)} and {type(y)}")

print(add_numbers(2, 3))
```

#### Planning for exceptions
```
def divide_numbers():
    
    try:
        dividend = int(input("Enter the integer to divide: "))
        divisor = int(input("Enter the integer to divide by: "))
        return (dividend/divisor)
    
    except Exception as e:
        print (type(e))
        print (e)
        
print(divide_numbers())
```

##### Value error

##### Zero division error

#### Additional clauses
##### Specific exceptions
```
def divide_numbers():

    try:
        dividend = int(input("Enter the integer to divide: "))
        divisor = int(input("Enter the integer to divide by: "))
        return (dividend/divisor)
    except ValueError: 
        print ("Enter an integer.")
    except ZeroDivisionError:
        print ("Cannot divide by zero.")
    except Exception as e:
        print (type(e))
        print (e)

print(divide_numbers())
```

##### The else block
```
def divide_numbers():
    try:
        dividend = int(input("Enter the integer to divide: "))
        divisor = int(input("Enter the integer to divide by: "))
        result = dividend/divisor
    except ValueError: 
        print ("Enter an integer.")
    except ZeroDivisionError:
        print ("Cannot divide by zero.")
    else: 
        return (result)

divide_numbers()
```

##### The finally block
```
try:
    file = open("myfile.txt", "r")
    # Perform some operations on the file
except FileNotFoundError:
    print("The file could not be found.")
except IOError:
    print("An error occurred while reading the file.")
else:
    print("File contents:", file.read())
finally:
    if 'file' in locals():
        file.close()
        print("File closed.")
```

#### Raising exceptions
```
def create_profile(username, age):
    """Creates dictionary with user details
    and calls function to create homepage """
    try: 
        if age < 13:
            raise Exception("Account holders must be 13 or older.")
        user_dict = {"name": username, "age": age}
        print (user_dict)
        create_homepage(user_dict)
    except Exception as e:
        print (e)
```

```
def create_profile(username, age):
    """Creates dictionary with user details
    and calls function to create homepage """
    try: 
        if age < 13:
            raise ValueError("Account holders must be 13 or older.")
        user_dict = {"name": username, "age": age}
        print (user_dict)
        create_homepage(user_dict)
    except Exception as e:
        print(type(e))
        print (e)
```

#### Logging Exceptions

### Week 8: Python 1 - Testing, Debugging, and SDKs
#### Common frameworks for testing software in Python
* Robot
* pytest
* unittest
* doctest
* Testify
* nose2

#### The unittest module
```
import unittest
def add(x, y):
    return x + y
class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 5), 10)
if __name__ == '__main__':
    unittest.main()
```

#### Test fixtures
A **test fixture** represents the preparation needed to perform one or more tests, and any associated cleanup actions.
* The **setUp()** method is a special method you use in test cases. 
* The **setUpClass()** method is useful when you need to run expensive setup operations that can be reused by multiple tests.
* **tearDown()**
* **tearDownClass()**

In the following example, you call the setUp() method to initialize two variables with values 100 and 50 respectively. You also call the tearDown() method to clean up any resources you used during the test. In this case, it sets the variable values to None. 

```
import unittest
class ExampleTestCase(unittest.TestCase):
    def setUp(self):
        self.x = 100
        self.y = 50
    def tearDown(self):
        self.x = None
        self.y = None
    def test_addition(self):
        result = self.x + self.y
        self.assertEqual(result, 150)
    def test_subtraction(self):
        result = self.x - self.y
        self.assertEqual(result, 50)
if __name__ == '__main__':
    unittest.main()
```

##### [Organizing test code](https://docs.python.org/3/library/unittest.html#organizing-tests)

#### Assert methods
* assertEqual(x, y)
* assertNotEqual(x, y)
* assertTrue(x)
* assertFalse(x)

#### Knowledge Check
##### Which framework can you use to write tests in the form of examples embedded in docstrings?
* doctest

Wrong answers:
* Robot
* Testify
* unittest

##### What is the purpose of assert methods in the unittest module?
* They verify that the test result matches the result you were expecting.

Wrong answers:
* They represent the preparation and cleanup needed to perform tests.
* They orchestrate running your tests and provide the outcome to you.
* They run your code unit tests in verbose mode.

A test fixture represents the preparation and cleanup needed to perform tests. A test runner orchestrates the carrying out of tests and provides the outcome to you. Using the -v flag runs your tests in verbose mode.

#### Summary
##### Principles of testing
* Testing cannot prove there are no defects at all in your software.
* Testing every possible scenario is not feasible
* The earlier you identify defects, the less costly and uncomplicated they are to fix.
* Certain components of your software usually contain the highest number of defects.
* Repeating the same tests over and over will eventually stop finding new defects.
* You should tailor your testing to the specific context of your software.
* Just because you didn’t find any defects, it doesn’t mean your software is defect-free.
* Test automation doesn't replace manual testing.
* You should conduct your testing in an environment that closely matches the production environment.
* Automated testing can be faster and more efficient, but it doesn’t replace the creativity and intuition of manual testing.  
* Testing should be an ongoing activity throughout the software development lifecycle, not just a phase at the end.

##### Testing frameworks
* **Robot** is an open-source test automation framework that uses a keyword-driven approach to testing.
* **pytest** provides an efficient way to write and run tests. Pytest has an intuitive syntax that makes it convenient to write and read tests.
* With **doctest**, you can write tests in the form of examples embedded in the code docstrings. It's lightweight and convenient to use, but not as powerful as other frameworks.
* **Testify** is a lightweight testing framework that provides a streamlined syntax for writing and running tests.
* **Nose2** is an extensible and configurable framework, which includes a rich set of features.

##### Unittest
Unittest is a module for unit-testing Python provides in its standard library. It provides a wide range of testing tools for writing and running tests. Unnitest is widely used, which means there are many resources and examples available for those who are new to it.

Some of the main features of the unittest module include the following:
* A test case is an individual unit of testing. It checks for a specific response to a particular set of inputs.
* A test fixture represents the preparation needed to perform one or more tests, and any associated cleanup actions.
* A test runner orchestrates running your tests and provides the outcome to you.
* Assert methods verify that the test result matches the result you were expecting.

#### Software Development Kits (SDKs)
A software development kit (SDK) is a set of platform-specific building tools for developers. 

#### The AWS SDK for Python

#### Boto3
```
pip install boto3
```

#### Boto3 with the new AWS Common Runtime (AWS CRT) libraries
AWS CRT libraries provide better performance and minimal footprint for the functional area they implement.

```
pip install boto3[crt]
```

##### [AWS Common Runtime (CRT) libraries](https://docs.aws.amazon.com/sdkref/latest/guide/common-runtime.html)

####  AWS Cloud9 EC2 development environment
AWS Cloud9 makes temporary AWS access credentials available in the environment. This means you don't need to store your permanent AWS access credentials anywhere in the environment, or set up an EC2 instance profile for managing temporary AWS access credentials. In summary, when using Boto3 from a Cloud9 environment on an EC2 instance, you don't need to explicitly provide or manage credentials in your code.

#### Example of using Boto3 with Amazon EC2
```
import boto3
# Create EC2 client object
ec2 = boto3.client('ec2')

# Retrieve information about instances
response = ec2.describe_instances()

# Get the list of instances
instances = response['Reservations'][0]['Instances']

# Loop over each instance
for instance in instances:

# Print instance ID
    print(instance['InstanceId'])
```

### Week 9: System Design and Whiteboarding Essentials Part 1

#### Flowcharts
A flowchart is a diagram that uses standardized symbols to represent different steps of a process in sequential order. It is often used to identify the interactions in designs. Flowcharts are generally created using software tools, and the symbols used in the chart have specific meanings. For example, an oval represents a start or end point, a rectangle represents a process, and a diamond indicates a decision. 

#### Sketching
Sketching is an informal technique that involves drawing rough, freehand images to quickly explore and communicate ideas, iterate on designs, and refine concepts. Sketches can be created using pencil and paper or using digital drawing tools.

#### Rapidly sketched flowcharts
A rapidly sketched flowchart is a technique that combines the elements of both flowcharts and sketching. It involves creating a flowchart using simple, hand-drawn symbols and lines. With this approach, you can quickly explore different design options and can be more flexible than with a traditional flowchart. Rapidly sketched flowcharts can be created on paper or using digital tools.

#### Applying rapidly sketched flowcharts to a workflow
1. Define the problem or challenge to address.
2. Generate as many ideas as possible to address the challenge.
3. Sketch out the user flow for each idea using the rapidly sketched flowcharts technique.
4. Refine and iterate the designs to simplify and streamline the process.
5. Create a final flowchart outlining the entire user flow.

#### Benefits of rapidly sketched flowcharts
* Speed
* Flexibility
* Collaboration

#### Using Visual Thinking to Decompose Tasks
Decomposition is the process of breaking down a large problem or program into smaller parts or functions.

#### Mind mapping technique
A mind map is a graphical way to represent ideas and concepts. It is another visual-thinking tool that helps to structure information. It helps you to better analyze, comprehend, recall, and generate new ideas. Mind mapping also helps you break down big goals into smaller and more actionable tasks. Mind maps typically start with a main idea or theme in the center of the map, with related ideas branching out in all directions.

#### Steps to decompose tasks
1. Write the task that you want to decompose in the center of the page.
2. Identify the key components of the task, and then write or draw each component as a branch extending from the central task.
3. Continue to break down each component into smaller sub-components when needed. Write or draw each sub-component as a branch extending from the component it belongs to.
4. Use symbols, colors, or other graphical cues to differentiate between components and sub-components. This helps keep track of the different parts of the task, and how they connect to each other.
5. Take a step back to evaluate the overall picture and think about if any components can be combined or eliminated. Then, make adjustments as necessary.
6. When you have decomposed the entire task, use your diagram to create a plan of action. 

#### Knowledge Check
##### One of the visual thinking techniques typically starts with the main idea in the center of the page, with related subcomponents branching out in all directions. What is the name of this visual thinking technique that helps to organize and connect ideas?
* Mind maps

Wrong answers:
* Bar charts
* Scatterplots
* Venn diagrams

A mind map is a graphical way to represent ideas and concepts. It is a visual thinking tool that helps structure information. It helps you to better analyze, comprehend, recall, and generate new ideas. Mind maps typically start with a main idea or theme in the center of the map, with related ideas branching out in all directions.

Bar charts are used to represent numerical data, not to organize ideas. Scatterplots are used to represent the relationship between two variables, not to organize ideas. Venn diagrams are used to show the relationship between different sets of data, and not necessarily to organize ideas.

##### What is a rapidly sketched flowchart?
* A method of quickly drawing and refining flowcharts by hand

Wrong answers:
* A type of software used for creating a detailed diagram
* A process for creating animations and interactive graphics
* A technique for designing user interfaces

Rapidly sketched flowcharts involve using simple hand-drawn sketches to quickly capture and refine flowchart diagrams.

##### How can visual thinking help with the decomposition of tasks?
* It can help identify dependencies and relationships between different tasks.

Wrong answers:
* It can simplify assigning tasks to team members.
* It can automate the task decomposition process.
* It can help to minimize the need for collaboration with others.

Visual thinking can help identify dependencies and relationships between different tasks. This simplifies breaking down a task into smaller, more manageable components. Although visual thinking can make it easier to communicate tasks to team members, it does not necessarily make it easier to assign tasks. And it doesn’t minimize the need for collaboration. Collaboration is actually encouraged. Visual thinking also does not automate the task decomposition process.

#### Whiteboarding and Backend System Design
#### Pre-assessment

##### What is a whiteboarding session?
* A collaborative activity where developers use a whiteboard to discuss and visually illustrate a technical problem or solution

Wrong answers:
* A meeting where participants demonstrate the final solution and showcase the polished product to stakeholders
* A solo activity where one person presents their ideas on a whiteboard, and participants don’t contribute
* A meeting where developers gather feedback from stakeholders after the product has been developed

A whiteboarding session is not a solo activity. It involves collaboration and brainstorming with others. It is also not a final solution nor a meeting where developers gather feedback after the product has been developed. It is a starting point that helps to clarify problems and ideas, and identify potential solutions.

##### What is a key benefit of using whiteboarding as a developer?
* Whiteboarding permits developers to share their ideas with others.

Wrong answers:
* Whiteboarding ensures that the final code is bug free.
* Whiteboarding lets developers to skip the planning phase of development.
* Whiteboarding is a purely optional step that can be skipped.

One of the main benefits of using whiteboarding is that it makes it possible for developers to readily share their ideas with others. This can lead to better collaboration and more effective problem solving. Developers can use whiteboarding to discuss code logic, design patterns, and potential bugs. But it is not used to ensure that their code is bug free. Whiteboarding is an important step of the design process and should not be skipped.

##### What is a key benefit of whiteboarding during a brainstorming session?
* It permits participants to see and build on each other’s ideas.

Wrong answers:
* It ensures that all participants have an equal amount of speaking time.
* It eliminates the need to collaborate with your team members.
* It eliminates the need for note taking during the session.

Whiteboarding can help participants visualize and build on each other’s ideas, leading to more creative and effective solutions. Whiteboarding does not directly impact speaking time. Whiteboarding actually facilitates collaboration because it allows everyone to contribute the same ideas freely in real time. Although whiteboarding might help with note taking for individuals, it is not a primary purpose for brainstorming. 

##### What is security by design?
* A process that incorporates security requirements from the start of system design

Wrong answers:
* A process of retrofitting security features to a system after it has been built
* A strategy that focuses on implementing security features only in high-risk areas of a system
* A design approach that prioritizes usability and functionality over security

Security by design is a process that prioritizes security by incorporating security and compliance requirements into the design process from the outset. It aims to ensure that security is an integral part of the design and development process rather than an afterthought.

#### The purpose of a whiteboarding session
A whiteboarding session is a collaborative activity in which developers use a whiteboard to discuss and visually illustrate a technical problem or solution.

#### Benefits of using whiteboarding
Whether you are meeting with people virtually or in-person, whiteboarding has the following benefits: 
* It makes the session more dynamic than just screen sharing.
* It helps the participants to follow the content flow more easily.
* It invites conversations and opportunities to clarify whether your understanding is correct.
* It helps participants feel more connected and included.

#### Where to use whiteboarding
##### Planning and design
You can use whiteboarding to sketch out the architecture of the systems or applications, map out user flows, and brainstorm different design ideas. These system designs are considered backend system design (compared to the frontend system design that you will learn about in the wireframing, mock-up, and prototyping topics).

##### Problem solving
You can use whiteboarding to visualize a problem by breaking it down into smaller chunks. This helps you trace the flow of data more readily, identify where the issue might be, and come up with potential solutions.

##### Coding collaboration
You can use a whiteboard to discuss code logic and design patterns, architectures, and potential bugs. And you can use it to work through complex code problems with other developers without setting up a programming environment to do so.

##### Technical presentations and discussions
You can use whiteboarding to explain complex concepts and provide visual elements to support your presentation. This helps participants to better understand the technical details and encourages participants to engage in the discussion.

##### Glossary
###### Backend system design
Backend system design refers to the process of designing the server-side components of a system or an application, including data storage, business logic, and APIs. The backend system design is responsible for processing and managing data, implementing the business logic of the application, and interacting with other systems. The primary goal of the backend system design is to provide a reliable, scalable, and efficient infrastructure that can handle the processing and storage of large volumes of data.

###### Frontend system design
Frontend system design refers to the process of designing the client-side components of a system or an application, including the user interface, user experience, and presentation layer. The frontend system design is responsible for rendering the data processed by the backend system in a user-friendly manner. This permits users to interact with the application, and provide a seamless user experience. The primary goal of the frontend system design is to provide a user-friendly, responsive, and intuitive interface that meets the needs of the target audience and enhances the user experience.

#### How to succeed in a whiteboarding session
* Understand the problem that you are trying to solve
* Take notes during the session
* Communicate clearly and concisely
* Be open to feedback

#### Structuring your whiteboarding session

##### Time management
* Have a clear start and end time.
* Allocate enough time for each section of discussion (working backward from your total meeting time).
* Monitor your time by using a clock or a watch, or ask someone to give you signals.
* Build in breaks, especially for longer sessions.

##### Space management
* Use dividers, labels, and whitespace to help your audience distinguish the difference between elements.
* Follow 1/4, 1/2, 1/4 rule to divide up your whiteboard: 
 * 1/4 for introduction and agenda
 * 1/2 for main content
 * 1/4 for takeaways and action items

#### When to whiteboard
A whiteboarding session can be used to brainstorm and discuss potential problems and solutions early in the development process. Whiteboarding can also be used in almost all meetings. Take into consideration the size of your audience.

##### Small audience (1 to 3)
If you have a smaller audience, like one to three people, you can use whiteboarding to do the following:
* Pivot the meeting based on the customer’s needs.
* Encourage a collaborative discussion.
* Dive deeply into problems and break them down into smaller parts to gain a better understanding of the issues and identify potential solutions.

##### Large audience
If you have a larger audience, whiteboarding is a great medium when introducing a service on a lower-difficulty level. You can also use whiteboarding when you meet with stakeholders for the first time. Because you can visually illustrate your ideas and concepts, which can be more effective than describing them verbally.

#### Whiteboarding and Brainstorming

#### Using whiteboarding to lead effective brainstorming sessions
Whiteboarding can have a significant impact on leading an effective brainstorming session by providing a visual representation of the ideas being discussed. 

##### Encouraging participation
Whiteboarding creates a shared space to discuss and generate ideas. Participants feel more comfortable contributing in a shared space.

##### Organizing ideas
Using whiteboarding can help to categorize and organize ideas and identify themes and patterns that help you to develop a project plan and determine clear next actions.

##### Facilitating collaboration
With whiteboarding, everyone can contribute ideas freely in real time. This can lead to more innovative solutions and greater buy-in from the team.

##### Encouraging visual thinking
Visual thinking is an important aspect of effective brainstorming. By using a whiteboard, participants can draw diagrams, charts, and other visual aids to help explain their ideas and communicate complex concepts more effectively.

##### Iterating ideas and solutions
Brainstorming sessions often involve multiple iterations of ideas and solutions. By using a whiteboard, participants can quickly make changes and revisions to the ideas being discussed. This leads to a more refined and effective solution.

#### Tips for Whiteboarding

#### Focusing on your purpose
The most effective whiteboarding sessions have a clearly defined agenda, structure, and purpose. To set the tone of the session and keep participants on track, write on the board the goal, purpose, or any issues to be resolved and what topics to focus on during these sessions.

##### Do
* Consider accessibility during whiteboarding by using high-contrast colors against the background. For example, in a virtual setting, a black background usually provides a better range of contrasting colors than white background for people who have low vision.
* Practice, practice, practice. Practice your storytelling and whiteboarding skills (that is, drawing and talking) offline to help you to improve your technique, find your own style, and boost your confidence.
* Prepare ahead of time. Make sure that you have a clear understanding of the topic that you will be presenting, and create an outline. Follow the 75/25 rule, where you might draw 75% of the topic before the meeting and leave 25% of the new content to be added in the meeting.
* Keep it simple and concise when whiteboarding. Avoid using overly technical jargon or complex diagrams that might confuse your audience.
* Engage your audience by asking them questions, encouraging them to participate, and asking for their feedback. Also, if you are doing whiteboarding in person, remember to establish eye contact and turn toward the audience when you are talking.
* Mindfully pause when you are actively drawing or writing on the board.
* Use color only for emphasis, not to impart meaning.
* Create a parking lot for great ideas that arise during the discussion but are not part of the current topic. This keeps discussions on track and moving forward. You can revisit everything in the parking lot at the end of the meeting.

##### Don't
* Don’t rush. Take your time when whiteboarding. Rushing through your ideas can cause confusion and make it difficult for your audience to follow along. Permit new drawers to take their time, too.
* Don’t talk at the board during in-person whiteboarding sessions; turn around to face your audience first.
* Don’t overload your whiteboarding. Avoid using too many visual elements and writing too much. This can be overwhelming and make it difficult for your audience to retain information. 
* Don’t be unprepared. Being unprepared can lead to mistakes and make it difficult to convey your ideas effectively.

#### Additional whiteboarding techniques

##### Annotating
These are tips for annotating:
* Use a single bright color (for example, orange).
* Use annotation on large and complex architectures to make notes.
* Use annotation on the AWS Global Infrastructure map to explain how points of presence (PoPs) work.

##### Diagramming
These are tips for diagramming:
* Use different colors to emphasize or distinguish different components.
* Use diagramming to explain a complex or abstract concept.
* Use diagramming when you have simple architectures that you can expand on.
* Use diagramming to explain a service.
* Use diagramming when you want to draw anything freehand.

**The whiteboard is a tool that facilitates an effective meeting. You are still in control of the conversation, so remember to work backward from the customer’s needs in an engaging, collaborative way.**

#### Common Tools Used for Whiteboarding

##### Physical whiteboard
A physical whiteboard is still the primary tool used in whiteboarding. It’s simple to use and can be used in many different settings, such as classrooms and offices. It is often considered a versatile and accessible tool for all levels of tech expertise. 

**Reasons to use a physical whiteboard:**
* Easy to use and intuitive, familiar to most people
* Great for collaborative brainstorming sessions and group discussions
* Can be used in any setting with no need for additional hardware or software
* Can be easily erased and modified

##### Draw.io
Draw.io is a diagramming tool that can be used to create flowcharts, process diagrams, and other visual representations of complex ideas. It has a wide range of templates and shapes to choose from. You can use the provided freehand drawing tool for whiteboarding.

**Reasons to use Draw.io:**
* Offers a wide range of tools and features for creating complex diagrams and visualizations
* Can be used both in person and remotely
* Content easily shared and modified
* Free to use

##### Epic Pen
Epic Pen is a digital whiteboarding tool that makes it possible for users to draw and annotate on their screens in real time. It can be used to draw over any software. It’s often used in remote or virtual collaboration settings. Epic Pen is particularly useful for those who want to collaborate on designs or share ideas visually in real time.

**Reasons to use Epic Pen:**
* Can be used with any application or software
* Allows users to draw and write directly on their computer screen
* Great for remote collaboration and virtual whiteboarding
* Easy to use with no necessary learning curve

##### Bluescape
Bluescape is a cloud-based whiteboarding tool that allows teams to collaborate in real time on a virtual canvas. Bluescape uses helpful features such as sticky notes to directly add feedback, callouts, and annotations to your board. You can also upload images, videos, files, or documents to your whiteboards, so you have everything in one place.

**Reasons to use Bluescape:**
* Offers a wide range of collaborative features for remote teams
* Great for large-scale projects and complex diagrams
* Content easily shared and saved digitally
* Customizable interface and tools

##### PowerPoint
PowerPoint can be used as a basic whiteboarding tool by creating a new presentation and using its drawing and text tools to sketch out ideas, diagrams, and other graphical elements. 

**Reasons to use PowerPoint:**
* Widely used and familiar to most people
* Offers a variety of tools for creating presentations and diagrams
* Content easily shared and modified
* Can be used both in person and remotely

#### Security by design
Security by design is an approach that considers security from the very beginning and integrates it throughout the development process.

#### The importance of security and compliance requirements

##### Applications are a primary target for hackers and cybercriminals.
Application design should include the strategies that protect the application and its users from unauthorized access, data breaches, and other security threats. By integrating security measures into the design, you can help to mitigate potential risks and safeguard sensitive user data. 

##### There are regulations and standards that applications must comply with.
For example, applications in the healthcare industry must comply with many healthcare regulations. Examples include the following:
* Health Insurance Portability and Accountability Act (HIPAA)
* General Data Protection Regulation (GDPR) if your application will be used in the European Union
* Payment Card Industry Data Security Standard (PCI DSS)
* Accessibility guidelines

Failure to follow these compliances can result in fines, legal actions, and damage to your client’s reputation.

##### You can save money in the long run.
Fixing security vulnerabilities or noncompliance issues after the application has been developed can be very costly and time consuming. Addressing these issues during the design and wireframing stage can help to prevent expensive and time-consuming rework.

##### You can ensure a positive user experience.
Users expect applications to be secure, reliable, and easy to use. Implementing security and compliance measures into the design can help build user trust and confidence in the application.

#### Identifying potential security and compliance requirements

##### Scenario
You are designing a new online-banking platform. Your task is to identify potential security and compliance requirements that should be considered during the initial system design.

##### Tasks
Using any whiteboarding tool of your choice, take notes while thinking through the following questions:
* What kind of personal data will be collected from users?
* What regulations must be followed—for example, GDPR, HIPAA, PCI DSS, and so on?
* What kind of security measures will be required (for example, encryption, firewalls, multi-factor authentication, and so on)?
* How will you ensure the privacy and security of user data?

##### What are some potential security threads that an online banking platform might face?
* Phishing attacks, 
* malware infections, 
* password theft, 
* and unauthorized access.

##### What are some compliance requirements that an online banking platform must meet?
* PCI DSS
* GDPR
* Bank Secrecy Act (BSA)

##### How might you incorporate security and compliance requirements into your system design during whiteboarding?
* Two-factor authentication
* Encryption
* User access control
* Data retention policy

#### Activity: Navigating AWS Architecture Center and Creating an Architecture Diagram

##### [AWS Architecture Center](https://aws.amazon.com/architecture/)

#### Creating an architecture diagram

##### Amazon S3 for hosting the static resources
**Why:** Amazon S3 provides low latency, high throughput, and high durability. Amazon S3 automatically scales for storage needs.

##### CloudFront for content distribution
**Why:** CloudFront provides abstraction over Amazon S3 so the S3 endpoint can be made private, to enhance security. CloudFront handles HTTP error codes to redirect to a specific location, and CloudFront makes web applcications available over HTTPS. 

##### Lambda@Edge for creating serverless functions
**Why:** Lambda@Edge allows the use of Amazon S3 with multiple subdirectories and conditional redirection to subdirectories (for example, a website supporting multiple languages).

**Note:** Lambda@Edge is a feature of Amazon CloudFront that lets you run code closer to users of your application, which improves performance and reduces latency.

##### Route 53 for domain name resolution
**Why:** The CloudFront URL is not very user friendly, so using Route 53 permits you to map custom domain names to CloudFront.

#### Key advantages of using Amazon S3 for static web hosting
##### Serverless
Content is hosted in Amazon S3. This eliminates the need to purchase a web server or virtual machine, which require 24/7 up-keep for the web application to be available all the time. 

##### Availability
High availability is driven by using AWS offerings such as CloudFront, Amazon S3, and Lambda@Edge. 

##### Auto scaling
Amazon S3 automatically scales as needed.

##### CDN advantages
Contents are served through CloudFront (an AWS CDN service), encompassing all benefits associated with a CDN.

##### Cost
Amazon S3 is relatively cheaper compared to other hosting options. Amazon S3 is charged based on what is being used. This is cheaper than hosting the application on a dedicated server because Example Hospital has to pay based on the server's uptime regardless of whether the web application being used.

#### Knowledge Check

##### What is the purpose of a whiteboarding session?
* To identify potential problems and solutions early in the development process

Wrong answers:
* To create a final, polished version of the product
* To test the functionality of a product and find bugs
* To gather feedback from stakeholders after the product has been developed

##### Which of the following is a benefit for developers to conduct whiteboarding sessions?
* To identify potential problems and solutions early in the development process

Wrong answers:
* To create a final and polished version of the product
* To test the functionality of a product and find bugs
* To gather feedback from stakeholders after the product has been developed

##### What is AWS Application Composer? 
* A service that is used to create and deploy serverless applications

Wrong answers:
* A service that is used to build AWS architecture diagrams
* A service that is used to build a wireframe of the user interface of a system
* A service that is used to draft system design during whiteboarding

AWS Application Composer is a visual designer that you can use to build your serverless applications from multiple AWS services. As you design, Application Composer automatically develops your infrastructure as code (IaC) templates, following AWS best practices. It’s not intended for creating AWS architecture diagrams, whiteboarding system design, or wireframing a user interface.

##### Which of these is an example of a security and compliance requirement that must be considered during the design process?
* Encryption of sensitive data during transmission and at rest

Wrong answers:
* Use of bright color schemes to enhance user experience
* Integration with social media platforms to increase user engagement
* Allowing multiple user logins with the same credentials

Encryption of sensitive data during transmission and at rest is a critical security requirement that should be considered during the design process to prevent unauthorized access and protect sensitive information. 

#### Summary

##### What is a whiteboarding session?
A whiteboarding session is a collaborative activity in which developers use a whiteboard to discuss and visually illustrate a technical problem or solution. 

##### Benefits of using whiteboarding and when to use whiteboarding
Whiteboarding is a valuable tool for developers that can be used in various scenarios such as planning and design, problem solving, coding collaboration, and technical presentations. Whiteboarding has several benefits over screen sharing, including the following:
* Making the session more dynamic
* Helping the participants to follow the content flow more readily
* Inviting conversations and clarification
* Making participants feel more connected and included

Incorporating whiteboarding can enhance productivity and collaboration between team members. 

##### How to succeed in a whiteboarding session
To succeed in a whiteboarding session, it's important to be prepared by knowing the topic, understanding the problem, and having a clear idea of the solution. You should also communicate clearly and concisely with the participants, actively listen to their ideas, and provide clear explanations of your own. Use the whiteboard effectively by organizing your thoughts and drawing diagrams. Be open to feedback and suggestions from others. 

Additionally, maintain a positive attitude, stay engaged in the sessions, and practice regularly to improve your whiteboarding skills. By following these tips, you can have successful whiteboarding sessions and contribute effectively to your team's work. 

##### How to structure a whiteboarding session
There are two parts to structuring a whiteboarding session: the first one is time management and the second one is space management: 
* **Time management:** This involves allocating enough time for each stage of the process by working backwards from your total meeting time, setting clear goals and timelines, and avoiding getting stuck on a single issue. 
* **Space management:** This includes using the whiteboard effectively to convey information and keep the session organized. Use dividers, labels, and whitespace to help your audience distinguish the difference between elements.

##### Tips for whiteboarding

##### Dos
* Consider accessibility during whiteboarding by using high-contrast colors against the background. For example, in a virtual setting, a black background usually provides a better range of contrasting colors than white background for people who have low vision.
* Practice, practice, practice. Practice your storytelling and whiteboarding skills (that is, drawing and talking) offline help you to improve your technique, find your own style, and boost your confidence.
* Prepare ahead of time. Make sure that you have a clear understanding of the topic that you will be presenting, and create an outline. Follow the 75/25 rule, where you might draw 75% of the topic before the meeting and leave 25% of the new content to be added in the meeting.
* Keep it simple and concise when whiteboarding. Avoid using overly technical jargon or complex diagrams that might confuse your audience.
* Engage your audience by asking them questions, encouraging them to participate, and asking for their feedback. Also, if you are doing whiteboarding in person, remember to establish eye contact and turn toward the audience when you are talking. 
* Mindfully pause when you are actively drawing or writing on the board.
* Use color only for emphasis, not to impart meaning.
* Create a parking lot for great ideas that arise during the discussion but are not part of the current topic. This keeps discussions on track and moving forward. You can revisit everything in the parking lot at the end of the meeting.

##### Don'ts
* Don’t rush. Take your time when whiteboarding. Rushing through your ideas can cause confusion and make it difficult for your audience to follow along. Permit new drawers to take their time, too.
* Don’t talk at the board during in-person whiteboarding sessions; turn around to face your audience first.
* Don’t overload your whiteboarding. Avoid using too many visual elements and writing too much. This can be overwhelming and make it difficult for your audience to retain information. 
* Don’t be unprepared. Being unprepared can lead to mistakes and make it difficult to convey your ideas effectively.

##### Why are security and compliance requirements important during system design?
Considering security and compliance requirements during the initial stage of system design is important for the following reasons:
* Applications are a primary target for hackers and cybercriminals.
* There are regulations and standards that applications must comply with.
* You can save money in the long run because fixing security vulnerabilities or noncompliance issues after the application has been developed can be very costly and time consuming.
* You can ensure a positive user experience because users expect applications to be secure, reliable, and easy to use.

##### What do AWS architecture diagrams do?
Architecture diagrams are a great way to communicate your design, deployment, and topology. 

###### Visualize the infrastructure
An architecture diagram helps you visualize the entire infrastructure needed to support your application. It shows the various components of your application, how they interact with each other, and the AWS services required to support them.

###### Identify potential issues
Creating an architecture diagram can help you identify potential issues with your infrastructure design early in the development process. For example, you might notice that you need to add additional resources to handle traffic spikes or that you have a single point of failure in your system.

###### Plan for scalability
Architecture diagrams can help you plan for scalability by showing you how your infrastructure can be expanded to handle increased traffic or data volume. This can help you make decisions about which AWS services to use, and how to configure them.

###### Collaborate with stakeholders
Architecture diagrams can help you communicate your infrastructure design to stakeholders, such as clients, developers, and project managers. This can ensure that everyone is in unison, and that the infrastructure meets the needs of the business.

##### What is AWS Application Composer?
AWS Application Composer is a visual designer that you can use to build your serverless applications from multiple AWS services. As you design, Application Composer automatically develops your IaC templates, following AWS best practices.

#### Additional Resources

##### [AWS Architecture Center](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&amp;cards-all.sort-order=desc&amp;awsf.content-type=*all&amp;awsf.methodology=*all&amp;awsf.tech-category=*all&amp;awsf.industries=*all&amp;awsf.business-category=*all)

##### [AWS Application Composer](https://aws.amazon.com/application-composer/)

### Week 10: System Design and Whiteboarding Essentials Part 2

#### Frontend Wireframing in System Design

#### Summary
##### Native applications and web applications 
Native applications are built for a specific platform or device type. The user must install the appropriate software version on their device of choice. Web applications are delivered over an internet browser. Users don't need to install them on their devices. 

##### Low-fidelity and high-fidelity design 
Low-fidelity designs are the initial quick overview of a future system or an application and help team members evaluate design concepts and ideas. The two elements of a low-fidelity design are the speed of creation and the simplicity of design. 

High-fidelity designs closely match the final result of a product’s design. Visual style, content, and any animated transitions work together to make high-fidelity assets look and work as close to the final product as possible. They are more realistic and can be used to test the functionality and usability of the design with users.

##### What is wireframing?
Wireframing is the process of creating a visual representation of the layout, structure, and functionality of a digital product, such as a mobile application or a website. Remember, a wireframe is just a sketch or a blueprint of a system or an application. It doesn't have to look exactly like the final product. Keep it simple. You generally don't use color or images in your wireframes. 

##### What is pseudocode?
Pseudocode is a high-level, plain language description used to describe the logic of a computer program or algorithm. It’s an informal way of writing code that is simple for humans to read and understand, without worrying about the specific syntax of a programming language.

##### Best practices for writing pseudocode
Here are some best practices and tips for you to write pseudocode: 
* Keep it simple and easy to understand.
* Use proper syntax and indention.
* Use descriptive variable names.
* Use comments.
* Keep it modular.
* Don't get stuck in syntax.

##### Code writing process
Writing code is a goal-oriented process. Here are the general steps to write an application:
1. **Planning:** Before you start writing code, it’s important to plan out what you are going to build. 
2. **Design:** This involves creating a high-level architecture for your code, determining what data structures you will use, and creating detailed diagrams and documentations. You will then begin writing pseudocode. 
3. **Implementation:** This is where you actually write the code. 
4. **Testing:** Once you have written your code and checked for any syntax errors, you are ready to start testing. 
5. **Debugging:** If you find any bugs or errors during testing, it’s important to debug them. 
6. **Maintenance:** This involves fixing bugs and errors that arise, updating your code to accommodate changes in the system or environment, and improving the performance and efficiency of your code over time.

##### Best practices for code writing
Here are some best practices for code writing:
* Use meaningful and descriptive names for variables, functions, and classes, and avoid overly complicated code.
* Avoid writing the same code twice by reusing code snippets, functions, and libraries. 
* Write modular and maintainable code, and avoid using global variables. 
* Use version control tools like Git to keep track of changes to your code.
* Include comments and documentation to explain the purpose and functionality of your code.

#### Frontend Mockups and Prototypes

#### Summary
##### What is a mockup?
A mockup is a more advanced visual representation of a digital product. It’s considered the next and more in-depth iteration of the wireframe outline. Mockups focus on the visual components in detail and show thought-out visuals, typography, and rich-colors and give viewers a realistic impression of what the final page or application will look like.

Mockups are neither interactive nor clickable. Mockups are typically used between wireframes and prototype to help developers and stakeholders get a better sense of how the product will look and feel and identify any potential issues or opportunities for improvement before moving on to prototyping.

##### Characteristics of a mockup
A mockup typically includes additional visual details, such as the following: 
* Colors, styles, graphics, and typography 
* Styled buttons and text 
* Navigation graphics 
* Component spacing

##### What is a prototype?
The purpose of the prototyping is to simulate the user experience. For this reason, your prototype should be clickable. You don’t need to make notes of what each element means and how each feature works on a prototype, you just simply click on the interface and something will happen, just like a real website or an application.

##### Characteristics of a prototype
* It has a functional interface. This means that you can click buttons on the page or screen and something will happen. 
* It is used to test functionality before you release the final product. 
* It closely represents the final product, functionally and visually. 

### Week 11: Software Development Lifecycle

#### The software development lifecycle
The software development lifecycle (SDLC) provides a well-defined list of all the operations necessary for planning, creation, and deployment of software. The main steps of the SDLC are as follows:
* Requirement analysis
* Planning 
* Architectural design
* Software development
* Testing
* Deployment

##### The 7th step: Maintenance
Despite not always being included as a step in the SDLC, maintenance should be considered a part of the software development lifecycle. The aim of this step is to ensure that the requirements and the customer needs are continuously satisfied. The maintenance tasks include the following:
* Corrections of errors linked to unplanned behavior of the application or unplanned situations encountered by users.
* Updates performed on the application to better fit the user needs that might vary in time.
* New options or features added.

#### SDLC benefits
When developing a software application, two aspects often surface as important concerns: cost and quality. By following the SDLC, you can address these aspects even though they may appear, at times, to be competing priorities. Using the SDLC offers several benefits, including the following: 
* Improved project and resource management
* Quality control
* Increased productivity
* Reduced costs

#### Source control
Whether you are writing an application alone, or collaborating with a team, source control is a vital component of the development process. Using the SCM system, you can track code changes, see a revision history, and revert to previous versions of a project when needed. You can use SCM systems to collaborate on code with your team and isolate your work until it is ready. You can also quickly troubleshoot issues by identifying who made changes and what the changes were. SCM systems help streamline the development process and provide a centralized source for all your code.

**Git is an open-source distributed source code management system. With Git, you can create a copy of your repository, known as a branch.**

#### AWS CodeCommit
AWS CodeCommit is a managed SCM system that hosts Git repositories and works with all Git-based tools.

AWS CodeCommit will store code, binaries, and metadata in a redundant fashion with high availability. You will be able to collaborate with local and remote teams to edit, compare, sync, and revise your code.

#### SDLC Methodologies

#### The waterfall model
The waterfall model was the first process model to be introduced. In a waterfall model, each phase must be completed before the next phase can begin, and there is no overlapping in the phases. 

All these phases cascade into each other, and progress is seen flowing steadily downward (like a waterfall). A phase is started only after the the goals for the previous phase are met; phases do not overlap. Some examples of when to use the waterfall model include projects that have the following attributes:
* The product definition is stable.
* They have short, clearly documented, fixed requirements.
* Resources with expertise are available to support the project.

#### The agile model
Project management also uses a form of agile, and while similar, this reference is to the SDLC agile model. The agile model focuses on process adaptability and customer satisfaction by rapid delivery of a working software product. Agile methods break the product down into small incremental builds. These builds are provided in iterations. Each iteration typically lasts from about 1–3 weeks. Iteration involves cross-functional teams working simultaneously on various areas, such as the following:
* Planning
* Requirements analysis
* Design
* Coding
* Unit testing
* Acceptance testing

#### Test-driven development (TDD)
TDD is a software development process which relies on software requirements being converted into test cases before software is fully developed. It focuses on tracking all software development by repeatedly testing the software against all possible test cases. This is opposed to first developing the software, and then testing it later. 

The three principles for writing unit tests include the following:
1. No production code should be written if you do not have the proper unit test to verify that your code works. This means that you need to ensure that your test can fail.
2. Only one unit test at a time should be written. A unit test that does not compile is considered as a failure.
3. Write the code that will help the unit test to pass and nothing else.

#### Other software development methodologies

##### Iterative development
In contrast to the agile method that uses cycles, iterative development split the product into units that will be developed in parallel. Then, once the units are be ready, they will be assembled to create a minimum viable product. This minimum viable product will be tested and then another iteration of the product will be performed. This is done by splitting the product again into units and performing parallel development.

In the iterative model, the product is divided into units. Each unit is developed in parallel. Once merged, the product is tested and the next iteration split again the different features and iterates based on the feedbacks from the testing. Once the iterations are done and the quality is satisfying, the product can be deployed.

##### The prototype model
The prototype model combines a prototyping step and an iterative process. During the prototyping step, the development team creates prototypes and asks customers for their feedback. Using the feedback, the prototype is refined until it fully meets expectations. Once done, the iterative process begins and the product is developed following the usual steps of the SDLC.

##### Rapid application development model
The rapid application development model is very close to the prototype model. Despite it also having a cycle of prototype and refinement, the requirements are known since the beginning. However, in the prototype model, requirements are added and refined during the prototype iterations.

##### Dynamic systems development model
Based on the rapid application development model, the dynamic systems development model goes beyond by including feasibility, foundations, and governance.

##### Big bang model
The big bang model is a method that does not specify any process to release the product. Using this model, the development team only needs to agree about timing, effort, and resources allocated to the development of the product.