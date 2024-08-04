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
### Week 7: Python 1 - Logging and Error Handling
### Week 8: Python 1 - Testing, Debugging, and SDKs
### Week 9: System Design and Whiteboarding Essentials Part 1
### Week 10: System Design and Whiteboarding Essentials Part 2
### Week 11: Software Development Lifecycle
