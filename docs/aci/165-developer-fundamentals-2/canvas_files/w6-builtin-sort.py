#!/usr/bin/env python
# coding: utf-8

# # <span style="color:blue">Built-in Python sorting
# AWS CLOUD INSTITUTE: PROVIDED FOR EDUCATIONAL INSTRUCTIONAL PURPOSES ONLY.

# # Built-in sort algorithms
# There are **two built-in algorithms** for sorting **in Python**. These algorithms are **sort() and sorted()**. We'll look at each in turn, and then contrast them.

# ## The *sort()* list method

# The **[sort() method ](https://docs.python.org/3/library/stdtypes.html#list.sort)** is a **built-in method for lists in Python** and is **used to sort** the **elements of a list**. Key characteristics:
# - Does **in-place sorting** (updates old list)
# - **Only works on lists**, **but** will work on lists of **any data type that supports** the **"<"** comparison.
# - Sorts in **ascending order by default**
# - **Returns *None***, because it updates the list in place

# ### Sorting int lists

# In[ ]:


int_list = [23, 11, 4, 9, 21, 34, 16, 8, 29, 12]


# In[ ]:


# sort the list
int_list.sort()

# print updated lists
print(int_list)


# #### Did that change the original list?
# Well, the answer is **obviously yes**, given that **I printed the original list**. **And it is sorted.**

# ### Sorting string lists

# In[ ]:


# create a list of strings with some of my dogs and cats
str_list = ["Rebecca", "Tracy", "Sammy", "Luke", "Max", "Tucker", "Moose", "Miley", "Mittenz",  "Lexi", "Finn"]


# In[ ]:


# sort the list
str_list.sort()

# print updated lists
print(str_list)


# ### Sorting lists of a custom class
# The list ***sort()*** method will work on lists of **any data type that supports** the **"<"** comparison. For custom classes, that means we **need to define the \_\_lt\_\_() operator.**

# #### Define a Pet class, with a \_\_lt\_\_() operator

# In[ ]:


class Pet:
    '''
    This class stores information about a house pet.
    '''
    def __init__(self, name, species, breed, weight):
        self.name = name
        self.species = species
        self.breed = breed
        self.weight = weight

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

    def __repr__(self):
        return f"({self.name},{self.species},{self.breed},{self.weight} lbs)"
    
    def __str__(self):
        return f"{self.name} - {self.species} - {self.breed} - {self.weight} lbs"


# #### Create Pet objects for some of my pets

# In[ ]:


pet_list = [Pet("Rebecca", "Dog", "Golden Retriever", 77.4),
            Pet("Tracy", "Dog", "Golden Retriever", 81.2),
            Pet("Sammy", "Dog", "Labrador Retriever", 71.6),
            Pet("Luke", "Dog", "Labrador Retriever", 94.0),
            Pet("Max", "Dog", "Cavalier King Charles Spaniel", 14.2),
            Pet("Tucker", "Dog", "Golden Retriever", 90.2),
            Pet("Moose", "Dog", "German Spitz", 24.5),
            Pet("Miley", "Cat", "American Shorthair", 9.0),
            Pet("Mittenz", "Cat", "Calico", 12.6),
            Pet("Lexi", "Cat", "Munchkin", 10.2),
            Pet("Finn", "Cat", "Munchkin", 11.4),
            Pet("Greeney", "Parakeet", "Budgerigar", 0.06),
            Pet("Indy", "Ferret", "Sable", 3.1),
            Pet("Deedee", "Ferret", "Sable", 2.8),
            Pet("Ruby", "Ferret", "Sable", 2.7),
            Pet("Mickey", "Hamster", "Syrian", 0.28),
            Pet("Bullet", "Tortoise", "Greek", 1.5),
            Pet("Tiger", "Guinea Pig", "American", 2.1)
           ]

for pet in pet_list:
    print(pet)


# #### Sort list of Pets

# In[ ]:


pet_list.sort()
for pet in pet_list:
    print(pet)


# ### Sorting in reverse order
# As we saw, by default, the sort is in ascending order. We can **sort in descending order** by **adding** the ***reverse=True* parameter**.

# In[ ]:


int_list = [23, 11, 4, 9, 21, 34, 16, 8, 29, 12]


# In[ ]:


# sort the list
int_list.sort(reverse=True)

# print updated lists
print(int_list)


# ### Sorting based on a custom criteria
# As we discussed, **by default** the **sort** method will **use** the **standard "<" comparison** for the data type **to decide how to order** elements. However, **if** we have a **specialized need**, we can **provide** a **custom function to return** a **different value *sort()* should use** in the comparison. This function is **passed in the *key* parameter**.

# #### Define a special function to sort pets by weight
# Let's say that for a special situation, we may want to **sort pets by weight**. This could be useful for transport purposes for instance.

# In[ ]:


# define function to return the weight of a Pet object
def get_pet_weight(pet):
    return pet.weight


# In[ ]:


# example
print(f"Weight of {pet_list[0].name}:", get_pet_weight(pet_list[0]))


# ### Sort pet list based on the weight

# In[ ]:


# sort pets by weight
pet_list.sort(key = get_pet_weight)
for pet in pet_list:
    print(pet)


# ## The *sorted()* function

# The **sorted() function** is a **built-in function in Python** and is **used to sort** the **elements of multiple types of iterables (list, tuples or strings)** . Key characteristics:
# - **Returns a new list**, so it does not update the original one.
# - **Works with any iterable data type**, such as lists, tuples, sets, stings, dictionaries, and others.
#     - It will **take** an **iterable** as an **input**, **but always returns** a **list** as the output 
# - Sorts in **ascending order by default**

# ### Sorting int lists

# In[ ]:


original_list = [23, 11, 4, 9, 21, 34, 16, 8, 29, 12]


# #### Sort the list

# In[ ]:


sorted_list = sorted(original_list)


# #### Note the original list has not changed

# In[ ]:


print(f"Original list: {original_list}")
print(f"Sorted   list: {sorted_list}")


# ### Sorting lists of other types
# We can **sort** the **same lists** we did earlier **using** the ***sort() method***, **by using** the ***sorted()*** function. The key difference there is that we would not be modifying the lists in place. Let's repeat the same examples.

# #### Sorting string lists

# In[ ]:


# create a list of strings with some of my dogs and cats
original_list = ["Rebecca", "Tracy", "Sammy", "Luke", "Max", "Tucker", "Moose", "Miley", "Mittenz",  "Lexi", "Finn"]

# sort the list
sorted_list = sorted(original_list)

# print both new and unmodified original
print(f"Original list: {original_list}")
print(f"Sorted   list: {sorted_list}")


# #### Sorting lists of custom classes
# Just like we saw with the list *sort()* method, I **can use the ***sorted()*** function** with any data type that supports a **"<" comparison**. So we **can sort** our **Pet class**, which **had a *\_\_lt()\_\_* method** defined.

# In[ ]:


# Create a list of Pet objects for some of my pets
original_list = [Pet("Rebecca", "Dog", "Golden Retriever", 77.4),
                 Pet("Tracy", "Dog", "Golden Retriever", 81.2),
                 Pet("Sammy", "Dog", "Labrador Retriever", 71.6),
                 Pet("Luke", "Dog", "Labrador Retriever", 94.0),
                 Pet("Max", "Dog", "Cavalier King Charles Spaniel", 14.2),
                 Pet("Tucker", "Dog", "Golden Retriever", 90.2),
                 Pet("Moose", "Dog", "German Spitz", 24.5),
                 Pet("Miley", "Cat", "American Shorthair", 9.0),
                 Pet("Mittenz", "Cat", "Calico", 12.6),
                 Pet("Lexi", "Cat", "Munchkin", 10.2),
                 Pet("Finn", "Cat", "Munchkin", 11.4),
                 Pet("Greeney", "Parakeet", "Budgerigar", 0.06),
                 Pet("Indy", "Ferret", "Sable", 3.1),
                 Pet("Deedee", "Ferret", "Sable", 2.8),
                 Pet("Ruby", "Ferret", "Sable", 2.7),
                 Pet("Mickey", "Hamster", "Syrian", 0.28),
                 Pet("Bullet", "Tortoise", "Greek", 1.5),
                 Pet("Tiger", "Guinea Pig", "American", 2.1)
                ]
# sort the list
sorted_list = sorted(original_list)

# print both new and unmodified original
print(f"Original list: {original_list}")
print(f"\nSorted   list: {sorted_list}")


# ### Sorting in reverse order
# The ***sorted()*** function also supports the the ***reverse=True* parameter** for a reveresed search.

# In[ ]:


# create a list of strings with some of my dogs and cats
original_list = [23, 11, 4, 9, 21, 34, 16, 8, 29, 12]

# sort the list
sorted_list = sorted(original_list, reverse=True)

# print both new and unmodified original
print(f"Original list: {original_list}")
print(f"Sorted   list: {sorted_list}")


# ### Sorting other iterables
# The **sorted()** function **works with any iterable data type**, such as **lists, tuples, sets, stings, dictionaries, and others**.
# It will take an iterable as an input, but <span style="color:red"> **always returns a list as the output.**</span>

# #### Sorting tuples

# In[ ]:


# create a tuple with some names
original_tuble = ("John Stiles", "Diego Ramirez", "Mary Major", "Ana Silva", "Soo-jin Ki", "Alejandro Rosale")

# sort the list
sorted_list = sorted(original_tuble)

# print original string, a sorted list
print(f"Original tuple: {original_tuble}")
print(f"Sorted    list: {sorted_list}")


# #### Sorting a string
# Sorting a string with *sorted()* will **iterate through** all the **characters in the string**, and **sort them** in order.

# In[ ]:


# create a string with random characters
original_string = "iahbkcdgefj"

# sort the list
sorted_list = sorted(original_string)

# print original string, a sorted list
print(f"Original string: {original_string}")
print(f"Sorted     list: {sorted_list}")


# But **what if** I **didn't want** a **list of the characters?** What if I **wanted a string back**, **with** the **ordered characters**?
# 
# Well, I just need to **use my "Python powers"** to **build** a **string back up** from the sorted list.

# In[ ]:


sorted_string = ""
for char in sorted_list:
    sorted_string += char

print(f"Original string: {original_string}")
print(f"Sorted     list: {sorted_list}")
print(f"Sorted   string: {sorted_string}")


# #### Sorting a dictionary
# Sorting a dictionary with *sorted()* by default will return a sorted list of the dictionary keys

# In[ ]:


# create a dictionary for names with ages
original_dict = {
    "John Stiles": 45,
    "Diego Ramirez": 32,
    "Mary Major": 28,
    "Ana Silva": 35,
    "Soo-jin Ki": 22,
    "Alejandro Rosale": 39
}

# sort the list
sorted_list = sorted(original_dict)

# print original string, a sorted list
print(f"Original dict: {original_dict}")
print(f"Sorted   list: {sorted_list}")


# ### Custom sorting criteria
# Like the *sort()* method, the ***sorted()*** function **allows you** to **provide** a **custom function to return** a **different value to use** in the comparison. This function is **passed in the *key* parameter**.

# #### Sorting a list of strings by their length
# To sort a list of strings by their length, I can **use a function** that **returns the string length**. Fortunately, **Python already** has the ***len*** function I can use for that.

# In[ ]:


# create a list of strings with some of my dogs and cats
original_list = ["Rebecca", "Tracy", "Sammy", "Luke", "Max", "Tucker", "Moose", "Miley", "Mittenz",  "Lexi", "Finn"]

# sort the list, using the len function as the key
sorted_list = sorted(original_list, key=len)

# print both new and unmodified original
print(f"Original list: {original_list}")
print(f"Sorted   list: {sorted_list}")


# ### <span style="color:blue">OPTIONAL:</span> Using a custom sort for a dictionary search
# In the previous dictionary example, the we simply get a list of sorted keys. What if we want to **sort by age**?

# #### Sort by the dictionary items
# First we try sorting with the dictionary items, not just the key. We **use the Dictionary items() method** to give me a **list of complete items**.

# In[ ]:


# create a dictionary for names with ages
original_dict = {
    "John Stiles": 45,
    "Diego Ramirez": 32,
    "Mary Major": 28,
    "Ana Silva": 35,
    "Soo-jin Ki": 22,
    "Alejandro Rosale": 39
}

# sort the list
sorted_list = sorted(original_dict.items())

# print original string, a sorted list
print(f"Original string: {original_dict}")
print(f"Sorted     list: {sorted_list}")


# Using ***items()*** got us the full item as a tuple, but the **tuples** are still **ordered by** the **first element**. To get around that, we'll use a custom function.

# #### Use lambda function to return second item in the tuple
# We could define a function the usual way (with the ***def*** statement), but **for something** as **simple as this**, we can **use a lambda function**. A **Python lambda function** is one you can **create "on the fly", without a name**, and **returning** a **value with a single expression**.

# In[ ]:


# create a dictionary for names with ages
original_dict = {
    "John Stiles": 45,
    "Diego Ramirez": 32,
    "Mary Major": 28,
    "Ana Silva": 35,
    "Soo-jin Ki": 22,
    "Alejandro Rosale": 39
}

# sort the list, with a lambda function that will return the second element in a tuple
sorted_list = sorted(original_dict.items(),
                    key=lambda item: item[1])

# print original string, a sorted list
print(f"Original string: {original_dict}")
print(f"Sorted     list: {sorted_list}")


# ## <span style="color:blue">OPTIONAL:</span> Comparing *sort()* and *sorted()* performance
# There is general understanding that the list *sort()* has sligtly better performance than using the *sorted()* function. Let's confirm that with a performance test. We will use some of the same mechanisms previously employed to generate random values, and time the operations.

# ##### Import modules
# We'll be using a couple of modules in the upcoming analysis, so we'll import them here

# In[ ]:


import time
import random


# #### Creating a list with random strings
# To **test** the functions, I want to have a lot of strings. I'll use **use** the **python random module** to **generate** a **large set of random numbers**, and convert them to strings.

# In[ ]:


# Use a variable to control the number of keys I generate, because we may want to change that to do different tests.
NUMBER_OF_KEYS = 1000000


# In[ ]:


# intially use a set, to guarantee no duplicates
str_set = set({})
while len(str_set) < NUMBER_OF_KEYS:
    # generate a very large random integer, convert it to a string, and add to set
    str_set.add(str(random.randint(0, 1000000000)))

# convert the set to a list
str_list = list(str_set)

# verify the size
print(f"Generated {len(str_list)} unique keys.")

# print the first 5 items so we can confirm the types of strings being inserted
print(f"Sample keys: {str_list[0:5]}")


# #### Comparing the performance of *sort()* and *sorted()*
# We'll use the same Python time module we have used in previous examples to measure the execution time.

# In[ ]:


print(f"\n------------------ Sorting {len(str_list):,d} elements ------------------")

# start timer
start_time = time.perf_counter()

# use sorted function to sort list
sorted_list = sorted(str_list)

# stop timer and calculate elapsed time
end_time = time.perf_counter()
sorted_function_time = end_time - start_time

# print sorted function time
print(f"\nTime using sorted() function: {sorted_function_time:.6f} seconds")
                     
# start timer
start_time = time.perf_counter()

# use sort function to sort list
str_list.sort()

# stop timer and calculate elapsed time
end_time = time.perf_counter()
sort_method_time = end_time - start_time

# print sorted function time
print(f"Time using sort() method: {sort_method_time:.6f} seconds")

# calculate the performance improvement
perf_factor = sorted_function_time / sort_method_time
print(f"The sort() method was {perf_factor:.2f} times faster than the sorted() function.")


# It **wasn't** a **huge difference** when I ran (between 1.1 and 1.5 times faster), **but all things being the same**, we should always **use the most efficient option** available.
