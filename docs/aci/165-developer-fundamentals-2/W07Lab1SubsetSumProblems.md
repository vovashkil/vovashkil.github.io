# Writing Code To Solve a Subset Sum Problem

## Lab overview

This lab teaches you the approach to solve problems using dynamic programming. You learn about the subset sum problem and solve it using methods of recursion and memoization.

The subset sum problem is a computer science decision problem. It can arise in situations where different resources have different costs or values, and you have to find a combination of resources that meets the given criteria. That criteria could be something like staying within a budget or maximizing value. Also, the subset sum problem can occur when scheduling and planning to find the combinations of tasks to complete within a certain time limit.

Review the following problem statement: Given a set of positive integers and a target sum, determine whether there is a subset of a given set that adds up to the specified target sum.

Review the following inputs:

Set of numbers (‘data’): A set of positive integers
Target (‘total’): The total that is expected
There are two approaches to solve the problem: recursion and memoization. First, you write code to solve this problem using recursion. Then you solve the problem using memoization.

Consider the following set of numbers [ 5, 4, 12, 2, 7 ]. The subset sum problem checks whether there is a set of numbers in this list that add up to the total (11 in this case). For this example, the program returns True because the subset [ 5, 4, 2] or [ 4, 7 ] satisfies the criteria.

Objectives
By the end of this lab, you will be able to do the following:

Recognize the elements of a basic subset sum problem.
Use recursion to solve the subset sum problem.
Use memoization to solve the subset sum problem.
Compare time and space complexity for the recursion and memoization approaches for the subset sum problem.
Technical knowledge prerequisites
This hands-on lab assumes that you have completed the Developer Fundamentals 1 (DF1) course and the associated labs.

Duration
This lab requires approximately 2 hours to complete.

Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Command: A command that you must run
 Expected output: A sample output that you can use to verify the output of a command or edited file
 Note: Additional information or elaboration on a point
 Task complete: A conclusion or summary point in the lab
Start lab
To launch the lab, at the top of the page, choose Start Lab.

 Caution: You must wait for the provisioned AWS services to be ready before you can continue.

To open the lab, choose Open Console .

You are automatically signed in to the AWS Management Console in a new web browser tab.

 Warning: Do not change the Region unless instructed.

Common sign-in errors
Error: Choosing Start Lab has no effect
In some cases, certain pop-up or script blocker web browser extensions might prevent the Start Lab button from working as intended. If you experience an issue starting the lab:

Add the lab domain name to your pop-up or script blocker’s allow list or turn it off.
Refresh the page and try again.
AWS services used in this lab
AWS Cloud9
AWS Cloud9 is a cloud-based integrated development environment (IDE) that offers a rich code-editing experience with support for several programming languages and runtime debuggers, and a built-in terminal. It contains a collection of tools that you use to code, build, run, test, and debug software, and it helps you release software to the cloud.

Task 1: Solve the problem using recursion
In this task, you become familiar with the problem statement, including its inputs and outputs. You solve the problem by using recursion.

Task 1.1: Define a base case
You define a base case that identifies the conditions that stop the recursion and return a result directly. For example, write the logic to return True or False.

Think about the following questions:

What will be the result of the function if asked for a sum of 0?
What will be the result of the function if it is passed an empty list?
To open the AWS Cloud9 environment, copy the Cloud9Environment URL value that is listed to the left of these instructions, and paste it into a new browser tab…

Open the subset.py file and add code to define the base cases:


# Define a function using recursion that takes a set of numbers and a target sum as input to solve the subset sum problem. 

def subset_sum(data, total):

# Define base cases here:
To view the source code and explanation, expand this section.
 Note: A function that uses recursion has been created for you. It takes a set of numbers and a target sum as input to solve the subset sum problem.

Task 1.2: Define the recurrence relation
You define the recurrence relation and use recursion to break down the problem into smaller subproblems.

In each recursive call, consider two scenarios:

Include the last element in data in the subset and reduce the total by its value.
Exclude the last element in data in the subset and keep the total unchanged.
Add code to define the recurrence relation in the subset.py file:
Include the last element in the subset(data[-1]) and check whether subset with (total - data[-1]) exists.
Exclude the last element in the subset and check whether subset with the total exists.

# Complete the follwoing line of code and define the recursive call for the 'included' case
included = 

# Complete the following line of code and define the recursive call for the 'excluded' case.
excluded =
To view the source code and explanation, expand this section.
Task 1.3: Test the program
You provide the inputs and test the program. After making recursive calls, combine the results to determine whether any valid subset sum exists. The program returns ‘True’ if either included or excluded subset sum is found; otherwise it returns ‘False’.

Add code to provide the inputs and test the program in the subset.py file:

    # Complete the following line of code and complete the return statement
    # return 

# Example input
data = [5,4,12,2,7]
target = 11

# Test the program
result = subset_sum(data, target)
print(result)
To view the source code and explanation, expand this section.
Save the file and run the program to see the output. If either of the recursive calls returns ‘True’, you return ‘True’(subset found to have sum that matches the given target).
 Expected output:


True


Process exited with code: 0
 Note: If you receive an error, expand the following section for the subset.py source code.

To view the source code and explanation, expand this section.
In the recursive approach for the subset sum problem, there are two recursive calls—one for the last element to be included in the subset and one that is not included. The recurrence relation can be expressed as the following:


T(n) = 2 * T(n-1)
T(n) is the time complexity for set of size n. T(n-1) represents the recursive calls for set of size n-1, and 2 is the factor for the inclusion and exclusion. This shows that there is exponential growth in the number of calls, leading to exponential time complexity.

Replace the target = 11 with target = 100 and test the program in the subset.py file:

# Define a function for Subset Sum problem

def subset_sum(data, total):
    # Test for base cases

    if total == 0:
        return True
    
    if not data or total < 0:
        return False
    
    # Recursion calls

    included = subset_sum(data[:-1], total - data[-1])

    excluded = subset_sum(data[:-1], total)

    return included or excluded

# Example input
data = [5,4,12,2,7]
# Replace the previous target number (target = 11) with the one here
target = 100

# Test the program
result = subset_sum(data, target)
print(result)
Save the file and run the program to see the output. If none of the recursive calls return ‘True’, you return ‘False’(no subset found with sum that matches the to given target).
 Expected output:


False


Process exited with code: 0
 Task complete: You have successfully solved the problem by using recursion.

Task 2: Solve the problem using memoization
In this task, you add code to the previous example to solve the problem using memoization. In the previous task, you solved the problem using recursion.

Task 2.1: Create a tuple
A tuple is data that is ordered and cannot be changed after it is created. A dictionary is where data is stored and retrieved by using key-value pairs. In this subtask, you use a tuple, and the total that you are testing for, for example: ((1, 2, 3, 4, 5, 5), 100). You create a tuple for the set of numbers so that you can use it as a key. Note the True/False result in the value in the memo dictionary. You check whether the tuple exists as a key in the memo dictionary. If it does, it means that the solution for this subset sum problem has already been memoized and stored in the memo dictionary. The print statement prints, indicating the memoization.

Open the subset_memo.py file, which contains an example of the following code:

def subset_sum(data, total, memo={}):

    # Base cases defined in the previous task
    if total == 0:
        return True
    
    if not data or total < 0:
        return False

    if (tuple(____),____) in memo:
       print(f"Memoization hit for {(tuple(data), total)}")
       return memo[(tuple(____), _____)]

    included = subset_sum(____, ____, ____)
    excluded = subset_sum(____, ____, ____)

    memo[(tuple(____), ____)] = included or excluded
    print(f"Memoization stored for {(tuple(data), total)}: {memo[(tuple(data), total)]}")
    
return included or excluded

# Example Input
data = [1,4,5,5,9,12,13,20,20,23]
target = 11

# Test the program
result = subset_sum(data, target)
print(result)
 Note: The base case used in the previous task is being used in the subset_memo.py file.

In this section of the subset_memo.py file, replace the blanks with the correct code, and remove the comment symbol:

    if (tuple(____),____) in memo:
        print(f"Memoization hit for {(tuple(data), total)}")
        return memo[(tuple(____), _____)]
To view the source code and explanation, expand this section.
Task 2.2: Store the result
You store the result of the element included or excluded in the dictionary.

In this section of the subset_memo.py file, replace the blanks with the correct code, and remove the comment symbol.
Include the last element in the subset(data[-1]) and check whether subset with (total - data[-1]) exists.
Exclude the last element in the subset and check whether subset with the total exists.
There is now a third argument.

    included = subset_sum(____, ____, ____)
    excluded = subset_sum(____, ____, ____)
To view the source code and explanation, expand this section.
Task 2.3: Memoize the result
You memoize the results, and a print statement is included that indicates that computation is being stored for the particular subset sum problem.

Replace the blanks with the correct code and remove the comment symbol in thIn this section of the subset_memo.py file, replace the blanks with the correct code, and remove the comment symbol.

    memo[(tuple(____), ____)] = included or excluded
    print(f"Memoization stored for {(tuple(data), total)}: {memo[(tuple(data), total)]}")
    
    return included or excluded


# Example Input
data = [1,4,5,5,9,12,13,20,20,23]
target = 11

# Test the program
result = subset_sum(data, target)
print(result)
To view the source code and explanation, expand this section.
Save the file and run the program to see the output.
 Expected output:


Memoization stored for ((1,), 2): False
Memoization stored for ((1, 4), 2): False
Memoization stored for ((1, 4, 5), 2): False
Memoization stored for ((1, 4, 5, 5), 2): False
Memoization stored for ((1,), 1): True
Memoization stored for ((1, 4), 1): True
Memoization hit for ((1,), 2)
Memoization stored for ((1,), 6): False
Memoization stored for ((1, 4), 6): False
Memoization stored for ((1, 4, 5), 6): True
Memoization hit for ((1, 4), 6)
Memoization stored for ((1,), 7): False
Memoization stored for ((1,), 11): False
Memoization stored for ((1, 4), 11): False
Memoization stored for ((1, 4, 5), 11): False
Memoization stored for ((1, 4, 5, 5), 11): True
Memoization stored for ((1, 4, 5, 5, 9), 11): True
Memoization stored for ((1, 4, 5, 5, 9, 12), 11): True
Memoization stored for ((1, 4, 5, 5, 9, 12, 13), 11): True
Memoization stored for ((1, 4, 5, 5, 9, 12, 13, 20), 11): True
Memoization stored for ((1, 4, 5, 5, 9, 12, 13, 20, 20), 11): True
Memoization stored for ((1, 4, 5, 5, 9, 12, 13, 20, 20, 23), 11): True
True
 Note: If you receive an error, expand the following section for the subset.py source code.

To view the source code if needed, expand this section.
In the memoization approach, you have n elements in the dataset and for each element, you consider two possibilities as included or excluded. For each recursive call, the algorithm performs constant time work, so the results are O(n). W can be used to represent a range of target totals. So the time complexity can be expressed as O(n-W), where n is the number of elements in the dataset and W is the range of sums.

Look at the impact on space complexity for both approaches (recursion and memoization). The time complexity for memoization is better because you are avoiding the number of redundant calculations, making memoization more appropriate for large datasets. The memoization approach for space complexity is more intensive, but it can be a tradeoff for improvement in the time complexity.

Consider the depth of the recursion stack to calculate the space complexity for the problem using the recursive approach. If n is the number of elements in the dataset, the space complexity is O(n). But the space complexity for the memoization approach depends on the space consumed by the table. The memoization table size depends on the number of unique subproblems. Just like complexity, the number of problems can be represented by (n-W), so the complexity is O(n-W).

 Task complete: You have successfully used memoization.

Conclusion
 Congratulations! You now have successfully done the following:

Recognized the elements of a basic subset sum problem
Used recursion to solve the subset sum problem
Used memoization to solve the subset sum problem
Compared time and space complexity for the recursion and memoization approaches for the subset sum problem
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End Lab and then confirm that you want to end your lab.