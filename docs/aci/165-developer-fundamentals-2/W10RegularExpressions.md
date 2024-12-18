# Regular Expressions

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to repo's main [README.md](../../../README.md)

## Regular Expressions and Python RegEx Functions

### Pre-assessment

#### Which character set is used to search for an abcdefg match?

* [a-g]

Wrong answers:

* a-g
* [^a-g]
* ([a-g])

Square brackets ([ ]) in regular expressions are special characters, also known as metacharacters. Square brackets help you to define a character set, which is a set of characters that you want to match.

The other options are incorrect because:

* a-g would match the literal characters a , -, and g.
* [^a-g] would match all characters except a, b, c, d, e, f, and g.
* ([a-g]) would create a capture group for the set of characters a-g, but it is not used to create a character set.

#### Which line of code do you use to import the regular expression library in Python?

* import re

Wrong answers:

* import .re
* import RE
* import re:

The regular expressions module, called the **re** module, is built into Python. To start using regular expressions, type **import re** at the beginning of your code block. It is case sensitive, so use lowercase text.

The other options are incorrect because they are invalid import commands. They use either the wrong case (**import RE**) or wrong syntax (**import re:** and **import .re**).

#### What does the regular expression pattern \d do?

* It matches digits (0, 1, …, 9).

Wrong answers:

* It matches the special character dot (.).
* It matches any calendar date (mm-dd-yyyy).
* It matches any non-digit characters.

The backslash **(\)** followed by a lowercase **d** (**\d**) is a metacharacter in regular expressions that matches any single digit from zero through nine (0-9).

The other options are incorrect because of the following:

* The special character dot is matched by **(.)**.
* The calendar date is matched by **\d{2}-\d{2}-\d{4}**.
* The non-digit characters are matched by **\D**.

#### What does the regular expression pattern [^abc] do?

* It matches all characters except a, b, or c.

Wrong answers:

* It matches the characters abc in a sequence.
* It matches any one of the characters a, b, or c.
* It matches the characters cba in a sequence.

The caret (^) typically signifies the start of a line, but when placed inside square brackets at the beginning of a character set, it negates the set. Thus, the pattern [^abc] matches any character that is not a, b, or c.

The other options are incorrect because of the following:

* **abc** would match the characters **abc** in a sequence.
* **[abc]** would match any one of the characters **a**, **b**, or **c**.
* **cba** would match the characters **cba** in a sequence.

#### Which of these options could you use to match digits in a string? (Select TWO.)

* \d
* [0-9]

Wrong answers:

* \n
* \D
* [0-9]
* \S

The choice represented by **\d** (backslash-d) matches any single digit from zero through nine (0-9). Another correct choice involves specifying a range of numbers in square brackets, as in **[0-9]**, which matches any single digit in that range.

The other options are incorrect because of the following:

* **\n** matches any newline character.
* **\D** matches any non-digit characters.
* **\S** matches any non-whitespace characters.

## Regular Expressions

A regular expression, often abbreviated as RegEx, is a sequence of characters that forms a search pattern used for matching specific text within strings. These patterns facilitate text matching and manipulation operations, and provide a concise and flexible way to describe complex search criteria.

At their core, regular expressions consist of literal characters and special characters or sequences.

* **Literal characters** match exactly what they represent.
* **Special characters and sequences** represent specific patterns or classes of characters.

For example, the dot (**.**) is a special character that matches any character except a newline, and **\d** is a sequence that matches any digit character.

#### Literal characters example

* RegEx: **cat**
* String: "**The cat sat on the mat.**"
* Match: The word "**cat**" in the string.

In this case, the RegEx cat is made up of literal characters **c**, **a**, and **t**.

It will match the sequence of characters **cat** wherever it appears in the text exactly as it is.

#### Special characters example

* RegEx: **.** (dot)
* String: "**Fire, Fare, Furry.**"
* Match: The dot matches any single character, so if you use the RegEx **F.re**, it would match the words **Fire** and **Fare**, because the **.**(dot) matches any character at that position in the word.

#### Sequences example

A common example is the **\d** sequence, which is used to match any digit.

* RegEx: **\d**
* String: "Room **101**"
* Match: This will match the digits **1**, **0**, and **1** in **Room 101**.

Regular expressions also support various constructs, such as character classes, anchors, word boundaries, quantifiers, and groupings. These constructs permit you to define more complex patterns and control how the pattern matches the target string.

### History

In the 1950s, mathematician Stephen Cole Kleene laid the foundation for the theory of regular languages by developing regular expressions   and establishing their algebraic properties. 

In 1951, he wrote the first paper on regular events, and he officially coined the term regular expression' in 1956, inspired by his work with neural networks.

Regular expressions, often called RegEx, are powerful pattern-matching tools used in programming and text processing. They allow for precise descriptions of patterns in textual data, ranging from simple sequences of literal characters to complex symbolic patterns   used to find matches in text. 

Regular expressions have a wide range of applications and can be applied to various tasks in software development.

One common use of RegEx is to validate user input.

### Basic concepts of regular expressions

1. **Syntax**. The rules for writing regular expressions.
2. **Notation**. The set of symbols and characters used to represent a pattern within a regular expression.
3. **Matching**. Searching a string to find sequences that match the given RegEx pattern.
4. **Patterns**. Defined sequence of characters that represents a search pattern.
5. **Capturing**. Capturing parts of the matched string into groups for later use or manipulation.
6. **Substitution**. The process of replacing text that matches a RegEx pattern with a new string.
7. **Flags**. Instructions that can change how the RegEx engine interprets a pattern, such as with case sensitivity.

### Common concepts related to RegEx

#### Alternation

Alternation allows you to specify multiple search patterns using an OR or alternative operator. For example, to search through a document for case-sensitive letters, you can use the pipe operator (|) to find all the matches.

```
import re

string = "PYTHON python Python."
pattern = re.findall('(PY|py|Py)', string)
print(pattern)

Result: ['PY', 'py', 'Py']
```

#### Anchors

Anchors match a position, not characters, and match the start or end of a string. You can use the caret (^) metacharacter to match the beginning of a string and the dollar sign ($) to match the end.  

```
import re

string = "python is the best programming language"
pattern = re.findall('.$', string)
print(pattern)

Result: ['e'] 
```

(the $ only matched the last character)

#### Capture group

A capture group allows you to pull out sections of a string that match a pattern. Create a capture group by enclosing the pattern in parenthesis. They allow you to extract sections of a matching string and manipulate the data.

```
import re

string = "python"
pattern = re.findall('(th)', string)
print(pattern)

Result: ['th']
```

#### Character class

A character class allows you to define a set of characters that any single character in the search text can match. To use this function, put the characters between square brackets and RegEx will match any one of the characters specified within the brackets.

```
import re

string = "python"
pattern = re.findall('[th]', string)
print(pattern)

Result: ['t', 'h']
```

#### Literal character

A literal character is the character that you are matching. If you are searching for the letter p, you would type 'p' as your search term.

```
import re

string = "python"
pattern = re.findall('p', string)
print(pattern)

Result: ['p']
```

#### Metacharacters

Metacharacters are characters that have a special meaning. For example, the dot (.) is a metacharacter that matches any character except a newline. To use a metacharacter as a literal character, you often place a backslash (\) in front of it.

```
import re

string = "python"
pattern = re.findall('.', string)
print(pattern)

Result: ['p', 'y', 't', 'h', 'o', 'n']
```

#### Quantifiers

Quantifiers follow a portion of the RegEx and allow you to indicate how many characters or character classes should be matched. You can use the asterisk (*) to match zero or more instances of the preceding pattern, or the plus sign (+) to match one or more occurrences.

```
import re

text = "python is python"
matches1 = re.findall(r'p*', text)
matches2 = re.findall(r'p+', text) 
print("Result for matches1 with *: ", matches1) 

print("Result for matches2 with +: ", matches2) 

#Output

Result for matches1 with *:  ['p', '', '', '', '', '', '', '', '', '', 'p', '', '', '', '', '', '']

Result for matches2 with +:  ['p', 'p']
```

### General use cases for regular expressions

* Data validation
* Document redaction
* Firewall rule definitions
* Log filtering

#### Data validation

Let's describe an email address as consisting of three main parts—a series of characters representing the username, followed by an @ sign, and then another series of characters representing the domain name, which includes a period.

```
import re

def isFormattedCorrectly(email): 
    pattern = r'\S+@\S+\.\S+'
    result = re.findall(pattern, email)
    return len(result) > 0 

while True: 
    email = input("Please enter a properly formatted email address: ")
    if isFormattedCorrectly(email):
        print("Your email looks good, thank you! ")
        break
    else:
        print("EMAIL ADDRESS DOESN’T HAVE THE PROPER FORMAT")

```

The letter **r** at the beginning of this pattern, r'\S+@\S+\.\S+', in Python denotes a raw string, which treats backslashes as literal characters. Without the **r**, every backslash in the pattern would have to be doubled.

#### Log filtering

Computer systems generate vast quantities of logs. When addressing an issue, a system operator might need to filter these logs to focus specifically on errors marked as "CRITICAL". Regular expressions can facilitate this process effectively. In environments like Amazon CloudWatch Logs, you can create metric filters and subscription filters that use regular expressions. By employing a regular expression, you can efficiently narrow down enormous volumes of log data to only the critical records.

#### Firewall rule definitions

A common security challenge for website operators is protecting their systems against malicious attacks. It is essential to block requests that contain dangerous content, such as SQL injection attacks. Regular expressions can be instrumental in addressing this problem. For instance, in AWS WAF, regular expressions are used to define firewall rules. These regular expressions help identify malicious content, ensuring that it can be effectively blocked.

#### Document redaction

Many government and health regulations mandate that personally identifiable information (PII) be kept confidential. When a document containing PII has to be printed, it's crucial to redact any sensitive information beforehand. Amazon Macie is a service that identifies sensitive information through machine learning and pattern matching. To achieve this, Macie employs regular expressions to locate and redact sensitive information effectively.

### Regular Expressions in AWS Services

AWS WAF, a web application firewall, allows you to configure security rules using RegEx patterns. These rules can either block malicious web requests or allow requests that meet specific criteria, all defined by your RegEx patterns.

You can also use RegEx when querying logs in Amazon CloudWatch to effectively filter, search, and analyze your data.

Additionally, Amazon Macie allows you to create custom data identifiers using regular expressions. This feature enables you to define and detect sensitive data patterns in Amazon Simple Storage Service, or Amazon S3.

More broadly, regular expressions are supported in structured query language, or SQL, which is used to manage data in relational databases. Many modern relational database management systems provide support for regular expressions in their queries. For example, PostgreSQL and MySQL, both available for deployment on Amazon Relational Database Service, or Amazon RDS, allow for complex querying capabilities using RegEx.

### Using RegEx with both CloudWatch and Athena to facilitate the detection of error messages in logs

#### RegEx pattern

The RegEx pattern to identify HTTP 4XX and 5XX status codes in log entries is as follows:

```
(4\d\d|5\d\d)
```

This pattern looks for a 4 or 5, and two or more digits, which correspond to the status codes for client and server errors, respectively.

Log entries, especially from web servers, often follow a standardized format where the status code is preceded by a space or the end of the line.

#### Solution 1: Monitoring with CloudWatch

Amazon CloudWatch offers powerful metric filters, which let you transform log data into actionable metrics. These filters can be designed to match specific patterns or keywords within the logs, using regular expressions to define these criteria.

After a pattern is identified, CloudWatch can transform this data into a quantifiable metric, something that can be counted or measured over time. This is particularly useful for monitoring applications for specific events, such as error messages or specific status codes in web server logs.

Here are examples of log events that you might encounter in your web server logs, demonstrating both HTTP 404 and 500 errors.

```
2024-03-29T12:34:56 GET /nonexistent-page 404 
2024-03-29T12:35:07 POST /submit-data 500 
2024-03-29T12:35:12 GET /index.html 200 
2024-03-29T12:35:14 GET /styles.css 200
2024-03-29T12:35:16 GET /scripts.js 200 
2024-03-29T12:35:18 GET /images/logo.png 200 
2024-03-29T12:35:20 GET /about 200 
2024-03-29T12:35:22 GET /contact 200 
2024-03-29T12:35:24 GET /blog 200
2024-03-29T12:35:26 GET /blog/post-1 200
2024-03-29T12:35:28 GET /products 200 
2024-03-29T12:35:30 GET /products/item-1 200 
2024-03-29T12:35:32 GET /cart 200 
2024-03-29T12:35:34 GET /user/profile 200 
2024-03-29T12:35:36 GET /admin/dashboard 200 
2024-03-29T12:35:38 GET /api/data 200 
2024-03-29T12:35:40 GET /search?q=example 200 
2024-03-29T12:35:42 GET /missing-resource 404
```

By creating a metric filter based on the regular expression '**(4\d\d|5\d\d)**', you can track the occurrence of HTTP 4XX and 5XX error status codes in your application logs. The metric filter would increment a counter each time the pattern is found in the log data.

This helps you to not only gain insights into the frequency of these errors, but also take advantage of other CloudWatch features, like CloudWatch alarms, which can notify you when error rates exceed certain thresholds.

```
SELECT *
FROM "your_log_table"
WHERE regexp_like(request, '(4\d\d|5\d\d)')
```

The regular expression **(4\d\d|5\d\d)** would match the following requests in the web server log:

```
2024-03-29T12:34:56 GET /nonexistent-page 404
2024-03-29T12:35:07 POST /submit-data 500
2024-03-29T12:35:42 GET /missing-resource 404
```

#### Solution 2: Analysis with Athena

Amazon Athena is a serverless, interactive query service that you can use to analyze data directly in Amazon Simple Storage Service (Amazon S3) using standard SQL. In the context of web server logs, Athena can be used to perform detailed analysis of historical log data.

By writing SQL queries that incorporate regular expressions, users can filter and dissect log entries to extract meaningful insights. For example, when examining web server logs for errors, a regular expression can be used with an Athena SQL query to isolate entries that contain HTTP 4XX and 5XX error status codes.

After ensuring that the web server logs are stored in Amazon S3 and cataloged in Athena, you can use Athena to run a query that uses the RegEx pattern, as follows:

```
SELECT *
FROM "your_log_table"
WHERE regexp_like(request, '(4\\d\\d|5\\d\\d)')
```

In this sample query, **your_log_table** and **request** would have to be replaced with the actual table name and the column containing the request status codes, respectively.

You might have noticed that the regular expression is written as **(4\\d\\d|5\\d\\d)** instead of
**(4\d\d|5\d\d)**. This is because in the context of SQL, the backslash character (\) is considered an escape character. This means that to represent a literal backslash in a string in the query, you need to escape it by using a double backslash (**\\**).

### Python RegEx Functions

#### Python re module functions

The Python **re** module offers a variety of powerful functions that extend beyond the commonly used **re.findall()**. Although **re.findall()** is great for extracting all non-overlapping matches of a pattern, several other functions cater to different needs in pattern matching and text manipulation.

Here is an overview of some common functions provided by the re module.

* **re.findall()** finds all occurrences of a pattern in a string.
* **re.match()** finds a pattern match at the beginning of a string.
* **re.search()** searches for the first occurrence of a pattern anywhere in the string.
* **re.fullmatch()** checks whether the entire string matches the pattern.

#### re.findall() function

To begin exploring regular expressions, the re module offers a handy function called **re.findall()**. This function searches for all occurrences of a specified pattern in a given string and returns them as a list. It requires two arguments—the **pattern**, defined as a string containing the regular expression, and the **target** string to be searched.

Consider the following example, which uses the pattern "**o**" to search through the string "**Python can copy an object.**" The **re.findall()** function will return a list containing all instances where o appears in the target string.

```
import re

pattern = "o"
target = "Python can copy an object."
result = re.findall(pattern, target)
print(result)
```

Output

```
Result: ['o', 'o', 'o']
```

Notice that the function returns a list of three '**o**' characters. That is because the letter o appears three times in the string.

Now, let's change the pattern to "**on**".

```
import re

pattern = "on"
target = "Python can copy an object."
result = re.findall(pattern, target)
print(result)
```

Output

```
Result: ['on']
```

This time, the function returns a list with only one string. That is because the characters o and n together only appear one time in the target.

 If the pattern does not match anything in the target, the re.findall() function returns an empty list, indicating there is no match.

```
import re

pattern = "ok"
target = "Python can copy an object."
result = re.findall(pattern, target)
print(result)
```

Output

```
Result: []
```

```
import re

pattern = "py"
target = "Python can copy an object."
result = re.findall(pattern, target)
print(result)
```

Output:

```
Result: ['py']
```

#### Search ignoring case

```
import re 

pattern = "py" 
target = "Python can copy an object." 
# Using the re.IGNORECASE flag
result = re.findall(pattern, target, re.IGNORECASE)  
print(result) 
```

Output:

```
['Py', 'py']
```

#### Wildcard dot (**.**)

```
import re

pattern = "o."
target = "Python can copy an object."
result = re.findall(pattern, target)
print(result)
```

Output:

```
['on', 'op', 'ob']
```

#### re.match(), re.search(), and re.fullmatch() functions

The **re.match()** function checks for a match specifically at the beginning of the string, without considering the rest.

```
import re

sentence = "The dog is loyal."
result = re.match("loyal", sentence)
print(result)
```

Output:

```
Result: None
```

The result doesn't yield a match because the word **loyal** is not located at the beginning of the string.

```
import re

sentence = "The dog is loyal."
result = re.search("loyal", sentence)
print(result)
```

Output:

```
Result: <re.Match object; span=(11, 16), match='loyal'>
```

**re.search()** finds a match because it scans the entire string for the pattern. Indexes 11, 12, 13, 14, and 15 contain the letters l, o, y, a, and l respectively. The **re.search()** function outputs the starting index and up to, but not including, the ending index.

**re.fullmatch()** is searching for the entire string to match the pattern.

```
import re

sentence = "The dog is loyal."
result = re.fullmatch("loyal", sentence)
print(result)
```

Output:

```
Result: None
```

```
import re
sentence = "The dog is loyal."
result = re.fullmatch("The dog is loyal.", sentence)
print(result)
```

Output:

```
# Output:
<re.Match object; span=(0, 17), match='The dog is loyal.'>
```

### Knowledge Check

#### Which of these AWS services support RegEx-based searching? (Select TWO.)

* Amazon CloudWatch
* Amazon Athena

Wrong answers:

* Amazon DynamoDB
* Amazon S3
* Amazon S3 Glacier

* **Athena**: Athena is an interactive query service that you can use to analyze data in Amazon S3 using standard SQL. It supports RegEx-based searching in SQL queries, so you can perform pattern matching and text manipulation on your data.
* **CloudWatch**: CloudWatch is a monitoring and observability service that collects and manages log data from various AWS resources. It supports RegEx-based searching and filtering of log data, so you can search for specific patterns within your logs.

Incorrect responses:

* **DynamoDB**: DynamoDB is a fully managed NoSQL database service. Although it supports querying and filtering data, it does not natively support RegEx-based searching. You would need to implement RegEx functionality in your application code, if required.
* **Amazon S3**: Amazon Simple Storage Service (Amazon S3) is an object storage service. It does not provide built-in support for RegEx-based searching. However, you can use other AWS services like Athena or AWS Lambda to process and search data stored in Amazon S3 using RegEx patterns.
* **Amazon S3 Glacier**: Glacier is an archival storage class for Amazon S3 and does not support RegEx.

#### Which of these regular expressions would match only the HTTP 4XX and 5XX error status codes in application logs in Amazon CloudWatch?

* **(4\d\d|5\d\d)**

Wrong answers:

* (2\d\d|4\d\d)
* (\d\d)
* (2\d\d|4\d\d|5\d\d)

The following are incorrect because:

* (2\d\d|4\d\d) will match 2XX and 4XX errors.
* (\d\d) will match any occurrences of two digits in a row.
* (2\d\d|4\d\d|5\d\d) will match 2XX, 4XX, and 5XX errors.

#### Which of these Python RegEx functions finds all occurrences of a pattern in a string?

* re.findall()

Wrong answers:

* re.match()
* re.search()
* re.fullmatch()

The following are incorrect:

* re.match() because it finds a pattern match at the beginning of a string
* re.search() because it searches for the first occurrence of a pattern anywhere in the string
* re.fullmatch() because it checks if the entire string matches the pattern

#### What will the following Python code block output when the user enters user@domain in reply to the Please enter a properly formatted email address:  request when the code is run?

```
import re

def isFormattedCorrectly(email):
    pattern = r'\S+@\S+\.\S+'
    result = re.findall(pattern, email)
    return len(result) > 0
    
while True:
    email = input("Please enter a properly formatted email address: ") 
    if isFormattedCorrectly(email):
        print("Your email looks good, thank you!")
        break
    else:        
         print("EMAIL ADDRESS DOESN'T HAVE THE PROPER FORMAT")
```

* EMAIL ADDRESS DOESN'T HAVE THE PROPER FORMAT

Wrong answers:

* user@domain
* Your email looks good, thank you!
* "Please enter a properly formatted email address: "

All the other responses are incorrect, because the given Python code is designed to validate email addresses using a regular expression pattern.

* The **user@domain** option is incorrect because it is not the output of the given Python code block. The code prompts the user to enter a properly formatted email address and then checks if the entered email address matches the specified regular expression pattern. If the email format is correct, it prints **Your email looks good, thank you!** and exits the loop. If the email is improperly formatted, it prints **EMAIL ADDRESS DOESN'T HAVE THE PROPER FORMAT**.
* The **Your email looks good, thank you!** option is incorrect because it is not the output for the input **user@domain**. The regular expression pattern used in the **isFormattedCorrectly** method is **r'\S+@\S+\.\S+'**. This pattern requires at least one non-whitespace character before the at sign (**@**), at least one non-whitespace character after the at sign and before the period (.), and at least one non-whitespace character after the period. The input **user@domain** does not match this pattern, because it lacks a top-level domain (for example, .com, .org, .edu) after the domain name. Therefore, the code will print **EMAIL ADDRESS DOESN'T HAVE THE PROPER FORMAT** for the input **user@domain**.
* The **Please enter a properly formatted email address:** option is incorrect because it is not the output of the code block. It is the prompt that displays to a user to enter a properly formatted email address. The code does not print this string as output; it is used as the input prompt.

### Summary

Regular expressions can be used with various AWS services. For example, in AWS WAF, you can set up rules to allow or block web requests based on whether they match specific patterns, as defined by regular expressions.

In your work with regular expressions in Python, you start by importing the re module, which is part of the Python Standard Library and provides support for regular expression operations.

The regular expression function **re.findall()** can be used to find all occurrences of a pattern in a string. There's a bunch of other regular expression functions, such as **re.search()**, **re.match()**, and **re.fullmatch()**. These functions can facilitate your operations when searching through text to find matches for specific patterns.

The RegEx syntax and basic concepts of regular expressions include **notation**, **matching**, **patterns**, **capturing**, **substitution**, and **flags**. Common syntax elements are:

* Alternation
* Anchors
* Capture groups
* Character classes
* Literal characters
* Metacharacters
* Quantifiers

## RegEx Syntax

In RegEx, all characters are categorized into two groups—literal characters and metacharacters. By using both literal characters and metacharacters, you can perform searches ranging from simple to complex.

### Literal characters

Literal characters, also known as ordinary characters, match exactly what they represent and have a literal meaning in RegEx. For instance, if you are searching for the sequence **py**, you would simply use **'py'** as your search term. Most characters in RegEx are considered literal characters.

The following block of code illustrates this principle. The pattern is the characters **py**. The target string is **'Python can copy an object.'** The **re.findall()** function will search for all occurrences of the pattern in the target.

```
import re

pattern = 'py'
target = 'Python can copy an object.'
result = re.findall(pattern, target)

print(result)
```

Output:

```
Result: ['py']
```

#### Code explanation

This code searches for **py** in the target string, Python can copy an object.
The result tells you that there is one occurrence of **'py'**.

'Python can co*py* an object.'

Notice that the result does not include **Py** at the beginning of the target string due to RegEx being case-sensitive. Therefore, **pattern = 'py'** only finds lowercase instances in the target.

### Metacharacters

Regular expressions reserve certain characters for more complex types of searching. These characters are known as special characters, or metacharacters. The following list presents some commonly used metacharacters:

* **Asterisk (*)**: Matches zero or more occurrences of the preceding character, group, or character class
* **Backslash (\)**: Escapes special characters, allowing them to be used as literal characters
* **Caret (^)**: Indicates that the following pattern must appear at the beginning of the string or line
* **Dollar sign ($)**: Indicates that the preceding pattern must appear at the end of the string or line
* **Dot (.)**: Matches any single character, except for a newline character
* **Pipe (|)**: Matches either of the expressions appearing before or after the pipe
* **Plus sign (+)**: Matches the preceding character, group, or character class at least once
* **Question mark (?)**: Matches the preceding character, group, or character class either zero or one time
* **Round parentheses (( ))**: Groups parts of expressions or characters together
* **Square brackets ([ ])**: Finds a set of characters that match the characters inside the brackets

#### . Dot

The **dot (.)** metacharacter acts like a wildcard. It matches any single character, except for newline characters.

Consider this example:

```
pattern = '.'
target = ('Python can copy an object.')
result = ['P', 'y', 't', 'h', 'o', 'n', ' ', 'c', 'a', 'n', ' ', 'c', 'o', 'p', 'y', ' ', 'a', 'n', ' ', 'o', 'b', 'j', 'e', 'c', 't', '.']
```

The result displays all characters in the target, including the spaces between words and the period at the end of the sentence.

The following RegEx code looks for matches where the letter **o** is followed by any other single character:

```
pattern = 'o.'
target = 'Python can copy an object.'
result = ['on', 'op', 'ob']
```

If you are specifically looking to match the period character (.) itself in the target, you would need to use the **backslash metacharacter (\)** before the dot (.) to treat it as a literal character.

#### + Plus

The **plus sign (+)** metacharacter specifies that the preceding character must occur one or more times in the target string.

In the following example, the pattern **'e+'** is used to find occurrences where there is at least one **e** character. As this metacharacter matches one or more of the preceding elements, it returns the longest sequence possible each time it finds a match.

```
pattern = 'e+'
target = 'trees'
result = ['ee']
```

In this example, the pattern **'e+'** matches the consecutive **ee** in the word **trees**, returning **'ee'** because the + quantifier aggregates all consecutive e characters into a single match.

#### \ Backslash

The **backslash (\)** metacharacter is used to turn metacharacters into literal characters.

For example, consider the following RegEx snippet that searches for the period (.) at the end of a target string:

```
pattern = '\.'
target = 'Python can copy an object.'
result = ['.']
```

Compare the following two patterns:

* **pattern =  '.'** – Here, the dot is a metacharacter that matches any single character except newline in the target string.
* **pattern = '\.'** – Here, the backslash-dot combination is an escaped character, specifically used to find literal periods in the target string.

The backslash serves two purposes:

* **Escape metacharacters**: When the backslash precedes a metacharacter, it neutralizes the special meaning of the metacharacter, making it act as a regular character for matching.
* **Define special sequences**: The backslash also introduces special sequences that have specific meanings in RegEx. These are not literal character matches but are instead used to denote character classes, backreferences, or other special RegEx constructs.

#### | Pipe operator

The **pipe (|)** operator signifies alternation in RegEx language, indicating **OR**.

For example, consider the following RegEx snippet that searches for either the name **Joe** or the name **Justin** in the target string:

```
pattern = 'Joe|Justin'
target = 'Joe or Justin could go buy the groceries.'
result = ['Joe', 'Justin']
```

Take a look at the pattern:

```
pattern =  'Joe|Justin'
```

Here, the pipe is a metacharacter that matches either what is to the left or right of it.

### Introduction to character classes

A character class, also known as a *character set*, is a fundamental component of regular expressions that allows for flexible pattern matching. By placing a set of characters within square brackets, you instruct the RegEx engine to match any one of those characters in the target string. This makes character classes extremely useful for matching any specific set of characters at a given position in the text.

Review the following code and the result.

```
import re

pattern = '[aeiou]'
target = 'Python can copy an object.'
result = re.findall(pattern, target)
print (result)
```

```
Result: ['o', 'a', 'o', 'a', 'o', 'e']
```

#### Code explanation

This code looks for any of these letters [aeiou] in the target string, and the result displays all occurrences.

Pyth*o*n c*a*n c*o*py *a*n *o*bj*e*ct.

```
result = ['o', 'a', 'o', 'a', 'o', 'e']
```

#### REMEMBER

Python does not generally display a syntax error for a backslash in a RegEx pattern unless the backslash leads to a syntactically incorrect escape sequence. However, to avoid any confusion or errors related to the handling of backslashes, especially in complex RegEx patterns, it is a good practice to use raw strings. Prefixing your RegEx pattern with the letter **r** forms a raw string and ensures that all backslashes are treated as literal characters rather than escape characters.

```
pattern = r'\.'
```

In Python, a backslash **(\)** in standard strings is used to introduce special character sequences, such as **\t** for a tab or **\n** for a newline. Using the **r** prefix to create a raw string prevents these sequences from being processed as escapes, which is particularly useful in RegEx to ensure that backslashes are interpreted correctly by the RegEx engine, not by Python as escape characters. Alternatively, you can escape the backslash itself, as follows:

```
pattern = '\\.'
```

#### RegEx Example 1

```
import re
text = "This might cost as much as $17.35."
matches = re.findall('cost', text)
print(matches)
```

```
Result: ['cost']
```

In this example, the code is simply matching the word **cost** in the text **"This might cost as much as $17.35."**. The pattern contains literal characters without any special RegEx symbols, so it directly matches the exact substring in the text. The output, as expected, is **'cost'**.

#### RegEx Example 2

```
import re
text = "This might cost as much as $17.35."
matches = re.findall('.s', text)
print(matches)
```

```
Result: ['is', 'os', 'as', 'as']
```

The regular expression pattern **.s** is designed to find sequences where any character **(.)** is followed directly by an **s**. Each match in the result involves a character followed directly by **s**, which is exactly what the pattern seeks to capture.

#### RegEx Example 3

```
import re
text = "This might cost as much as $17.35."
matches = re.findall(r'\.', text)
print(matches)
```

```
Result: ['.', '.']
```

The code escapes the period by preceding it with a backslash **(\)** in the pattern. This tells Python to treat the dot as a literal period, not as a metacharacter. Because the sample text contains two periods, the RegEx successfully identifies and matches both of them.

#### RegEx Example 4

```
import re
text = "This might cost as much as $17.35."
matches = re.findall('[abcdef]', text)
print(matches)
```

```
Result: ['c', 'a', 'c', 'a']
```

Using the character set **[abcdef]**, the pattern matches any individual **a**, **b**, **c**, **d**, **e**, or **f** character found in the text. The matches include **c** from **cost**, **a** from **as**, **c** from **much**, and another **a** from the second **as**, totaling four occurrences.

#### Quick Review

| Target | Pattern | Result |
| ---------------------------------- | ------ | -------- |
| This might cost as much as $17.35. | 'cost' | ['cost'] |
| This might cost as much as $17.35. | '.s' | ['is', 'os', 'as', 'as'] |
| This might cost as much as $17.35. | r'\.' | ['.', '.'] |
| This might cost as much as $17.35. | '[abcdef]' | ['c', 'a', 'c', 'a'] |

### Creating special sequences with the backslash

Two distinct uses of the backslash metacharacter:

* Converting a metacharacter into a literal character
* Transforming a literal character into a special sequence

Special sequences with backslashes:

* **\A** matches the expression at the start of a string, whether single-line or multi-line.
* **\b** matches the empty string at the word boundary, either at the beginning or the end of a word.
* **\B** matches positions where \b does not, typically within words.
* **\D** matches any non-digit character, equivalent to **[^0-9]**.
* **\s** matches any whitespace character, including tab **(\t)**, newline **(\n)**, return **(\r)**, and space.
* **\S** matches any non-whitespace character.
* **\W** matches non-alphanumeric characters, equivalent to **[^a-zA-Z0-9]**.
* **\Z** matches the position at the end of a string.
* **\w** searches for alphanumeric characters (including the underscore), shorthand for **[a-zA-Z0-9_]**.
* **\d** searches for digits in a target, serving as shorthand for the zero through nine character set **[0-9]**.

#### Example 1 – \w

The following code searches for just the **w** character in a string pattern.

```
import re

pattern = 'w'
target = 'Python can copy an object'
result = re.findall(pattern, target)
print (result)
```

Output:

```
Result: []
```

Notice that an empty result is returned because there are no **w** characters in the target string.

The addition of a backslash in the pattern transforms the variable to a RegEx special character, **(\w)**.

```
import re

pattern = '\w'
target = 'Python can copy an object'
result = re.findall(pattern, target)
print (result)
```

Output:

```
Result: ['P', 'y', 't', 'h', 'o', 'n', 'c', 'a', 'n', 'c', 'o', 'p', 'y', 'a', 'n', 'o', 'b', 'j', 'e', 'c', 't']
```

#### Example 2 – \d

The **\d** searches for only numeric characters, as opposed to both numbers and letters.

```
import re

pattern = 'd'
target = 'This will cost about $17.35.'
result = re.findall(pattern, target)
print (result)
```

Output:

```
result: []
```

The **'d'** searches for the **d** character in the text. The result is an empty list. This tells you that the letter d does not exist in the target.

The addition of a backslash in the pattern transforms the variable into a RegEx special character, **(\d)**.

```
import re

pattern = '\d'
target = 'This will cost about $17.35.'
result = re.findall(pattern, target)
print (result)
```

Output:

```
result: ['1', '7', '3', '5']
```

### Special sequence \w+

The **plus sign (+)** metacharacter instructs the pattern-matching engine to repeat the preceding regular expression one or more times in the target string.

```
import re

pattern = r'\w+'
target = 'This will cost about $17.35'
result = re.findall(pattern, target)
print (result)
```

```
Result: ['This', 'will', 'cost', 'about', '17', '35']
```

The **\w+** pattern matches each sequence of word characters (alphanumeric characters and underscores) in the target string.

In the previous example, notice that both **17** and **35** are included in the results. This is because **\w** matches all alphanumeric characters (letters and digits), not punctuation such as the dot. Consequently, **17** and **35** are identified as separate words due to the decimal point between them. It's important to remember that a decimal point—a dot (.)—is not considered an alphanumeric character and therefore is not matched by **\w**.

Adding a **+** after **\w** changes the behavior significantly. The plus sign is a quantifier in RegEx that means "one or more" of the preceding elements.

Therefore, **\w+** matches one or more consecutive alphanumeric characters or underscores. This quantifier tells the RegEx engine to match as long a sequence as possible of consecutive **\w** characters.

Using **\w+** is particularly useful when you want to extract whole words or numbers from a text, because it simplifies capturing these elements by automatically grouping all contiguous **\w** characters. This makes it highly effective for tasks like parsing text for words or processing log files to extract numeric identifiers.

#### Examples

```
target = 'This will cost $17.35.'
pattern = r'\w'
result = ['T', 'h', 'i', 's', 'w', 'i', 'l', 'l', 'c', 'o', 's', 't', '1', '7', '3', '5']
```

```
target = 'This will cost $17.35.'
pattern = r'\w\w'
result = ['Th', 'is', 'wi', 'll', 'co', 'st', '17', '35']
```

```
target = 'This will cost $17.35.'
pattern = r'\w\w\w'
result = ['Thi', 'wil', 'cos']
```

```
target = 'This will cost $17.35.'
pattern = r'\w+'
result = ['This', 'will', 'cost', '17', '35']
```

```
import re
text = "This might cost as much as $17.35."
pattern = r'\d'
result = re.findall(pattern, text)
print(result)

Result: ['1', '7', '3', '5']
```

```
import re
text = "This might cost as much as $17.35."
pattern = r'\d\d'
result = re.findall(pattern, text)
print(result)

Result: ['17', '35']
```

```
import re
text = "This might cost as much as $17.35."
pattern = r'\$\d\d\.\d\d'
result = re.findall(pattern, text)
print(result)

Result: ['$17.35']
```

```
import re
text = "This might cost as much as $17.35."
pattern = r'\$[0123456789][0123456789]\.[0123456789][0123456789]'
result = re.findall(pattern, text)
print(result)

Result: ['$17.35']
```

### Pipe operator (|)

Use the pipe operator to retrieve multiple words in a search. The pipe operator signifies alternation in RegEx language, indicating OR.

```
import re
string = "Regular expressions are useful search tools."
match = re.findall("Regular|tools", string)
print(match)

Result: ['Regular', 'tools']
```

## Anchors and Word Boundaries

### Anchors

*Anchor* metacharacters specify where to look for a pattern string within a target string. In this lesson, you will learn how to find pattern strings at the beginning or the end of a target string by using the caret **(^)** and the dollar sign **($)** anchors.

* The **caret sign (^)** indicates that a match should be at the beginning of the string. In other words, it anchors a pattern to the start of a line or string.
* The **dollar sign ($)** denotes the end of the line or end of string match. It is the counterpart to the caret (^) sign, marking the end rather than the beginning.

#### Caret sign (^)

##### Example 1

```
import re

pattern = '^Python'
target = 'Python can copy objects. What else can Python do?'
result = re.findall(pattern, target)
print (result)

Result: ['Python']
```

##### Example 2

```
import re

pattern = '^can'
target = 'Python can copy objects. What else can Python do?'
result = re.findall(pattern, target)
print (result)

Result: []
```

##### Example 3

```
import re

pattern = '^\w+'
target = 'Python can copy objects. What else can Python do?'
result = re.findall(pattern, target)
print (result)

Result: ['Python']
```

#### Dollar sign ($)

The dollar sign is used to anchor a search to the end of a string, allowing you to match the last word, the last characters, or a specific word that appears at the end of the string.

```
import re

pattern = '...$'
target = 'Python can copy objects. What else can Python do?'
result = re.findall(pattern, target)
print (result)

Result: ['do?']
```

#### Validating email address formats with anchors in RegEx

```
import re

pattern = r'^\w+@\w+\.\w+$'
email = "example@email.com"
match = re.match(pattern, email)
print("Match" if match else "No match")
```

```
Result: Match
```

This pattern uses the **^** anchor to start matching at the beginning of the string and the **$** anchor to ensure that it ends exactly where we expect. The **\w+** matches one or more word characters before and after the **@**, ensuring that the email address starts with an alphanumeric character and includes a domain name followed by a top-level domain (**.com**). Given that the example email address adheres to these specifications, it results in a **Match**.

```
import re
pattern = r'^\w+@\w+\.\w+$'
email = " @email.com"
match = re.match(pattern, email)
print("Match" if match else "No match")
```

```
Result: No match
```

Because the email address starts with a space character, it results in **No match**. This demonstrates the strict requirement enforced by the caret anchor for the pattern to match from the very start of the string.

```
import re
pattern = r'^\w+@\w+\.com$'
email = "example@website.com"
match = re.match(pattern, email)
print("Match" if match else "No match")
```

```
Result: Match
```

By adjusting the pattern to **\.com$**, we ensure that the email address must end with **.com**. This makes our RegEx more suited for situations where domain-specific validation is crucial.

```
import re
pattern = r'^\w+@\w+\.com$'
email = "example@website.org"
match = re.match(pattern, email)
print("Match" if match else "No match")
```

```
Result: No match
```

This pattern fails to match the email address because it ends with **.org** instead of **.com**, illustrating how the dollar sign anchor can be used to enforce specific domain endings for certain validations.

### Word boundaries

The **\b** sequence is used to find word boundaries in a target string. Word boundaries represent positions where words start or end. **\b** does not match any characters; instead, it matches the position between word characters and non-word characters.

Word boundaries are useful when searching for whole words, because they denote the start and end of a word. For example, the RegEx pattern **\bout\b** searches specifically for the word out as a standalone entity. It will only return matches where **out** appears as a distinct word, not part of another word like *out*er, ab*out*, or b*out*ique.

If you want to find the occurrence of **out** in the word **boutique**, use **\B** instead of **\b**. **\B** finds matches where the specified pattern is not at a word boundary, meaning that it is preceded and followed by other letters or characters. Therefore, the pattern **\Bout\B** effectively locates the out in **boutique**.

* **\b** matches positions where a word boundary exists, which is ideal for isolating whole words.
* **\B** matches positions where no word boundary exists, which is perfect for identifying segments in larger words.

#### Word boundaries on both sides

Word boundaries on both sides ensure precise matching. The pattern **r'\bout\b'** specifically searches for the string out as a standalone word, not as part of another word.

Notice the **\b** both before and after the target string. This ensures that out is isolated as a separate word.

#### Word boundary at the beginning of a word

Using a word boundary at the beginning of a word ensures that the pattern only matches when the word starts with the specified string. The pattern **r'\bout'** is designed to find words that **begin with out**, such as **outside** and **outer**.

Notice that the **\b** is placed before the character string **out**. This placement ensures that **out** must be at the start of the word, preventing matches where **out** appears in the middle or at the end of a word.

#### Word boundary at the end of a word

Placing a word boundary at the end of a word ensures that the pattern only matches when the word ends with the specified string. The pattern **r'out\b'** is specifically designed to find words that **conclude with out**, such as **about** and **without**.

Notice that the **\b** is positioned after the character string **out**. This placement guarantees that out must be at the end of the word, ensuring that it does not match words where out appears at the beginning or in the middle.

#### Matching words using word boundaries

```
import re
text = "the theory was that they would help."
matches = re.findall(r'\bthe\b', text)
print(matches)
```

```
Result: ['the']
```

Here, **'\bthe\b'** targets the when it stands as a separate word. This pattern matches **the** at the beginning because it is surrounded by spaces—true word boundaries. It ignores any **the** that is part of another word, like **theory** or **they**.

```
import re
text = "the theory was that they would help."
matches = re.findall(r'\bthe', text)
print(matches)
```

```
Result: ['the', 'the', 'the']
```

With the pattern **'\bthe'**, the code looks for the that starts a word or segment, without requiring it to be a standalone word. This captures **the** at the beginning and also in **theory** and **they**.

```
import re
text = "the theory was that they would help."
matches = re.findall(r'\Bthe\B', text)
print(matches)
```

```
Result: []
```

You use the pattern **'\Bthe\B'** to find occurrences of the that are not at the beginning or end of a word. The **\B** (non-word boundary) asserts that the position should not be at the start or end of a word. In the example text, the word **the** appears at the start of the text and as a separate word, so it doesn't match the pattern. This results in no matches and an empty list as the output.

```
import re
text = "the theory was that they would help."
matches = re.findall(r'the\B', text)
print(matches)
```

```
Result: ['the', 'the']
```

This **'the\B'** variation matches **the** at the beginning of words such as in **theory** and **they**, but it does not match the standalone word **the**.

#### Capturing every complete word

```
import re
text = "the theory was that they would help."
matches = re.findall(r'\b\w+\b', text)
print(matches)
```

```
Result: ['the', 'theory', 'was', 'that', 'they', 'would', 'help']
```

The pattern **'\b\w+\b'** captures entire words, from beginning to end, demonstrating the versatility of word boundaries in isolating full words.

### Knowledge Check

#### What does the regular expression pattern n+ match in a string?

* One or more consecutive n characters

Wrong answers:

* A single n only
* Any string that does not contain n
* Zero or more n characters

The **plus sign (+)** is a quantifier that matches one or more occurrences of the preceding element. 

Therefore, the pattern **n+** specifically matches sequences where the letter **n** appears consecutively one or more times.

This means that it will match **n**, **nn**, **nnn**, and so on, but it will not match an empty string or strings without **n**.

#### What does the regular expression pattern [aeiou] match in the following script?

```
import re
text = "Simple script"
matches = re.findall("[aeiou]", text)
print(matches)
```

* It matches any vowels in the text.

Wrong answers:

* It matches the word script only.
* It does not match anything in the text.
* It matches the exact string [aeiou].

Square brackets **([ ])** denote a character class, which is used to match any one of the characters enclosed within the brackets.

In this case, the character class **[aeiou]** is used to match any single vowel in the string. 

Therefore, the pattern finds all instances of **a**, **e**, **i**, **o**, and **u** in the text, which are the vowels.

The output of this script will be **['i', 'e', 'i']**.

#### Which RegEx pattern should you use to extract all individual words from the text in the following script?

```
import re
text = "Hello, world! Welcome to coding."
matches = re.findall("_____", text)
print(matches)
```

* r'\w+'

Wrong answers:

* [^a-zA-Z]
* [a-zA-Z]+
* r'\s+'

The special sequence **r'\w+'** in regular expressions matches one or more word characters. A word character is any letter, decimal digit, or underscore (_), that corresponds to the RegEx shorthand character class **[a-zA-Z0-9_]**.

For the given text, the pattern **r'\w+'** will output **['Hello', 'world', 'Welcome', 'to', 'coding']**, because it skips over spaces and punctuation, capturing only the sequences of word characters.

#### Which RegEx pattern would correctly identify the word cat when it appears at the beginning of a word and which do the same when it appears as a standalone word within a text? (Select TWO.)

* r'\bcat\b'
* r'\bcat'

Wrong answers:

* cat
* r'cat\b'
* r'\Bcat\B'

The pattern **r'\bcat\b'** uses the **\b** word boundary both before and after cat, ensuring that cat is matched only if it appears as a standalone word.

The pattern **r'\bcat'** uses the **\b** word boundary before **cat**, which allows it to match cat when it appears at the beginning of a word. It will correctly identify **cat** in contexts like **catalog** or **catastrophe** where **cat** starts the word.

#### Which RegEx pattern is needed to check if a given text begins with the word Start?

* ^Start

Wrong answers:

* Start
* Start$
* ^Start$

The caret (^) anchor is specifically used to ensure that a pattern matches only at the beginning of the string. By using the pattern **^Start**, you ensure that the RegEx engine checks whether the string starts precisely with the word **Start**.

### Summary

* Literal characters and metacharacters in regular expressions
* Character classes and special sequences in regular expressions
* Anchors and word boundaries in regular expressions

#### Ordinary characters and metacharacters

Ordinary characters, also known as literal characters, match exactly what they represent and carry literal meanings in RegEx. Most characters used in RegEx are considered ordinary characters.

Metacharacters are special characters reserved in RegEx for more complex search operations. Throughout this topic, you have learned how to use various metacharacters.

#### Metacharacters

##### Backslash (\)

The backslash (\) serves two purposes:

* When the backslash precedes a metacharacter, it neutralizes the special meaning of the metacharacter, making it act as a regular character for matching.
* The backslash also introduces special sequences that have specific meanings in RegEx.

```
pattern = '\.'
target = 'Python can copy an object.'
result = ['.']
```

##### Caret (^)
The caret (^) is an anchor that indicates the following pattern must appear at the beginning of the string or line.

```
pattern = '^Python'
target = 'Python can copy objects. What else can Python do?'
result = ['Python']
```

##### Dollar sign ($)

The dollar sign ($) is an anchor that indicates the preceding pattern must appear at the end of the string or line.

```
pattern = '...$'
target = 'Python can copy objects. What else can Python do?'
result = ['do?']
```

##### Dot (.)
The dot (.) metacharacter acts like a wildcard. It matches any single character, except for newline characters.

```
pattern = '.'
target = 'Python can copy an object.'
result = ['P', 'y', 't', 'h', 'o', 'n', ' ', 'c', 'a', 'n', ' ', 'c', 'o', 'p', 'y', ' ', 'a', 'n', ' ', 'o', 'b', 'j', 'e', 'c', 't', '.']
```

##### Plus sign (+)
The plus sign (+) matches the preceding character, group, or character class at least once.

```
pattern = 'e+'
target = 'trees'
result = ['ee']
```

##### Square brackets ([ ])
Square brackets ([ ]) define a character set. By placing a set of characters within square brackets, you instruct the RegEx engine to match any one of those characters in the target string.

```
pattern = '[aeiou]'
target = 'Python can copy an object.'
result = ['o', 'a', 'o', 'a', 'o', 'e']
```

#### Special sequences

Special sequences are created by adding a backslash (\) in front of certain ordinary characters or metacharacters, forming combinations that simplify and facilitate common search patterns. These sequences make it easier to conduct complex searches with greater efficiency. You learned about special sequences like **\d**, **\w**, and **\w+**.

#### Anchors and word boundaries

Anchors and word boundaries are essential tools in RegEx for specifying the exact location where a pattern should match within the target string: **\b**, **\B**, **^**, and **$**.

## Quantifiers

### The concept of quantifiers

With quantifiers, a type of metacharacter in a regular expression (RegEx), you can specify the quantity of a match. You can also define how many times a given character or group of characters should be matched, accommodating patterns of various sizes.

Quantifiers are categorized as either greedy or lazy. A greedy quantifier attempts to match as much of the string as possible, capturing the largest possible string that fits the pattern. In contrast, a lazy (or non-greedy) quantifier aims to match as little of the string as possible, capturing the smallest possible string that fits the pattern.

| Quantifier | Name | Meaning | Example |
|----------- | ---- | ------- | ------- |
| * | Asterisk | Matches zero or more occurrences of the preceding element | a* matches "", "a", "aa", "aaa", and so on. |
| + | Plus sign | Matches one or more occurrences of the preceding element | a+ matches "a", "aa", "aaa", and so on, but not "". |
| ? | Question mark | Matches zero or one occurrence of the preceding element, making it optional | a? matches "", "a", but not "aa". |
| {n} | Brace quantifier | Matches exactly n occurrences of the preceding element. | a{3} matches "aaa", but not anything with more than 3 "a" characters. |
| {n,} | Brace quantifier | Matches at least n occurrences of the preceding element | a{2,} matches "aa", "aaa", and so on. |
| {m,n} | Brace quantifier | Matches from m to n occurrences of the preceding element | a{2,4} matches "aa", "aaa", or "aaaa". |

### The ? quantifier when used with re.findall()

```
import re
letters = "pyyyyyyyyy"
quantifier=re.findall('py?',letters)
print (quantifier)
```

Output:

```
Result: ['py']
```

The question mark quantifier affects the character immediately preceding it, making that character optional. Therefore, in the provided code, **re.findall('py?', letters)** looks for occurrences of *p* followed by zero or one y. The match found in the string **"pyyyyyyyyy"** is **'py'**, where **p** is followed by a single *y*. The ? means it will match **p** by itself or **p** followed by one y, but it does not extend to more than one **y**.

### The * quantifier when used with re.findall()

```
import re
letters = "pyyyyyyyyy"
quantifier=re.findall('py*',letters)
print (quantifier)
```

Output:

```
Result: ['pyyyyyyyyy']
```

This time, the * quantifier matches zero or more occurrences of the preceding element. So, it returns all of the **y** characters following **p** in the string. In contrast, the quantifier **?** only matches zero or one occurrence of the preceding element, which is why it didn't match the entire string of **y** characters.

```
import re
letters = "pppppppppp"
quantifier=re.findall('py*',letters)
print (quantifier)
```

Output:

```
Result: ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p']
```

The asterisk quantifier matches zero or more occurrences of the preceding element, which here is the letter **y**. Because there are no **y** characters in the string letters, the pattern py* will match the **p** characters that are not followed by a **y**. Therefore, the **re.findall('py*', letters)** call will return a list of **p** characters from the string.


```
import re
letters = "pppppppppp"
quantifier=re.findall('py+',letters)
print (quantifier)
```

Output:

```
Result: []
```

### Greedy and lazy quantifiers

Quantifiers in regular expressions are categorized as greedy or lazy based on how they search and match patterns within a string. Greedy quantifiers attempt to match as much of the input as possible, whereas lazy quantifiers match as little as possible, taking a more conservative approach.

#### Greedy quantifiers

Greedy quantifiers, such as ?, *, +, and {m,n}—where m and n are placeholders for numbers specifying a range—are called greedy because they attempt to match as many characters as possible. This approach is often referred to as finding the longest possible match.

```
import re
greedy='aaaaaaaaaa'
letters= re.findall('a?',greedy)
print(letters)
```

Output:

```
Result: ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', '']
```

Because ? makes the preceding character optional, it matches either zero or one a. Each a in the string **aaaaaaaaaa** is matched by **a?** because the pattern can match one occurrence of **a**. After matching the last **a**, the RegEx engine checks the position at the end of the string. Although there are no more a characters to match, the pattern **a?** still matches an empty string because it can match zero occurrences of **a**. This is a standard behavior of RegEx quantifiers, which check for matches even at the string's end.

The ? quantifier demonstrates its greedy nature by ensuring that every possible occurrence of **a** is matched, and then extends its reach to include an additional match of an empty string at the end of the string, maximizing the number of matches.

```
import re
greedy='aaaaaaaaaa'
letters= re.findall('a*', greedy)
print(letters)
```

```
Result: ['aaaaaaaaaa', '']
```

The *quantifier matches zero or more occurrences of the preceding element, which here groups all consecutive a characters together, because it seeks the longest possible sequence without interruption. An empty string at the end of the string is also included in the results.

```
import re
greedy='aaaaaaaaaa'
letters= re.findall('a+', greedy)
print(letters)
```

```
Result: ['aaaaaaaaaa']
```

The + quantifier is used to find one or more consecutive occurrences of a in the string. This results in the list **['aaaaaaaaaa']**, which captures all the **a** characters grouped together as a single match.

Unlike the ? and * quantifiers, which match zero occurrences and can thus include an empty string at the end of the search, the + quantifier requires at least one occurrence of a to make a match. Therefore, it does not return an empty string at the end, because there are no zero occurrences of a to match.

Another commonly used greedy quantifier is the exact match, denoted by **{m}**, where **m** represents a specific number of occurrences.

```
import re
greedy='aaaaaaaaaa'
letters= re.findall('a{2}',greedy)
print(letters)
three_letters = re.findall('a{3}',greedy)
print(three_letters)
```

```
Result:

['aa', 'aa', 'aa', 'aa', 'aa']
['aaa', 'aaa', 'aaa']
```

The pattern **'a{2}'** searches for occurrences of two consecutive a characters in the string. The result is **['aa', 'aa', 'aa', 'aa', 'aa']**, showing five groups of two a characters each, which covers all 10 a characters in the string. Subsequently, the pattern **'a{3}'** is used to find occurrences of three consecutive a characters. This results in **['aaa', 'aaa', 'aaa']**, which shows three groups of three a characters each. Both patterns demonstrate the use of the **{m}** quantifier to match precise numbers of consecutive characters.

### Non-greedy quantifiers

Non-greedy quantifiers, also known as lazy quantifiers, include ??, *?, +?, and {m,n}?. These quantifiers are designed to find the smallest possible match, meaning they capture the fewest characters necessary to satisfy the pattern. For example, when the pattern **a+?** is applied to the string **aaaa**, it matches only the first **a** instead of the entire string of **a** characters. This demonstrates the non-greedy or lazy behavior by stopping at the shortest match possible.

```
import re 

lazy = 'aaaabac' 

# Greedy matching 
greedy_pattern = 'a+' 
greedy_matches = re.findall(greedy_pattern, lazy) 
print("Greedy matches:", greedy_matches) 

# Non-greedy matching 
non_greedy_pattern = 'a+?' 
non_greedy_matches = re.findall(non_greedy_pattern, lazy) 
print("Non-greedy matches:", non_greedy_matches)
```

```
# Output:
Greedy matches: ['aaaa', 'a']
Non-greedy matches: ['a', 'a', 'a', 'a', 'a']
```

For greedy matching, we use the pattern **a+**, which matches one or more consecutive occurrences of the letter **a**. The **re.findall()** method finds all matches in the string **aaaabac**.

The greedy quantifier + matches the longest possible sequences of **a**, resulting in **['aaaa', 'a']**.

For non-greedy matching, the example uses the pattern a+?, which also matches one or more consecutive occurrences of the letter a, but in a non-greedy manner.

The **re.findall()** method finds all matches, but the non-greedy quantifier +? matches the shortest possible sequences of a that satisfy the pattern, resulting in **['a', 'a', 'a', 'a', 'a']**.

The key difference is that the greedy quantifier + matches the longest possible sequence of a characters in each match, whereas the non-greedy quantifier +? matches the shortest possible sequence of a characters in each match.

With greedy matching, the first match consumes all the consecutive **a** characters, leaving only one **a** for the second match.

With non-greedy matching, each **a** character is matched individually, resulting in separate matches for each occurrence.

### Character Sets and Ranges

Placing characters or character sets inside square brackets **([ ])** defines a character range. For example, **[a-z]** uses a hyphen, also known as the range operator, to include all lowercase letters from **a** through **z**.

In regular expressions, the hyphen **(-)** has a special meaning when it's used inside square brackets. When it's positioned between two characters, like **[a-z]**, it represents a character range and matches any character from **a** through **z**, inclusive. However, when the dash is placed at the beginning or the end of the square brackets, like **[-a]** or **[a-]**, it's treated as a literal hyphen character. So, in the pattern **[-a]**, it matches either a dash or the character a. This behavior ensures that if you want to include the dash as a possible match in a character class, you can place it at the beginning or end of the class without it being interpreted as part of a character range specifier.

### Character sets

To define a character set, place a group of characters inside square brackets.

For example, place the characters **[dog]** in square brackets to treat **d**, **o**, and **g** as a set. This set will match any one of these characters in the text. You can combine this set with other regular characters to create a versatile search pattern.

```
import re
sentence = "The dog is loyal"
set = re.findall("[hgo]", sentence)
print(set)
if set:
    print("Yes, there is at least one match!")
else:
    print("No match")
```

```
Result:

['h', 'o', 'g', 'o']  
Yes, there is at least one match!
```

The character set **[hgo]** successfully matched all instances of h, g, and o in the sentence.

Now, modify your character set to **[h-s]** to include a range of characters from h through s in the alphabet. When you run the code with this change, you will find that it matches all the letters in the sentence that fall within the range of **h** through **s**, inclusive.

```
Result:

['h', 'o', 'i', 's', 'l', 'o', 'l']  
Yes, there is at least one match!
```

This time, we want the character set to exclude all characters from the range **h** through **s**. To achieve this, add a caret symbol inside the square brackets: **[^h-s]**. Remember, the **^** serves dual purposes in regular expressions—it matches the beginning of a line or string when used outside square brackets, and it negates the character set when placed inside square brackets.

```
Result:

['T', 'e', ' ', 'd', 'g', ' ', ' ', 'y', 'a']  
Yes, there is at least one match!
```

As a result, **[^h-s]** matches and returns every character in the sentence that does not fall within the range from **h** through **s**, including white spaces—the spaces between characters.

#### Finding lowercase and uppercase letters in a sentence

```
import re
txt = "The 3 dogs are named Rex, Tiger, and Skip"
x = re.findall("[a-zA-Z]", txt)
print(x)
```

```
Result: 

['T', 'h', 'e', 'd', 'o', 'g', 's', 'a', 'r', 'e', 'n', 'a', 'm', 'e', 'd',
 'R', 'e', 'x', 'T', 'i', 'g', 'e', 'r', 'a', 'n', 'd', 'S', 'k', 'i', 'p']
```

#### Finding numbers in a string

```
import re
txt = "The 2 dogs were hungry at 4:15pm"
#Check if the string has any digits:
x = re.findall("[0-9]", txt)
print(x)
if x:
     print("Yes, there is at least one match!")
else:
     print("No match")
```

```
Result:

['2', '4', '1', '5']
Yes, there is at least one match!
```

#### Searching for two-digit numbers

```
import re
txt = "The 3 dogs are 8, 12, and 15 years old"
x = re.findall("[0-5][0-9]", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
```

```
Result:

['12', '15']  
Yes, there is at least one match!
```

#### Special characters in sets

When special characters are included within square brackets in sets, they lose their special properties and are treated as normal characters.

```
import re
txt = "The 3 dogs are named Rex, Tiger, and Skip."
x = re.findall("[+]", txt)
print(x)
if x:
     print("Yes, there is at least one match!")
else:
     print("No match")
```

```
Result:

[]  
No match
```

#### Which special character is the only one to return a match when is used in a set?

* Dot (.)

Wrong answers:

* Asterisk (*)
* Pipe (|)
* Dollar sign ($)
* Caret (^)

A **dot (.)** in a character set matches a literal period character, and there is a period at the end of the target string.

The other options are incorrect because:

* The **asterisk (*)** character is not in the target string.
* The **pipe (|)** character is not in the target string.
* The **dollar sign ($)** character is not in the target string.
* The ***caret (^)** is incorrect because, when placed at the start of a character set, it is interpreted as a negation operator, leading to an "unterminated character set" error.

#### Character set examples

##### [amk]

Matches any one of the characters a, m, or k individually anywhere in the string.

##### [a-z]

Matches any lowercase letter from a through z.

##### [a\-z]

Matches the letters a or z, and the dash (-) character as a literal. The dash needs to be escaped with a backslash (\) inside the character class to treat it as a literal character and not a range operator.

##### [a-]

Matches the letter a or a dash, as these are the only characters specified.

##### [-a]

Matches a dash or the letter a.

##### [a-zA-Z0-9]  

Matches any lowercase letter (a through z), any uppercase letter (A through Z), or any digit (0 through 9).

##### [(+*)]

Matches the characters (, +, *, and ) as literals because the brackets neutralize their special functions.

##### [^hg4]  

Matches any character except h, g, or 4, effectively negating these specified characters within the brackets.

### Using character ranges

A character set can encompass a range of characters. Instead of listing every individual letter like **[abcdefghijklmnopqrstuvwxyz]**, it's much more efficient to use a character range such as **[a-z]**. This uses the dash, which acts as a range operator. You can include multiple ranges in a single set, and they can be arranged in any order.

The RegEx pattern **[a-z0-9]** is used to find all lowercase letters and digits individually within a string.

```
import re
string = "The 2 dogs were hungry at 4:15pm"
result = re.findall("[a-z0-9]", string)
print(result)
```

Output:

```
Result: 

['h', 'e', '2', 'd', 'o', 'g', 's', 'w', 'e', 'r', 'e',
 'h', 'u', 'n', 'g', 'r', 'y', 'a', 't', '4', '1', '5', 'p', 'm']
```

#### Finding numbers and white spaces

```
import re
string = "The 2 dogs were hungry at 4:15pm"
result = re.findall("[\d\s]", string)
print(result)
```

Output:

```
Result: [' ', '2', ' ', ' ', ' ', ' ', ' ', '4', '1', '5']
```

#### Searching for phone number area codes in a string

```
import re
number = "777, 789, 788, 312, 404"
result = re.findall("[7-9][7-9][7-9]", number)
print(result)
```

Output:

```
Result: ['777', '789', '788']
```

### Groupings, Backreferences, and Alternation

When using regular expressions to search through text, it is common to segment the text into groups. For example, when filtering an email list, you might only want to extract specific parts of the emails, not the entire message. In these cases, groups in regular expressions prove invaluable. There are two types of RegEx groups—capturing and non-capturing.

* **Capturing groups**: You can use capturing groups to extract and refer back to parts of a match. 
* **Non-capturing groups**: Non-capturing groups are used to apply quantifiers to parts of your pattern, but they do not capture the text matched by those parts.

Groups facilitate the division of text into sections for more targeted searches, rather than matching the entire string. Parentheses **(( ))** are the only symbols used to denote groups.

Character classes use square brackets **([ ])** and quantifiers use curly brackets **({ })**.

### Capturing groups

Capturing groups in a pattern search helps you segment multiple characters into individual sections. For instance, if you were tasked with organizing a document containing phone numbers and email addresses, you could create two separate capturing groups to distinguish these categories. With capturing groups, you can also treat multiple characters as a single unit, enhancing the manageability of complex patterns.

#### Isolating similar phrases in a sentence

```
import re
ages = "Todd is 8 years old and Lisa is 6 years old, but Alex is 4 years old. "
groups = re.findall('[A-Za-z]+ \w+ \d+ \w+ \w+', ages)
print (groups)
```

```
Result: ['Todd is 8 years old', 'Lisa is 6 years old', 'Alex is 4 years old']
```

By enclosing the uppercase and lowercase letter range in parentheses ([A-Za-z]+), you can isolate only the names.

```
import re
ages = "Todd is 8 years old and Lisa is 6 years old, but Alex is 4 years old. "
groups = re.findall('([A-Za-z]+) \w+ \d+ \w+ \w+', ages)
print (groups)
```

```
Result: ['Todd', 'Lisa', 'Alex']
```

The result shows that only the names were returned. This is because the capturing group **([A-Za-z]+)** isolates and captures only the part of the pattern that matches the names, excluding the rest of the text matched by the pattern.

##### Listing only the ages

```
import re
ages = "Todd is 8 years old and Lisa is 6 years old, but Alex is 4 years old. "
groups = re.findall('[A-Za-z]+ \w+ (\d+) \w+ \w+', ages)
print (groups)
```

```
Result: ['8', '6', '4']
```

##### Grouping both the names and the ages

```
import re
ages = "Todd is 8 years old and Lisa is 6 years old, but Alex is 4 years old. "
groups = re.findall('([A-Za-z]+) \w+ (\d+) \w+ \w+', ages)
print (groups)
```

```
Result: [('Todd', '8'), ('Lisa', '6'), ('Alex', '4')]
```

The result is a list of tuples where each tuple contains a name and the corresponding age extracted from the string. By using capturing groups for both names and ages, the re.findall() function returns only the parts of the string in these groups.

```
import re
ages = "Todd is 8 years old and Lisa is 6 years old, but Alex is 4 years old. "
groups = re.findall('([A-Za-z]+) (\w+) (\d+) \w+ \w+', ages)
print (groups)
```

```
Result: [('Todd', 'is', '8'), ('Lisa', 'is', '6'), ('Alex', 'is', '4')]
```

The result is a list of tuples. Each tuple contains a name, a verb, and an age, reflecting the structured and targeted extraction of data based on the specified capturing groups. 

#### Using .group() and .groups()

The **.group()** method returns specific groups from the match, whereas .**groups()** returns a tuple of all the capture groups.

**re.compile()** function enhances efficiency when using the same pattern multiple times.

```
import re
pattern = re.compile(r'(\w+)\s+(\d+)')
match = pattern.match('Product 123')
print(match.group())
```

```
Result: Product 123
```

The regular expression **(\w+)\s+(\d+)** is designed to match a word followed by a space and a number. The **re.compile()** function creates a compiled RegEx object with the pattern. This approach is known as *compiled regular expressions*. The **.group()** method without any arguments returns the entire match, which is **Product 123**.

##### Using .group(2) to retrieve a specific part of the match

```
import re
pattern = re.compile(r'(\w+)\s+(\d+)')
match = pattern.match('Product 123')
print(match.group(2))
```

```
Result: 123
```

#### .groups() returns all the captured groups as a tuple

```
import re
pattern = re.compile(r'(\w+)\s+(\d+)')
match = pattern.match('Product 123')
print(match.groups())
```

```
Result: ('Product', '123')
```

#### Conclusion

Use **.group()** to return the exact substring of a capture group and **.groups()** to retrieve all captured groups as a tuple.

### Backreferences

Backreferencing in regular expressions is used to find duplicates by matching a previously captured group within the same expression. It refers back to the value stored in a group earlier in the pattern. The syntax for a backreference involves a backslash (\) followed by the group number, which indicates the order of the capturing group in the expression.

```
import re
print(re.search(r'(\w+) \1' , 'Hello Hello World'))
```

```
Result: <re.Match object; span=(0, 11), match='Hello Hello'>
```

In this pattern, **(\w+)** is a capturing group that matches one or more word characters. The **\1** is a backreference that matches the exact text previously matched by the first capturing group. This means it looks for a sequence where a word is followed by a space and then repeated exactly.

```
import re
print(re.search(r'(\w+) \1' , 'Hello, Hello World'))
```

```
Result: None
```

The expression failed to find the two identical words because the comma introduced between them disrupted the expected sequence of characters in the group.

```
import re
print(re.findall(r'(\w+) \1','Hello Hello World. Regular Expressions Expressions'))
```

```
Result: ['Hello', 'Expressions']
```

```
import re
print(re.findall(r'(\w+) \1','Hello Hello World World Regular Regular Expressions'))
```

```
Result: ['Hello', 'World', 'Regular']
```

The result shows the first word of each pair of duplicate words in the string. 

#### Including the group of words in the expression by adding .group(1) to retrieve the first group

```
import re
print(re.search(r'(\w+) \1','Hello Hello World World Regular Regular Expressions').group(1))
```

```
Result: Hello
```

**re.search() finds the first occurrence of a pattern in a string. It enables extracting specific captured groups from the match using the .group() method. re.findall() returns all matches as a list but doesn't support .group().**

```
import re
str1 = "Betty Smith and Sara Smith are sisters"
pattern = r'\b(\w+).*\1\b'
print(re.search(pattern, str1).group(1))
```

```
Result: Smith
```

#### Explanation

```
pattern = r'\b(\w+).*\1\b'
```

1. **\b** at the start and end of the pattern denotes a word boundary, ensuring that the pattern matches complete words only.
2. **(\w+)** is the first capturing group that matches one or more word characters. This group captures the first word it encounters, which is Betty.
3. The symbols .* follow the capturing group. The dot (.) matches any character except a newline. The asterisk (*) is a greedy quantifier. It matches as many characters as possible. The search extends to the rest of the string. It continues until a repetition of the captured group is found.
4. **\1** is a backreference to the first captured group. It looks for an exact duplicate of whatever was matched by **(\w+)** later in the string.
5. The final **\b** ensures that the duplicated word is also bounded by word limits, preventing partial matches.

The result indicates that **Smith** is the word that appears twice in the string as a whole word, separated by other characters. This pattern effectively finds repeated words in a sentence by using capturing groups, greedy quantifiers, and backreferences within word boundaries.

### Alternation

Alternation acts like the logical OR operator in Python. With alternation, you can specify multiple alternatives to match against within the same pattern. The syntax for alternation involves the pipe operator (|).

```
import re
sentence = 'coffee is better than tea'
pattern = 'coffee|tea'
alternation = re.findall(pattern,sentence)
print(alternation)
```

Output:

```
Result: ['coffee', 'tea']
```

The **re.findall()** function returns all matches for these terms in the order they appear.

```
import re
print(re.search("coffee|tea", "I love drinking coffee"))
print(re.search("coffee|tea", "I love drinking tea"))
```

Output:

```
Result:

<re.Match object; span=(16, 22), match='coffee'>
<re.Match object; span=(16, 19), match='tea'>
```

Each **re.search()** call returns the first occurrence of either coffee or tea in the string.

#### Searching for dog breeds using re.compile()

```
import re
pattern= re.compile("Retriever|Poodle|Beagle" )
print(pattern.search("My dog is a Retriever"))
print(pattern.search("My dog is a Poodle"))
print(pattern.search("My dog is a Beagle"))
print(pattern.search("My dog is a mixed breed"))
```

Output:

```
Result:

<re.Match object; span=(12, 21), match='Retriever'>
<re.Match object; span=(12, 18), match='Poodle'>
<re.Match object; span=(12, 18), match='Beagle'>
None
```

#### Example

```
import re
pattern= re.compile("^[a-zA-Z]{4}|\d{2}$")
print(pattern.search("abcd"))
print(pattern.search("12"))
print(pattern.search("ab"))
print(pattern.match("1234"))
```

Output:

```
Result:

<re.Match object; span=(0, 4), match='abcd'>
<re.Match object; span=(0, 2), match='12'>
None
None
```

The pattern uses two alternations. The first part **^[a-zA-Z]{4}** looks for exactly four alphabetical characters. The second part \d{2}$ looks for exactly two digits. The caret (^) ensures that, for the letters, the match must start at the beginning of the string. The dollar sign ($) ensures that, for the numbers, the match must end at the end of the string.

#### Switching from using pattern.match() to pattern.search()

```
import re
pattern= re.compile("^[a-zA-Z]{4}|\d{2}$")
print(pattern.match("abcd"))
print(pattern.match("12"))
print(pattern.match("ab"))
print(pattern.search("1234"))
```

Output:

```
Result:

<re.Match object; span=(0, 4), match='abcd'>
<re.Match object; span=(0, 2), match='12'>
None
<re.Match object; span=(2, 4), match='34'>
```

Even though **re.match()** would fail to find a match because it starts checking from the beginning of the string and **"1234"** doesn’t begin with two digits, **re.search()** scans through the entire string. When it reaches the last two characters, **34**, it successfully finds a match because **34** fits the **\d{2}$** condition, which matches two digits at the end of the string.

### Non-capturing groups

Sometimes, you might not need to capture a group within your RegEx pattern. In such cases, you can use a non-capturing group, which is defined by the syntax (?:). With this, you can use groups to organize or apply quantifiers without storing the matched result.

#### With capturing group

```
import re
ages = "Todd is 8 years old and Lisa is 6 years old, but Alex is 4 years old. "
groups = re.findall('([A-Za-z]+) \w+ \d+ \w+ \w+', ages)
print (groups)
```

```
Result: ['Todd', 'Lisa', 'Alex']
```

#### With non-capturing group

```
import re
ages = "Todd is 8 years old and Lisa is 6 years old, but Alex is 4 years old. "
groups = re.findall('(?:[A-Za-z]+) \w+ \d+ \w+ \w+', ages)
print (groups)
```
```
Result: ['Todd is 8 years old', 'Lisa is 6 years old', 'Alex is 4 years old']
```

The non-capturing group (?:[A-Za-z]+) matches one or more alphabetical characters, which are the names in the sentence. However, unlike capturing groups, the non-capturing group does not save the matched names for later use or output. Instead, it checks for their presence as part of the larger pattern that includes matching words for is, the age numbers, and the words years old. 

The result is the entire matched strings. This differs from what would have occurred with a capturing group, where only the specific captured parts (for example, the names) would be returned. This illustrates how non-capturing groups can be useful in complex patterns where you need to use a group for structure or to apply quantifiers, but you do not need to capture and return the group's contents.

### Knowledge Check

#### Which option contains two lazy quantifiers?

* *? , +?

Wrong answers:

* *, +
* ?, *
* +, ?

Both the asterisk (*) and the plus sign (+) can be made lazy, or non-greedy, by adding a question mark (?). The patterns *? and +? halt their search as soon as the pattern is matched, doing the minimum required to satisfy the match.

All other responses are combinations of greedy modifiers.

#### Which characters will match the expression [0-5]?

* All the digits from 0 through 5

Wrong answers:

* Digits from 6 and up
* Exactly five digits
* Odd numerals between 1 and 5

The regular expression range [0-5] matches any single digit from 0 through 5. To match two-digit numbers where each digit ranges from 0 through 5, you would use [0-5][0-5], which makes combinations like '00' to '55' possible.

The other responses are incorrect because the regular expression range calls for all digits from 0 through 5, so all digits outside that range would be incorrect, and it does not specify even or odd, or a specific number of digits.

#### What will the range [p-y] return in this code example?

```
import re
word = "python"
result = re.findall("[p-y]",word)
print (result)
```

* ['p', 'y', 't']

Wrong answers:

* 'py'
* 'python'
* ['py']

The range [p-y] matches any letter from p through y, so it would return 'p', 'y', and 't' from the word python. If the dash between p and y were removed, resulting in the regular expression [py], the match would be limited to a character class specifically returning only those two letters, ['p', 'y'].

#### Which element causes the result of the first print statement in this script to be None?

```
import re
print(re.search("Dog|Cat", "I love having a dog"))
print(re.search("dog|cat", "I love having a cat"))

Result:
None
<re.Match object; span=(16, 19), match='cat'>
```

* The word dog uses an uppercase D in the pattern but not in the string.

Wrong answers:

* The string only has the word dog and not cat.
* The word cat in the string must start with an uppercase C.
* The word cat uses an uppercase C in the pattern but not in the string.

Because the first alternation pattern requires uppercase letters and there are no uppercase letters in the string, the first function did not find a match. The pipe character (|) in the RegEx represents an either-or choice, where the alternation can match either of the specified patterns. Consequently, the lowercase c in cat matched the second pattern because it specified lowercase letters.

The other responses are incorrect because neither cat nor Cat is not found in the first statement.

#### What is the output of this code?

* ['Todd is 8 years old', 'Lisa is 6 years old', 'Alex is 4 years old']

Wrong answers:

* ['Todd', 'Lisa', 'Alex']
* "Todd is 8 years old and Lisa is 6 years old, but Alex is 4 years old."
* ['is 8 years old', 'is 6 years old', 'is 4 years old']

This code uses a non-capturing group (?:[A-Za-z]+). This part matches one or more alphabetic characters, either uppercase or lowercase. The '?:...' syntax is used for groups that should not be captured and returned in the results. Here, it matches the names Todd, Lisa, and Alex. Because the non-capturing group does not return its matches, the entire strings describing each person's age are returned as complete matches.

### Summary

* Greedy and non-greedy quantifiers
* Character sets and ranges
* Capturing and non-capturing groups, backreferences, and alternation

#### Quantifiers

Quantifiers in regular expressions are divided into two categories—greedy quantifiers and lazy (or non-greedy) quantifiers. With these quantifiers, you can control the amount of data matched by specifying how many times a given pattern should repeat.

* **Greedy quantifiers**: These include ?, *, +, and {m,n}. Greedy quantifiers attempt to match as much of the input as possible, capturing the maximum number of characters allowed by the pattern, which is often described as the longest possible match.
* **Lazy quantifiers**: Represented by ??, *?, +?, and {m,n}?, lazy quantifiers do the opposite of greedy ones. They strive to match the fewest characters possible, making what is known as the shortest possible match.

Greedy quantifiers are useful when you want to ensure that the largest possible part of a string that fits a particular pattern is matched, whereas lazy quantifiers are beneficial when you need to find the smallest piece of the string that satisfies the pattern, often used to prevent overreaching matches in complex strings.

#### Character sets and ranges

Using character sets and ranges, you can specify one or more alphanumeric characters to match within a string. By placing characters or predefined character sets inside square brackets ([ ]) and using a dash (-) to denote ranges, you can target specific characters or sequences of characters. This approach helps focus the search and exclude other characters in the string.

#### Capturing and non-capturing groups, backreferences, and alternation

* **Character classes**: Defined by square brackets ([ ]), character classes match any one of the characters specified within the brackets. For example, [a-z] matches any lowercase letter from a through z.
* **Capturing groups**: Defined by parentheses (( )), capturing groups match and capture sequences of characters for further processing. For instance, (abc) captures the sequence abc.

When using regular expressions to search through text, you often need to match specific information for later use. With capturing groups, you can segment the text into sections, rather than capturing the entire string. When capturing is unnecessary, you can use a non-capturing group, denoted as ?:..., which groups the pattern without saving the match.

#### Backreferencing and alternation

* **Backreferencing**: With this feature, you can find duplicates by matching a group’s previous match within the same expression. For example, (\w+) \1 matches two consecutive, identical words.
* **Alternation**: Denoted by the pipe symbol (|), alternation can perform a search for one of several options. For example, cat|dog matches either cat or dog.

## RegEx Functions in Depth

### Overview of RegEx functions

| Type | Function | Description |
| --------- | ---------- | ------------------------------------------------ |
| Searching | re.match() | Matches a pattern at the beginning of the string |
| Searching | re.fullmatch() | Matches a pattern against the entire string |
| Searching | re.search() | Searches for matches anywhere in the string |
| Searching | re.findall() | Returns a list of all matches of a pattern in the string |
| Searching | re.finditer() | Scans the string from left to right and returns an iterator that yields match objects for each match found |
| Modifying | re.sub() | Substitutes occurrences of a pattern with specified replacement text |
| Modifying | re.split() | Splits the string at occurrences of the pattern and returns a list of the resulting substrings |

### re.match() and re.fullmatch()

* re.match() searches for a match only at the beginning of the string
* re.fullmatch() requires the entire string to match the pattern

#### re.match()

```
import re
sentence = "The dog is loyal."
result = re.match("T", sentence)
print(result)
```

```
Result: <re.Match object; span=(0, 1), match='T'>
```

#### re.fullmatch()

```
import re
sentence = "The dog is loyal."
result = re.fullmatch("The dog is loyal.", sentence,)
print(result)
```

```
Result: <re.Match object; span=(0, 17), match='The dog is loyal.'>
```

The **re.fullmatch()** function returned the entire string because it requires the entire string to exactly match the specified pattern.

#### re.match() with unmatched pattern

```
import re
sentence = "The dog is loyal."
result = re.match("d", sentence)
print(result)
```

```
Result: None
```

### re.search()

The re.search() function searches throughout the entire string for a match. 

```
import re
sentence = "The dog is loyal."
result = re.search("s", sentence)
print(result)
```

```
Result: <re.Match object; span=(9, 10), match='s'>
```

### re.search() with multiple matches - it picks up only the 1st

```
import re
sentence = "The dog is loyal and sweet."
result = re.search("s", sentence)
print(result)
```

```
Result: <re.Match object; span=(9, 10), match='s'>
```

Even though the word **sweet** later in the sentence also contains an s, re.search() returns a match object for the first s it encounters. Here, that is in the word **is**.

### re.search() with special characters

```
import re
match=re.search('d.+','The dog is loyal.')
print(match)
```

```
Result: <re.Match object; span=(4, 17), search='dog is loyal.'>
```

The re.search() function is used with the pattern d.+, where d specifies that the match must start with the letter d, and the combination of the period (.) followed by the plus sign (+) means it will match any character (.) repeated one or more times (+). As a result, the search starts at the d in dog and continues to match every subsequent character until the end of the string. This returns 'dog is loyal.' as the match.

```
import re
match=re.search('g.+','The dog is loyal.')
print(match)
```

```
Result: <re.Match object; span=(6, 17), match='g is loyal.'>
```

Here, the search begins at the g in dog and continues until the end of the string. Therefore, the function returns 'g is loyal.' as the match, capturing everything from g onwards.

### re.findall() and re.finditer()

The function **re.findall()** has a companion function, **re.finditer()**. Although both functions search for all matches of a pattern in the string, **re.finditer()** differs in that it returns an iterator rather than a list.

**re.finditer()** consumes less memory because it doesn't store all matches at once. Instead, it generates matches as needed during iteration.

#### re.findall() Example

```
import re
sentence = "The dog is loyal and lovely."
result = re.findall("lo", sentence)
print(result)
```

Output

```
Result: ['lo', 'lo']
```

The pattern **lo** matches any occurrence of these two consecutive characters in the string. In this particular sentence, lo appears twice—once in **loyal** and once in **lovely**. The result is a list of all matches found.

#### re.finditer() Example

```
import re
sentence = "The dog is loyal and lovely."
result = re.finditer("lo", sentence)
print(result)
```

Output:

```
Result: <callable_iterator object at 0x10ccaf670>
```

#### Printing human readable result

```
import re
sentence = "The dog is loyal and lovely."
result = re.finditer("lo", sentence)

for match in result:
    print(match.group(), match.start(), match.end())
```

Output:

```
Result: 

lo 11 13
lo 21 23
```

Each match object contains methods that provide additional information about the match.

* **match.group()** returns the actual text that was matched, which in this example will always be **lo**.
* **match.start()** provides the starting index of the match in the string.
* **match.end()** provides the ending index of the match in the string.

As the loop iterates over the iterator returned by **re.finditer()**, it prints the matched substring along with its starting and ending positions in the original string. This shows that **lo** was found twice—first in the word **loyal** starting at index **11** and ending at index **13**, and second in the word lovely starting at index **21** and ending at index **23**.

**Remember, the ending index does not include the last character of the match.**

The **finditer()** function is useful if you are processing large text files or need detailed information about each match. This is because it yields match objects that provide details without loading all matches into memory at once.

### re.sub()

The **re.sub()** function performs substitutions within a string, replacing specified patterns with a new substring. In this example, we use **\s** to match any white space in the string, and then replace it with the number **4**.

```
import re
sentence = "The dog is loyal and lovely."
result = re.sub("\s","4", sentence)
print(result)
```

```
Result: The4dog4is4loyal4and4lovely.
```

#### re.sub() Example

```
import re
sentence = "The dog is loyal and lovely."
result = re.sub('dog','cat', sentence)
print(result)
```

```
Result: The cat is loyal and lovely.
```

### re.split()

The **re.split()** function divides a string into a list by splitting it at each match of the specified pattern. In this example, we use **\s** to denote white space. As a result, the string is split at each space, separating the words.

```
import re
sentence = "The dog is loyal and lovely."
result = re.split("\s", sentence)
print(result)
```

```
Result: ['The', 'dog', 'is', 'loyal', 'and', 'lovely.']
```

#### re.split() Example

```
import re
sentence = "The dog is loyal. The cat is friendly."
result = re.split("\.", sentence)
print(result)
```

```
Result: ['The dog is loyal', ' The cat is friendly', '']
```

When the function encounters period characters in the sentence, it splits the string at those points. As a result, the output is a list of the segments of the string that were separated by the periods. Notice that the output includes an empty string ('') as the last element of the list. This happens because there is a period at the end of the sentence with no characters following it.

If you want to keep the periods in the result, enclose the regular expression inside parentheses, like this: '(\.)'.

#### Use parentheses to keep .'s in the result

In the provided code, re.split("(\.)", sentence) splits the sentence string at every period (.), while also including the periods in the resulting list. This is because the parentheses create a capturing group that captures the periods as part of the splitting process.

```
import re
sentence = "The dog is loyal. The cat is friendly."
result = re.split('(\.)', sentence)
print(result)
```

```
Result: ['The dog is loyal', '.', ' The cat is friendly', '.', '']
```

### Flags

There are *modifiers*, also known as *flags*, when patterns require additional functionality to enhance their matching capabilities.

#### re.M | re.MULTILINE

Makes the caret (^) and dollar sign ($) able to match the start and end of each line, not only the start and end of the string.

```
import re 
text = "Line 1\nLine 2\nLine 3"
pattern = r'^Line'
matches = re.findall(pattern, text, flags=re.MULTILINE)
print(matches)

# Output: ['Line', 'Line', 'Line'] |
```

#### re.I | re.IGNORECASE

Makes case-insensitive matching possible, so characters can match regardless of case.

```
import re
text = "Hello World"
pattern = r'hello'
matches = re.findall(pattern, text, flags=re.IGNORECASE)
print(matches)

# Output: ['Hello']
```

#### re.S | re.DOTALL

Makes the dot (.) match every character, including newline characters, which it does not normally match.

```
import re
text = "Line 1\nLine 2\nLine 3"
pattern = r'Line.*3'
match = re.search(pattern, text, flags=re.DOTALL)
print(match.group(0))

# Output: Line 1\nLine 2\nLine 3
```

#### re.X | re.VERBOSE

```
import re
name = "Shirley\nterry\nJorge\n"
match = re.search('''shirley. #This word can be matched when using re.IGNORECASE
terry. #This word can be matched because of the re.DOTALL AND re.IGNORECASE
 jorge''', name, re.DOTALL | re.IGNORECASE | re.VERBOSE)
if match:
    print(match[0])
else:
    print('No match')
```

Output:

```
Shirley
terry
Jorge
```

### Best practices in regular expressions

Mathematician Stephen Kleene first formalized regular expressions in 1951 and coined the term by 1956.

In the 1960s, Ken Thompson further integrated regular expressions into the Unix “e-d” text editor, establishing their early use in computing by 1968.

1. Keep your RegEx patterns as simple as possible.
2. Use character classesand special sequamces frequently.
3. Continuously test your regular expressions.
4. Leave comments in your RegEx code. Comments can be added to your RegEx pattern by using the re.VERBOSE flag, which allows for clearer and more maintainable code.
5. Use Python's designated raw string notation by prefixing your RegEx patterns with the r character.
6. Use flags to enhance your RegEx's functionality. The re.IGNORECASE flag allows for case-insensitive matching, and re.VERBOSE enhances readability by allowing white space and comments in your pattern. The re.MULTILINE flag adjusts the caret and dollar sign anchors to match the start and end of each line, not just the whole string.

## Practical Applications of Regular Expressions

### RegEx use cases

* Extracting or redacting specific parts of emails
* Searching for specific information in customer accounts
* Modifying content in a database
* Web scraping to extract data such as product details or prices
* Validating user-submitted inputs in web applications, such as password character requirements and email format

### Extract and parse data from text

Extract all timestamps for events logged between certain hours to analyze server activity during peak times.

Let's assume the timestamps are in the format **YYYY-MM-DD HH:MM:SS**. We want to extract timestamps between **10:00:00** and **17:00:00**.

```
import re

# Example log data
log_data = """
2023-04-01 09:15:00 Event A
2023-04-01 10:30:00 Event B
2023-04-01 16:45:00 Event C
2023-04-01 18:00:00 Event D
"""

# Regular expression to match timestamps between 10:00:00 and 17:00:00
pattern = r'\d{4}-\d{2}-\d{2} (1[0-6]:\d{2}:\d{2}|17:00:00)'

# Find all matching timestamps
matches = re.findall(pattern, log_data)

# Print the matches
for match in matches:
    print("Match found:", match)
```

Output:

```
Result:

Match found: 10:30:00
Match found: 16:45:00
```

The script finds timestamps between 10:00:00 to 17:00:00 in log data using **re.findall()**.

The RegEx pattern specifically matches any full hour from 10 through 16, and exactly at 17:00:00.

### Using RegEx to parse a URL to extract components

Using RegEx, parse a URL to extract components like domain names, port numbers, or paths.

```
import re 
 # web address
string = 'http://www.example.com/index.html' 
address = re.findall('(\w+)://([\w\-\.]+)/(.*)', string)
print(address)
```

Output:

```
Result: [('http', 'www.example.com', 'index.html')]
```

The pattern (\w+)://([\w\-\.]+)/(.*) is structured as follows:

* (\w+) matches the protocol part of the URL (for example, http), capturing one or more word characters until it encounters a colon (:).
* :// matches the literal characters ://, which are standard in URLs after the protocol.
* ([\w\-\.]+) matches and captures the domain part of the URL (for example, **www.example.com**). This part includes one or more word characters, hyphens, or dots.
* /(.*) matches a forward slash followed by any sequence of characters (.*), capturing this as the path of the URL (for example, **index.html**).

The result is a list of tuples, with each tuple containing the protocol, domain, and path as captured by the RegEx groups.

### Modifying the contents of files

```
import os
import re

# Path to the directory with files
directory = 'path/to/files'

# RegEx pattern to find '2023'
pattern = r'2023'

# Loop over each file in the directory
for filename in os.listdir(directory):
    # Assuming we only want to edit .txt files
    if filename.endswith('.txt'):
        file_path = os.path.join(directory, filename)
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Replace '2023' with '2024' using re.sub()
        updated_content = re.sub(pattern, '2024', content)

        # Write the changes back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(updated_content)

print("Content update completed.")
```

### Validating user input

```
import re

# Function to validate phone number
def validate_phone_number(phone_number):
    # RegEx pattern for validating a phone number 
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    
    # Match the pattern to the input
    if re.fullmatch(pattern, phone_number):
        return "Phone number is valid."
    else:
        return "Invalid phone number format."

# Example phone numbers to test
phone_numbers = ["555-456-7890", "555-456-789", "5554567890", "abc-def-ghij"]

# Validate each phone number
for number in phone_numbers:
    result = validate_phone_number(number)
    print(result)
```

Output:

```
Output

Result:

Phone number is valid.
Invalid phone number format.
Invalid phone number format.
Invalid phone number format.
```

### Validating user input with RegEx

#### Validating email imput

```
import re
regex=re.compile(r'\S+@\S+\.\S+')
def isValid(email):
    return regex.fullmatch(email) is not None
while True:
    email=input("Please enter a valid email address: ")
    if isValid(email):
        print("Your email is valid, thank you! ")
        break
    else:
        print("Please enter a valid email")
```

### Analyzing social media posts

#### Extracting hashtags, mentions, and URLs from a series of sample social media posts

```
import re

# Sample social media posts
posts = [
    "Check out our new product! #innovation #2023 https://example.com/new-product",
    "Thanks for the support @user1! Visit us at http://example.com",
    "What an amazing experience at #TechConference @company #exciting"
]

# RegEx patterns for hashtags, mentions, and URLs
hashtag_pattern = r'#(\w+)'
mention_pattern = r'@(\w+)'
url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

# Function to extract information
def extract_info(posts):
    hashtags = []
    mentions = []
    urls = []
    for post in posts:
        hashtags.extend(re.findall(hashtag_pattern, post))
        mentions.extend(re.findall(mention_pattern, post))
        urls.extend(re.findall(url_pattern, post))
    return hashtags, mentions, urls

# Extract information from posts
extracted_hashtags, extracted_mentions, extracted_urls = extract_info(posts)

# Display extracted information
print("Hashtags:", extracted_hashtags)
print("Mentions:", extracted_mentions)
print("URLs:", extracted_urls)
```

Output:

```
Result:

Hashtags: ['innovation', '2023', 'TechConference', 'exciting']
Mentions: ['user1', 'company']
URLs: ['https://example.com/new-product', 'http://example.com']
```

### Applying regular expressions in AWS services

1. **Amazon CloudWatch Logs**. Regular expressions can be used to filter and search through log data. For instance, you can write RegEx patterns to extract error codes or specific log messages that match certain criteria, helping in debugging and monitoring applications.
2. **AWS WAF**. Regular expressions can be employed to create custom rules that filter web traffic. These rules can identify and block potentially harmful SQL injection attacks or cross-site scripting (XSS) by matching patterns known to represent malicious content.
3. **Amazon Simple Storage Service (Amazon S3)**. Amazon S3 itself does not process regular expressions. However, the tools interfacing with Amazon S3, like Amazon S3 Select, can use RegEx to filter object content directly on Amazon S3. This facilitates efficient data retrieval without needing to download entire files.
4. **Amazon Athena**. Athena supports RegEx within its SQL queries. Users can perform complex data searches directly in Amazon S3 data, such as filtering log files or complex data patterns, making data querying more flexible and powerful.
5. **AWS Lambda**. In Lambda, RegEx can be used in the function code to process incoming event data. For example, you might use RegEx to parse and validate incoming JSON from Amazon API Gateway, or route events based on content matching specific patterns.
6. **Amazon Kinesis**. Regular expressions can be used in processing streaming data for real-time analytics with Amazon Kinesis. This might involve filtering or transforming incoming data streams based on patterns that indicate important events or anomalies.
7. **AWS Glue**. AWS Glue can use regular expressions during extract, transform, and load (ETF) jobs to cleanse or transform data. RegEx can be used to parse and standardize formats, such as dates and phone numbers, ensuring consistency across data sets.
8. **Amazon OpenSearch Service**. OpenSearch Service uses regular expressions for complex searches that might involve pattern-based queries within documents, useful in scenarios like full-text search or log analysis.

### Knowledge Check

#### What will be the output of the following Python code using the re.split() function?

```
import re
text = "Python,Java;C++|Ruby"
result = re.split('[,;|]', text)
print(result)
```

* ['Python', 'Java', 'C++', 'Ruby']

Wrong answers:

* ['Python', 'Java;C++|Ruby']
* ['Python', 'Java;C++', 'Ruby']
* ['Python, Java;C++| Ruby']

The **re.split()** function is used to split the string text using a regular expression pattern that includes multiple delimiters. The pattern **[ , ; | ]** specifies a character class that matches any one of these delimiters. As a result, the string is split at each occurrence of these characters, effectively dividing it into the words **'Python'**, **'Java'**, **'C++'**, and **'Ruby'**.

The other responses are not split correctly using the split method because they do not split the original string by all the members of the character class.

#### Which of these flags permit comments inside the RegEx?

* re.VERBOSE

Wrong answers:

* re.MULTILINE
* re.IGNORECASE
* re.ASCII

The **re.X** flag, also known as **re.VERBOSE**, supports white space and comments within regular expressions, enhancing their readability.

The other responses do not permit comments inside the RegEx.

#### What will be the output of the following Python code using the re.sub() function?

```
import re
text = "100 cats, 23 dogs, and 40 birds."
result = re.sub(r'\d+', 'many', text)
print(result)
```

* Many cats, many dogs, and many birds

Wrong answers:

* 100 cats, 23 dogs, and 40 birds
* 100 many cats, 23 many dogs, and 40 many birds
* 100, 23, 40

The **re.sub()** function is used to substitute all occurrences of a pattern in a string with a specified replacement. Here, the pattern **\d+** matches one or more digits, which represent the quantities of animals in the text. The function replaces every sequence of digits with the word **many**. This leads to a transformation of the original string into **"many cats, many dogs, and many birds"**.

#### What will be the output of the following Python code using the re.match() function?

```
import re
text = "he was smiling"
sub = re.match('(.*) (.*?) (.*)', text)
print(sub.groups())
```

* (‘he’, ‘was’, ‘smiling’)

Wrong answers:

* (‘he’, ‘smiling’)
* (‘he was smiling’)
* ('he, was, smiling')

Each word is captured by one of the groups in the pattern:

* The first (.*) is greedy but stops at the first space because of the next group. It captures the first word he.
* The middle (.*?) is lazy, capturing just enough to allow the next part of the pattern to match. It captures the next word was.
* The final (.*) captures the remainder of the string after the last space, in this case, smiling.

**re.match()** is used to find a match at the beginning of the string. It matches the pattern against the string from the start, which is why it captures the full string if the pattern allows.

**sub.groups()** is called to return a tuple containing all the groups captured by the RegEx. This is because **re.match()** does not automatically return the captured groups. The purpose of **sub.groups()** is specifically to retrieve and display these groups.

### Summary

#### RegEx functions and flags

* **re.findall()** returns a list of all matches of a pattern within the string.
* **re.finditer()** scans the string from left to right, returning an iterator that yields match objects for each match found.
* **re.fullmatch()** matches a pattern against the entire string.
* **re.match()** matches a pattern at the beginning of the string.
* **re.search()** searches for matches anywhere in the string.
* **re.split()** splits the string at occurrences of the pattern and returns a list of the resulting substrings.
* **re.sub()** substitutes occurrences of a pattern with specified replacement text.

#### RegEx flags or modifiers

They adjust a search pattern for more precise matching.

* re.M - re.MULTILINE
* re.I - re.IGNORECASE
* re.S - re.DOTALL
* re.X - re.VERBOSE
* re.L - re.LOCALE
* re.A - re.ASCII

#### Best practices and practical applications

* **Start with the basics.** Begin with straightforward patterns and gradually incorporate complexity as needed.
* **Use character classes.** Use character classes frequently to streamline your patterns.
* **Use iterative testing.** Continuously test your regular expressions to ensure they perform as expected.
* **Comment on your code.** Add comments to clarify what your patterns are designed to match. This practice helps make your code more understandable to others and to yourself when revisiting it later.

#### Practical applications of regular expressions

The applications include parsing and extracting data from text, modifying file contents, validating user input, and analyzing social media posts.

### [Lab: Using Regular Expressions in Real Life](./W10Lab1RegularExpressions.md)
