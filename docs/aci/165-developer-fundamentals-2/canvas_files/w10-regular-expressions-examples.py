#!/usr/bin/env python
# coding: utf-8

# # <span style="color:blue"> Regular Expressions Examples
# AWS CLOUD INSTITUTE: PROVIDED FOR EDUCATIONAL INSTRUCTIONAL PURPOSES ONLY.

# ## Prerequisite
# **This is a continuation of the *"w10-regular-expressions-concepts"* notebook**, which covers all the basic constructs and functions. Unless you are confortable with all the RegEx constructs and Python re functions, **you should review that notebook first**.

# ## Python re Module
# **Python's built-in re module**, part of the Python Standard Library, provides a **comprehensive suite of functions** for working with **regular expressions**. You can view the **full documention** for the re module **here: https://docs.python.org/3/library/re.html**

# In[ ]:


import re


# # Redacting text
# Redacting is a process of replacing certain sensitive text with placeholders. It's very common when you want to remove **Personal Identifiable Information (PII)** from documents. That **includes, but is not limitted to, names, phone numbers, IP addresses, email addresses, etc.**

# ## Basic python implementation
# To be very clear, **this is just a simple example for educational purposes**. I'm not claiming in any way that this is a sufficient or accurate mechanism for redacting personal details.
# 
# In this example, we will be looking for:
# - Phone numbers
# - IP addresses
# - Email addresses
# - Social security numbers

# ### Input Data
# In most cases we would be reading this from a file, but for the sake of simplicity, I'll just use long multi-line strings here.

# #### An example of a customer complaint email.
# This **example has** *emails, phone numbers and IP addresses**. **No social security** number here.

# In[ ]:


input_text = "\
To whom it may concern:\n\n\
My names is Carlos Salazar, and I am having an issue with my router. I initially get a connection, but after a while it drops.\n\
My telephone number, in case you need to call me, is 732-555-0278. I'm available after 5pm everyday.\n\
You can also email me at carlos_salazar@example.com . I'll monitor my email regularly.\n\
Finally, if you need to do some troubleshooting, my IP address is 192.168.2.8, but I think that might be an internal one. \n\
I'm not sure what my external IP would be.\n\n\
Thanks\n\n\
Carlos Salazar\n"


# In[ ]:


print("-------------- Initial Text --------------")
print(input_text)


# ### Patterns used
# The key **patterns I used here** to match each element where:
# - **Phone numbers** - "(?:1-)?\d{3}-\d{3}-\d{4}"
# - **IP addresses** - "(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)"
# - **Email addresses** - "\w+@(?:\w+\.)+(?:com|edu|net|org)"
# - **Social security numbers** - "\d{3}-\d{2}-\d{4}"
# 
# Please note that the details about these patterns were discussed in the "w10-regular-expressions-concepts" notebook.

# ### Pattern Application

# #### Redact phone numbers

# In[ ]:


pattern = r"(?:1-)?\d{3}-\d{3}-\d{4}"


# In[ ]:


new_text = re.sub(pattern, "###-###-####", input_text)
print("-------------- Redacted Phone Numbers --------------")
print(new_text)


# #### Redact IP addresses

# In[ ]:


pattern = r"(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d).){3}(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)"


# In[ ]:


new_text = re.sub(pattern, "###.###.###.###", new_text)
print("-------------- Redacted IP Addresses --------------")
print(new_text)


# #### Redact email addresses

# In[ ]:


pattern = r"\w+@(?:\w+.)+(?:com|edu|net|org)"


# In[ ]:


new_text = re.sub(pattern, "####@###.###", new_text)
print("-------------- Redacted email Addresses --------------")
print(new_text)


# #### Redact social security numbers
# Our current **input doesn't have** any **social security numbers**, but **if** the **pattern doesn't match**, we simply **get** the **same text back**.

# In[ ]:


pattern = r"\d{3}-\d{2}-\d{4}"


# In[ ]:


new_text = re.sub(pattern, "###-##-####", new_text)
print("-------------- Redacted social security numbers --------------")
print(new_text)


# # Parsing Logs
# Parsing logs to look for specific information is another common usage of regular expressions. **There are logs of every type, shape, and size**. **Some** are **very structured** in format, and **others** allow for more **free form text**. 

# ## Parsing CloudWatch Logs
# As an example, we will look at AWS CLoudWatch logs. Even within CloudWatch, each log will have their own formats. For this example, we will look at logs for AWS CodeBuild. I have downloaded **CloudWatch log files for the "Tucker Pet Adoption" application CodeBuild Project**. **Tucker Pet Adoption** is an application which **was used in Developer Fundamentals 1 as an example for DevOps**. In particular, the logs are for the **build phase** of the project deployment.
# 

# ### Input Data

# In[ ]:


# log file name
log_file_name = r"data\TuckerPetAdoptionBuildProject.log"


# In[ ]:


# read log file lines
log_file = open(log_file_name, 'r')
log_lines = log_file.readlines()
log_file.close()


# In[ ]:


# print the first 10 lines
for i in range(10):
    print(log_lines[i])


# ### Patterns used
# The patterns used will obviously depend on what is it that I'm interested looking for in the log. **For my particular example**, let's **assume** I was having **occasional issues** with my the build. The application in question is a **NodeJS based application**, so the **npm tool critical in the build process**. Therefore, the **pattern** I'm using **looks for warnings and errors for npm**.
# - Pattern to look for npm warnings and errors - "npm\s(ERR|WARN)"

# ### Pattern Application

# In[ ]:


# RegEx search pattern
pattern = r"npm\s(ERR|WARN)"


# In[ ]:


# iterate through log lines
for line in log_lines:
    # apply RE to each line
    result = re.search(pattern, line)
    if (result):
        print(line)


# #### Tweaking the pattern
# Looking at the data, **I see** that **all the warnings** are **related to deprecated libraries**. This **probably wouldn't cause a build to fail** at this.
# 
# So it's **not uncommon to update the pattern to focus on different areas**. So we'll **tweak** the **pattern to remove** any **matches that include "deprecated"** after the match.
# - Updated pattern to remove "deprecated" - "npm\s(ERR|WARN)(?! deprecated)"
# 
# This is **using** an **advanced feature called** a **"Negative Lookahead"**. That's what you see in the *"(?! deprecated)"* expression.

# ### Pattern Application

# In[ ]:


# RegEx search pattern
pattern = r"npm\s(ERR|WARN)(?! deprecated)"


# In[ ]:


# iterate through log lines
for line in log_lines:
    # apply RE to each line
    result = re.search(pattern, line)
    if (result):
        print(line)


# ### Final observations
# **After removing warnings for deprecated features**, we are **only left with errors**, which seem to be **related to issues opening a log file**. This would lead me to look at **potential issues with disk space**, or previous **build processes that didn't complete gracefully**. 
# 
# Based on the timestamp on the file, it looks like this log is from March 2024, so at this point it's not something we can look and troubleshoot in detail. But hopefully this provided an example of how we can use the pattern matching to zero in on specific areas of interest.

# # <span style="color:blue">OPTIONAL FOR REVIEW</span>

# ## Parsing API Gateway Access Logs
# **When working with REST APIs**, it is very **important to understand what requests are being made, where they are coming from, and whether the request was sucessfull**. **API Gateway provides** the ability to create **access logs** that will log basic information for every request. We will look at real access log from an educational application used on other AWS classes.
# 
# We **will show multiple examples of parsing logs** with regular expressions, based on ficticious scenarios. The scenarios will look for:
# - **Filter** a request **based on location**
# - **Filter** requests **based on the HTTP status code**
# - **Filter** requests **based on API resource called**

# ### Input Data

# In[ ]:


# log file name
log_file_name = r"data\api_gateway_accesss_log.log"


# In[ ]:


# read log file lines
log_file = open(log_file_name, 'r')
log_lines = log_file.readlines()
log_file.close()


# In[ ]:


# print the first 10 lines
for i in range(10):
    print(log_lines[i])


# ### Patterns to filter based on request location
# **In order to determine the source of the REST API call**, and common mechanism is to **look at the IP address**. In most cases that should provide the country of origin. **In our scenario**, we'll assume we were trying to **look for calls originating outside the United States**, to determine our international adoption.
# 
# For my example, I used a VPN to original calls from **Brazil, Turkey, India, China, and the Ukraine**. This was a random selection based on no particular reason. I then looked up the IP address to match the countries they originated from.

# #### Patterns used
# **DISLAIMER**: The patterns below are based on an unnoficial lookup, and only represent a small sampling of IP addresses for these countries. **This should not be used in any way as a complete or accurate way to map IP addresses to these countries**.
# 
# From my sampling, I created the following rules from matching locations:
# - API calls from **Brazil** = r"193\\.\d{1,3}\\.\d{1,3}\\.\d{1,3}"
# - API calls from **India** = r"81\\.\d{1,3}\\.\d{1,3}\\.\d{1,3}"
# - API calls from **China** = r"(111|123)\\.\d{1,3}\.\d{1,3}\\.\d{1,3}"
# - API calls from **Ukraine** = r"37\\.\d{1,3}\\.\d{1,3}\\.\d{1,3}"
# - API calls from **Turkey** = r"195\\.\d{1,3}\\.\d{1,3}\\.\d{1,3}"

# #### Pattern Application

# ##### API calls from India

# In[ ]:


# RegEx search pattern
pattern = r"81.\d{1,3}.\d{1,3}.\d{1,3}"


# In[ ]:


# iterate through log lines
for line in log_lines:
    # apply RE to each line
    result = re.search(pattern, line)
    if (result):
        print(line)


# **Hold on** ... **I see** some **calls from IP addresses** that do **not start with 81. For instance**:
# ```
# | 1713481524320 | { "requestId":"cd09a709-7933-4803-b886-bcd8a12e14d7", "ip": "89.248.171.23", "caller":"-", "user":"-","requestTime":"18/Apr/2024:23:05:24 +0000", "httpMethod":"GET","resourcePath":"/moviesummary", "status":"200","protocol":"HTTP/1.1", "responseLength":"4478" }     | 8cdc959f069244cb30b8ad47bce0771d
# ```
# **What gives?**
# 
# Looking closer at my **pattern, "81.\d{1,3}.\d{1,3}.\d{1,3}"**, it **looks right, but** I made a mistake. I used the "." to represent the dot in the IP address. But **I forgot that "." has a very special meaning in RegEx**, which is to **match any item**. So basically I ended up macthing any sequence of numbers that had an 81 in it. If you look at that log line, you'll see that the very first time stamp. "17134**81**524320" has the number **81** in it, followed by other numbers.
# 
# The fix is simply to **use "\\" to escape the dots**, and have them be interpreted literally.

# In[ ]:


# RegEx search pattern
pattern = r"81\.\d{1,3}\.\d{1,3}\.\d{1,3}"


# In[ ]:


# iterate through log lines
for line in log_lines:
    # apply RE to each line
    result = re.search(pattern, line)
    if (result):
        print(line)


# **Much better!**

# ##### API calls from Brazil

# In[ ]:


# RegEx search pattern
pattern = r"193\.\d{1,3}\.\d{1,3}\.\d{1,3}"


# In[ ]:


# iterate through log lines
for line in log_lines:
    # apply RE to each line
    result = re.search(pattern, line)
    if (result):
        print(line)


# ##### API calls from China

# In[ ]:


# RegEx search pattern
pattern = r"(111|123)\.\d{1,3}\.\d{1,3}\.\d{1,3}"


# In[ ]:


# iterate through log lines
for line in log_lines:
    # apply RE to each line
    result = re.search(pattern, line)
    if (result):
        print(line)


# ##### API calls from Ukraine or Turkey
# Just to show we can, let's group both Turkey and Ukraine together. Perhaps we were looking for calls from Eastern Europe.

# In[ ]:


# RegEx search pattern
pattern = r"37\.\d{1,3}\.\d{1,3}\.\d{1,3}|195\.\d{1,3}\.\d{1,3}.\d{1,3}"


# In[ ]:


# iterate through log lines
for line in log_lines:
    # apply RE to each line
    result = re.search(pattern, line)
    if (result):
        print(line)


# ### Patterns to filter based on HTTP return
# As you can see in the log examples, there is field from the response that includes the status. Generally speaking, with an **HTTP request**, a **response in the 200 range** is **considered a success**. So let's **look for responses** that do **NOT have a status starting with 2**. So essentially we are looking for failed requests.
# - Pattern for non 2XX responses: '"status":"[^2]'
# 
# **Two things to notice** in that pattern:
# - Because I **wanted to match the literal double quote** character (") in the log, I **used a single quote to specify the pattern**. Another option would have been to escape the double quotes with a backslash.
# - The **[^2] expression matches anything which is NOT a number 2**. That **can be confusiong because "^" is also used as an anchor** for the beginning of a sentence in other patterns. **But when placed** in the **beginning of a set**, it has the **property of negating a set**.

# #### Pattern Application

# In[ ]:


# RegEx search pattern
pattern = r'"status":"[^2]'


# In[ ]:


# iterate through log lines
for line in log_lines:
    # apply RE to each line
    result = re.search(pattern, line)
    if (result):
        print(line)


# #### Observations
# At this point, I would **examine** these **failed calls** to try **to understand a potential problem**. Looking up the **status code 403**, I would find that it is used to indicate that a **request was made without propper access**. It's **also known as a "Forbidden" response**. That is in fact something important to check, because it implies a possiple malicious attack. In my case, those were simulated by me, requesting resources I knew were not valid, so we are all good :-)
# 
# 

# ### Patterns to filter based on the resource requested
# In an **REST API**, we **use HTTP requests to get or add information on specific resources**. **Multiple resources can be supported by the same API**. In this example, we will **assume** we are **looking specifically for the "movies" resource**. Just to make it a little more interesting, **also assume** we were **trying to find accesses** originating **from a specific IP address** (4.105.94.144 in this example). Perhaps there was a **report of an unusual high number of calls** to the resource **from that IP**, which **could indicate a denial of service attack**.
# - Pattern for specific resource from a specific IP: '"74.105.94.144"[\w\W]*"resourcePath":"/movies"'

# #### Pattern Application

# In[ ]:


# RegEx search pattern
pattern = r'"ip": "74.105.94.144".*"resourcePath":"/movies"'


# In[ ]:


# iterate through log lines
for line in log_lines:
    # apply RE to each line
    result = re.search(pattern, line)
    if (result):
        print(line)


# #### Observations
# I do **see a cluster of calls** on 9/11/2024, so **maybe there is any issue ...**
# 
# Fortunately in this case, I know the nefarious character making those calls was me. **That's my IP address in good old New Jersey** :-)
