#!/usr/bin/env python
# coding: utf-8

# # <span style="color:blue">Insertion Sort Analysis
# AWS CLOUD INSTITUTE: PROVIDED FOR EDUCATIONAL INSTRUCTIONAL PURPOSES ONLY.

# ## Insertion Sort
# Insertion sort **progressively builds** a **sorted list** from **left to right**, **one element at a time**.
# - Iterate forward, **starting at the beginning**
# - **Make** the **item at the current position "the key"**
#     - **Iterate backward from** the **current location** to the beginning of the list
#         - **Compare key to each previous item**, and place the key in the correct location 
# - Now go back to the top of the loop, which will move the loop forward to the next list position
# 
# This is not an easy algorithm to visualize, so we'll have a version with print statements later.

# ### Insertion sort implementation

# In[ ]:


def insertion_sort(my_list):

    # iterate forward, one index at the time, starting at the second item (index = 1)
    for i in range(1, len(my_list)):
        key = my_list[i]

        # now iterate backwards from key item, until we find an item >= than the key item (or reach the beginning)
        j = i - 1
        while j >= 0 and key < my_list[j]:
            # move the current item forward, since it's bigger than the key
            my_list[j + 1] = my_list[j]
            
            # decrease the index so we can keep moving backward
            j -= 1
        
        # at the end of the loop, we must at the point where we hit an item smaller than the key
        # so we can place the key after it
        my_list[j + 1] = key

    return my_list


# ### Basic test

# In[ ]:


# define a simple list
int_list = [8, 5, 2, 4, 3, 1, 10, 9, 7, 6]
print(f"Original list: {int_list}")

# sort the list
sorted_list = insertion_sort(int_list)

# print sorted lists
print(f"Sorted list: {sorted_list}")


# #### Does the original list get changed?

# In[ ]:


print(f"Original list after sorting: {int_list}")


# Yes, the algorithm modifies the input list. If we didn't want that behavior, we could make a copy before calling it.

# ### Modified version with print statements
# Let's create a **modified version**, **with print statements** (hence the "_wp" in the name, as in "with print") to **visualize what happens** during the sorting processing.

# In[ ]:


def insertion_sort_wp(my_list):

    # iterate forward, one index at the time, starting at the second item (index = 1)
    for i in range(1, len(my_list)):
        key = my_list[i]
        print(f"Iteration {i} - List: {my_list} - Key: {key}")
        print(f"                    <-" + "|".rjust(3*i,"-"))
        
        # now iterate backwards from key item, until we find an item >= than the key item (or reach the beginning)
        j = i - 1
        while j >= 0 and key < my_list[j]:
            print(f"    Key({key}) < {my_list[j]}, so move {my_list[j]} forward")
            # move the current item forward, since it's bigger than the key
            my_list[j + 1] = my_list[j]
            # decrease the index so we can keep moving backward
            j -= 1
            print(f"    List after change: {my_list}")

        # at the end of the loop, we must at the point where we hit an item smaller than the key
        # so we can place the key after it
        my_list[j + 1] = key
        
        # print message depending on why we exited loop
        if (j < 0):
            print(f"Exited loop at beginning - Inserted key({key}) there")
        else:
            print(f"Exited loop when Key({key}) > {my_list[j]} - Inserted key after {my_list[j]}")

        print(f"List after iteration: {my_list}\n")

    return my_list


# #### Smaller test
# Let's test with a small list, because this will print a lot.

# In[ ]:


# define a small list
int_list = [5, 2, 4, 1, 3]

# sort the list
sorted_list = insertion_sort_wp(int_list)

# print sorted lists
print(f"\nFinal sorted list: {sorted_list}")


# ### Complexity analysis
# In this **average case**, I can see I **have an outer loop**, **and most of the time** I'll execute **several steps in the inner loop**. So it's a typical n * n.
#   
# - **Time complexity for average case: <span style="color:blue">O(n<sup>2</sup>)**</span>

# In[ ]:


# define a small list
int_list = [1, 2, 3, 4, 5]

# sort the list
sorted_list = insertion_sort_wp(int_list)

# print sorted lists
print(f"\nFinal sorted list: {sorted_list}")


# ### Complexity analysis
# In this case my **list was fully sorted**, I **never** had to **go into** my **inner loop** and do any swaps. So it's like I only had a single loop. So in this case, **instead of the O(n<sup>2</sup>)**, I get from the nested loops, my **peformance would be O(n).**
#   
# - **Time complexity for fully ordered list: <span style="color:blue">O(n)**</span>

# In[ ]:




