# Dynamic Programming

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to repo's main [README.md](../../../README.md)

## Dynamic Programming

### Pre-assessment

#### What is the best definition of *dynamic programming*?

* Dynamic programming is a method for solving complex problems by breaking them down into simpler, overlapping subproblems and storing the results of these subproblems.

Wrong answers:

* Dynamic programming is a method for solving problems by continuously changing the parameters until the optimal solution is found.
* Dynamic programming is a method for solving problems by using a single, static algorithm that does not change based on the problem's parameters.
* Dynamic programming is a method for solving problems by using a random approach to explore all possible solutions.

Dynamic programming is a method for solving complex problems by breaking them down into simpler, overlapping subproblems and storing the results of these subproblems to avoid repeated calculations. Subproblems can be solved from the bottom-up using tabulation or from the top-down using memoization.

#### What are the two main approaches for dynamic programming? (Select TWO.)

* Tabulation
* Memoization

Wrong answers:

* Recursion
* Polymorphism
* Iteration

The two main approaches to dynamic programming are a top-down approach using memoization and a bottom-up approach using tabulation.

#### Why is the Fibonacci sequence a classic example of a problem that can be solved with dynamic programming?

* It has an optimal structure and overlapping subproblems.

Wrong answers:

* It can be solved using iteration.
* It can be solved using recursion.
* It can be solved using a divide-and-conquer technique.

The Fibonacci sequence is a classic example of a problem that can be solved with dynamic programming because it has optimal substructure, meaning it can be broken down into smaller parts. It also has overlapping subproblems. Although dynamic programming can be solved using iteration or recursion, these characteristics are not unique to dynamic programming.

### Dynamic Programming Overview

Dynamic programming is a powerful problem-solving technique used for solving complex problems by breaking them into subproblems. After a bigger problem is broken into smaller subproblems and solved individually, the solutions are stored in a data structure. This is to ensure that each subproblem does not need to be recalculated.

When a recursive function calls itself over and over to solve the same subproblem, not only does it take more time, it is also inefficient.

Dynamic programming is a method for solving complex problems by solving overlapping subproblems only once.

It works by storing the solutions to subproblems in a data structure, so it is not necessary to calculate a problem more than once. Dynamic programming is an optimization of recursion. Wherever there is a recursive solution that has repeated calls, the values of those calls can be stored in a data structure and accessed again later.

This avoids redundant function calls on the call stack. Dynamic programming can be solved **top-down**, using **memoization**, or from the **bottom-up**, using **tabulation**.

It is one of the most powerful techniques for solving optimization problems that can be broken down into smaller subproblems. It helps optimize solutions to problems by caching values for future use, and it helps improve the runtimes of recursive algorithms.

### Dynamic Programming and Recursion

Recursion is a concept in computer science where a function calls itself in its own definition. It's a problem-solving technique that works by breaking a problem into smaller and smaller subproblems. Many problems are recursive in nature, meaning that they can be solved by solving smaller versions of themselves. Some common examples of problems that are recursive in nature are factorials and Fibonacci numbers.

Although many problems lend themselves well to recursion, many recursive functions are not efficient. This is because each time a recursive function is called, another frame object is added to the call stack. For some problems, these recursive calls grow exponentially and include several repeated subproblems that slow down your algorithm.

Dynamic programming is a way to optimize a recursive algorithm by storing the values of repeated subproblems in memory. Recursion and dynamic programming are both techniques to solve subproblems, but dynamic programming is a broader approach to optimizing algorithms by eliminating duplicate work.

#### Recursion

* Recursion is a programming technique where a function calls itself to solve a smaller instance of the same problem.
* The main problem is broken into subproblems using a top-down approach.
* Recursion might be slower because of the overhead of function calls and repeated calculations.
* In terms of memory usage, recursion does not require extra memory beyond stack space.

#### Dynamic Programming

* Dynamic programming is a tool for solving complex problems by breaking them into overlapping subproblems and solving each subproblem only once.
* The solutions to the subproblems are stored in a data structure, like an array, which can be accessed later if the same subproblems come up again.
* Dynamic programming can be faster because of the optimized subproblem solving and memoization where it remembers previously computed results.
* Dynamic programming requires additional memory to record these intermediate results.

### Using dynamic programming

Dynamic programming is useful for problems that have two main characteristics.

#### Optimal substructure

*Optimal substructure* means a problem can be broken into smaller, more manageable subproblems. It also means that the optimal solution to the main problem can be constructed from the optimal solutions of its smaller subproblems. Optimal substructure is one of the main characteristics of problems that can be solved recursively.

#### Overlapping subproblems

*Overlapping subproblems* means the same subproblems are encountered and solved repeatedly during the process of solving the main problem. With dynamic programming, you can store the results of subproblems and reuse them, which can significantly reduce the amount of computations needed.

Although most recursive problems have an optimal substructure, not all recursive problems have overlapping subproblems. Dynamic programming should be used when a problem has both of these characteristics. When dynamic programming is used with problems that have optimal substructure and overlapping subproblems, it can improve efficiency.

### Time and Space Complexity Review

One advantage of dynamic programming is that it can significantly reduce the time and space complexity of recursive algorithms. Most problems can be solved in different ways with different types of algorithms. Time and space complexity are ways to evaluate and compare the efficiency of algorithms. This helps programmers identify the optimal solution for different use cases.

#### Time Complexity

Time complexity measures the running time of an algorithm. It estimates the amount of time an algorithm takes to complete as the input size grows bigger.

#### Space Complexity

Space complexity estimates the amount of space or memory required for an algorithm to complete as the input size grows bigger.

#### Big O Notation

Both the time complexity and space complexity of an algorithm are expressed by Big O notation. Big O notation expresses how an algorithm behaves in terms of runtime or memory usage as its input size grows arbitrarily large. Using algebraic terms with the variable n representing the size of the input, it gives us a way to evaluate and classify algorithms based on their time and space complexities.

The best complexity is (O(1) Constant) and the worst time complexity is (O(n!) Factorial).

### Comparing time complexities

O(n!), O(2^n), and O(n^2) are the worst complexities. O(n log n) is considered bad. O(n) is a fair time complexity. The best time complexities are O(log n), and O(1).

### Common time complexities for dynamic programming

The purpose of dynamic programming is to improve the efficiency of algorithms. For algorithms that have optimal substructure and overlapping subproblems, the runtime can improve exponentially with dynamic programming.

Although dynamic programming can improve both the time and space complexity of a problem, let's focus on three main time complexities.

#### Exponential: O(2^n)

An algorithm is said to have an exponential time complexity, O(2^n), when the time required to complete the task grows exponentially with each addition to the input dataset.

When an algorithm has O(2^n) time complexity, it is one of the worst time complexities because it performs very slow or not at all in the worst-case scenarios.

An example of O(2^n) time complexity is randomly guessing the passcode on a phone. It gets exponentially harder as there are more digits to the passcode.

#### Linear: O(n)

In the linear time complexity, O(n), the algorithm's runtime grows linearly with the size of the input.

O(n) is much more efficient compared to exponential time complexity.

An example of O(n) time is opening each unread message on your phone and reading it. If you have three unread messages, you will have to tap open and read a message three times. If you have 20 unread messages, you will have to tap open and read a message 20 times.

#### Constant: O(1)

When the algorithm's runtime does not depend on the size of the input, the runtime is constant. This is represented in Big O notation as O(1) and is the most efficient runtime.

Dynamic programming can be used to retrieve the results of pre-calculated subproblems in constant time.

An example of O(1) time is opening your messages on your phone and reading the first message. Whether you have 1 unread message or 100 unread messages, reading the first message only requires you to open one message.

### Knowledge Check

#### Which statement describes the relationship between dynamic programming and recursion?

* Dynamic programming is a way to make recursion more efficient.

Wrong answers:

* Recursion is often more efficient than dynamic programming.
* Both dynamic programming and recursion store solutions for future use.
* Recursion consumes more heap memory compared to dynamic programming.

Dynamic programming is an optimization over recursion. It often makes the program run faster because it stores values for future use. Because dynamic programming stores solutions for future use, it typically consumes more heap memory compared to recursion alone.

#### What are some benefits of dynamic programming? (Select THREE.)

* It helps improve the runtimes of recursive algorithms.
* It can lead to an optimal solution to the larger problem through solving the smaller subproblems.
* It helps optimize solutions to problems by storing values for future use.

Wrong answers:

* It can help reduce the memory footprint of a solution.
* It simplifies the coding process by automating the work.
* It eliminates the need for recursion.

Because dynamic programming stores solutions for future use, it helps improve the runtimes of recursive algorithms, optimizes solutions to problems by storing values for future use, and often finds the optimal solution to a problem. However, because dynamic programming typically requires storing results of all solved subproblems, it **increases** the memory footprint of a solution.

#### When should dynamic programming be used by developers?

* Developers should use dynamic programming when a problem has optimal substructure and overlapping subproblems.

Wrong answers:

* Developers should use dynamic programming to optimize an algorithm whenever a recursive function is used.
* Developers should use dynamic programming for searching algorithms.
* Developers should use dynamic programming for problems with high space complexity requirements.

Dynamic programming should be used when a problem has optimal substructure and overlapping subproblems. Although it is used to optimize recursive functions, it is not used to optimize all recursive functions. Dynamic programming is not used for searching algorithms.

### Summary

Recursion is a valuable problem-solving technique where a function calls itself in its own definition. Recursion is beneficial because many problems are recursive in nature, meaning that they can be solved by breaking a problem into smaller subproblems. This tree-like structure is also referred to as **optimal substructure**.

Dynamic programming can be used when a problem has optimal substructure and repeated subproblems. It is an optimization of recursion because wherever there is a recursive solution that has repeated calls, the value of those calls can be stored in a data structure and accessed again later. This avoids redundant function calls on the call stack.

Understanding dynamic programming is important to programmers because it helps optimize solutions to problems by caching values for future use and it helps improve the runtimes of recursive algorithms.

## Memoization and Tabulation Overview

| Aspect | Memoization | Tabulation |
| ------ | ----------- | ---------- |
| Definition | Top-down approach to dynamic programming | Bottom-up approach to dynamic programming |
| Implementation| Uses recursion | Uses iteration |
| Approach | Caches the results of subproblems in memory as they are computed | Stores the results of subproblems in a table (often implemented as a list or array) before solving the main problem |
| Difficulty (or intuitiveness) | Generally more intuitive to implement because you store solutions to subproblems as they are computed | Generally less intuitive to implement because you must know which subproblems you will need to store before solving the main problem |
| Efficiency | Generally less efficient in terms of space | Generally more efficient in terms of space |
| Use case | Good for problems with a relatively small set of inputs | Good for problems with a large set of inputs |

### Memoization with Factorials

Memoization is a specific form of caching, or storing information to memory, that is used in dynamic programming.

#### What is memoization?

Memoization is the top-down approach to optimizing algorithms with dynamic programming. It involves caching the results of function calls in a memo, which can then be returned if the function is called again with the same inputs. It's typically implemented using recursion.

#### When do you use memoization?

You can use the memoization technique where the use of the previously calculated results is beneficial. This technique is particularly useful in the context of recursion, especially when problems have overlapping subproblems.

#### Why do you use memoization?

The main purpose of memoization is to improve the performance of algorithms, especially when the same subproblems are encountered and solved repeatedly. Memoization can be applied to store and reuse the results of these subproblems. This helps reduce repeated computations and improve the overall efficiency of the algorithm.

#### How do you use memoization?

If you notice a problem has optimal substructure and overlapping subproblems, solve the subproblem once. Use a dictionary object as your cache to store the results of function calls. Then, use recursion to compute the results. Finally, reuse this stored solution whenever the same subproblem reoccurs.  

### Factorials

Factorials are a common example of recursion because they can be broken up into smaller subproblems. A factorial is a mathematical operation that multiplies a given number by every whole number less than it down to 1. It's often shown by an exclamation point (!) after a number.

For example, the factorial of 5 (written as 5!) would be calculated as:

5! = 5 *4* 3 *2* 1 = 120

#### Factorial with a naive recursive approach

To write a recursive function in Python, first define the base case and the recursive case. The base case is when the recursion will stop, and the recursive case includes the arguments that are passed to the base case. Start by defining your factorial function. Set the base case first, in which 1 is returned if the variable n is less than 2. Else, we return the product of the variable n multiplied by the value of the recursive call to the factorial function, with an argument of n-1.

```
def factorial(n):
    if n < 2: 
        return 1 
    else: 
        return n * factorial(n - 1) 

num = 5
print("Number : " , num) 
print("Factorial : ", factorial(num))
```

When you run this code, it prints the number and the factorial.

```
Number:  5 
 
Factorial:  120 
```

Each time a recursive call is made, another frame object is added to the call stack. In this case, there are five recursive calls that are added to the call stack before the base case is met and the function unwinds.

### Memoization factorial example

If you are going to be using these numbers frequently, it is beneficial to optimize the algorithm using a dynamic programming technique like memoization. When you implement memoization, you will cache the results of each factorial calculation the first time it is performed. You can quickly retrieve the factorial of any number you need in constant time.

#### Calculating a factorial using memoization manually

Practice applying the top-down approach to dynamic programming by saving the results of a previously computed factorial as a memo. When you create a memo, you cache the information in memory so each subproblem is only calculated once.

```
factorial_memo = {}
def factorial(n): 
    if n < 2: return 1 
    if n not in factorial_memo: 
        factorial_memo[n] = n * factorial(n-1) 
    return factorial_memo[n] 

num = 5  
print("Number : " , num) 
print("Factorial : ", factorial (num)) 
```

1. **factorial_memo = {}** - This line creates an empty dictionary called factorial_memo. This dictionary will be used to store the results of factorial calculations.
2. **if n < 2: return 1** - This line is the base case of the recursion. If n is less than 2 (for example if n is 0 or 1), the function returns 1. The base case of the factorial of 0 or 1 is 1.
3. **if n not in factorial_memo:** - This line checks if the factorial of n has already been calculated and stored in **factorial_memo**. If it has not been calculated, the code proceeds to the next line to calculate it.
4. **factorial_memo [n] = n * factorial (n-1)** - This line calculates the factorial of n by multiplying n by the factorial (n-1), which is calculated by a recursive call to the factorial function. The result is then stored in **factorial_memo** with n as the key.
5. **return factorial_memo[n]** - This line returns the factorial of n from factorial_memo. If the factorial of n was just calculated in the previous line, this will be that value. If the factorial of n was already stored in factorial_memo, this will retrieve that stored value.

This example of memoization uses a top-down approach. It starts with the original problem of calculating the factorial of n and breaks it into smaller problems. In this case, the program stores the recursive calls made when it calculates each smaller factorial within the larger factorial.

#### Using the built-in cache decorator in Python

The built-in **@functools.cache** decorator in Python is another way to cache the results of function calls using memoization. When a function is computationally expensive and is called multiple times with the same arguments, caching can significantly improve performance by avoiding redundant computations.

The @cache decorator is easy to use and can be added to any function with a single line of code. Python takes care of the cache management automatically, so you do not have to worry about when to store results or when to retrieve them. Although this is convenient for simple use cases, one of the drawbacks is that you do not get to set fine-grained control over the cache, such as setting maximum cache size or custom eviction policies. If you need fine-grained control, a dictionary for memoization is preferred.

```
import functools
 
@functools.cache
def factorial(n):
    return n * factorial(n-1) if n else 1

print(factorial(10))
print(factorial(5))
print(factorial(12))
```

In this example, the factorial function is decorated with @functools.cache. This means that the results of the function calls are stored. 

* When you call **factorial(10)**, the function makes 11 recursive calls.
* When you call factorial(5), instead of recalculating the factorial, the function just looks up the result (120) in the cache and returns it. This is faster than recalculating the factorial.
* When you call factorial(12), the function only needs to make two new recursive calls for 12 and 11. This is because the other calls from 10 to 0 are already in the cache.  

#### Memoization benefits and limitations

##### Benefits of memoization

* Reduces the number of function calls
* Keeps data that can be used later accessible
* Offers an intuitive approach—easy to understand and implement
* Solves subproblems only when it's required
* Generally makes debugging easier
* Generally results in more straightforward and less complex code than tabulation

##### Limitations of memoization

* Uses more memory than tabulation (bottom-up dynamic programming) because it creates a dictionary to store the results of function calls
* Is not a one-size-fits-all solution to optimize all problems—works best for problems with optimal substructure and overlapping subproblems
* Is slower than tabulation if you need access to many different stored results
* Risks stack overflow conditions when when recursion is too deep

### Tabulation with Factorials

Tabulation works from the bottom up and finds all the solutions to subproblems, storing them in a table. This table is often implemented with a list or an array.

#### What is tabulation?

Tabulation is a bottom-up approach to dynamic programming. It starts with the smallest possible subproblem, called the base case, and then works step-by-step up to each subproblem. As each subproblem is solved, its solution is saved and used to solve the next lowest subproblem. In the end, these building solutions lead to the answer to the main problem. It is called tabulation because the information is often stored in a table. This table is often implemented with a list or an array.

#### When do you use tabulation?

Tabulation is beneficial when an algorithm has overlapping subproblems and optimal substructure. If all subproblems must be solved at least once, a bottom-up dynamic programming algorithm usually outperforms a top-down memoization algorithm. It also works well for problems that have a large set of inputs.

#### Why do you use tabulation?

The main purpose of tabulation is to improve the performance of an algorithm to make it run more efficiently. Tabulation is very fast because you directly access previous states from a table. Many algorithms make repeated calculations in a way that is expensive in terms of memory and time. With tabulation, the information is calculated all at once and stored in a table or array where it can be easily accessed when needed.

#### How do you use tabulation?

In tabulation, you use an array-like structure as a table to store the results of subproblems that are calculated from the bottom up. Initialize the table with a starting value. Next, run a loop that iterates over each subsequent value until the required value is reached. At every iteration of the loop, update the current entry in the lookup table by combining the solutions to the previously solved subproblems. Store that intermediate solution in the table at each iteration. Finally, when the loop is complete, return the last value stored in the table. This solution to the subproblems is the solution to the overall problem.

### Understanding the iterative process in tabulation

To illustrate the iterative process of tabulation, imagine the natural process of creating a table on paper. To create a table on paper for the factorials of 1–15, imagine the following process.

1. Begin by constructing a table designed to hold the factorials of 1–15.
2. Starting at the base case, fill in the table by calculating and recording the factorial of each number 1–15.
3. After you finish writing all the factorials, the table serves as a reference for future problems. If you need to calculate any factorial of 1–15, you can use your table to look up the results.

### Example of tabulation in Python

```
def tabulation(n): 
    # Create a table to store results. 
    table = [0] * (n + 1) 
    # Base case: factorial of 0 is 1. 
    table[0] = 1 
    # Fill in the table iteratively. 
    for i in range(1, n+1): 
        table[i] = i * table[i - 1]
    # Return table with factorials from 0 to n
    return table

# Calculate the factorials from 0 to 15
factorials = tabulation(15)

# Print the factorials from 1-15
for i in range(1, 16):
    print(f"The factorial of {i} is {factorials[i]}")
```

### Tabulation benefits and limitations

#### Benefits of tabulation

* Increases efficiency and improves the performance of a program
* Avoids redundant computations by storing solutions to subproblems in a table
* Keeps data that can be used later accessible 
* Usually outperforms a top-down memoization algorithm if all subproblems must be solved at least once
* Does not rely on system stack and solves problems with larger input sizes
* Offers better cache performance and improved speed because it fills the table sequentially

#### Limitations of tabulation

* Is less intuitive than memoization
* Gets complicated when a lot of conditions are required
* Is not a one-size-fits-all for every type of problem—works best for problems with optimal substructure and overlapping subproblems

### Knowledge Check

#### Which approach to dynamic programming is generally more efficient in terms of space but less intuitive?

* Tabulation

Wrong answers:

* Iteration
* Recursion
* Memoization

Tabulation is the bottom-up approach. It is generally more efficient in terms of space but less intuitive.

#### Which approach to dynamic programming is generally more intuitive to implement but less efficient in terms of space?

* Memoization

Wrong answers:

* Iteration
* Recursion
* Tabulation

Memoization is the top-down approach. It is generally more intuitive but less efficient in terms of space.

#### Which benefit is an advantage of memoization?

* It improves the performance of a program by storing solutions in cache.

Wrong answers:

* It avoids redundant computations by storing the solutions to subproblems in a table.
* It usually outperforms tabulation.
* It can be used for every type of problem.

Memoization increases efficiency and improves the performance of a program. It works from the top down and stores the solutions to subproblems in cache. Memoization can be used for problems that have optimal substructure and repeated subproblems.

#### Which benefit is an advantage of tabulation?

* Tabulation avoids redundant computations by storing the solutions to subproblems in a table.

Wrong answers:

* Tabulation solves subproblems only when it is required.
* The code in tabulation is less complicated than memoization.
* Tabulation is easier to understand and implement compared to memoization.

Tabulation is often considered more complicated to implement compared to memoization but more efficient. Tabulation avoids redundant computations by storing the solutions to subproblems in a table.

### Summary

Dynamic programming is helpful for problems that have optimal substructure and overlapping subproblems. It is inefficient and unnecessary to solve the same subproblems repeatedly. Dynamic programming is a technique to store these values. It can be done using a top-down approach, known as memoization, or a bottom-up approach, known as tabulation.  

| Memoization | Tabulation |
| ----------- | ---------- |
| Top-down approach to dynamic programming | Bottom-up approach to dynamic programming  |
| Uses recursion | Uses iteration |
| Caches the results of subproblems in memory| Stores the results of subproblems in a table |
| Generally more intuitive to implement but less efficient in terms of space | Generally more efficient in terms of space but less intuitive to implement |
| Good for problems with a relatively small set of inputs | Good for problems with a large set of inputs |
| Easier and less complicated code | More complicated code, as you need to know the order |
| Sometimes slower than tabulation because it creates memos as you go| Sometimes faster than memoization because you already know the order and dimensions of the table |
| Cache completes as you go | Fully completed table |

### Use Cases Overview

In the real world, dynamic programming is often applied to find the maximum or minimum solution to a problem.

#### Programming tools

* Tree traversals
* Sorting techniques
* Divide-and-conquer techniques
* Dynamic programming

#### Clues for Dynamic programming

1. Optimal substructure (recursion)
2. Overlapping subproblems
3. Keywords:
 a. shortest
 b. longest
 c. minimized
 d. maximized

* Given two sequences, find the length of the longest subsequence present in both. 
* Given a list of cities and the distances between each pair, find the shortest route that visits each city once and returns to the origin city.
* Given an unlimited supply of coins of certain values, find the minimum number of coins needed to get a desired change.

If you can solve a problem by enumerating all possible solutions and finding the best one, it is likely a good candidate for dynamic programming.

### Memoization and tabulation review

The two approaches to dynamic programming are the top-down approach, memoization, and the bottom-up approach, tabulation. Each approach optimizes the algorithm in a different order, so how you solve the problem will depend on what makes more sense. 

#### When to use memoization

The top-down approach might be easier to understand because it follows the natural logic of the problem. It can involve a lot of recursion and might have a larger memory footprint because of the call stack.  

This dynamic programming technique is good for a relatively small set of inputs where you might not need to know all of the results of each subproblem. It is used "as you go" to store information because it is calculated and is generally considered intuitive to implement.

#### When to use tabulation

The bottom-up approach can be more efficient because it avoids recursion and uses a loop instead. Although the speed is usually faster than memoization, it also requires a better understanding of the problem to build the solution iteratively.

This dynamic programming technique is good for large amounts of inputs where you might need the results to many subproblems. It is generally considered less intuitive to implement. You start from the base case and work your way up.

#### When to use either approach

In many cases, either approach to dynamic programming can improve the efficiency of the algorithm. It might make more sense to solve the problem using one or the other based on your own understanding of the problem. Your choice will also depend on the problem at hand and the specific requirements of your program.

## Common use cases

Dynamic programming is common in the real-world for optimization problems. For example, when you use a GPS to find the fastest route to somewhere, or when you need to decide which stocks are best to invest in with the money you have. These are real world examples of dynamic programming. Remember to look for the clues of optimal substructure and overlapping subproblems. Also remember that dynamic programming is an optimization over recursion, so if a problem uses recursion and has overlapping subproblems, dynamic programming can be used.

Some common use cases that are used in programming interviews are as follows:

* Knapsack problem
* Coin-change problem
* Fibonacci sequence

## Knapsack Problem: Memoization

*You are given a set of items with a set cost and weight for each item. You are also given a knapsack that can carry a fixed value of weight. Find the combination of items that maximizes the cost of items to put in the knapsack so the total weight does not surpass the maximum capacity of the knapsack.*

Note: You can either put an item in the bag or keep it out.

This is a dynamic programming problem because it has both optimal substructure and overlapping subproblems. The problem is broken down into smaller subproblems of the same type. You must consider each item and determine if it should be put in the knapsack or not. In this problem, the maximum value you can get from packing the knapsack with a given weight limit can be determined by previously computed maximum values for smaller weight limits. There are many overlapping subproblems.

### Sample knapsack recursive code in Python

Imagine the weights of the objects are [2, 3, 4, 5] and the values of the objects are [3, 4, 5, 6]. The capacity of your knapsack is 5. The goal is to put the items into the bag so that the sum of values associated with them is the maximum possible.

```
def knapsack(weights, values, capacity, i):
    # Base case: if the capacity is 0 or no items are left
    if i == 0 or capacity == 0:
        return 0
        # If the weight of the nth item is more than the capacity, it can't be included
    if weights[i - 1] > capacity:
        return knapsack(weights, values, capacity, i - 1)
        # Return the maximum of two cases:
    # 1. nth item included
    # 2. nth item not included

    else:
        included = values[i - 1] + knapsack(weights, values, capacity - weights[i - 1], i - 1)
        excluded = knapsack(weights, values, capacity, i - 1)
        return max(included, excluded)
        # Example usage

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
items = len(weights)
max = knapsack(weights, values, capacity, items)
print("Maximum value:", max)
```

```
Maximum value: 7
```

#### Explanation

The program calculates all the possible solutions and chooses the optimal solution. There are no items that are greater than the capacity of the bag. If you put the item that has a weight of 5 in the bag, your maximum value will only be 6. If you put the item that has a weight of 4, your maximum value will only be 5. But if you put two items in your bag (one with a weight of 2 and another with a weight of 3), you will find the optimal solution. The maximum value is 7. 

### Memoization approach

In the top-down dynamic programming approach, you use the same recursive algorithm to solve the problem. But instead of simply returning the computed values from your function, you will store it in a two-dimensional array that can store a particular state. Now if you come across the same state again, you can directly return its result stored in the table in constant time instead of calculating it in exponential complexity.

```
def knapsack_memo(weights, values, capacity, i, memo):
    # Base case: if the capacity is 0 or no items are left

    if i == 0 or capacity == 0:
        return 0

    # Check if the result is already computed
    if memo[i][capacity] != -1:
        return memo[i][capacity]

    # If the weight of the nth item is more than the capacity, it can't be included
    if weights[i - 1] > capacity:
        result = knapsack_memo(weights, values, capacity, i - 1, memo)

    else:
        # Return the maximum of two cases:
        # 1. nth item included
        # 2. nth item not included
        included = values[i - 1] + knapsack_memo(weights, values, capacity - weights[i - 1], i - 1, memo)
        excluded = knapsack_memo(weights, values, capacity, i - 1, memo)
        result = max(included, excluded)

    # Memoize the result
    memo[i][capacity] = result
    return result

# Example usage
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
items = len(weights)
# Initialize memoization table with -1
memo_table = [[-1 for _ in range(capacity + 1)] for _ in range(items + 1)]
max = knapsack_memo(weights, values, capacity, items, memo_table)
print("Maximum value:", max)
```

### Time and space complexities

#### Before Memoization

* Time complexity: O(2^n)
* Space complexity: O(n)

If you solve the knapsack problem using only recursion, you end up with a solution that has exponential time complexity. This is because for each item, you make a decision whether to include it in the knapsack or not. This leads to two recursive calls per item and results in a binary tree of decisions. If there are n items, the height of this tree is n, leading to a time complexity of O(2^n).

The space complexity for a recursive solution is O(n), which is the maximum depth of the recursion tree.

#### After Memoization

* Time complexity: O(n*W)
* Space complexity: O(n*W)

To improve the time complexity, it is better to store all of your previously calculated values so you do not have to recompute them later. This drastically reduces the number of computations.

The time complexity of the knapsack problem with memoization is O(n*W), where n is the number of items and W is the capacity of the knapsack. This is because we only need to solve the (n*W) unique subproblems.

The space complexity is also O(n*W), as you need to store the result of each unique subproblem in a two-dimensional array or table. If a result has already been calculated, you can access it in constant time.

### Real-world examples of the knapsack problem

Some common examples include finding the least wasteful way to cut raw materials, selecting stock investments and portfolios, and mapping workflows.

* You have a limited amount of time per day. The way you optimize how you use your time and workflow is a real-world example of the knapsack problem.
* You have a limited amount of money to invest in stocks. Selecting the optimal stock investments is a real-world example of the knapsack problem.

## Coin Change Problem: Tabulation

*Given a set of coins, find the total number of ways you can make change for a given amount of money.*

The coin change problem can be solved using dynamic programming because it has both optimal substructure and overlapping subproblems. In the context of the coin change problem, a subproblem might be how you can make change for a smaller amount. By solving the subproblems for all the smaller amounts, you can use the solutions of these subproblems to build up to the solution for the original amount. Storing the results of repeated subproblems helps solve the coin change problem more efficiently.

### Sample coin change recursive code in Python

Before looking at a dynamic programming approach, first examine a recursive code for the coin change problem. The coin values and sum will remain the same, as follows: 

* Coins = [1, 2, 3]
* Number of coins = 3
* Sum value = 4

```
coins = [1, 2, 3]
number_of_coins = 3
sum_value = 4

def solution(sol, i):
    if number_of_coins == 0 or sol > sum_value or i >= number_of_coins:
        return 0
    elif sol == sum_value:
        return 1
    else:
        return solution(sol + coins[i], i) + solution(sol, i + 1)

print("Total solutions: ", solution(0, 0))
```

```
Total solutions:  4
```

#### Explanation

The program uses recursion to test all the options and then prints the total solutions. The function solution takes two arguments—the current sum and the current index in the coins list (i). It checks if the current sum is greater than the target. If there are no coins, or if the index is out of range, it returns 0, because the target sum cannot be achieved. If the current sum equals the target, it returns 1, indicating a valid combination. Otherwise, it recursively calls itself twice. Once adding the current coin to the sum, and once moving to the next coin, effectively exploring all possible combinations. The function is initially called with arguments 0 (current sum) and 0 (current index). The result, which is the total number of ways to make up the target sum, is printed.

The following are four combinations that can be used to make the sum of 4.

* 1 + 1 + 1 + 1
* 1 + 3
* 1 + 1 + 2
* 2 +2

### Tabulation approach

To illustrate the tabulation process, make a table with the number of coins in rows 1–3 and the total ways you can make a sum from 0–4 in each of the columns.

| Number of Coins | How Many Ways Can You Make 0? | How Many Ways Can You Make 1? | How Many Ways Can You Make 2? | How Many Ways Can You Make 3? | How Many Ways Can You Make 4? |
| ------------------- | - | - | - | - | - |
| 1 coin (1, 2, or 3) | 1 | 1 | 1 | 1 | 1 |
| 2 coins (1, 2, or 3) | 1 | 1 | 2 | 2 | 3 |
| 3 coins (1, 2, or 3) | 1 | 1 | 2 | 3 | 4 |

This table shows the tabulation approach to the coin change problem. If you wanted to continue this problem for more coins or for a higher integer, you could easily add to this table. For each row and column, ask yourself each question as it relates to the number of coins.

### Showing this in Python

1. Create a list or table of size total + 1 and initialize all elements to 0, except the first one, which should be 1. This is because there is exactly one way to make a sum of 0, which is by not picking any coins.
2. Iterate over each coin in your list of coins. For each coin, iterate through the table starting from the value of the coin up to total. In each iteration, add the value at the index of the current total minus the coin value to the value at the current index. This is done because every time you consider a coin, you reduce the remaining total by the value of the coin. The number of ways to make this remaining total is already stored in the table from previous computations.
3. The result, which is the total number of ways to make change for the given total using the provided coins, is stored in the last entry of the table. This is then returned by the function.

```
def cointable(coins, total):
 
    # Initialize table to store number of ways to make change for each amount
    table = [0] * (total + 1)
    # There is one way to make change for amount = 0 (no coins)
    table[0] = 1
 
    # Iterate over each coin and update the table
    for coin in coins:
        for i in range(coin, total + 1):
            table[i] += table[i - coin]
 
    # The result is stored in the last entry of the table
    return table[total]
 
# Example usage
coins = [1, 2, 3]
total = 4
 
ways = cointable(coins, total)
print("Number of ways to make change:", ways)
```

### Time and space complexities

#### Before Tabulation

* Time complexity: O(2^n)
* Space complexity: O(n)

The time complexity of the recursive approach is O(2^n), where n is the target sum. This is because in the worst-case scenario, the function might end up exploring all possible combinations of coins, which can be represented as a binary tree with a depth of n.

The space complexity is O(n), which is the maximum depth of the recursion tree. This is because each recursive call is added to the call stack and takes up space.

#### After Tabulation

* Time complexity: O(m*n)
* Space complexity: O(n)

The time complexity of the dynamic programming approach is O(m*n), where m is the number of coin denominations and n is the target sum. This is because you are filling a table with m rows, one for each coin denomination, and n columns, one for each value from 0 to the target sum.

The space complexity is O(n), where n is the target sum. This is because we are creating a table with n+1 elements to store the number of ways to make each value from 0 to the target sum.

### Real-world examples of the coin change problem

Some examples include currency exchange, project scheduling, and investing.

* A vending machine must make the optimal decision based on the coins that have been dispensed and the coins that are still in the machine.
* A cashier might use a variation of the coin change problem to determine the fewest number of coins or bills to give to a customer as change.

## Fibonacci Overview

### Fibonacci sequence

The Fibonacci sequence is often used by programmers to practice optimizing code from a recursive approach to a dynamic programming approach. Like factorial numbers, the Fibonacci sequence is a useful way of illustrating dynamic programming because it has optimal substructure and overlapping subproblems.

The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding numbers. It starts with 0 and 1, and so the sequence is: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and so on.

* The Fibonacci spiral can be found in art, architecture, and nature. The proportion, size, and placement of one element compared to another creates a sense of harmony.
* Pascal’s triangle is an array of numbers where each number is the sum of the two directly above it. The diagonal rows of this triangle represent the Fibonacci sequence.
* The Fibonacci sequence can be found in nature with the arrangement of seeds in a sunflower or in the spiral of a shell.

### Calculating a Fibonacci number

A Fibonacci number is the sum of the two previous Fibonacci numbers.

A Fibonacci tree grows exponentially. To illustrate the number of calculations that happen for each Fibonacci number, look closely at the trees for the Fibonacci numbers 0–5.

The Fibonacci sequence is a classic example of a recursive problem. To find the fifth number in the Fibonacci sequence, it's necessary to first determine the fourth and third Fibonacci numbers. To calculate the fourth Fibonacci number, you need to calculate the third and second Fibonacci numbers. This pattern continues until you reach the base case. Not only does the size of the tree grow exponentially, but there are many repeated subproblems.

### Approaches to solving algorithms with the Fibonacci sequence

You can solve the Fibonacci sequence using several approaches. Three main approaches include the naive recursive approach, the top-down approach using memoization, and the bottom-up approach using tabulation.

* **Naive recursive approach**. The basic way to find the nth Fibonacci number is to use recursion. This is not a dynamic programming method and is very inefficient.
* **Top-down approach**. The top-down approach uses memoization. Memoization is a dynamic programming approach. It also uses recursion, but it doesn't recalculate each subproblem. Instead, it stores the calculations that have already been made as a memo in cache. When a recursive function calls a problem that has already been solved, it retrieves the repeated calculations from memory. This makes the algorithm run much faster.
* **Bottom-up approach**. The bottom-up approach uses tabulation. Tabulation is also a dynamic programming approach. It starts with the base cases and uses iteration to calculate each value. It stores the results of each calculation in a table. With this approach, each calculation is also only made once.

### Naive Recursive Approach

#### Calculating fib(5)

* Each problem is split into subproblems. The same subproblems are calculated over and over again. As the Fibonacci numbers grow, the numbers of nodes and calculations also grow.
* There are many repeated calculations. Fib(1) is calculated five times, Fib(2) three times, and Fib(3) twice. These repeated calculations show that the naive recursive approach is inefficient.

```
def fibonacci(n):
	if n <2:
		return n
	return fibonacci(n-1) + fibonacci(n-2)

for n in range(1,11):
	print(n, ":", fibonacci(n)) 
```

#### Explanation

The naive recursive approach is inefficient because each time the recursive function calls to itself, it is taking time to recompute each subproblem even if it has already been solved before. The higher the number, the more calculations must be performed to arrive at an answer. The time increases exponentially based on the value of n. Exponential time complexity is one of the worst time complexities. By using dynamic programming, you can make your algorithm more efficient.

### Top-Down Approach: Memoization

Recursion generally involves repeated recursive calls, which increases the program’s time complexity. In Python, you can use memoization to store the output of previously calculated values. If you save the results of subproblems, the next time you make a recursive call with these values, it will use the previously stored outputs instead of calculating them again. In this way, you can improve the performance of your code and make your program run more efficiently.

### Practice

```
def fibonacci(n, mem={}):
    # Check if the result for the current value of n is already memoized
    if n in mem:
        return mem[n]
    if n < 2: 
        return n
    # Compute the result and store it in mem before returning it
    mem[n] = fibonacci(n-1, mem) + fibonacci(n-2, mem)
    return mem[n]

# Example usage
n = 10
result = fibonacci(n)
print(f"The {n}-th Fibonacci number is: {result}")
```

The function first checks if the result for the current n is already in the memo. If it is, it returns that result immediately. If it is not, and n is less than 2, it returns n because the first two numbers in the Fibonacci sequence are 0 and 1. Otherwise, it calculates the Fibonacci number by recursively calling itself, stores the result in the memo, and then returns the result. This way, if the function is called again with the same n, it can return the stored result instead of recalculating it.

### Printing the first 10 numbers in the Fibonacci sequence using memoization.

```
def fibonacci(n, mem={}):
    # Check if the result for the current value of n is already memoized
    if n in mem:
        return mem[n]
    if n < 2: 
        return n
    # Compute the result and store it in mem before returning it
    mem[n] = fibonacci(n-1, mem) + fibonacci(n-2, mem)
    return mem[n]

# Example usage to print Fibonacci numbers from 1-10
n = 10
result = fibonacci(n)
for n in range(1, 11):
    print(n, ":", fibonacci(n))
```

```
1 : 1
2 : 1
3 : 2
4 : 3
5 : 5
6 : 8
7 : 13
8 : 21
9 : 34
10 : 55
```

### Using the built-in Python attribute for memoization

It is possible to use a built-in Python attribute to memoize the naive implementation. This is a neater way to use the built-in features of Python. 

```
@cache
def fibonacci(n):
    if n < 2: 
        return n
    return fibonacci(n-1) + fibonacci(n-2)  

for n in range(1,11): 
    print(n, ":", fibonacci(n))
```

In this code, the cache decorator from the functools module is imported. The @cache line applies the cache decorator to the fib function. This means that whenever Fibonacci is called, Python will first check if the result is already in the cache for the given arguments. If it is, Python will return the cached result instead of recalculating it. If it's not, Python will calculate the result and add it to the cache.

### Exploring how time improves using a memoization approach

* **1-10**. Similar to the recursive approach, the program runs efficiently for the first 10 numbers.
* **1-50**. Unlike the recursive approach, the numbers are quick to compute for the first 50 numbers.
* **1-100**. The program does not slow down. It takes the same time to compute the larger numbers as the smaller numbers.

### Explanation

The memoization approach is more efficient. Although this approach still uses recursion, the results to the subproblems are stored in memory. There is no need to recalculate a problem that has already been calculated before. Regardless of how high the number gets, the time complexity will be linear.

#### Before Memoization

* Time complexity: O(2^n)
* Space complexity: O(n)

The time complexity of the recursive Fibonacci sequence without memoization is O(2^n), where n is the number of terms. This is because each function call branches into two new calls in the recursion tree, leading to an exponential number of function calls.

The space complexity is O(n), where n is the depth of the recursion tree. This is because at any given point, you have to keep track of the remaining function calls in the call stack, which goes as deep as n.

#### After Memoization

* Time complexity: O(n)
* Space complexity: O(n)

With memoization, the time complexity reduces to O(n). This is because each Fibonacci number is calculated only once and then stored for future reference. This removes the need for redundant calculations.

The space complexity remains O(n) with memoization because you need to store all previously calculated Fibonacci numbers up to n. However, the nature of this space usage is different from the recursive case without memoization. Here, the space is used to store computed values for reuse rather than to keep track of recursive calls.

### Bottom-Up Approach: Tabulation

Tabulation is a bottom-up approach to dynamic programming because it starts with the smallest possible subproblem, called the base case, and then works step-by-step up to each subproblem. As each subproblem is solved, its solution is saved and used to solve the next lowest subproblem. In the end, these building solutions will lead to the answer for the main problem. It is called tabulation because the information is often stored in a table. 

### Practice

```
def ftab(n):
    # Initialize a table to store Fibonacci numbers
    fib_table = [0] * (n + 1)
    # Base cases
    fib_table[0] = 0
    fib_table[1] = 1
    # Populate the table using bottom-up approach
    for i in range(2, n + 1):
        fib_table[i] = fib_table[i - 1] + fib_table[i - 2]
        # The result is the Fibonacci number at index n
    return fib_table[n]

# Example usage
n = 10
result = ftab(n)
print(f"The {n}-th Fibonacci number is: {result}")
```

### Exploring a bottom-up approach for storing results.

* **1-10**. Similar to the top-down approach and recursive approach, the program runs efficiently with a range of 1–10 using tabulation.
* **1-100**. Similar to the top-down approach, the numbers compute much faster than the naive recursive approach.
* **1-1000**. The program continues to run efficiently even at a large range.

### Explanation

Tabulation can be more counterintuitive than a recursive approach with memoization. This is because tabulation requires you to explicitly determine the order in which subproblems are solved. Each subproblem must be solved before it is used to solve larger problems. This often involves thinking about the problem in a different way than you would with a recursive approach that uses memoization to cache the results to subproblems as you go.

#### Before Tabulation

* Time complexity: O(2^n)
* Space complexity: O(n)

The time complexity of the recursive Fibonacci sequence without dynamic programming is O(2^n), where n is the number of terms. This is because each function call branches into two new calls in the recursion tree, which leads to an exponential number of function calls. 

The space complexity is O(n), where n is the depth of the recursion tree. This is because at any given point, you have to keep track of the remaining function calls in the call stack, which goes as deep as n.

#### After Tabulation

* Time complexity: O(n)
* Space complexity: O(n)

With tabulation, the time complexity reduces to O(n) if a pre-calculated table is used with each call. This is because each Fibonacci number is calculated only once in a sequential manner. This removes the need for redundant calculations.

The space complexity with tabulation is O(n) because you need to store all previously calculated Fibonacci numbers up to n in a table.

## Use Cases Summary

### Comparing dynamic programming to recursion

Although both recursion and dynamic programming approaches such as memoization and tabulation can handle the task of solving problems, they have significant differences in terms of processing intermediate results and time complexities.  

For the examples such as the knapsack problem, coin change problem, and Fibonacci numbers, where the problem has optimal substructure and overlapping subproblems, dynamic programming works to make the algorithm run more efficiently.

| Feature or Algorithm | Naive Recursive Approach | Dynamic Programming |
| -------------------- | ------------------------ | ------------------- |
| Coding Logic | Base case + pattern | Base case + pattern |
| Store Intermediate Result | No | Yes |
| Procedure Plot | Tree like | Linear |
| O (Time Complexity) | O(2^n) | O(n) |
| O (Space Complexity) | O(n) | O(n) |

### Knowledge Check

#### Which options indicate a developer might be able to use dynamic programming? (Choose THREE.)

* The problem uses recursion.
* There are overlapping subproblems.
* There is optimal substructure.

Wrong answers:

* The problem uses iteration.
* The problem has a O(n) time complexity.
* The memory available to solve the problem is limited.

Three clues that it might be a dynamic programming problem are that the problem uses recursion, it has optimal substructure, and it has overlapping subproblems. Remember that not all recursive problems have overlapping subproblems.

#### What is the benefit of using a dynamic programming approach over a naive recursive approach when calculating the Fibonacci sequence?

* It improves the time complexity by avoiding redundant calculations.

Wrong answers:

* It increases the accuracy of the results.
* It simplifies the code and makes it easier to understand.
* You make your code object-oriented with dynamic programming.  

Dynamic programming does not improve the accuracy of the results or simplify the code, but it does improve the time complexity by avoiding redundant calculations.

#### What is the time complexity of a naive recursive implementation of the Fibonacci sequence? 

* O(2^n)

Wrong answers:

* O(n)
* O(n log n)
* O(n!)

The runtime of a basic recursive Fibonacci sequence program increases exponentially with the size of the input; therefore, the time complexity is O(2^n).

#### What is the time complexity of the Fibonacci sequence using memoization or tabulation? 

* O(n)

Wrong answers:

* O(n log n)
* O(2^n)
* O(n^2)

The time complexity of the Fibonacci sequence for both memoization and tabulation is O(n). This is because each Fibonacci number is only calculated once and then stored. The time it takes to run the program depends on the size of the input.

### Summary

* Describe dynamic programming and how it can be used to optimize recursion.
* Define memoization and tabulation.
* Discuss the benefits, types, and usage of memoization and tabulation.
* Review the differences between memoization and tabulation and review use cases.
* Review various Fibonacci examples.

#### Basics of dynamic programming

The basics of dynamic programming include breaking a problem into smaller subproblems, solving each subproblem independently, storing the solutions to subproblems to avoid redundant computation, using the solutions to the subproblems to construct the overall solution, and using the principle of optimality to ensure that the most appropriate solution is used. 

The key characteristics of a dynamic programming algorithm include overlapping subproblems, optimal substructure, memoization or tabulation, and the use of either iterative or recursive methods.

#### Memoization and tabulation

The two main approaches for optimizing algorithms in dynamic programming are the top-down approach and the bottom-up approach. The top-down approach is often referred to as memoization, and it uses recursion. The bottom-up approach is known as tabulation, and it uses iteration. Both of these approaches help improve the efficiency of an algorithm.

#### Use cases

It makes sense to use dynamic programming if a problem has optimal substructure and overlapping subproblems. There are several common examples that use dynamic programming. These use cases include factorials, knapsack problem, coin change problem, and Fibonacci numbers.

#### Fibonacci examples

One of the classic examples to illustrate dynamic programming is the Fibonacci sequence. This sequence begins with two ones, and each subsequent number is the sum of the two preceding numbers. In this sequence, it is easy to see how much dynamic programming improves the efficiency of a program compared to how the algorithm runs with a naive recursive approach.

## [Lab: Writing Code to Solve Subset Sum Problems](./W07Lab1SubsetSumProblems.md)

