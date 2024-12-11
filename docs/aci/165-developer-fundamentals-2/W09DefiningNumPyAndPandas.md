# Defining NumPy and Pandas

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to repo's main [README.md](../../../README.md)

## NumPy

### Manipulations on Arrays

#### Iteration with np.nditer()

The **nditer** method is particularly useful when you must perform element-wise operations on arrays, because it allows you to access and manipulate each element individually. It also provides various options to control the iteration order, data types, and other aspects of the iteration process.

### Searching arrays

#### .where(variable == x)

### Performing data analysis

* The **mean**, or the average, is the sum of all values divided by the number of values.
* The **median** is the middle value in a dataset ranging from least to greatest. The median is a true measure of central tendency in a dataset because it is not influenced by extreme values.
* **Standard deviation** measures the spread of data around the mean. It calculates the amount of variation around the mean value.

* **Mean**    **np.mean(data)**
* **Median**    **np.median(data)**
* **Standard deviation**    **np.std(data)**

### Replacing missing values with a specific value

* Replace values with zero    **new_data = np.nan_to_num(data,nan=0)**
* Drop rows    **new_data = data[~np.isnan(data).any(axis=1)]**
* Drop columns    **new_data = data[: , ~np.isnan(data).any(axis=0)]**

### [Data Processing with NumPy and Pandas](./W09Lab1NumPyPandas.md)
