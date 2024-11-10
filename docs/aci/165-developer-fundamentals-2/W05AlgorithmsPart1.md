# Algorithms Part 1

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to repo's main [README.md](../../../README.md)

### Pre-assessment

#### Which of the following are examples of algorithms? (Select TWO.)

* The steps of a recipe for making pancakes.
* A procedure checklist for a pilot experiencing engine failure.

Wrong answers:

* A list of food you need to buy at the grocery store.
* The list of all birthdays for your family and closest friends.
* A log of the time you sleep and wake up each day.

An algorithm is a detailed list of steps to be followed to obtain a specific output. The steps in a recipe and the checklist for a pilot to remedy an engine failure are examples of algorithms, which give detailed instructions or steps to follow.

The list of foods and birthdays are lists. Although procedures often appear in a numbered list, they represent instructions to be followed in a particular order, not just items that have something in common.

The log of the time you went to sleep and woke up could be represented in many different data structures. However, it still does not represent a detailed list of procedures to follow, so it is not an algorithm.

#### What is recursion?

* A concept in computer science where a function calls itself in its own definition.

Wrong answers:

* A concept in computer science used to optimize algorithms.
* A concept in computer science used for sorting elements in an array.
* A system in computer science for managing memory in a computer program.

Recursion is a concept in computer science where a function calls itself in its own definition. Recursion works by breaking up a problem into smaller and smaller subproblems of itself.

#### Which algorithm is also called a sequential search algorithm? 

* Linear search algorithm

Wrong answers:

* Quick search algorithm
* Binary search algorithm
* Selective search algorithm

A linear search algorithm is also called a sequential search algorithm because it tries to search the desired element by going over the list sequentially.

### Algorithms Overview

**Algorithms** consist of a **series of specific steps**. They are used to solve common problems in a repeatable way.

* **Language:** Algorithms are **not dependent on the specific programming language you are using**. Instead, algorithms are written in natural language or pseudocode, and can be used to write programming code in any programming language. Pseudocode is a detailed, yet readable, description of what a computer program or algorithm should do.
* **Finite:** Algorithms must have a **finite number of steps**. They must be able to start and stop. If using a loop, to avoid an **endless loop**, an algorithm must test for the end and provide a way to exit the loop.
* **Precise:** An algorithm must be **clear and precise**. Famed computer scientist Donald Knuth called this "principle definiteness." Algorithms must **not have multiple interpretations**, so anyone who performs the steps will get the same result.
* **Inputs:** Algorithms take **well-defined** inputs such as an unsorted list, a binary search tree, or a directed graph. These inputs are used within the steps of the algorithm to solve a problem. Sometimes, the inputs are **hard-coded** into the algorithm. In such cases, the algorithm would take no inputs. Without inputs, the output would be constant and never change.
* **Outputs:** The output of an algorithm represents the solution to a problem. Example outputs include a sorted list, returned data point, or balanced tree. Outputs can be of **any type**, but they should be **specifically defined**.
* **Effectiveness and feasibility:** If an algorithm yields an incorrect solution to the problem it is given, the algorithm is faulty. However, as you saw with the traveling salesperson problem, algorithms sometimes produce a solution that might be **correct but not optimal**. This is due to consideration of computer resources, time, or money. Selecting the correct algorithm for your dataset is an important task for all programmers.

### Algorithms provide repeatable solutions

Because of their repeatable nature, algorithms allow you to use pre-defined processes to solve problems, where possible. This way, you avoid having to solve every problem from the beginning every time you encounter it.

Programmers use algorithms to focus on implementation, rather than problem solving.

### Algorithmic thinking develops transferable skills

Learning to create and use algorithms helps you develop transferable skills sought after by many employers in project management, resource allocation, data analysis, and other professions.

#### Detail-oriented

Computers need all the details spelled out completely. Creating algorithms that a computer can perform requires you to focus on every detail of the process, no matter how small. 

#### Problem-solver
Algorithms are built by breaking down larger problems into smaller, more manageable components that can be solved efficiently. This problem-solving skill can be used in many fields. 

#### Analytical

Creating and evaluating algorithms helps you focus on performance of specific solutions. This ability to analyze different options and select the ones that have optimal results is an important analytical skill.

#### Time and resource management

Selecting the right use of algorithms for the dataset you are working with helps you learn to manage time and computing resources wisely.

### Factorial algorithm example

* **Result** – This is the variable that houses the final answer after you have calculated the factorial of the number.
* **n** – This is the value you input as n for n!.
* **x** – This is a variable that cycles through the loop, increasing each time it cycles. Its value will be multiplied by the result with each cycle.

You initialize the result to 1. That will take care of the multiplication with 1. Then, for your algorithm, you can start by multiplying by 2, then 3, then 4, and so forth, until you reach n.

The algorithm is as follows:

1. **Initialize:** 
```
     result = 1
     n = 1
```
2. **Loop:**
```
     For every value of x from 2 to n 
          change result to (result*x)
```
3. **Return:** Result

Although this algorithm is not written in Python or any programming language, a programmer could use the steps outlined to create code in their chosen language.

### Common computer algorithms

You now understand the basics of algorithms and their applications to real-world problems. In the coming topics, you will explore some computer algorithms that create repeatable processes for solving common data operations, such as the following:

* Searching for and retrieving data
* Inserting new data
* Deleting old data
* Sorting data into an ordered structure
* Updating and balancing data structures after an operation
* Traversing graphs and tree data structures

Remember that there are common elements in algorithms that perform a similar function, such as sorting data.

### Knowledge Check

#### Which of these are examples of an algorithm? (Select TWO.)

* An instruction manual with images of parts and assembly order showing how to assemble a new bicycle
* A job aid outlining specific steps to follow to log in to the company intranet and change insurance benefits selections

Wrong answers:

* A list of soccer games played by the local high school, along with detailed statistics about each player's performance
* A job aid giving phone numbers of all coworkers and the days they work in the office, along with the job title and areas they support
* A glossary of terms used in a learning module, complete with possible applications of the terms that might be encountered in a job

The other three items (list of soccer games, list of coworkers phone numbers, and a glossary of terms) might be useful for solving a problem. However, they are just lists and not specific steps that need to be taken to get a particular output, so they do not qualify as algorithms.

### Use the following algorithm to calculate the unpaid balance on a credit card that accrues monthly compound interest

**Initialize:**

* **Balance** = (input credit card balance at beginning of term)
* **Int_rate** = (input monthly interest rate)
* **Term** = (input number of months the balance is carried)
* **Total_interest** = 0

**Loop:**

* For every **month** from 1 to **term**
 * **Change Balance to (Balance + (Balance * Int_rate))**

**Return:  Balance**

For one credit card user, the original balance owed was $100, and their monthly interest rate was .01 (1 percent).

What would be the total balance owed at the end of 3 months if no payments were made toward the balance?

* $103.03

Wrong answers:

* $130
* $103
* $133.33

Each month, the previous month's balance is used to calculate the interest paid. This means that the amount paid in interest will increase every month if no payments are made.  

The new balance each month is calculated by adding the interest paid that month to the previous balance.

* Month 1: Balance = (100 + (100 * .01)) = 101
* Month 2: Balance = (101 + (101 * .01)) = 102.01
* Month 3: Balance = (102.01 + (102.01 * .01)) = 103.0301.

Because this is dealing with dollars and cents, the last two digits can be truncated and the balance represented as $103.03.

#### What is a basic requirement for a well-written algorithm?

* It should have a finite number of steps.

Wrong answers:

* It should be written in Python code.
* It should include vague steps open to interpretation by the programmer.
* It should not contain loops or cycles.

A well-written algorithm can be written in pseudocode or natural language. It should be independent of any specific programming language, and it can be implemented by the programmer using the syntax of any language, not just Python.

Algorithms often contain loops or cycles, but they must have a way to exit the cycle when the end of the structure is reached to prevent endless loops.

### Recursion Overview

Recursion is a concept in computer science where a function calls itself within its own definition. It is a method of solving problems that involves breaking down a problem into smaller and smaller versions of itself. This repeats until you arrive at the base case, which ends the recursion.

### When to use recursion

#### Tree-like structure

In all recursion problems, it must be possible to decompose the original problem into smaller instances of the same problem. This recursive process makes a tree-like structure. In a tree, a node branches into other nodes. Each branching point looks similar to the foot of a smaller subtree. By finding the solutions to subproblems, you find the solution to the main problem.

#### Backtracking

In backtracking, an algorithm tries several solutions to a problem until it finds one that works. For example, in a maze, you take each path one step at a time.  When you reach a dead end, you backtrack to a previous decision point and continue on a new path until you find a solution that works. Recursion naturally fits the structure of a backtracking problem.

#### Practicality

Although some problems naturally have a tree-like structure or backtracking, it is not always practical to use recursion. For example, a recursive tree might have so many levels of branches that it risks causing a stack overflow error. This error occurs when the call stack exceeds the amount of available memory and, in such cases, a naïve recursive approach is not the best option. Additionally, if you notice so many repeated subproblems that your code efficiency is terrible, a naïve recursive approach is not the best choice.

### Advantages and disadvantages of recursion

| Advantages | Disadvantages |
| ---------- | ------------- |
| Recursion can make a complex problem more manageable by breaking it into smaller subproblems. | For most problems, it is more difficult for the average programmer to solve a problem using recursion. It is often more convenient to write code using loops. |
| Some algorithms naturally lend themselves well to recursion because they are recursive in nature. | For some problems, a recursive solution, although possible, will be more awkward than elegant compared to solving the same problem in a different way. |
| Recursion can often reduce the amount of code needed to solve a problem, making the code appear more elegant and concise. | Recursive algorithms often have a worse performance because of the amount of memory and time that is taken when making recursive calls. |
| Understanding recursion helps programmers understand other programming techniques, such as dynamic programming. | Recursive algorithms are susceptible to stack overflow errors and can be difficult to debug. |

### Recursive thinking

Recursive thinking, or the ability to see a problem in terms of smaller instances of itself.

### Classic Recursive Examples

* Factorials
* Fibonacci numbers

### How to write a recursive function

The structure of a recursive function typically involves an if-else statement, which separates the function into two parts: the base case and the recursive case.

The following example code shows how this is structured in Python.
```
if answer is known:
    # base case
    return answer
else:
    # recursive case
    make a recursive call with a modified answer
```

#### Base case

The base case in recursion determines when the recursion will stop. When a base case is reached, a definitive answer is returned immediately, given the inputs of the function call. This leads to the solution to the next subproblem and so on, as the function return is made to the previous call and the recursion unwinds.

Determining the base case is a necessary step because without it, a function call will call itself indefinitely. This will lead to a stack overflow error.  

For factorial(3): In the context of factorials, the base case is factorial(0), which is defined to be 1. Each time a recursive call is made, the function will check if the input is 0. If the input is 0, the function will return 1. If it is not 0, you enter the recursive case where the function will continue to make recursive calls to itself until the base case is reached. 

The base case is factorial(0), which returns 1.

#### Recursive case

The recursive case is the part of the function that calls itself. This part of the function is important because it breaks down the main problem into smaller and smaller problems until the base case is reached. Then, it combines the solutions of the smaller problems together until the solution to the original problem is reached.

The leap of faith in recursion means it is not necessary to try to understand all of the different recursive functions that are being called in this step. You just need to understand the parameters and trust that your code will work itself out.  

For a factorial(3). Recursive behavior continues until factorial(0) does not make a recursive call. Then, the call stack unwinds, each call to factorial returning its answer to the caller until factorial(3) returns to main.

Factorial(3) calls factorial (2), which calls factorial(1).

### Call stack

The call stack is what a program uses to keep track of method calls. It is a data structure that stores the local variables, the values of the parameters of the problem, and the return address.

The call stack is made up of individual units known as stack frames. Each stack frame corresponds to a single function call and contains specific information related to that call. Because there are no variables for the call stack, the call stack can be hard for programmers to visualize. When each new recursive function is called, another invisible frame object is added to the call stack. This process works behind the scenes and is managed by the programming language itself.

The call stack is important because it is a limited resource. If the recursion goes too deep, there will be too many saved local variables. If you run out of space in the call stack, your program crashes.

### How to determine the base case and recursive case

To determine when a recursion needs to stop and the parameters for a problem, ask yourself the following three questions:

1. What is the base case?
2. What are the arguments that are passed to the recursive function call? 
3. How do these arguments become closer to the base case?

The base case defines the stopping condition for the recursive call to stop. After the function reaches the base case, it starts to unwind toward the solution for the problem. Python protects the call stack from consuming all the available memory with a setting for the maximum recursion limit. Reaching this limit will cause a RecursionError because the function will call itself indefinitely.

The second and third questions help you to determine how to write your recursive case. If you understand how to solve your problem for smaller values so that it reaches the base case, the recursive function can work for larger values, as well.

All problems that can be solved using recursion can also be solved with a loop and a stack. Thinking about a problem iteratively first might help you understand the base case and the recursive case. It is not necessary to solve all problems iteratively first. However, knowing that the parameters are similar to the iterative method will help when solving more complex problems with recursion.

### Example 1: Factorials

A factorial is a mathematical operation that multiplies a given number by every whole number less than it down to 1. It's often shown by an exclamation point (!) after a number.

One common example is permutations, which refer to the various ways a set of objects can be arranged or ordered. Factorials can also be used to calculate probability or series expansion.

An example of a permutation problem is arranging books on a shelf. If there are n different books on a shelf, how many different ways can you arrange the books?

#### Iterative solution

```
# Iterative example for factorial
def factorial(n):
    # Iterative case: multiply each number from 1 to n
    product = 1
    for i in range(1, n + 1):
        product = product * i
    return product

print(factorial(5))
```

1. When the **factorial(5)** function is called, a new frame is pushed onto the call stack. This frame contains the local variables and parameters for the **factorial** function. In this case, the parameter n is set to 5.
2. The local variable **product** is initialized to 1 in the function's frame on the call stack. The function then enters a **for** loop, which iterates from 1 to n. For each iteration, the value of i is multiplied with the current value of **product**, and the result is stored in **product**.
3. After the **for** loop has finished running, the final value of **product** is the factorial of n. This value is returned by the function.

In the iterative implementation of the factorial function, only one function call gets added to the call stack. Nothing else is added to the call stack because the function factorial is called once and performs its calculations in a loop. It is not necessary to push any new function calls or frames onto the stack.

#### Recursive solution

```
# Recursive example for factorial
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n < 2:
        return 1
    else:
        # Recursive case: n! = n * (n-1)!
        return n * factorial(n-1)

# Calculate the factorial of 5
print(factorial(5))
```

1. The base case is set to if **n < 2: return 1**. This means that when the recursive function reaches 1, the recursion will stop. In this case, factorial(1) returns 1.  
2. If n is not less than 2, the function calls itself with the argument **n-1**. This is the recursive case: return **n * factorial(n-1)**. This means that the factorial of **n** is calculated as **n** times the factorial of **(n-1)**.
3. When **factorial(5)** is called, the function does not immediately return a value. Instead, it makes a recursive call to *factorial(4)*. This process continues until the base case is reached. The following example is how the stack of calls looks:
 * factorial(5) first call, waits for factorial(4)
 * factorial(4) called by factorial(5), waits for factorial(3)
 * factorial(3) called by factorial(4), waits for factorial(2)
 * factorial(2) called by factorial(3), waits for factorial(1)
 * factorial(1) called by factorial(2), hits the base case and returns 1
4. After the base case is hit, the stack starts to unwind. In the following example, each waiting function call now has the result from its recursive call and can complete its computation:
 * factorial(1) returns 1 to factorial(2)
 * factorial(2) computes 2*1 = 2, returns 2 to factorial(3)
 * factorial(3) computes 3*2 = 6, returns 6 to factorial(4)
 * factorial(4) computes 4*6 = 24, returns 24 to factorial(5)
 * factorial(5) computes 5*24 = 120, returns 120 to the original call
5. Finally, the original call **print(factorial(5))** prints the result **120**. 

#### Tracing what happens to the call stack

Tracing involves tracking and recording the sequence of function calls, operations, and values of variables during the running of a program. 

Recursion is built on the basic idea that a function can call itself. Each time a recursive function is called, it pushes a new frame object to the call stack. Because a recursive function calls itself, more and more frame objects will be added to the call stack until it reaches the base case. Then, the function will unwind and pop a frame object from the call stack one at a time. The computer handles stacks implicitly, but each new frame added to the call stack adds more time and memory.

When factorial(5) is called, it initiates the call stack. To calculate factorial(5), factorial(4) is called. This also adds a new frame object to the call stack. A total of five frame objects are added to the call stack before it reaches the base case. The base case of factorial(1) is 1. After it reaches the base case, it starts to unwind until it returns the answer.

#### Inefficiency of calculating a factorial with recursion

When compared with the iterative method, you might have noticed that calculating a factorial with recursion is much less efficient. With the iterative method, only one frame object starts the call stack. The looping happens within that frame. With recursion, on the other hand, each time a recursive function is called, another frame is added to the call stack. Each recursive call requires additional memory. With a factorial of 5, five frames are added to the call stack. 

In Python, there is typically a default limit of 1,000 items that can be added to the call stack. If you try to solve a problem using recursion that exceeds 1,000 calls, you will get a RecursionError. This is Python's way of telling you that you have exceeded the maximum recursion depth. You might also get this error if you forget to define your base case. In that case, your recursive function is invoked indefinitely and will crash when it reaches 1,000 invocations.

### Example 2: Fibonacci numbers

The sum of a Fibonacci number is calculated by getting the sum of the two previous Fibonacci numbers.  

The Fibonacci sequence begins with the numbers 0 and 1, and then continues from there. The next number in the sequence is the sum of the previous two numbers. This creates the sequence 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, and so on, forever.

A Fibonacci number has two variables for each calculation. When a recursive function calls itself twice, it makes a tree-like structure.

The tree-like structure of the fifth Fibonacci number has five levels, with each level representing a Fibonacci number. The top node represents the number 5, and it branches out into smaller parts that follow the Fibonacci sequence.

#### Tree-like structure

A tree-like structure is one of the clues that recursion can be used. **The tree-like diagram is in the solution and not in the algorithm itself**. In this example, to calculate the fifth Fibonacci number, it is necessary to calculate the fourth Fibonacci number and the third Fibonacci number first. However, to calculate the fourth Fibonacci number, you also need to calculate the third Fibonacci number and the second Fibonacci number. This pattern continues until you reach the base case. One recursive call for Fib(5) will lead to 15 items being placed on the call stack before it reaches the base case and starts to unwind.

#### Iterative solution

Although Fibonacci numbers are recursive in nature, it is also possible to find the solution using iteration. Solving a problem iteratively can help determine the base case, in addition to both the arguments that are passed to the base case. Unlike the factorial example, which only had one variable, an iterative solution will use a for loop and two variables.

```
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print(fib(10))
```

1. The function **fib(n)**takes an integer **n** as input, which represents the position in the Fibonacci sequence that you want to calculate.
2. The variables **a** and **b** are initialized to 0 and 1, which are the first two numbers in the Fibonacci sequence.
3. The function then enters a loop that runs n times. In each iteration of the loop, it updates **a** and **b** to be the next two numbers in the Fibonacci sequence.
4. After the loop has run **n** times, **a** will be the nth number in the Fibonacci sequence, so the function returns a.
5. The line **print(fib(10))** calls the function with n set to 10, and prints the result. This will print the tenth number in the Fibonacci sequence, which is 55.

#### Recursive method

```
def fib(n):
    # base case: the first Fibonacci number is 0
    if n == 0:
        return 0
    # base case: the second Fibonacci number is 1
    elif n == 1:
        return 1
    # recursive case
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(10))
```

In the recursive fib() function, the base case happens when n is 0 or 1. In this case, the function returns 0 or 1, because the first and second Fibonacci numbers are 0 and 1. Any other case is a recursive case, so the value that is returned is the sum of fib(n - 1) and fib(n - 2). As long as the original n argument is an integer greater than 0, these recursive calls will eventually reach the base case and stop making more recursive calls.

#### Inefficiency in the recursive Fibonacci sequence

The Fibonacci algorithm using naïve recursion is very inefficient. It repeats so many of the same subproblems over and over again that the larger the number, the exponentially slower the algorithm performs.

To calculate the fifth Fibonacci number, notice that fib(3) is called twice, fib(2) is called three times, and fib(1) is called five times. This slows the overall algorithm because of repeated calculations.

Dynamic programming is a programming tool that optimizes recursion to significantly improve the efficiency of an algorithm by storing repeated subproblems in memory.

### Comparing iteration and recursion

Both iteration and recursion involve repetition and can occur infinitely. The following table shows the key differences between iteration and recursion. 

| Iteration | Recursion |
| --------- | --------- |
| Represents a control structure where user-defined repetition occurs.| Achieves repetition through repeated function calls. |
| Stops when the loop continuation condition fails. | Stops when a base case is met. |
| Modifies a counter or condition until the loop continuation condition is no longer met. | Streamlines the original problem through each recursive call until the base case is reached. |
| Occurs within a loop, so no extra memory is allocated for each iteration. | Adds a new frame object to the call stack with each recursive call, which can consume a significant amount of memory. |
| Makes efficient use of processor's operating time, generally. | Can increase the processor's operating time due to the overhead of repeated function calls. |

Compared to iteration, recursive code often runs more slowly. This is because the overhead of a loop is smaller than the overhead for many function calls and returns. At the same time, if it is more convenient to think about an algorithm using recursion, you can code it as a recursive method. This is because sometimes the reduction in efficiency does not outweigh the advantage of readable code that is uncomplicated to debug.

## Example: The Tower of Hanoi

The Tower of Hanoi is a puzzle that has three rods and several stacked disks. In the puzzle, the largest disk is on the bottom, and there are progressively smaller disks stacked above each disk.

In the Tower of Hanoi puzzle, each disk has a hole in the center so it can be moved from one rod to another. The goal is to move all of the disks from the first rod to the last rod in a way where the largest disk stays on the bottom. The disks continue decreasing in size until the smallest disk, which is at the top.

To move the disks, the player must follow three rules.

* Only move one disk at a time.
* Only move the disks to and from the top of a rod.
* You cannot place a bigger disk on top of a smaller disk.

Figure out how to solve the Tower of Hanoi for one to three disks and how to arrive at the base case. Then you can use that information to write a recursive function that calls itself to solve the Tower of Hanoi for many disks. Thinking about the problem using recursion almost feels like cheating. When a problem is recursive in nature, you only need to figure out how to solve a smaller version of the same problem. Then, you apply it to the larger problem.

### Solve for the base case and notice patterns

#### Solve for one disk

Solving for one disk gives you the base case. With one disk, the solution is very straightforward. Move the disk from the starting rod to the final rod. In this case, the base case is 1.

#### Solve for two disks

Solving the Tower of Hanoi for two disks is also straightforward. Move the top disk to the helper rod and then the second disk to the final rod. After you have done this, solve for the smallest disk by putting it on top of the second disk. 

#### Solve for three disks

When you solve for three disks, it is more complicated. To solve for three disks, you must solve for two disks, but this time they will be placed on the helper rod. After you have solved for two disks on the temporary rod, you will be able to move the third disk over to the final rod. Then you will repeat the pattern to solve for two disks, but this time by solving for two disks again on the final rod.

To solve a tower of n disks from the start rod to the end rod, you must do the following.

1. Solve the n-1 disks by moving those disks to the helper rod.
2. Move the nth disk from the start rod to the end rod.
3. Solve the n-1 disks puzzle by moving those disks from the helper rod to the end rod.

As mentioned previously, the recursive case is also known as the leap of faith. It might be straightforward to physically solve the Tower of Hanoi puzzle for three to four disks and understand each recursive call that is made. However, the more disks there are, the harder it becomes to trace all of the recursive calls. It is reassuring to remember that it is not necessary to track each recursive call that is being made. Just trust that recursion is happening in this step.

### How to write the Tower of Hanoi code in Python

To write the Tower of Hanoi solution in code, start by defining the function **tower_of_hanoi** and determining the base case. This function takes four arguments: **number_of_ disks**, **source**, **destination**, and **helper**. The base case is indicated in the line **number_of_disks == 1**. When the function reaches the base case, it prints a message indicating that this disk is moved from the source rod to the destination rod.

```
def tower_of_hanoi(number_of_disks, source, destination, helper):
    moves = 1
    if number_of_disks == 1:
        # Base case: when there is only one disk left to move
        print(f"Move disk {number_of_disks} from rod {source} to rod {destination}")
```

Next, write the recursive case. If there is more than one disk to move, the function first recursively moves all but the last disk from the source rod to the helper rod. To do this, it uses the destination rod as the new helper rod. Then, it moves the largest disk, or the the last remaining disk on the source rod, from the source rod to the destination rod. Finally, it recursively moves the stack of disks from the helper rod to the destination rod, using the source rod as the new helper rod. In the code, also add a function to keep track of the total number of moves made in each step.

```
  else:
        # Recursive case: when there are more disks to move than 1
        # move all but last disk from source to helper rod
        # destination thus becomes the new helper rod
        moves += tower_of_hanoi(number_of_disks - 1, source, helper, destination)
        # move the largest disk from the source to the target
        print(f"Move disk {number_of_disks} from rod {source} to rod {destination}")
        # move tower reduced by one from helper rod to the target
        moves += tower_of_hanoi(number_of_disks - 1, helper, destination, source)
```

Finally, write the driver code to solve for five disks, in addition to printing the total number of moves. This part of the code calls the main function with a specific number of disks and names for the rods. In this case, it solves the problem for five disks, with **'A'** as the source rod, **'C'** as the destination rod, and **'B'** as the helper rod.

```
# Driver code
n = 5
result = tower_of_hanoi(n, 'A', 'C', 'B')  # A, C, B are the name of rods

# Print the total number of moves
print(f"Total moves: {result}")
```

### [Run the Tower of Hanoi puzzle in Python](./W05HanoiPuzzle.py)

The output:

```
Move disk 1 from rod A to rod C
Move disk 2 from rod A to rod B
Move disk 1 from rod C to rod B
Move disk 3 from rod A to rod C
Move disk 1 from rod B to rod A
Move disk 2 from rod B to rod C
Move disk 1 from rod A to rod C
Move disk 4 from rod A to rod B
Move disk 1 from rod C to rod B
Move disk 2 from rod C to rod A
Move disk 1 from rod B to rod A
Move disk 3 from rod C to rod B
Move disk 1 from rod A to rod C
Move disk 2 from rod A to rod B
Move disk 1 from rod C to rod B
Move disk 5 from rod A to rod C
Move disk 1 from rod B to rod A
Move disk 2 from rod B to rod C
Move disk 1 from rod A to rod C
Move disk 3 from rod B to rod A
Move disk 1 from rod C to rod B
Move disk 2 from rod C to rod A
Move disk 1 from rod B to rod A
Move disk 4 from rod B to rod C
Move disk 1 from rod A to rod C
Move disk 2 from rod A to rod B
Move disk 1 from rod C to rod B
Move disk 3 from rod A to rod C
Move disk 1 from rod B to rod A
Move disk 2 from rod B to rod C
Move disk 1 from rod A to rod C
Total moves: 31
```

### Remember this

The tree-like structure for solving the Tower of Hanoi puzzle makes it a prime candidate for recursion. When you think about writing a recursive function, ask yourself the following questions to set up your recursive function:

* What is the base case?
* What are the arguments that are passed to the recursive function call? 
* How do these arguments get closer to the base case?

First thinking about a problem iteratively and then seeing how to solve the base case will help you write a recursive function.

## Backtracking

Backtracking is a fundamental strategy in computer science and problem-solving. In backtracking, an algorithm tries many different solutions to a problem until it finds one that works. Consider a maze, for example. When solving a maze, if you try a path and it does not work, you **back up** and try a different path. Backtracking is used with recursion, but it is not always necessary to try out every possible solution. Although this is not an optimal technique, backtracking is especially useful when solving puzzles and games where there is no time limit.

### Backtracking examples

#### Paths through mazes

Mazes are a common example of backtracking. You start at one point, and your goal is to get to the exit. You explore different paths in the maze, and if you hit a dead end, you go back and try a different path and continue this pattern until you find the exit.

#### Sudoku puzzle

Sudoku is a game where you have a 9x9 grid, and you need to fill it with numbers from one to nine. The challenge is that each row, each column, and each 3x3 box within the grid must contain all the numbers from one to nine, and cannot repeat. When solving, you continually check multiple possibilities that will satisfy multiple criteria until you find the solution that works.

#### 8-Queens Problem

The 8-Queens problem is a puzzle that is solved on a chessboard. If you have an 8x8 chessboard and you need to place eight queens on it, the challenge is that no queen should be able to attack another. This means no two queens can be on the same row, column, or diagonal. This problem can be solved by placing one queen at a time and then checking and backtracking as needed. The 8-Queens problem is a specific instance of the more general N-Queens problem.

### Backtracking uses recursion

To recognize recursion and break the problem into smaller versions of itself, it helps to visualize the tree-like structure in the solution to the problem. In a maze, for example, you can think of the paths as a recursive, self-similar shape. The maze branches into different paths, and when it reaches a dead end, it must backtrack to an earlier branching point.

A maze's path has a tree-like structure. Even though there is a visual difference between maze paths and tree-shaped paths, their branching points are related to each other in the same way, and mathematically, they are the same.

Backtracking involves building a solution one step at a time, removing the solutions that do not work, and then building further. Although a maze is a classic example of backtracking, this approach can be used with many different types of problems.

Some types of naturally recursive problems that can be solved using backtracking include the following:

* Finding one or more solutions to a decision problem
* Solving optimization problems
* Finding all of the solutions to an enumeration problem

Backtracking is conveniently implemented with recursion because the runtime stack keeps track of the choices that led to a given point. When a choice leads to a dead end, the algorithm can backtrack to the previous choice by returning from the current recursive call. This pops the current call off the stack and returns the program to the previous call. In this way, you undo the last choice and allow the algorithm to try a different path.

### N-Queens problem

The N-Queens problem is a puzzle that involves placing N chess queens on an N×N chessboard so that no two queens threaten each other. In other words, no two queens should share the same row, column, or diagonal line.

To clarify this problem, we will examine a 4x4 chessboard with four queens. The goal is to reach a solution step-by-step. When a placement fails, try another path. Continue the process until you arrive at a solution that works.

#### Visual example

Start with a queen in the upper-left corner in row 0, position 0. You will place each queen systematically one by one and then check to see if the solution is still working after each new placement. After checking each of the parameters (vertical, horizontal, and diagonal), you will decide if you can continue with the next queen or need to backtrack. If a placement does not work, you go back to the last position that did work and change it to the next possible placement. Continue until you have successfully placed the final queen in the last row. Sometimes, you might only have to backtrack to the last step, but in other cases, you might have to backtrack all the way to the beginning row.

After placing the first two queens in the first row, first column and second row, third column, you realize you cannot place the third queen in the third row. There is no cell in the third row out of reach of the first two queens. You have to find a better placement for the second queen.

To continue the problem, you must backtrack. Each time you try new spots, you are making recursive calls. Each time you backtrack, you pop those recursive calls off the stack and continue from a previous point.

You've backtracked and put the second queen in row 2, column 4. Now the third queen can go in row 3, column 2. But when you try to place the fourth queen, you see there is no cell in the fourth row safe from the other three queens. You have to backtrack again.

Now, back at the second row, you try the queen in the fourth position. This works for the second and third rows for placing additional queens. However, when you reach the fourth row, the placement fails. A queen cannot be placed in this row. Again, you must backtrack to find another solution. You pop a few of the recursive calls off the stack and backtrack to the third row. Unfortunately, the third row has no spots that work. Again, you must backtrack, but this time, you pop almost all of the recursive calls off the call stack and return back to the first row.

You backtrack quite a bit and put the first queen in row 1, column 2; the second queen in row 2, column 4; the third queen in row 3, column 1; and the fourth queen in row 4, column 3. The solution has been found.

The solution for the the N-Queens problem with four queens is one queen in the first row, second column. A second queen is in the second row, fourth column. A third queen is in the third row, first column, and the fourth queen is in the fourth row, third column.

#### Explanation

You might have noticed that you were naturally able to use recursion and backtracking to arrive at an additional solution for the 4-Queens problem. With recursion, you were able to break down the problem into smaller, more manageable parts. By using backtracking, you could solve those parts incrementally, one by one. When a solution did not work, you were able to backtrack and continue to systematically solve by choosing the next placement.

### N-Queens problem in Python

The two constants are **QUEEN** and **FREE_SPACE**. These two constants are used to represent the state of a cell in the chessboard.

Continue by creating a recursive solver function. Write a function **_queens_helper(board, row)**. This function tries to place a queen in each column of the current row and then recursively checks if this leads to a solution. If placing a queen in a certain position leads to a solution, it returns **True**. If it doesn't, it removes the queen from that position (backtracks) and continues to the next column. If it has tried all columns in the current row and none leads to a solution, it returns **False**.

```
QUEEN = 'Q'
FREE_SPACE = '-'

def _queens_helper(board, row):
    """
    Recursive solver function

    Parameters:
    - board(List[List[int]]): chess board
    - row(int): current row

    Returns:
    - bool
    """
    if row >= len(board):
        return True

    for col in range(len(board)):
        if _is_valid_position(board, col, row):
            # Place the queen on given position
            board[row][col] = QUEEN

            if _queens_helper(board, row + 1):
                return True

            # If the placement doesn't lead to solution, remove the queen
            board[row][col] = FREE_SPACE

    return False
```

