#!/usr/bin/env python
# coding: utf-8

# # <span style="color:blue">Introduction to Jupyter Notebooks Demo
# AWS CLOUD INSTITUTE: PROVIDED FOR EDUCATIONAL INSTRUCTIONAL PURPOSES ONLY.

# ## Markdown cells

# These first three cells are "Markdown" cells. I can **use them for headings, formatted texts**, and even to include image attachments.
# - You can edit the markdown cells by just double-clicking them
# - You can do special mark downs like bullets, **bold text**, *italic text*, and many others
# - When you are done editing, **type (Shift-Enter) to execute**
# 
# So when you see plain text like this, or fancy formatting, or headings, it's a Markdown cell

# ## Code cells
# Code cells is where you can **run Python code**:
# - You can write any Python code in them.
# - You can **execute each cell** individually, by clocking the little play button in the action bar, or more easily by **clicking (Shift-Enter)** inside the cell
# 
# The next few cells are code cells.

# In[ ]:


var1 = "Hello World"
print(var1)


# The **last value in a cell**, or a value alone in a cell, will automatically output the **string representation** for that value.

# In[ ]:


var1


# ### Functions, classes and variables

# You can write a whole function or class in a cell, or across cells. The **variables and functions carry over**.

# In[ ]:


my_list = [1 , 2 , 4 , 5 , 6, 7 , 8 , 10]


# I can put a random explanation line here in a Markdown cell before I define this function ...

# In[ ]:


def add_numbers(val_list):
    total = 0
    for num in val_list:
        total += num

    return total


# In[ ]:


def mult_numbers(val_list):
    total = 1
    for num in val_list:
        total = total * num

    return total


# Then I can write some more ... and the variable and function will be in the Python kernel memory to be used next ...

# In[ ]:


total_sum = add_numbers(my_list)
print(f"Total sum of list is {total_sum}")


# In[ ]:


total_sum = mult_numbers(my_list)
print(f"Total sum of list is {total_sum}")


# ### Order of execution

# I can **execute and re-execute cells in any order**. It doesn't have to be top to bottom.
# 
# So I can go back to the *my_list* definition cell, change the values and run the cell, then go back down to the cell that prints the total and re-execute that.
# 
# The **little number** on the left **tells** you the **order cells were executed**.

# ## Restarting or Stopping the kernel and clearing values

# The **kernel** is the thing that runs your code in the Jupyter Notebook. There are a few commands in the action bar, and the menu bar that are important:
# - You can stop the kernel if for some reason a cell is stuck (you see a "*" symbol on the left forever, that number becomes a number)
# - You can restart the kernel to clear the memory
#     - You can restart and leave the old results showing, or you can restart an clear all values

# ## Saving and loading Jupyter Notebooks

# You can **save a Jupyter Notebook as a ".ipynb" file**, with all the special formatting. You should be able to view and run it in any environment, as long as they have the necessary libraries being used in the notebook. In addition to the standard Jupyter Notebook and Jupyter Lab, there are other IDEs and cloud environments (such as SageMaker Studio Lab) which can view and run Jupyter Notebooks.
# 
# Examples in this class will not include any fancy libraries, so they should be able to run in any basic installation.

# #### Saving as Python

# You can also export a Jupyter Notebook as a standard ".py" Python file. The Markdown cells become Python comments, and the code blocks are saved as Python code sequentially.

# #  <span style="color:red"> Optional</span>: Where can I get this?

# **All practice exercises and Labs are still in Cloud9** as they were in DF1, so there is not requirement for you to use Jupyter Notebooks.<br>
# You **only need** it **if** you **want to view the fully documented demo examples** in the .ipynb format, **or** if you want to **play with it**.<br>
# It's extremely popular for Data Analytics and Machine Learning.

# ## Free download from jupyter.org

# Jupyter is an open source tool, and you can download and install for free.<br>
# Website: [https://jupyter.org](https://jupyter.org/)
# 
# **Note: We will not be discussing or supporting installation in this class, as it is not an Amazon product**

# ### Jupyterlite
# From the jupyter,org web site, you can also access a **free limitted environment** called  **Jupyterlite**(https://jupyterlite.github.io/demo/lab/index.html). Again, this is **not an AWS site**, so it's **something you would try on your own**.

# ## Free Amazon supported account under SageMaker Studio Lab

# **Amazon supports Jupyter Lab environment in the Cloud**, which is **currently free** for anyone.
# - **No credit card required**
# - **Not associated with** an **AWS Account**
# - Currently a **1 to 5 business days automated approval process**
# 
# Website for registration and all details: **[https://studiolab.sagemaker.aws/](https://studiolab.sagemaker.aws/)**

# ## Other tools
# Given Jupyter Notebooks popularity, there are a lot of third party tools which support the format, either directly or with plugins. This include VSCode and PyCharm.

# In[ ]:




