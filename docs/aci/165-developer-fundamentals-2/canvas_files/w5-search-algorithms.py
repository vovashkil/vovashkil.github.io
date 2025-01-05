#!/usr/bin/env python
# coding: utf-8

# # <span style="color:blue"> Search Algorithms
# AWS CLOUD INSTITUTE: PROVIDED FOR EDUCATIONAL INSTRUCTIONAL PURPOSES ONLY.

# # Linear Search

# The **linear search algorithm** tries to **search** for the desired element by **going over** the **list sequentially**. It **compares every element** in the list **to** the **one** you are **looking for**.

# ## Search for location of an item in a list or array
# This method will do the common operation of **searching for** an **item in a list** or array. It will **return** the **index of the item** if found, or **-1 if not found**.

# In[ ]:


def linear_search(items, search_value):
    for i in range(len(items)):
        if items[i] == search_value:
            return i
    return -1


# This function **can be used** for **any data type** that **supports** an **equality operator**.

# ### Time and space complexity
# - **Time complexity: <span style="color:blue">O(n)**</span>
# - **Space complexity: <span style="color:blue">O(1)**</span>

# ### Test with builtin Python data types

# #### Test with integers

# In[ ]:


# Define a simple list of 10 numbers
int_list = [8, 2, 9, 7, 10, 6, 3, 1, 4, 5]


# In[ ]:


# Test with item present in the list
val = 4
idx = linear_search(int_list, val)
if (idx != -1):
    print(f"Index of {val} is {idx}")
else:
    print(f"{val} was not found")

# Test with item NOT present in the list
val = 20
idx = linear_search(int_list, val)
if (idx != -1):
    print(f"Index of {val} is {idx}")
else:
    print(f"{val} was not found")


# Note that this is **exactly** the **same result** we would get **if** we **used** the **standard Python list** *index()* method. Let's **copy/paste almost the same test**, but **use** the *index()* **operation** instead. The **only difference** is that instead of returning a "-1" when an item is not found, the **Python list** method **raises** an **exception** we need to catch.

# In[ ]:


# Test with item present in the list
val = 4
try:
    idx = int_list.index(val)
    print(f"Index of {val} is {idx}")
except ValueError:
    print(f"{val} was not found")


# Test with item NOT present in the list
val = 20
try:
    idx = int_list.index(val)
    print(f"Index of {val} is {idx}")
except ValueError:
    print(f"{val} was not found")


# As expected, the **result** is **precisely the same**. But **now** when we use the Python list *index()* method, **we know what's happening underneath**.

# #### Test with string

# In[ ]:


# create a list of strings with some of my dogs and cats
str_list = ["Rebecca", "Tracy", "Sammy", "Luke", "Max", "Tucker", "Moose", 
            "Miley", "Mittenz",  "Lexi", "Finn"]


# In[ ]:


# Test with item present in the list
val = "Luke"
idx = linear_search(str_list, val)
if (idx != -1):
    print(f"Index of {val} is {idx}")
else:
    print(f"{val} was not found")
    
# Test with item NOT present in the list
val = "Scooby Doo"
idx = linear_search(str_list, val)
if (idx != -1):
    print(f"Index of {val} is {idx}")
else:
    print(f"{val} was not found")


# ### <span style="color:blue">Optional:</span> Test with custom types
# **If** we **want** to **perform** a **linear search with** my **own class** objects, I just need to make sure items can be compared. For a custom class, that means the **class** needs to **implement** the ***\_\_eq\_\_*** operator.
# 
# **Note** that I'm **not changing** my **linear search function**. It's the same one I used for ints and strings. 

# #### Define my own class

# In[ ]:


class Pet:
    '''
    This class stores information about a house pet.
    '''
    def __init__(self, name, species, breed):
        self.name = name
        self.species = species
        self.breed = breed

    def __eq__(self, other):
        '''
        This method overrides the equality operator.
        '''
        return (self.name == other.name and 
                self.species == other.species and
                self.breed == other.breed)

    def __repr__(self):
        return f"({self.name},{self.species},{self.breed})"
        
    def __str__(self):
        return f"{self.name} - {self.species} - {self.breed}"


# In[ ]:


# create a list of Pet objects with some of my dogs, cats, ferrets, guinea pigs, hamsters, and birds
pet_list = [Pet("Rebecca", "Dog", "Golden Retriever"),
            Pet("Tracy", "Dog", "Golden Retriever"),
            Pet("Sammy", "Dog", "Labrador Retriever"),
            Pet("Luke", "Dog", "Labrador Retriever"),
            Pet("Max", "Dog", "Cavalier King Charles Spaniel"),
            Pet("Tucker", "Dog", "Golden Retriever"),
            Pet("Moose", "Dog", "German Spitz"),
            Pet("Miley", "Cat", "American Shorthair"),
            Pet("Mittenz", "Cat", "Calico"),
            Pet("Lexi", "Cat", "Munchkin"),
            Pet("Finn", "Cat", "Munchkin"),
            Pet("Indy", "Ferret", "Sable"),
            Pet("Deedee", "Ferret", "Sable"),
            Pet("Ruby", "Ferret", "Sable"),
            Pet("Bullet", "Tortoise", "Greek"),
            Pet("Buttercup Baby", "Guinea Pig", "American"),
            Pet("Mickey", "Hamster", "Syrian"),
            Pet("Bluey", "Parakeet", "Budgerigar"),
            Pet("Greeney", "Parakeet", "Budgerigar")
           ]
print(pet_list)


# In[ ]:


# Test with item present in the list
val = Pet("Tucker", "Dog", "Golden Retriever")
idx = linear_search(pet_list, val)
if (idx != -1):
    print(f"Index of {val.name} is {idx}")
else:
    print(f"{val.name} was not found")
    
# Test with item NOT present in the list
val = Pet("Otto", "Dog", "Doberman")
idx = linear_search(pet_list, val)
if (idx != -1):
    print(f"Index of {val.name} is {idx}")
else:
    print(f"{val.name} was not found")


# # Binary Search

# **Binary search searches for the desired element** by **repeatedly eliminating half** of the **search space** and searching in the other half. It divides the search space into two in every iteration, hence the name binary. Binary search **requires** that a **list is in order**, ascending or descending.
# 
# You can **implement binary search using regular iteration, or recursion**. Let's examine both.

# ## Binary Search using iteration
# Let's implement the **same function** we **used in** the **linear search example, but** using a **binary search instead**. Remember that in this case, there is a **required assumption** that the **list** is **sorted**.

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


# #### Test for integers
# Let's try our **binary search for integers** with the **same *int_list*** we had **used for the linear search**. In fact we'll copy paste the same test code, anf just update the function call.

# In[ ]:


# Test with item present in the list
val = 4
idx = binary_search_loop(int_list, val)
if (idx != -1):
    print(f"Index of {val} is {idx}")
else:
    print(f"{val} was not found")

# Test with item NOT present in the list
val = 20
idx = binary_search_loop(int_list, val)
if (idx != -1):
    print(f"Index of {val} is {idx}")
else:
    print(f"{val} was not found")


# Hum ... that doesn't seem right. **4 is in my list! Why didn't my fancy binary search find it?!**

# In[ ]:


# print int_list
print(int_list)


# Ahh ... I forgot! **Binary search requires** that the **list must be sorted**. Let's **try** that **again with** a **sorted list**.

# In[ ]:


sorted_int_list = sorted(int_list)
print(sorted_int_list)


# In[ ]:


# Test with item present in the list
val = 4
idx = binary_search_loop(sorted_int_list, val)
if (idx != -1):
    print(f"Index of {val} is {idx}")
else:
    print(f"{val} was not found")

# Test with item NOT present in the list
val = 20
idx = binary_search_loop(sorted_int_list, val)
if (idx != -1):
    print(f"Index of {val} is {idx}")
else:
    print(f"{val} was not found")


# Now **that's more likely!**

# ### Time and space complexity
# - **Time complexity: <span style="color:blue">O(log n)**</span>
# - **Space complexity: <span style="color:blue">O(1)**</span>

# ## Binary Search using recursion
# The **binary search algorithm with recursion** follows the **same principle as** the **one with the loop**. It's **just** a **different way to implement** the same thing.
# 
# Once again, let's implement the **same search function** we **used in** the previous examples.

# In[ ]:


def _binary_search_recursive(items, search_value, start, end):
    '''
    This method will search for an item in a list of ascending order.
    It will retur the index of the item if found, or -1 if not found.
    '''

    # If we "cross over", and the end is smaller, it means we dind't find the item
    if start > end:
        return -1

    # split the search space in the middle
    middle = (start + end) // 2

    # if the search value is equal to the middle value, then we found it, so return the index
    if search_value == items[middle]:
        return middle
        
    # else, if the search value is less than the middle value, recursively search the lower half
    elif search_value < items[middle]:
        return _binary_search_recursive(items, search_value, start, middle - 1)
        
    # else, the search value is greater than the middle value, recursively search the upper half
    else:
        return _binary_search_recursive(items, search_value, middle + 1, end)

def binary_search_recursive(items, search_value):
    '''
    Invokes the recursive function implementing the binary search, passing the initial start end end values
    '''
    return _binary_search_recursive(items, search_value, 0, len(items) - 1)


# #### Test for strings
# Let's try our **binary search for strings** with the **same *str_list*** we had **used for the linear search**. But this time we'll **remember to sort the list.**

# In[ ]:


sorted_str_list = sorted(str_list)
print(sorted_str_list)


# In[ ]:


# Test with item present in the list
val = "Luke"
idx = binary_search_recursive(sorted_str_list, val)
if (idx != -1):
    print(f"Index of {val} is {idx}")
else:
    print(f"{val} was not found")
    
# Test with item NOT present in the list
val = "Scooby Doo"
idx = binary_search_recursive(sorted_str_list, val)
if (idx != -1):
    print(f"Index of {val} is {idx}")
else:
    print(f"{val} was not found")


# ### Time and space complexity
# - **Time complexity: <span style="color:blue">O(log n)**</span>
# - **Space complexity: <span style="color:blue">O(log n)**</span>
# 
# Do you **see a difference?** The **time complexity** is the **same**, **but** the **space complexity changed from O(1) to O(log n)**. That's because **recursion** will require **extra memory**.

# ### Simple example: number guessing game
# **Binary Search** is so effective, that the **log n performance** feels **practically like magic**. Many many ... many years ago, **when** I **first learned of "binary search"**, I **wrote** my first **"computer game"** to impress friends and relatives: **fguess** (clearly I wasn't a marketing genious at that young age)

# #### Audience picks a number between 1 - 500, or I'll let the computer pick

# In[ ]:


# if nobody in the audience wants to pick, generate a random integer between 1 and 500
import random
secret_number = random.randint(1, 500)
print(f"Computer picked {secret_number}. Shhh .... don't tell anyone")


# #### Define the amazing ***fguess*** game

# In[ ]:


# define constant for maximum number
MAX_NUMBER = 500

def fguess():
    '''
    This function will ask the player to pick a number, and then it will use a binary search to 
    repeatedly narrow down the options, and eventually guess the number.
    '''

    # Explain the game, and wait for user to press enter to start
    print(f"Think of a number between 1 and {MAX_NUMBER}, and don't tell me. I'll guess it!\n")
    input("Press Enter to start ... ")

    # write some fun and exciting sentences
    print("\n\nOk, let's go!")
    print("I'm looking inside your brain ... and reading your mind ... \n")

    # initialize the start and end of our loop, which will be updated as the search progresses
    start = 1
    end = MAX_NUMBER

    # count the number of tries
    tries = 1
    
    # continue the loop as long as start is <= to end. If we "cross over", and the end is smaller
    # it will mean that we never found the item
    while start <= end:
        # split the search space in the middle
        middle = (start + end) // 2
        
        # ask the user if the number is equal, higher, or lower
        answer = input(f"\nHow about ... {middle}?\nAnswer Yes (y), Higher(h) or Lower(l)").lower()

        # if the answer is "y", we found the number, so return
        if (answer == "y"):
            print(f"\nAh ha! I thought so! I only needed {tries} tries to guess it!\nThanks for playing.\nGoodbye now.")
            return
        # if the answer is "l", the number is lower
        elif (answer == "l") : 
            # print fun message, then update the search space to the lower half
            print("I had a feeling that was the case! I feel I'm getting closer")
            end = middle - 1
        # else, the number must be higher
        else:
            # print fun message, then update the search space to the higher half
            print("I know I'n getting hotter! You can run but you can't hide")
            start = middle + 1

        # increment the number of tries
        tries += 1
        
    # if we get here, and we never guessed it, something went wrong
    print("\nHum ... I smell a rat!\nWere you paying attention?")
    print("I think you answered something wrong.\nPlease try again.")


# #### Play the game!

# In[ ]:


# call fguess function to play the game
fguess()


# Obviously that are a lot more practical examples than a simple game. **Binary search** is **widely used** to **search** for **items in a collection**. The only thing to **remember**, is that the **list must be maintained in order**.

# ### <span style="color:blue">Optional:</span> Test with custom types
# Similar to what we did in the linear search, **if** we **want** to **perform** a **binary search with** my **own class** objects, I just need to make sure items can be compared for greater than and/or less than (depedning on which one I used in my function). For a custom class, that means the **class** needs to **overload the operators for <, <=, >, and >=**. So let's **update** the **previous Pet class** to **add these operators**. And let's not forget, my list will need to be sorted.

# #### Define my own class

# In[ ]:


class Pet:
    '''
    This class stores information about a house pet.
    '''
    def __init__(self, name, species, breed):
        self.name = name
        self.species = species
        self.breed = breed

    def __eq__(self, other):
        '''
        This method overrides the equality operator.
        '''
        return (self.name == other.name and 
                self.species == other.species and
                self.breed == other.breed)

    def __lt__(self, other):
        '''
        This method overrides the < operator. The method will compare by name, then breed, then species
        '''

        # compare by name first
        if self.name < other.name:
            return True
        elif self.name > other.name:
            return False
        # name is equal, so compare by breed
        else:
            if self.breed < other.breed:
                return True
            elif self.breed > other.breed:
                return False
            # bread is equal, so compare by species
            else:
                if self.species < other.species:
                    return True
                else:
                    return False

    def __le__(self, other):
        '''
        This method overrides the <= operator. The method will compare by name, then breed, then species
        '''

        # compare by name first
        if self.name < other.name:
            return True
        elif self.name > other.name:
            return False
        # name is equal, so compare by breed
        else:
            if self.breed < other.breed:
                return True
            elif self.breed > other.breed:
                return False
            # bread is equal, so compare by species
            else:
                if self.species > other.species:
                    return False
                else:
                    return True

    def __gt__(self, other):
        '''
        This method overrides the > operator. The method will compare by name, then breed, then species
        '''

        # compare by name first
        if self.name > other.name:
            return True
        elif self.name < other.name:
            return False
        # name is equal, so compare by breed
        else:
            if self.breed > other.breed:
                return True
            elif self.breed < other.breed:
                return False
            # bread is equal, so compare by species
            else:
                if self.species > other.species:
                    return True
                else:
                    return False

    def __ge__(self, other):
        '''
        This method overrides the >= operator. The method will compare by name, then breed, then species
        '''

        # compare by name first
        if self.name > other.name:
            return True
        elif self.name < other.name:
            return False
        # name is equal, so compare by breed
        else:
            if self.breed > other.breed:
                return True
            elif self.breed < other.breed:
                return False
            # bread is equal, so compare by species
            else:
                if self.species < other.species:
                    return False
                else:
                    return True

    def __repr__(self):
        return f"({self.name},{self.species},{self.breed})"
    
    def __str__(self):
        return f"{self.name} - {self.species} - {self.breed}"


# #### Bonus! I can now use the standarded Python sorted function with my custom class
# **Because** we have **defined** the **comparison operators**, I will be **able to use** the standard **Python *sorted* function**. I won't bother showing, but you can test that if you do not have those operators, *sorted* will return an error. 
# 
# I'll have the recreate my original list of Pets, because the previous one was created using the Pet class that didn't have these new operators defined yet.

# In[ ]:


# re-create my original list of Pet objects, using the updated Pet class
pet_list = [Pet("Rebecca", "Dog", "Golden Retriever"),
            Pet("Tracy", "Dog", "Golden Retriever"),
            Pet("Sammy", "Dog", "Labrador Retriever"),
            Pet("Luke", "Dog", "Labrador Retriever"),
            Pet("Max", "Dog", "Cavalier King Charles Spaniel"),
            Pet("Tucker", "Dog", "Golden Retriever"),
            Pet("Moose", "Dog", "German Spitz"),
            Pet("Miley", "Cat", "American Shorthair"),
            Pet("Mittenz", "Cat", "Calico"),
            Pet("Lexi", "Cat", "Munchkin"),
            Pet("Finn", "Cat", "Munchkin"),
            Pet("Indy", "Ferret", "Sable"),
            Pet("Deedee", "Ferret", "Sable"),
            Pet("Ruby", "Ferret", "Sable"),
            Pet("Bullet", "Tortoise", "Greek"),
            Pet("Buttercup Baby", "Guinea Pig", "American"),
            Pet("Mickey", "Hamster", "Syrian"),
            Pet("Bluey", "Parakeet", "Budgerigar"),
            Pet("Greeney", "Parakeet", "Budgerigar")
           ]

# sort the list of Pet objects
sorted_pet_list = sorted(pet_list)
print(sorted_pet_list)


# #### Test with both the iterative and the recursive versions

# In[ ]:


# Test with item present in the list on iterative version
print("Testing the iterative version ...")
val = Pet("Tucker", "Dog", "Golden Retriever")
idx = binary_search_loop(sorted_pet_list, val)
if (idx != -1):
    print(f"Index of {val.name} is {idx}")
else:
    print(f"{val.name} was not found")
    
# Test with item NOT present in the list on iterative version
val = Pet("Otto", "Dog", "Doberman")
idx = binary_search_loop(sorted_pet_list, val)
if (idx != -1):
    print(f"Index of {val.name} is {idx}")
else:
    print(f"{val.name} was not found")

# Test with item present in the list on recursive version
print("\nTesting the recursive version ...")
val = Pet("Indy", "Ferret", "Sable")
idx = binary_search_recursive(sorted_pet_list, val)
if (idx != -1):
    print(f"Index of {val.name} is {idx}")
else:
    print(f"{val.name} was not found")
    
# Test with item NOT present in the list on recursive version
val = Pet("Giles Villeneuve", "Dog", "German Shephard")
idx = binary_search_recursive(sorted_pet_list, val)
if (idx != -1):
    print(f"Index of {val.name} is {idx}")
else:
    print(f"{val.name} was not found")


# # Comparing Linear Search and Binary Search Performance
# This is going to be very similar to what we did when we compared Binary Search Trees against a regular Python list. The **key point** here is to **highlight** the **difference between** an **O(n) search, vs and Order (log n) search**.

# ##### Import modules
# We'll be using a couple of modules in the upcoming analysis, so we'll import them here

# In[ ]:


import time
import random


# #### Loading data for my search
# To **test** my **searches** I **need** to have a **lot of keys**. The binary search requires an orderdered list, so I'll use integers in order, but I'll covert them to strings, and left-pad with zeros (so they are sorted alphabetically properly).

# In[ ]:


# Use a variable to control the number of keys I generate, because we may want to change that to do different tests.
NUMBER_OF_KEYS = 10000


# In[ ]:


# initialize and empty key list
key_list = []

# iterate through the required number of keys
for num_key in range(NUMBER_OF_KEYS):
    # I want my keys to have 10 characters, so I'll convert the number to a string, and left pad it with zero up to 10 characters
    str_key = str(num_key).zfill(10)
    # append the key to my list
    key_list.append(str_key)

# print the first 5 and last 5 items so we can confirm it looks right
print(f"Sample keys: {key_list[0:5]} ... {key_list[-5:]}")


# #### Testing the performance of linear and binary searches
# Let's **search** the **same elements** in the list **using both linear and binary search**, and **test the performance**. **We'll use** the **iterative version** of the binary search, which should be the **same as the recursive from a performance standpoint**. We'll use the same Python time module we have used in previous examples to measure the execution time.

# In[ ]:


# generate some random keys from our list to searcho for
random_keys = []
for x in range(10):
    random_keys.append(key_list[random.randint(0, len(key_list) - 1)])

print(f"------------------ Searching through {len(key_list):,d} elements ------------------")

print("\nLinear Search:\n--------------")

# initialize total linear search time
total_linear_search_time = 0
                     
# iterate through search words
for search_key in random_keys:  
    # start timer
    start_time = time.perf_counter()

    # perform linear search
    idx = linear_search(key_list, search_key)

    # stop timer
    end_time = time.perf_counter()
    
    # print result
    print(f"Search for {search_key} completed in {(end_time - start_time):.6f} seconds")
    
    # accumulate the search times so we can average in the end
    total_linear_search_time += (end_time - start_time)

# calculate final average across all searches
avg_linear_search_time = total_linear_search_time / len(random_keys)
print(f"\nAverage linear search time: {avg_linear_search_time:.6f} seconds")

print("\n\nBinary Search:\n--------------")

# initialize total linear search time
total_binary_search_time = 0
                     
# iterate through search words
for search_key in random_keys:  
    # start timer
    start_time = time.perf_counter()

    # perform linear search
    idx = binary_search_loop(key_list, search_key)

    # stop timer
    end_time = time.perf_counter()
    
    # print result
    print(f"Search for {search_key} completed in {(end_time - start_time):.6f} seconds")
    
    # accumulate the search times so we can average in the end
    total_binary_search_time += (end_time - start_time)

# calculate final average across all searches
avg_binary_search_time = total_binary_search_time / len(random_keys)
print(f"\nAverage binary search time: {avg_binary_search_time:.6f} seconds")

# compare the two average values
perf_factor = int(avg_linear_search_time / avg_binary_search_time)
print(f"\nFor {len(key_list)} items, the binary search is about {perf_factor} times faster than the linear search")


# #### Turbo charging that comparison ...
# Now that we get the idea of how I'm testinh this, let's **do it for many different list sizes**. **To simplify** the output, I'll **only print the average** (so no individual results), but you can varify I'll be doing the same calls.
# 
# 

# ##### Define the list sizes I want to test

# In[ ]:


list_sizes = [1000, 10000, 100000, 1000000, 10000000]


# ##### Iterate to create lists for each test size, and compare average performance for them

# In[ ]:


# iterate through all requested list sizes
for list_size in list_sizes:
    
    # create a key list of the requested size
    key_list = []
    for num_key in range(list_size):
        str_key = str(num_key).zfill(10)
        key_list.append(str_key)

    # generate some random keys from our list to search for
    random_keys = []
    for x in range(10):
        random_keys.append(key_list[random.randint(0, len(key_list) - 1)])

    print(f"\n------------------ Searching through {len(key_list):,d} elements ------------------")
    
    # perform the linear search and time it
    total_linear_search_time = 0
    for search_key in random_keys:
        start_time = time.perf_counter()
        idx = linear_search(key_list, search_key)
        end_time = time.perf_counter()
        total_linear_search_time += (end_time - start_time)
        
    # calculate the average linear search time
    avg_linear_search_time = total_linear_search_time / len(random_keys)

    
    # perform the binary search and time it
    total_binary_search_time = 0
    for search_key in random_keys:
        start_time = time.perf_counter()
        idx = binary_search_loop(key_list, search_key)
        end_time = time.perf_counter()
        total_binary_search_time += (end_time - start_time)
        
    # calculate the average binary search time
    avg_binary_search_time = total_binary_search_time / len(random_keys)

    # calculate the performance improvement
    perf_factor = int(avg_linear_search_time / avg_binary_search_time)

    # print the results
    print(f"Average linear search time: {avg_linear_search_time:.6f} seconds")
    print(f"Average binary search time: {avg_binary_search_time:.6f} seconds")
    print(f"Binary search is about {perf_factor} times faster than the linear search")


# ##### Why is it faster?
# 
# At the risk of sounding like a broken record ...
# - The **regular list** has **O(n) time complexity**, because it will have through **walk through the whole list** to locate the one you want.
# - The **Binary Search** has **O(log n) time complexity**, because it **splits** the **search space in half each time** you progress down the tree.

# # <span style="color:blue">Optional:</span> Jump Search
# There are a **lot of other search algorithms out there**, with **various** different **time complexity values**. **Many** of them **follow** the similar **"dive and conquer" approach** of binary search, where the **search space** is **reduced each time**. Just to change things up, I figured I'd **cover one** that **uses** a **different approach: Jump Search.**
# 
# 

# ### Jump Search Algorithm
# The Jump Search Algorithm reduces the number of steps by "jumping ahead". It requires a sorted list, and follows these steps:
# - Select a jump step, or "block size". That's usually the square root of the list size. So for instance, for a list of 16 items, the block size would be 4.
# - Instead of searching each item, skip ahead each time by the block size
# - After each skip, compare again the current item
#     - If the current item is greater than the search value, then back track to the previous
#     - Otherwise jump forward again
# - After backtracking, perform a linear search forward until the search value is found

# ### Jump Search Implementation

# In[ ]:


import math

def jump_search(list, search_value):
    '''
    Implements the jump search algorithm
    '''

    # define the block step as the square root of the list size, and initialize starting step and last step
    block_size = int(math.sqrt(len(list)))
    step = block_size
    last_step = 0

    # Loop skipping ahead by the block size, until we've gone past the search value or past the end of the list
    while list[min(step, len(list) - 1)] < search_value:
        # remember the previews step, then advance step by the block size
        last_step = step
        step += block_size

        # if we when past the end of the list, the item is not found
        if last_step > len(list):
            return -1

    # at this point, we should be at the beginning of the block that has the value (if the value is there)
    # so perform linear search within the block.
    end_block = min(step, len(list))
    for i in range(last_step, end_block):
        # check for the item
        if list[i] == search_value:
            return i
    
    # if we got to the end of the block and did not exit the loop, the item is not in the list
    return -1


# ### Time and space complexity
# - **Time complexity: <span style="color:blue">O(sqrt(n))**</span>
# - **Space complexity: <span style="color:blue">O(1)**</span>

# ### Quick test with integers
# We'll do the same test with did for the lenear and binary search

# In[ ]:


int_list = [ 0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ]


# In[ ]:


# Test with item present in the list
val = 34
idx = jump_search(int_list, val)
if (idx != -1):
    print(f"Index of {val} is {idx}")
else:
    print(f"{val} was not found")

# Test with item NOT present in the list
val = 20
idx = jump_search(int_list, val)
if (idx != -1):
    print(f"Index of {val} is {idx}")
else:
    print(f"{val} was not found")


# ## The final showdown ...
# **Let's compare all three searches now!**
# We'll use exactly the **same comparison code** we did before.

# ##### Define the list sizes I want to test

# In[ ]:


list_sizes = [1000, 10000, 100000, 1000000, 10000000]


# ##### Iterate to create lists for each test size, and compare average performance for them

# In[ ]:


# iterate through all requested list sizes
for list_size in list_sizes:
    
    # create a key list of the requested size
    key_list = []
    for num_key in range(list_size):
        str_key = str(num_key).zfill(10)
        key_list.append(str_key)

    # generate some random keys from our list to search for
    random_keys = []
    for x in range(10):
        random_keys.append(key_list[random.randint(0, len(key_list) - 1)])

    print(f"\n------------------ Searching through {len(key_list):,d} elements ------------------")
    
    # perform the linear search and time it
    total_linear_search_time = 0
    for search_key in random_keys:
        start_time = time.perf_counter()
        idx = linear_search(key_list, search_key)
        end_time = time.perf_counter()
        total_linear_search_time += (end_time - start_time)
        
    # calculate the average linear search time
    avg_linear_search_time = total_linear_search_time / len(random_keys)

    
    # perform the binary search and time it
    total_binary_search_time = 0
    for search_key in random_keys:
        start_time = time.perf_counter()
        idx = binary_search_loop(key_list, search_key)
        end_time = time.perf_counter()
        total_binary_search_time += (end_time - start_time)
        
    # calculate the average binary search time
    avg_binary_search_time = total_binary_search_time / len(random_keys)

    # perform the jump search and time it
    total_jump_search_time = 0
    for search_key in random_keys:
        start_time = time.perf_counter()
        idx = jump_search(key_list, search_key)
        end_time = time.perf_counter()
        total_jump_search_time += (end_time - start_time)
        
    # calculate the average binary search time
    avg_jump_search_time = total_jump_search_time / len(random_keys)
    
    # calculate the performance improvement2
    perf_factor1 = int(avg_linear_search_time / avg_jump_search_time)
    perf_factor2 = int(avg_linear_search_time / avg_binary_search_time)

    # print the results
    print(f"Average linear search time: {avg_linear_search_time:.6f} seconds")
    print(f"Average jump search time: {avg_jump_search_time:.6f} seconds")
    print(f"Average binary search time: {avg_binary_search_time:.6f} seconds")
    print(f"Jump search is about {perf_factor1} times faster than the linear search")
    print(f"Binary search is about {perf_factor2} times faster than the linear search")


# In[ ]:




