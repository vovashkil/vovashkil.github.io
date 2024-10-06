###### back to AWS Cloud Institute repo's root [aci.md](../aci.md)
###### back to repo's main [README.md](../../../README.md)
# Object Oriented Programming 

## Programming Paradigms

### Pre-assessment
#### What is a programming paradigm? 
* Programming paradigms establish the style and structure of the code.  

Wrong answers:
* Programming paradigms establish the class type and attributes of the code.  
* Programming paradigms establish the syntax for all programming languages.  
* Programming paradigms establish the functions that programs use.

#### Python supports object-oriented programming. Which other programming paradigms does Python support? (Select THREE.) 
* Imperative 
* Functional
* Procedural  

Wrong answers:
* Declarative
* Reflective

Python doesn’t support declarative programming (Java does), reflective programming (Ruby does), or component-oriented programming (C Sharp does).

#### Which sentence is true about object-oriented programming (OOP)? 
* OOP is used to write classes, attributes, and methods.  

Wrong answers:
* OOP relies on predefined classes, like strings and integers. 
* OOP is used for problems that require mathematical transformations. 
* OOP is used to give commands in a step-by-step manner.

While using OOP, you can benefit from predefined classes, but you are not restricted to those. You can also create your own classes.  

Functional programming is used for problems that require mathematical transformations. 

Imperative programming gives commands in a step-by-step manner.

### The Four Main Programming Paradigms
#### Imperative programming
*Imperative programming* is used to deliver directions or give commands in a detailed, step-by-step manner. The order in which the commands are given is important.

#### Functional programming
Functional programming is used for problems requiring mathematical transformations of values, filtering information, mapping, and reductions. It is based on lambda calculus. It emphasizes immutability and the use of functions that produce consistent outputs for the same inputs. It involves higher-order functions and tools like map, filter, and reduce. 

#### Procedural programming
Procedural programming is a subtype of imperative programming and is also a stateful model. It focuses on procedures and routines, and you write the code in the order it will be ran from top to bottom.  

#### Object-oriented programming
Object-oriented programming (OOP) is a programming paradigm that uses objects that are based on real-world objects. In this programming paradigm, everything in your project gets organized as classes and then as tangible and intangible objects. OOP is used for problems that involve many interrelated objects with certain attributes that can change over time, depending on certain conditions. With OOP, you can create classes, define inheritance hierarchies, and achieve polymorphism.

### Choosing a paradigm
A data processing pipeline can be a mix of programming styles. You can use the imperative style for filtering and transforming raw data. Functional programming can be used for data transformation like mapping and reducing operations. OOP can be used for organizing code in reusable components.

### Knowledge Check

#### What is a purpose for which a developer might use object-oriented programming (OOP)? 
* For organizing code in reusable components

Wrong answers:
* For writing scripts to extract information from webpages to monitor the pricing of products
* For writing code that changes a program's state
* For data transformation, like mapping and reducing operations

You can use imperative programming for writing code that changes a program's state. These programs are a sequence of steps that the computer takes to solve a task. 

You can use functional programming for data transformation like mapping and reducing operations. It also involves other higher-order functions and tools like a filter.

You can use procedural programming for writing scripts to extract information from webpages to monitor the product pricing. It can also be used for collecting data for research. 

#### Which programming paradigm is used for problems that require mathematical transformations of values? 
* Functional programming

Wrong answers:
* Imperative programming
* Procedural programming
* Object-oriented programming (OOP)

Functional programming is used for problems requiring mathematical transformations of values.

Imperative, procedural, and object-oriented programming are not used for problems requiring mathematical transformations.

#### What is true about the programming paradigms? 
* With Python, developers can choose the best style for each situation.

Wrong answers:
* Only one programming paradigm can be used for a whole project.
* Developers can agree on the best coding style.
* The paradigms solve problems in the same way. 

When coding in Python, developers have the choice of combining styles. They do not have to commit to one style for their whole project.

There is no all-time best coding style that works for all instances, and each developer might have a preference. 

Each paradigm has its own way of solving problems, performing tasks, organizing code, and expressing computations.

### Summary
#### Programming paradigms
There are four programming paradigms in Python: imperative, functional, procedural, and object-oriented. A programming paradigm is an approach to programming that dictates the style and structure of the code.   
* **Imperative programming** is used to deliver directions or give commands in a detailed, step-by-step manner. It takes a how-to-solve approach. The order in which the commands are given is important. 
* **Functional programming** is used for problems requiring mathematical transformations of values, filtering information, mapping, and reductions. It takes a what-to-solve approach. It emphasizes immutability and the use of functions that produce consistent outputs for the same inputs. It involves higher-order functions and tools like map, filter, and reduce.
* **Procedural programming** is a subtype of imperative programming and is also a stateful model. It focuses on procedures and routines, and you write the code in the order it will run from top to bottom.  
* In **Object-oriented programming (OOP)**, everything in your project gets organized as classes and then as tangible and intangible objects.

## Classes and Objects

### Pre-assessment
#### Which option represents the correct Python syntax if a developer were to create a Dog class?
* class Dog:

Wrong answers:
* class(Dog)
* classDog
* class __Dog__

The correct syntax for creating a class is the keyword class, followed by a space, followed by the name of the class, and then followed by a colon. 

The other three options are incorrect. The second option includes unnecessary parentheses, the third is missing the space and colon, and the fourth includes unnecessary underscores before and after the class name.

#### What is an object in Python? 
* An object is an instance of the class.

Wrong answers:
* An object is a function that performs specific tasks.
* An object is a variable that stores essential data.
* An object is a method to call functions.

#### What are operations within a class called? 
* Methods

Wrong answers:
* Attributes
* Instances
* Objects

Methods in a class indicate what the class can do. They are also called operations, behaviors, or functions. 

Attributes are the characteristics within a class. They are also called properties or variables. 

Classes are used to create objects, also known as instances.

### Using Classes and Objects in Python

### OOP
**OOP** is a programming paradigm in which everything in a project is organized as classes and then as objects, which are based on real-world objects. The objects can be tangible, like people, cars, or animals. They can also represent intangible things such as a zip code or an electronic ticket.

### Classes and objects
A class is a blueprint, which is a detailed drawing with instructions to build something, like a house. 

A Python object (also known as an **instance** of a class) has the following: 
* **Attributes**, also known as **properties** or **variables**, can describe characteristics of an object such as name, color, speed, size, phone number, address, or date. They can be any data type, such as a string, integer, float, Boolean, list, or dictionary. Remember that a variable is a container for storing data values. 
* **Methods** are blocks of code that perform a specific task, like adjusting speed or changing color. A method is a function that is attached to an object.

### Class and instance variables
* **Class variables** are shared by all instances or objects of the classes. A change in the class variable will change the value of that property in all of the objects of the class. 
* **Instance variables** are unique to each instance or object of the class. A change in the instance variable will change the value of the property in that specific object only.

### Defining class variables and instance variables

```
class Car: 
    number_of_wheels = 4 # Class variable

    def __init__(self, body_style, color): 
        self.body_style = body_style # Instance variable
        self.color = color # Instance variable
```

### Incorrect use of class variables
The best practice for code readability, reliability, and consistency is to access class variables by their class name and not by object references.

```
class Car: 
    fleet_size = 0 # Another class variable
    number_of_wheels = 4 

    def __init__(self, body_style, color): 
        self.body_style = body_style
        self.color = color 

car_one = Car("SUV", "blue")
car_one.fleet_size = car_one.fleet_size + 1 # Incorrect use of class variable 

print(f"Car class fleet size: {Car.fleet_size}")
print(f"Fleet size accessed from car one: {car_one.fleet_size}")
```

### Correct use of class variables
It would be more efficient if the Car class managed its fleet size internally and automatically. A more programmatic approach and correct usage of class variables is shown in the following example.

```
class Car: 
    fleet_size = 0 # Another class variable
    number_of_wheels = 4 

    def __init__(self, body_style, color): 
        self.body_style = body_style
        self.color = color 
        Car.fleet_size += 1 # Automatically increment fleet_size when a Car instance is created

    # The destructor method __del__ is called when an object is deleted
    def __del__(self):
         Car.fleet_size -= 1 # Automatically decrement fleet_size when a Car instance is deleted
```

In the previous example, the class variable fleet_size is now updated in the __init__ method. This means every time a new Car object is created, the fleet_size value will automatically be incremented. 

When objects are deleted in Python, the destructor method __del__ is called. Here, the fleet_size value is decremented in the destructor whenever a Car object is deleted. 

Now the Car class manages its fleet size automatically and internally. 

### Class and object relationship
Consider a real-world example using classes, objects, and variables. You could create an Employee class with attributes or properties like ID, Salary, and Department, and actions or behaviors like Tax on Salary and Salary per day. 

You would normally capitalize a person's first name according to English language rules. However, Python convention is to use CapitalizedWords for class names. It is also Python convention to use lower_case_with_underscores for class instances (objects), other variable names, and methods. However, if you are writing someone's name as part of a string, then you would capitalize it.

When naming instances of the Employee class for the employees Jorge and Mary, it is convention to write them in lowercase letters: jorge and mary.

### Benefits of objects and classes 
* You can organize your code in a manageable way. 
* You can make your code more reusable. 
* You can maintain your code more efficiently. 
* You can create complex applications in Python. 

This is why classes and objects are considered the building blocks of object-oriented programming. 

### Class Methods and Static Methods

### Types of Methods
* instance methods
* class methods
* static methods

### Methods purpose
Methods act as an interface between a program and the properties of a class in the program. 

These methods can either alter the content of the properties or use their values to perform a particular computation. 

### Definition and declaration 
A **method** is a group of statements that performs some operations and might or might not return a result. 

#### Method parameters 
Method parameters make it possible to pass values to the method. In Python, the first parameter of the method should ALWAYS be self (as you have learned previously), followed by the remaining parameters. 

#### Return statement 
The return statement makes it possible to get the value from the method. 

### Class methods and syntax 
Class methods work with class variables and are accessible using the class name rather than its object. Because all class objects share the class variables, class methods are used to access and modify class variables.

Class methods are accessed using the class name and can be accessed without creating a class object.

To declare a method as a class method, use the decorator **@classmethod**. Using a decorator gives you the ability to wrap one function with another function to enhance and extend the behavior. 

The variable **cls** is used to refer to the class just like **self** is used to refer to the object of the class. You can use any other name instead of cls, but cls is used as per convention.

**Just like instance methods, all class methods have at least one argument, cls.**

The syntax is as follows.

```
class MyClass:
    class_variable = "educative"

    @classmethod
    def demo(cls):
        return cls.class_variable
```

The following is a code implementation for class methods.

```
class Car:
    number_of_wheels = 4 # Class variable

    def __init__(self, body_style):
        self.body_style = body_style # Instance variable

    @classmethod
    def get_number_of_wheels(cls):
        return cls.number_of_wheels

print(Car.get_number_of_wheels())
```

Output
```
4
```

The **@classmethod** decorator has been used to define **get_number_of_wheels** as a class method. In the final line, the method is called by using the class name.

### Static methods and syntax 
Static methods are usually limited to a class only and not their objects. They have no direct relation to class variables or instance variables. They are used as utility functions that don't need access to class data. 

**Static methods can be accessed using the class name or the object name. Conventionally, they are accessed by the class name. They are associated with the class, rather than instances of the class.**

To declare a method as a static method, use the decorator **@staticmethod**. It does not use a reference to the object or class, so you do not have to use **self** or **cls**. You can pass as many arguments as you want and use this method to perform any function without interfering with the instance or class variables.

```
class MyClass: 
    @staticmethod 
    def demo() 
        print("I am a static method") 
```

Think back to the **Car** class example. A common utility function for cars could be to convert miles to kilometers for different informational displays, such as speed or fuel efficiency. The following is code for a static method called **convert_miles_to_km** within the **Car** class.

```
class Car:
    number_of_wheels = 4 # Class variable

    def __init__(self, body_style):
        self.body_style = body_style # Instance variable

    @staticmethod
    def convert_miles_to_km(miles):
        return miles * 1.6093

car_one = Car("Sedan")

# Accessing static methods from an object is possible, but should be avoided
print(f"100 miles is equivalent to {car_one.convert_miles_to_km(100)} kilometers")

# Best practice is to access static methods through the class name
print(f"100 miles is equivalent to {Car.convert_miles_to_km(100)} kilometers")
```

Output

```
100 miles is equivalent to 160.93 kilometers
100 miles is equivalent to 160.93 kilometers
```

Static methods do not know anything about the state of the class, meaning that they should not modify class attributes. The purpose of a static method is to use its parameters and produce a useful result. 

Suppose that there is a class, **BodyInfo**, containing information about the physical attributes of a person. The following shows a static method created to calculate BMI for a given weight and height.

```
class BodyInfo: 
    @staticmethod 
    def calculate_bmi(weight, height): 
        return weight / (height**2) 

weight = 75 
height = 1.8 
print(BodyInfo.calculate_bmi(weight, height)) 
```

Output

```
23.148148148148145
```

### Summary

#### Classes
A **class** in programming is a blueprint used to create objects. A class represents the idea of an object (without any data). After you have a class, you can create as many objects as you want. 

#### Objects
An **object** is an instance of a class that has attributes and methods. You create a new kind of object by defining a new class. Objects can be tangible and intangible.

#### Variables
A **variable** is a container for storing data values and could be any number of things, such as a string of text, a list, or an object. Variable names are case-sensitive and are also known as **attributes** or **properties**. 

#### Functions
**Functions** are blocks of code that perform a specific task, like adjusting speed or changing color. Functions are also known as **methods** or **behaviors**. 

#### Object-oriented programming
**OOP** is a programming paradigm in which everything in a project gets organized as classes and then as objects.

#### Dunder methods
Also called magic methods, Python special methods begin and end with a double underscore, which is where the name **dunder** comes from. With **Dunder** methods, you can control how a program displays an object in several common forms of output, such as what you get from the **print()** function, formatted strings, and interactive environments. They are designed to be internally called by a class.

#### Dot notation
You can access the methods and attributes for a given object using dot notation where you provide the object name, a dot (.), and the name of the method or attribute.

### Class methods and static methods
If not explicitly identified as class or static methods, the term methods will refer to instance methods.
* **Class methods** work with class variables and are accessible using the class name rather than its object. Because all class objects share the class variables, class methods are used to access and modify class variables. Regarding the syntax to declare a method as a class method, use the decorator **@classmethod**.
* **Static methods** are usually limited to a class only and not their objects. They have no direct relation to class variables or instance variables. They are used as utility functions inside the class or when you do not want the inherited classes to modify a method definition. Regarding the syntax to declare a method as a static method, use the decorator **@staticmethod**.

### Declaring a Python class
You can create a class by using the keyword class, followed by a space, followed by the name of the class, and then followed by a colon.   

```
class ClassName: 
```

#### __init__() method and initializing objects
The __init__ function is called a constructor, or initializer, and it is automatically called when you create a new instance (object) of a class. It is sometimes referred to as a constructor, and it initializes the attributes of the object with the values passed as arguments. 

Remember the difference between a class and an object: __init__ doesn’t initialize a class, it initializes an instance, or object, of a class.

After you have the __init__ method, you cannot pass arguments when creating an object, as this will result in errors.

#### self argument
The **self** parameter is known as the default constructor and it represents the current instance of the class. You can use it to access the attributes and methods of the class. If you are accessing variables outside of the class, you would use the object's name instead of **self**. 

You can access the attributes and methods for an object by using **dot notation**. This means using the object name, followed by a dot, and then the method or attribute name, which is written as self.attribute, for example.

#### Object printing with str() and repr() 
Two inbuilt functions you can use to describe objects using a string representation are **str()** and **repr()**. The following explains when to use each function:
* Use the **str()** method to describe objects as human-readable strings and as a debugging tool to check the members of your class. 
* Use the **repr()** method to access an official string representation to help you debug and maintain the code. You can also use it to create an object that is identical to the original object.

### Access modifiers 
In Python, you can impose access restrictions on different data members and member functions. The restrictions are specified through access modifiers, which are are tags associated with each member to define which parts of the program can access it directly. 

Most object-oriented languages use three access modifiers to restrict access to class variables and functions: **private**, **public**, and **protected**.  

#### Public
Members declared public are accessible from any part of the program through the object of the class. By default, all class data members and member functions are made public. 

#### Protected
Members declared protected are only accessible by their inherited or child class. To create a protected data member within a class, use a single underscore (_) before the data member. 

#### Private
Members declared private can only be accessed by objects of the same class. External access outside the class is restricted, and you will receive an error message from the compiler if you try to do so.

Using a double underscore (__) before a variable name limits access to class members, keeping them private and inaccessible to other classes.

**Properties and their related private attributes follow the standard naming convention. They are generally prefixed with an underscore, and corresponding properties are named identically without the underscore.**

## Core Concepts in OOP
* encapsulation
* data abstraction
* inheritance
* polymorphism

## Information (Data) Hiding

## Components of data hiding

### ENCAPSULATION
**Encapsulation** tells you *how* to protect something. Encapsulation protects data from unauthorized access by providing a physical structure to hold the data. It focuses on hiding the information at the implementation level from unauthorized access by restricting access to the data.

Encapsulation is a way of hiding the complexity of something and exposing only the parts you wish to expose. For example, if you have a class that has one or more private fields that you use to store the data, that would be an example of encapsulation. The class contains the data and has methods that expose the public data.

### Data Abstraction
**Data abstraction** tells you what to protect. Abstraction is about hiding complexity at the design level by ignoring unwanted details and focusing on what is required.

## Encapsulation
**Encapsulation** involves bundling data and the methods operating on that data within one unit, such as a class. Depending on this unit, objects are created.

A class can be thought of as a capsule that has methods and attributes inside it. This protects the attributes and methods, just like how medicine is encased (encapsulated) in an outer shell or coating to protect it from humidity and moisture.

### Encapsulation in Python 
Encapsulation is essential for several reasons, namely that it protects the internal data of a class from unauthorized access and modification. It also hides the state and representation of an object from outside. 

```
class BankAccount:
    def __init__(self, account_number):
        self._account_number = account_number # Protected attribute
    
    def __validate_pin(self, pin):
        return len(str(pin)) == 4
```

In the previous encapsulation example in Python, the _account_number attribute is protected. Encapsulation prevents direct modification from outside the class but allows modification by its subclasses due to the use of a protected attribute.

When encapsulating classes, a good convention is to declare all variables of a class private. This will restrict direct access by the code outside that class.

To allow controlled access to properties from outside the class, use **getter** and **setter** methods. You can also implement other custom methods.
* A **getter** method allows reading a property’s value.
* A **setter** method allows modifying a property’s value.

### Advantages of encapsulation 
* Classes make the code easy to change and maintain.
* Properties to be hidden can be specified easily.
* You decide which outside classes or functions can access the class properties.

### Differences between data encapsulation and data hiding 
In Python, encapsulation and data hiding work simultaneously towards the common goal of keeping sensitive data private. Use properties to hide the internal state of your class and ensure that you have complete control over access before allowing access or modification. This is especially important if you need to validate or change the data. It is also crucial if data is revised or modified before access or modification is permitted. 

Data encapsulation focuses on packaging (encapsulating) complex data to provide a simplified view for users. In contrast, data hiding focuses on limiting program access to data  and is used to ensure data security.

You can think of how these themes work in the real world with devices such as smartphones.

#### Data encapsulation
There are three ways to communicate with your smartphone. The buttons, the screen, and the camera serve as user-friendly interfaces or methods. A smartphone's inner workings are very complex with software, circuits, and processors, but you don't need to know how everything works to use it. 

**Key takeaway** 

Data encapsulation is like a smartphone, stripping away all the complex inner workings but providing an easy way to use apps, take photos, and make calls.

#### Data hiding
Now, think about your smartphone password or PIN. Your PIN is sensitive information that you want to restrict access to. Your smartphone hides this information from unauthorized users. Although the phone has internal mechanisms to manipulate the PIN code, it does not expose them. 

**Key takeaway** 

Data hiding protects sensitive information and ensures that bad actors cannot access it. 

## Getters and Setters
### Get and set with a code example 
It is a common convention to write the name of the corresponding member fields with the get or set command. The following example shows get and set methods for __username in the User class.

```
class User:
    def __init__(self, username = None):  
        self.__username = username

    def set_username(self, x):
        self.__username = x

    def get_username(self):
        return (self.__username)

john = User("john1")
print("Before setting:", john.get_username())
john.set_username("john2")
print("After setting:", john.get_username())
```

Output

```
Before setting: john1
After setting: john2
```

In the code, User, you have defined a private property named __username, which the main code cannot access. Also, note that the name of this private property starts with __ (double underscore).

For this property to interact with any external environment, use the get and set functions. The get function, get_username(), returns the value of __username, and the set_username(x) sets the value of __username equal to the parameter x passed.

## Understanding Encapsulation Using Examples
### Overall understanding of encapsulation in Python
The goal of encapsulation is to prevent the data bound in a class from any unwanted access by the code outside this class. Consider an example of a **Student** class that stores their name, age, and grade. These data attributes are protected within the class and can only be accessed and modified through well-defined methods. The following is an example.

```
class Student:
    def __init__(self, name, age, grade):
        self._name = name # Protected attribute
        self._age = age # Protected attribute
        self._grade = grade # Protected attribute
    
    # Getter method
    def get_name(self):
        return self._name
    
    # Setter method
    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self._grade = grade

# Create a Student object
student1 = Student("Ana Carolina", 18, 90)

# Accessing attributes through methods
print(student1.get_name()) # Output: "Ana Carolina"

# Modifying attributes through methods
student1.set_grade(95)
```

Output

```
Ana Carolina
```

In the previous example, a single underscore protects each attribute.

### Accessing modifiers in Python encapsulation
Encapsulation is implemented using access modifiers that determine the visibility and accessibility of a class's members (attributes and methods) in Python. 

The three access modifiers are 
* public, 
* private,
* and protected.

#### Encapsulation in Python using public members 
Public members are accessible anywhere within and outside the class. By default, all members are public unless explicitly marked as private. 

Consider a class, **Car**, as an example.

In the following example, **body_style** and **color** attributes are public, and the **start** method is also public. They can be accessed directly from outside the class. 

```
class Car:
    def __init__(self, body_style, color):
        self.body_style = body_style # Public attribute
        self.color = color # Public attribute
    
    def start(self):
        print(f"{self.color} {self.body_style} is starting.") # Public method
```

#### Encapsulation in Python using private members 
Private members are exclusively accessible within the class. To mark a member as private, prefix its name with double underscores (__). 

This example explores how to use private members in Python.

```
class BankAccount:
    def __init__(self, account_number):
        self.__account_number = account_number # Private attribute
    
    def __validate_pin(self, pin):
        # Private method to validate the PIN
        return len(str(pin)) == 4
```

In the previous data encapsulation in Python example, the **__account_number** attribute and the **__validate_pin** method are marked as private using double underscores. They can be accessed within the class.

#### Name mangling to access private members 
Name mangling is a technique in Python you can use to access private members from outside the class by prefixing their names with the class name and an underscore (**_ClassName__**). You can use this technique to make private members somewhat accessible, but it is generally discouraged to maintain encapsulation and code clarity. The following is an example.

```
class BankAccount:
    def __init__(self, account_number):
        self.__account_number = account_number # Private attribute
    
    def __validate_pin(self, pin):
        return len(str(pin)) == 4

# Creating an instance of the class
account = BankAccount("12345")

# Accessing private attributes using name mangling
print(account._BankAccount__account_number) # Output: 12345

# Accessing private method using name mangling
print(account._BankAccount__validate_pin(1234)) # Output: True
```

Output

```
12345
True
```

#### Encapsulation in Python using protected members 

Protected members are accessible within the class itself and its subclasses, maintaining data integrity while allowing for some degree of flexibility. You indicate a member as protected by prefixing its name with a single underscore (_). 

The following example shows this encapsulation in Python.

```
class Animal:
    def __init__(self, name):
        self._name = name # Protected attribute
    
    def _make_sound(self, sound):
        print(f"{self._name} makes a {sound} sound.") # Protected method

# Subclass of Animal
class Dog(Animal):
    def bark(self):
        self._make_sound("bark")

# Creating instances
animal = Animal("Generic Animal")
dog = Dog("Buddy")

# Accessing protected attribute
print(animal._name) # Output: Generic Animal

# Accessing protected method
dog.bark() # Output: Buddy makes a bark sound.
```

Output

```
Generic Animal
Buddy makes a bark sound.
```

## Data Abstraction
**Data abstraction** is when you hide data from a user or another programmer when they don’t need to see or access it. A programmer or a company can use data abstraction to change data within the code without the user knowing, as long as it yields the same output. The user can view certain relevant functionalities, but not the internal details. That is abstraction, whereas encapsulation is what hides the internal details. 

Data abstraction is useful not only for hiding sensitive or confidential information from the user but also for reducing the complexity for the user. They see enough to access what is necessary.

### Real-world applications
Real-world applications of data abstraction include the following:
* An API provides a simple method to interact with a device or program without revealing what is going on internally. 
* Any modern device, whether it is a phone, thermostat, laptop, tablet, battery charger, or car, has an internal interface where processes are happening behind the scenes. 
* Teams can code base classes and share them as a library without requiring everyone to re-implement all of the base classes.
* You can create generalized functions that you can adapt for various purposes.

### Knowledge Check
#### Which sentence represents data abstraction?
* A user knows that a phone app will perform a certain function without knowing how the code works.

Wrong answers:
* Because of shared DNA, a puppy born to two dogs with brown fur will probably also have brown fur.
* Each department at a company work with data and restrict access for people outside of their department.
* All vehicles have a method for starting, but it might be a key start or a push-button start.

Inheritance explains how with shared DNA, a puppy born to two dogs with brown fur will probably also have brown fur.

Encapsulation is like how each department at a company will work with data and restrict access for people outside of their department. 

Polymorphism is how all vehicles have a method for starting, but depending on the car, it might be a key start or a push-button start.

#### What is a getter in object-oriented programming? 
* A getter retrieves attribute values within the class.

Wrong answers:
* A getter performs calculations on values. 
* A getter changes new values in the class. 
* A getter sets new property values in the class. 

### Summary

#### Information (data) hiding
**Information hiding**, also called **data hiding**, refers to the concept of hiding the inner workings of a class and providing an interface through which the outside world can interact with the class without knowing what’s going on inside.

Data hiding promotes abstraction, provides better control over the object and its internal state, and improves security. It also reduces the risk of unwanted changes.

Data hiding can be divided into two primary components: **encapsulation** and **data abstraction**.    

#### Encapsulation
**Encapsulation** involves bundling attributes and methods within one unit, such as a class, to protect the attributes and methods. Encapsulation is a way to restrict access to variables and methods and prevent them from being modified accidentally. It also hides the state and representation of an object from outside.

To allow controlled access to properties from outside the class, use **getter** and **setter** methods.  

#### Getter and setter methods
* A **getter** method allows reading a property’s value.
* A **setter** method allows modifying a property’s value. 

You can write read-only attributes by defining a property using the **getter** method but not the **setter** method. It is useful when you want to provide users with information without giving them the ability to change it.  

Achieve specific requirements by invoking the custom behavior in the **getter**, **setter**, and **deleter** methods. This might involve data validation, logging, or complex calculations.

#### Name mangling
Name mangling is a technique in Python you can use to access private members from outside the class by prefixing their names with the class name and an underscore (**_ClassName__**). This technique used to make private members somewhat accessible, but it is generally discouraged to maintain encapsulation and code clarity.

#### Difference between data encapsulation and data hiding 
In Python, encapsulation and data hiding work simultaneously towards the common goal of keeping sensitive data private. 

Data encapsulation focuses on packaging, or encapsulating, complex data to provide a simplified view for users. In contrast, data hiding focuses on limiting program access to data used to ensure data security. 

#### Data abstraction
**Data abstraction** is when you hide data from a user or another programmer when they don’t need to see or access it. You can use this to change data within the code without changing the output. Data abstraction is also useful for reducing the complexity for the user. They see enough to access what is necessary. 

## Inheritance
Inheritance provides a way to create a new class, known as a **child class**, from an existing class, known as a **parent class**. The new class is a specialized version of the existing class such that it inherits all the non-private fields, or variables, and methods of the existing class. The existing class is used as a starting point, or as a base to create the new class. 

A **parent class** is also called a **base class** or **superclass**. 

A **child class** is also called a **derived class**, **inherited class**, or **subclass**.

A **child** class has all the **public** attributes of the **parent** class.

After you have defined a parent class, you can define child classes, each of which will have the same properties and methods as the parent class. Inheritance allows for the creation of a hierarchy (or different levels) of classes with shared properties and methods.

Wherever you come across an **IS A** relationship between objects, you can use inheritance.

You can build new classes by extending existing classes.

| Existing Classes | Derived Classes |
| ---------------- | --------------- |
| Shape | Square |
| Programming language | Python |
| Vehicle | Car |

Square **IS A** Shape. Python **IS A** Programming Language. Car **IS A** Vehicle. 

### Types of inheritance
There are five types of inheritance in Python: 
* single inheritance, 
* multiple inheritance, 
* multilevel inheritance, 
* hierarchical inheritance, 
* and hybrid inheritance.

### Syntax and Terminologies

| Class Type | Purpose |
| ---------- | ------- |
| Parent class (superclass or base class) | This class allows the reuse of its public properties in another class. |
| Child class (subclass or derived class) | This class inherits or extends the superclass. |

```
class ParentClass:
    # Attributes of the parent class

class ChildClass(ParentClass):
    # Attributes of the child class
```

Consider the following example of a **Vehicle** class as the parent class, and implement a **Car** class that will extend from this **Vehicle** class. Because a car **IS A** vehicle, the inheritance relationship between these classes is valid.

```
class Vehicle:
    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model

    def print_details(self):
        print("Manufacturer:", self.make)
        print("Color:", self.color)
        print("Model:", self.model)

class Car(Vehicle):
    def __init__(self, make, color, model, doors):
        # Calling the parent class's initializer
        Vehicle.__init__(self, make, color, model)
        self.doors = doors

    def print_car_details(self):
        # Calling the parent class's print_details method
        self.print_details()
        print("Doors:", self.doors)

obj1 = Car("Car Brand A", "Gray", "2015", 4)
obj1.print_car_details()
```

Output

```
Manufacturer: Car Brand A
Color: Gray
Model: 2015
Doors: 4
```

In the previous example, the parent class is **Vehicle**, and the child class is **Car**.

The **Car** class inherits all the properties and methods of the **Vehicle** class and can access and modify them. For example, in the **Car** class's **print_car_details()** method, the **print_details()** method is called. The **print_details()** method is defined in the Vehicle class. It is available to the Car class through inheritance.

### Types of Inheritance
#### Single inheritance 
In single inheritance, there is only a single class extending from another class. 

#### Multilevel inheritance
When a class is derived from a class that itself is derived from another class, it is called multilevel inheritance. 

Example Hybrid extends Car extends Vehicle:
* A **Car** IS A **Vehicle**.
* A **Hybrid** IS A **Car**.
* The **Car** class is a child class of **Vehicle**, but itself is the parent of the **Hybrid** class.

#### Hierarchical inheritance 
In hierarchical inheritance, more than one class extends from the same base class. The common attributes of these child classes are implemented inside the base class. 

#### Multiple inheritance 
When a class is derived from more than one base class (in other words, when a class has more than one immediate parent class), it is called multiple inheritance. 

#### Hybrid inheritance 
Hybrid inheritance is a combination of multiple and multi-level inheritance. 

### Using the super() function
The use of super() function comes into play when you implement inheritance. The benefits of super() in single inheritance are minimal. However, it is almost impossible to use multiple inheritance without using super(). It is used in a child class to refer to the parent class without explicitly naming it. It makes the code more manageable, and there is no need to know the name of the parent class to access its attributes.

#### Use cases of the super() function 
You can use the super() function in the following three relevant contexts:
* To access parent class properties
* To call the parent class methods
* To use with initializers

#### Using the super() function with multiple inheritance and method resolution order (MRO)

```
class Parent:
    def __init__(self):
        print("This is the parent class")

class Parent1:
    def __init__(self):
        print("This is the parent1 class")

class Child(Parent1, Parent):
    def __init__(self):
        # Calling initializer of the Parent 1 class
       super().__init__()

ob = Child()
```

Output

```
This is the parent1 class
```

Method resolution order (MRO) defines the order of the inherited methods in the child class.

In the previous example, the initializer was accessed using the **super()** function. The **super()** function will search the initializer according to the order of the inherited class. It will search first in the **Parent1** class and then in the **Parent** class.

In the previous case, the initializer is already present in the **Parent1** class, which is why the constructor of the **Parent1** class is run instead of the **Parent** class. Also, the **super()** function in Python is used to access the immediate parent class members. 

Consider the following example to understand the order of inheriting class by the child class.

```
class Parent:
    def __init__(self):
        print("This is the parent class")

class Parent1:
    def __init__(self):
        print("This is the parent1 class")

class Child(Parent1, Parent):
    def __init__(self):
        # Calling initializer of the Parent 1 class
       super().__init__()
 
print(Child.mro())
```

Output

```
[<class '__main__.Child'>, <class '__main__.Parent1'>, <class '__main__.Parent'>, <class 'object'>]
```

The **Child** class first extends the **Parent1** class and then extends the **Parent** class. The object class is the superclass of all the classes in Python, which is why the Child class also extends the object class by default.

#### Accessing the method of the Parent class using the super() function

```
super(ImmediateClassName, current_object)
```

This super() function accepts the following two parameters in multiple inheritance:
* **ImmediateClassName** – The name of the class that is inherited just before the class that you want to access using the super() function
* **current_object** – The current object of the class

Consider the following example to understand how to access the initializer of the Parent class from the Child class.

```
class Parent:
    def __init__(self):
        print("This is the parent class")

class Parent1:
    def __init__(self):
        print("This is the parent1 class")

class Child(Parent1, Parent):
    def __init__(self):
        # Calling initializer of the Parent 1 class
       super(Parent1, self).__init__()
 
ob = Child()
```

Output

```
This is the parent class
```

The constructor of the **Parent** class is accessed using the super() function in the Child class and passing in **Parent1** as the first argument.

### Accessing parent class properties 
Consider the fields named **fuel_cap** defined inside a **Vehicle** class to keep track of the fuel capacity of a vehicle. Another class named **Car** extends from this **Vehicle** class. Declare a class property inside the **Car** class with the same name, **fuel_cap**, but with a different value. If you want to refer to the **fuel_cap** field of the parent class inside the child class, use the **super()** function.

```
# Defining the parent class
class Vehicle: 
    fuel_cap = 90

# Defining the child class
class Car(Vehicle): 
    fuel_cap = 50

    def display(self):
        # Accessing fuel_cap from the Vehicle class using super()
        print("Fuel cap from the Vehicle Class:", super().fuel_cap)
        # Accessing fuel_cap from the Car class using self
        print("Fuel cap from the Car Class:", self.fuel_cap)

# Creating a car object
my_car = Car() 
# Calling the Car class method display()
my_car.display() 
```

Output

```
Fuel cap from the Vehicle Class: 90
Fuel cap from the Car Class: 50
```

### Calling the parent class methods
**super()** is also used with methods. Whenever a parent class and the immediate child class have any methods with the same name, use **super()** to access the methods from the parent class inside of the child class. 

```
# Defining the parent class
class Vehicle: 
    # Defining display method in the parent class
    def display(self): 
        print("I am from the Vehicle Class")

# Defining the child class
class Car(Vehicle): 
    # Defining display method in the child class
    def display(self):
        super().display()
        print("I am from the Car Class")

# Creating a car object
my_car = Car() 
# Calling the Car class method display()
my_car.display() 
```

Output

```
I am from the Vehicle Class
I am from the Car Class
```

### Using with initializers
Another essential use of the function **super()** is to call the initializer of the parent class from inside the initializer of the child class.

The call to **super()** in a method or an initializer doesn't need to be made in the first line of the method.

#### Example 1
```
class ParentClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class ChildClass(ParentClass):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

obj = ChildClass(1, 2, 3)
print(obj.a)
print(obj.b)
print(obj.c)
```
Output
```
1
2
3
```

#### Example 2
```
class ParentClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class ChildClass(ParentClass):
    def __init__(self, a, b, c):
        self.c = c
        super().__init__(a, b)

obj = ChildClass(1, 2, 3)
print(obj.a)
print(obj.b)
print(obj.c)
```
Output
```
1
2
3
```

In the previous two examples, swapping the order of the following two lines does not change the functionality of the code.

```
self.c = c
super().__init__(a, b)
```

The user can manipulate parameters before passing them into the parent class method.

The following two examples show two different ways to refer to the parent class.

#### Example 3
This example does not make use of the **super()** function. The parent class is accessed as follows:

```
class Vehicle:
    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model

    def print_details(self):
        print("Manufacturer:", self.make)
        print("Color:", self.color)
        print("Model:", self.model)

class Car(Vehicle):
    def __init__(self, make, color, model, doors):
        # If you don't use the super function, you need to use the self parameter
        Vehicle.__init__(self, make, color, model)
        self.doors = doors

    def print_car_details(self):
        self.print_details()
        print("Doors:", self.doors)

my_car = Car("Car Brand A", "Gray", "2015", 4)
my_car.print_car_details()
```

Output

```
Manufacturer: Car Brand A
Color: Gray
Model: 2015
Doors: 4
```

As noted, if **super()** is not used and the parent class's __init__ function is called through the parent class, the self parameter must be used.

#### Example 4
In this example, the parent class's constructor is called with the **super()** function as follows.

```
class Vehicle:
    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model

    def print_details(self):
        print("Manufacturer:", self.make)
        print("Color:", self.color)
        print("Model:", self.model)

class Car(Vehicle):
    def __init__(self, make, color, model, doors):
        # Calling the super function (no need to use the self parameter)
        super().__init__(make, color, model)
        self.doors = doors

    def print_car_details(self):
        self.print_details()
        print("Doors:", self.doors)

my_car = Car("Car Brand A", "Gray", "2015", 4)
my_car.print_car_details()
```

Output

```
Manufacturer: Car Brand A
Color: Gray
Model: 2015
Doors: 4
```

As noted, when using **super()**, you do not have to pass in the self parameter when calling the parent's constructor.

The previous two examples produced the same output, but using **super()** makes the code more manageable.

### Advantages of Inheritance

#### Reusability of code
Inheritance makes the code reusable, which means you can avoid duplicating it. This makes the code cleaner.

#### Code modification
If you make inconsistent edits to existing code, you might introduce bugs. Use inheritance to localize changes and avoid inconsistencies. 

#### Extensibility
You can extend the base class as needed to upgrade specific parts of a product without changing the core attributes. An existing class can act as a base class and pass on upgraded features. 

#### Data hiding
The base class can keep some data private so the derived class cannot alter it. This concept is called encapsulation. 

#### Cost-saving
Inheritance uses a simple structure and requires less time for development and maintenance, which saves money.

#### Familiarity
Inheritance parallels real-world relationships.

### Reusability of code
If you design a banking system using classes, your model might have the following:
* A parent class: **BankAccount**
* A child class: **SavingsAccount**
* Another child class: **CheckingAccount**

The **BankAccount** class has attributes **holders_name**, **account_balance**, **account_number**, and **methods get_balance()**, **get_details()**, **withdraw()**, and **deposit()**. The **SavingsAccount** and **CheckingAccount** classes inherit the attributes from **BankAccount**. **SavingsAccount** comes with additional attributes **interest_amount** and **add_interest()**. **CheckingAccount** comes with additional attributes **linked_atm_card** and **deduct_fee()**. You don’t need to duplicate the code for the **deposit()** and **withdraw()** methods inside the child classes, because they are inherited from the parent class. In this way, you can avoid the duplication of code.

#### Extending the example further
You realize at a later point that you have to diversify this banking application by adding another class for **MoneyMarketAccount**. Rather than implementing this class from scratch, you can extend it from the existing **BankAccount** class as a starting point. You can also reuse the attributes that are shared with **MoneyMarketAccount**.

### Method Overriding
Method overriding is the process of redefining a parent class’s method in a subclass.

In other words, if a subclass provides a specific implementation of a method that has already been defined in one of its parent classes, it is known as method overriding.

In method overriding, these terms are defined as follows:
* The method in the parent class is called the **overridden** method.
* The methods in the child classes are called the **overriding** methods.

```
class Shape:
    def __init__(self):
        # Initializing sides of all shapes to 0
        self.sides = 0

    # This method will be overridden in child classes
    def calculate_area(self): 
        pass

# Rectangle is derived from the Shape class
class Rectangle(Shape): 
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height
        self.sides = 4

    # Rectangle overrides the method to calculate area with its own implementation
    def calculate_area(self): 
        return (self.width * self.height)

# Circle is also derived from the Shape class 
class Circle(Shape): 
    def __init__(self, radius = 0):
        self.radius = radius

    # Circle also overrides the method to calculate area with its own implementation
    def calculate_area(self):
        return (self.radius * self.radius * 3.142)

shapes = [Rectangle(6, 10), Circle(7)]
print("Area of rectangle is:", str(shapes[0].calculate_area()))
print("Area of circle is:", str(shapes[1].calculate_area()))
```

Output

```
Area of rectangle is: 60
Area of circle is: 153.958
```

#### Advantages and key features of method overriding
Method overriding comes with certain requirements and benefits, as follows:
* Method overriding needs inheritance, and there should be at least one derived class to implement it.
* The derived classes can give their own specific implementations to inherited methods without modifying the parent class methods.
* For any method, a child class can use the implementation in the parent class or make its own implementation.
* The methods in the derived classes usually have a dissimilar implementation.

### Knowledge Check

#### Which type of inheritance is when a child class inherits from more than one parent class? 
* Multiple inheritance

Wrong answers:
* Multilevel inheritance
* Single inheritance
* Hierarchical inheritance 

Multiple inheritance is when a child class inherits from multiple parent classes.

Multilevel inheritance is when there is a child and grandchild relationship. 

Single inheritance is when a child class inherits from only one parent class. 

Hierarchical inheritance is when more than one class is derived from a single base class.

#### Which option explains why the following code example will not compile?
```
class A:
    def __init__(self, x):
        self.x = x

class B(A):
    def __init__(self, x, y):
        self.y = y
        super().__init__(self, x)

b = B(5, 6)
```
* When calling the parent initializer in the child initializer using super(), the self parameter is not used.

Wrong answers:
* x is a private variable and cannot be accessed by the child class B.
* super().__init__(self,x) should be the first line in the child initializer.
* y is a private variable and cannot be accessed by the child class B.

When calling **super().__init__(self, x)**, the **self** argument is passed as **self**, which is not needed because **super()** already knows the current class context. This could potentially lead to unexpected behavior.

To fix this vulnerability, the **self** argument should be removed from the **super().__init__(self, x)** call in the B class constructor. This way, you only pass the required argument x when calling the superclass constructor.

#### What will be the output of the following code?
```
class Test:
    def __init__(self):
        self.x = 0

class Derived_Test(Test):
    def __init__(self):
        self.y = 1

def main():
    b = Derived_Test()
    print(b.x, b.y)

main()
```

* An error because class **Derived_Test** inherits **Test**, but variable **x** isn't inherited

Wrong answers:
* An error because when an object is created, an argument must be passed like **Derived_Test(0)**
* An error because class **Derived_Test** inherits **Test**, but variable **y** isn't inherited
* An error because when an object is created, an argument must be passed like **Derived_Test(1)**

In the original code, the **__init__** method of the **Derived_Test** class does not call the **__init__** method of the base class **Test**. This means that the **x** attribute from the **Test** class is not initialized when an instance of **Derived_Test** is created, potentially causing unexpected behavior.

To fix this issue, the corrected code uses **super().__init__()** in the **__init__** method of the **Derived_Test** class to explicitly call the constructor of the base class **Test**. This ensures that both **x** and **y** attributes are properly initialized when an instance of **Derived_Test** is created.

By making this change, the code now correctly initializes both **x** and **y** attributes, avoiding any unexpected behavior because of missing attribute initialization.

#### What will be the output of the following code?
```
class A:
    def disp(self):
        print("A disp()")

class B(A):
    def __init__(self):
        super().__init__()

obj = B()
obj.disp()
```
* * A disp()

Wrong answers:
* An invalid syntax for inheritance
* An error because when an object is created, an argument must be passed
* Nothing is printed

Class **B** inherits class **A**; therefore, the function **disp()** becomes part of class **B**’s definition. The **disp()** method is properly run and the line is printed.

### Summary
#### Inheritance
**Inheritance** in programming is a way of defining a class that inherits all the methods and properties from another class. Inheritance allows for the creation of a hierarchy of classes with shared properties and methods.

A **parent** class is also called a **base** class or **superclass**. 

A **child** class is also called a **derived** class or **subclass**.

A **child** class has all public attributes of the **parent** class.

#### Syntax
The name of the parent class is written in parentheses after the name of the child class, which is followed by the body of the child class, as shown in the following example.

```
class ParentClass:
    # Attributes of the parent class

class ChildClass(ParentClass):
    # Attributes of the child class
```

#### Types of inheritance 
The following are the types of inheritance:
* **Single inheritance** is when a child class inherits from only one parent class. 
* **Multiple inheritance** is when a child class inherits from multiple parent classes. 
* **Multilevel inheritance** is when there is a child and grandchild relationship. 
* **Hierarchical inheritance** is when more than one class is derived from one parent class. 
* **Hybrid inheritance** is a combination of more than one type of inheritance.

#### Inheritance and the super() function 
The use of **super()** comes into play when you implement inheritance. It is especially useful with multiple inheritance. It is used in a child class to refer to the parent class without explicitly naming it. It makes the code more manageable, and there is no need to know the name of the parent class to access its attributes. 

To access the constructor of the **Parent** class using the **super()** function, use the method resolution order, or MRO. The MRO defines the order of the inherited methods in the child class. The **super()** function in Python is used to access the immediate parent class members.

You can use the **super()** function in the following three relevant contexts:
* To access parent class properties
* To call the parent class methods
* When using with initializers

#### Advantages of using inheritance
The advantages of using inheritance include the following:
* The reusability of code to the code cleaner
* Code modification while avoiding inconsistencies
* Extensibility
* Data hiding
* Saving money and time
* Familiarity in that it parallels real-world relationships

#### Method overriding
**Method overriding** is the process of redefining a parent class’s method in a subclass.

In other words, if a subclass provides a specific implementation of a method that had already been defined in one of its parent classes, it is known as method overriding.

In method overriding, these terms are defined as follows:
* The method in the parent class is called the **overridden** method.
* The methods in the child classes are called the **overriding** methods.

## Introduction: Polymorphism

### Pre-assessment
#### What does polymorphism mean? 
* Many forms

Wrong answers:
* Many functions
* Many meanings
* Many faces

Polymorphism comes from the root words poly, meaning many, and morph, meaning form. It refers to the ability of an object to take on many forms.  

The other answers are incorrect. Polymorphism does not mean many functions, many meanings, or many faces.

#### Which option describes polymorphism? 
* Allows objects of different types and behaviors to be treated as the same type

Wrong answers:
* The ability of a class to derive members of another class as a part of its definition
* A means of bundling instance variables and methods to restrict access to certain class members
* Focuses on variables and passing of variables to functions

Polymorphism is a feature of object-oriented programming languages. With it, you can implement elegant software that is well-designed and easily modified.

#### Which descriptions are true about polymorphism? (Select THREE.)
* It is a concept of object-oriented programming.
* It helps improve the readability of the program.
* It helps in redefining the same functionality.

Wrong answers:
* It increases overhead of function definition.
* It gives child classes the functionality of their parents.
* It keep data and implementation details private. 

Polymorphism does not increase function definition overhead. It helps to write more efficient code.

Giving child classes the functionality of their parent classes describes inheritance. Keeping data and implementation details private describes encapsulation. 

### Polymorphism
**Polymorphism** comes from the Greek root words poly, meaning many, and morph, meaning form. In programming, polymorphism refers to the same object exhibiting different forms and behaviors when the code is subject to different conditions. Polymorphism helps create flexibility and the reusability of code. 

### Implementing Polymorphism Using Methods
Consider two shapes that are defined as classes: **Rectangle** and **Circle**. These classes contain the **calculate_area()** method that calculates the area for the respective shape depending on the values of their properties, as shown in the following example.

```
class Rectangle:
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height
        self.sides = 4

    def calculate_area(self):
        return (self.width * self.height)

class Circle:
    def __init__(self, radius = 0):
        self.radius = radius
        self.sides = 0

    def calculate_area(self):
        return (self.radius * self.radius * 3.142)

# Declare a list that has two objects in it
shapes = [Rectangle(6, 10), Circle(7)]

print("Sides of a rectangle are", str(shapes[0].sides))
print("Area of rectangle is:", str(shapes[0].calculate_area()))

print("Sides of a circle are", str(shapes[1].sides))
print("Area of circle is:", str(shapes[1].calculate_area()))
```

Output

```
Sides of a rectangle are 4
Area of rectangle is: 60
Sides of a circle are 0
Area of circle is: 153.958
```

The explanation is as follows.
* In the main function, you have declared a list that has two objects in it in the following line of code.
```
shapes = [Rectangle(6, 10), Circle(7)]
```
* The first object is a **Rectangle** with width **6** and height **10**, and the second object is a **Circle** of radius **7**.
* Both the classes have the method **calculate_area()** but the logic of this method is different for each class.
* The methods to call the area of the two shapes look identical, but different methods are called. Thus, you have achieved polymorphism. The two methods used in the example are as follows.

```
print("Area of rectangle is:", str(shapes[0].calculate_area()))
print("Area of circle is:", str(shapes[1].calculate_area()))
```

### Implementing Polymorphism Using Inheritance
Instead of having two shapes defined as separate classes, consider defining the **Shape** class as the base class. Shapes like **Rectangle** and **Circle** that extend from the base class are derived classes. These derived classes inherit the **calculate_area()** method and provide a shape-specific implementation, which calculates its area.

```
class Shape:
    # Initializing sides of all shapes to 0
    def __init__(self): 
        self.sides = 0

    def calculate_area(self):
        pass

class Rectangle(Shape): 
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.sides = 4

    def calculate_area(self):
        return (self.width * self.height)

class Circle(Shape):
    def __init__(self, radius=0):
        self.radius = radius

    def calculate_area(self):
        return (self.radius * self.radius * 3.142)

shapes = [Rectangle(6, 10), Circle(7)]
print("Area of rectangle is:", str(shapes[0].calculate_area()))
print("Area of circle is:", str(shapes[1].calculate_area()))
```

Output

```
Area of rectangle is: 60
Area of circle is: 153.958
```

### Operator Overloading
In addition to method overriding, another way of implementing polymorphism in Python is **operator overloading**. Operators in Python can be overloaded to operate in a certain user-defined way. Whenever an operator is used in Python, its corresponding method is invoked to perform its predefined function. 

For example, when the **+** operator is called, it invokes the special function, **__add__**, in Python, but this operator acts differently for different data types. For example, the **+** operator adds the numbers when it is used between two **int** data types and merges two strings when it is used between string data types. The following is an example of the **+** operator.

```
print(5 + 3) # adding integers using '+'
print("money" + "maker") # merging strings using '+'
```

Output

```
8
moneymaker
```

#### Overloading operators for a user-defined class for complex numbers
When you add a complex number, the real part is added to the real part, and the imaginary part is added to the imaginary part. Similarly, when you subtract a complex number, the real part is subtracted from the real part, and the imaginary part is subtracted from the imaginary part.

Similarly, whenever two objects of class **Complex** are subtracted using the - operator, the overloaded **__sub__** method is called. This method subtracts the real and the imaginary properties separately, and then returns a new **Complex** class object that is initialized by these differences.

The following example implements the complex number class and overloads the **+** and **-** operators.

```
class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    # Overloading the + operator
    def __add__(self, other): 
        temp = Complex(self.real + other.real, self.imag + other.imag)
        return temp
    
    # Overloading the - operator
    def __sub__(self, other): 
        temp = Complex(self.real - other.real, self.imag - other.imag)
        return temp

obj1 = Complex(3, 7)
obj2 = Complex(2, 5)

obj3 = obj1 + obj2
obj4 = obj1 - obj2

print("real of obj3:", obj3.real)
print("imag of obj3:", obj3.imag)
print("real of obj4:", obj4.real)
print("imag of obj4:", obj4.imag)
```

Output

```
real of obj3: 5
imag of obj3: 12
real of obj4: 1
imag of obj4: 2
```

With this example we overloaded the built-in methods **__add__** and **__sub__** that are invoked when the **+** and the **-** operators are used.

Whenever two objects of class **Complex** are added using the **+** operator, the overloaded **__add__** method is called.

This method adds the **real** property separately, and the **imag** property separately, and then returns a new **Complex** class object that is initialized by these sums.

Note that **__add__** and **__sub__** methods have two input parameters. The first one is **self**, which you know is the reference to the class itself. The second parameter is **other**, which is a reference to the other objects that are interacting with the class object.

In the following line, **obj2** will be considered the **other** object, the operator will be called on the **obj1** object, and the returned object will be stored in **obj3**.

```
obj3 = obj1 + obj2
```

In the following line, **obj2** will be considered the other object, the operator will be called on the **obj1** object, and the returned object will be stored in **obj4**.

```
obj4 = obj1 - obj2
```

The **other** object also has **Complex** class attributes and thus, it has the **real** and **imag** properties.

### Special functions for common operators 
Some common special functions can be overloaded while implementing operators for objects of a class, including the following:
* **+**       **__add__ (self, other)**
* **-**       **__sub__ (self, other)**
* **/**       **__truediv__ (self, other)**
* *****       **__mul__ (self, other)**
* **<**       **__lt__ (self, other)**
* **>**       **__gt__ (self, other)**
* **==**       **__eq__ (self, other)**

### Knowledge Check
#### What will be the output of the following code?

```
class Demo:
    def __init__(self):
        self.x = 1

    def change(self):
        self.x = 10

class Demo_derived(Demo):
    def change(self):
        self.x = self.x + 1
        return self.x

def main():
    obj = Demo_derived()
    obj.change()
    print(obj.x)

main()
```
* 2

Wrong answers:
* 1
* 11
* An exception

The derived class method **change()** overrides the base class method. The **__init__** from the base class is being used to initialize the **Demo_derived()**.

#### What will be the output of the following code?
```
class A:
    def __str__(self):
        return "1"

class B(A):
    def __str__(self):
        return "2"

class C(B):
    def __str__(self):
        return "3"

obj1 = A()
obj2 = B()
obj3 = C()

print(obj1, obj2, obj3)
```
* 1 2 3

Wrong answers:
* 1 1 1
* '1' '1' '1'
* An exception

When different objects are invoked, each of the individual classes return their individual values, and hence it is printed.

Each class (**A**, **B**, and **C**) defines a **__str__** method to return a specific string representation when an instance of the class is converted to a string.

Instances of classes **A**, **B**, and **C** are created (**obj1**, **obj2**, and **obj3**) and their string representation is printed using the print function.

#### What will be the output of the following code?
```
class Square:
   def __init__(self, side):
       self.side = side

   def calculate_area(self):
       return self.side ** 2

square = Square(4)
result = square.calculate_area()
print(result)
```
* 16

Wrong answers:
* 8
* 12
* 20

The code creates an instance of the **Square** class with a side length of 4 and calculates the area using the **calculate_area** method (4 ** 2). 

The other answers are incorrect because 4 x 4 = 16 and not 8, 12, or 20.

### Summary
#### Polymorphism
**Polymorphism** comes from the root words poly, meaning many, and morph, meaning form. It and refers to the ability of a class or an object to run methods, functions, or operators with the same name in different ways.

You can implement polymorphism by using methods and inheritance.

#### Implementing polymorphism using methods 
A function that can evaluate or be applied to values of different types is known as a polymorphic function. With polymorphism, each subclass can have its own way of implementing a method. 

#### Implementing polymorphism using inheritance
You can add new data and methods to a class through inheritance. With polymorphism, you can have specialized implementations of the same methods for each class. 

#### Operator overloading
You can overload operators in Python to operate in a certain user-defined way. Whenever you use an operator in Python, its corresponding method is invoked to perform its predefined function. 

#### Overloading operators for a user-defined class 
When you define a class, its objects can interact with each other through the operators, but it is necessary to define the behavior of these operators through operator overloading.

## Additional Resources
### [Week 1 Glossary.pdf](./files/Week01Glossary.pdf)

## Python 2: Part 1 Assessment
