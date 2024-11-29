# Scripting Part 1

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to repo's main [README.md](../../../README.md)

## Scripting

### Pre-assessment

#### Which task is a use case for scripting?

* Automating file backups

Wrong answers:

* Writing drivers for hardware components
* Developing high-performance video games
* Creating operating system kernels

Scripting is commonly used for automating tasks like file backups, system administration, and routine processes.

Using a device driver typically involves low-level programming, not scripting. Developing a high-performance video game or an operating system kernel are usually done with compiled languages.

#### Which scenario commonly uses Ruby?

* Web development

Wrong answers:

* Embedded systems programming
* Operating systems
* Scientific computing

Ruby is commonly used for web development tasks, thanks to frameworks like Ruby on Rails.

The remaining answers do not represent common use cases for Ruby.

#### What is a potential disadvantage of synchronous processing in the context of automating operational tasks?

* Scripts running longer

Wrong answers:

* Complex error-handling mechanisms
* Synchronous scripts are unable to port between platforms
* More complicated code

Synchronous processing in automating operational tasks can result in scripts running longer.

### Introduction to Scripting

Through the use of scripting languages, you can deploy resources, modify security settings, create user accounts, and more, all in an orderly fashion. Scripting brings a number of benefits to your organization, including 

* efficiency,
* standardization,
* and governance.

**Efficiency** is achieved through the automation of tasks like deploying large numbers of resources.

**Standardization** can be achieved through the use of infrastructure as code. By using a standardized deployment script, you can ensure that you’re getting the same resource with the same configuration every time.

Finally, scripting can help you with **governance**. The standardization and templatization that is capable through the use of infrastructure as code can help to ensure that your organization operates within the guidelines and regulations set by applicable governing bodies.

The term **scripting** is often used interchangeably with similar terms, like **programming and coding**. **Scripting** is, in essence, a **type of programming**. Both provide instructions to a computer, and both can use a variety of languages to achieve their intended outcome.

Programming is used to create a program. Generally, code is **compiled** prior to being run, and the compiled code runs in the same static way each time, unless it is recompiled. Put simply, compiling is the process of converting the language into machine code.

Scripting uses languages that **interpret** code to automate tasks and processes. Interpreting code means that instructions are active immediately, even if the code isn’t compiled yet. Languages like Java compile code, while Python interprets it.

### Advantages of using scripting

Scripting is a powerful tool for automating tasks, enhancing efficiency, and streamlining workflows.

* Productivity and efficiency
* Consistency and portability
* Ease of debugging
* Security and access control
* Integration

### Scripting use cases

* **Automating file backups**. You can use scripting to automate the process of copying files and directories to designated backup locations. With scripting, you can schedule backups at specific intervals, or run them after specific events like a code deployment. Additionally, it facilitates the implementation of versioning and retention policies for efficient management of historical backups.
* **Monitoring disk space**. Continuous monitoring of disk space is crucial to prevent storage-related challenges. You can use scripting to enable real-time monitoring of available disk space on your servers or storage devices. You can set thresholds to create alerts or actions when your disk space falls below a certain level. With scripting, you can generate reports or log events for historical analysis.
* **CI/CD**. Automation scripts are crucial to streamline the building, testing, and deployment of application code. When integrated with continuous integration and continuous deployment (CI/CD) tools, scripts run automated pipelines whenever code changes occur. Scripts can also implement rollbacks and automated testing procedures to maintain code quality and application reliability.
* **Log file rotation**. Automating log file rotation is a common practice for managing log files efficiently. You can use scripting to automate tasks such as compressing, archiving, and deleting old log files. This ensures that log files do not consume excessive disk space and are organized for convenient retrieval.

### Scripting Languages

Scripting languages are programming languages that are used to automate various tasks and procedures. Scripts are **interpreted at runtime**, unlike lower-level programming languages, which must be compiled before they run.

Some of the most commonly used scripting languages are Python, JavaScript, Ruby, Bash, and PowerShell.

#### Bash

Bash scripts can be used to:

* Compress and archive files for backup
* Filter, parse, and insert log files into databases
* Schedule scripts to automate tasks
* Deploy scripts to perform system administration and maintenance

Bash scripts use the .sh file extension, and scripts written with the language start with a #!, which is commonly referred to as a shebang.

#### PowerShell

PowerShell is a command-line shell and scripting language. As a Microsoft product, it comes preinstalled locally on Windows-based systems, and is built on .NET. PowerShell scripts are often used for system management tasks, like:

* User account management
* Managing processes and services
* Registry key management
* Managing infrastructure as code

PowerShell scripts use the .ps1 file extension, and can either run interactively from the PowerShell prompt or run directly like any executable.

PowerShell uses a set of built-in commands known as **cmdlets** that follow a standard verb- noun naming scheme.

Bash is the default shell installed locally on Linux and Mac systems, while PowerShell is the default shell on Windows.

### Synchronous and Asynchronous Processing

#### Synchronous processing

Synchronous processing, sometimes referred to as blocking, is a traditional approach to scripting where tasks are run sequentially. In synchronous processing, each task is run one-by-one, in the order you defined them in your script. When a script encounters a time-consuming operation, such as reading a large file, the entire script is paused, or blocked, until it completes the operation. This can lead to inefficient resource usage and slower run times.

Synchronous processing is useful when you need a predictable and straightforward order of operations. Synchronous processing generally means more straightforward code that's more convenient to maintain. Synchronous processing is not well-suited for situations when parallelism is required.

#### Asynchronous processing

Asynchronous processing allows tasks to run independently without blocking the processing of the script. Instead of waiting for a task to complete, the script continues running other tasks. This non-blocking behavior results in more efficient resource utilization. Asynchronous processing is well-suited for tasks that have no dependencies with one another, and can be run in parallel. These might include handling multiple client requests or performing I/O intensive operations. Asynchronous processing can significantly improve the overall performance and responsiveness of your applications.

Asynchronous code typically involves the use of callbacks (or promises) to manage the flow of operations. With these mechanisms, you can specify what should happen after a task is completed, without waiting for it to finish. Many asynchronous systems, like Node.js, use an event loop to manage asynchronous tasks. This event-driven approach efficiently handles tasks, such as I/O operations, by delegating them to background processes.

### Processing in Bash and PowerShell

In Bash and PowerShell, synchronous processing is the default behavior. When you run a series of commands, as in the following Bash example, they run in the order they appear in the script. 

```
echo "This is a synchronous command"
echo "This is another synchronous command"
```

One way of implementing asynchronous processing with Bash and PowerShell is by using the & operator. In the following basic example below, all tasks run concurrently, and the script proceeds without waiting for each individual task completion. You will learn more about operators later in this module.

```
./script.py & 
./script2.py & 
./script3.py &
```

#### Processing in AWS Lambda functions

In the context of building AWS infrastructure, you can invoke AWS Lambda functions synchronously and asynchronously. Synchronous invocations are generally appropriate for short-lived functions, while asynchronous invocations are suited for longer-running functions. In synchronous invocations, the caller waits for the function to finish running before continuing. In asynchronous invocations, the caller does not wait for the function to finish running before continuing. Asynchronous invocations are more scalable than synchronous invocations. To learn more, see [Comparing Lambda Invocation Modes](https://docs.aws.amazon.com/lambda/latest/operatorguide/invocation-modes.html)in the AWS Lambda Operator Guide.

### Knowledge Check

#### What is a primary characteristic of synchronous processing?

* Tasks run one after the other in a sequential manner

Wrong answers:

* Tasks run in parallel
* Tasks overlap and continue before others complete
* Tasks are completely independent of each other

#### What is the primary focus of scripting?

* Automation of specific tasks

Wrong answers:

* Developing complex algorithms
* Building graphical UIs
* Low-level memory manipulation

#### What is the standard file extension for PowerShell scripts?

* .ps1

Wrong answers:

* .bat
* .ps
* .sh

### Summary

#### Scripting languages

Scripts are configuration files that can help efficiently automate routine computing tasks. A script offers a straightforward set of instructions to complete small, specific tasks. Some of the most commonly used scripting languages are Python, JavaScript, Ruby, Bash, and PowerShell. The following is a list of the main scripting languages and their characteristics.

* Python is a versatile programming language that is commonly used for scripting and applications.
* JavaScript is a popular scripting and programming language, and it’s often referred to as the scripting language of the web. This is because JavaScript is commonly used by developers to make webpages more interactive.
* Ruby is a general-purpose scripting language that is intuitive and human-readable. Ruby scripts are used to automate a variety of tasks, from basic system administration to testing applications.
* Bash is a common shell and scripting language for Linux and Mac operating systems. It is a command-line interpreter that gives you the ability to automate tasks by writing plaintext scripts that contain a series of commands.
* PowerShell is a command-line shell and scripting language. As a Microsoft product, it comes preinstalled locally on Windows-based systems, and is built on .NET.

#### Types of processing

##### Synchronous processing

**Synchronous** processing is a traditional approach to scripting where tasks are run sequentially. In synchronous processing, each task is run one by one in the order you defined them in your script. Synchronous processing is useful when you need a predictable and straightforward order of operations.

##### Asynchronous processing

**Asynchronous** processing allows tasks to run independently without blocking the processing of the script. Instead of waiting for a task to complete, the script continues running other tasks. Asynchronous processing can significantly improve the overall performance and responsiveness of your applications.

## AWS CLI

### Pre-assessment

#### Which of the following is a characteristic of the AWS Command Line Interface (AWS CLI)?

* It is compatible with Linux and Windows shells.

Wrong answers:

* It only supports networking and storage AWS services.
* It provides a graphical user interface (GUI) for better visibility.
* It is exclusive to on-premises environments.

You can use the AWS CLI in many different environments, including Linux and Windows shells.

The AWS CLI supports a wide range of services beyond just networking and storage. The AWS CLI is a command-line tool and does not provide a GUI. The AWS CLI is designed for cloud environments and is not exclusive to on-premises environments.

#### True or False: The AWS Command Line Interface (AWS CLI) provides the capability to perform tasks equivalent to those in the console, but from a command prompt or terminal program.

* True

Wrong answers:

* False

#### How does AWS CloudShell benefit users in terms of accessibility?

* It is accessible from the AWS Management Console.

Wrong answers:

* It is only accessible from a specific type of browser.
* It requires users to install a proprietary software.
* It is accessible only through the AWS Command Line Interface (AWS CLI).

AWS CloudShell is accessible from the AWS Management Console, requiring no installation and providing a web-based shell environment.

CloudShell is accessible from various web browsers. AWS CloudShell does not require users to install any software. While it includes the AWS CLI, it is not limited to AWS CLI access.

### The tools yo interact with AWS services

* The **AWS Management Console** is a web-based graphical user interface (GUI) that provides a visual means of interacting with AWS services. The console is a good choice for tasks that require manual management and exploration of AWS services.
* AWS provides **SDKs** for various programming languages, such as Python, Java, Ruby, and more. SDKs are libraries that streamline the process of making programmatic requests to AWS services. SDKs abstract many of the low-level details of the AWS API, making it more convenient for developers to integrate AWS functionality into their applications.
* **AWS CloudFormation** is an AWS service that gives you the ability to define and provision AWS infrastructure using templates. You write the templates in JSON or YAML, and use them to describe AWS resources and their desired configurations. Use CloudFormation to create and manage resources in a predictable and repeatable manner.
* The **AWS CLI**, the focal point of this topic, is a command-line tool ideal for automating interactions with AWS services. The AWS CLI offers a comprehensive set of commands for resource configuration and management. It's a useful tool for writing scripts that interact with AWS services.

### Getting started with the AWS CLI

The AWS CLI is a powerful tool that allows for programmatic interaction with AWS services from the command line.

The AWS CLI provides the capability to perform tasks equivalent to those in the console, but from a command prompt or terminal program. With the AWS CLI, you can explore service capabilities and create scripts for resource creation and management. You can use the AWS CLI in many different environments, including Linux and Windows shells.

#### AWS CLI versions

AWS CLI version 2 is the latest major release, featuring support for the most recent AWS features. Some features in version 2 are not available in version 1. If you are a version 1 user, you need to upgrade to access the latest functionality. During upgrades, be aware that there are breaking changes between versions that might require script adjustments. For version history and updates, see the [AWS CLI Version 2 Changelog](https://raw.githubusercontent.com/aws/aws-cli/v2/CHANGELOG.rst) on GitHub.

### Benefits of using the AWS CLI

* **Comprehensive service coverage**. Automation is a key function of scripting.
* **Cross-platform compatibility**. The AWS CLI is platform-agnostic.
* **Output customization**. By default, the output is JSON. But it can be changed, for example, to text.
* **Easy configuration**. Using credentials through AWS SSO, importing credentials from .csv file, using wizard with a guided walkthrough of configuring AWS credentials.
* **Interactive features**.

### Installing the AWS CLI

Before starting with the AWS CLI, you need an active AWS account and IAM credentials. You should create a user with least privilege to provide access credentials to the tasks you will be running in AWS. After creating an account and IAM credentials, you can install the AWS CLI on your computer. You can alternatively access the AWS CLI using a Docker image or using CloudShell.

### Examples of creating a streamlined solution

#### Components

* An Amazon Simple Storage Service (Amazon S3) bucket to store car pictures.
* An Amazon Elastic Compute Cloud (Amazon EC2) instance to host a web application.
* An Amazon Relational Database Service (Amazon RDS) instance for managing customer data.
* A Lambda function to process images when they are uploaded.

```
aws s3api create-bucket --bucket <bucket-name> --region <region>
aws ec2 run-instances --image-id ami-XXXXXXXXXXXXXXXXX --instance-type t2.micro --key-name my-key-pair
aws rds create-db-instance --db-instance-identifier my-db-instance --db-instance-class db.t2.micro --engine mysql --allocated-storage 20 --master-username myuser --master-user-password mypassword
aws lambda create-function --function-name my-lambda-function --runtime nodejs18.x --role arn:aws:iam::123456789012:role/execution-role --handler index.handler --code file://my-lambda.zip
```

### AWS CloudShell

CloudShell is a browser-based shell that is built right into the AWS Management Console. It provides access to a Linux machine with the AWS CLI and tools installed, all without the need to provision an EC2 instance. And because CloudShell comes preconfigured with tools like PowerShell and Python, you can start using it immediately without any additional setup.

CloudShell provides you with a persistent environment, meaning that your credentials, configuration changes, and command history is maintained between sessions.

CloudShell also lets you run commands using your preferred shell, such as Bash or PowerShell. The machine uses your pre-authenticated IAM user credentials for immediate use of the AWS CLI commands. And because CloudShell also has access to resources in your AWS account, you can manage those resources immediately.

CloudShell has a number of common use cases, such as:

* Testing and troubleshooting
* Quickly accessing resources to run scripts through the shell
* Developing and testing Lambda functions by cloning code repositories into Cloudshell
* Experimenting with AWS services without affecting production resources

These use cases are possible because of the pre-installed software tools that come with CloudShell. These tools include shells like Bash and PowerShell, CLIs such as AWS CLI and AWS Tools for PowerShell, and runtimes like node.js and Python. You can also use the pre-installed development tools and utilities, like code repositories and text editors.

### Demo: Getting Started with AWS CloudShell

Uploading a file within CloudShell, creating an S3 bucket, adding the file to the bucket.

1. **IAM permissions**. To obtain permission for AWS CloudShell attach the following AWS managed policy to your AWS Identity and Access Management (IAM) identity (such as a user, role, or group): **AWSCloudShellFullAccess**: Provides users with full access to AWS CloudShell and its features. Add a policy that grants, at a minimum, the **s3:CreateBucket** and **s3:PutObject permissions**.
2. Create a file add_prog.py:
```
import sys
x=int(sys.argv[1])
y=int(sys.argv[2])
sum=x+y
print("The sum is",sum)
```
3. **Option 1: Signing in to AWS Management Console – IAM user sign-in**. You can access the AWS Management Console by using an IAM users sign-in URL.
4. **Option 2: Signing in to AWS Management Console – Main sign-in page**.
5. **Selecting a Region**. Navigate to the Region selection drop-down menu and select a supported AWS Region.
6. **Launching CloudShell**. From the AWS Management Console, you can launch CloudShell by choosing one of the following options:
 a. On the navigation bar, choose the **CloudShell** icon.
 b. In the Search box, type **CloudShell**, and then choose **CloudShell**.
 c. In the Recently visited widget, choose **CloudShell**.
 d. Choose **CloudShell** on the console toolbar, on the lower left of the console.
7. **Adjusting your CloudShell workspace**.
 a. To adjust the height of your CloudShell session, drag the = icon.
 b. To switch your CloudShell session to a full screen,  choose the **Open in new browser tab** icon.
8. **Choosing a shell**. To choose a pre-installed shell to work with, enter its program name at the command-line prompt. By default, CloudShell opens with a Bash workspace.
 a. **PowerShell (pwsh)**. When you switch to PowerShell, the symbol at the command prompt updates to **PS>**.
 b. **Z shell (zsh)**. When you switch to Z shell, the symbol at the command prompt updates to **%**.
 c. **Bash (bash)**. When you switch back to Bash, the symbol at the command prompt updates to **$**.
9. **Uploading a file to CloudShell**.
 a . To check your current working directory, enter **pwd** at the command prompt. When you press Enter, the shell returns your current working directory (for example, **/home/cloudshell-user**).
 b. To upload a file to this directory, go to the **Actions** drop-down menu and choose **Upload file**. The **Upload file** dialog box appears.
 c. In your system's **File upload** dialog box, select the text file that you created for this tutorial (**add_prog.py**) and choose **Open**.
 d. A progress bar tracks the upload. If the upload is successful, a message confirms that **add_prog.py** was added to the root of your home directory. You can verify this by using the ls command.
 e. To create a directory for the file, enter the make directories command: **mkdir mysub_dir**.
 f. To move the uploaded file from the root of your home directory to the new directory, use the mv command: **mv add_prog.py mysub_dir**.
 g. To change your working directory to the new directory, enter **cd mysub_dir**. The command prompt updates to indicate you have changed your working directory.
 h. To view the contents of the current directory, mysub_dir, enter the **ls** command. The contents of the working directory are listed and include the file that you just uploaded.
10. **Downloading a file from CloudShell**. To download a file, go to the **Actions** menu and choose **Download file**. The **Download file** dialog appears. In the Download file dialog box, enter the path for the file to be downloaded. Note that you can use absolute or relative paths when specifying a file for download. With relative pathnames, **/home/cloudshell-user/** is added automatically to the start by default. So, to download the **add_prog.py** file that you created and uploaded, both of the following paths are valid:
 a. **Absolute path**: /home/cloudshell-user/mysub_dir/add_prog.py
 b. **Relative path**: subfolder/add_prog.py
 c. Choose **Download**.
11. **Removing a file from CloudShell**.
 a. **find -type f -name '*.pdf' -delete**
12. **Restarting a shell session**. To restart a shell session, choose **Actions**, then **Restart AWS CloudShell**. You're notified that restarting CloudShell stops all active sessions in the current **Region**. To confirm, choose **Restart**.
12. **Deleting a shell session home directory**. To delete a shell session, choose **Actions**, then **Delete AWS CloudShell home directory**. You will be notified that deleting AWS CloudShell home directory deletes all data currently stored in your CloudShell environment. To confirm deletion, enter **delete** in the text input field, and then choose **Delete**. CloudShell stops all active sessions in the current Region and creates a new environment immediately.
 a. **Manually exiting shell sessions**: With the command line, you can leave a shell session and log out using the **exit** command. You can then press any key to reconnect and continue to use CloudShell.
13. **Editing your file's code and running it using the command line**. Edit the file to add 3 numbers a, b, and c.
 a. Run the file **python3 add_prog.py 4 5 6**. Output should be **15**.
14. **Using CloudShell to create a bucket and add a file as an object in an Amazon S3 bucket**.
 a. **Create a bucket**: **aws s3api create-bucket --bucket insert-unique-bucket-name-here   --region us-east-1**.
 b. **Note that if you're creating a bucket outside of the us-east-1 Region, add create-bucket-configuration with the LocationConstraint parameter to specify the Region. For example**: **aws s3api create-bucket --bucket my-bucket --region eu-west-1 --create-bucket-configuration LocationConstraint=eu-west-1**.
 c. If the call is successful, the command line displays a response from the service similar to the following output: **{ "Location": "/insert-unique-bucket-name-here" }**
 d. **Upload the file to the bucket**: **aws s3api put-object --bucket insert-unique-bucket-name-here --key add_prog --body add_prog.py**.
 e. After the object is uploaded to the Amazon S3 bucket, the command line displays a response from the service similar to the following output: **{"ETag": "\"ab123c1:w:wad4a567d8bfd9a1234ebeea56\""}**. The ETag is the hash of the object that was stored. You can use this hash to check the integrity of the object uploaded to Amazon S3.

### Demo: Editing a File with GNU (GNU's Not Unix) Nano

1. Check: **nano --version**.
2. If no version is returned run **apt install nano** or **yum install nano**.
3. **Running nano**: **nano**.
4. **Entering text and saving changes**.
 a. Once finished adding the lines of text, **Ctrl + S** is used to save the file. A notification is received stating the number of lines written, which can be seen at the bottom center of the page, just above the shortcut list. **Ctrl + X** is used to exit the editor.
 b. Note: If you attempt to exit nano without saving after editing the file, you will be prompted to save or discard your changes.

### [Lab: Using the AWS CLI in Bash to Interact with AWS](./W07Lab1-AWSCLIInBash.md)

### Knowledge Check

#### How does AWS CloudShell streamline the process of testing AWS services?

* It provides a pre-configured environment with the AWS CLI and common tools.

Wrong answers:

* It requires users to create a separate AWS account.
* It is limited to a core set of AWS services.
* It requires users to install the AWS Command Line Interface (AWS CLI) on their local machines.

#### What is the primary purpose of the aws ec2 run-instances command in the AWS Command Line Interface (AWS CLI)?

* To create and launch new Amazon Elastic Compute Cloud (Amazon EC2) instances

Wrong answers:

* To terminate existing Amazon Elastic Compute Cloud (Amazon EC2) instances
* To check the status of running Amazon Elastic Compute Cloud (Amazon EC2) instances
* To list all available Amazon Elastic Compute Cloud (Amazon EC2) instances in an AWS Region

#### How does output customization in the AWS Command Line Interface (AWS CLI) enhance user experience?

* It provides flexibility in choosing output formats and content.

Wrong answers:

* By automatically formatting output based on user preferences
* It  speeds up command operations.
* It offers exclusive customization options for AWS CLI power users.

The AWS CLI requires user intervention for output customization. It does not automatically format output. Increased speed is not a direct result of output customization. There aren't exclusive options reserved for AWS CLI power users.

### Summary

#### AWS CLI

The AWS CLI is a powerful tool that allows for programmatic interaction with AWS services from the command line. Benefits of using the AWS CLI include the following:

* Comprehensive service coverage
* Cross-platform compatibility
* Output customization
* User-friendly configuration
* Interactive features

#### AWS CloudShell

CloudShell is a browser-based shell that streamlines the management of AWS resources. It comes pre-authenticated with your console credentials and includes common development and operations tools such as the following:

* Testing and troubleshooting
* Quickly accessing resources to run scripts through the shell
* Developing and testing Lambda functions by cloning code repositories into CloudShell
* Experimenting with AWS services without affecting production resources

## Scripting with the Bash Shell

### Bash Fundamentals

* **System variables** are special, built-in variables created and maintained by the Linux operating system. As an example, the system variable USERNAME indicates the name of the current user.
* **User-defined variables** are created by you, the user. You typically use them to store custom data or values specific to your script.

#### Capitalization in system-defined variables

In Bash, system-defined variables are typically defined in capital letters. This is a convention that most Bash scripts and programs follow.

```
#!/bin/bash
name="Shirley Rodriguez"
car="Mercedes Benz"
echo "Customer name is $name. $name has a $car."
```

### Arrays

An array is a data structure that gives you the ability to store multiple values under a single variable. You identify each value by using an index, starting from 0. Arrays are versatile for organizing and managing related pieces of information.

```
#!/bin/bash

car_wash_services=("Basic wash" "Premium wash" "Interior detail" "Full service")
echo ${car_wash_services[0]} #output: Basic wash
```

### Functions

Functions are named blocks of code that you can define and reuse within your scripts. By using functions, you can encapsulate a series of commands, making your code more modular, convenient to read, and maintainable. With functions, you can group commands and give them a meaningful name.

```
function_name() {
   [block of code]
}

function_name
```

```
#!/bin/bash
greet() {
    echo "Welcome to AnyCompany Car Washes!"
}
greet
```

#### Functions types and variable scope

In Bash functions, variables play a crucial role in storing and manipulating data. When working with functions, it is important to understand the different types of variables you can create and when to use them. In Bash, your variables can have **local** or **global** scope.

By default, all variables you define in Bash are global variables. Global variables are variables you can access anywhere from within your script.

Local scope variables are only accessible inside your function. You can create local variables with the same name in different functions. Local variables you declare inside a function are also separate from global variables with the same name. This gives you the ability to create variables with different levels of visibility, which you can use for different purposes within your scripts. You declare a local variable within a function by using the 'local' keyword.

```
# Global variable
length=5

# Function to calculate the area of a rectangle
calculate_area() {
    local width=3 # Local variable for the width of a rectangle
    local area=$((length*width)) # Calculate the area
    echo "The area of the rectangle is $area square units."
}

# Call the function
calculate_area

# Attempt to access the local variables outside the function
echo "Outside the function: "
echo "Length: $length" #Global variable
echo "Width: $width" #Local variable
```

### Conditionals

```
if [ condition ]
then
[ block of code to run if condition is true ]
fi
```

#### Spacing considerations

In Bash, the spaces before and after a [ ] construct are important for proper syntax and interpretation of the command. Spaces are necessary to distinguish this construct from other parts of the command.

```
#!/bin/bash

num=5

if [ $num -eq 5 ]
then
    echo "Number is 5"
fi
```

```
#!/bin/bash

num=2

if [ $num -ge 1 ] && [ $num -le 10 ]
then
    echo "Number is between 1 and 10"
fi
```

#### If-else statements

```
if [condition]
then
    [block of code to run if condition is true]
else
    [block of code to run if the condition is false]
fi
```

```
#!/bin/bash

num=6

if [ $num -eq 5 ]
then
    echo "Number is 5."
else
    echo "Number is not 5."
fi
```

#### Else if (elif)

```
if [condition1]
then
    [block of code to run if condition1 is true]
elif [condition2]
then
    [block of code to run if condition2 is true]
elif [condition3]
then
    [block of code to run if condition3 is true]
else
    [block of code to run if none of the conditions are true]
fi
```

```
#!/bin/bash

num=8

if [ $num -eq 5 ]
then
    echo "Number is 5."
elif [ $num -eq 10 ]
then 
    echo "Number is 10"
else
    echo "Number is neither 5 nor 10."
fi
```

### Loops

* **For loop**. Use for loops to iterate over a list of items or values and run a set of commands for each item on the list.
* **Until loop**. Use until loops to repeatedly run a set of commands as long as a specific condition remains false.
* **While loop**. Use while loops to repeatedly run a set of commands, as long as a specific condition remains true.

#### For loops

```
for <variable> in <list>
do 
<commands>
done
```

```
#!/bin/bash
for i in $(seq 1 10)
do
   echo $i
done
```
```
#!/bin/bash
for i in {10..20}
do
   echo $i
done
```

You can also run for loops using a three-expression loop. This type of loop has three expressions separated by a semicolon: **initialization**, **condition**, and **update**:

1. **Initialization**: In the initialization expression, you set the initial value of a loop control variable. The initialization expression is run only once, at the beginning of the loop.
2. **Condition**: The condition expression is evaluated before each iteration of the loop. If the condition expression is true, the loop runs. If it evaluates to false, the loop terminates.
3. **Increment or Decrement**: This expression is run at the end, and is responsible for updating the loop control variable in each iteration. It can be an increment or a decrement operation.

```
#!/bin/bash
for ((i=1 ;i<=5; i++)) 
do
   echo "Iteration $i"
done
```

#### While loops

```
while [condition]
do
[commands to be run in each iteration]
done
```

```
#!/bin/bash
count=1
while [ $count -le 5 ];
do
   echo "Count: $count"
   count=$((count +1))
done
```

#### Until loops

The **until** loop is similar to the **while** loop, but it runs a block of code as long as a condition remains false. After the condition becomes true, the until loop stops. Following is the basic syntax of an until loop.

```
until [condition]
do
[commands to run in each iteration]
done
```

```
#!/bin/bash
count=1
until [ $count -gt 5 ];
do
   echo "Count: $count"
   count=$((count+1))
done
```

```
#!/bin/bash

countdown=5

echo "Starting car wash..."

until [ $countdown -eq 0 ];
do
    echo "T-$countdown"
    ((countdown--))
    sleep 1 
done

echo "Your wash is complete!"
```

### [Lab: Using the AWS CLI and Bash to Automate Linux](./W07Lab2-AWSCLIToAutomate.md)

### Knowledge Check

#### What is the purpose of the shebang at the beginning of a script?

* To specify the interpreter that should run the script

Wrong answers:

* To run a script as a background process
* To comment out a line of code in a script
* To encrypt the contents of the script for security

Running scripts in the background is not related to the shebang. Although it starts with #, the purpose of the shebang is not commenting. Encryption is not the purpose of the shebang.

#### True or false: Local variables are accessible from outside of the functions where they are defined

* False

Wrong answer:

* True

Local variables are not accessible from outside of the functions where they are defined.

Global variables are variables that can be accessed anywhere from within the script.

#### What is an if statement used for?

* To run a block of code based on a condition

Wrong answers:

* To define functions and procedures
* To perform arithmetic operations
* To run a file and print its output

### Summary

A Bash script is a plain text file containing a series of commands in the Bash programming language. Bash scripts start with a shebang line. Its purpose is to provide a path to the interpreter, indicating the location of the Bash shell in your system.

```
#!/bin/bash
```

You can set the execute (run) permission for your script file using the chmod command.

```
chmod +x practice
```

You can run a file using the './' notation followed by its name.

```
./practice
```

#### Bash shell elements

##### Variables

Variables are like containers that hold any kind of data. Variables store information that you can use in commands and expressions. There are two types of variables available: system (or environment) variables and user-defined variables. System variables are special, built-in variables created and maintained by the Linux operating system. User-defined variables are created by you, the user.

##### Arrays

An array is a data structure that gives you the ability to store multiple values under a single variable. You identify each value by using an index, starting from 0. Arrays are versatile for organizing and managing related pieces of information. Declaring an array involves listing elements inside parentheses. You access elements in an array by referencing their indices.

##### Loops

You can use loops to run a series of commands in a script repeatedly. Loops are ideal for automating repetitive tasks in a programmatic way:

* Use for loops to iterate over a list of items or values and run a set of commands for each item on the list.
* Use until loops to repeatedly run a set of commands as long as a specific condition remains false.
* Use while loops to repeatedly run a set of commands as long as a specific condition remains true.

##### Conditionals

You can use conditionals to make decisions and control the flow of your script, based on certain conditions. Just like in Python, Bash provides several conditional constructs, including if, else, and else if (elif).

* With the if statement, you can run a block of code if a condition is true.
* By using if-else statements, you can run a block of code if a condition is true and another block of code if the condition is false.
* You can use elif statements within an if-elif-else statement to check multiple conditions sequentially. When the if condition is not met, the script condition evaluates the elif conditions one by one until it finds a true condition or reaches the else block.

##### Functions

Functions are named blocks of code that you can define and reuse within your scripts. By using functions, you can encapsulate a series of commands, making your code more modular, convenient to read, and maintainable. With functions, you can group commands and give them a meaningful name.

## Error Handling and Troubleshooting

### Pre-assessment

#### What is the exit code for a successful command in Bash?

* 0

Wrong answers:

* 1
* 99
* 255

#### What is the primary purpose of the trap command in Bash?

* Catch and handle signals

Wrong answers:

* Stop the script
* Run a command after every line
* Set system variables

The primary purpose of the trap command is to catch and handle signals, allowing the script to respond to specific events.

Terminating a script, running a command after every line, and setting environment variables are not primary functions of the trap command.

#### What does exponential backoff do?

* Increases the wait time between retries exponentially

Wrong answers:

* Increases the script's complexity over time
* Reduces the number of retries gradually
* Reverses the order of retry attempts

Exponential backoff involves progressively increasing the time between retries,  helping avoid overwhelming a system with frequent retry attempts.

Increasing the complexity over time, gradually reducing the number of retries, and reversing the order of retry attempts do not align with the concept of exponential backoff.

#### Which logging level is commonly used to provide additional information for debugging purposes in Bash?

* DEBUG

Wrong answers:

* INFO
* WARNING
* ERROR

The DEBUG logging level is commonly used to provide additional information for debugging purposes, helping cloud application developers identify and troubleshoot issues.

INFO, WARNING, and ERROR serve other purposes in logging.

### Troubleshooting 

#### Error handling in scripting

Error handling is the practice of anticipating, detecting, and addressing errors that might occur while you run a script.

#### Benefits of error handling

1. **Reliability**. Error handling ensures that a script behaves predictably, even in the presence of errors. Error handling can help prevent unexpected failures and catastrophic system crashes.
2. **Robustness**. Robust scripts can gracefully handle unexpected situations, recover from errors, and continue running. They provide a better user experience and minimize downtime.
3. **Effective debugging**. Effective error handling provides detailed information about errors, making it more convenient to diagnose and fix issues. Additionally, error logging provides a clear history of events and errors for review.

### Troubleshooting scripts

Proper error handling, along with systematic troubleshooting, is essential for building reliable and maintainable scripts. Troubleshooting is the process of diagnosing and resolving issues in scripts. It often involves analyzing errors, logs, and script behavior to determine the root causes of problems.

Effective troubleshooting in scripting often involves the following:

* **Understanding error messages**: Interpret error messages and exit codes to determine the nature of the issue.
* **Logging**: Use logging mechanisms to capture relevant information about your script performance, including errors. Analyzing logs can help identify patterns and recurring issues. 
* **Reviewing code**: Inspect your script's code to identify potential sources of errors, such as unhandled edge cases or incorrect assumptions.
* **Testing**: Develop test cases that simulate various scenarios to validate how the script handles errors. Testing can help uncover hidden issues and ensures that error-handling logic works as expected.

### Common errors in scripting

Common issues in scripting can often revolve around syntax, logic, and file referencing errors.

#### Syntax errors

Common syntax errors include unclosed quotes or incorrect use of semicolons. Forgetting to close single or double quotes can lead to syntax errors. Always ensure you open and close quotes properly.

Incorrect use of semicolons for command separation can also cause issues. Use semicolons to separate multiple commands on a single line, but don't forget spaces around them.

Incorrectly referencing variables, such as missing the $ sign, can result in errors.

#### Logic and conditional errors

Incorrect conditional syntax, such as misusing conditional statements like if, elif, and fi, can cause errors. Ensure you are using correct syntax for conditionals.

#### File and directory errors

Attempting to work with files and directories that don't exist will lead to errors. Always check if a file or directory exists before referencing it in your script.

### Error Handling in Bash

Exit codes are numerical codes Bash scripts return to indicate the outcome of commands. Exit codes are an essential part of error handling. You can use exit codes to determine the success or failure of commands in your script. Following is more information about Bash exit code values:

* **0**: This is a standard exit code for successful processing of your code. When your script exits with code 0, it indicates that it ran without errors.
* **1-225**: Non-zero exit codes (1 to 255) typically represent various error conditions. For example, an exit code of 127 often indicates that a command or script was not found.

### Using `set -e` to check exit codes in your commands

You can use the `set -e` option to affect the behavior of your script in response to non-zero exit codes. When you enable `set -e`, if any command returns a non-zero exit code, the script will immediately exit, unless the command is part of a conditional statement. If `set -e` is not enabled, the script will continue running, even if the command returns a non-zero exit code.

```
#!/bin/bash
set -e # Enable error handling

echo "Starting script"

# This command will fail, and the script will immediately exit
ls non_existent_directory

# This line will not be reached
echo "Script continues after ls command"
```

Using `set -e` can streamline error handling by automatically exiting the script on error, reducing the need for explicit error checking after each command. `set -e` can also help diagnose issues quickly, because the script halts as soon as an error occurs.

### Using `$?` to check exit codes in your commands

`$?` is a special variable in Bash that stores the exit status of the most recently run command. You can access the exit status using $? and use it to make conditional decisions based on the outcome of a command.

```
#!/bin/bash

# Attempt to remove non-existent file
rm non_existent_file

# Check the exit code and perform custom error handling
if [ $? -ne 0 ]
then
   echo "Error: Failed to remove the file."
   # Add custom error handling actions here
else
   echo "File removed successfully"
fi

# Continue running script
echo "Script continues running after error handling"
```

Use `$?` in situations where your command might fail, but you want the script to continue processing. `$?` is appropriate for non-critical errors where you want to perform specific actions but continue the script's action. Relying solely on `$`?` for debugging can be challenging because it doesn't automatically halt the script on errors.

#### `set -e` and `$?` usage

In practice, the choice between `set -e` and `$?` depends on the specific requirements of your script. It's common to use a combination of both, where `set -e` is enabled for critical failures, and `$?` for partial failure tolerance.

### Trap and Exit

Using the trap and exit commands is crucial for effectively handling errors and gracefully stopping scripts. With the trap command, you can intercept and respond to signals, while exit ensures a clean exit from the script, preventing side effects. Using these commands is helpful for enhancing script reliability and contributes to a more predictable performance.Using the trap and exit commands is crucial for effectively handling errors and gracefully stopping scripts. With the trap command, you can intercept and respond to signals, while exit ensures a clean exit from the script, preventing side effects. Using these commands is helpful for enhancing script reliability and contributes to a more predictable performance.

#### Using the exit command

By using the exit command in Bash, you can explicitly terminate your script and specify an exit code to indicate the script's outcome. The exit command is useful for controlled script termination and providing exit status information to associated scripts or programs. The exit code can be any integer. As you learned previously, a value of 0 indicates success, while non-zero values indicate errors.

```
exit [EXIT_CODE]
```

#### Using the trap command

By using the trap command in Bash, you can set up signal handlers, which are functions or commands that run in response to specific signals or conditions. This provides a way to customize how your script responds to events, such as errors. The basic syntax for the trap command is as follows:

```
trap 'commands' SIGNAL
```

**A signal is a software interrupt, event, or notification that you can send to a running script to notify it of certain events or request specific actions.**

Signals and the **trap** command help you customize how your script responds to various events. When using **trap**, you are setting up signal handlers to specify how your script should respond when they receive a particular signal. Signals are identified by names, such as **ERR (error)**. Each signal name corresponds to a specific event or action.

```
#!/bin/bash

# Define a custom error handling function
handle_error() {
   echo "An error occurred. Exiting script."
   exit 1
}

# Set up a trap to run the error handling function on ERR signal
trap 'handle_error' ERR

# Simulate an error
non_existent_command
```

### Retries and Backoff

Retrying is a technique for ensuring the resilience and reliability of your scripts. In the context of Bash, a retry refers to the act of reattempting an operation after an initial failure. You usually use retries to handle transient failures, which are temporary errors that might resolve themselves when the operation is run again. The purpose of a retry is to increase the likelihood of successful completion of a task, even when faced with intermittent problems.

#### Implementing retries

You can define variables to control the retry mechanism. The following example includes defining the maximum number of retry attempts, the sleep (seconds) interval between retries, and the exit status code to indicate that a retryable error occurred. Note that the exact number to include is dependent on the characteristics of your application.

```
MAX_RETRIES=3
SLEEP_INTERVAL=5
RETRYABLE_ERROR=1
```

```
MAX_RETRIES=5
SLEEP_INTERVAL=3
RETRYABLE_ERROR=1

retries=0

while [ $retries -lt $MAX_RETRIES ]; do
    # Run an HTTP request 
    curl -I https://aws.amazon.com
    if [ $? -eq 0 ]; then
        # Successful command, exit the loop
        break
    else
        # Retryable error, increment retries and sleep before the next attempt
        retries=$((retries + 1))
        sleep $SLEEP_INTERVAL
    fi

done
if [ $retries -eq $MAX_RETRIES ]; then
    echo "Maximum retry attempts reached. Exiting script."
    exit 1
fi
```

#### Backoff

Backoff refers to the practice of increasing the time interval between consecutive retry attempts in response to an error. Exponential backoff is a strategy you use to progressively increase the waiting time between retries. The purpose of using backoff in retry mechanisms is to reduce the risk of overwhelming the target system and to give it more time to recover or resolve the issue.

```
MAX_RETRIES=5
INITIAL_SLEEP_INTERVAL=3
BACKOFF_MULTIPLIER=2
RETRYABLE_ERROR=1

retries=0

sleep_interval=$INITIAL_SLEEP_INTERVAL
while [ $retries -lt $MAX_RETRIES ]; do
    # Run an HTTP request
    curl -I https://nonexistenturl.com
    if [ $? -eq 0 ]; then
        # Successful command, exit the loop
        break
    else
        # Retryable error, increment retries, apply exponential backoff, and sleep
        retries=$((retries + 1))
        sleep $sleep_interval
        sleep_interval=$((sleep_interval * BACKOFF_MULTIPLIER))
    fi
done

if [ $retries -eq $MAX_RETRIES ]; then
    echo "Maximum retry attempts reached. Exiting script."
    exit 1
fi
```

### Logging

Logging is an important record-keeping mechanism in Bash scripts. Logs capture information such as script start and end times, events, and errors. This data is useful for understanding script behavior during troubleshooting. You can also use logs as a debugging aid, providing insights into flow control, actions taken by the script, and much more.

### stdout and stderr

There are two primary channels for the output that a Bash script or command produces:

* **stdout (standard output)**: This is the default channel where regular output is sent. It includes the normal, expected output for a command.
* **stderr (standard error)**: This channel is specifically designed for error messages. If something goes wrong while running your script or command, the error messages are sent to stderr.

You can capture both regular and error messages into a log file, because they can provide valuable information for debugging and monitoring. The following example is a basic script that produces an error.

```
 #!/bin/bash

echo "Attempting to divide 10 by 0"
result=$((10 / 0))

echo "Result: $result"
```

Now, you will redirect the stderr to a file. By running the following command, the message is written to the error.log file. In Bash, **2>** is the syntax you use to redirect stderr output of a command or script. Run the following script and then examine the contents of the error.log file.

```
./practice 2> error.log
```

### Logging levels

Logging levels are a way to categorize log messages based on their severity or importance. They provide a structured approach to differentiate between various types of messages in logs. The choice of logging levels is not strictly standardized in Bash itself, but is often adopted from general logging conventions from other programming languages or frameworks. Cloud application developers can define their logging levels based on the specific requirements of their scripts and projects.

1. **CRITICAL (or FATAL)**. Use CRITICAL to log severe issues that can cause a script failure. CRITICAL is reserved for urgent errors that require immediate attention and intervention.
2. **ERROR**. Use ERROR to log error messages or any unexpected conditions that could impact your script's operation. Errors often indicate issues that you should address for the script to function correctly.
3. **WARN**. Use WARN to log information that might not be errors, but could lead to potential problems if not addressed. It serves as a warning about conditions that might need further investigation.
4. **INFO**. Use INFO to log general information about the script's progress or key events.
5. **DEBUG**. Use DEBUG to log detailed information for debugging purposes.

The logging levels follow a hierarchy where each level includes all the levels below it in terms of severity. For example, for the logging level, DEBUG, it includes DEBUG, INFO, WARN, ERROR, and CRITICAL messages.

### Logging functions

Logging functions are functions that encapsulate the logic of recording messages at different levels of severity. Using functions enhances your code's modularity and provides convenient adjustment of how log messages are handled.

There are many ways you can implement logging functions. The following is a basic example that defines several logging functions ('log_debug', 'log_info', and more). Each function appends a formatted log message to the log file 'script.log' based on the log level.

```
#!/bin/bash
LOG_FILE="script.log"
log_debug() {
    echo "$(date): DEBUG - $1" >> "$LOG_FILE"
}
log_info() {
    echo "$(date): INFO - $1" >> "$LOG_FILE"
}
log_warn() {
    echo "$(date): WARN - $1" >> "$LOG_FILE"
}
log_error() {
    echo "$(date): ERROR - $1" >> "$LOG_FILE"
}
# Simulate various log messages
log_info "Script started."
log_warn "Warning: Something unexpected happened."
log_error "Error: Critical issue occurred."
```

### Log rotation

Log rotation is a preventive measure to manage log files efficiently, preventing them from becoming too large. It involves creating new files and archiving old ones, ensuring logs size is manageable.

```
#!/bin/bash

MAX_LOG_SIZE=1000000
CURRENT_LOG_SIZE=$(wc -c < "script.log")

if [ "$CURRENT_LOG_SIZE" -gt "$MAX_LOG_SIZE" ]; then
    mv "script.log" "script.log.old"
    touch "script.log"
fi
```

### Centralized logging

In some circumstances, you might need to gather log data from multiple sources into a centralized location. This streamlines log analysis and monitoring across a distributed system.

In the following example, you use scp (Secure Copy Protocol) to transfer your local log file (script.log) to a central log server (central-log-server). This is a basic example of centralized logging where you consolidate logs from various sources for streamlined analysis.

```
#!/bin/bash

CENTRAL_LOG_SERVER='central-log-server.com'
LOG_FILE='script.log'

scp "$LOG_FILE" "#CENTRAL_LOG_SERVER:/path/to/central/logs/"
```

### [Lab: Troubleshooting AWS CLI and Bash in Linux Environments](./W07Lab3-TroubleshootingAWSCLI.md)

### Knowledge Check

#### What does the WARN logging level typically indicate?

* A potential issue or warning

Wrong answers:

* An informational message
* A critical error
* Standard program output

#### What is a potential consequence of implementing retry strategies without backoff?

* Overwhelmed system with retry attempts

Wrong answers:

* Increased script performance
* Faster error recovery
* More script dependencies

Aggressive retry strategies without backoff can flood the system with repeated attempts, hindering recovery.

#### What is the significance of an exit code of 2?

* Unsuccessful operation

Wrong answers:

* Successful operation
* DEBUG logging level enabled
* Security alert

An exit code of 2 typically represents an error. 

#### What is a signal in Bash?

* An event or notification you can send to a script

Wrong answers:

* A special type of conditional statement
* A method for encrypting data during transmission
* The act of re-attempting an operation after an initial failure

In Bash, a  signal is a form of inter-process communication you use to send software interrupts, events, or notifications to scripts.

### Summary

#### Troubleshooting the Bash shell

#### Trap and exit

Using the **trap** and **exit** commands is crucial for effective error handling and graceful termination of scripts. With the **trap** command, you can intercept and respond to signals, while **exit** ensures a clean exit from the script, preventing side effects. Using these commands is helpful for enhancing script reliability and contributes to a more predictable performance.

#### Retries and backoff

Retrying is a technique for ensuring the resilience and reliability of your scripts. In the context of Bash, a retry refers to the act of reattempting an operation after an initial failure. You usually use retries to handle transient failures, which are temporary errors that may resolve themselves when the operation is run again. The purpose of a retry is to increase the likelihood of successful completion of a task, even when faced with intermittent problems.

Backoff refers to the practice of increasing the time interval between consecutive retry attempts in response to an error. Exponential backoff is a strategy you use to progressively increase the waiting time between retries. The purpose of using backoff in retry mechanisms is to reduce the risk of overwhelming the target system and give it more time to recover or resolve the issue.

#### Logging

Logging is an important record-keeping mechanism in Bash scripts. Logs capture information, such as script start and end times, events, and errors. This data is useful for understanding script behavior during troubleshooting. You can also use logs as a debugging aid, providing insights into flow control, actions taken by the script, and much more.
