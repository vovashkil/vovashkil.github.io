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

