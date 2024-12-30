#!/usr/bin/env python
# coding: utf-8

# # <span style="color:blue"> Requests and APIs
# AWS CLOUD INSTITUTE: PROVIDED FOR EDUCATIONAL INSTRUCTIONAL PURPOSES ONLY.

# # HTTP and API Introduction
# The notebook will focus on practical aspects, and will assume eLearning will introduce all the theory behind these. Just to level set on terminology, here is a quick definition of each.

# ## HTTP
# HTTP is the **fundamental protocol used to transfer data across the web**. It acts as the foundation for data communication on the web, facilitating the transfer of hypertext requests and information between servers and clients.
# 
# **HTTP** is the  **protocol used** when  **browsers invoke web pages**, in which case, the content returned will be HTML and JavaScript. It is  **also frequently used to in application to application calls** (see APIs below), to exchange information. In that case the content can vary.
# 
# **HTTPS is a variation of HTTP** that  **uses encryption to secure communications** between a client and server.

# ## APIs
# APIs (Application Programming Interface) are **mechanisms that enable** two **software components to communicate with each other** using a set of definitions and protocols. Interface can be thought of as a **contract of service between two applications**. This contract defines how the two communicate with each other using requests and responses.
# 
# **API is a general definition**, and it **does not mean** a **specific protocol**. Well known **types of protocols** for APIs include **SOAP, RPC, Websocket, and ... REST**. **RESP APIs** are **supported through HTTP**, and will be the **primary focus of this module**. 

# ### Note on APIs used in demos
# There are a **wide number of APIs available in the internet**, and there are **many** which are **free and public**. I encourage everyone to do some internet searches, and look for some fun ones to play with.
# 
# **For my demos**, I will **use AWS APIs, or public government APIs**, which are open to use without any type of licensing required. They may not be the most exciting ones, but it allows me to share the notebook without any licensing concerns.

# # HTTP Requests
# **HTTP supports multiple methods** of requests, **including** but no limited to **GET, POST, PUT, and DELETE**. Although any of those can be used, the **two most widely** used across the internet are:
# - **GET** - Used to request data from a specified resource
# - **POST** - Used to send data to a server to create/update a resource
# 
# Some APIs will also support PUT and DELETE operations, but not nearly as widely as GET and POST.

# ## HTTP Request Components
# An HTTP request is **comprised of multiple low level components**, including the **method specification** (GET, POST, etc), a wide number of **header options**, and optional **authorization information**. You will **occasionally view or work** with an **HTTP request in** that **raw format**, with all of these individual pieces. However **in most cases** we **use tools and libaries** that will **simplify the interface** to make such calls.
# 
# For invoking in the command line, *curl* is a simple tool we can use to send HTTP requests. Programatically in Python, there are a number of libraries available, and we will look at one below.

# ### curl
# **curl** is a **popular command line tool** available in most operating systems, either pre-installed, or with a free download. We will **not be looking at it** here **in a Notebook**, but it is something I suggest everyone plays around with, because it's useful for quick debugging and validation.

# ### Request Library
# There are **multiple libraries** available **supporting HTTP requests** with Python. One of the **most widely used** ones is the Python provides a **[Requests module](https://requests.readthedocs.io/en/latest/)**. It allows you **to programmatically make HTTP requests** to any server supporting the HTTP protocol. The Requests library is **not part** of the **Python standard library** and **requires** a **separate installation** (official instructions available at https://requests.readthedocs.io/en/latest/user/install/#install).
# 
# **Once** it's **installed**, we **can import** the libary and use it in our Python code.

# In[ ]:


import requests


# ## Invoking HTTP Requests
# We will look at REST APIs later, but we will start with just looking at requests purely from an HTTP perspective. 

# ### Retrieving a web page
# Let's **start with** a **simple example of retrieving** a **web page**, since that's one of the things most people initially associate "http" with. We will **use** the **requests library** to **make** an **HTTP GET request to** the **specified URL**. The requests library will return a **response object**, which will c**ontain the full HTML content** for the page.
# 
# I'll be using the URL for a very simple web page created just for training. If by chance this web page is remove in the future, almost any well knwon web site URLs can be used to illustrate the point.

# #### Set the URL

# In[ ]:


# set URL for an example web page
req_url = "https://d3l74483rkhp1p.cloudfront.net/hello_df2_http.html" 


# #### Execute HTTP request

# In[ ]:


# make the HTTP GET request
response = requests.get(req_url)


# #### Print the HTML page response

# In[ ]:


# print the response
print(response.text)


# ## Invoke an HTTP API
# **Invoking** an **HTTP based API** will work the **same way, but** the **output is** not an HTML file, but **data**. The data can be structured however you want, including CSV, XML, JSON, Parquet and custom formats. Recently **JSON** has become the **most popular format** in recent years.
# 
# We can break up an HTTP request into two parts:
# - **Service endpoint**: The URL for the **web service endpoint**. 
# - **Query Parameters**: Optional **request parameters**, appended to the URL after a "?" character.

# ### Specify end point and query string
# We'll put the end point and query options in a separate cell, because in the real code, those would likely be generate separately and can change. The actual HTTP call doesn't change.

# For **this example** and the next few, I'll be using the **[United States Department of Transportation Vehicle API](https://vpic.nhtsa.dot.gov/api/)**. It provides different ways to gather **information on cars and their specifications**.

# #### End point
# In this example, we will be invoking an operation to **get all the manufacturers stored in the database**.

# In[ ]:


# Get All Manufacturers operation
end_point = "https://vpic.nhtsa.dot.gov/api/vehicles/GetAllManufacturers"


# #### Query string

# In[ ]:


# specify output format
query_string = "?format=xml"


# #### Build complete request URL

# In[ ]:


# build the URL from the endpoint and query string
req_url = end_point + query_string


# #### Execute API request

# In[ ]:


# make the HTTP GET request
response = requests.get(req_url)


# Next, we'll look at how we process this response.

# ## Processing HTTP Response
# Like the HTTP request, an **HTTP response** will **include** some **header information and response data**. And like the HTTP request, we will **rarely work directly with the raw format**.

# ### Requests Module HTTP Response
# The Requests Module **response object** supports various **attributes and methods** to retrieve **response information**.

# #### Check the response status
# It's usually important to **first check whether the request was successful**. There are a lot of possible failure codes, but **200** is generally universally accepted as the **success return code**.

# In[ ]:


if (response.status_code == 200):
    print("Request was successful")
else:
    print(f"Request failed. Failure code {response.status_code}")


# If you want to see an example of a failed request, just add a couple random characters to the request URL, such that the URL will not be found. This will generate a return code of 404.

# #### Retrieve response data
# There are **multiple attributes and methods** that **return response data** in **different formats**. We'll start by just returning the **plain text representation**.

# In[ ]:


# print the response
print(response.text)


# #### Processing the data
# That's a whole **lot of data** above. The **next step** would be to write **code to extract** the **data into data structures** we can easily manipulate. The **XML format above was** the most **common format in the SOAP APIs** which were very common some years back, and **there are libraries** that would easily **encode them into data structures**. **Nowadays**, we're more likely to use **JSON** for that, and we'll see examples next.

# # REST APIs
# From a coding perspective, a **REST API** is simply a **set of standards** added **on top of** an **HTTP API**. So all we saw earlier regarding an HTTP request and APIs will apply here. We just add more to it.
# 
# With a **REST API**, we **introduce** the **notion** that we are **manipulating a resource**. A **resource can be almost anything**, depending on the domain. Books, employees, cars, products, financial instruments, etc. In this case, the existing **HTTP actions** of GET, POST, PUT, and DELETE will refer to **operations on those resources**.

# ## Invoke a REST API
# **Invoking** a **REST API** is the same as invokingan HTTP API ... because a REST API is an HTTP API. The only difference is in how we interpret the URL. In a classic REST API, by convention the URL is **split in these components**:
# - **Service endpoint**: The URL for the **web service endpoint**. 
# - **Resource**: The path to the **resource we're working with**.
# - **Query Parameters**: Optional **request parameters**, appended to the URL after a "?" character.

# ### Specify end point, resource and query string
# For this example we want to **list** all the **current models for Ferraris**. We'll make a few calls to narrow down to what we want.

# #### End point
# The endpoint will point to the **overall National Highway Traffic Safety Administration api (NHTSA) endpoint**.

# In[ ]:


# NHTSA service end point
end_point = "https://vpic.nhtsa.dot.gov/api"


# #### Resource path
# The **resource narrows into the resource** we want, which in this case is the **makes for a car manufacurer**.

# In[ ]:


# Get makes of a manufacturer operation
resource_path = "/vehicles/GetMakeForManufacturer/ferrari"


# #### Query string

# In[ ]:


# specify output format
query_string = "?format=json"


# #### Build complete request URL

# In[ ]:


# build the URL from the endpoint, resource and query string
req_url = end_point + resource_path + query_string


# #### Execute API request

# In[ ]:


# make the HTTP GET request
response = requests.get(req_url)


# ### Process response data

# In[ ]:


# Check response status
if (response.status_code == 200):
    print("Request was successful")
else:
    print(f"Request failed. Failure code {response.status_code}")
    
# print the response
print(response.text)


# ### Make additional calls to drill down on resource
# We can **use** the **make id in** this **response**, to **make** a **different call** and **get** a **list of all** the **current models**.
# 
# The **end_point and query strings** are the **same**, so we only need to **update the resource** we are requesting.

# In[ ]:


# Get All Manufacturers operation
resource_path = "/vehicles/GetModelsForMakeIdYear/makeId/603/modelyear/2024"


# In[ ]:


# build the URL from the endpoint and query string
req_url = end_point + resource_path + query_string


# #### Execute API request

# In[ ]:


# make the HTTP GET request
response = requests.get(req_url)


# ### Process response data

# In[ ]:


# Check response status
if (response.status_code == 200):
    print("Request was successful")
else:
    print(f"Request failed. Failure code {response.status_code}")
    
# print the response
print(response.text)


# **JSON data** is **best represented in Python dictionary**. We could use the Python json module to create a dictionary from the response text, but the **Requests library** has a **json() method** will return the **JSON response as** a **Python dictionary**.

# In[ ]:


# get the response JSON as a dictionary
response_data = response.json()

print(response_data)


# Looking at the data, looks like the actual **results** are **inside the "Results" attribute**, so we'll get a direct reference to that, and print our results nicely.

# In[ ]:


# get the list of models
models = response_data["Results"]

# print list of models
for model in models:
    print(f"{model['Make_Name']} {model['Model_Name']}")


# ### One more vehicle request - VIN lookup
# **Another operation supported** in the NHTSA API allows you to **look up information about a car based on the VIN**. In case you don't know, a VIN is a number that uniquely identifies a car. You can find it in the car registration. Feel free to enter a VIN you know here to test.
# 
# We'll **put** the whole thing **in a function**, so we can call it for multiple VINs.

# #### Define lookup function
# We'll **put** the whole thing **in a function**, so we can call it for multiple VINs.
# 
# You might wonder **how I knew the right fields** to get the data from. **In some cases** you can look up the **API documentation**. In this case, **I just printed the whole data first**, and looked for the fields I wanted. You can change the function above and print the whole response to see it.

# In[ ]:


def decode_vin(vin):
    # service end point and query string are the same, but we'll repeat so the function is complete
    end_point = "https://vpic.nhtsa.dot.gov/api"
    query_string = "?format=json"

    # add the vin to the resource path
    resource_path = f"/vehicles/DecodeVinValues/{vin}"

    # build the URL from the endpoint and query string
    req_url = end_point + resource_path + query_string

    # make the HTTP GET request
    response = requests.get(req_url)
    
    # Check response status a raise exception if it's a failure
    if (response.status_code != 200):
        raise Exception(f"Request failed. Failure code {response.status_code}")
    
    # get vehicle data from request response
    vehicle_data = response.json()["Results"][0]

    # print the most relevnt information
    print(f"Full model: {vehicle_data['Make']} {vehicle_data['Model']} {vehicle_data['Trim']}")
    print(f"Year: {vehicle_data['ModelYear']}")
    print(f"Vehicle type: {vehicle_data['VehicleType']}")
    print(f"Engine cylinders: {vehicle_data['EngineCylinders']}")
    print(f"Displacement: {vehicle_data['DisplacementCC']}")


# #### Execute function to decode VINs

# In[ ]:


# Invoke the function for my car
decode_vin("JM3KE4CY0G0655389")


# In[ ]:


# Invoke the function for my motorcycle
decode_vin("JKAEXEF14DDA03901")


# # Adding security to a REST APIs using Amazon API Gateway
# **Most production APIs will have some type of security**. There are **many different ways of implementing** this, and the details are not in the scope of this discussion. I will show a simple example here to illustrate the concept.
# 
# **For this example**, I will be using an **API deployed in** the **Amazon API Gateway**. **API Gateway** is an **AWS service** for creating, publishing, maintaining, monitoring, and securing REST, HTTP, and WebSocket APIs at any scale. I **supports multiple types of authentication**.

# ## The Tucker Quest API
# We **have used** the **"Tucker Quest" game** in a couple of **examples** in **previous modules**. There is an **alternate version** of the application, which **uses** a **DynamoDB database** for storing game data, **Lambda functions** to access it, and **REST APIs** to direct requests to it. These **APIs** are **implemented using** the **API Gateway**. 

# ### Using an API Key
# There are **multiple authentication mechanisms** supported in **API Gateway**, but for the sake of simplicity, we'll use one of the more straightforward approaches. We **will require** an **API Key for** our **requests**.
# 
# The **API key** has already been **created and associated with the Tucker Quest API**. We will **see how** the **key** is **specified in** the **request**.

# ### Retrieving a player character

# #### Retrieve character info function
# We'll define a **function to retrieve the basic information** for a **player character**. The **REST API resource** will **include** the **id of** the player **character** we are retrieving.

# In[ ]:


def get_character_info(id):
    # API gateway endpoint
    end_point = "https://7979hqqsq4.execute-api.us-east-2.amazonaws.com/prod"
    
    # The resource will point to a specific character
    resource_path = f"/character/{id}"
    
    # build the URL from the endpoint, resource and query string
    req_url = end_point + resource_path

    # make the HTTP GET request
    response = requests.get(req_url)
    
    # Check response status a raise exception if it's a failure
    if (response.status_code != 200):
        raise Exception(f"Request failed. Failure code {response.status_code}")
    
    # return dictionary with player info
    return response.json()


# Now we can **call** the **function to retrieve the information for a player** currently in our database. A player character id follows the format *"\<user id\>.\<character name\>"*. That's not relevant to the REST API code, but it's being noted for context.

# In[ ]:


# retrieve information for one of our characters
char_data = get_character_info("fttg.LukeWarrior")

# print selected character info
print(f'{char_data["name"]} - {char_data["description"]}')


# **Ooops!!! Why did it fail?**
# 
# This **API requires** an **API key!** So we'll add one.

# #### Specify the key in the request header
# The **key** was **randomly generated in** the **API Gateway**. It **should be treated like passwords**, and **maintained in safe storage**. In AWS, services like Secrets Manager and Parameter Store will support that.
# 
# <span style="color:red">**PLEASE NOTE**: </span> **For the sake of simplicity**, I'll **include** the **API key value direcly in** the **cell** below, but this is **NOT a good security practice**. At the end of the quarter, I'll deactivate the key.

# In[ ]:


API_KEY = "LwclnkKmPL11KiTvCyfF27TvvhEbbq1d1bgfDdD3"


# #### Redefine function to use the API Key

# In[ ]:


def get_character_info(id):
    # API gateway endpoint
    end_point = "https://7979hqqsq4.execute-api.us-east-2.amazonaws.com/prod"
    
    # The resource will point to a specific character
    resource_path = f"/character/{id}"
    
    # build the URL from the endpoint, resource and query string
    req_url = end_point + resource_path

    # Retrieve API key. Normally is generally programatically retrieved from a secure storage mechanism.
    # In our example here, we're simply getting it from the global variable specified earlier
    api_key = API_KEY

    # add key to the request header
    headers = {
        "x-api-key": api_key
    }
    
    # make the HTTP GET request, adding the header to the request
    response = requests.get(req_url, headers=headers)
    
    # Check response status a raise exception if it's a failure
    if (response.status_code != 200):
        raise Exception(f"Request failed. Failure code {response.status_code}")
    
    # return dictionary with player info
    return response.json()


# Now we can **call** the **function to retrieve the information for a player** currently in our database.

# In[ ]:


# retrieve information for one of our characters
char_data = get_character_info("fttg.LukeWarrior")

# print selected character info
print(f'{char_data["name"]} - {char_data["description"]}')


# ### Using the POST HTTP REST action to insert a new character

# #### Define function to insert character

# In[ ]:


def add_character_info(new_char):
    # API gateway endpoint
    end_point = "https://7979hqqsq4.execute-api.us-east-2.amazonaws.com/prod"
    
    # The resource will point to a specific character
    resource_path = f"/character"
    
    # build the URL from the endpoint, resource and query string
    req_url = end_point + resource_path

    # Retrieve API key. Normally is generally programatically retrieved from a secure storage mechanism.
    # In our example here, we're simply getting it from the global variable specified earlier
    api_key = API_KEY

    # add key to the request header
    headers = {
        "x-api-key": api_key
    }
    
    # make the HTTP GET request, adding the header to the request
    response = requests.post(req_url, json = new_char, headers=headers)
    
    # Check response status a raise exception if it's a failure
    if (response.status_code != 200):
        raise Exception(f"Request failed. Failure code {response.status_code}")


# We'll **need to define** a **character using** all the **attributes expected** in the database. To see what those are, we can simply **look at** the **full record** we **retrieved earlier**. Many of them are null, because they are used during game play.

# In[ ]:


# print the full character data from the previous call so we can view the complete structure
print(char_data)


# Now we can **create our own character data in that format.**
# 
# **Feel free to update the fields** below to **create your own character** name and descriptions here.

# In[ ]:


# define a new player character
new_char = {
    'id': 'fttg.Bex', 
    'name': 'Bex', 
    'pronoun': 'she', 
    'type': '2', 
    'status': 2, 
    'description': 'A powerful wizard', 
    'level': 3, 
    'max_health': 2000, 
    'health': None, 
    'attack_item': None, 
    'defense_item': None, 
    'inventory': None, 
    'sword': None
}


# Before we insert the character, we'll **try to retrieve** to **confirm it's not currently there**.

# In[ ]:


# retrieve information for one of our characters
char_data = get_character_info(new_char["id"])

# print selected character info
print(f'{char_data["name"]} - {char_data["description"]}')


# Now **insert the new character** using our API request.

# In[ ]:


# insert new character
add_character_info(new_char)


# **Confirm the operation was successful** retrieving the new character.

# In[ ]:


# retrieve information for one of our characters
char_data = get_character_info(new_char["id"])

# print selected character info
print(f'{char_data["name"]} - {char_data["description"]}')

