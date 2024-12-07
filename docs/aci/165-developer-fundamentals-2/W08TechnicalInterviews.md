# Technical Interviews

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to repo's main [README.md](../../../README.md)

## Coding Interviews

### Pre-assessment

#### A cloud application developer is trying to solve an algorithmic problem. What actions should they take to solve the problem before starting to code? (Select THREE.)

* Break down the problem
* Choose the most efficient solution
* Design a systematic approach

Wrong answers:

* Directly start to code by copying existing code snippets
* Use Python's standard library for inspiration
* Collect an assortment of algorithmic coding examples

Three steps to solving a problem include break down the problem, design a systematic approach, and choose an efficient solution.

Starting to code by copying existing code snippets or using Python's standard library for inspiration is NOT a starting point to solve an algorithmic problem.

#### Which option best defines critical thinking?

* Evaluating information objectively, questioning assumptions, and considering alternative perspectives

Wrong answers:

* Memorizing facts and information that seem related to the task
* Analyzing information and feedback if time permits
* Exploring only previously tried solutions as a viable option

Critical thinking involves actively and skillfully analyzing, synthesizing, and evaluating information to reach reasoned conclusions. It goes beyond acceptance of information and involves questioning assumptions, considering different viewpoints, and examining evidence objectively.  

The other choices describe behaviors that do not align with critical thinking and are more passive in nature.

#### A hiring manager is interviewing candidates for a role as a cloud application developer. The candidates are required to complete an assignment quickly, efficiently, and under a strict time constraint. What primary skill set is the interviewer looking for in the candidates?

* Performance under pressure skills

Wrong answers:

* Coding proficiency skills
* Adaptability skills
* Logical thinking skills

Performance under pressure skills are important in order to deliver results quickly and efficiently.

The other skills are overall just as vital to be successful in the role, but in this situation, the hiring manager is looking for a specific skill set to showcase whether the candidates can work under pressure.

## The Essentials

### Topics

* Big O
* data structures
* sorting
* coding terminology

### Top skills

#### Number 1: Problem-solving skills

Ability to solve problems. Algorithms are fundamental in solving these types of problems. They are used by the interviewer to assess the candidate’s ability to break down a problem, design a systematic approach, and arrive at an efficient solution.

#### Number 2: Logical thinking skills

Along with showing your ability to problem solve, algorithm-based questions help an interviewer evaluate your critical thinking skills, ability to identify patterns, and devise logical solutions.

#### Number 3: Coding proficiency skills

Using and implementing algorithms in a coding problem means you will need to write code. Technical interviews usually include coding exercises to see if you can translate the algorithm into code. They are assessing your proficiency and style.

#### Number 4: Adaptability skills

Show how you would rewrite a solution based on an x or y condition changing. You will show you are adaptable and a problem solver.

#### Number 5: Performance under pressure skills

You may face time constraints to deliver efficient solutions quickly. The purpose? To show how you work under pressure.

#### Number 6: Industry relevance and familiarity

There are specific challenges in this industry that require implementation of algorithms. Asking questions that require algorithms to solve lets the interviewer know how familiar you are with industry standards. The interviewer will expect you to know which algorithms to use at what time based on the specific problem domain.

### Knowledge Check

#### Why do interviewers ask algorithmic problem-solving questions?

* To gauge a candidate's problem-solving skills, algorithmic thinking, and ability to write efficient code

Wrong answers:

* To assess a candidate's ability to memorize and repeat complex algorithms
* To evaluate a candidate's ability in a specific programming language
* To test a candidate's knowledge of theoretical computer science concepts

These questions focus on evaluating a candidate's problem-solving approach, their understanding of algorithmic principles, and their capability to write clean, efficient, and bug-free code. While programming language ability is important, algorithmic problem-solving questions aim to assess a candidate's problem-solving skills and ability to translate solutions into error-free code.

#### Why is it important for a candidate to demonstrate familiarity with a variety of algorithms in coding interviews?

* To signal to the interviewer that the candidate understands the challenges of the industry and can apply appropriate algorithms to solve them

Wrong answers:

* To impress the interviewer with memorized algorithmic solutions that can be used in every industry
* To showcase a broad understanding of theoretical algorithms that can be used in a variety of fields
* To demonstrate expertise in a wide range of algorithms, even if those algorithms are not applicable to the specific job role

In coding interviews, demonstrating familiarity with algorithms is crucial because it shows the interviewer that you understand the practical requirements and challenges of the job role. Using relevant algorithms indicates that you can effectively address the specific problems encountered in the industry, which is highly valued by employers.

The others are incorrect because they either emphasize irrelevant factors or overlook the importance of tailoring algorithmic solutions to the industry's needs.

#### Which best describes the adaptability skill set?

* The ability to rewrite solutions based on multiple different conditions

Wrong answers:

* The ability to use and implement algorithms to solve a complex problem
* The ability to identify patterns and devise logical solutions
* The ability to face time constraints and deliver efficient solutions quickly

### Summary

In addition to coding skills, there are other essential skills a cloud application developer needs to demonstrate during the interview process. These skills include the following:

* Problem-solving
* Logical thinking
* Adaptability
* Performing under pressure
* Familiarity with relevant industry concepts

## Developer Fundamentals and Interviews

### Pre-assessment

#### What will be the output of the following code?

```
myStack = []

myStack.append("A")
myStack.append("B")
myStack.pop()
myStack.append("C")
myStack.append("D")
myStack.pop()
myStack.pop()

print(myStack)
```

* ["A"]

Wrong answers:

* ["A", "C", "D"]
* ["A", "B", "C", "D"]
* ["D"]

The code uses **append()** to push A and B to the stack. It then uses **pop()** to remove B. Next, it pushes C and D to the stack and uses pop to remove D and C. Thus, only A remains on the stack.

#### What is the correct implementation of a Node class for a linked list?

```
 class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

Wrong answers:

```
class Node:
    def __init__(self, data):
        self.head = data
        self.next = None
```
```
class Node:
    def __init__(self):
        self.head = None
```
```
class Node:
    def __init__(self, data):
        self.data = data
        self.head = None
```

The class **Node** defines a node structure for a linked list with a data attribute and a next attribute that points to the next node in the list or none if it's the last node in the list.

#### What will be the output of the following code?

```
def binary_search_recursive(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2 
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search_recursive(data, target, low, mid-1)
        else:
            return binary_search_recursive(data, target, mid+1, high)

data = [2, 4, 5, 7, 8, 9]
target = 2

print(binary_search_recursive(data, target, 0, 5))
```

* True

Wrong answers:

* 2
* False
* 0

The **binary_search_recursive** function returns True as the target value is found. The given code example demonstrates the usage of this function by searching for the target value 2 in the data list [2, 4, 5, 7, 8, 9] with the initial search range from index 0 to 5.

## Object-Oriented Programming and Other Programming Paradigms

### Object-oriented programming

In **object-oriented programming (OOP)** programming paradigm, everything in your project gets organized as classes and then as tangible and intangible objects. OOP is used for problems that involve many interrelated objects with certain attributes that can change over time, depending on certain conditions. With OOP, you can create classes, define inheritance hierarchies, and achieve polymorphism.

#### Real-world analogy: Homes construction company

```
class House:
    def __init__(self, address, color, roof_type):
        self.address = address
        self.color = color
        self.roof_type = roof_type

    def describe(self):
        print(f"House at {self.address} has {self.color} color and a {self.roof_type} roof.")

    def repaint(self, new_color):
        self.color = new_color
        print(f"House at {self.address} repainted to {new_color}.")
```

Class Definition: The House class defines the blueprint for how a house should be structured in our software. It includes: Attributes (address, color, roof_type). These are like the specifications in the blueprint—details that every house will have. Methods (describe, repaint) are like the instructions or capabilities of the house. For example, repaint allows changing the color of the house.

```
house1 = House("123 Sunset Blvd", "blue", "tile") 
house2 = House("125 Sunset Blvd", "green", "shingle") 

house2.repaint("purple")
```

Each instance of the House class is like building a new house using the blueprint. House1 and house2 are two homes in the community, each built with the same layout but customized with different colors and roof types. House 2 also gets to update its color property by calling on the repaint method.

### Other programming paradigms

#### Imperative Programming

* This programming provides directions or commands in a step-by-step manner.
* An example is a teacher giving directions to their class.

#### Functional Programming

* This programming organizes the code using functions.
* An example is using SQL, in which there can be built-in functions and methods that are automatically applied if and when certain conditions are met. A function is pulled as needed without being as detailed while following a precise order, like imperative programming.

#### Procedural Programming

* This programming focuses on procedures and routines, and is a subset of imperative programming.  
* An example is a fixed script that could be written for steps or procedures that need to be followed in order, like a baking recipe.

### Example interview questions

### OOPs

#### Advantages

* Maintained and updated easier
* Reusable
* More secure with less chance of breaches
* Able to simplify the process through efficiency and accuracy

#### Disadvantages

* Requires that everything be treated as an object—the programmer should work to hone their critical thinking skills
* Requires planning
* Does not provide a solution for all problems

### Classes and objects

Create a class to maintain a student's grade across three subjects (physics, chemistry, and biology) and calculate the student's final grade. The final grade will be the average of the individual grades.

You will need to create a **Student** class with the following:

* Four public properties to record the student's name and grades in the three classes
* Method **final_grade** to return the student's final grade
* Public attributes, properties, and methods

#### Test input

```
student = Student("Ana Carolina Silva", 83, 56, 68)
print(f"{student.name} final grade: {student.final_grade()}")

student = Student("John Stiles", 98, 67, 72)
print(f"{student.name} final grade: {student.final_grade()}")
```

#### Expected output

```
Ana Carolina Silva final grade: 69.0
John Stiles final grade: 79.0
```

#### Solution

```
class Student:
    def __init__(self, name, phy, chem, bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def final_grade(self):
        return((self.phy + self.chem + self.bio)  / 3)
```

### Inheritance

```
class Account:
    def __init__(self, accountholder=None, balance=0):
        self.accountholder = accountholder
        self.balance = balance
        
class SavingsAccount(Account):
    def __init__(self, accountholder=None, balance=0, interestRate=0):
        super().__init__(accountholder, balance)
        self.interestRate = interestRate
```

## Data Structures

### Real-world applications

#### Stacks

Stacks can help a user go forward or backward on their browser webpage, allow your playlist to move to the next song or go back to a previous one, and sort emails in ascending or descending order.

#### Queues

Queues can help an operating system schedule jobs, create the order for cars at a car wash, and handle website traffic (think of when a big-ticket item is launched and there is a queue before entry to purchase).

### Example interview questions

## Stacks

You will be provided a starting class, MyStack, which implements a stack using a Python list. You are asked to do the following:

* Examine the implementation of MyStack and understand how a list is used to support the standard push and pop stack operations.
* Implement a sort_stack() method in the class. The method will sort the elements in the stack such that if you pop and print all the elements, they will come out in ascending order.

#### Test input

```
# create stack and push items in unsorted order  
stack = MyStack()
stack.push(3)
stack.push(43)
stack.push(9)
stack.push(25)
stack.push(12) 

# Sorting the stack 
stack.sort_stack()
 
# Printing the sorted stack 
print("Stack after sorting") 
print([stack.pop() for i in range(stack.size())])
```

#### Expected output

```
Stack after sorting
[3, 9, 12, 25, 43]
```

#### Resources provided

```
class MyStack:  
    def __init__(self): 
        self.stack_list = [] 

    def is_empty(self):  
        return len(self.stack_list) == 0  

    def peek(self):  
        if self.is_empty():  
            return None  
        return self.stack_list[-1]  

    def size(self):  
        return len(self.stack_list)  

    def push(self, value):  
        self.stack_list.append(value)  

    def pop(self):  
        if self.is_empty():  
            return None  
        return self.stack_list.pop() 

    # placeholder for your new method
    def sort_stack(self):
        pass
```

#### Solution

```
class MyStack:  
    def __init__(self): 
        self.stack_list = [] 
 
    def is_empty(self):  
        return len(self.stack_list) == 0  
 
    def peek(self):  
        if self.is_empty():  
            return None  
        return self.stack_list[-1]  
 
    def size(self):  
        return len(self.stack_list)  
 
    def push(self, value):  
        self.stack_list.append(value)  
 
    def pop(self):  
        if self.is_empty():  
            return None  
        return self.stack_list.pop() 
  
    def sort_stack(self):
        self.stack_list.sort(reverse=True)
```

### Queues

Implement a queue using only stacks for data storage. This is a challenging problem because queues and stacks operate nearly opposite to each other. In a queue, the first element in will be the first one out (FIFO). In a stack, the last element in will be the first one out (LIFO).

You will be provided a MyStack class to use for your solution. You are asked to do the following:

Implement a **MyQueue** class that will use the provided **Stack** class in its implementation.
Implement the **enqueue()** and **dequeue()** standard queue methods.

* **enqueue( )** inserts a value into the queue.
* **dequeue( )** extracts and returns the oldest value in the queue.

#### Test input

```
queue = MyQueue()
for i in range(5):
    print("Enqueued {}".format(i+1))
    queue.enqueue(i+1)
print("----------")
for i in range(5):
    print("Dequeued {}".format(queue.dequeue()))
```

#### Expected output

```
Enqueued 1
Enqueued 2
Enqueued 3
Enqueued 4
Enqueued 5
----------
Dequeued 1
Dequeued 2
Dequeued 3
Dequeued 4
Dequeued 5
```

#### Resources provided

You are provided with the MyStack class to be used in your solution. It has the standard push and pop methods expected in a stack. You can use MyStack without modifications. 

#### MyStack

```
class MyStack:  
    def __init__(self): 
        self.stack_list = [] 

    def is_empty(self):  
        return len(self.stack_list) == 0  

    def peek(self):  
        if self.is_empty():  
            return None  
        return self.stack_list[-1]  

    def size(self):  
        return len(self.stack_list)  

    def push(self, value):  
        self.stack_list.append(value)  

    def pop(self):  
        if self.is_empty():  
            return None  
        return self.stack_list.pop() 
```

#### MyQueue prototype

```
class MyQueue:
    # Can use size from argument to create stack 
    def __init__(self): 
        pass

    # Inserts Element in the Queue 
    def enqueue(self, value): 
        pass

    # Removes Element From Queue 
    def dequeue(self): 
        pass
```

#### Solution 1

The following is the first complete solution. In this solution, most of the work is done in the enqueue method.

```
class MyQueue: 
    def __init__(self):
        self.main_stack = MyStack()
        self.temp_stack = MyStack()

    # Inserts Element in the Queue 
    def enqueue(self, value): 
        # if the queue is empty, just push the first value
        if self.main_stack.is_empty(): 
            self.main_stack.push(value)
        # else, the queue is not empty
        else:
            # pop all the elements in the main stack while pushing them into a temporary stack
            while not self.main_stack.is_empty(): 
                self.temp_stack.push(self.main_stack.pop()) 
            # now push the latest item into the main stack
            self.main_stack.push(value)
            # pop all the elements in the temp stack while pushing them back into the main stack
            while not self.temp_stack.is_empty(): 
                self.main_stack.push(self.temp_stack.pop()) 

    # Removes Element From Queue 
    def dequeue(self): 
        # If stack empty then return None 
        if self.main_stack.is_empty(): 
            return None 
        value = self.main_stack.pop() 
        return value
```

## Linked Lists and Heaps

