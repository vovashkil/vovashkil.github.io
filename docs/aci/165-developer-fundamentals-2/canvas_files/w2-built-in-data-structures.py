#!/usr/bin/env python
# coding: utf-8

# # <span style="color:blue">Python Built-in Data Structures
# AWS CLOUD INSTITUTE: PROVIDED FOR EDUCATIONAL INSTRUCTIONAL PURPOSES ONLY.

# # Lists
# Lists are a **versatile ordered collections of objects** with the following key chracteristics:
# - They are **mutable** in that they can be changed after creation. For example, lists can start empty but can grow and shrink later.
# - They are **ordered** and **indexed in sequence starting with zero**
# - They support **fast access by index**.
# - Lists can consist of **mixed-value types**.
# - Lists **can include duplicate values**.
# - Lists are **created using brackets \[\]**
# 
# We'll **cover** some of the **basic operations here**. **For** a **full definition** of the list class, you can **refer to** the **[official list class documentation](https://docs.python.org/3/tutorial/datastructures.html).**

# ## Creating a list

# In[ ]:


# Creating a list of string
pets = ["Tucker", "Moose", "Finn"]
print(pets)


# In[ ]:


# Creating a list of integerrs
brazil_wc = [1958, 1962, 1970, 1994]
print(brazil_wc)


# In[ ]:


# Creating a list of floats
we_all_float_here = [3.1416, 0.3, 1.75, 5.674]
print(we_all_float_here)


# In[ ]:


# creating a list of mixed integers and strings
superbowls_90 = [1990, "San Francisco", 1991, "New York Giants", 1992, "Washington", 1993, "Dallas Cowboys", 1994, "Dallas Cowboys",
                 1995, "San Francisco", 1996, "Dallas Cowboys", 1997, "Green Bay Packers", 1998, "Denver Broncos", 1999, "Denver Broncos"]
print(superbowls_90)


# You **can also** simply **create an empty list** to initialize the variable, and then  **add elements later**.

# In[ ]:


# Creating an empty list
empty_list = []
print(empty_list)


# ## Operations
# This is a sample of some of the common operations. It is not a complete list

# ### Access list items
# You can **access** list **items by** their **index**, which **start at 0**.

# In[ ]:


# get the second pet
print(pets[1])


# In[ ]:


# print first world cup year
print(brazil_wc[0])


# In[ ]:


# accessing with an index out of range will generater an error
try:
    print(we_all_float_here[10])
# catch and print exception
except Exception as e:
    print(f"<<ERROR>> {e}")


# ### Update list items
# You can also **update** list **items by** their **index**.

# In[ ]:


print(f"List before: {pets}")

# update the 3rd pet (index 2)
pets[2] = "Lexi"

print(f"List  after: {pets}")


# ### List length

# In[ ]:


# To find the length of a list, use the `len()` function.
print(len(pets))
print(len(brazil_wc))
print(len(we_all_float_here))
print(len(superbowls_90))


# ### Adding elements

# #### append()
# append() **adds** an **element** to the **end of the list**.

# In[ ]:


print(f"List before: {brazil_wc}")

# add one more world cup for Brazil
brazil_wc.append(2002)

print(f"List  after: {brazil_wc}")


# #### insert()
# insert() **adds** an **element** to a **specified position**.

# ##### Insert in the beginning

# In[ ]:


print(f"List before: {pets}")

# add my first dog at the beginning
pets.insert(0, "Rebecca")

print(f"List  after: {pets}")


# ##### Insert at specific location

# In[ ]:


print(f"List before: {we_all_float_here}")

# add my a float in the 3rd position (3rd position has index 2)
we_all_float_here.insert(2, 1.85)

print(f"List  after: {we_all_float_here}")


# ### Removing elements

# #### remove()
# ***remove(\<item\>)* removes** the **specified item from** the **list**. If the item appears more than once, the first occurance is removed.

# In[ ]:


print(f"List before: {superbowls_90}")

# Remove the first instance of San Francisco from the list (because the actual season was still in the 80s)
# Remove the year 1990 as well, so we don't end up with a stranded year
superbowls_90.remove("San Francisco")
superbowls_90.remove(1990)

print(f"\nList  after: {superbowls_90}")


# #### pop()
# ***pop(\<index\>)* removes and returns** the **item in the index position** provided. **If** the **no index is passed**, the **last element** is **removed and returned**.

# ##### Pop the last element

# In[ ]:


print(f"List before: {pets}")

# pop the last element
last_pet = pets.pop()
print(f"Removed pet: {last_pet}")

print(f"List  after: {pets}")


# ##### Pop first element

# In[ ]:


print(f"List before: {brazil_wc}\n")

# pop the first element by passing index of 0
first_brazil_wc = brazil_wc.pop(0)
print(f"Removed Brazil's first world cup: {first_brazil_wc}")
print("Brazil defeated Sweden, the home team, by a score of 5 x 2. The legendary Pelé, when he was just 17, scored two goals.\n")

print(f"List  after: {brazil_wc}")


# ### Iterating

# #### Iterating using indexes
# Because index based access is very fast, you can iterate with a simple loop

# In[ ]:


# Iterate through each pet using the index
print("Iterating through each pet using the index:")
for i in range(len(pets)):
    print(f"- {pets[i]}")


# #### Iterating using Python iterators
# Python has a common iteration mechanism that works for most collections.

# In[ ]:


# Iterate through each pet using an iterator
print("\nIterating through each pet using an iterator:")
for pet in pets:
    print(f"- {pet}")


# # Dictionaries
# Dictionaries are **collections of key value pairs**. Some of the key characteristics are:
# - They are **mutable** in that they can be changed after creation.
# - They are **ordered and indexed by a specified key**
# - They support **fast access by key**.
# - The keys **can be of multiple types** (strings and integers are common) and the **value** associated with the key **can be of any type**.
# - **Duplicates** are **not allowed**.
# - Dictionaries are **created using braces \{ \}**
# 
# We'll **cover** some of the **basic operations here**. **For** a **full definition** of the list class, you can **refer to** the **[official dictionary class documentation](https://docs.python.org/3/tutorial/datastructures.html#dictionaries).**

# ## Creating a Dictionary

# ### Simple mapping examples

# In[ ]:


# Creating a dictionary to map the age of each pet
pet_ages = {"Tucker": 5,"Moose": 4, "Finn": 9}
print(pet_ages)


# In[ ]:


# creating a dictionary to map the winners of the last 10 baseball world series
ws_winners = {2023: "Texas Rangers", 
              2022:	"Houston Astros",
              2021:	"Atlanta Braves",
              2020:	"Los Angeles Dodgers",
              2019:	"Washington Nationals",
              2018:	"Boston Red Sox",
              2017:	"Houston Astros",
              2016:	"Chicago Cubs",
              2015:	"Kansas City Royals",
              2014:	"San Francisco Giants"}
print(ws_winners)


# ### More complex examples

# A **dictionary value can be** a **complex type** like a list, a dictionary, or a custom object.

# In[ ]:


# store data for the lst of drivers for a few Formula 1 teams
f1_team_drivers = {"Ferrari": ["Charles Leclerc", "Carlos Sainz Jr", "Oliver Bearman"],
                   "Mercedes": ["Lewis Hamilton","George Russell"],
                   "Red Bull": ["Max Verstappen", "Sergio Perez"],
                   "McLaren": ["Lando Norris", "Oscar Piastri"],
                   "Williams": ["Alexander Albon", "Logan Sargeant", "Franco Colapinto"]}
print(f1_team_drivers)


# \
# A **dictionary can store all** the **attributes for an object**, including those of **different types**.

# In[ ]:


# store data for one basketball player in a dictionary
bb_player = {"name": "Lebron James",
             "team": "Los Angeles Lakers",
             "number": 23,
             "position": "SF",
             "height": 6.9,
             "weight": 250,
             "previous_teams": ["Cleveland Cavaliers", "Miami Heat", "Los Angeles Lakers"]}
print(bb_player)


# \
# You **can also** simply **create an empty dictionary** to initialize the variable, and then  **add elements later**.

# In[ ]:


# Creating an empty dictionary
empty_dict = {}
print(empty_dict)


# ## Operations
# This is a sample of some of the common operations. It is not a complete list

# ### Access dictionary items

# #### Get an item by key
# You can **access** dictionary **items by** indexing on their **key**. In fact, the **ability to efficently retrieve** an **item based on a key**, is one of the **primary advantages of a dictionary**.

# In[ ]:


# print the age for Tucker
print(f"Tucker's age: {pet_ages['Tucker']}")


# In[ ]:


# print basketball player name and previous teams
print(f"{bb_player['name']} has previously played for {bb_player['previous_teams']}")


# #### Get dictionary keys and values
# You can **access** **dictionary keys and values separately**

# In[ ]:


# recall the world series dictionary
print(ws_winners)


# ##### Get dictionary keys

# In[ ]:


# print the world series years
print(ws_winners.keys())


# ##### Get dictionary values

# In[ ]:


# print the world series winners
print(ws_winners.values())


# ### Update dictionary items
# You can also **update** dictionary **items by** using their **key**.

# In[ ]:


print(f"Dictionary before: {pet_ages}")

# update Finn's age to 8
pet_ages["Finn"] = 8

print(f"Dictionary  after: {pet_ages}")


# In[ ]:


print(f"Dictionary before: {f1_team_drivers}")

# update the Ferrari and Mercedes drivers with expected 2025 changes
f1_team_drivers["Mercedes"] = ["George Russell", "Andrea Kimi Antonelli"]
f1_team_drivers["Ferrari"] = ["Charles Leclerc","Lewis Hamilton"]

print(f"\nDictionary  after: {f1_team_drivers}")


# ### Dictionary length
# The **length of a dictionary** returned by the len() function, is the **number of keys**.

# In[ ]:


# To find the length of a dictionary, use the `len()` function.
print(len(pet_ages))
print(len(ws_winners))
print(len(f1_team_drivers))
print(len(bb_player))


# ### Adding elements
# **Adding** an **element to** a **dictionary** is **as simple as assigning a value to a key**. **If** the **key** is **not in the dictionary** yet, the **key and associated value** it will be **added**. **If it is**, it will **update the value**.

# In[ ]:


print(f"Dictionary before: {ws_winners}")

# add another world series winner
ws_winners[2013] = "Boston Red Sox"

print(f"\nDictionary  after: {ws_winners}")


# ### Updating elements
# As mentioned above, **updating is just like adding**. **If** the **key** is **in the dictionary** it will **update the value**.

# In[ ]:


print(f"Dictionary before: {ws_winners}")

# update world series winner
ws_winners[2013] = "Milwaukee Brewers"

print(f"\nDictionary  after: {ws_winners}")


# ### Removing elements

# #### pop()
# ***pop(\<key\>)* removes and returns** the **item in the index position** provided. **If** the **no index is passed**, the **last element** is **removed and returned**.

# In[ ]:


print(f"Dictionary before: {pet_ages}")

# remove Moose
pet_ages.pop("Moose")

print(f"\nDictionary  after: {pet_ages}")


# ### Iterating
# Since **Dictionaries have both keys and values**, **iterating** can mean **different** things **depending on what** you want to **iterate on**.

# In[ ]:


# recall the formula 1 dictionary
print(f1_team_drivers)


# #### Iterating through the keys

# In[ ]:


# Iterate through each each formula 1 team
for team in f1_team_drivers:
    print(f"Team: {team}")


# #### Iterating through keys and items together using items()

# ##### Get dictionary keys

# In[ ]:


# Iterate through formula 1 team and drivers together
for team, drivers in f1_team_drivers.items():
    print(f"Team: {team}")
    print(f"Drivers: {drivers}\n")


# # Sets
# Sets are a fixed **collection of unique items**. Some of the key characteristics are:
# - They are **not mutable**, so items cannot be update after creation. You can add or delete items, but not change existing ones.
# - They are **not indexed or ordered** in any specific order.
# - Sets **cannot include duplicate values**.
# - Sets can consist of **mixed-value types**.
# - Sets are **created using brackets \{ \}**
# 
# We'll **cover** some of the **basic operations here**. **For** a **full definition** of sets, you can **refer to** the **[official set documentation](https://docs.python.org/3/tutorial/datastructures.html#sets).**

# ## Creating a set

# In[ ]:


# Creating a set for dog breeds
dog_breeds = {"Labrador Retriever", "German Shepherd", "Golden Retriever", "Cavalier King Charles Spaniel", "Poodle", "Collie"}

print(dog_breeds)


# In[ ]:


# Creating a set of the last 20 summer olympic games years
summer_olympics = {1980, 1984, 1988, 1992, 1994, 1996, 1998, 2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016, 2018, 2020, 2022, 2024}

print(summer_olympics)


# ## Operations
# This is a sample of some of the common operations. It is not a complete list

# ### Access/Iterate set items
# You **cannot access** a specific **set item by index or key**. But you **can get to** the **values by iterating**.

# In[ ]:


# Iterate through each dog breed
for breed in dog_breeds:
    print(breed)


# ### Check if item is in set
# A **common use for sets**, is to maintain a **list of valid values**. We can **use** the ***in* operation** to **check if an item is in a set**.

# In[ ]:


# check if there was a summer olympic in specific years
year = 1966
if year in summer_olympics:
    print(f"There was a summer olympics in {year}")
else:
    print(f"There was no summer olympics in {year}")

# check if there was a summer olympic in specific years
year = 1994
if year in summer_olympics:
    print(f"There was a summer olympics in {year}")
else:
    print(f"There was no summer olympics in {year}")


# ### Set length

# In[ ]:


# To find the length of a set, use the `len()` function.
print(len(dog_breeds))
print(len(summer_olympics))


# ### Adding elements

# #### add ()
# add() **adds** an **element** to the **set**.

# In[ ]:


print(f"Set  before: {dog_breeds}")

# add another breed to the set
dog_breeds.add("Rhodesian Ridgeback")

print(f"Set   after: {dog_breeds}")


# Remember that **sets do not allow duplicates**. **If** we **add** an **item** that is **already in the set**, it will **silently do nothing**.

# In[ ]:


print(f"Set  before: {dog_breeds}")

# add an existing breed to the set
dog_breeds.add("Golden Retriever")

print(f"Set   after: {dog_breeds}")


# ### Removing elements

# #### remove()
# ***remove(\<item\>)* removes** the **specified item from** the **set**.

# In[ ]:


print(f"Set  before: {summer_olympics}")

# remove 2012 from the olympics, since the world was supposed to end
summer_olympics.remove(2012)

print(f"Set   after: {summer_olympics}")


# # Tuples
# Tuples provide a simple way to **store multiple values in a single variable**. Some of the key characteristics are:
# - They are **not mutable**, so **after creation**, you **cannot update items**.
# - They are **unchangeable**, so **after creation**, you **cannot add or delete items**.
# - They are ordered and **indexed in sequence starting with zero**
# - Sets can consist of **mixed-value types**.
# - Sets are **created with a comma separated list**, which **can be grouped for clarity using** paranthesis **\( \)**
# 
# We'll **cover** some of the **basic operations here**. **For** a **full definition** of sets, you can **refer to** the **[official set documentation](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences).**

# ## Creating a tuple

# In[ ]:


# Creating a tuple for a dog name, age, and breed
dog = ("Tucker", 5, "Golden Retriever")

print(dog)


# In[ ]:


# Creating a tuple an olympic host city, and the year hosted
olympic_host = "London", 2020

print(olympic_host)


# ## Operations
# This is a sample of some of the common operations. It is not a complete list

# ### Access list items

# #### Access by index
# You can **access** tuple **items by** their **index**, which **start at 0**.

# In[ ]:


# get the first value in the olympic_host tuple
country = olympic_host[0]

# get the 2nd value in the olympic_host tuple
year = olympic_host[1]

# print host city and year
print(f"The {year} summer olympics were hosted in {country}.")


# #### Assigning tuple to individual variables
# You **can assign each element of a tuple to** an **individual variable** in a single statement.

# In[ ]:


# get dog information from the dog tuple
dog_name, dog_age, dog_breed = dog

# print dog information
print(f"{dog_name} is a {dog_breed} and is {dog_age} years old.")


# ### Tuples as function/method return values
# Because **tuples** can **group multiple values** in a **single variable**, and **common use** for them is to **return multiple values from a function**.

# Let's **create** a **function that takes two numbers**, and will return the **result of adding** them, **multiplying** them, and **diving** them.

# In[ ]:


def all_ops(num1, num2):
    add = num1 + num2
    mult = num1 * num2
    div = num1 / num2
    return add, mult, div


# **Note** that all **three operation results** were **returned together as a tuple**.
# 
# Let's **test it out**.

# In[ ]:


# use all_ops to add, multiply, and divide two numbers
result_tuple = all_ops(10, 5)

# confirm the type of the result_tuple variable
print(f"result_tuple type: {type(result_tuple)}\n")

# print each result from the result tuple
print(f"Addition result: {result_tuple[0]}")
print(f"Multiplication result: {result_tuple[1]}")
print(f"Division result: {result_tuple[2]}")



# We **could** also **take** the **function return values directly into** the **specific variables**.

# In[ ]:


# use all_ops to add, multiply, and divide two numbers, and assign to specific variables
add_result, mult_result, div_result = all_ops(10, 4)

# print the results
print(f"Addition result: {add_result}")
print(f"Multiplication result: {mult_result}")
print(f"Division result: {div_result}")


# ### Tuple length

# In[ ]:


# To find the length of a tuple, use the `len()` function.
print(len(dog))
print(len(olympic_host))


# ### Iterating
# Iterating is not something we will often do in a tuple, but it can be done similar to a list, where you can do it **via index or iterators**.

# In[ ]:


# Iterate through each dog tuple item by index
for i in range(len(dog)):
    print(dog[i])


# In[ ]:


# Iterate through each olympic_host item with an iterator
for item in olympic_host:
    print(item)


# # Comparing the data structures
# 

# |          | Lists    | Dictionaries | Sets | Tuples |
# | -------- | -------- | ------------ |----- | ------ |
# |**Summary**|Versatile ordered collections of objects |Collections of key value pairs|Fixed collection of unique items|Store multiple values in a single variable|
# |**Mutable**|Yes|Yes|No|No|
# |**Ordered**|Yes|Yes|No|Yes|
# |**Duplicates**|Yes|No|No|Yes|
# |**Use cases examples**|Most flexible collection, which can be used to implement arrays, queues, stacks, and a variety of other data structures |Used for scenarios where fast key based lookup is required, or to represent structures with multiple attribute/value pairs|Maintain list of unique values, which may be used in field validation, or eliminating duplicates from lists|Grouping multiple values into a single variable, which is particularly useful in function return values|

# In[ ]:




