#!/usr/bin/env python
# coding: utf-8

# # <span style="color:blue">Time Complexity
# AWS CLOUD INSTITUTE: PROVIDED FOR EDUCATIONAL INSTRUCTIONAL PURPOSES ONLY.

# Time complexity measures the relative efficiency of an algorithm. 

# #### Measuring time with Python's Time Libray
# If we're going to compare time efficiency, let's use a Python module to measure it. There are a few available choices, and we'll use the **time** module (https://docs.python.org/3/library/time.html). I'll also use the random module to generate random numbers for some examples.

# In[ ]:


import time
import random


# ## Constant Time Complexity: O(1)
# A few non-repetitive operations are practically instanteneous

# ### Algorithm example

# In[ ]:


def add_numbers(x , n):
    return x + n


# #### Time Complexity Test

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

# ### Algorithm example: Linear Search
# The linear search we looked at in an earlier session, is a classic example of a O(n) algorithm.

# In[ ]:


def linear_search(items, search_value):
    for i in range(len(items)):
        if items[i] == search_value:
            return i
    return -1


# #### Time Complexity Test

# ##### Define the list sizes I want to test

# In[ ]:


list_sizes = [100, 150, 200, 1000, 10000, 100000]


# ##### Iterate to create lists for each test size, and observe the average performance for them

# In[ ]:


# iterate through all requested list sizes
for list_size in list_sizes:
    
    # Creata a set of unique keys for the specified list_size
    str_set = set({})
    while len(str_set) < list_size:
        # generate a very large random integer, convert it to a string, and add to set
        str_set.add(str(random.randint(0, 1000000000)))
    
    # convert the set to a list
    str_list = list(str_set)

    # generate some random keys to searcho for
    random_keys = []
    for x in range(10):
        random_keys.append(str_list[random.randint(0, len(str_list) - 1)])

    print(f"\n------------------ Searching {len(str_list):,d} elements ------------------")
    
    # initialize total linear search time
    total_linear_search_time = 0
                         
    # iterate through search words
    for search_key in random_keys:  
        # start timer
        start_time = time.perf_counter()
    
        # perform linear search
        idx = linear_search(str_list, search_key)
    
        # stop timer
        end_time = time.perf_counter()
       
        # accumulate the search times so we can average in the end
        total_linear_search_time += (end_time - start_time)
        
    # calculate final average across all searches
    avg_linear_search_time = total_linear_search_time / len(random_keys)
    print(f"Average linear search time: {avg_linear_search_time:.6f} seconds")


# #### Changes in the same order of magnitude won't make a big difference

# It took a loop 1,000 times bigger to begin making a significant difference. Another fancy way of saying this, is that **only a change of a significant "order of magnitute", makes a significant difference**. That's what the **"O" in the Big O notation** stands for: *"Order of"*.
# 
# In this case, where we have a **single loop**, that will only change the number of steps depending on one variable, we say they occur in **"Linear Time"**, and use the notation **O(n)**

# ## Quadratic Time Complexity: O(n<sup>2</sup>)
# 

# What if we have a **loop, inside a loop**? That's what we saw in Bubble Sort

# ### Algorithm example: Bubble Sort

# In[ ]:


def bubble_sort(my_list):
    """
    Sorts the given list using the Bubble Sort algorithm.
    This algorithm modifies the list in place.
    """
    # Get the length of the list
    n = len(my_list)

    # Outer loop to traverse through the list
    for i in range(n):
        # Inner loop to compare adjacent elements
        for j in range(0, n-i-1):
            # Compare adjacent elements
            if my_list[j] > my_list[j+1]:
                # Swap elements if they are in the wrong order
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
                
    # Return the sorted list
    return my_list  


# #### Time Complexity Test

# ##### Define the list sizes I want to test

# In[ ]:


list_sizes = [100, 1000, 10000]


# ##### Iterate to create lists for each test size, and observe the average performance for them

# In[ ]:


# iterate through all requested list sizes
for list_size in list_sizes:
    
    # Creata a set of unique keys for the specified list_size
    str_set = set({})
    while len(str_set) < list_size:
        # generate a very large random integer, convert it to a string, and add to set
        str_set.add(str(random.randint(0, 1000000000)))
    
    # convert the set to a list
    str_list = list(str_set)

    # generate some random keys to searcho for
    random_keys = []
    for x in range(10):
        random_keys.append(str_list[random.randint(0, len(str_list) - 1)])

    print(f"\n------------------ Sorting {len(str_list):,d} elements ------------------")
    
    # start timer
    start_time = time.perf_counter()
    
    # sort using merge_sort
    sorted_list = bubble_sort(str_list)
    
    # stop timer and calculate elapsed time
    end_time = time.perf_counter()
    bubble_sort_time = end_time - start_time
    
    # print sorted function time
    print(f"Bubble sort time: {bubble_sort_time:.6f} seconds")


# #### Changes that are squared, will make an impact much quicker ...
# With a small number like "100", even this is pretty fast. It's good to remember that even a bad algorithm will probably run fast if you only have a few steps to run.
# 
# However, by the time we got to 10,000, the performance had deterioted **a lot**. If I went up to 100,000 , it would probably take minutes, or timed out.

# So moral of the story is, when you have **loops insides loops**, you need to be **careful** with **how many iterations** you have, because they can **significantly change the order of magnitute**. We say they occur in **"Quadratic Time"**, and use the notation **O(n<sup>2</sup>)**

# ## Logarithmic Time Complexity: O(log n)
# 

# Don't get scared with the Math. The simple question is, what if I have a **loop** that **keeps splitting something in half**, over and over. For instance
# ```
# while n > 1:
#     n = n // 2
#     print("New n is", n)
# ```
# We've **already seen multiple algorithms that will split the problem**, in the **"divide and conquer" approach**. In **some cases** it's **in** a **iteration** like above, but in **other cases** the **split happens via recursion**.

# ### Algortithm example: binary search

# In[ ]:


def binary_search_loop(items, search_value):
    '''
    This method will search for an item in a list of ascending order.
    It will retur the index of the item if found, or -1 if not found.
    '''

    # initialize the start and end of our loop, which will be updated as the search progresses
    start = 0
    end = len(items) - 1

    # continue the loop as long as start is <= to end. If we "cross over", and the end is smaller
    # it will mean that we never found the item
    while start <= end:
        # split the search space in half, by getting the middle value between the current start and end
        middle = (start + end) // 2

        # if the search value is equal to the middle value, then we found it, so return the index
        if items[middle] == search_value:
            return middle
        # else, if the search value is less than the middle value, update the end to look at the lower half
        elif search_value < items[middle]:
            end = middle - 1
        # else, the search value is greater than the middle value, so update the start to look at the upper half
        else:
            start = middle + 1

    # if we get here, we never found the item, so return -1
    return -1


# #### Time Complexity Test

# ##### Define the list sizes I want to test

# In[ ]:


list_sizes = [100, 1000, 10000, 100000, 1000000]


# ##### Iterate to create lists for each test size, and observe the average performance for them

# In[ ]:


# iterate through all requested list sizes
for list_size in list_sizes:
    
    # Creata a set of unique keys for the specified list_size
    str_set = set({})
    while len(str_set) < list_size:
        # generate a very large random integer, convert it to a string, and add to set
        str_set.add(str(random.randint(0, 1000000000)))
    
    # convert the set to a list
    str_list = list(str_set)

    # generate some random keys to searcho for
    random_keys = []
    for x in range(10):
        random_keys.append(str_list[random.randint(0, len(str_list) - 1)])

    print(f"\n------------------ Searching {len(str_list):,d} elements ------------------")
    
    # initialize total linear search time
    total_linear_search_time = 0
                         
    # iterate through search words
    for search_key in random_keys:  
        # start timer
        start_time = time.perf_counter()
    
        # perform linear search
        idx = binary_search_loop(str_list, search_key)
    
        # stop timer
        end_time = time.perf_counter()
       
        # accumulate the search times so we can average in the end
        total_linear_search_time += (end_time - start_time)
        
    # calculate final average across all searches
    avg_linear_search_time = total_linear_search_time / len(random_keys)
    print(f"Average linear search time: {avg_linear_search_time:.6f} seconds")


# #### How does the performance scale?
# As we can see, with the ninary search our performance barely changed even going up to 1,000,000 items.

# So moral of the story is, when you an **alorithm**, **where steps are based on something being split in half multiple times**, the **performance is great**. That's because as we can see in the output, the number of steps stay very small, even for large numbers.

# You don't need to understand the Math to see the number of iterations will grow very slowly. We say that these **algorithms** that keep **splitting the steps in half** have occur in "**Logarithmic Time**", and use the notation **O(log n)**

# ## Quasilinear time complexity: O(n log n) 
# 

# **What if** you have an **algorithm that performs in O(log n)**, which we know is very fast, **but you repeat that *n* times**. That combination of linear and logarithmic operations is what we call Quasilinear time complexity.

# ### Algorithm example: Quicksort

# In[ ]:


def quicksort(my_list):
    '''
    Implements the quicksort algorithm
    '''
    # Base case: if the list has one or less elements, it's considered sorted
    if len(my_list) <= 1:
        return my_list 

    # assign the pivot point as the first element
    pivot = my_list[0]

    # Create two sublists, one for items less than the pivot and one for greater
    # These are essentially for loops, but we use Python list comprehension to do each on one line
    less_than_pivot = [i for i in my_list[1:] if i <= pivot] 
    greater_than_pivot = [i for i in my_list[1:] if i > pivot]

    # Now recursively call quicksort on the left and right sub-lists
    # In the end, we'll be returning <sorted left list>, pivot, <sorted right list>
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)


# #### Time Complexity Test

# ##### Define the list sizes I want to test

# In[ ]:


list_sizes = [100, 1000, 10000, 100000, 1000000]


# ##### Iterate to create lists for each test size, and observe the average performance for them

# In[ ]:


# iterate through all requested list sizes
for list_size in list_sizes:
    
    # Creata a set of unique keys for the specified list_size
    str_set = set({})
    while len(str_set) < list_size:
        # generate a very large random integer, convert it to a string, and add to set
        str_set.add(str(random.randint(0, 1000000000)))
    
    # convert the set to a list
    str_list = list(str_set)

    # generate some random keys to searcho for
    random_keys = []
    for x in range(10):
        random_keys.append(str_list[random.randint(0, len(str_list) - 1)])

    print(f"\n------------------ Sorting {len(str_list):,d} elements ------------------")
    
    # start timer
    start_time = time.perf_counter()
    
    # sort using merge_sort
    sorted_list = quicksort(str_list)
    
    # stop timer and calculate elapsed time
    end_time = time.perf_counter()
    quicksort_time = end_time - start_time
    
    # print sorted function time
    print(f"Quicksort time: {quicksort_time:.6f} seconds")


# #### How did that fare?
# **If** you **compare to** the **O(log n)** of binary search, this one **didn't stay super fast forever**. **But** even for 1,000,000 items, it did complete in a reasonable time. If you **compare** that **to the **O(n<sup>2</sup>)** bubble sort**, that's much **much faster**.

# ## Factorial time complexity: O(n!) 
# An algorithm has a factorial time complexity when its runtime grows factorially based on the size of the input data. 
# 
# For those who don't know, the **"factorial of n"** is **represented as "n!"**, and it it's the product of n * (n - 1) * (n - 2) * ... * 1.
# 
# Examples:
# - 3! = 3 * 2 * 1 = 6
# - 4! = 4 * 3 * 2 * 1 = 24
# - 5! = 5 * 4 * 3 * 2 * 1 = 120

# This may seem like an unlikely thing to need in computing, but it's actually **frequently used in combinatorial and statistics problems**. 
# 
# One of the **simplest examples**, is **generating permutations**. For instance, imagine **you have a class of students**, and you want to decide **how many possible ways** you can **line up the students for a class** picture. That would be a **permutation problem**. **Depending on how many** students you have in the class, that **number can be very very high**. For instance, even in a class of 15 students, there would be 1,307,674,368,000 possible arrangements. That's in the order of 1 trillion!!!

# ### Algorithm example: generating permutations
# The algorithm or permutations is a classic recursion example.

# In[ ]:


def generate_permutations(elements, current_permutation=[], all_permutations = []): 
    # Recursion exit: if there are no more elements to add, add the current permutation to result list
    if not elements: 
        all_permutations.append(current_permutation) 
    else:
        # iterate through list of elemenst
        for i in range(len(elements)):
            # build a list of all items except the current element
            remaining_elements = elements[:i] + elements[i + 1:] 
            # now recursively generate permutations of all the other items, while adding the current element to the current permutation
            generate_permutations(remaining_elements, current_permutation + [elements[i]], all_permutations)

    # return the list of all permutations
    return all_permutations


# ##### Very quick example of the execution

# In[ ]:


students = ["John", "Diego", "Ana", "Soo-jin Ki"]
all_permutations = generate_permutations(students)
for permutation in all_permutations:
    print(permutation)


# Wow! That's a lot of options for just 4 students!

# #### Time Complexity Test

# ##### Define the list sizes I want to test

# In[ ]:


list_sizes = [2 , 4, 6, 8, 10]


# ##### Iterate to create lists for each test size, and observe the average performance for them

# In[ ]:


# iterate through all requested list sizes
for list_size in list_sizes:
    
    # Creata a set of unique keys for the specified list_size
    str_set = set({})
    while len(str_set) < list_size:
        # generate a very large random integer, convert it to a string, and add to set
        str_set.add(str(random.randint(0, 1000000000)))
    
    # convert the set to a list
    str_list = list(str_set)

    print(f"\n------------------ Generating permutations for {len(str_list):,d} elements ------------------")
    
    # start timer
    start_time = time.perf_counter()
    
    # sort using merge_sort
    permutations = generate_permutations(str_list)
    
    # stop timer and calculate elapsed time
    end_time = time.perf_counter()
    permutations_time = end_time - start_time
    
    # print sorted function time
    print(f"Generating permutations time: {permutations_time:.6f} seconds")


# #### How did that fare?
# Did you see that?! Good thing I didn't try this for 1,000,000. We would all be long gone for this earth before it was done :-)
# 
# In fact, you can see the performance was already going downhill fast, even in a number as little as 10.

# In[ ]:




