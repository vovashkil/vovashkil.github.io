# Using Regular Expressions in Real Life

## Lab overview

This lab reinforces your regular expression (regex) knowledge by using real-world examples that simulate practical scenarios that a developer might encounter. For these tasks, you act as a developer who extracts useful information from server logs, such as the most visited websites and the time it takes to send email. You also anonymize a sensitive data file that contains personnel names and email addresses.

Objectives
By the end of this lab, you should be able to do the following:

Parse a web server access log and generate statistics about its items.
Parse an email server log to check how quickly an application sends .
Anonymize a file by replacing names and email addresses with anonymous data.
Technical knowledge prerequisites
This hands-on lab assumes that you have completed the Developer Fundamentals 1 (DF1) course and the associated labs.

Duration
This lab requires approximately 2 hours to complete.

Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Command: A command that you must run
 Expected output: A sample output that you can use to verify the output of a command or edited file
 Note: Additional information or elaboration on a point
 Hint: A hint to a question or challenge
 Task complete: A conclusion or summary point in the lab
Start lab
To launch the lab, at the top of the page, choose Start lab.

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

Task 1: Establish the development environment
In this task, you connect to the AWS Cloud9 IDE.

To open the AWS Cloud9 environment, copy the Cloud9Environment URL value that is listed to the left of these instructions, and paste it into a new browser tab.

 Expected output: A new browser tab opens and displays the AWS Cloud9 IDE.

 Task complete: You have successfully connected to the AWS Cloud 9 IDE.

Task 2: Measure web server log statistics
In this task, you gather and print out statistics from a web server log, such as the most visited pages. To accomplish this, you write regex within the argument of re.compile() to match the server log entries and store them in regex groups within a regex object. The regex object is then used by additional Python functions to gather and display the web server log statistics.

Task 2.1: Analyze the web server log
In the sample-data folder, open the access.log file. It is a web server traffic log.
Inspect the structure of a web server log entry. The following is an example entry:


192.0.2.18 - - [01/Jan/2023:00:01:00 +0100] "GET /about HTTP/1.1" 404 154122 "https://example.org"
The log entry can be divided into the following sections:

Item	Section from log entry
client IP	192.0.2.18
dashes separator	- -
timestamp	[01/Jan/2023:00:01:00 +0100]
request	“GET /about HTTP/1.1”
status code	404
bytes sent	154122
referrer	“https://example.org”
Task 2.2: Write regex to parse the web server log
In this task, you write regex groups that match the sections of a log entry.

Open the access_log.py file.
Take a moment to familiarize yourself with code in the file. Be sure to read the comments within the functions to understand what they do. The following is a summary of the code within the file:

First, you use re.compile() to generate a regex object.

Next, the parse_logfile() function uses this regex object to parse the log file, and stores the results inside a list of tuples. Each tuple contains the strings that were matched by the regex groups.

The ip_stats() function takes the list of tuples that was returned from parse_logfile(), and generates a dictionary containing the statistics for the most visited pages. Then it iterates through the dictionary to print out the keys and values.

The page_stats() and error_stats() functions follow a format and behavior similar to the ip_stats() function.

Find the line starting with regex = re.compile.

 Note: You can also press Ctrl+F on Windows or Cmd+F on Mac to search for regex = re.compile.


regex = re.compile(r'([\d.]+) - - ')
In the argument of re.compile(), add regex groups to capture all the sections of a log entry.
 Note: The correct regex can be challenging to find, so reference the regex in the following table if you need help completing the solution.

To see a table of matching regex groups, expand this section.
To see the solution code if needed, expand this section.
From the File menu, choose Save.

 Command: Run the following command in the bash terminal:


python access_log.py
 Expected output:


Most frequent client IP addresses:
203.0.113.228: 881
198.51.100.190: 852
192.0.2.30: 829
203.0.113.0: 824
192.0.2.40: 810

Most visited pages:
/cart: 591
/user/login: 565
/contact: 561
/products: 560
/about: 556

Error count:
4xx: 1661
5xx: 1627
 Task complete: You have successfully used regex to parse your web server log and gather its statistics.

Task 3: Measure email delivery speed
In this task, you check the time that it takes for an email application to send email. To accomplish this, you write regex within the argument of re.compile() to match the server log entries and store them in regex groups within a regex object. Next, additional Python functions will use the regex object to calculate the time that it takes to send the email.

Task 3.1: Analyze the email log
In the sample-data folder, open the mail.log file.
Find a line where an email enters the server. It will have a message-id attribute.

 Command: Press Ctrl+F on Windows or Cmd+F on Mac and search for message-id.
An example search result would be the following log entry:


Jan 14 03:45:14 mail postfix/cleanup[15994]: F1FDBB0221: message-id=<pat_candella@example.net>
Next, find a line where an email leaves the server for its destination. It will have a status attribute.

 Command: Press Ctrl+F on Windows or Cmd+F on Mac and search for status.
An example search result would be the following log entry:


Jan 14 03:45:15 mail postfix/pipe[15995]: F1FDBB0221: to=<john_stiles@example.net>, orig_to=<john_stiles@example.net>, relay=example.net, delay=0.05, delays=0.01/0.01/0/0.02, dsn=2.0.0, status=sent (delivered by example.net service)
Using the previous log entry as an example, any log entry for an email entering or leaving the server can be divided into the following sections.

Item	Example section from a log entry
month	Jan
day	14
time	03:45:15
server process	postfix/cleanup[15994] ( Note: postfix is the name of the email server software.)
queue ID	F1FDBB0221
message	to=john_stiles@example.net, orig_to=john_stiles@example.net, relay=example.net, delay=0.05, delays=0.01/0.01/0/0.02, dsn=2.0.0, status=sent (delivered by example.net service)
Task 3.2: Write regex to parse the email log
In this task, you write regex groups that match the sections of a log entry for email entering or leaving the server.

Open the mail_log.py file.
Take a moment to familiarize yourself with the code in the file. Be sure to read the comments within the functions to understand what they do. re.compile() and parse_logfile() are used here again for the same purpose as in the previous exercise. get_line_timestamp() is a helper function that is used by postfix_stats() to calculate the time duration for an email entering and leaving the server.

Find the regular expression on the line starting with regex = re.compile, as shown in the following code snippet.
 Note: You can also press Ctrl+F on Windows or Cmd+F on Mac to search for the line.


regex = re.compile(r'(\w{3}) (\d{1,2})')
To help you get started, the regex groups to capture the month and day have already been filled out.

In the argument of re.compile(), add regex groups to capture all the sections of a log entry.
 Note: The correct regex can be challenging to find, so reference the regex in the following table if you need help completing the solution.

To see the a table of matching regex groups, expand this section.
To see the solution code if needed, expand this section.
From the File menu, choose Save.

 Command: Run the following command in the bash terminal:


python mail_log.py
 Expected output:


Email queue stats:
[F1FDBB0221] sent in 1 seconds
[902B4AF92F] sent in 0 seconds
[B6C0BAF930] sent in 0 seconds
[F143FAF931] sent in 1 seconds
[DCBCCAF932] sent in 1 seconds
[AF822AF934] sent in 0 seconds
[11599B0308] sent in 0 seconds
[A3573B0133] sent in 0 seconds
[C7B8CB0244] sent in 0 seconds
[5F11BB0245] sent in 0 seconds
[160C1AFDF7] sent in 0 seconds
[6CEF3AFF25] sent in 0 seconds
[252CEAFF26] sent in 0 seconds
[B5BBAB0134] sent in 1 seconds
[11DD8B018A] sent in 0 seconds
These results represent the time that it takes for the application to send email (0 seconds means that the email was sent in under 1 second).

 Task complete: You have successfully used regex to parse your email application log to measure the duration to send email.

Task 4: Anonymize a Data File
In this task, you anonymize a data file that contains the names and email addresses of personnel. The names and email addresses have to be replaced with randomly generated, anonymized versions.

In the sample-data folder, open the people.dat file.
Inspect the content structure. The following is a snippet from the file:


"name": "Alejandro Rosalez"
"email": "Alejandro_Rosalez@example.com"
"job": "Engineer, production"
---
"name": "Akua Mansa"
"email": "Akua_Mansa@example.com"
"job": "Engineering geologist"
---
"name": "Arnav Desai"
"email": "Arnav_Desai@example.com"
"job": "Publishing rights manager"
Open the anonymize.py file.

Find the line starting with regex_name =, as shown in the following code snippet.


regex_name = r'"name": "(<INSERT_NAME_REGEX>)"'
Add regex to complete the regex pattern for finding a name. Your regex should replace <INSERT_NAME_REGEX>.
 Hint: The regex should capture Alejandro Rosalez from “name”: “Alejandro Rosalez”.

To see the solution code if needed, expand this section.
Find the line starting with regex_email =, as shown in the following code snippet:

regex_email = r'"email": "(<INSERT_EMAIL_REGEX>)"'
Add regex to complete the regex pattern for finding an email. Your regex should replace <INSERT_EMAIL_REGEX>.
To see the solution code if needed, expand this section.
From the File menu, choose Save.

 Command: Run the following command in the bash terminal:


python anonymize.py
 Expected output: A new file called people-anonymized.dat is generated.

Open the newly created people-anonymized.dat file.

Check to see if the file contains new names and email addresses.

 Command: You can check the differences in both versions in the terminal by running the following command:


diff -uw  sample-data/people.dat people-anonymized.dat
 Expected output:


-"name": "Alejandro Rosalez"
-"email": "Alejandro_Rosalez@example.com"
+"name": "REDACTED"
+"email": "REDACTED@example.com"
 "job": "Engineer, production"
 ---
-"name": "Akua Mansa"
-"email": "Akua_Mansa@example.com"
+"name": "REDACTED"
+"email": "REDACTED@example.com"
 "job": "Engineering geologist"
 ---
-"name": "Arnav Desai"
-"email": "Arnav_Desai@example.com"
+"name": "REDACTED"
+"email": "REDACTED@example.com"
 "job": "Publishing rights manager"

 ---
 Note: This is only the beginning portion of the expected output, showing the first three people. The minus signs ( - ) indicate what has been deleted, and the plus signs ( + ) indicate what has been added.

All names should have been replaced with “REDACTED,” and all email addresses should have been replaced with “REDACTED@example.com”.

 Task complete: You have successfully anonymized the file.

Conclusion
 Congratulations! You now have successfully done the following:

Parsed a web server access log and generated statistics about its items.
Parsed an email server log to check how quickly an application sends email.
Anonymized a file by replacing names and email addresses with anonymous data.
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End lab and then confirm that you want to end your lab.

For more information about AWS Training and Certification, see https://aws.amazon.com/training/.

Your feedback is welcome and appreciated.
If you would like to share any feedback, suggestions, or corrections, please provide the details in our AWS Training and Certification Contact Form.
