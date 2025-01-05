#!/usr/bin/env python
# coding: utf-8

# # <span style="color:blue">Sorting algorithms
# AWS CLOUD INSTITUTE: PROVIDED FOR EDUCATIONAL INSTRUCTIONAL PURPOSES ONLY.

# # Sorting Algorithms
# In **most cases**, we should be able to **use** the **built-in Python *sort()*** method and ***sorted()*** functions. **However** it's **helpful to understand** the characteristics of popular **searching algorithms**. This will help us understand **time complexity differences, and interesting examples of recursion**. We'll focus our discussion on three well known algorithms.
# - Bubble sort
# - Merge sort
# - Quicksort

# ## Bubble Sort
# In bubble sort, **adjacent elements in a list are compared and swapped** until the entire list is sorted. Elements "bubble" to their correct position in the list. 

# ### Bubble sort implementation

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


# ### Basic test

# In[ ]:


# define a simple list
int_list = [8, 5, 2, 4, 3, 1, 10, 9, 7, 6]
print(f"Original list: {int_list}")

# sort the list
sorted_list = bubble_sort(int_list)

# print sorted lists
print(f"Sorted list: {sorted_list}")


# #### Does the original list get changed?

# In[ ]:


print(f"Original list after sorting: {int_list}")


# Yes, the algorithm modifies the input list. If we didn't want that behavior, we could make a copy before calling it.

# ### Modified version with print statements
# Let's create a **modified version**, **with print statements** (hence the "_wp" in the name, as in "with print") to **visualize what happens** during the sorting processing.

# In[ ]:


def bubble_sort_wp(my_list):
    """
    Sorts the given list using the Bubble Sort algorithm.
    This algorithm modifies the list in place.
    """
    # Get the length of the list
    n = len(my_list)

    # Outer loop to traverse through the list
    for i in range(n):
        print(f"\nITERATION {i+1} - List: {my_list}")
        for j in range(0, n-i-1):
            print(f"   Comparing ({my_list[j]}, {my_list[j+1]}) ...")
            # Compare adjacent elements
            if my_list[j] > my_list[j+1]:
                # Swap elements if they are in the wrong order
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
                print(f"   SWAP ({my_list[j]}, {my_list[j+1]}) - Updated list: {my_list}")
            else:
                print(f"   NO swap - List not changed: {my_list}")
    
    # Return the sorted list
    return my_list


# #### Smaller test
# Let's test with a small list, because this will print a lot.

# In[ ]:


# define a small list
int_list = [5, 2, 4, 1, 3]

# sort the list
sorted_list = bubble_sort_wp(int_list)

# print sorted lists
print(f"\nFinal sorted list: {sorted_list}")


# Note that the **last two iterations** were **wasted**. In fact, if we call our **standard bubble_sort with a fully sorted list**, it will **take as long** as one **completely unsorted**. Let's see that.

# In[ ]:


# define a small list
int_list = [1, 2, 3, 4, 5]

# sort the list
sorted_list = bubble_sort_wp(int_list)

# print sorted lists
print(f"\nFinal sorted list: {sorted_list}")


# The code still went through all the iterations, even though it didn't have to change anything. Can we improve that?

# ### <span style="color:blue">OPTIONAL:</span> Enhanced bubble sort with early exit
# This version will **track whether swaps occurred**, and **exit earlier** if we are done.

# In[ ]:


def bubble_sort_enhanced_wp(my_list):
    """
    Sorts the given list using the Bubble Sort algorithm.
    This algorithm modifies the list in place.
    """
    # Get the length of the list
    n = len(my_list)

    # Outer loop to traverse through the list
    for i in range(n):
        # initialize variable to track whether any swaps occurred
        swapped = False
    
        print(f"-------- Iteration {i+1} --------")
        for j in range(0, n-i-1):
            # Compare adjacent elements
            if my_list[j] > my_list[j+1]:
                # Swap elements if they are in the wrong order
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
                print(f"Swapped ({my_list[j]}, {my_list[j+1]}) - List: {my_list}")

                # update flag to indicate a swap occurred
                swapped = True

        # if no swaps occurred, the list is already sorted, so we can stop
        if not swapped:
            print("No swaps occurred. We are done!")
            break
    
    # Return the sorted list
    return my_list


# #### Test with an almost sorted lists

# In[ ]:


# define a small list
int_list = [1, 4, 3, 2, 5]

# sort the list
sorted_list = bubble_sort_enhanced_wp(int_list)

# print sorted lists
print(f"\nFinal sorted list: {sorted_list}")


# #### Clean Enhanced bubble sort version
# Let's have a clean version of the enhanced bubble sort, so we can use for comparisons later. **Nothing changed, but** just **removing** the **print statements.**

# In[ ]:


def bubble_sort_enhanced(my_list):
    """
    Sorts the given list using the Bubble Sort algorithm.
    This algorithm modifies the list in place.
    """
    # Get the length of the list
    n = len(my_list)

    # Outer loop to traverse through the list
    for i in range(n):
        # initialize variable to track whether any swaps occurred
        swapped = False
    
        for j in range(0, n-i-1):
            # Compare adjacent elements
            if my_list[j] > my_list[j+1]:
                # Swap elements if they are in the wrong order
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

                # update flag to indicate a swap occurred
                swapped = True

        # if no swaps occurred, the list is already sorted, so we can stop
        if not swapped:
            break
    
    # Return the sorted list
    return my_list


# ### Bubble sort complexity analysis
# **With** that **nested loop**, we can see that in the **worst case**, the **inner loop** will **execute *n* times** for **every** one of the ***n* iterations of** the **outer loop**. So we will execute **(n \* n)** steps, or **n<sup>2</sup>**.
# - **Time complexity: <span style="color:blue">O(n<sup>2</sup>)**</span>
# - **Space complexity: <span style="color:blue">O(1)**</span>

# ## Merge Sort
# Merge sort **divides an array into smaller sub-arrays, sorts every sub-array, and then merges the sorted sub-arrays back together** to form the final sorted array. It is **based on** the **divide-and-conquer strategy** using recursion.

# ### Merge sort implementation
# Merge sort is a **divide and conquer algorithm**, and in it there is a **very clear split of these phases**.
# - The main ***merge_sort* function** is the one initially calles, and **recursively divides equally** the **lists into smaller sublists**
# - Then, the ***ordered_merge* functions** **merges** the two **sublists** while **ordering** the **elements**.

# #### The main *merge_sort()* function
# This is the function that will be initially called. It will do the job of recursively splitting the lists, and then calling ordered_merge to put them together in sorted order.

# In[ ]:


def merge_sort(my_list):
    '''
    The merge_sort function follows the divide-and-conquer approach to sort the input list.
    It works by recursively dividing the input array into two halves, sorting each half,
    and then merging the sorted halves back together into a single sorted array.
    '''
    
    # Base case: if my list length is 1 or 0, then there is nothing to split
    if len(my_list) <= 1:
        return my_list

    # split the list in two halves
    mid = len(my_list) // 2
    left_half = my_list[:mid]
    right_half = my_list[mid:]
          
    # recursively sort the two halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # merge the sorted halves
    return ordered_merge(left_half, right_half)


# #### The *ordered_merge()* function
# This *ordered_merge* function does most of the actual sorting. Some implementations just call it simply *merge*, but I find that to be an "disservice" to the function. Because ***ordered_merge*** is **not simply merging lists**, **but** it's **making sure** the **items** are **merged in order**.

# In[ ]:


def ordered_merge(left_list, right_list):
    '''
    The merge function is responsible for merging the sorted left and right halves
    into a single sorted array. It is called after the recursive calls to merge_sort
    have sorted the left and right halves.
    '''
    # initialize a result list
    result = []

    # Iterate simultaneously through left an right lists
    # The iteration is not symetrical, alternating left an right.
    # It will pick the smallest elements first, from either list.
    # This means any leftover items, will be guarantee to be larger
    left_idx = right_idx = 0
    while left_idx < len(left_list) and right_idx < len(right_list):
        # if the left item is smaller or equal ...
        if left_list[left_idx] <= right_list[right_idx]:
            # add the left element, and move the left index forward
            result.append(left_list[left_idx])
            left_idx += 1
        # else, the right element is smaller ...
        else:
            # add the right element, and move the right index forward
            result.append(right_list[right_idx])
            right_idx += 1

    # After the loop, we might have left over items, but based on the logic
    # of the loop, they will certainly be larger, so we add them to the end.
    # It's ok if one of the lists we are adding is empty. The extend method
    # will simply not extend anything
    result.extend(left_list[left_idx:])
    result.extend(right_list[right_idx:])
    
    return result


# ### Quick test

# In[ ]:


# define a small list
int_list = [4, 6, 1, 2, 5, 3]

# sort the list
sorted_list = merge_sort(int_list)

# print sorted lists
print(f"\nSorted list: {sorted_list}")


# #### Was my original list changed?

# In[ ]:


#print original list
print(f"\nOriginal list: {int_list}")


# **No**. This algorithm is **not changing** the **list in place**. If we look at it, we can see ***ordered_merge*** **creates** a **new *result* list** to accumulate the sorted values.

# ### Modified version with print statements
# Once again, let's create a **modified version**, **with print statements** to **visualize what happens** during the sorting processing. Since we are using recursion, we'll also **add** an ***rlevel* parameter** to **track how far into the recursions we are**, so we can do some fancy indenting.

# #### The main *merge_sort_wp()* function

# In[ ]:


def merge_sort_wp(my_list, rlevel = 0):
    '''
    The merge_sort function follows the divide-and-conquer approach to sort the input list.
    It works by recursively dividing the input array into two halves, sorting each half,
    and then merging the sorted halves back together into a single sorted array.
    '''
    
    # Base case: if my list length is 1 or 0, then there is nothing to split
    print()
    print("".rjust(rlevel*4) + f">>> Sorting: {my_list}")
    if len(my_list) <= 1:
        print("".rjust(rlevel*4) + f"<< Returning sorted: {my_list}")
        return my_list

    # split the list in two halves
    mid = len(my_list) // 2
    left_half = my_list[:mid]
    right_half = my_list[mid:]
    print("".rjust(rlevel*4) + f"Split: Left={left_half}  -  Right={right_half}")
          
    # recursively sort the two halves
    print("".rjust(rlevel*4) + f"Recursing on Left ...")
    left_half = merge_sort_wp(left_half, rlevel +1)
    print("\n" + "".rjust(rlevel*4) + f"Recursing on Right ...")
    right_half = merge_sort_wp(right_half, rlevel +1)

    # merge the sorted halves
    merged_list = ordered_merge_wp(left_half, right_half, rlevel)
    print("".rjust(rlevel*4) + f"<< Returning merge sorted: {merged_list}")
    return merged_list


# #### The *ordered_merge_wp*() function

# In[ ]:


def ordered_merge_wp(left_list, right_list, rlevel):
    '''
    The merge function is responsible for merging the sorted left and right halves
    into a single sorted array. It is called after the recursive calls to merge_sort
    have sorted the left and right halves.
    '''
    print()
    print("".rjust(rlevel*4) + f">>## Merging {left_list} and {right_list}")
    
    # initialize a result list
    result = []

    # Iterate simultaneously through left an right lists
    # The iteration is not symetrical, alternating left an right.
    # It will pick the smallest elements first, from either list.
    # This means any leftover items, will be guarantee to be larger
    left_idx = right_idx = 0
    while left_idx < len(left_list) and right_idx < len(right_list):
        # if the left item is smaller or equal ...
        if left_list[left_idx] <= right_list[right_idx]:
            # add the left element, and move the left index forward
            result.append(left_list[left_idx])
            left_idx += 1
        # else, the right element is smaller ...
        else:
            # add the right element, and move the right index forward
            result.append(right_list[right_idx])
            right_idx += 1

    # After the loop, we might have left over items, but based on the logic
    # of the loop, they will certainly be larger, so we add them to the end.
    # It's ok if one of the lists we are adding is empty. The extend method
    # will simply not extend anything
    result.extend(left_list[left_idx:])
    result.extend(right_list[right_idx:])
    
    print("".rjust(rlevel*4) + f"<<## Merged result {result}")
    return result


# ### Re-run test and observe ...
# We're running the same exact test, but pay close attention to the output of the print statements.
# - Note that we don't start merging, until the lists are broken down to single elements
# - Watch as we build them back up, how each individual part gets merged in order

# In[ ]:


# define a small list
int_list = [4, 6, 1, 2, 5, 3]

# sort the list
sorted_list = merge_sort_wp(int_list)

# print sorted lists
print(f"\nSorted list: {sorted_list}")


# ### Merge sort complexity analysis
# To understand the merge sort **time complexity**, we have to look at the two main parts:
# - The ***merge_sort* part** does all of the **successive splits**. As we've seen before when looking at binary searches, the process of repeately splitting a list will have **order *log(n)***.
# - But then **for each** of those splits, the ***ordered_merge*** function will **iterate through** the **sub-lists**. If we look at that algorithm, we iterated through them together. It wasn't a nested loop, but a **single loop**. As we've seen before, iterating through a single loop will be **order *n***.
# 
# So the final time complexity will be **order *n* times *log(n)***, or ***O(n log(n))***
# 
# It's worth noting that the *ordered_merge* function, will iterate through the full sublists regardless of whether the list of how will the lists are already sorted. So it will always do the same number of steps. That means that ***O(n log(n))*** **complexity is consistent**, regardless of the input list.
# 
# For **space complexity**, we need to see what additional memory requirements there are beyond the original list. If we look at the ***ordered_merge*** function, it **creates** a **new list for the result**, and it will insert the same *n* elements there (in order). So we have **O(n)** complexity.
#   
# - **Time complexity: <span style="color:blue">O(n log n)**</span>
# - **Space complexity: <span style="color:blue">O(n)**</span>

# ## Quicksort
# Fo starters, it's not a typo in the name, there is **no space between "quick" and "sort"**. **"Quicksort"** is the **name of the algorithm**.
# 
# Quicksort **selects a pivot and partitions the input list into two sub-lists**, one with items smaller than the pivot and the second with larger items. The algorithm then **sorts both sub-lists recursively until the entire list is completely sorted**.
# 
# That sounds very similar to merge sort at a high level, but we'll see the differences when we look at the details.

# ### Quicksort implementation
# The first obvious difference if quicksort, is how short the algorithm is. We don't have the the two phases calling each other. It's just one recursive function.

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


# ### Quick test

# In[ ]:


# define a small list
int_list = [2, 5, 1, 4, 6, 3]

# sort the list
sorted_list = quicksort(int_list)

# print sorted lists
print(f"\nSorted list: {sorted_list}")


# #### Was my original list changed?

# In[ ]:


#print original list
print(f"\nOriginal list: {int_list}")


# **No**. This algorithm is **not changing** the **list in place**. The **list comprehension steps** are **creating new lists** for the **left and right sides**.

# ### Modified version with print statements
# Once again, let's create a **modified version**, **with print statements** to **visualize what happens** during the sorting processing. Since we are using recursion, we'll also **add** an ***rlevel* parameter** to **track how far into the recursions we are**, so we can do some fancy indenting.

# In[ ]:


def quicksort_wp(my_list, rlevel = 0):
    '''
    Implements the quicksort algorithm
    '''
    print()
    print("".rjust(rlevel*4) + f">>> Sorting: {my_list}")

    # Base case: if the list has one or less elements, it's considered sorted
    if len(my_list) <= 1:
        print("".rjust(rlevel*4) + f"<< Returning sorted: {my_list}")
        return my_list 

    # assign the pivot point as the first element
    pivot = my_list[0]
    print("".rjust(rlevel*4) + f"Pivot: {pivot}")
    
    # Create two sublists, one for items less than the pivot and one for greater
    # These are essentially for loops, but we use Python list comprehension to do each on one line
    less_than_pivot = [i for i in my_list[1:] if i <= pivot] 
    greater_than_pivot = [i for i in my_list[1:] if i > pivot]
    
    # Now recursively call quicksort on the left and right sub-lists
    # In the end, we'll be returning <sorted left list>, pivot, <sorted right list>
    print("".rjust(rlevel*4) + f"Invoking: quicksort({less_than_pivot}) + {pivot} + quicksort({greater_than_pivot})")

    left_sort = quicksort_wp(less_than_pivot, rlevel + 1) 
    right_sort = quicksort_wp(greater_than_pivot, rlevel + 1)
    print("".rjust(rlevel*4) + f"Combining: {left_sort} + {pivot} + {right_sort}")

    sorted_list = left_sort + [pivot] + right_sort
    print("".rjust(rlevel*4) + f"<< Returning: {sorted_list}")
    
    return sorted_list


# ### Re-run test and observe ...
# We're running the same exact test, but pay close attention to the output of the print statements.
# - Note that we repeatedly split the list, but not always in half. Depending on the pivot, it maybe an uneven split.
# - Every invocation will split into two recursive calls, so look for the same indendation to visuallize when the result of both calls completed

# In[ ]:


# define a small list
int_list = [2, 5, 1, 4, 6, 3]

# sort the list
sorted_list = quicksort_wp(int_list)

# print sorted lists
print(f"\nSorted list: {sorted_list}")


# ### Quicksort complexity analysis
# Similar to the merge sort, the quicksort algorithm **time complexity** will break based on two different parts:
# - **In** a **case** where the **pivot value splits the list near half** each time, the number of **recursive executions** would be in the **order *log(n)***. Similar to our binary searches. However, **if** we are very unlucky in the way the list is ordered initially, and the **pivot splits** are very **uneven**, we could end up **recursively calling *n* times**, which would make that **worst case O(n)**.
# - **Within** the **iterations**, we need to **loop through the list** to split items less than and greater than. That would be a simple **order *n***.
# 
# So the final time complexity might depending on the original order of the list. If the splits are relatively even, the order will be **order *n* times *log(n)***, or ***O(n log(n))*** . But if the splits are very uneven, it could be approach **order *n* times *n***, or ***O(n<sup>2</sup>)***. We'll see an **example below**.
# 
# For **space complexity**, we create new less than and greater than lists each time we recurse, and insert the same *n* elements there (half in each). So we have **O(n)** complexity.
#   
# - **Time complexity**:
#     - Average case: **<span style="color:blue">O(n log(n))**</span>
#     - Worst case: **<span style="color:blue"> O(n<sup>2</sup>)**</span>
# - **Space complexity: <span style="color:blue">O(n)**</span>

# #### Quicksort worst case
# **To** better **visualize** the **worst case scenario** above, let's **re-run** the **example** above, but **using** a **list** that is **already sorted**. You might think that would be the fastest, but it will actually be the slowest. Because we are using the first element as the pivot, **note in the output** that we are **only reducing the list by 1 in each iteration**. So instead of the log(n) reduction we get when we split in half, we are simply going one by one, or O(n).
# 
# You might be tempted to think that's only a problem because we picked the first element as the pivot, but that can happen regardless of which pivot we pick. It's just that with different pivots, the type of list that leads to the worst case would change.

# In[ ]:


# define a small list
int_list = [1 , 2 , 3 , 4 , 5 , 6]

# sort the list
sorted_list = quicksort_wp(int_list)

# print sorted lists
print(f"\nSorted list: {sorted_list}")


# # <span style="color:blue">OPTIONAL</span>: The Final Showdown!!!
# Let's compare the three algorithms we looked at, using the same mechanisms we've been using in other examples to generate strings and time the calls.
# 

# #### Import modules
# We'll be using a couple of modules in the upcoming analysis, so we'll import them here

# In[ ]:


import time
import random


# ##### Define the list sizes I want to test

# In[ ]:


list_sizes = [100, 1000, 10000]


# ##### Iterate to create lists for each test size, and compare average performance for them

# In[ ]:


# iterate through all requested list sizes
for list_size in list_sizes:
    
    # intially use a set, to guarantee no duplicates
    str_set = set({})
    while len(str_set) < list_size:
        # generate a very large random integer, convert it to a string, and add to set
        str_set.add(str(random.randint(0, 1000000000)))
    
    # convert the set to a list
    str_list = list(str_set)

    print(f"\n------------------ Sorting {len(str_list):,d} elements ------------------")

    ########################## testing merge sort ##########################
    # start timer
    start_time = time.perf_counter()
    
    # sort using merge_sort
    sorted_list = merge_sort(str_list)
    
    # stop timer and calculate elapsed time
    end_time = time.perf_counter()
    merge_sort_time = end_time - start_time
    
    # print sorted function time
    print(f"Merge sort time: {merge_sort_time:.6f} seconds")

    ########################## testing quicksort ##########################
    # start timer
    start_time = time.perf_counter()
    
    # sort using merge_sort
    sorted_list = quicksort(str_list)
    
    # stop timer and calculate elapsed time
    end_time = time.perf_counter()
    quicksort_time = end_time - start_time
    
    # print sorted function time
    print(f"Quicksort time: {quicksort_time:.6f} seconds")

    ########################## testing bubble sort ##########################
    # start timer
    start_time = time.perf_counter()
    
    # sort using merge_sort
    sorted_list = bubble_sort_enhanced(str_list)
    
    # stop timer and calculate elapsed time
    end_time = time.perf_counter()
    bubble_sort_time = end_time - start_time
    
    # print sorted function time
    print(f"Bubble sort time: {bubble_sort_time:.6f} seconds")

    # calculate the performance improvement
    perf_factor1 = bubble_sort_time / merge_sort_time
    perf_factor2 = bubble_sort_time / quicksort_time
    print(f"Merge sort was {perf_factor1:.1f} times faster than bubble sort.")
    print(f"Quicksort was {perf_factor2:.1f} times faster than bubble sort.")


# ### Conclusions
# We can see that both **merge sort and quick sort** are **much faster than bubble sort**, and that difference becomes **even more pronounced** as the **list grows in size**. In fact we can't even try for a larger list size, or the bubble sort would take too long to run. That illustrates the **marked difference** between an **O(n<sup>2</sup>) algorithm and** a **O(n log(n)) algorithm**.
# 
# With these small sample sizes and number of executions it's harder to compare quicksort and merge sort. So let's repeate the comparison, but without bubble sort, we can try some bigger sizes.

# ##### Define the list sizes I want to test

# In[ ]:


list_sizes = [10000, 100000, 1000000]


# ##### Iterate to create lists for each test size, and compare average performance for them

# In[ ]:


# iterate through all requested list sizes
for list_size in list_sizes:
    
    # intially use a set, to guarantee no duplicates
    str_set = set({})
    while len(str_set) < list_size:
        # generate a very large random integer, convert it to a string, and add to set
        str_set.add(str(random.randint(0, 1000000000)))
    
    # convert the set to a list
    str_list = list(str_set)

    print(f"\n------------------ Sorting {len(str_list):,d} elements ------------------")

    ########################## testing merge sort ##########################
    # start timer
    start_time = time.perf_counter()
    
    # sort using merge_sort
    sorted_list = merge_sort(str_list)
    
    # stop timer and calculate elapsed time
    end_time = time.perf_counter()
    merge_sort_time = end_time - start_time
    
    # print sorted function time
    print(f"Merge sort time: {merge_sort_time:.6f} seconds")

    ########################## testing quicksort ##########################
    # start timer
    start_time = time.perf_counter()
    
    # sort using merge_sort
    sorted_list = quicksort(str_list)
    
    # stop timer and calculate elapsed time
    end_time = time.perf_counter()
    quicksort_time = end_time - start_time
    
    # print sorted function time
    print(f"Quicksort time: {quicksort_time:.6f} seconds")

    # calculate the performance improvement
    perf_factor = quicksort_time / merge_sort_time

    # print different message depending on who was faster
    if (perf_factor > 1):
        print(f"Merge sort was {perf_factor:.1f} times faster than quicksort.")
    else:
        print(f"Quicksort was {(1/perf_factor):.1f} times faster than merge sort.")


# ### Conclusions
# I ran this many times, and **usually quicksort outperformed merge sort by a small margin** (somewhere around 1.2 times faster). However, it's **important to remember** that **merge sort has** an **advantage of being stable**, meaning that its **performance will not vary** **depending on** the **order of the input list**.
# 
# To my knowledge, there is no universally accepted best practice. It depends on the list size, and how random your input list is. In the end, the key fact is that they are very close, and both infinitely faster than one of the O(n<sup>2</sup>) algorithms.
