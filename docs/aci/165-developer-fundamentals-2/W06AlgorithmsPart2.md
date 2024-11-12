# Algorithms Part 2

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to repo's main [README.md](../../../README.md)

## Sorting Algorithms

### Pre-assessment

#### Which sorting algorithm is relatively straightforward to understand and implement and provides a foundation to learn more advanced sorting algorithms?

* Bubble sort

Wrong answers:

* Quick sort
* Selection sort
* Merge sort

Bubble sort is relatively straightforward to understand and implement. However, because of low efficiency with larger data sets it is not often used. Yet, it is still introduced to new learners to help them understand the process of sorting in computation.

#### Which scenario guarantees the performance level of the algorithm will NOT drop below a certain level?

* Worst-case scenario

Wrong answers:

* Best-case scenario
* Average-case scenario
* Amortized-case scenario

The worst-case scenario guarantees the performance level won't drop below a certain level. The worst-case scenario occurs when the algorithm faces the most challenging input or condition.

#### What is the term for the time complexity when the algorithm's runtime remains constant and does NOT depend on the size of the input?

* Constant time complexity

Wrong answers:

* Linear time complexity
* Exponential time complexity
* Quadratic time complexity

In constant time complexity, even with the increase in the input, the time taken to complete the task is constant. The algorithm with constant time complexity is considered the most efficient and fastest of all.

### What is Sorting?

**Sorting** is the process of arranging items in a specific order. Libraries use sorting extensively to organize books. A library employs sorting to arrange books alphabetically by author, title, or subject. This helps library visitors to conveniently locate the books they are looking for. Imagine you walk into a library and want to find a book on a specific topic. Without sorting, finding a specific book would be very challenging.

In computer science, sorting puts elements of a list into a specified order. The most frequently used orders are ascending or descending. Efficient sorting is important for optimizing the efficiency of other algorithms that require input data to be in sorted lists.

### Sorting requirements

The output of any sorting algorithm must satisfy the following conditions: 

* Sorting must be done as per the prescribed order.
* The number of elements in the input and the number of elements in the output must be equal.

### Sorting Algorithms and Their Benefits

### Sorting algorithms

A sorting algorithm is a sequence of steps that sorts the elements in a list in the desired order. There are many different ways to sort a list, which is why there are different sorting algorithms. The following sorting algorithms will be covered in this topic: 

* Bubble sort
* Selection sort
* Insertion sort
* Merge sort
* Quicksort

### Benefits of sorting algorithms

There are four main purposes for using sorting algorithms when you are writing code. They are as follows:

* **Searching:** Searching for an item in the list is much more convenient and efficient when the list is sorted.
* **Selection:** Sorting helps you quickly select items from a list.
* **Finding duplicates:** Sorting helps to find duplicate entries in a list.
* **Analyzing distribution:** Analyzing the frequency distribution of items is more convenient when the list is sorted.

### Benefits of sorting with real-life examples

#### Searching

Finding a book in the library becomes more convenient because the books are sorted first by genre or theme, and then alphabetically.

#### Selection

A teacher can conveniently identify the highest or lowest scorer on a test if the answer sheets are sorted in ascending or descending order by score.

#### Finding duplicates

Sorting makes it more convenient to find out how many students in the class have the same name.

#### Analyzing distribution

Sorting students in the class according to their favorite subject helps to analyze how many students prefer one subject over another subject.

### Knowledge Check

#### What is the primary purpose of sorting algorithms in computation?

* Facilitating efficient searching and selection

Wrong answers:

* Enhancing code readability
* Optimizing memory allocation
* Minimizing code complexity

Sorting algorithms are used to organize data in a specific order, making it more convenient to search for items and quickly select them from the sorted list.

#### Which benefit does sorting provide for analyzing the frequency distribution of items?

* Convenient identification of repeated entries

Wrong answers:

* Improved code performance
* Enhanced code maintainability
* Streamlined code debugging

Sorting facilitates the identification of repeated entries in a list of items.

#### Which requirements must be fulfilled during the sorting process? (Select TWO.)

* The number of elements in the input and output must be equal.
* Sorting must be done as per the prescribed order.

Wrong answers:

* The number of elements in the output must be greater than those in the input.
* Sorting must be done using for-loops.
* The number of elements in the output must be less than those in the input.

This ensures that the sorting process does not alter the number of elements and orders those elements as specified.

### Summary

* Describe the characteristics of sorting.
* Identify the two conditions of sorted output.
* Describe the benefits of sorting.

## Built-in sorting algorithms

There are two built-in algorithms for sorting in Python. These algorithms are **sort()** and **sorted()**.

### The sort() method

The characteristics of the sort() method are as follows:

* sort() is a method in the list class in Python.
* sort() is used to sort the elements in the list.
* sort() sorts the list in place, so it modifies the original list.
* sort() returns None, because it modifies the original list.

#### Sorting in reverse order

sort(reverse=True)

#### Sorting by length

sort(key=len)

The **sort()** method can accept an optional **key** parameter to specify how to sort the elements in the list. You can pass in a function like the **len()** function that is used in this example with **key=len**. The function specified as the key will be called on each element in the list, and the value returned from the function will be used to compare and sort the elements. In this case, the string lengths returned from calling **len()** on each element are being used as the sort key to compare and sort the strings.

### The sorted() function

The characteristics of the sorted() function are as follows:

* sorted() is a built-in function in Python.
* sorted() is used for sorting any iterable, such as lists, tuples, and strings.
* sorted() creates a new list. It does not modify the original iterable.
* sorted() returns the new sorted **list** even the input is tuples or strings.

#### Sorting with lambdas

In case you're needing to sort by two keys: First, you need to sort the strings by their length, and then by alphabetical order if the string lengths are equal. The **key** parameter can only accept one function argument.

You can use a lambda function as your key. This allows you to write a custom function that returns one or more custom values to sort by, such as both string length and alphabetical order

```
string_list = ["apple", "orange", "banana", "grape", "kiwi"]
print("Input list of strings before sorting:")
print(string_list)

# Sorting the list using sorted function with a lambda function
sorted_strings = sorted(string_list, key=lambda x: (len(x), x))
print("Sorted list of strings based on their length:")
print(sorted_strings)
```

Expected output

```
Input list of strings before sorting:
['apple', 'orange', 'banana', 'grape', 'kiwi']

Sorted list of strings based on their length:
['kiwi', 'apple', 'grape', 'banana', 'orange']
```

Notice that the strings for "orange" and "banana" each have the same length of six characters. However, the lambda function sorts "banana" before "orange" because "banana" comes before "orange" in alphabetical order.

Unlike the sort() method, which can only be called on lists, the sorted() method can be called on any iterable. This includes calling it directly on strings.

### Knowledge Check

#### What is the purpose of the Python list sort() method? 

* To sort elements in place

Wrong answers:

* To create a new list
* To modify the original iterable
* To return a new sorted list

The **sort()** method is used to sort the elements in the list in place, which means it modifies the original list.

#### What value does the sort() method return after sorting the elements in the list?

* None

Wrong answers:

* New sorted list
* Original list
* Length of the list

The **sort()** method modifies the original list in place and returns **None**.

#### Which of the following statements is true?

* The sorted() function creates a new list.

Wrong answers:

* The sort() method creates a new list.
* The sorted() function modifies the original list.
* The sorted() function returns nothing.

The **sorted()** function creates a new list from an iterable, and it returns the new sorted list.

### Summary

* Describe the Python **sort()** method and its application for sorting data.
* Describe the Python **sorted()** function and its usage for sorting data.
* Identify the differences between the **sort()** method and the **sorted()** function.

## Importance of algorithm analysis

The goal of algorithm analysis is to forecast the performance of an algorithm without the need for actual implementation. Predicting the precise behavior of an algorithm is challenging due to various influencing factors. However, algorithm analysis can help to predict the approximate behavior of an algorithm.

Algorithm analysis provides two primary benefits:

* Firstly, when you focus on prediction rather than running the algorithm for every conceivable input type and size, it conserves time and effort. This approach avoids the necessity of implementing the algorithm each time you modify the input.
* Secondly, algorithm analysis empowers you to make informed decisions regarding which algorithm to use in a particular problem-solving scenario.

For analyzing the algorithm, you conduct a performance analysis based on external and internal factors.

### External Factors

In the analysis of external factors, elements to consider include response time, throughput, resource utilization, the efficiency of the compiler, and the overall effectiveness of the system. The outcome of this evaluation depends on how well the system can run the algorithm. External factors are variables influenced by machine configurations and the proficiency of compilers.

External factors can change based on how the machine is set up and how good the compiler is at its job. Considering external factors means checking how well the whole computer setup works with the algorithm to get the job done.  

### Internal Factors

Internal factors examine how much time and space an algorithm needs to get a job done. 

1. **Time complexity:** This is about figuring out how fast the algorithm can complete its task. You want to know how many operations it needs to complete and how long each operation takes.
2. **Space complexity:** This is about understanding how much memory (space) the algorithm requires while it's performing its task. You want to know how efficiently it uses computer memory.

The internal analysis examines the algorithm itself. You're not thinking about the outside world or the computer it's running on; you're just focused on the algorithm's characteristics. It's a bit like looking at how well a car engine runs without considering the road or traffic—it's all about what's happening inside the engine.

### Complexity analysis

#### Time complexity

Time complexity estimates the amount of time an algorithm takes to complete as the input size grows bigger.

#### Space complexity

Space complexity estimates the amount of memory an algorithm takes to complete as the input size grows bigger.

Both time and space complexities are often expressed using Big-O notation.

These complexities are used to describe the performance of an algorithm under different conditions, or scenarios.

The following are three different scenarios to consider when analyzing time and space complexities:

* Best case
* Worst case
* Average case

### Best, worst, and average case example

#### Best Case

The best-case scenario refers to the minimum amount of resources (in terms of time and space) that an algorithm requires to solve a problem under ideal conditions. It represents the most favorable input for the algorithm, where it performs optimally. Best-case time complexity provides a lower bound on the algorithm's efficiency.

#### Worst Case

The worst-case scenario represents the maximum amount of resources an algorithm might need to solve a problem. It occurs when the algorithm faces the most challenging input or condition. Worst-case time complexity provides an upper bound on the algorithm's efficiency.

#### Average Case

The average-case scenario considers the expected performance of an algorithm when applied to a random or typical input. It provides a more realistic measure of efficiency than best-case or worst-case alone. Average-case time complexity is often more complex to analyze and might involve probabilities.

### Computational example

Take the linear search algorithm as an example, where the task is to find a particular element within an unsorted array.

Consider the array: [2, 7, 6, 5, 8, 9, 3].

In the **worst-case scenario**, searching for the target 3 would be the most time-consuming, given it is placed at the end of the array. Every single element in the array must be checked before finding the target.

Conversely, the **best-case scenario** occurs when the target is 2, which is positioned at the beginning of the array. Only one element had to be checked before finding the target.

For the **average case**, imagine searching for the target 5, which is in the middle of the array. About half of the elements must be checked before finding the target.

When describing the time complexity of an algorithm, it usually means the worst-case scenario. This is because the worst-case scenario guarantees that the time required to complete the function will not be more than the worst case. This way, you know that the performance of the algorithm won't drop below a certain level.

### Knowledge Check

#### What are the two main advantages of algorithm analysis?

* Save time and effort during implementation and make informed algorithmic choices.

Wrong answers:

* Save time and effort during implementation and improve system proficiency.
* Predict exact algorithm behavior and make informed algorithmic choices.
* Improve the proficiency of the system and analyze internal factors affecting performance.

An algorithm analysis helps save time and effort during actual implementation. It also assists in making informed decisions about which algorithm to use in a particular problem-solving scenario.

#### What is the best-case scenario in terms of algorithm complexity analysis?

* The algorithm performs optimally.

Wrong answers:

* The algorithm faces the most challenging input.
* The algorithm's efficiency provides an upper bound.
* The algorithm's efficiency is more realistic.

The best-case scenario refers to the minimum number of resources, in terms of time and space, that an algorithm requires to solve a problem under ideal conditions. It represents the most favorable input for the algorithm, where it performs optimally.

#### During the performance analysis of an algorithm, the team evaluates the response time, throughput, and overall effectiveness of the system. Which aspect of algorithm analysis is this focusing on?

* External factors

Wrong answers:

* Internal factors
* Time complexity
* Space complexity

The team is focusing on external factors because they are assessing elements such as response time, throughput, and overall system effectiveness. These factors are influenced by machine configurations and the proficiency of compilers, making them external to the inherent characteristics of the algorithm itself.

### Summary

* Identify the internal and external factors that influence the performance of algorithms.
* Understand time and space complexities to evaluate algorithm efficiency.
* Understand the best-case, worst-case, and average-case scenarios for analyzing time and space complexities.

## Big O Notation

### What is Big O notation?

The time and space complexity of an algorithm is expressed by **Big O** notation.  

Big **Omega (Ω)** describes the lower bound or the best-case performance, and **Big Theta (Ɵ)** describes the average-case performance of an algorithm in terms of its input size.

Big O notation is a mathematical notation to describe the upper bound or worst-case performance of an algorithm in terms of its input size. In basic terms, Big O notation provides a mathematical formula to measure the time and space complexity of an algorithm. Different algorithms with the same growth rate will be represented as the same Big O notation.  

In mathematics, Big O notation expresses how the size of a mathematical function behaves as the input grows. Imagine there are two mathematical functions, **f(x)** and **g(x)**, and you want to see how fast their runtimes grow as the value of x increases.  

Big O notation is an asymptotic notation that gives you the extent to which a value (runtime or space) grows as the input size approaches infinity.

### Common time complexities

This module focuses on the most common time complexities. The following are some common time complexities expressed using Big O notation.

| Time Complexities | Big O Notation |
| ----------------- | -------------- |
| Constant | O(1) |
| Logarithmic | O(log n) |
| Linear | O(n) |
| Quasilinear | O(n log n) |
| Quadratic | O(n^2) |
| Exponential | O(2^n) |
| Factorial | O(n!) |

### Constant time complexity: O(1)

When the algorithm's runtime does not depend on the size of the input, it is called constant time complexity, or O(1). The runtime remains the same, no matter the size of the input.

#### Constant time complexity example

Assume you are playing a card game and you have to pick the first card from the deck. It doesn't matter how small or big the deck is. The time required to pick the first card will always be constant because you only have to pick the first card.

So, the process of picking the first card from the deck (no matter the size of the deck) has a time complexity of O(1).

#### Mathematical expression

Mathematically, constant time complexity is expressed as the following: 

**f(n) = O(1)**

where:

* **f(n)** represents the function that describes the algorithm's time and space complexity.
* **O(1)** indicates that the complexity of the algorithm is constant.

If an algorithm has a time complexity of O(1), it means that the time it takes to complete remains constant even if the input size (n) grows.

#### Code example

The following Python code shows the first element of a list being printed.

```
my_list = [10, 20, 30, 40, 50] 

# Print the first element 
print("The first element of the list is:", my_list[0]) 
```

Expected output:

``
The first element of the list is: 10
``

In this example, the list **my_list** contains five items. However, even if **my_list** contains millions of items, the time it takes to access the first element will always be constant.

**Note:** Constant time complexity is considered the most efficient type of time complexity because the runtime is independent of the input size. However, this time complexity is difficult to achieve when solving real-world problems.

### Logarithmic time complexity: O(log n)

Algorithms with logarithmic time complexity, O (log n), reduce the size of the input with each step. These types of algorithms repeatedly divide the problem into smaller subproblems and discard half of the search space with each step. Binary search is an example of an algorithm with logarithmic time complexity.

#### Logarithmic time complexity example

Imagine you are playing a number-guessing game with a friend. You ask your friend to choose a number from a sorted list of 10 numbers. Your friend starts guessing by asking you if the number is higher or lower than the median number. If the number lies in the first half of the list, that means she eliminates the entire second half of the list. She does the same with the remaining portion of the list and comes up with an answer in just a few iterations or operations.

This is what exactly happens in a binary search.

#### Mathematical expression

Mathematically, logarithmic time complexity is expressed as the following: 

**f(n) = O(log n)**

where:

* **f(n)** represents the function that describes the algorithm's time and space complexity. 
* **O(log n)** indicates that the complexity of the algorithm grows logarithmically with the input size n.

If an algorithm has a time complexity of **O(log n)**, it means that the time it takes to complete increases logarithmically as the input size (n) grows.

#### Code example

The following basic Python code example demonstrates logarithmic time complexity using a recursive binary search algorithm.

```
def binary_search(sorted_list, target, low, high):

    if low <= high: 

        mid = (low + high) // 2  # Calculate the middle index 
 
        if sorted_list[mid] == target: 
            return mid  # Found the target, return its index 

        elif sorted_list[mid] < target: 
            return binary_search(sorted_list, target, mid + 1, high)  # Search in the right half 

        else: 
            return binary_search(sorted_list, target, low, mid - 1)  # Search in the left half 
  
    return -1  # Target not found in the list 

  
# Example usage: 
sorted_numbers = [1, 5, 8, 9, 16, 23, 28, 33, 46, 65] 
target_number = 28 

 
result = binary_search(sorted_numbers, target_number, 0, len(sorted_numbers) - 1) 

if result != -1: 
    print(f"Target {target_number} found at index {result}") 

else: 
    print(f"Target {target_number} not found in the list")
```

Expected output:

```
Target 28 found at index 6
```

#### Code explanation

The function **binary_search** performs a recursive binary search.

* It takes the sorted list and the target number. It starts to search the whole list from 0 to n-1.
* It then checks if **low** is less than or equal to **high**. If it is, the function can proceed. But if **low** is greater than **high**, the target has not been found in the list and the function returns -1.
* If the middle element is equal to the target, it returns the index.
* If the middle element is less than the target, it recursively searches in the right half of the list. This is where elements greater than the current middle element, possibly including the target, could still be found.  
* If the middle element is greater than the target, it recursively searches in the left half of the list.

This recursive binary search demonstrates logarithmic time complexity because, with each recursive call, the search space is divided in half. This leads to logarithmic growth in the time taken to complete the task as the size of the input increases.

**Note:** An algorithm with a time complexity of **O(log n)** is the second-best option because the algorithm eliminates half of the input size at every step. This makes the algorithm very efficient. However, it is less efficient than an algorithm with a constant time complexity.

### Linear time complexity: O(n)

In the linear time complexity, the algorithm's runtime grows linearly with the size of the input. Here, the algorithm examines all values in the input data.

#### Linear time complexity example

Consider an example where there are around 50 books on a bookshelf, and you are asked to write the title of every book on a piece of paper. How long will it take you to write the titles? Now assume there are 100 books on the bookshelf instead of 50. It will probably take you about twice as long to write down the names of 100 books. Linear time complexity is when the number of steps to complete an algorithm scales in a one-to-one relationship with the size of the input.

#### Mathematical expression

Mathematically, linear time complexity is expressed as the following:  

**f(n) = O(n)** 

where:

* **f(n)** represents the function that describes the algorithm's time and space complexity.
* **O(n)** indicates that the complexity of the algorithm grows linearly with the input size n.

If an algorithm has a time complexity of **O(n)**, it means that the time it takes to complete increases linearly as the input size **(n)** grows.

#### Code example

The following is a basic Python code example with a function that sums up all the elements in a list.  

```
def sum_elements(my_list):
    total = 0

    for element in my_list:
        total += element
    return total

# Example usage:
numbers = [1, 2, 3, 4, 5]
result = sum_elements(numbers)
print(f"The sum of the elements is: {result}")
```

Expected output:

```
The sum of the elements is: 15
```

#### Code explanation

In this example, the **sum_elements** function takes a list of numbers as input.

* It uses a for loop to iterate through each element in the list.
* For each element, it adds the element to a running total
* Finally, it returns the total sum of all elements in the list.

The time complexity of this function is linear, or **O(n)**, because the number of iterations through the loop is directly proportional to the size of the input list. If the list has 10 elements, it will perform 10 additions; if the list has 100 elements, it will perform 100 additions. The time it takes to compute the sum increases linearly with the size of the input list.

**Note:** An algorithm with a time complexity of **O(1)** or **O(log n)** is more efficient than an algorithm with linear time complexity, or **O(n)**.

### Quasilinear time complexity: O(n log n) 

Quasilinear time complexity involves a combination of linear and logarithmic operations. Quasilinear time complexity involves a logarithmic factor that makes it slower compared to linear or logarithmic complexity.

#### Quasilinear time complexity example

Consider an example where there are around 50 books on a bookshelf, and you are asked to write the titles of all the books on a piece of paper. How much time would it take? It will take even more time if you are asked to write them down in alphabetical order. One way to approach this would be to sort the books alphabetically and then write the titles down. This quasilinear process involves extra steps beyond the linear process of writing down the titles. 

#### Mathematical expression

Mathematically, quasilinear time complexity is expressed as the following:  

**f(n) = O(n log n)**

where:

* **f(n)** represents the function that describes the algorithm's time and space complexity.
* **O(n log n)** indicates that the complexity of the algorithm grows quasilinearly with the input size n.

If an algorithm has a time complexity of **O(n log n)**, it means that the time it takes to complete increases quasilinearly as the input size **(n)** grows.

#### Code example

The following is a Python code example where the list of elements is sorted in ascending order using Python's built-in sorted() function.

```
def quasilinear_sort(input_list):

    # Sorting the list using Python's built-in sorting algorithm 
    sorted_list = sorted(input_list) 
    return sorted_list 

# Example usage 
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5] 
sorted_result = quasilinear_sort(my_list) 

print("Original List:", my_list) 
print("Sorted List:", sorted_result) 
```

Expected output:

```
Original List: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
Sorted List: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
```

#### Code explanation

In this example, **sorted()** is a built-in function in Python that typically uses a sorting algorithm with **O(n log n)** time complexity.

The input list **my_list** is sorted in ascending order.

* In Python, both the built-in list **sort()** method and **sorted()** function use Timsort as their default sorting algorithm. Timsort is a hybrid sorting algorithm that combines two other popular algorithms: merge sort and insertion sort. This combination makes Timsort highly adaptable and efficient in handling different types of datasets.

**Note:** Quasilinear time complexity is less efficient than linear time complexity. However, quasilinear time complexity is considered to be efficient for very complex tasks. A good example of an algorithm with quasilinear time complexity is merge sort.

### Quadratic time complexity: O(n^2)

In quadratic time complexity, the algorithm takes time, proportional to the square of the input size, to complete a task. An algorithm has a quadratic time complexity when it needs to perform a linear time operation for each value in the input data. Bubble sort is a good example of an algorithm with quadratic time complexity.

#### Quadratic time complexity example

Consider an example where a group of five friends decides to organize a gift exchange event. Every friend should gift every other person in the group something handcrafted for the event. They also decide that the gift should take approximately two hours to craft and package. Can you count how many hours it would take to complete this project? What if instead of five friends, there are 50 friends? How much time would it take? The relationship between the number of friends (n) and the total time required is quadratic because each friend contributes to the creation of gifts for every other friend. Here the quadratic equation will be as follows:

Total time = 2*(n*(n-1)/2), which simplifies to n^2-n.

#### Mathematical expression

Mathematically, quadratic time complexity is expressed as the following: 

**f(n) = O(n^2)**

where:

* **f(n)** represents the function that describes the algorithm's time and space complexity.
* **O(n^2)** indicates that the complexity of the algorithm grows quadratically with the input size n.

If an algorithm has a time complexity of **O(n^2)**, it means that the time it takes to complete increases quadratically as the input size **(n)** grows.

#### Code example

The following Python code illustrates the example of five friends organizing a gift exchange.

```
def calculate_total_time(num_friends):
    total_time = 0

    for i in range(num_friends): 
        for j in range(num_friends - 1): 
            # Assuming 2 hours per pair for crafting and packaging 
            total_time += 2 
    return total_time 
  
# Example usage with 5 friends 
num_friends = 5 
total_time = calculate_total_time(num_friends) 

print(f"With {num_friends} friends, the total time required is: {total_time} hours")
```

Expected output:

```
With 5 friends, the total time required is: 40 hours
```

#### Code explanation

The code illustrates how the runtime of an algorithm can scale quadratically with the size of the input.

* The **calculate_total_time** function takes the number of friends **(num_friends)** as an argument.
* It initializes a variable **total_time** to store the cumulative time required for crafting and packaging.
* It uses nested loops to iterate through pairs of friends. The outer loop **(i)** represents one friend, and the inner loop **(j)** represents every other friend after the current friend.
* It increments **total_time** by 2 hours for each pair, assuming it takes 2 hours to craft and package a gift.

This code illustrates quadratic time complexity, or **O(n^2)**, because the total time required grows quadratically with the number of friends. The nested loops consider each pair of friends, leading to a quadratic relationship between the input size (number of friends) and the total time.

### Exponential time complexity: O(2^n)

An algorithm has an exponential time complexity when the time required to complete the task grows exponentially with each addition to the input data set.

#### Exponential time complexity example

Imagine a scenario where a computer virus spreads from device to device, and each infected computer has the potential to infect multiple others. The number of new devices affected on each day is proportional to the number of existing devices with the virus. This leads to exponential growth in the number of infected devices. On day 1, one computer is infected. On day 2, each infected computer infects three new computers. On day 3, each of the newly infected computers from the previous day infect three more computers, and so on. The number of infected computers on each day follows an exponential growth pattern. If you plot the number of infected devices over time, you'll see an exponential curve.

#### Mathematical expression

Mathematically, exponential time complexity is expressed as the following:  

**f(n) = O(2^n)**

where:

* **f(n)** represents the function that describes the algorithm's time and space complexity. 
* **O(2^n)** indicates that the complexity of the algorithm grows exponentially with the input size n.

If an algorithm has a time complexity of **O(2^n)**, it means that the time it takes to complete increases exponentially as the input size **(n)** grows.

#### Code example

The following Python code is for an algorithm with exponential time complexity, specifically dealing with recursively calculating the power of a number. The algorithm adopts a basic recursive method.

```
def get_infected_count(number_of_devices: int, call_count: int = 0) -> 'Tuple[int, int]':
    """
    Params:
    - number_of_devices(int): number of infected computers
    - call_count(int): call count
    Returns:
    - Tuple[int, int]: (infected count, total function call count)
    """
    call_count += 1
    if number_of_devices == 1:
        return (3, call_count)
    infected, count = get_infected_count(number_of_devices - 1, call_count)
    return (infected + 3, count)

def get_affected_count(days: int = 1, initial_affected_count: int = 1) -> 'Tuple[int, int]':
    """
    Params:
    - days(int): number of days
    - initial_affected_count(int): initial count of infected computers
    Returns:
    - Tuple[int, int]: (affected count, total function call count)
    """
    affected_count: int = initial_affected_count
    call_count: int = 0
    for _ in range(days):
        infected, count = get_infected_count(affected_count)
        affected_count += infected
        call_count += count

    return (affected_count, call_count)

print(get_affected_count())
print(get_affected_count(days=2))
print(get_affected_count(days=3))
print(get_affected_count(days=4))
print(get_affected_count(days=5))
# RecursionError: maximum recursion depth exceeded in comparison
# print(get_affected_count(days=10))
```

Expected output:

```
(4, 1)
(16, 5)
(64, 21)
(256, 85)
(1024, 341)
```

#### Code explanation

This code illustrates the use of recursion to calculate an exponent and has exponential time complexity.

* The function **get_infected_count** is a recursive function that describes the spread of a computer virus. It also tracks the number of function calls completed during recursion.
* The function **get_affected_count** is a function that calculates the total number of devices infected over a specified period of days. It also returns the total number of function calls that were performed and uses **get_infected_count** as a helper function.
* By default, it is assumed that one computer will infect three other devices per day.
* When you run the code, the exponential growth in the infected devices is evident.

**Note:** An algorithm with exponential time complexity is highly inefficient. It is not feasible in most scenarios to use this kind of algorithm with bigger input sizes.

### Factorial time complexity: O(n!)

An algorithm has a factorial time complexity when its runtime grows factorially based on the size of the input data.

#### Factorial example

Imagine you have four friends—Mary, Paulo, Diego, and Wei—and you want to arrange them in a line for a team photo. How many ways can you arrange them? You can arrange them in 4! or 4*3*2*1 = 24 different ways. The time complexity of generating all possible arrangements in this scenario is factorial. If you have five friends, the ways that you can arrange them increases to 5! or 5*4*3*2*1 = 120. If you have six friends, this jumps to 6! or 6*5*4*3*2*1 = 720 possible arrangements. The jump in the number of possible arrangements from 24, 120, and 720, as the number of friends increases from four, five, and six, illustrates the rapid growth of factorials.

#### Mathematical expression

Mathematically, factorial time complexity is expressed as the following: 

**f(n) = O(n!)** 

where:

* **f(n)** represents the function that describes the algorithm's time and space complexity. 
* **O(n!)** indicates that the complexity of the algorithm grows factorially with the input size n.

If an algorithm has a time complexity of **O(n!)**, it means that the time it takes to complete increases factorially as the input size **n** grows.

#### Code example

The following Python code is for an algorithm that involves generating all permutations of a set of elements using a recursive approach.

```
def generate_permutations(elements, current_permutation=[]):

    if not elements: 
        print(current_permutation) 
    else: 
        for i in range(len(elements)): 
            remaining_elements = elements[:i] + elements[i + 1:] 
            generate_permutations(remaining_elements, current_permutation + [elements[i]]) 
  
# Example: Generate all permutations of a small set 
elements = ['A', 'B', 'C'] 
generate_permutations(elements) 
```

Expected output:

```
['A', 'B', 'C']
['A', 'C', 'B']
['B', 'A', 'C']
['B', 'C', 'A']
['C', 'A', 'B']
['C', 'B', 'A']
```

#### Code explanation

The **generate_permutations** function recursively generates all permutations of a given set of elements.

* The base case is when there are no more elements to consider. At this point, it prints the current permutation.
* The function is called with an initial empty **current_permutation** list.
* When you run this code with the example set ['A', 'B', 'C'], it will print all possible permutations of the elements.

The number of permutations grows factorially with the number of elements, illustrating a factorial time complexity.

**Note:** An algorithm with factorial time complexity has the worst efficiency of all and is nearly impossible to use in real-world scenarios.

### Comparing Time Complexities

| Time complexity | Big O notation | Example | Efficiency |
| --------------- | -------------- | ------- | ---------- |
| Constant | O(1) | Accessing elements in an array by index | Excellent |
| Logarithmic | O(log n) | Binary search in a sorted list | Good |
| Linear | O(n) | Iterating through the elements in the list, such as adding all the elements in the list | Fair |
| Quasilinear | O(n log n) | Merge sort | Considerable |
| Quadratic | O(n^2) | Bubble sort | Bad |
| Exponential | O(2^n) | Recursive algorithm | Worse |
| Factorial | O(n!) | Permutations | Worst |

Algorithms with quadratic, exponential, or factorial time complexities are poorly performing algorithms and should not be considered for practical purposes.

### Space Complexity

**Space complexity** estimates the amount of memory space an algorithm takes to complete as the input size grows bigger. When an algorithm solves a problem, it uses the memory for the following:

* Input variables and constants
* Program instructions
* Running the program

The space required by the algorithm for program instructions and running the program is called the **auxiliary space**.

The space complexity includes both the input size, which consists of input variables and constants, and the auxiliary space.

Space complexity is a parallel concept to time complexity. The types of space complexities are similar to those of time complexities. The upper bound of space complexities is expressed by Big O notation.

The following table and graph summarize and compare the common space complexities.

| Space complexity | Big-O notation | Description | Efficiency |
| ---------------- | -------------- | ----------- | ---------- |
| Constant time complexity | O(1) | The space used by the algorithm remains constant regardless of the input size. | Excellent |
| Logarithmic time complexity | O(log n) | The space used by the algorithm grows logarithmically with the size of the input. | Good |
| Linear time complexity | O(n) | The space used by the algorithm grows linearly with the size of the input. | Fair |
| Quasilinear time complexity | O(n log n) | The space used by the algorithm grows quasi-linearly with the size of the input. | Considerable |
| Quadratic time complexity | O(n^2) | The space used by the algorithm grows quadratically with the size of the input. | Bad |
| Exponential time complexity | O(2^n) | The space used by the algorithm grows exponentially with the size of the input. | Worst |

### Factors affecting the significance of space complexity

#### Abundant memory

Today's computers typically have large amounts of memory, compared to earlier times. As a result, algorithms with moderate space complexities might work just as well and won't pose any significant challenge.

#### Advanced hardware

Improvements in hardware technology, such as faster processors and larger memory capacities, have mitigated the impact of space complexity in many cases. This allows for more liberal use of memory without sacrificing overall system performance. 

#### Reduced memory cost

The cost of memory has decreased significantly over time, making it more economically feasible to use additional memory if it improves the efficiency of an algorithm.

### Knowledge Check

#### Recursive binary search is an example of which time complexity?

* Logarithmic

Wrong answers:

* Constant
* Linear
* Quasilinear

The recursive binary search demonstrates logarithmic time complexity. With each recursive call, the search space is divided in half. This leads to logarithmic growth in the time taken to complete the task as the size of the input increases.

#### Which of the following statements are true? (Select TWO.)

* The built-in sorted() function in Python has a quasilinear time complexity.
* The space required by the algorithm for program instructions and running the program is called the auxiliary space.

Wrong answers:

* An algorithm with quasilinear time complexity is more efficient than one with linear time complexity.
* A function that sums up the elements in the list is an example of logarithmic time complexity.
* The space required by the algorithm to store input variables and constants is called the auxiliary space.

#### ich of the following has all the correct pairs of time complexities and their Big O notations?

* Constant- O(1); Logarithmic- O(log n); Linear- O(n); Quasilinear- O(n log n); Quadratic- O(n^2); Exponential- O(2^n); Factorial- O(n!)

Wrong answers:

* Constant- O(1); Logarithmic- O(n log n); Linear- O(n); Quasilinear- O(log n); Quadratic- O(n^2); Exponential-O(2^n); Factorial- O(n!)
* Constant- O(1); Logarithmic- O(n log n); Linear- O(n); Quasilinear- O(log n); Quadratic- O(2^n); Exponential-O(n^2); Factorial- O(n!)
* Constant- O(1); Logarithmic- O(log n); Linear- O(n); Quasilinear- O(n log n); Quadratic- O(2^n); Exponential- O(n^2); Factorial- O(n!)

### Summary

* Understand the Big O notations associated with common time and space complexities.
* Learn detailed examples that illustrate common time and space complexities.
* Compare various time and space complexities.

## Types of Sorting Algorithms

### Sorting algorithms

* Bubble Sort
* Selection Sort
* Insertion Sort
* Merge Sort
* Quicksort

### Characteristics of algorithm

The following characteristics are the basis for how the performance and the suitability of an algorithm are evaluated.

1. Time complexity

Time complexity was discussed in detail in a previous section. When evaluating the effectiveness of algorithms, you take into account how their runtime scales as input size grows. An algorithm can have a different time complexity in the best-case, worst-case, and average-case scenarios. This can provide valuable insights for selecting the most suitable algorithm based on specific requirements.

2. Space complexity

When assessing the efficiency of algorithms that share the same time complexity, you can also consider their space complexity, or how efficiently they use memory as the input size scales. By evaluating an algorithm's best-case, worst-case, and average-case space complexities, you can select the most suitable algorithm for a given use case.

3. Stability

Stability refers to the ability of an algorithm to retain the relative order of equal elements after sorting. If you have two equal elements in the original list where one appears before the other, their relative order will still be maintained in the sorted list. 

Consider the example of the following tuple, which needs to be sorted based on the first element of the tuple:

**Unsorted list: [(5, 'apple'), (3, 'banana'), (5, 'cherry')]**

There are two ways this list could be sorted in ascending order.

* **Option 1: [(3, 'banana'), (5, 'apple'), (5, 'cherry')]**
* **Option 2: [(3, 'banana'), (5, 'cherry'), (5, 'apple')]**

In option 1, the relative order of the tuples **(5, 'apple')** and **(5, 'cherry')** is maintained. In the sorted output, they appear in the same relative order as they do in the unsorted input, with the tuple **(5, 'apple')** coming before the tuple **(5, 'cherry')**. This is a stable sort because the items' relative order has been preserved.

In option 2, the relative order of the tuples **(5, 'apple')** and **(5, 'cherry')** is not maintained. In the sorted output list, the tuple **(5, 'cherry')** now comes before **(5, 'apple')**, instead of after. This is an unstable sort because the original order of the items has not been maintained.

4. Adaptability

Adaptability in sorting algorithms refers to the ability of an algorithm to perform efficiently on partially sorted or nearly sorted input data. An adaptable sorting algorithm can take advantage of existing order in the data and adapt its strategy to minimize unnecessary work. The more presorted the input is, the faster it should be sorted. 

Consider the following two lists:

* **list_1= [2,3,4,5,8,1,6,9]**
* **list_2= [3,9,1,8,4,7,5,2]**

When you observe the two lists, you will notice that **list_1** is partially sorted and **list_2** is completely unsorted.

An adaptive sorting algorithm will take less time to sort **list_1** than it takes to sort **list_2**. However, a non-adaptive algorithm will take an equal amount of time to sort **list_1** and **list_2**.

5. Parallelization

Parallelization in sorting algorithms involves dividing the sorting task into multiple subtasks that can be run simultaneously or concurrently. The goal is to use multiple processors, cores, or threads to improve the overall speed and efficiency of the sorting process. Parallelizing sorting algorithms can be particularly beneficial for very large datasets and can take advantage of the increasing prevalence of multi-core processors and parallel computing architectures. 

Imagine you have a big pile of books and you want to arrange them in order. Instead of doing it one by one by yourself, you decide to ask your friends to help. Each friend takes a portion of the books and starts arranging them independently. This way, everyone is working at the same time, making the whole process much faster.

In computing terms, when you have a lot of data to sort, like a large list of numbers, instead of sorting them one by one, you can break the task into smaller parts. Parallelization allows the computer to sort multiple things at the same time, making the sorting process quicker and more efficient.

Parallelization, in the context of sorting algorithms, means getting multiple parts of the sorting task done at the same time.

### Bubble Sort Algorithm

Bubble sort is one of the most straightforward sorting algorithms and is often used to introduce the concept of sorting algorithms to new learners. In bubble sort, adjacent elements in a list are compared and swapped until the entire list is sorted. Elements "bubble" to their correct position in the list. The following video explains the bubble sort process.

#### Complexity analysis of bubble sort algorithm

To learn more about the time complexity and space complexity of the bubble sort algorithm, expand each of the following two categories.

##### Time Complexity: O(n^2)

Bubble sort has quadratic time complexity, in which the runtime scales quadratically as the number of elements to be sorted increases.

##### Space Complexity: O(1)

Bubble sort is an in-place sorting algorithm, which means it does not require additional space as input size increases. Its space complexity is O(1), meaning it has constant space complexity.

#### Strengths and weaknesses of bubble sort algorithm

##### Strengths

1. **Straightforward**. The bubble sort algorithm is comparatively straightforward to understand and implement for learners who are new to sorting algorithms. It provides a foundation to learn more advanced sorting algorithms.
2. **Low space complexity**. It has a constant space complexity. The memory requirement doesn't increase proportionally as the input size increases.
3. **Stability**. The bubble sort is a stable algorithm, so it retains the relative order of the elements, even after sorting.

##### Weaknesses

1. **High time complexity**. It has a quadratic time complexity of O(n^2) which makes it very slow for large input sizes.
2. **Impractical to use**. In practice, software developers use more efficient sorting algorithms. Bubble sort is comparatively slow and impractical to use for large data sets.
3. **Non-adaptive**. It takes the same amount of time to execute even if the data is partially sorted. As we saw in our example, the algorithm was still comparing the elements through all four passes, even though the list was already sorted by the end of the second pass.

### Selection Sort Algorithm

It works by repeatedly finding the smallest element in the unsorted part of a list and putting it at the beginning of that part of the list. This process is repeated until the entire list is sorted. The following video explains the selection sort process.

#### Selection sort: Step-by-step process

##### First pass

The algorithm selects the smallest element, 11, and places it at the front of the list, resulting in [11,18,12,15,19].
The input list is [19, 18, 12, 15, 11]. The algorithm starts by traversing the list from index 0 (i[0]) to index 4 (i[4]) to select the smallest element. When found, the algorithm swaps the position of the smallest element with the element at i[0].

Here, the smallest element is 11. So, it swaps its position with i[0], which is 19, resulting in the following order: [11, 18, 12, 15, 19]. This completes the first pass. At the end of the first pass, the smallest element, 11, has selected its correct position.

##### Second pass

The algorithm selects the next smallest element, 12, and places it at the front of the unsorted portion of the list.
The list is currently [11, 18, 12, 15, 19]. The first element, 11, is sorted. The algorithm now traverses through the unsorted portion of the list (i[1] to i[4]) to select the smallest element in the remaining unsorted list. It swaps its position with the element at i[1].

Here, the smallest element in the unsorted portion of the list is 12. The algorithm swaps its position with the element at i[1], which is 18. This results in the following order: [11, 12, 18, 15, 19]. This is the second pass. At the end of pass two, the second smallest element, 12, selects its correct position.

##### Third pass

In pass 3, the next smallest element, 15, is selected and placed at the front of the unsorted portion of the list.
The list is currently [11, 12, 18, 15, 19]. Next, the algorithm traverses the unsorted portion of the list (i[2] to i[4]) to again select the smallest element. It swaps the position of the smallest element with the element at i[2], moving the smallest element to the front of the unsorted portion of the list.

Here, the smallest element in the unsorted portion of the list is 15. It swaps with i[2], which is 18. This gives the following order: [11, 12, 15, 18, 19]. This is the third pass. At the end of pass three, the third-smallest element, 15, selects its correct position.

##### Fourth Pass

In pass 4, the smallest remaining element, 18, is already at the front of the unsorted sub-list, and no swap is needed.
The list is currently [11, 12, 15, 18, 19]. Finally, the algorithm traverses the unsorted list (i[3] to i[4]) to select the smallest element in the remaining unsorted list. 

Here, the smallest element in the unsorted portion of the list is 18. There is no need for swapping, since 18 is already at its correct position.

Note that the list was sorted at the end of the third (previous) pass. However, the algorithm carries on to the fourth pass as seen here, proving that the selection sort algorithm is non-adaptive.  

So, the order at the end of the fourth pass is the same as that at the end of third pass: [11, 12, 15, 18, 19].

#### Code example

The following is the Python code for sorting a list of integers using the selection sort algorithm.

The code provides an example of using the selection_sort function with an input list [64, 34, 25, 12, 22, 11, 90].

```
def selection_sort(data):

    for i in range(len(data)):
        min_index = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_index]:
                min_index = j

        data[i], data[min_index] = data[min_index], data[i]
    return data

# Example of usage
input_list = [64, 34, 25, 12, 22, 11, 90]
print(f"Original list: {input_list}")

# Sort the list using selection sort
sorted_list = selection_sort(input_list)
print(f"Sorted list: {sorted_list}")
```

#### Code explanation

Selection sort uses nested loops to find the smallest value in the unsorted part of the list and moves it to the beginning of the unsorted part.

* **def selection_sort(data):** – This line defines a function named **selection_sor**t that takes a list of elements **(data)** as an argument. The purpose of this function is to sort the elements in ascending order using the selection sort algorithm.
* **for i in range(len(data)):** – The outer for loop iterates over the range of **len(data)**, representing the number of elements in the list.
* **for j in range(i + 1, len(data)):** – The inner for loop iterates over the range from **i + 1** to **len(data)**. It searches for the minimum element in the unsorted part of the list.
* **if data[j] < data[min_index]:** – This if statement checks if the element at index j is smaller than the element at **min_index**.
* **data[i], data[min_index] = data[min_index], data[i]** – If the condition is true, it swaps the positions of the two elements, effectively moving the smallest element to its correct position.
* **return data** – This return statement returns the sorted list after both loops are complete.
* **selection_sort(input_list)** – This line calls the **selection_sort** function to sort the **input_list**.

Finally, the original and the sorted lists are printed.

Expected output:

```
Original list: [64, 34, 25, 12, 22, 11, 90]
Sorted list: [11, 12, 22, 25, 34, 64, 90]
```

#### Complexity analysis of selection sort algorithm

##### Time Complexity: O(n^2)

Selection sort has quadratic time complexity. The number of steps required to complete the algorithm scales quadratically with the number of elements in the input sequence.

##### Space Complexity: O(1)

Selection sort is an in-place sorting algorithm, which means it does not require additional space even as input size increases. Its space complexity is O(1). That means it has constant space complexity.

#### Strengths and weaknesses of the selection sort algorithm

##### Strengths

1. **Straightforward**. The selection sort algorithm is comparatively straightforward to understand and implement.
2. **Low space complexity**. It has a constant space complexity. The memory requirement doesn't increase proportionally as the input size increases.

##### Weaknesses

1. **High time complexity**. It has a quadratic time complexity of O(n^2), which makes it very slow for large input sizes.
2. **Unstable**. It is an unstable sorting algorithm. The relative order between two equal elements may not be maintained in the sorted list.
3. **Non-adaptive**. It takes the same amount of time to execute even if the data is partially sorted. As we saw in the example, the algorithm was still comparing the elements in four passes even if the list was already sorted by the end of the second pass.
4. **Not suitable for large input size**. It is not efficient for large data sets.

### Insertion Sort Algorithm

#### Insertion sort: Step-by-step process

##### First Pass

In the list [29,21,27,23,25], the first two elements are compared. 21 is smaller and the key element, and is swapped with 29.
The input list is [29, 21, 27, 23, 25]. The algorithm considers the first element at index 0 (i[0]) as the first item in the sorted sub-array. It then compares this value with the value at index 1 (i[1]), which is the first element in the unsorted sub-array.  This item is called the key element. If i[0] > i[1], the elements swap their positions. Otherwise, no swapping takes place.

Here, because 29 > 21, the elements swap their positions, and 21 is inserted into its correct position in the sorted sub-array. Now the new order becomes [21, 29, 27, 23, 25]. This results in the sorted sub-array [21,29], which consists of the first two sorted elements in the array, and the unsorted sub-array [27, 23, 25].

##### Second Pass

The key element 27 is inserted into its correct position in the sorted sub-array, resulting in [21,27,29,23,25].
The array is now [21, 29, 27, 23, 25]. The algorithm selects the next key element, which is the first element of the unsorted sub-array. The insertion sort algorithm inserts the key element into its correct position in the sorted sub-array by swapping.  

The current key element is 27, so 27 has to be inserted in its correct position in the sorted sub-array. 27 and 29 swap positions. This results in the following order: [21, 27, 29, 23, 25]. Now [21, 27, 29] are the values in the sorted sub-array, and [23, 25] remain in the unsorted sub-array.

##### Third Pass: Step 1

The key element 23 is swapped with 29, resulting in [21,27,23,29,25].
The array is now [21, 27, 29, 23, 25]. Next, the algorithm selects the key element from the unsorted sub-array and inserts it in the correct position in the sorted sub-array. Here, the key element is 23. Because 29 > 23, they swap their positions, and the new array order becomes [21,27,23,29,25]. However, the sorted sub-array [21, 27, 23, 29] is still not sorted, because 23 is less than 27 and should come before it.  

##### Third Pass: Step 2

The key element 23 is swapped again to find its correct position in the sorted sub-array, resulting in [21,23,27,29,25].
The sub-array [21, 27, 23, 29] is still not fully sorted, as the key element 23 has not found its correct position. The algorithm compares 23 to its neighbor. Because 27 > 23, they swap their positions so that the sub-array becomes [21,23,27,29]. This sub-array is now sorted. So, the new order of the array becomes [21,23,27,29,25].

##### Fourth Pass: Step 1

The last key element, 25, is swapped with its neighbor, resulting in [21,23,27,25,29].
The array at this point is [21, 23, 27, 29, 25]. Finally, 25 is selected as the key element and is also the last element remaining to be sorted.  

Here, because 29 > 25, the elements again swap their positions, resulting in the following order: [21, 23, 27, 25, 29].

The array is still not sorted because 25 is less than 27.

##### Fourth Pass: Step 2

The key element 25 is swapped once more, this time with 27, resulting in [21,23,25,27,29].
The array is [21, 23, 27, 25, 29], and the key element 25 still needs to find its correct position. Because 27 > 25, the elements swap their positions, resulting in the following order: [21, 23, 25, 27, 29].  

Now, the entire array is sorted, and no more action is required.

#### Code example

The following is the Python code for sorting a list of integers using the insertion sort algorithm.

The code provides an example of using the insertion_sort function with an input list [64, 34, 25, 12, 22, 11, 90].

```
def insertion_sort(data):

    for i in range(1, len(data)):
        key = data[i]

        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

    return data

# Example of usage
input_list = [64, 34, 25, 12, 22, 11, 90]
print(f"Original list: {input_list}")

# Sort the list using insertion sort
sorted_list = insertion_sort(input_list)
print(f"Sorted list: {sorted_list}")
```

#### Code explanation

Insertion sort uses nested loops to place elements into the correct position of the sorted sub-list.

* **def insertion_sort(data):** – This line defines a function named **insertion_sort** that takes a list of elements **(data)** as an argument. The purpose of this function is to sort the elements in ascending order using the insertion sort algorithm.
* **for i in range(1, len(data)):** – The for loop iterates over the range from 1 to the length of the list. It starts from 1 because the element at index 0 is considered to be part of the sorted portion initially.
* **key = data[i]** – The current element to be inserted into the sorted portion is stored in the variable **key**.
* **j = i - 1** – The variable, j, is set to the index before the current element in the sorted portion.
* **The while loop:**
 * **while j >= 0 and key < data[j]:** – This loop compares the key with each element in the sorted portion until it finds the correct position for the key.
 * **data[j + 1] = data[j]* – Shifts the elements greater than the key one position to the right.
 * **j -= 1** – Decrements the index to check the previous element in the sorted portion.
* **data[j + 1] = key** – Inserts the key into its correct sorted position.
* **return data** – This return statement returns the sorted list after both loops are complete.
* **insertion_sort(input_list)** – This line calls the **insertion_sort** function to sort the **input_list**.

Finally, the original and the sorted lists are printed.

Expected output:

```
Original list: [64, 34, 25, 12, 22, 11, 90]
Sorted list: [11, 12, 22, 25, 34, 64, 90]
```

#### Complexity analysis of insertion sort algorithm

##### Time Complexity: O(n^2)

Insertion sort has a quadratic worst-case time complexity. As the number of elements to be sorted increases, insertion sort's runtime scales quadratically. 

##### Space Complexity: O(1)

Insertion sort is an in-place sorting algorithm, which means it does not require additional space as input size increases. Its worst-case space complexity is O(1), meaning it has constant space complexity.

#### Strengths and weaknesses of the insertion sort algorithm

##### Strengths

1. **Straightforward**. The insertion sort algorithm is comparatively straightforward to understand and implement for learners who are new to sorting algorithms. It provides a foundation to learn more advanced sorting algorithms.
2. **Efficient space complexity**. It has a constant worst-case space complexity. The memory requirement doesn't increase proportionally as the input size increases.
3. **Stable**. The relative order of the equal elements is retained.
4. **Adaptive**. It is efficient if the list is partially sorted.
5. **Suitable for small input size**. It is very efficient for smaller data sets.

##### Weaknesses

1. **High time complexity**. It has a quadratic time complexity of O(n^2), which makes it very slow for large input sizes.
2. **Not suitable for large input size**. It is not efficient for large data sets.

### Merge Sort Algorithm

Merge sort divides an array into smaller sub-arrays, sorts every sub-array, and then merges the sorted sub-arrays back together to form the final sorted array. It is based on the divide-and-conquer strategy. A problem is divided into smaller problems, solved recursively, and finally merged into one solution.

#### Merge sort: Step-by-step process

##### Step 1

The list [39,30,37,32,36], divided on the median at index 2, resulting in two sub-lists, [39,30] and [37,32,36].
First, the algorithm decides the median of an array and breaks it into two halves. Here, the median is the element at index 2, or i[2] = 37. This gives two sub-arrays: [39,30] and [37,32,36].

##### Step 2

The sub-arrays are further divided into two halves on their medians.
Next, the algorithm again breaks each sub-array into halves.

This breaks the sub-array [39,30] into two separate sub-arrays: [39] and [30].

Then, it breaks [37,32,36] into two separate arrays: [37] and [32,36].

##### Step 3

The sub-arrays are divided on their medians until each has only one element. An array with one element is considered sorted.
Now, there are four separate sub-arrays: [39], [30], [37], and [32, 36]. The sub-arrays [39] and [30] each have one element and cannot be further divided. An array with one element is considered sorted.

The sub-array [37] also cannot be further divided. The algorithm divides the sub-array [32,36] into two more sub-arrays: [32] and [36].

This results in five separate sub-arrays: [39], [30], [37], [32] and [36], which cannot be broken down any further.

##### Step 4

[39] and [30] are sorted and merged into [30,39]. [37] is skipped for now. [32] and [36] are sorted and merged into [32,36].
The divide phase is now over, and the original array has been divided out into sub-arrays of one element each: [39], [30], [37], [32], and [36]. At this step, the merge phase of the sub-arrays begins. The algorithm merges the sub-arrays [39] and [30] into a single, sorted sub-array: [30,39].

The sub-array [37] will be skipped for now and merged in the next step.

The algorithm then merges [32] and [36] and returns another sorted sub-array: [32, 36].

The sub-arrays are now: [30, 39], [37], and [32, 36].

##### Step 5

[37] is sorted and merged with [32,36], resulting in the sub-array [32,36,37].
The sorted and merged sub-arrays are currently [30, 39], [37], and [32, 36]. Now the sub-arrays [37]  and [32, 36] are sorted and merged, resulting in the sorted sub-array: [32, 36, 37].

You now have two sorted final sub-arrays: [30, 39] and [32,36,37].

##### Step 6:

The final step of merge sort, in which the last two sub-arrays are merged into the final sorted array.

Finally, the two sorted sub-arrays are [30,39] and [32,36,37]. They are sorted and merged, and you get a final sorted array: [30, 32, 36, 37, 39].

#### Code example

The following is the Python code for sorting a list of integers using the merge sort algorithm. 

The code provides an example of using the merge_sort function with an input list [64, 34, 25, 12, 22, 11, 90].

```
def merge_sort(data):

    if len(data) <= 1:
        # Already sorted
        return data

    # Split the list into two halves
    mid = len(data) // 2
    left_half = data[:mid]
    right_half = data[mid:]

    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):

    result = []
    i = j = 0

    # Compare elements from left and right and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append the remaining elements, if any, from both lists
    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Example of usage
input_list = [64, 34, 25, 12, 22, 11, 90]
print(f"Original list: {input_list}")

# Sort the list using merge sort
sorted_list = merge_sort(input_list)
print(f"Sorted list: {sorted_list}")
```

#### Code explanation

Merge sort consists of two phases. First, the divide phase, in which the list is recursively broken out into sub-lists. Then, the conquer phase, in which the sub-lists are sorted and merged back together.

* **def merge_sort(data):** – This function takes a list of elements **(data)** and implements the merge sort algorithm to sort the elements in ascending order.
* **if len(data) <= 1:** – If the length of the list is 1 or less, it is already considered sorted, and the original list is returned.
* **mid = len(data) // 2** – Calculates the midpoint of the list.
* **left_half = data[:mid]** – Splits the list into the left half.
* **right_half = data[mid:]** – Splits the list into the right half.
* **left_half = merge_sort(left_half)** – Recursively applies the merge sort to the left half.
* **right_half = merge_sort(right_half)** – Recursively applies the merge sort to the right half.
* **return merge(left_half, right_half)** – Merges the sorted left and right halves using the **merge** helper function.
* **def merge(left, right):** – This helper function takes two sorted lists (**left** and **right**) and merges them into a single sorted list.
* **result = []** – Initializes an empty list to store the merged result.
* **i = j = 0** – Initializes counters for the left and right lists.
* **The while loop:**
 * Compares elements from the left and right lists and appends the smaller element to the result list.
 * Increments the corresponding counter (i or j) for the list from which the element was appended.
* **result.extend(left[i:])** – Appends the remaining elements, if any, from the left list to the result list.
* **result.extend(right[j:]** – Appends the remaining elements, if any, from the right list to the result list.
* **return result** – Returns the merged and sorted list.
* **merge_sort(input_list)** – Calls the **merge_sort** function to sort the **input_list**.

Finally, the original and the sorted lists are printed.

Expected output:

```
Original list: [64, 34, 25, 12, 22, 11, 90]
Sorted list: [11, 12, 22, 25, 34, 64, 90]
```

#### Complexity analysis of merge sort algorithm

##### Time Complexity: O(n log n)

Merge sort has quasilinear worst-case time complexity. Merge sort has a more efficient worst-case time complexity than the previous sorting algorithms covered. Bubble sort, selection sort, and insertion sort all have a worst-case time complexity of O(n^2).

##### Space Complexity: O(n)

In merge sort, all elements are copied into an auxiliary array. So the auxiliary space required for merge sort scales linearly with the size of the input. The merge sort has linear space complexity, which is higher than the space complexity of the previous sorting algorithms.

#### Strengths and weaknesses of merge sort algorithm

##### Strengths

1. **Lower time complexity**. The merge sort algorithm has a worst-case time complexity of O(n log n), which is lower than the time complexities of bubble sort, selection sort, and insertion sort. Thus, the algorithm is efficient for large input sizes.
2. **Stable**. The relative order of the equal elements is retained.
3. **Adaptive**. It is efficient if the list is partially sorted. 
4. **Parallelization**. It can handle multiple processes and threads simultaneously. 
5. **Suitable for large input size**. It is efficient for large data sets.

##### Weaknesses

1. **Higher space complexity**. The merge sort algorithm has a worst-case space complexity of O(n), which means it has higher space requirements. It requires additional memory to store merged sub-arrays and also to store the sorted data.
2. **Not suitable for small input size**. Its efficiency is lower for small data sets compared to the insertion sort.

### Quicksort Algorithm

Quicksort selects a pivot and partitions the input list into two sub-lists, the first with items smaller than the pivot and the second with items larger than the pivot. The algorithm then sorts both sub-lists recursively until the entire list is completely sorted. The following video explains the quicksort process.

#### Quicksort: Step-by-step process

##### First Pass: Step 1

The third element, 45, is picked as a pivot and swaps with the element at the end, 49. The list is now: 47,40,49,46,42,41,45.
The algorithm selects a pivot to break the array [47, 40, 45, 46, 42, 41, 49] into two sub-arrays. It partitions the array around the pivot, putting every smaller element into a lower array and every larger element into a higher array. The pivot can be any number in the array; sometimes, the first, middle, or last element is chosen as the pivot. Here, a pivot will be chosen at random.

The algorithm randomly selects the element 45 as the pivot in this example. The algorithm then moves the pivot to the very end of the array so that can sort the rest of the array. For this to be achieved, the pivot is swapped with the last element of the array. So, in this example, the elements 45 and 49 are swapped, resulting in an updated array of [47, 40, 49, 46, 42, 41, 45].

##### First Pass: Step 2

The left-side element 47, greater than the pivot 45, and the right-side element 41, smaller than the pivot, are swapped.
With the pivot moved to the end, the array is now [47, 40, 49, 46, 42, 41, 45]. Next, to sort the array, the algorithm aims to find the smaller-than-pivot elements and group them on one side of the pivot. The greater-than-pivot elements will be grouped on the other side of the pivot. So, the algorithm looks for smaller-than-pivot elements starting from the right-most index before the pivot, and swaps their positions with greater-than-pivot elements from the left-most index.

The algorithm keeps repeating the process until the index looking for smaller-than-pivot elements from the right is smaller than the index looking for greater-than-pivot elements from the left. When this happens, the correct position for the pivot has been found.

In this example, 41 is the first smaller-than-pivot element from the right-most index before the pivot, and 47 is the first greater-than-pivot element from the left-most index. So, the algorithm swaps their positions.

##### First Pass: Step 3

The list is now 41,40,49,46,42,47,45. The elements 42 and 49 are swapped. The updated list is now 41,40,42,46,49,47,45.
The array after the last swap is  [41, 40, 49, 46, 42, 47, 45]. Now, 42 is the first smaller-than-pivot element from the end of the array, and 49 is the first greater-than-pivot element from the beginning. So, the algorithm swaps their positions too, resulting in an updated array of [41, 40, 42, 46, 49, 47, 45].

##### First Pass: Step 4

The pivot 45 is moved between the partitioned lists, between 42 and 46. The updated list will now be 41,40,42,45,46,49,47.
The array is now [41, 40, 42, 46, 49, 47, 45]. In this step, the index of the smaller-than-pivot element from the right is now at index 2, and is smaller than the index 3 of the greater-than-pivot element from the left. So, no more swapping is needed. At this point, the algorithm obtains the correct position for the pivot 45, which is between the elements 42 and 46, at index 3.  

##### First Pass: Step 5

The list is now 41,40,42,45,46,49,47. The pivot, 45, is between the sub-arrays of values lower and higher than the pivot.
The pivot 45 is inserted in its correct position at index 3, resulting in an updated array of [41, 40, 42, 45, 49, 47, 46]. Now, all smaller-than-pivot elements are before the pivot, and all greater-than-pivot elements are after the pivot. Thus, the pivot divides the array into two partitions: the lower sub-array [41,40,42] and the higher sub-array [49, 47, 46]. These sub-arrays will be sorted recursively, following the same set of steps as this first pass.

##### Second Pass: Step 1

Pivots swap with the last elements in the sub-arrays. Now, the lower sub-array is 42,40,41; the higher sub-array is 49,46,47.
For both the lower sub-array and the higher sub-array, the pivot is randomly selected again and is placed at the end of the sub-array. This is done by swapping it with the last element of the sub-array.

The algorithm randomly selects 41 as a pivot in the lower sub-array [41,40,42] and the element 47 as the pivot in the higher sub-array [49, 47, 46].

In the lower sub-array, the pivot element 41 is swapped with the last element 42, resulting in [42, 40, 41]. 

And in the higher sub-array, the pivot element 47 is swapped with the last element 46, resulting in [49, 46, 47].

##### Second Pass: Step 2

In lower sub-array 42,40,41, elements 42 and 40 are swapped. In higher sub-array 49,46,47, elements 49 and 46 are swapped.
In the lower sub-array [42,40,41], the element 41 is the pivot. The element 40 is the first smaller-than-pivot element from the right-most index before the pivot, and 42 is the first greater-than-pivot element from the beginning of the sub-array. The algorithm swaps their positions to partition elements based on how they compare to the pivot.

In the higher sub-array [49, 46, 47], the element 47 is the pivot. The element 46 is the first smaller-than-pivot element from the right-most index before the pivot, and 49 is the first greater-than-pivot element from beginning of the sub-array. The algorithm swaps their positions as well.

##### Second Pass: Step 3

In sub-array 40,42,41, the pivot 41 moves between 40 and 42. In sub-array 46,49,47, the pivot 47 moves between 46 and 49.
The process of sorting the sub-arrays continues.

For the lower sub-array [40,42,41], which uses a pivot of 41, the index of the smaller-than-pivot element from the right is now pointing to index 0, which is smaller than the index of the greater-than-pivot element from the left, which now points at index 1. So, no further swapping takes place, and the correct position for the pivot 41 is found at index 1.

In the higher sub-array [46,49,47], which uses a pivot of 47, the index of the smaller-than-pivot element from the right is now smaller than the index of the greater-than-pivot element from the left. No further swapping takes place, and the correct position for the pivot 47 has been found.

##### Second Pass: Step 4

The sub-arrays are sorted and can now be joined with the original pivot to form the fully sorted array: 40,41,42,45,46,47,49.
In the lower sub-array, the pivot element 41 is inserted in its correct position. The sorted lower sub-array is [40, 41, 42].

In the higher sub-array, the pivot element 47 is inserted in its correct position. The sorted higher sub-array is [46, 47, 49].

Now, the sorted lower sub-array and the sorted higher sub-array are obtained. And finally, with the original pivot element 45, we get a completely sorted array: [40, 41, 42, 45, 46, 47, 49].

#### Code example

The following is the Python code for sorting a list of integers using the quicksort algorithm.

The code provides an example of using the quick_sort function with an input list of [64, 34, 25, 12, 22, 11, 90]. Note that in this implementation of quicksort, the pivot is the last element in the list, instead of a random element. 

```
def quick_sort(data):

    if len(data) <= 1:
        return data

    pivot = data[-1]

    less_than_pivot = [x for x in data[:-1] if x <= pivot]
    greater_than_pivot = [x for x in data[:-1] if x > pivot]

    sorted_less = quick_sort(less_than_pivot)
    sorted_greater = quick_sort(greater_than_pivot)

    return sorted_less + [pivot] + sorted_greater

# Example of usage
input_list = [64, 34, 25, 12, 22, 11, 90]
print(f"Original list: {input_list}")

# Sort the list using quick sort
sorted_list = quick_sort(input_list)
print(f"Sorted list: {sorted_list}")
```

#### Code explanation

Quicksort selects a pivot element and partitions the list into sublists of elements greater than or less than the pivot element. This continues recursively until the entire list is sorted.

* **def quick_sort(data):** – This function takes a list of elements **(data)** and implements the quicksort algorithm to sort the elements in ascending order.
* **if len(data) <= 1:** – If the length of the list is one or less, it is already considered sorted, and the original list is returned.
* **pivot = data[-1]** – Selects the last element of the list as the pivot element.
* **less_than_pivot = [x for x in data[:-1] if x <= pivot]** – Creates a list of elements less than or equal to the pivot.
* **greater_than_pivot = [x for x in data[:-1] if x > pivot]** – Creates a list of elements greater than the pivot.
* **sorted_less = quick_sort(less_than_pivot)** – Recursively applies the quicksort to the list of elements less than or equal to the pivot.
* **sorted_greater = quick_sort(greater_than_pivot)** – Recursively applies the quicksort to the list of elements greater than the pivot.
* **return sorted_less + [pivot] + sorted_greater** – Combines the sorted lists of elements less than or equal to the pivot, the pivot itself, and the sorted list of elements greater than the pivot.
* **quick_sort(input_list)** – Calls the **quick_sort** function to sort the **input_list** of numbers.

Finally, the original and the sorted lists are printed.

Expected output:

```
Original list: [64, 34, 25, 12, 22, 11, 90]
Sorted list: [11, 12, 22, 25, 34, 64, 90]
```

#### Complexity analysis of quicksort algorithm

##### Time Complexity: O(n^2)

Quicksort has a worst-case time complexity of **O(n^2)**. This means it has a higher worst-case time complexity compared to merge sort, which has a worst-case time complexity of **O(n log n)**. Quicksort's best-case and average-case time complexities are both **O(n log n)**, where **n** is the number of elements in the input sequence.

##### Space Complexity: O(n)

Quicksort has a worst-case space complexity of **O(n)**, similar to that of a merge sort. Quicksort's space complexity is a result of the additional recursive calls it puts on the call stack. In the worst case, when the algorithm chooses the pivots poorly (for example, always the largest element), the depth of the recursion stack will be proportional to the input size n. 

In the best case, when the algorithm chooses the pivot optimally (close to the middle value) and creates even partitions, the space complexity is logarithmic.  

#### Strengths and weaknesses of quicksort algorithm

##### Strengths

1. **Lower best-case and average-case time complexity**. The quicksort algorithm has a time complexity of **O(n log n)** for best and average cases. Thus, the algorithm is efficient and quick for large input sizes.  

2. **Parallelization**. It can handle multiple processes and threads simultaneously. 

##### Weaknesses

1. **High worst-case time complexity**. The quicksort algorithm has a time complexity of O(n^2), making it less reliable in cases where a certain level of performance needs to be guaranteed.
2. **High worst-case space complexity**. The quicksort algorithm has a linear space complexity of O(n), meaning it has higher space requirements.  
3. **Not suitable for small input size**. Its efficiency is lower for small data sets compared to the insertion sort.
4. **Unstable**. It is an unstable sorting algorithm. The relative order between the two equal elements might not be maintained in the sorted list.
5. **Non-adaptive**. The runtime does not decrease, even if the list is partially sorted.

**Note:** The worst-case time complexity of quicksort is relatively inefficient at O(n^2). However, in practice and with optimizations, quicksort beats most other sorting implementations. Because of recursion, quicksort is considered inefficient for smaller input sizes and might even perform worse on those data sets than bubble sort.

### Comparing Sorting Algorithms

| Algorithm | Time complexity | Space complexity | Stability | Adaptability | Small dataset | Large dataset |
| --------- | --------------- | ---------------- | --------- | ------------ | ------------- | ------------- |
| Bubble sort | O(n^2) | O(1) | Stable | Non-adaptive | Efficient | Inefficient |
| Selection sort | O(n^2) | O(1) | Unstable | Non-adaptive | Efficient | Inefficient |
| Insertion sort | O(n^2) | O(1) | Stable | Adaptive | Efficient | Inefficient |
| Merge sort | O(n log n) | O(n) | Stable | Adaptive | Inefficient | Efficient |
| Quicksort | O(n^2) for worst-case, O(n log n) for average case | O(n) | Unstable | Non-adaptive | Inefficient | Efficient |

### Knowledge Check

#### What does adaptive mean in sorting algorithms?

* Efficient for partially sorted lists

Wrong answers:

* Suitable for large input sizes
* Stable sorting behavior
* Low space complexity

Adaptive sorting algorithms efficiently handle partially sorted lists, adjusting their performance based on the existing order.

#### Which sorting algorithm selects a pivot to carry out its operation?

* Quicksort

Wrong answers:

* Bubble sort
* Merge sort
* Insertion sort

 With quicksort, the algorithm selects a pivot element and partitions the input array into two sub-arrays, based on elements smaller and larger than the pivot. The process is then recursively applied to the sub-arrays.

#### What is parallelization in algorithms?

* The transformation of an algorithm into a program that is capable of parallel processing

Wrong answers:

* The reduction of an algorithm's time complexity by parallelizing its operations
* The optimization of an algorithm's space complexity by introducing parallel processing
* The transformation of an algorithm into a recursive structure for parallel processing

Parallelization involves converting an algorithm into a parallel program that can run multiple operations simultaneously. It takes advantage of parallel processing capabilities to enhance performance. It is about dividing the workload and running different parts concurrently to achieve faster overall computation.

### Summary

**Bubble sort, selection sort, and insertion sort:** Generally inefficient for large datasets. 

**Merge sort:** Stable and efficient for large datasets, but requires additional space. 

**Quicksort:** Efficient for large datasets, but its worst-case time complexity can be problematic. With optimizations, it becomes more practical.

Keep in mind that the actual performance might vary, based on the implementation and environmental factors. The choice of sorting algorithm depends on the specific requirements and characteristics of the data being sorted.

## [Lab: Benchmarking Your Algorithms](./W06Lab1BenchmarkingAlgorithms.md)
