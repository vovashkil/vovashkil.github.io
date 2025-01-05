#!/usr/bin/env python
# coding: utf-8

# # <span style="color:blue"> NumPy
# AWS CLOUD INSTITUTE: PROVIDED FOR EDUCATIONAL INSTRUCTIONAL PURPOSES ONLY.

# # Introduction
# We will be looking in depth at various aspects of NumPy, but let's quickly start of with some of the basics.

# ## NumPy documentation
# **NumPy** has a **wide number of functions available**, and we will **make use of a number of them** in this notebook. Please **refer to the [NumPy documentation](https://numpy.org/doc/stable/user/index.html)** **for** all of the **details**. 
# 
# Whenever possible, **when I use a function** I'll try to **include hyperlinks** to the **official documentation** for it.

# ## Import libraries
# These are libraries will will need for this notebook.
# - **NumPy**, imported as ***np***
# - **sys, math, random and time** to help with some examples
# 
# I also update the default length of a line when printing NumPy arrays

# In[ ]:


import numpy as np
import sys
import math
import random
import time

# change default length of print line for NumPy
np.set_printoptions(linewidth=130)


# ## Creating a NumPy Array
# We will look at NumPy array creation in more details later, including arrays of multiple dimensions, but for the purpose of examining data types, we will **start with 1-dimensional arrays**, which will resemble a standard Python list. Let's look at ***some simple examples**.

# In[ ]:


int_arr = np.array([1, 2, 3, 4])
print(int_arr)


# In[ ]:


float_arr = np.array([1.6, 2.5, 3.6, 4.2])
print(float_arr)


# In[ ]:


str_arr = np.array(["Tucker", "Max", "Luke", "Moose"])
print(str_arr)


# ### Creating an empty or pre-initialized array
# If we need to **create a NumPy array of specific size**, but will **add the actual values later**, there are a couple of **functions available**: **[empty](https://numpy.org/doc/stable/reference/generated/numpy.empty.html#)**, **[zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html)**, and **[full](https://numpy.org/doc/stable/reference/generated/numpy.full.html).**

# In[ ]:


# create an empty array of size 10
empty_array = np.empty(10, dtype='int32')
print(empty_array)


# Althought the **function is called "empty"**, it **allocates random values**. If you want to **explicitly initialize the values to zero**, the **numpy.zeros** function will do that.

# In[ ]:


# create an empty
zero_array = np.zeros(10, dtype='int32')
print(zero_array)


# Or you **can use full** to **initialize the arra**y to any **predefined value**.

# In[ ]:


# create a array of "lucky 7s
seven_array = np.full(10, fill_value=7, dtype='int32')
print(seven_array)


# ## The ndarray Class
# NumPy arrays are objects of the ndarray class.

# In[ ]:


print(type(int_arr))


# You can **view** all the **methods and attributes of ndarray** in the **[official documentation](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html)**. I'll be showing a number of operations in this Notebook, but there is a lot more.

# ## Accessing elements
# We will look at many different ways of traversing and manipulating NumPy arrays later, but as one would expect from an array, an **index based access is supported**.

# In[ ]:


# print elements based in index
print(int_arr[0])
print(float_arr[1])
print(str_arr[2])


# ## Adding elements to a NumPy array
# **In reality**, there is **no way to add an element to a NumPy array in place**. They are **not meant to dynamically grow** like a list. You **should preallocate the required space** as discussed earlier.
# 
# If you really need to, one **option is to use** the NumPy **[append function](https://numpy.org/doc/stable/reference/generated/numpy.append.html)**. But please note that **this will make a copy of the original array**. It is not modifying the array in place.

# In[ ]:


# append an item to the array
new_arr = np.append(int_arr, [5])

# print original and new
print(f"Original array: {int_arr}")
print(f"     New array: {new_arr}")


# **if** we **want to modify** the **original array**, we would have to **reassign the copy to it**

# In[ ]:


# append an item to the original array and reassign to itself
int_arr = np.append(int_arr, [5])

# print original and new
print(f"Original array: {int_arr}")


# # NumPy Array Data Types
# **NumPy arrays** have **homogeneous data types**, meaning **all** the **elements** must be of the **same data type**.
# - The data type can be explicitly set at creation, or automatically derived
# - Homogenous data types **allow for improved memory efficiency and performance**

# ## Automatically assigned data type examples
# We'll see shortly how we can explictly set the NumPy array data type. If we do not specify one, NumPy will automatically assign it. If we look at the three arrays we created earlier, we can see reasonable data types were assigned.

# In[ ]:


print(int_arr.dtype)
print(float_arr.dtype)
print(str_arr.dtype)


# **Everything is self-explanatory** enough, **except for** that **"<U6"** for my **string** array. We'll discuss that a little later when we talk about strings.

# ## Specifying a data type
# If we want to **explicitly set** the **data type in a NumPy array**, we can **use the dtype attribute**. Some of the reasons for specifying the data type include:
# - **Memory efficiency**: By specifying the data type, you can **optimize the memory usage** of your NumPy arrays.
# - **Performance optimization**: **Certain operations** in NumPy are **optimized for specific data types**.
# - **Precision control**: **Float data types have different levels of precision**. For instance, dtype=np.float32 has a lower precision than dtype=np.float64. By **choosing the appropriate data type**, you can **control the trade-off between precision and memory usage** based on your application's requirements.
# - **Type safety**: Specifying the data type can help **catch potential errors during runtime** if you accidentally try to assign the wrong type.
# 
# We'll look at some examples now.

# ### Integer arrays
# Looking at our **earlier example**, we saw that our **simple integer array** was **created with** a **type of *int32***. The **"32" means 32 bits of memory**, or **4 bytes**, are allocated for **each element**. For integer that means a **2<sup>32</sup> possible values**, or **4,294,967,296**. Since we represent both negative and positive integers, the **range of values is -2,147,483,648 to 2,147,483,647**.
# 
# **Depending on our needs**, that might be **too much or too little**. If our numbers are not approaching those values, we are unncessarily wasting memory. We we try to assign a bigger number, we will get an error. So we'll see **next**, how we can **assign precisely what we want**.

# #### Basic examples

# In[ ]:


# Create a 32 bit int array
arr_int32 = np.array([-1, 0, 1, 2], dtype='int32')
print(arr_int32.dtype)
print(arr_int32)


# In[ ]:


# Create a 64 bit int array
arr_int64 = np.array([-1, 0, 1, 2], dtype='int64')
print(arr_int64.dtype)
print(arr_int64)


# In[ ]:


# Create a 8 bit int array
arr_int8 = np.array([-1, 0, 1, 2], dtype='int8')
print(arr_int8.dtype)
print(arr_int8)


# There is **no difference in the output values**, and we wouldn't expect to see any. The **difference** is **in the memory used to store** those **elements**. We'll break that down in detail later.

# ### <span style="color:blue">OPTIONAL</span> Unsigned Integer arrays

# As mentioned earlier, the standard integer data type represents both negative and positive integers. **If** you know you are **working with positive numbers only**, you can **double the maximum value by using an unsigned integer**. **For instance**, we saw earlier that the **range for int32** data type is **-2,147,483,648 to 2,147,483,647**. The **unsigned data type uint32** on the other hand has a **range of 0 to 4,294,967,296**

# #### Basic examples

# In[ ]:


# Create a 32 bit UNSIGNED int array
arr_uint32 = np.array([1, 2, 3, 4], dtype='uint32')
print(arr_uint32.dtype)
print(arr_uint32)


# In[ ]:


# Create a 64 bit UNSIGNED int array
arr_uint64 = np.array([1, 2, 3, 4], dtype='uint64')
print(arr_uint64.dtype)
print(arr_uint64)


# #### Observing the difference
# So **what diffence did that make?** Let's **try to assign 4,000,000,000** to **both** an **unsigned uint32** array, **and** a **regular int32 array**. We'll see that the **regular int32 will generate an error**, because the maximum value there is 2,147,483,647.

# In[ ]:


# Create a 32 bit UNSIGNED int array
arr_uint32[0] = 4000000000
print(f"I was able to assign {arr_uint32[0]}")


# In[ ]:


# try to assign 4,000,000,000 to a regular int32
try:
    arr_int32[0] = 4000000000
    print(f"I was able to assign {arr_uint32[0]}")
except Exception as err:
    print(f"ERROR: {err}")


# ### Float arrays
# Like integers, **floating point numbers**, or floats, can **also** be **created with specific data types**. As we saw in the earlier example, float64, is the default. That means we have 8 bytes of storage. **For floats we have float16, float32, float64, or float128** (thought float128 is not available in every platform). When it comes to **floating point numbers, having more bytes of storage** is **not as much about supporting a very large value** as we do with interegers, **but** supporting **more precision.** 

# #### Basic examples

# In[ ]:


# Create a 16 bit float array
arr_float16 = np.array([1.1, 2.2, 3.3, 4.4], dtype='float16')
print(arr_float16.dtype)
print(arr_float16)


# In[ ]:


# Create a 32 bit float array
arr_float32 = np.array([1.1, 2.2, 3.3, 4.4], dtype='float32')
print(arr_float32.dtype)
print(arr_float32)


# In[ ]:


# Create a 64 bit float array
arr_float64 = np.array([1.1, 2.2, 3.3, 4.4], dtype='float64')
print(arr_float64.dtype)
print(arr_float64)


# #### Precision difference
# As I mentioned earlier, having a **bigger float data type means more precision**. To visualize that, let's **see the difference** in precision in the three NumPy arrays above, **if I want to store Math's most famous constant: π (aka, "Pi")**

# In[ ]:


import math

arr_float16[0] = math.pi
print("Pi with float16: ", arr_float16[0])

arr_float32[0] = math.pi
print("Pi with float32: ", arr_float32[0])

arr_float64[0] = math.pi
print("Pi with float64: ", arr_float64[0])


# ### String arrays
# **NumPy is primarily focused on numerical calculations** (it's right there in the name!), **but has some basic memory efficient support for strings**. Let's look again at the simple string array we created earlier, and another one.

# In[ ]:


str_arr = np.array(["Tucker", "Max", "Luke", "Moose"])
print(str_arr)
print(f"Data type: {str_arr.dtype}\n")

str_arr2 = np.array(["Golden Retriever", "Cavalier King Charles Spaniel", "Labrador Retriever", "German Spitz"])
print(str_arr2)
print(f"Data type: {str_arr2.dtype}\n")


# Instead of a plain *string* type, we see **<U6 and <U29**. **What does that mean?** The **"U" stands** for the fact that **strings are stored as 4 byte Unicode characters**. The **number after it** is the **number of characters allocated for each string**. If you look at our arrays, the **largest element in str_arr ("Tucker") had 6 characters**, and the **largest element in str_arr2 ("Cavalier King Charles Spaniel") had 29 characters**. NumPy tries to be as space efficient as possible, allocating only as much space as it needs. The **"<" before the "U"** is a very low level concept, related to **how the bytes are encoded**. It's not something we're going to cover here, but if anyone is curious, you can refer to https://numpy.org/doc/stable/reference/generated/numpy.dtype.byteorder.html for the details.

# ### Other data types
# **NumPy supports a number of other data types, including support for complex numbers, booleans, and other specialized types**. We will not discuss all of them here, but you can **refer to** the **[NumPy data type documentation](https://numpy.org/doc/stable/user/basics.types.html)** for a **full description of data types**.

# ## Comparing memory utilization
# We've mentioned how NumPy is using these precise data types to optimize memory utilization. Let's confirm this. We can **use** the Python **[getsizeof function](https://docs.python.org/3/library/sys.html#sys.getsizeof)** in the **built-in sys module** to verify the **size in bytes of a variable.**

# ### Create arrays of different data types
# Let's recreate our integer arrays, but this time will allocate space for more elements.

# In[ ]:


# make array size a variable so we can change later if we want
arr_size = 1000


# In[ ]:


# initalize arrays of multiple int data types
arr_int8 = np.empty(arr_size, dtype='int8')
arr_int16 = np.empty(arr_size, dtype='int16')
arr_int32 = np.empty(arr_size, dtype='int32')
arr_int64 = np.empty(arr_size, dtype='int64')

# initalize arrays of multiple float data types
arr_float32 = np.empty(arr_size, dtype='float32')
arr_float64 = np.empty(arr_size, dtype='float64')


# ### Assign random items to arrays
# Let's recreate our integer arrays, but this time will allocate space for more elements.

# In[ ]:


for i in range(arr_size):
    # generate a random value
    value = random.randint(0, 127)

    # assign same value to all arrays
    arr_int8[i] = value
    arr_int16[i] = value
    arr_int32[i] = value
    arr_int64[i] = value
    arr_float32[i] = value
    arr_float64[i] = value

# print a few numbers just to confirm it worked
print(f"arr_int8[0] = {arr_int8[0]}")
print(f"arr_int16[0] = {arr_int16[0]}")
print(f"arr_int32[0] = {arr_int32[0]}")
print(f"arr_int64[0] = {arr_int64[0]}")
print(f"arr_float32[0] = {arr_float32[0]}")
print(f"arr_float64[0] = {arr_float64[0]}")


# ### Verify memory utilized for each array

# In[ ]:


# print the memory allocated for each
print("Memory utilized for int arrays:")
print(f"  int8  array: {sys.getsizeof(arr_int8)} bytes")
print(f"  int16 array: {sys.getsizeof(arr_int16)} bytes")
print(f"  int32 array: {sys.getsizeof(arr_int32)} bytes")
print(f"  int64 array: {sys.getsizeof(arr_int64)} bytes")
print(f"  float32 array: {sys.getsizeof(arr_float32)} bytes")
print(f"  float64 array: {sys.getsizeof(arr_float64)} bytes")


# ### Observations
# We can see there is a **clear difference**, which is not surprising. So if you're operating with smaller numbers, there is an obvious memory improvement in utilizing the correct data type. **In this case**, since our **elements were not exceeding 127**, we **could have used an int8** array, which would be **8 times smaller than** the corresponding **int64** array.
# 
# It's interesting to see that int32 and float32, and int64 and float64, have the same size. So there is not extra overhead for floats.

# ### What about Python lists?
# **We said** that a **NumPy array** is **more memory efficient than a Python list**. So let's **verify** what would be the **memory utilized for a Python list** of similar integers. For a **regular list**, we are bound by the **standard Python integer type**.

# In[ ]:


int_list = []
for i in range(arr_size):
    # generate a random value
    value = random.randint(0, 127)

    # assign same value to all arrays
    int_list.append(value)

# print a first number just to confirm it worked
print(f"int_list[0] = {int_list[0]}")


# In[ ]:


# print the memory allocated for each
print("Memory utilized for int arrays:")
print(f"  int_list: {sys.getsizeof(int_list)} bytes")


# If we compare with the sizes for the NumPy arrays, that **seems comparable** (a little bigger) **to** a **NumPy int64 array**. **That's a bit wasteful**, considering that's the largest possible data type in NumPy.

# ## <span style="color:blue">OPTIONAL</span> Data type conversions

# If **after creating an array** you realize you need to **change the data type**, you can do that using the **[astype function](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.astype.html)**. You may want to do that either because you realized the data type you have is more than you need, or because you realize you need a bigger data type to fit new values. You may also need to change if the data type was incorrecly set, such as an array that was meant for floats, created as an int array.
# 
# Please note that **this will not make a change in place**, but will instead **create a new copy**. 

# ### Conversion to a different data type size

# In[ ]:


# Update the int64 array to a new more efficient int32 array
new_arr_int32 = arr_int64.astype(np.int32)

# Confirm data was not changed, by printing the first element
print("Data is the same:")
print(f"arr_int64[0] = {arr_int64[0]}")
print(f"new_arr_int32[0] = {new_arr_int32[0]}")

# Confirm data type and memory utilization have changed
print("\nData type and memory used changed:")
print(f"arr_int64.dtype     = {arr_int64.dtype} - Memory usage: {sys.getsizeof(arr_int64)} bytes")
print(f"new_arr_int32.dtype = {new_arr_int32.dtype} - Memory usage: {sys.getsizeof(new_arr_int32)} bytes")


# ### Conversion to a different data type
# One **common scenario is converting between int and float**. Look at the scenario below, where I create an array initalizing values to 0, which I plan to use to add floating point values.

# In[ ]:


# create a new array, initializing values to 0
new_arr = np.array([0, 0, 0, 0, 0])

# Enter Pi as the first value
new_arr[0] = 3.1416

# print the value of Pi
print("Pi, up to 4 decimal places is: ", new_arr[0])


# **What hapenned?**
# 
# **In this line**:
# > new_arr = np.array([0, 0, 0, 0, 0])
# 
# We **did not specify a dtype**, so **NumPy defaulted to an integer array** (int32 to be precise). We'll verify that next.
# 
# So **in this line**, we were **trying to assign** a **float** value **in** an **integer array**:
# > new_arr[0] = 3.1416
# 
# **NumPy automatically converts the float value to an int**, truncating the decimal part. That's why the next line will print "3".
# 
# To resolve this problem, we'll **convert the array to a float array**.

# In[ ]:


# print the current array type
print(f"Current array type: {new_arr.dtype}")

# convert the array to a float32 array
print("\nConverting array ...")
new_arr = new_arr.astype(np.float32)

# print the updated array type
print(f"\nUpdated array type: {new_arr.dtype}")

# Enter Pi as the first value
new_arr[0] = 3.1416

# print the value of Pi
print("\nPi, up to 4 decimal places is: ", new_arr[0])


# **What's all this extra "warnings" stuff?** 
# This one is a bit complicated, because it's **something that is getting changed**. The **error** here **is** when we try to **assign 200 to the array**. That's because an **int8 array** can only have **numbers in the range of -128 to 127** . 2<sup>8</sup> is 256, but in a signed array half of that is used for negative values.
# 
# **Currently, NumPy will automatically convert the number**, which sometimes can be good, but in this is a bit dangerous, since it will NOT actually set it to 200 (you can't fit something bigger than the space you have). So that **conversion** feature **for overflows is being deprecated**, and in the future it will generate an error.
# 
# **In order to force it to make it an error** now, I **use the two lines you see in the beginning of the block**. Had I not done that, we would get a nasty looking deprecation warning.

# # NumPy Array Dimensions
# All the examples we've seen so far have been with one-dimensional arrays. We started with them, because they are the most common, and the easiest to visualize. However **NumPy** can **support arrays of multiple dimensions**:
# - **Zero-dimensional** arrays – referred to as **scalars**, these are **single values** or elements
# - **One-dimensional** arrays – referred to as **vectors**, these are **ordered sequence** of elements
# - **Two-dimensional** arrays - referred to as a **matrices**, they resemble **tables with rows and columns**
# - **Three-dimensional** arrays - referred to as **tensors** , they are **cube-like** structures
# - **Four-dimensions and beyond**
#     - **NumPy** will **support** arrays of nearly **unlimited dimensions**
#     - They are not easy to visualize, but are useful in scientific calculations and machine learning among other things

# We'll look at examples of how to create arrays of each dimension now. I'll **use** a common **theme of grades in a class** as I progress from dimension to dimension. In our examples, when we want to **check the number of dimensions**, we can **use** the **[ndim attribute](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.ndim.html#).**. We can also **view** the **number of elements accross each dimension**, or axis, **using** the **[shape attribute](https://numpy.org/devdocs/reference/generated/numpy.ndarray.shape.html)**.

# ## Zero-dimensional array (scalar)
# Zero-dimensional arrays, referred to as scalars, are single values or elements. So for our example, let's say I'm creating a **single grade for one student in a test for one class**. Assume our grading scale is from 0 to 100.

# In[ ]:


# create a single grade element
grade = np.array(92)

# print the value and number of dimensions
print(f"Dimensions: {grade.ndim}")
print(f"Value: {grade}")


# This **may seem** a bit **uncessary**, creating a NumPy ndarray for a single element, and that's true. We **wouldn't normally create individual zero-dimensional arrays** like this. In practical terms, a **zero-dimensional array, or scalar**, can be thought of as the **type of a single element in a larger array**.
# 
# For example, let's **recreate** the **simple one-dimensional array** we used earlier in our introduction. We can print a single element staright out as if it was a plain value. But if we check the **type of a single element**, we see that it is in fact a **numpy object**, of **dimension 0**.

# In[ ]:


# create a simple one dimensional NumPy arrar
arr_int32 = np.array([-1, 0, 1, 2], dtype='int32')

# print the first element
print(f"First element value: {arr_int32[0]}")
print(f"First element type: {type(arr_int32[0])}")
print(f"First element dimensions: {arr_int32[0].ndim}")


# ## One-dimensional array (vector)
# One-dimensional arrays, referred to as vectors, are ordered sequence of elements. 
# 
# Going back to our grade example, now we need to **store** the **final grades** for **one student** in **each quarter of a class**. So assume the **student** had a grade of **92 in the first quarter**, **then 83, 90, and 87** in the subsequent quarters. We will **store** these **values in a one-dimensional NumPy array**. We can **visualize** this structure in the **image below**.

# ![Picture1.png](attachment:da4bcfd8-6b67-4b65-9217-c238a6111552.png)

# Let's create it:

# In[ ]:


# create a single grade element
class_grades = np.array([92, 83, 90, 87], dtype='int8')

# print the value and number of dimensions
print(f"Dimensions: {class_grades.ndim}")
print(f"Shape: {class_grades.shape}")
print(f"Value: {class_grades}")


# **Note**: Did you notice that I **used** the very **small dtype of int8**? If I used the **default integer** size, which is int32, I would allocating 32 bits for each grade, which is large enough for a value of **2,147,483,647**.  But that would be a **great waste**, considering my **maximum grade is 100**. **int8** can go **up to 127**, so that's a **good fit**, and I'm being **memory efficient.**
# 
# The **shape attribute** value of **(4,)** tells us we **have 4 elements in this axis**, which is the only one we have, since this is a one-dimensional array.

# ## Two-dimensional array (matrix)
# Two-dimensional arrays, referred to as a matrices, resemble **grids with rows and columns**.
# 
# For an example, let's continue on our class grades journey. Now, we want to **store a student grade's for 3 classes**. As we commonly do in IT, we will **map the class names to an integer**, since numbers are faster to process than strings. So we define the class numbers as:
# - 0: English
# - 1: Math
# - 2: History
# 
# We will create a **two-dimension NumPy array**, where **each row represents one class**. We **represent** each **class grades as we did before**, with one element for each quarter. We can **visualize** this matrix in the **image below**.

# ![Picture2.png](attachment:64323c9a-b764-4f65-ac9b-c8a89e5f06e7.png)

# Let's create it:

# In[ ]:


# create a NumPy for 3 classes and 4 quarter2
student_grades = np.array([[77, 79, 75, 80],
                           [92, 83, 90, 87],
                           [72, 86, 94, 95]],
                          dtype='int8')

# print the value and number of dimensions
print(f"Dimensions: {student_grades.ndim}")
print(f"Shape: {student_grades.shape}")
print(f"Value:\n {student_grades}")


# The cool part here is that **now we can have lightening fast access to specific grades**, by **using array indexes**. In our NumPy array, a grade for one class in one quarter will be: `student_grades[<class index>][<quarter index>]`
# 
# For example ...

# In[ ]:


# Print the english grade in the second quarter 
print(f"Grade[0][1]: {student_grades[0][1]}")

# Print the history grade in the fourth quarter 
print(f"Grade[2][3]: {student_grades[2][3]}")


# ## Three-dimensional array (tensor)
# Three-dimensional arrays, referred to as tensors, they are cube-like structures.
# 
# Let's continue with our grades scenario for an example. **Right now**, we **have** a **2 dimensional array** that can store **grades for a one class in** each **rows**, and the **grade for each quarter in** the **columns** for **one student**. **What if** we **want to store** the **grades for all** my **students?** I would need one of these 2 dimensional arrays for each of my students. I can **combine them all in a 3 dimensional array**, where the **first dimension will be an index for the student**. So if each of my students are assigned a number from 0 to n (assigning numbers to students is a common practice in any case), my **array would look like**: `all_student_grades[<student index>][<class index>][<quarter index>]`
# 
# For our example, so that our initializations don't get crazy long, let's assume we are tracking 4 students. The students in my class (named after my pets) are:
# - 0: Tucker
# - 1: Luke
# - 2: Finn
# - 3: Lexi
# 
# We can **visualize** this multi-dimensional array in the **image below**, where each student is one "slice" in the cube.

# ![Picture3.png](attachment:4dab3adc-7deb-4742-9f91-24186fa0fe62.png)

# Let's create it:

# In[ ]:


# create a NumPy for 4 students, 3 classes and 4 quarter grades
all_student_grades = np.array([[[77, 79, 75, 80],
                                [92, 83, 90, 87],
                                [72, 86, 94, 95]],
                               [[88, 91, 89, 77],
                                [78, 82, 80, 98],
                                [92, 86, 94, 86]],
                               [[91, 93, 90, 92],
                                [88, 82, 80, 87],
                                [72, 76, 74, 75]],
                               [[81, 83, 80, 82],
                                [78, 82, 80, 87],
                                [92, 86, 94, 95]]],
                              dtype='int8')

# print the value and number of dimensions
print(f"Dimensions: {all_student_grades.ndim}")
print(f"Shape: {all_student_grades.shape}")
print(f"Value:\n {all_student_grades}")


# The **shape of (4, 3, 4)** tells me I have **4 elements** in the **first axis (4 students)**, **3 elements** in the **second axis (3 classes)**, and **4 elements** in the **third axis (4 quarters)**.
# 
# And once again, I can **use indexes to directly access any value**. For example ...

# In[ ]:


# Print the Tucker's Math grade in the third quarter
print(f"Grade[0][1][2]: {all_student_grades[0][1][2]}")

# Print Finn's history grade in the first quarter 
print(f"Grade[3][2][0]: {all_student_grades[3][2][0]}")


# ### Reminder of initialization of arrays
# That **creation of our 3-dimensional array required a very long statement**. **In reality**, we wouldn't be creating an array like with all the values spelled out at creation time. We would **either** be **populating** them **from a file**, **or updating** them **over time**. Take our grades scenario for instance. Grades would be added one at a time, as the school year progressed.
# 
# We **showed earlier** how we can **initialize an array** with the expected number of elements, without having to specify them. We will use the **[full function](https://numpy.org/doc/stable/reference/generated/numpy.full.html)** to initialize aour array with -1 values (we don't want to use 0, because sadly that could be someones real grade). In the earlier examples we used them to unitialize a one-dimensional array, but we **can provide** the **shape as** an **input**, and the functions will **initialize values across all dimensions**.

# #### Initialize three dimensional array with zeros
# Let's **initialize a three dimensional array for our grades scenario**. Remember, we need to allocate space for **4 students**, **3 classes**, and grades for **4 quarters**. So our **shape was (4, 3, 4)**.

# In[ ]:


# create an new grade array initialized with -1 in all elements
new_student_grades = np.full((4, 3, 4), fill_value = -1, dtype='int8')

# print the value and number of dimensions
print(f"Dimensions: {new_student_grades.ndim}")
print(f"Shape: {new_student_grades.shape}")
print(f"Value:\n {new_student_grades}")


# Now we are **able** to **set grades individually**. 
# 
# **For example**, if **Luke** (student index of 1), **received 95 in** his **English** test (class index of 0), in the **3rd quarter** (quarter index of 2), we could **update it as follows**:

# In[ ]:


# set grade for Luke, in English, on 3rd quarter
new_student_grades[1][0][2] = 95

# print updated array
print(f"Value:\n {new_student_grades}")


# ## Four-dimensional array
# **You thought we were done? No!** The NumPy world doesn't end with three dimensions.
# 
# Although we **cannot easily visualize** them with a picture, **multi-dimensional arrays** can be **used to express** how various **different factors contribute to an end value**. In Machine Learning, each dimension might represent a different attribute, and the values in the indovidual elements represent how all the different attributes contributed to a result.
# 
# Even our simple **class grade example can be expanded into a four dimensioanl array**. Let's say we want to **expand** our **previous example** of grades for students, such that we now **track their whole academic history**, from 1st grade to 12th. Our NumPy array will have the school year as the first axis, and the following axes will be the same ones we had before. So **these would be the axes**:
# 1. **School year**: 1st grade (index 0) through 12th grade (index 11)
# 2. **Student #**: Index representing the student
# 3. **Class subject**: O for English, 1 for Math, and 2 for History
# 4. **School quarter**: Q1 (index 0) through Q4 (index 3) 
# 
# 
# We **can't visualize** arrays **beyond 3 dimensions with** clear **images**, but that might be a good thing. Because we **can start viewing** these **arrays as** just **ways of representing multiple attributes**, without getting too bogged down with the Math.

# ### Initialize a four-dimensional array
# We're **not** going to **manually** enter 12 grades worth of grades for our students **as we create** the **array**. It's possible, but it would not be practical. So we **will use** the same **full function** we use previously.
# 
# Since we're not entering values one by one, we might as well make it more realistic, and **add a few more students to our class**. Let's say **30**. So my **array dimensions will be**:
# - **12** in the **school year axis**
# - **30** in the **student # axis**
# - **3** in the **class subject axis** (because English, Math, and History are probably the only subjects common between 1st and 12th grade)
# - **4** for **school quarter axis**
# 
# **With** the **values above**, our **array shape** is **(12, 30, 3, 4)**. This **array will have 4320** elements (12 x 30 x 3 x 4), which we **can verify with** the **[size attribute](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.size.html#)**.

# In[ ]:


# initialize a four dimensional array for complete student history
all_students_transcript = np.full((12, 30, 3, 4), fill_value = -1, dtype='int8')

# print the value and number of dimensions
print(f"Dimensions: {all_students_transcript.ndim}")
print(f"Shape: {all_students_transcript.shape}")
print(f"Size: {all_students_transcript.size}")

# print the value, but truncate the output to a max 200 characters
print(f"Value:\n {str(all_students_transcript)[:200]}")


# ### Assign values to a four-dimensional array
# We will **not** be **manually setting 4,320 elements** in our array. We'll **use loops to generate** all the **indexes**, and **generate random grades between 50 and 100** for each grade.

# In[ ]:


# setting a specifc random seed will always generate the same sequence of random numbers
# this is not required, but I wanted to see the same grades every time I run this cell
random.seed(7)

# this nested loop will generate every combination of indexes for school year, student, subject, and quarter
for year in range(12):
    for student in range(30):
        for subject in range(3):
            for quarter in range(4):
                # generate a random number between 50 and 100, and assign to array
                grade = random.randint(50, 100)
                all_students_transcript[year][student][subject][quarter] = grade


# ### Retrieve values from a four-dimensional array
# As we've done before, **retrieving information** for any **one element** is a **simple** matter of **using the indexes**. Independent of size and dimension, this **retrieval** will always be a very fast **O(1) time complexity** operation.

# In[ ]:


# Get the 2nd quarter history grade, for student # 17, on his 6th grade in middle-school. So:
# Grade index: 5 (remember indexes start at 0)
# Student index: 17
# Subject index: 2
# Quarter index: 1
print(f"Grade[5][17][2][1]: {all_students_transcript[5][17][2][1]}")

# Get the 1st quarter English grade, for student # 5, on his 9th grade in high-school. So:
# Grade index: 8
# Student index: 5
# Subject index: 0
# Quarter index: 0
print(f"Grade[8][5][0][0]: {all_students_transcript[8][5][0][0]}")


# ## More and more dimensions
# **I'm going to stop at four dimensions**. For one thing, I don't think I can stretch my grade example anymore, unless we go into the real of science fiction, and I start maintaining a student's transcript across multiple parallel universes.
# 
# **However, arrays of many dimensions** are **used in multiple fields** of science. They can be **used to express** how various **different factors contribute to an end value**. In **Machine Learning**, **each dimension** might represent a **different attribute**, **and the values** in the individual elements **represent how** all the **different attributes contributed to a result**.
# 
# Even without examples, I'm sure you can visualize that they would continue to work in a similar way to what I did with the four-dimensional array.

# # NumPy operations
# There are a **wide number of operations** which can be performed on arrays **using NumPy**. We'll **cover just a sampling** in here as we go through a scenario, but **for all** the **details** please refer to the **[full documentation](https://numpy.org/doc/stable/index.html)**.

# ## Auto-racing example
# Just for a little variety, let's switch to an **auto-racing example for data examples**. We'll create arrays with a few different NumPy arrays around that domain. We'll also **see** some **NumPy functions** being used **while we created** this **data**.
# 
# Here, we'll just start by creating an array from our racers.

# In[ ]:


# Create a NumPy array for our racers
racers = np.array(["John Stiles", 
                   "Alejandro Rosalez", 
                   "Akua Mansa", 
                   "Marcia Oliveria", 
                   "Diego Ramirez",
                   "Wei Zhang",
                   "Saanvi Sarkar",
                   "Jorge Souza",
                   "Arnav Desai", 
                   "Mary Major"])


# ## Some basic math functions

# ### NumPy random
# **NumPy has** a number of **builtin functions** to **generate random numbers**, they'll create the numbers and have them ready in a numpy array. In our example, **we'll use** the **[Generator class](https://numpy.org/doc/stable/reference/random/generator.html)**, and the **[uniform method](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.uniform.html)**.

# In[ ]:


# define a NumPy random Generator object (passing a seed to get the same numbers in each run)
rng = np.random.default_rng(3)


# In[ ]:


# generate 20 random lap times between 120 and 150 seconds
lap_times = rng.uniform(120.0, 150.0, 20)
lap_times


# We successfully **created** a **NumPy array with 25 elements for** our **lap times.** However, to be realistic, these **laptimes should go up to milliseconds** in precision, so will **need to round** those really long numbers.

# ### NumPy round
# **NumPy has functions** perform**typical mathematical operations** **across an entire array** in one shot. That's the **concept of vectorizarion**, which we will discuss next. In this case, we'll use use the **[round function](https://numpy.org/doc/stable/reference/generated/numpy.round.html#)** to **round** all the **numbers to 3 decimal points**.

# In[ ]:


lap_times = np.round(lap_times, 3)
lap_times


# That's perfect!

# ## Combining functions to create more data
# You can **combine multiple NumPy functions** to generate the array you want. You **can do** that **one function at a time**, **or chain multiple operations together** in a single line. We'll see one example here.

# Assume we can **map our racers to a racer index**. So for the example abover we might have:
# - 0 - John Stiles
# - 1 - Alejandro Rosalez
# - 2 - Akua Mansa
# - 3 - Marcia Oliveria
# - 4 - Diego Ramirez
# - 5 - Wei Zhang
# - 6 - Saanvi Sarkar
# - 7 - Jorge Souza
# - 8 - Arnav Desai
# - 9 - Mary Major
# 
# So we can now **create a two dimensional array**, to **record the laps for each racer** in a race of **15 laps**. We'll use two functions here:
# - **First** we'll **use** the **uniform function**, and we'll **specify the shape of the output array** to give use 10 racers, with 15 laps
# - We **chain** that **output** directly **to** the **round function**, to round all laps to milliseconds

# In[ ]:


# Create a two dimenstional array with 15 random lap times for 10 racers
racers_lap_times = rng.uniform(120.0, 150.0, (10, 15))

# round the lap times to 3 decimals
racers_lap_times = np.round(racers_lap_times, 3)

# print the value and number of dimensions
print(f"Dimensions: {racers_lap_times.ndim}")
print(f"Shape: {racers_lap_times.shape}")
print(f"Value:\n {racers_lap_times}")


# ## More indexing and slicing

# ## Retrieving elements from the end
# A **negative index retrieves elements from the end**

# In[ ]:


# Retrieve the last racer name
print(f"Last racer: {racers[-1]}")


# In[ ]:


# retrive the lap time for the 2nd to last racer index
print(f"Penultimate racer final lap time: {racers_lap_times[-2][-1]}")


# ### Slicing portions of the array

# In[ ]:


# Retriving the racers name from 2 to 8
print(f"Racers 2 to 8: {racers[2:8]}")


# In[ ]:


# Retrieving the last 5 laps for the first 3 racers
print(f"Last 5 laps for first 3 racers:\n {racers_lap_times[:3, -5:]}")


# ### Slicing with alternating elements

# In[ ]:


# Retrieving every other lap for the 3rd racer
print(f"Every other lap for 3rd racer:\n {racers_lap_times[2, ::2]}")


# ### Assigning to slices
# You can assign new values to a slice, and that will modify that data in place.

# In[ ]:


# print the last racer's lap times
print(f"   Last racer laps: {racers_lap_times[-1]}")

# Replace laps 5 through 9 for the last racer with new random values
racers_lap_times[-1, 5:10] = np.round(rng.uniform(120.0, 150.0, 5), 3)

# print the updated last racer's lapo times
print(f"Updated racer laps: {racers_lap_times[-1]}")


# **Note** that the **first 5 laps** are **not changed**, **but laps 5-10 are different** in the updated array.

# ## Iterating
# We've already seen that we **can iterate using the array indexes**, **but** NumPy **also** supports standard **Python iterators.**

# ### Iterating in one dimension

# In[ ]:


# iterate through array of racer
for racer in racers:
    print(f"Item: {racer}")


# ### Iterating in two dimensions

# In[ ]:


# iterate through racer laps
for racer_laps in racers_lap_times:
    print(f"Item: {racer_laps}")


# **Note** that **even though racers_lap_times has two dimensions**, our **iteration** by default only **walked through** the **array row by row**. Each item, replaced one entire row. If we want to iterate through all the items, we have a couple of options.

# #### Using a nested loop

# In[ ]:


# iterate through each racer lap
for racer_laps in racers_lap_times:
    for lap in racer_laps:
        print(f"{lap} ", end='')


# #### Using the nditer class
# **Another way to**  want to **iterate through every element**  in a **multi-dimensional array**, I can **use** the **[nditer class](
# https://numpy.org/doc/stable/reference/generated/numpy.nditer.html#)**.

# In[ ]:


# iterate through each racer lap using nditer
for lap in np.nditer(racers_lap_times):
    print(f"{lap}", end=' ')


# nditer has a few other options for iterations beyond just stepping through each item, but we won't discuss them here.

# ## <span style="color:blue">OPTIONAL:</span> Using the ndenumerate class

# **There are a number** of other **iteration mechanisms provided in NumPy**, which in the interest of time we cannot cover here. Once such example is the ndenumarate class.
# 
# **If** you want to **iterate through an array**, but also **keep track of which index you are in order**, you can  **use** the **[ndenumerate class](
# https://numpy.org/doc/stable/reference/generated/numpy.ndenumerate.html#)**. **In addition to returning the element**, it **returns** an **tuple** containing the **position of** the **element in** the **array**.

# In[ ]:


# iterate through each racer's with ndenumarate, and use index to print corresponding racers's name
racer_idx = -1
for index_tuple, lap in np.ndenumerate(racers_lap_times):
    # check if this is a new racer
    if index_tuple[0] > racer_idx:
        racer_idx = index_tuple[0]
        print(f"\n{racers[racer_idx]} laps: ", end='')
    print(lap, end=' ')


# ## Searching
# **Searching for items in** an **NumPy array** will **return the index location** for **items found**. We will **use** the **[where function](https://numpy.org/doc/stable/reference/generated/numpy.where.html)**  to **search**  a **NumPy array based on a specified condition** . 

# ### Searching in one dimension
# We'll start with a one dimension array to make things simpler. We'll **take the laps** for just the **last racer**, Mary Major. Notice we'll **use the [copy function](https://numpy.org/doc/stable/reference/generated/numpy.copy.html)**, so that we **create a new array**, **otherwise** this **would be just a reference**, and changes that we made in the new array would impact the original.

# In[ ]:


# set a NumPy array for just the last racer
mary_laps = racers_lap_times[-1].copy()
print(f"mary_laps dimensions: {mary_laps.ndim}")
print(f"Mary Major's laps: {mary_laps}")


# Now let's **find** all the **laps** which were **under 130 seconds**

# In[ ]:


# find all laps under 130 seconds
under_130 = np.where(mary_laps < 130.0)
print(f"Laps indexes less than 130 seconds: {under_130}")


# If you look above, you can see the **numbers match the indexes** of **elements with values under 130**. **If** we want the **actual lap values**, which just need to **use the indexes**, which as we know, are nearly instantenous with NumPy

# In[ ]:


for lap in mary_laps[under_130]:
    print(f"{lap}", end=' ')


# ### Searching in multiple dimension
# Now that we've seen how the results are returned as a tuple for one dimension, let's see what happens when we have multiple dimensions.

# In[ ]:


# print all the race laps
print(f"All race laps:\n{racers_lap_times}\n")

# find all laps under 130 seconds
under_130 = np.where(racers_lap_times < 130.0)
print(f"Laps indexes less than 130 seconds: {under_130}")


# **Wow, what is that?**
# This looks a little confusing, but the way this is returned, is **one array for each dimension**. So if you **match up each element in the first and second array**, you **get the the first and second indexes**. For instance, **in my execution**, the **first three elements in the 1st array are 0, 0, 0**, and the **first three elements in the second array are 0, 2, 3.** That **means** the **elements at positions (0,0), (0,2) and (0,3) will be less then 130**.
# 
# <span style="color:red">**PLEASE NOTE**</span> that **each time** you **run this Notebook in your environment**, the **numbers generated might be different**, so the **positions with values under 130** might be **different each time**. If you use the same seed value on the generator they should be the same ... but if you end up re-running cells that could change. Either wasy, the **concept is the same though**, and you just need to apply to the numbers you see. 

# In[ ]:


# print the value at position (0,0), (0,2) and (0,3)
print(f"Values at (0,0), (0,2) and (0,3): {racers_lap_times[0][0]}, {racers_lap_times[0][2]}, {racers_lap_times[0][3]}")


# #### <span style="color:blue">OPTIONAL:</span> Flexing our Python skills to create tuples for each location

# If we want to get fancier, we **can use list comprehension** to **create a list of tuples for each location**. We **use** the **[Python zip function](https://docs.python.org/3.3/library/functions.html#zip)** to **group elements** from the **first and second array**. Please bear in mind that this is not a NumPy thing, but just some fancy Python list manipulation.

# In[ ]:


#  use list comprehension to create a list of tuples from the under_130 tuple of arrays
under_130_list = [tuple([x , y]) for x , y in zip(under_130[0], under_130[1])]
print(f"Laps indexes less than 130 seconds:: {under_130_list}")


# Now we can walk nice walk through each position and print all fast laps

# In[ ]:


for position in under_130_list:
    print(f"Lap[{position[0]},{position[1]:2}]: {racers_lap_times[position]} ")


# ## Filtering
# Let's look at how we can **filter an array based on a condition**.

# Once again, let's **use the one dimensional array of Mary Major's laps**.

# In[ ]:


print(f"Mary Major's laps: {mary_laps}")


# But to start out with, I'll use an **even smaller array**, with just her **first 5 laps**.

# In[ ]:


mary_5_laps = mary_laps[:5].copy()
print(f"Mary Major's first 5 laps: {mary_5_laps}")


# ### Using a boolean index list
# At the simplest level, **filtering works** by **passing a list of boolean values**, where **each value** has a **True or False** to **indicate whethe**r an **element** should be **filtered or not.**

# For **example**, let's **filter the array** to **keep only** elements on **indexes 2 and 3**. **In my environment**, that corresponded to **elements between 120 and 140**.
# 
# **PLEASE NOTE** that **in your environment the numbers could change**, in which case, just update the indexes to match your environment.

# In[ ]:


# create a filter for indexes 1 and 3
filter = [False, False, True, True, False]


# Now we can **apply** that **filter** in our array

# In[ ]:


# apply filter to mary_5_laps array
print(mary_5_laps[filter])


# ### Directly creating filter with NumPy
# Although it's good to understand what's hapenning underneath, clearly this is not really practical. But the good news is **NumPy can** automatically **create** those **filters from a condition**.

# Let's **create** a **filter** to **keep only elements between 120 and 140**. **With NumPy**, you **can use a "&"** **as** a **[logical AND operator](https://numpy.org/doc/2.0/reference/generated/numpy.logical_and.html#)**.

# In[ ]:


# create a filter for indexes 1 and 3
filter = (mary_5_laps >= 120) & (mary_5_laps <= 140)
print(f"Filter: {filter}")


# Now we can **apply** that **filter** in our array

# In[ ]:


# apply filter to mary_5_laps array
print(mary_5_laps[filter])


# ### Filtering directly on array
# And now that we've seen each step, we **can** save time and **put** the **condition directly in the array** in one statement.

# In[ ]:


# Print Mary's first 5 laps between 120 and 140
print(mary_5_laps[(mary_5_laps >= 120) & (mary_5_laps <= 140)])


# And now that we don't have to visualize that whole list of True and False, we can **use** that **filter** easily **on all of Mary's laps**.

# In[ ]:


# Print Mary's all laps between 120 and 140
print(mary_laps[(mary_laps >= 120) & (mary_laps <= 140)])


# ### Filtering directly on multi-dimensional array
# **Will this work on a multi-dimensional array? Sure!**
# 
# Let's go **back to** our **original list** with **all** the **racer laps**.

# In[ ]:


# print all racer laps
print(racers_lap_times)


# Earlier we searched for **laps under 130**. Let's **create** a **filtered array** of all such laps.
# 
# First, let's **visualize**  the **multi-dimension filter**, and confirm it will still work the same way.

# In[ ]:


# show filter for laps under 130
print (racers_lap_times < 130)


# So yes, we end up with a **multi-dimensional array of True and False** values **indicating elements that match the condition**. So we can **apply** that **condition directly into our array**, and **get** the **values under 130**.

# In[ ]:


# get the laps under 130 seconds
laps_under_130 = racers_lap_times[racers_lap_times < 130]

# print laps under 130
print(f"Laps under 130:\n {laps_under_130}")


# ### More on searching and filtering ...
# There are **countless other options available for searching and filtering in NumPy**. We can't show everything here, but we'll **see** a few **more indirectly when we look at Pandas** dataframes. **Pandas is based on NumPy**, so the operations supported there are ultimately implemented with NumPy.

# ## Sorting
# We can easily sort NumPy arrays using the **[sort function](https://numpy.org/doc/stable/reference/generated/numpy.sort.html#)**. We'll look at sorting on one and two dimensions.

# ### Sorting in one dimension
# Sorting in one dimensional is simple to understand and visualize.

# In[ ]:


# print all racer laps
print(mary_laps)


# In[ ]:


# sort all of Mary Major's laps
mary_sorted_laps = np.sort(mary_laps)

# print Mary's sorted laps
print(f" Mary Major's sorted laps:\n {mary_sorted_laps}")


# ### Sorting in two dimensions
# **Sorting** in a **two dimensional array** poses a few more questions. Because we **could do any of the following:**
# - **Sort each row**.
# - **Sort each column**.
# - **Sort all the values together**
# 
# **By default**, **NumPy sorts** the **column values in each row**. **But** we'll see that we **can change that**.

# In[ ]:


# print all racer laps
print(racers_lap_times)


# In[ ]:


# sort all race laps row by row
sorted_laps_rows = np.sort(racers_lap_times)

# print sorted laps
print(f"Sorted laps:\n{sorted_laps_rows}")


# #### <span style="color:blue">OPTIONAL:</span> Using the axis parameter to change the sort calculation

# The **sort function has** an **axis parameter** which can be **used to choose how to sort**. The **axis parameter** is **used in various functions in NumPy**, and it **can be hard to understand** sometimes. The way **I like to think of**, is that the **axis parameter** tells **which axis, or array dimension**, is **being manipulated**. **Axis 0 is the first dimension**, and **axis 1 is the second.** 
# 
# The **default behavior** is **shifting column values within the rows**. **So** it's the **2nd dimension, or axis 1**, which is **being moved** around. We can **confirm** that by **calling the function** again **with axis = 1**, and see that we **get** the **same results**.

# In[ ]:


print(np.sort(racers_lap_times, axis = 1))


# **To sort** the **row values withing each column**, we would pass **axis = 0**. So in this case, it would be the first dimension row values that get moved.
# 
# This **doesn't** really **make** a lot of **sense** to do **in our scenarion**, because we would be mixing laps between different racers, **but** it's **worth testing** to **see the behavior**. Look at how each column has row values that increase in ascending order.

# In[ ]:


print(np.sort(racers_lap_times, axis = 0))


# And what if I want to **sort all the values together** in one big list? **axis = None** will do that.

# In[ ]:


print(np.sort(racers_lap_times, axis = None))


# ## Statistical functions
# NumPy has **multiple functions** to support **statistical analysis**. We'll look do a **quick survey of a few of them** here. We'll see more of these calculations with a more interesting example, when we look at the Pandas.
# 
# We'll **continue using** our **racing data**, both the full set of **laps for all racers** (***racers_lap_times***), **laps for Mary Major** (***mary_laps***). We also look up the **list of racer names** based on their **index** (***racers***)

# ### Mean
# The mean, or the average, is the sum of all values divided by the number of values. We **use the [mean function](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#)** for that.

# #### Mean in one dimension
# Let's start with example of calculating the mean of a one dimensional array. We'll use the array with Mary Major's laps.

# In[ ]:


# print mary major's laps
print(f"Mary Major's laps:\n{mary_laps}\n")

# calculate and print the average lap time for Mary Major
result = np.mean(mary_laps)
print(f"Mary Major's average lap time: {result:.3f}")


# #### Mean in multiple dimensions
# You **can also calculate** the **mean on a multi-dimensional array**. Similar to what we saw with sorting, that opens up the **question of whether** we are doing a **mean across one specific dimension**, **or across all values**. We'll see that **by default**, the mean will **apply to all values**, **but** we **can** **use** the **axis parameter** to change the behavior.
# 
# We will used the racers_lap_times two dimensional array.

# In[ ]:


# calculate and print the average lap time for all racers together
result = np.mean(racers_lap_times)
print(f"All racers average lap time: {result:.3f}")


# #### <span style="color:blue">OPTIONAL:</span> Using the axis parameter to change the mean calculation

# **By default** that gave me **all** of the **values averaged out together**. **What if** I **wanted** to get the **average for each racer**? We can **use** the **axis parameter**. Since the **values I want to manipulate** (average out) **are** the **column values**, we need to **pass axis = 1.**
# 
# **In this case**, the **mean function** will **return an array** with the **average for each racer**. I can then iterate through the array. We'll **also look up the racer name** based on the index, to have a really nice output.

# In[ ]:


# calculate and print the average lap time for each racers
result = np.mean(racers_lap_times, axis = 1)

# result will be a list of averages, so we'll iterate to print each racer
for racer_idx, avg in np.ndenumerate(result):
    print(f"{racers[racer_idx]:18} average lap time: {avg:.3f}")


# ### Standard deviation
# Standard deviation measures the spread of data around the mean. It calculates the amount of variation around the mean value. We **use the [std function](https://numpy.org/doc/stable/reference/generated/numpy.std.html)** for that.
# 
# For standard deviation and some of the other functions we **will stick mostly to** the **one dimension** example, since it's **simpler to visualize**. **But the same approach** we **used in** the **mean function** **for multi-dimensional arrays** would **apply here** as well.

# In[ ]:


# print Mary Major lap times
print(f"Mary Major's lap times:\n{mary_laps}\n")

# calculate and print the standard devision of lap times for Mary Major
result = np.std(mary_laps)
print(f"Mary Major's standard deviation of lap times: {result:.3f}")


# ### Min and Max
# **Identifying the minimum and maximum values** are very common, and the are **supported with** the **[min function](https://numpy.org/doc/stable/reference/generated/numpy.min.html)** and **[max function](https://numpy.org/doc/stable/reference/generated/numpy.max.html#)**.
# 
# Usually when you get a max or min value, you also **want to know which element index** they **corresponded to**. The **[argmin](https://numpy.org/doc/stable/reference/generated/numpy.argmin.html)** and **[argmax](https://numpy.org/doc/stable/reference/generated/numpy.argmax.html#)** functions will provide that.

# #### Min and argmin
# We'll do the **min across one dimension**.

# In[ ]:


# print Mary Major lap times
print(f"Mary Major's lap times:\n{mary_laps}\n")

# Identify and print the fastest (minimum) lap time for Mary Major
result = np.min(mary_laps)
print(f"Mary Major's fastest lap time: {result:.3f}")


# We can also **use argmin** to **identify which specific lap was the fastest**

# In[ ]:


# identify index of min value
result = np.argmin(mary_laps)
print(f"Index of Mary Major's fastest lap time: {result}")


# #### Max and argmax
# We'll do a **max across two dimensions**, looking for the **slowest lap across all racers**. **By default**, **with** a **multi-dimensional array** **min and max** will **look at all the values together**, **but** we **could use the axis parameter** to custumize that as we've seen with mean.

# In[ ]:


# print all racer lap times
print(f"All racer lap times:\n{racers_lap_times}\n")

# Identify and print the slowest (maximum) lap time across all racers
result = np.max(racers_lap_times)
print(f"The slowest lap time across all racers: {result:.3f}")


# We can also **use argmax** to **identify which lap was the slowest**

# In[ ]:


# identify index of max value
result = np.argmax(racers_lap_times)
print(f"Index of slowest lap time: {result}")


# **Why** did I get a **single value** (136 in my case), **if this was** a **multi-dimenssional array?** **Because max was calculated across all values**, so the **array was flattened into a single dimension** for that calculation.

# #### <span style="color:blue">OPTIONAL:</span> Using our Python and Math skills to get a nice (row, col) location

# **If** I **want to convert** that single **index value from** the **flattened array** back **into** a **two-demensional indexes**, I just need to **use a little Math**. Since we now the shape of the array, we can derive the row and column index as follows:

# In[ ]:


# get the number of columns of the array from the shape
num_cols = racers_lap_times.shape[1]

# the row index will be the flattened array index divided by num_cols (integer division)
row_idx = result // num_cols

# the column index will be the flattened array index modulo num_cols
col_idx = result % num_cols

print(f"Slowest lap time index: [{row_idx},{col_idx}]")


# If we check in the array, we'll see that's correct.

# ## <span style="color:blue">OPTIONAL:</span> Reading data from external files
# **NumPy** is **at its best** when we are **dealing with large amount of data**, and we're **not likely** to be **creating data by hand**. **Generally** we will be reading data from **data files or a database**. **NumPy offers** a number of **different functions to support** that.

# **For our example**, we will **use** the **[genfromtxt function](https://numpy.org/doc/stable/reference/generated/numpy.genfromtxt.html#)** to **read lap times** for **1000 racers**, and **50 laps**. Not something we would do by hand. **genfromtext** can **read elements from** a **text files** **with** a **specified delimiter**. 

# #### Define the data file name

# In[ ]:


# file name (the "\" works on windows, but might be different in other OSs)
racer_laps_file = r"data\racer_laps.csv"


# #### Read racer laps
# We are using a **CSV file**, so the  **delimiter** will be a  **","**.

# In[ ]:


new_racer_laps = np.genfromtxt(racer_laps_file, delimiter=",")


# #### Print array information
# Let's just **print** some **general information** about the array **using** some of the functions we've seen**, to confirm the reading of the data worked.

# In[ ]:


# print the dimensions and shape
print("----- Shape and Dimension -----")
print(f"Dimensions: {new_racer_laps.ndim}")
print(f"Shape: {new_racer_laps.shape}")

# print the first and last rows
print("\n----- First and Last rows -----")
print(f"First row: {new_racer_laps[0]}")
print(f"Last row: {new_racer_laps[-1]}")

# print the min, max, mean, and standard deviation
print("\n----- Statistics -----")
print(f"Min: {np.min(new_racer_laps):.3f}")
print(f"Max: {np.max(new_racer_laps):.3f}")
print(f"Mean: {np.mean(new_racer_laps):.3f}")
print(f"Standard Deviation: {np.std(new_racer_laps):.3f}")


# We'll **see more examples** of file processing **when** we **look at pandas**.

# ## And more and more and more ...
# At the risk of being repetitive, there are more functions in NumPy than we could possibly show here. Please refer to the [NumPy web site](https://numpy.org/) to dive deeper.

# # Vectorization
# "Vectorization" is a word that has a lot of meanings in IT, Machine Learning, algorithms and Math. In our context, a **vector is a one-dimensional array**, and **vectorization** will refer to **performing operations across all elements** in the array **together, as opposed to** operating on elements **one at a time** in a loop.
# 
# This being a programming course, we will focus strictly on the programming aspect, and not Math theory. **When operating with large arrays of numbers**, a **vectorization approach** will be **far more efficient**.

# ## Vector operations using a Python list
# Let's **start** by **seeing how** we would **operate on vectors** using a **standard Python list** based array.

# ### Create a Python list based array

# In[ ]:


# create a list with 11 numbers
my_list1 = [2, 5, 6, 7, 1, 0, 8, 3, 4, 9, 10]
print(f"my_list1: {my_list1}")


# ### Multiplying by a constant
# Now what do we do if we want to multiply all these numbers by 2?

# In[ ]:


# try multiplying the list by 2
double_list = my_list1 * 2

print(f"double_list: {double_list}")


# That worked ... but **didn't do what we wanted**. If we want to multiply all the numbers in the list, **we'll have to use a loop**.

# In[ ]:


double_list = []
for number in my_list1:
    double_list.append(number * 2)

print(f"double_list: {double_list}")


# ### Adding two arrays
# Now what do we do if we want to add all the corresponding items in two arrays

# In[ ]:


# create a second list with 11 numbers
my_list2 = [8, 5, 4, 3, 9, 10, 2, 7, 6, 1, 0]

# try adding the two lists
summ_list = my_list1 + my_list2

print(f"my_list1: {my_list1}")
print(f"my_list2: {my_list2}")
print(f"\nsumm_list: {summ_list}")


# Again, **not what we wanted**. So once again, we'll **have to use a loop**.

# In[ ]:


summ_list = []
for i in range(len(my_list)):
    summ_list.append(my_list[i] + my_list2[i])

print(f"my_list1: {my_list1}")
print(f"my_list2: {my_list2}")
print(f"\nsumm_list: {summ_list}")


# ## Vector operations using NumPy
# Now let's look at the vectorization approach with NumPy.

# ### Create a NumPy array

# In[ ]:


# create a NumPy array from the same list we used earlier
np_arr1 = np.array(my_list1)
print(f"np_arr1: {np_arr1}")


# ### Multiplying by a constant
# Now what do we do if we want to multiply all these numbers by 2?

# In[ ]:


# try multiplying the list by 2
double_np = np_arr * 2

print(f"double_np: {double_np}")


# That worked the way we wanted. **No loops required!**

# ### Adding two arrays
# Now what do we do if we want to add all the corresponding items in two NumPy arrays

# In[ ]:


# create a NumPy array from the second list we used earlier
np_arr2 = np.array(my_list2)

# try adding the two lists
summ_np = np_arr + np_arr2

print(f"np_arr1: {np_arr1}")
print(f"np_arr2: {np_arr2}")
print(f"\nsumm_np: {summ_np}")


# **Again**,we got what we wanted, **without a loop**.

# ### Other operations
# There are **multiple other operations** which can be **performed on a vector**, including **multiplication, division, and others**. We are not going over all of them, but you can check the NumPy documentations.

# ## Vectorization performance improvement
# We said vectorization would improve performance. Let's test that out.

# ### Define the list size I want to test

# In[ ]:


list_size = 1000000


# ### Create a array of random numbers
# We'll create an **array of random numbers**, represented **both as a list**, **and using NumPy**.

# In[ ]:


# generate a list of random integerss
int_list = []
for i in range(list_size):
    # generate random integer, and add to list
    int_list.append(random.randint(0, 1000000000))

# create a NumPy array from it
int_np = np.array(int_list)

# print first 10 numbers to confirm list looks ok
print(int_list[:10])


# ### Test multiplying by a constant

# In[ ]:


const_val = 17


# #### Test with a Python list based array
# As we saw earlier, **for a Python list**, I'll **need to iterate through** the **array**.

# In[ ]:


# start timer
start_time = time.perf_counter()

# multiply each element in a loop
mult_list = []
for number in int_list:
    mult_list.append(number * const_val)

# stop timer and calculate elapsed time
end_time = time.perf_counter()
list_mult_time = end_time - start_time

# print time
print(f"Multiplication using list based array: {list_mult_time:.6f} seconds")


# #### Test with NumPy Array
# With **NumPy**, it will be a **single call**.

# In[ ]:


# start timer
start_time = time.perf_counter()

# multiply using NumPy multiplication
mult_np = int_np * const_val

# stop timer and calculate elapsed time
end_time = time.perf_counter()
np_mult_time = end_time - start_time

# print time
print(f"Multiplication using NumPy array: {np_mult_time:.6f} seconds")

# Calculate and print improvement factor
perf_factor = list_mult_time / np_mult_time
print(f"\nNumpy was around {perf_factor:.0f} times faster")


# #### Analysis
# **In my runs**, the **NumPy performance** was anywhere between **50 to 150 times faster**.

# ### Test adding two vectors

# #### Create a second set of random numbers

# In[ ]:


int_list2 = []
for i in range(list_size):
    # generate random integer, and add to list
    int_list2.append(random.randint(0, 1000000000))

# create a NumPy array from it
int_np2 = np.array(int_list2)

# print first 10 numbers to confirm list looks ok
print(int_list2[:10])


# #### Test with a Python list based array
# Again, **for a Python list**, I'll **need to iterate through** the **array**.

# In[ ]:


# start timer
start_time = time.perf_counter()

# add each element in a loop
summ_list = []
for i in range(len(int_list2)):
    summ_list.append(int_list[i] + int_list2[i])

# stop timer and calculate elapsed time
end_time = time.perf_counter()
list_add_time = end_time - start_time

# print time
print(f"Addition using list based array: {list_add_time:.6f} seconds")


# #### Test with NumPy Array
# For **NumPy**, just **one call**.

# In[ ]:


# start timer
start_time = time.perf_counter()

# add using NumPy addition
summ_np = int_np + int_np2

# stop timer and calculate elapsed time
end_time = time.perf_counter()
np_add_time = end_time - start_time

# print time
print(f"Multiplication using NumPy array: {np_add_time:.6f} seconds")

# Calculate and print improvement factor
perf_factor = list_add_time / np_add_time
print(f"\nNumpy was around {perf_factor:.0f} times faster")


# #### Analysis
# **In my runs**, the **NumPy performance** was anywhere between **75 to 175 times faster**.
