#!/usr/bin/env python
# coding: utf-8

# # <span style="color:blue">Time Complexity Basics
# AWS CLOUD INSTITUTE: PROVIDED FOR EDUCATIONAL INSTRUCTIONAL PURPOSES ONLY.

# Time complexity measures the relative efficiency of an algorithm. 

# #### Measuring time with Python's Time Libray
# If we're going to compare time efficiency, let's use a Python module to measure it. There are a few available choices, and we'll use the **time** module (https://docs.python.org/3/library/time.html).

# In[ ]:


import time


# #### Example of time measure
# We will **use the *perf_counter* function** in the time module, which returns a simple time stamp in seconds

# In[ ]:


# take a timestamp before doing something
start_time = time.perf_counter()
print(f"Start timestamp: {start_time:.4f} seconds")

# do something
print("\nDoing something...")
for x in range(100):
    print(x, end="-")
print("\nDone\n")

# take a final timestamp and calculated ellapsed time
end_time = time.perf_counter()
print(f"End timestamp: {end_time:.4f} seconds\n")
print(f"Ellapsed time: {(end_time - start_time):.4f} seconds")


# ######
# We can see that **even looping 100 times**, took **fractions of seconds**. Which leads us to ...

# ### Computers are really fast ...

# Relative **small differences in the number of steps** performed **won't make** a really **big difference** in time. Let's try this out, using our timer.

# ## Constant Time Complexity: O(1)
# A few non-repetitive operations are practically instanteneous

# ##### Algorithm

# In[ ]:


def add_numbers(x , n):
    print(f"Adding {x} and {n}")
    sum = x + n
    return sum


# ##### Time measurement

# In[ ]:


start_time = time.perf_counter()

# do a couple operations
x = 10
n = 30
print(f"{x} + {n} = ", add_numbers(x, n))

end_time = time.perf_counter()

print(f"Ellapsed time: {(end_time - start_time):.4f} seconds")


# <br>We say these **few quick, non-repeatitice operations**, occur in **"Constant Time"**, and use the notation **O(1)**

# ## Linear Time Complexity: O(n)
# Repeatitive steps in a single loop are still pretty fast, as long as I'm not significantly changing the number of iterations.

# ##### Algorithm

# In[ ]:


def multiply_numbers(x , n):
    total = 0
    for i in range(n):
        total += x
    return total


# ##### Time measurement

# In[ ]:


start_time = time.perf_counter()

# do a couple operations
x = 10
n = 30
print(f"{x} * {n} = ", multiply_numbers(x, n))

end_time = time.perf_counter()

print(f"Ellapsed time: {(end_time - start_time):.4f} seconds")


# #### Changes in the same order of magnitude won't make a big difference
# Let's **try changing *n*** above to **make the loops longer**, and **see the impact** in the time.

# My results the were:
# - 30 loops: 0.0002 seconds
# - 300 loops: 0.0003 seconds
# - 3,000 loops: 0.0006 seconds
# - 30,000 loops: 0.0023 seconds
# 
# So it took a loop 1,000 times bigger to begin making a significant difference. Another fancy way of saying this, is that **only a change of a significant "order of magnitute", makes a significant difference**. That's what the **"O" in the Big O notation** stands for: *"Order of"*.
# 
# In this case, where we have a **single loop**, that will only **change the number of steps depending on one variable**, we say they occur in **"Linear Time"**, and use the notation **O(n)**

# ## Quadratic Time Complexity: O(n<sup>2</sup>)
# 

# What if we have a **loop, inside a loop**? Something like this:
# ```
# for x in range(100):
#     for y in range(200):
#         print(x + y)
# ```
# In this case, for **every iteration** of the **first loop**, we do a **full iteration of the second loop**. So that print statement would run **100 x 200 times**. That's the kind of thing that would **change** our **"order of magnitute"**. Let's test it out.

# ##### Algorithm

# In[ ]:


def square_number(n):
    total = 0
    for i in range(n):
        for j in range(n):
            total += 1
    return total


# ##### Time measurement

# In[ ]:


start_time = time.perf_counter()

# do a couple operations
n = 30
print(f"{n} square = ", square_number(n))

end_time = time.perf_counter()

print(f"Ellapsed time: {(end_time - start_time):.4f} seconds")


# #### Changes that are squared, will make an impact much quicker ...
# With a small number like "30", even this is pretty fast. It's good to remember that even a bad algorithm will probably run fast if you only have a few steps to run.
# 
# However ...
# 
# Let's **try changing *n*** above again to **make both loops longer**, and **see the impact** in the time.
# 
# My initial results the were:
# - 30 loops: 0.0004 seconds
# - 300 loops: 0.0053 seconds
# - 3,000 loops: 0.3708 seconds
# - 30,000 loops: 41.2883 seconds
# 
# **Wow!!** Now that got ugly fast :-)  

# So moral of the story is, when you have **loops insides loops**, you need to be **careful** with **how many iterations** you have, because they can **significantly change the order of magnitute**. We say they occur in **"Quadratic Time"**, and use the notation **O(n<sup>2</sup>)**

# ## Logarithmic Time Complexity: O(log(n))
# 

# Don't get scared with the Math. The simple question is, what if I have a **loop** that **keeps splitting something in half**, over and over. For instance
# ```
# while n > 1:
#     n = n // 2
#     print("New n is", n)
# ```
# Just printing the number may seem useless, but we'll see **many cases** in upcoming modules where **loops like this** will be **very useful**. Let's test how it performs.

# ##### Algorithm
# In this algorithm we'll count how many times we split the number before it's less than one (which is the number of times we go through the loop)

# In[ ]:


def count_splits(n):
    total = 0
    # while n greated than 1, keep diving it by 2
    while n > 1:
        n = n // 2
        total += 1
    
    return total


# ##### Time measurement

# In[ ]:


start_time = time.perf_counter()

# do a couple operations
n = 30
print(f"To fully split {n}, we looped {count_splits(n)} times")

end_time = time.perf_counter()

print(f"Ellapsed time: {(end_time - start_time):.4f} seconds")


# #### So how will the performance progress here ...
# With a small number like "30", as usual, this is pretty fast.
# 
# Let's **try changing *n*** above again and **see the impact** in the time.
# 
# My initial results the were:
# - 30 loops: 0.0003 seconds
# - 300 loops: 0.0007 seconds
# - 3,000 loops: 0.0003 seconds
# - 30,000 loops: 0.0004 seconds
# 
# What's hapenning here?! I can't seem to make this bad. So let's go crazy ...
# - 30,000,000  loops: 0.0004 seconds
# 
# What?! Is this an algorithm or a super-villan? I'm not giving up
# - 30,000,000,000 loops: 0.0004 seconds
# 
# Ok, now I give up :-) 

# So moral of the story is, when you have a **loop** like that, **where steps are based on something being split in half multiple times**, the **performance is great**. That's because as we can see in the output, the number of steps stay very small, even for large numbers.

# ##### So how many loop iterations I need to divide a number in half down to 1?
# You **don't need to memorize**, but that's a **Math thing**. The number of **steps will be** the **log base 2 of n**. Python has a function that calculates that, so let's run it with our numbers (and round it off)

# In[ ]:


import math
print(int(math.log2(300)))
print(int(math.log2(300000)))
print(int(math.log2(300000000)))


# You don't need to understand the Math to see the number of iterations will grow very slowly. We say that these **algorithms** that keep **splitting the loop in half** have occur in "**Logarithmic Time**", and use the notation **O(log(n))**

# ## And there is more ...

# These were simple examples to explain the basic concepts, but there is a lot more. We **also have time complexities** of **O(n log(n)), O(2n), O(n!)**, etc.  But that's a **topic for another time** ...
