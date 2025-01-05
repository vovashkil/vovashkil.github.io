#!/usr/bin/env python
# coding: utf-8

# # <span style="color:blue">Arrays
# AWS CLOUD INSTITUTE: PROVIDED FOR EDUCATIONAL INSTRUCTIONAL PURPOSES ONLY.

# # Arrays in Python

# There are **multiple ways** that you can **implement arrays in Python**. Some of them were already covered in the eLearning. We'll give some examples here (some are in the eLearning, and some are not).

# ## Implementation #1: Using the built-in Python List as is
# The **standard Python List** class already **supports all** the basic **requirememts for** an **array** implementation.
# - Supports **efficient index based access**
# - Supports **arrays of multiple dimensions**

# ### Creating arrays
# Creating an array will look no different than creating a standard list.

# #### Create a one dimensional array

# In[ ]:


# create a one dimensional array to store the books of a popular series in order
wot_books = ["The Eye of the World", 
             "The Great Hunt", 
             "The Dragon Reborn", 
             "The Shadow Rising", 
             "The Fires of Heaven", 
             "Lord of Chaos",
             "A Crown of Swords",
             "The Path of Daggers",
             "Winter's Heart",
             "Crossroads of Twilight",
             "Knife of Dreams",
             "The Gathering Storm",
             "Towers of Midnight",
             "A Memory of Light"]

print(wot_books)


# In[ ]:


# create a an array to store prices of 10 products
product_prices = [9.99, 14.99, 19.99, 24.99, 29.99, 34.99, 39.99, 44.99, 49.99, 54.99]
print(product_prices)


# #### Create a two dimensional array
# A **two dimensional array** will essentially be created as a **list of lists**.

# In[ ]:


# create a two dimensional array to store a crossword puzzle
crossword = [[" ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", "S", " ", " ", " ", " ", " "],
             [" ", " ", "T", " ", "T", " ", "P", " "],
             [" ", " ", "A", "R", "R", "A", "Y", " "],
             [" ", " ", "C", " ", "E", " ", "T", " "],
             [" ", " ", "K", " ", "E", " ", "H", " "],
             [" ", " ", " ", " ", " ", " ", "O", " "],
             [" ", " ", " ", " ", " ", " ", "N", " "],
             [" ", " ", " ", " ", " ", " ", " ", " "]]

print(crossword)


# Ugh! We can print a little nice iterating

# In[ ]:


for line in crossword:
    print(line)


# **What about more dimensions?** Yes, we **can do 3 and more**. **We'll see that later**, because they are harder to create with intialized values like we see above.

# ### Index based access
# A **fast index based access** is one of the most **defining characteristics** of an **array**. We know that Pyhton lists can support that. Just **remember** that **indexes start at 0**.

# #### Access in one dimension

# We can **use the indexes to retrieve values**.

# In[ ]:


# get the first book in the book series
print(wot_books[0])

# get the fifth book in the book series
print(wot_books[4])


# Also **use the indexes to update values**.

# In[ ]:


# print the current product prices
print(f"Current prices: {product_prices}")

# update the 3rd item price
product_prices[2] = 24.99

# print the updated prices
print(f"Updated prices: {product_prices}")


# #### Access in two dimensions

# We can **use the indexes to retrieve values**.

# In[ ]:


# print the cross array again to visualize the puzzle
for line in crossword:
    print(line)

# print the word "ARRAY" character by character
print(f"\nWord: {crossword[3][2]}{crossword[3][3]}{crossword[3][4]}{crossword[3][5]}{crossword[3][6]}")


# Also **use the indexes to update values**. Let's **add the word "SET"** to the puzzle.

# In[ ]:


# Add the word "SET" to the puzzle (the "T" is already there)
crossword[2][0] = "S"
crossword[2][1] = "E"

# print the cross array again to visualize the puzzle
for line in crossword:
    print(line)


# ### Iterating
# We know there are various ways to iterate with a Python list. But since we're discussing arrays here, the **"classic" way** to **iterate in an array** is using for **loops with indexes**.

# #### Loop in one dimension

# In[ ]:


# print all the books in the series
for i in range(len(wot_books)):
    print(wot_books[i])


# #### Loop in two dimensions

# In[ ]:


# print all the non-empty characters in the crossword
for i in range(len(crossword)):
    for j in range(len(crossword[i])):
        if crossword[i][j] != " ":
            print(crossword[i][j], end=" ")


# #### Loop in three dimensions
# We'll finally **show a three dimensional array**, **using** a **loop to create** it.
# 
# For an example of a **3 dimensional array**, imagine we were trying to track the **hourly temperature each day for a year**. So we would have:
# - Month of the year (0-11)
# - Day ot the month (0-30)
# - Hour of the day (0 - 23)
# 
# Remember, aside from the hour, which can start with 0 at midnight, the month and day will be offset by 1, since the **indexes always start at 0**.
# 
# **Note**: we **could add** some **if statements in** the **code below** to **account for** the **different number of days in each month**, **but we'll keep it simple**, and fill in **every month** to **31 days**. Feel free to play around with the code, and make it more accurate.

# In[ ]:


# use the Python random module to generate some random temperatures
import random


# In[ ]:


# create a three dimensional array to store hourly temperatures for a year
# initilize values to -1, using list comprehension
temperatures = [[[-1 for hour in range(24)] for day in range(31)] for month in range(12)]

# loop through the three dimensions, and set a random value
for month in range(12):
    for day in range(31):
        for hour in range(24):
            # use the 3 dimensions indexes to set the temparature
            temperatures[month][day][hour] = random.randint(60, 100)


# Now we can **use the indexes to get the temperature for any day**

# In[ ]:


# get the temperature for May 12th at 9am
print(f"Temperature on May 12th at 10pm: {temperatures[4][11][9]}°F")

# get the temperature for February 19th at 10pm
print(f"Temperature on February 19th at 10pm: {temperatures[1][18][22]}°F")


# ## Implementation #2: Using the Python array module
# Python also has a **built-in [array module](https://docs.python.org/3/library/array.html)**, which is **specifically created** to **efficiently manage numeric arrays**. It **supports all** the basic **requirememts for** an **array** implementation.
# - Supports **efficient index based access**
# - Supports **arrays of multiple dimensions**

# #### Why would we use the array module?
# 
# The array module is **more memory efficient than** the a **standard List**, and has broader support of various numeric types. It **requires homogenous data types**, meaning that all array elements are of the same type. It is a **good option if** we're **operating** on **large arrays of numbers**.

# ### Import the array module
# The array module is a **built-in module**, so it **does not have to be installed** separately from Python. But we do **need to import it**. It's a good convention to **import it as "arr"**, and then every **subsequent operation** will be **prefixed with "arr."**

# In[ ]:


import array as arr


# ### Create an array module array
# **Creating an array module array** is very similar, but it **takes** an **additional argument** to **specify the data type**. Having a well defined homogeneous data type allows the array module to be more memory efficient.

# In[ ]:


# create an integer array to story daily temperatures by the hour
daily_temps = arr.array('i', [55, 58, 59, 63, 65, 72, 75, 77, 78, 79, 80, 81, 82, 80, 78, 77, 75, 73, 70, 65, 64, 63, 62, 60])

print(daily_temps)


# In[ ]:


# create a floating point array to store prices of 10 products
product_prices = arr.array('f', [9.99, 14.99, 19.99, 24.99, 29.99, 34.99, 39.99, 44.99, 49.99, 54.99])
print(product_prices)


# You see the array having a lot of extra precision added.

# #### Two dimensional arrays?
# The **array module doesn't cleanly support multi-dimensional arrays**. **For a memory efficient array solution supporting multiple dimensions**, we will look at the **NumPy module** later in this course

# ### Index based access
# **Index based access** will be **nearly identical** to what we saw with lists.

# In[ ]:


# print the the temperature at 2am
print(daily_temps[2])


# Also **use the indexes to update values**.

# In[ ]:


# print the current product prices (rounded to 2 decimal places)
print(f"Current prices: {product_prices}")

# update the 5th item price
product_prices[4] = 24.99

# print the updated prices
print(f"Updated prices: {product_prices}")


# I'm **not crazy about all the extra decimals**, but when we **can round** it **when we use** it.

# In[ ]:


# print the first price rounded to 2 decimal places
print(f"First price: {product_prices[0]:.2f}")


# ### Iterating

# In[ ]:


# print all the temperatures in the array
for i in range(len(daily_temps)):
    print(f"Hour {i+1}: {daily_temps[i]}F")


# # <span style="color:blue">OPTIONAL</span> 

# # Initializing a list based array
# In this Notebook, **we saw** the **following statement** being **used to initialize an array**:
# - temperatures = [[[-1 for hour in range(24)] for day in range(31)] for month in range(12)]
# 
# How did that work?
# 
# The **statement is creating three nested lists using List comprehension**. List comprehension is not in the scope of our discussion, but you can view the documentation 
# **[here](https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions)**. I'll try to break it doen here.

# ## Basic list comprehension
# **List comprehension** allows you to **create a list from other lists and expressions in a single line**. This is a bigger topic, but I'll show some simple examples here. But there is a lot more to it.

# ### One dimension

# In[ ]:


# create a list of numbers 1 to 10 with list comprehension
nums = [i for i in range(1, 11)]
print(nums)


# In[ ]:


# create a with 10 numbers, all of them 7
# in this case, the for loop is used just to count how many "7"s I add
sevens = [7 for i in range(10)]
print(sevens)


# ### Two dimensions
# A **two dimensional array**, is simply **a list, where each element is another list**. So **to initialize** that to a value, I **need** to have **list comprehension inside another list comprehension**.

# In[ ]:


# Initialize an 4 x 3 array to with -1 values
rows = 4
cols = 3

# The i loop is going to generate the number of rows needed
# Then each row, will be one of the lists generated in the j loop
grid = [[-1 for j in range(cols)] for i in range(rows)]

print(grid)


# ### Three dimensions
# **Three dimensions** will be a **list of a list of a list**. Yes, that's getting **crazy!**
# 
# So **to initialize**, I **add one more list comprehension around**.

# In[ ]:


# Initialize a 2 x 4 x 3 array to with 0 values
x = 2
y = 4
z = 3

# Each loop in each list comprehension adds another dimension
cube = [[[0 for k in range(z)] for j in range(y)] for i in range(x)]

print(cube)

# it's hard to visually I have 3 dimensions printing the whole thing
# We can see we can check some values to confirm that we have 3 dimensions now
print()
print(f"The cube[1][3][1] value is {cube[1][3][1]}")
print(f"The cube[0][2][2] value is {cube[0][2][2]}")


# ### Create and initialize an array for 24 hours
# Based on the example above, it's easy to see how we can create just the hourly part of our target statement.

# In[ ]:


# create a with 24 numbers for each hour, initialized to -1
hour_temps = [-1 for hour in range(24)]
print(hour_temps)


# **If** we were just **creating temparartures in a month**, then it will be **just like the two dimensions example** above. Just so we can print it a little easier, lets **do it for only 10 days**, instead of 31

# In[ ]:


monthly_temps = [[-1 for hour in range(24)] for day in range(10)]
print(monthly_temps)


# Just like the earlier example, **to add the months in the year**, we need to **add** just **one more list comprehension in the end**, to account **for the 12 months**.

# In[ ]:


yearly_temps = [[[-1 for hour in range(24)] for day in range(10)] for month in range(12)]
print(yearly_temps)


# ### Which brings us back to ...
# Now we can see why the following works

# In[ ]:


# create a three dimensional array to store hourly temperatures for a year
# initilize values to -1, using list comprehension
temperatures = [[[-1 for hour in range(24)] for day in range(31)] for month in range(12)]

# loop through the three dimensions, and set a random value
for month in range(12):
    for day in range(31):
        for hour in range(24):
            # use the 3 dimensions indexes to set the temparature
            temperatures[month][day][hour] = random.randint(60, 100)

# print a few temparatures to test
print(f"Temperature on May 12th at 10pm: {temperatures[4][11][9]}°F")
print(f"Temperature on February 19th at 10pm: {temperatures[1][18][22]}°F")

