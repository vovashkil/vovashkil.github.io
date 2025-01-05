#!/usr/bin/env python
# coding: utf-8

# # <span style="color:blue">Dynamic Programming
# AWS CLOUD INSTITUTE: PROVIDED FOR EDUCATIONAL INSTRUCTIONAL PURPOSES ONLY.

# # Tabulation

# Tabulation is a **bottom-up approach to dynamic programming**. 
# - It **starts** with the **smallest possible subproblem**, called **the base case**, and then **works step-by-step up to each subproblem**. -
# - **As each subproblem** is **solved**, its **solution is saved** and **used to solve the next lowest subproblem**. -
# - In the end, these building solutions lead to the answer to the main problem.
# 
# It is **called tabulation** because the **information** is **often stored in** a **table.**

# ## Calculating Factorial
# Let's look at the implementation of factorials.

# ### Factorial - Recursive implementation
# We saw this implemention during our discussion of recursion.

# In[ ]:


def factorial_rec(n):
    '''
    Recursive implementation of factorials
    '''
    # Base case: factorial of 0 or 1 is 1
    if n < 2:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial_rec(n-1)


# #### Basic test

# In[ ]:


for n in range(10):
    print(f"Factorial of {n}: {factorial_rec(n)}")


# Ok, that works well enough for these small numbers.

# #### Testing with a big number

# We looked at this in our recursion discussion. Just **to refresh our memory**, let's **see what happens** if I try to calculate the **factorial of 10,000 using recursion**.

# In[ ]:


#n = 10000


# #### <span style="color:red">**WARNING: This next step will probably crash your Python kernel**</span>
# <span style="color:red"> Save your notebook if you made changes.</span>

# In[ ]:


# calculate the factorial using recursion
result = factorial_rec(n)

# print factorial, or a message if the number is bigger than 1 trillion
if (result > 1000000000000):
    print(f"Wow! Factorial of {n} is bigger than one trillion!")
else:
    print(f"Factorial of {n}: {result}")


# <span style="color:red">**Kaboom!!!**</span> (if you didn't crash your notebook, try 100000)
# 
# **As we've discussed** in the past, we get an **error because** we go over the **recursion limit**. **Recursion uses extra memory** to maintain the call stack, so **Python sets** a **maximum limit** to prevent an application from taking over too much memory. You can **view** that **limit using** the **[sys.getrecursionlimit() call](https://docs.python.org/3/library/sys.html#sys.getrecursionlimit)**.
# 
# **If** you **don't want to keep crashing**, **comment out** the ***n=10000*** line.

# #### Why did I crash?
# As we've discussed in the past, **recursion uses** extra **memory to maintain** the **call stack**. We don't want a misbehaving program to take over all of our memory, so **there is a system limit**. The **value can vary**, but you can **verify it using** the ***sys.getrecursionlimit()***

# ### Factorial - Tabulation implementation

# #### Is this a good fit for tabulation?
# First things first. Let's check if this solutions meets the key characteristics for dynamic programming:
# - **Optimal structure** - **Can** this **problem** be **broken down** in **smaller subproblems?**
#     - **Yes**. We can start with factorials of smaller numbers, and build our way up.
# - **Overlapping subproblems** - Are the **subproblems encountered repeatedly** during the process of solving the main problem?
#     - **Yes**. By it's very definition, every factorial includes factorials of all the numbers smaller than it.
#   
# If we're still not sure, let's check out the implementation using tabulation. Note that there is **no recursion involved**.

# #### Implementation

# In[ ]:


def factorial_tab(n):
    '''
    Tabulation implementation of factorials
    '''

    # Create a table to store results. 
    fact_results = [0] * (n + 1)
    
    # Base case: factorial of 0 is 1. 
    fact_results[0] = 1
    
    # calculate answer building on previous results
    for i in range(1, n+1): 
        fact_results[i] = i * fact_results[i - 1]
        
    # Return final result
    return fact_results[n]


# #### Basic tests

# In[ ]:


for n in range(10):
    print(f"Factorial of {n}: {factorial_tab(n)}")


# Ok ... that works too. But **why bother?** The recursive solution seemed smaller.

# #### Retesting with a big number
# Let's **repeat** the **same code block**, but **this time** we'll **use** our **tabulation** code. And such is my confidence, I'm **starting out with "n = 20000"**.
# 
# Yes, **you heard me!** I'm **seeing that 10,000** that broke the recursion, and **raising it to 20,000! Bold move!**

# In[ ]:


n = 20000


# In[ ]:


# calculate the factorial using tabulation
result = factorial_tab(n)

# print factorial, or a message if the number is bigger than 1 trillion
if (result > 1000000000000):
    print(f"Wow! Factorial of {n} is bigger than one trillion!")
else:
    print(f"Factorial of {n}: {result}")


# That **works**, because we **didn't have to recurse**.

# ### <span style="color:blue">OPTIONAL</span>: Better Implementation
# **This implementation** is seen in a few places, and it's **enough to explain the concept of tabulation**. **However**, it **doesn't** really **demonstrate** the **advantage**, because as it is, it's **no better than** a regular **iterative approach** to factorial. You still have to go through every number every time.
# 
# The **benefit of tabulation** comes from **reusing previous results**. So a **better implementation** would **move** the **table outside the function**, and **only re-calculate** values **if** they had **not been calculated before**. You can see that implementation here.

# #### Implementation
# I **added** a few **print statements** in the solution just so we can **see when tabulation saved time**. In a final implementation we wouldn't include them.

# In[ ]:


# Create a table to store results, initializing it with factorial of 0, which is 1
fact_results = [1]


# In[ ]:


def factorial_tab(n):
    '''
    Tabulation implementation of factorials
    '''

    # get the highest factorial currently available in the table
    max_fact = len(fact_results) - 1
    
    # if the factorial we need is smaller or equal to the max available, just return it
    if n <= max_fact:
        print(f"Factorial of {n} available. Returning imediatelly")
        return fact_results[n]

    # else, complement the factotrial table up to the one we need
    print(f"Complementing factorial table from {max_fact + 1} to {n} ...")
    for i in range(max_fact + 1, n + 1):
        fact_results.append(i * fact_results[i - 1])

    # Return final result
    return fact_results[n]


# #### Tests

# In[ ]:


# Start with 100. This will be our first complementation.
n = 100
result = factorial_tab(n)
print(f"Factorial of {n}: {result}\n")

# Try 50. This time we should have the result ready
n = 50
result = factorial_tab(n)
print(f"Factorial of {n}: {result}\n")

# Try 500. We'l have to extend from 101 to 500
n = 200
result = factorial_tab(n)
print(f"Factorial of {n}: {result}\n")

# Try 155. This time we should have the result ready
n = 155
result = factorial_tab(n)
print(f"Factorial of {n}: {result}\n")


# ## The Coin Change Problem
# The coin change problem is another classic example of dynamic programming. The problem is:
# - **Given** a **set of coins**, **find** the **total number of ways** you can make **change for** a **given amount of money**.
# - **Assume** you have an **unlimitted suply of coins**, so you **can repeat** a **coin as many times as you need**.
# 
# **Example**:
# In the US monetary system, our coins would have ammounts of 1 (penny), 5 (nickle), 10 (dime), and 25 (quarter). And yes, there are rarer 50 and $1 coins. However, the **problem** is **easier to visualize using fictitious coins of values 1, 2, and 3** cents.
# 
# So **for these coins**, **how many ways** could you **make change for 4 cents?** The **answer is 4**.
# - [1, 1, 1, 1]  adds up to 4
# - [1, 1, 2]  adds up to 4
# - [1, 3]  adds up to 4
# - [2, 2]  adds up to 4
# 
# **Bear in mind** that although I'm showing the different options here, the **real "classic" coin change problem** is to find **HOW MANY ways** there are. **NOT what** are the different **ways**.

# ### Define  our set of available coins
# We define those as a global outside the function, since our "monetary system" is not something that changes every time. You could also pass the list of available coins to the function everytime if you prefer.

# In[ ]:


# define our set of available coins
coins = [1, 3, 4]


# ### Coin Change - Recursive implementation
# This is similar to the solution provided on eLearning, but clearer variable names, and comments.

# In[ ]:


def coin_change_rec(target_value, curr_total = 0, curr_coin = 0):
    # if we went over the total, or we've reached the last coin, this is not a solution
    if curr_total > target_value or curr_coin >= len(coins):
        return 0
    # else if we the total matches the target, this is a solution, and will be added to count
    elif curr_total == target_value:
        return 1
    else:
        # calculate the total if we include current current coin
        total_with = coin_change_rec(target_value, curr_total + coins[curr_coin], curr_coin)
        total_without = coin_change_rec(target_value, curr_total, curr_coin + 1)

        # final answer is the summ of the options with and without
        return total_with + total_without


# #### Basic test

# In[ ]:


print("Total solutions: ", coin_change_rec(4))


# #### Implementation with list of possible solutions
# We are not going to spend too much time looking at the recursive algorithm, since this is not the topic at hand. 
# 
# But one thing I wanted to do, is **enhance** the **algorithm to** actually **list the solutions**. The implementation gets surprisingly longer for that. I also **used** the **approach** we've see before, of **having** an **outside function that initializes starting values** for the recursion, and then **calls** an **internal one** to start the **recursive part**.

# In[ ]:


def _coin_change_rec_ws(target_value, curr_total, coin_idx, curr_sol, all_solutions):
    # if we went over the total, or we've reached the last coin, this is not a solution
    if curr_total > target_value or coin_idx >= len(coins):
        return 0
    # else if we the total matches the target, this is a solution, and will be added to count
    elif curr_total == target_value:
        # append this solution to the list of all  solutions
        all_solutions.append(curr_sol.copy())
        return 1
    else:
        curr_sol.append(coins[coin_idx])
        # calculate the total if we include current current coin
        total_with = _coin_change_rec_ws(target_value, curr_total + coins[coin_idx], coin_idx, curr_sol, all_solutions)

        # calculate the total if we exclude the current coin (so pop it from solution first)
        curr_sol.pop()
        total_without = _coin_change_rec_ws(target_value, curr_total, coin_idx + 1, curr_sol, all_solutions)

        return total_with + total_without

def coin_change_rec_ws(target_value):
    # initialize variables
    curr_sol = []
    all_solutions = []

    # call recursive function with initial values
    total_solutions = _coin_change_rec_ws(target_value, 0, 0, curr_sol, all_solutions)

    # return count of solutions plus list of all solutions
    return total_solutions, all_solutions


# #### Basic test with solutions

# In[ ]:


# set the amount we're breaking change for
total_ammount = 4

# calculate change options
total_solutions, solutions_list = coin_change_rec_ws(total_ammount)
print(f"Total solutions: {total_solutions}")

print("\nSolutions:")
for sol in solutions_list:
    print(sol)


# #### Will this work for regular US coins?
# Sure, so let's change our coin set to the typical US denominations

# In[ ]:


coins = [1, 5, 10, 25]


# ##### Now rerun the function, and check for how many ways you can provide change for 30 cents. 
# You'll see the list can get pretty long, which is why we're not picking a big value

# In[ ]:


# set the amount we're breaking change for
total_ammount = 30

# calculate change options
total_solutions, solutions_list = coin_change_rec_ws(total_ammount)
print(f"Total solutions: {total_solutions}")

print("\nSolutions:")
for sol in solutions_list:
    print(sol)


# #### Reset available coins
# Let's reset our coins so we have an even comparison in the next section

# In[ ]:


coins = [1, 3, 4]


# ### Complexity analysis
# This recursion is very clever, but the time **complexity** can be very **high** in the worst case. Because at **each recursive step**, you are potentially **making two additional calls** (the "with" call, and the "without" call). So the final number of steps would be **2 x 2 x ... x 2**, however many time it takes to reach the total. So **that's 2<sup>n</sup>**, which we call exponential time complexity. The *n* in this case is the target value, since we're recursing until we reach it.
# - **Time complexity: <span style="color:blue">O(2<sup>n</sup>)**</span>

# ### Coin Change - Tabulation implementation

# #### Is this a good fit for tabulation?
# First things first. Let's check if this solutions meets the key characteristics for dynamic programming:
# - **Optimal structure** - **Can** this **problem** be **broken down** in **smaller subproblems?**
#     - **Yes**. We can start with solutions for a small total value, and build our way up.
# - **Overlapping subproblems** - Are the **subproblems encountered repeatedly** during the process of solving the main problem?
#     - **Yes**. We will see that the solution for a total value, will be a combination of smaller total values calculated before.
#   
# If we're still not sure, let's check out the implementation using tabulation. Note that there is **no recursion involved**.

# #### Implementation
# This is a **similar approach to** the **solution** provided seen **on eLearning**, **but** I use very **explicit variable names, and** a whole **lot of comments**.
# 
# I'm **also breaking down key intermediate steps**. In many cases they could be represented in less statements, but it becomes harder to understand.
# 
# Read the comments carefully, and they should explain the appraoch.

# In[ ]:


def coin_change_tab(target_value):
    # Initialize table to store the number of solutions for each target amount
    sols_table = [0] * (target_value + 1)
    
    # Base case: There is one way to make change for amount = 0 (no coins)
    sols_table[0] = 1    
    # Iterate over each available coin
    for coin in coins:
        # clearly I won't be able to use this coin for any value smaller than it
        # so I'll iterate starting at the value, up to the target
        for val in range(coin, target_value + 1):
            # get the current solutions we already have for that value before using this coin
            sols_without_coin = sols_table[val]
            
            # if we use this coin, how much left would we have
            total_minus_coin = val - coin

            # So if we use this coin, we would also have all the solutions for the remainder value
            sols_with_coin = sols_table[total_minus_coin]
            
            # Now we can update the solutions table value to be the ones with and without this coin
            sols_table[val] = sols_without_coin + sols_with_coin
 
    # The result is stored in the last entry of the table
    return sols_table[target_value]


# #### Basic test

# In[ ]:


print("Total solutions: ", coin_change_tab(4))


# #### Modified version with print statements
# Let's create a **modified version**, **with print statements** (hence the "_wp" in the name, as in "with print") to **visualize what happens** during the sorting processing. This includes adding a *print_table()* utility function that prints our solutions table.
# 
# This will print a lot of info, but it's a **good way to visualize** the **bottom up progress**.

# In[ ]:


def print_table(table, extra_indent = 0):
    '''
    Simple utility to print our solutions table
    '''
    print("".rjust(extra_indent) + "Target   value  : ", end="")
    for i in range(len(table)):
        print(str(i).rjust(3), end="")
    print()

    print("".rjust(extra_indent) + "Num of solutions: ", end="")
    for i in range(len(table)):
        print(str(table[i]).rjust(3), end="")
    print()
        
def coin_change_tab_wp(target_value):
 
    # Initialize table to store the number of solutions for each target amount
    sols_table = [0] * (target_value + 1)
    
    # Base case: There is one way to make change for amount = 0 (no coins)
    sols_table[0] = 1

    print("Initial table:")
    print_table(sols_table)
    
    # Iterate over each available coin
    for coin in coins:
        print(f"\nChecking coin: {coin}")
        
        # clearly I won't be able to use this coin for any value smaller than it
        # so I'll iterate starting at the value, up to the target
        for val in range(coin, target_value + 1):
            print()
            print(f"----- Checking Total = {val} and Coin = {coin} ------")
            # get the current solutions we already have for that value before using this coin
            sols_without_coin = sols_table[val]
            print(f"      Current solutions for total of {val} without coin = {sols_without_coin}")

            # if we use this coin, how much left would we have
            total_minus_coin = val - coin
            print(f"      Remaining total if coin is used = {val} - {coin} = {total_minus_coin}")
            
            # So if we use this coin, we would also have all the solutions for the remainder value
            sols_with_coin = sols_table[total_minus_coin]
            print(f"      Additional solutions for total of {total_minus_coin} with coin = {sols_with_coin}")

            # Now we can update the solutions table value to be the ones with and without this coin
            sols_table[val] = sols_without_coin + sols_with_coin
            print(f"      Updated solutions = {sols_without_coin} + {sols_with_coin} = {sols_table[val]}")

            print("\n      Updated table:")
            print_table(sols_table, 6)
            
        print(f"\nFull updated table after adding coin {coin}:")
        print_table(sols_table)
 
    # The result is stored in the last entry of the table
    return sols_table[target_value]


# #### Basic test

# In[ ]:


print("Total solutions: ", coin_change_tab_wp(4))


# #### Implementation with list of possible solutions?
# It's possible to do this for tabulation, but it becomes a whole separate issue, and a very long brute force algorithm. It's not in our scope here, so we'll skip it.

# ### Complexity analysis
# Our **recursive approach** was **smaller**, and probably easier to follow than this tabulation one. So **why bother?**
# 
# Recall that the **recursive algorithm** has a complexity of **O(2<sup>n</sup>)**, where *n* was the target value. 
# 
# In the **tabulation algorithm** we have a **nexted loop**. The **first loop** will **iterate through** the **coins available**, which is **relatively small**. Let's **call that *m***. The **second loop** **iterates up to the target value**, so we **call that *n***, as we did before. So the **final complexity is *n\*m***. Why not O(n<sup>2</sup>)? In this case the variables controller the outer and inner loop are very different, so *n\*m* is more accurate.
# - **Time complexity: <span style="color:blue">O(n\*m)**</span>

# # <span style="color:blue">OPTIONAL</span>: Fibonacci
# We've already seen the **Fibonacci series**, where **each number** is the **sum of** the **two previous** numbers: ***0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...***
# 
# The **Fibonnaci problem** is usually about **returning** the ***nth* Fibonnaci number**. So:
# - fibonnaci(4) = 3
# - fibonnaci(5) = 5
# - fibonacci(6) = 8
# - fibonacci(7) = 13

# ## Fibonacci

# ### Fibonacci - Recursive implementation
# We saw this implemention during our discussion of recursion.

# In[ ]:


def fibonacci_rec(n): 
	# Base case: First Fibonacci number is 0 
	if n == 0: 
		return 0 
	# Base case: Second Fibonacci number is 1 
	elif n == 1: 
		return 1 
	# Recursive case 
	else: 
		return fibonacci_rec(n - 1) + fibonacci_rec(n - 2) 


# #### Basic test

# In[ ]:


# Set  number to find fibonnaci for
fib_num = 10

print(f"Fibonnaci({fib_num}) = {fibonacci_rec(fib_num)}")


# #### Larger number test
# Let's try a **larger number**. Doesn't even need to be that big. **100** will be **enough to cause problems**.

# #### <span style="color:red">**WARNING: This next step will hang your Python kernel** </span>
# <span style="color:red">You can **stop the cell** to break.</span>

# In[ ]:


# Set  number to find fibonnaci for
fib_num = 100

print(f"Fibonnaci({fib_num}) = {fibonacci_rec(fib_num)}")


# ### Complexity analysis
# Once again, the recursion is clever, but the time **complexity** is **high**. Because at **each recursive step**, you are **making two additional calls** (the *"(n - 1)"* call, and the *"(n - 2)"* call). So the final number of steps would be **2 x 2 x ... x 2**, or **2<sup>n</sup>**.
# - **Time complexity: <span style="color:blue">O(2<sup>n</sup>)**</span>

# ### Fibonacci - Tabulation implementation

# #### Is this a good fit for tabulation?
# Let's check if this solutions meets the key characteristics for dynamic programming:
# - **Optimal structure** - **Can** this **problem** be **broken down** in **smaller subproblems?**
#     - **Yes**. We can start with solutions for a smaller Fibonacci problems, and build our way up.
# - **Overlapping subproblems** - Are the **subproblems encountered repeatedly** during the process of solving the main problem?
#     - **Yes**. By it's very definition, a Fibonacci problem depends on the values before.

# #### Implementation
# This is one of the more straightforward examples of tabulation. As usual, notice no recursion is used.

# In[ ]:


def fibonacci_tab(n):
    # Initialize a table to store Fibonacci numbers
    fib_table = [0] * (n + 1)
    
    # Base fibnacci cases
    fib_table[0] = 0
    fib_table[1] = 1
    
    # Populate the table using bottom-up approach
    for i in range(2, n + 1):
        fib_table[i] = fib_table[i - 1] + fib_table[i - 2]

    # The result is the Fibonacci number at index n
    return fib_table[n]


# #### Basic test

# In[ ]:


# Set  number to find fibonnaci for
fib_num = 10

print(f"Fibonnaci({fib_num}) = {fibonacci_tab(fib_num)}")


# #### Larger number test
# Let's **try again**. And once again, we'll **raise the stakes**. Let's do **1,000!**

# #### <span style="color:red">**WARNING ...** </span>
# <span style="color:blue">Just kidding. **No warning needed**. This will be a breeze!</span>

# In[ ]:


# Set  number to find fibonnaci for
fib_num = 1000

print(f"Fibonnaci({fib_num}) = {fibonacci_tab(fib_num)}")


# ### Complexity analysis
# If we look at the code, this is just a simple loop up to *n*. So the classic **O(n)**. 
# - **Time complexity: <span style="color:blue">O(n)**</span>
