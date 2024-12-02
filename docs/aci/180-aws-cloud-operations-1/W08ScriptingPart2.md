# Scripting Part 2

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to repo's main [README.md](../../../README.md)

## AWS Tools for PowerShell

The AWS Tools for Powershell are a set of modules built on the AWS SDK for .NET. A module refers to a collection of cmdlets, functions, and scripts that work together to provide specific functionality related to Amazon Web Services (AWS) services. The AWS Tools for Powershell are designed to facilitate scripting operations on AWS resources directly within the PowerShell command line.

### Pre-assessment

#### What are AWS Tools for PowerShell?

* A collection of PowerShell cmdlets for managing AWS resources

Wrong answers:

* A web-based interface for AWS management
* A Python library for AWS automation
* A virtualization platform on AWS

AWS Tools for PowerShell are a set of PowerShell cmdlets, functions, and scripts specifically designed for managing AWS resources.

AWS Tools for PowerShell are not a web-based interface for AWS resources. AWS Tools for PowerShell are not focused on Python. They are not a virtualization platform, either.

#### True or False: AWS Tools for PowerShell can be used to launch AWS CloudFormation stacks. 

* True

Wrong answer:

* False

AWS Tools for PowerShell integrate with AWS CloudFormation, facilitating the creation and management of AWS resources through PowerShell scripts, providing infrastructure as code capabilities.

#### Which statement is true regarding the installation of AWS Tools for PowerShell on Windows-based Amazon Machine Images (AMIs)?

* AWS Tools for Powershell are installed by default on Windows-based AMIs.

Wrong answers:

* AWS Tools for Powershell cannot be installed on Windows-based AMIs.
* AWS Tools for Powershell are installed by default on Windows-based AMIs only when using specific AWS Regions.
* AWS Tools for Powershell are installed by default only on certain Windows-based AMIs.

### PowerShell characteristics

1. **Simplified automation**. AWS Tools for PowerShell provides a comprehensive set of PowerShell cmdlets for all AWS services.
2. **Enhanced productivity**. The PowerShell cmdlets in AWS Tolls for PowerShell are designed to be idiomatic and easy to use, enabling you to quickly run tasks and manage your AWS infrastructure efficiently.
3. **Flexible credential management**. AWS Tools for PowerShell supports credential management options including IAM user credentials, temporary security tokens, and IAM roles.
4. **Cross-platform compatibility**. AWS Tools for PowerShell can be installed on computers running Windows, Linux, or macOS operating systems.
5. **Open source availability**. AWS Tools for PowerShell is open-sourced under the Apache version 2 license.
6. **Modular architecture** allows you to install only the modules you need.

### AWS Tools for PowerShell and Windows-based AMIs

The AWS Tools for Windows PowerShell are installed by default on all Windows-based Amazon Machine Images (AMIs).

### AWS Tools for PowerShell Cmdlet Reference

Refer to the [AWS Tools for PowerShell Cmdlet Reference guide](https://docs.aws.amazon.com/powershell/latest/reference/) to learn how to use AWS Tools for PowerShell to perform common AWS tasks.

### AWS Tools for PowerShell packages

1. **AWS.Tools** introduces a modularized approach to AWS Tools for PowerShell, so you can selectively load only the necessary service modules. This version is ideal for users who want a tailored, hands-on experience with AWS resource management. You can install this version on computers running PowerShell Core 6.0 or later on Windows, Linux, or macOS. You can also use it with Windows PowerShell 5.1 or later on Windows with the .NET Framework 4.7.2 or later.
2. **AWSPowerShell.NetCore** consists of a single module that contains support for all AWS services. You can install this version on the same computer operating systems and versions as AWS.Tools. This version is appropriate for users who prefer a single, convenient-to-install module and are not concerned about module size.
3. **AWSPowerShell**. This version of AWS Tools is compatible only with Windows computers that are running Windows PowerShell versions 2.0 through 5.1. This legacy version is appropriate for users that are running older versions of PowerShell and are not able to upgrade.

### Key features

1. **IAM integration**. The AWS Tools for PowerShell are flexible, so you can handle credentials, including support for the AWS Identity and Access Management (IAM) infrastructure. You can use the tools with IAM user credentials, temporary security tokens, and IAM roles.
2. **Parameter validation and tab completion**. PowerShell cmdlets include robust parameter validation, ensuring that input values meet the required criteria. Tab completion is also supported, which enhances the user experience by providing suggestions during command entry.
3. **Filtering and querying**. With AWS Tools for PowerShell, you can filter and query AWS resources efficiently, providing precise retrieval and manipulation of data. This is particularly useful for scripting and automation.
4. **Error handling and logging**. AWS Tools for PowerShell offers detailed error handling and logging capabilities, aiding in troubleshooting and monitoring script launches. This is crucial for maintaining the reliability of automated processes.
5. **Cross-platform compatibility**. AWS Tools for PowerShell work on various platforms, which offers flexibility for users who might need to manage AWS resources from different operating systems.
6. **Updates and maintenance**. Regular updates and maintenance releases for AWS Tools for PowerShell keep the toolset current with AWS service changes, bug fixes, and improvements. This ensures compatibility with the latest AWS features and APIs.

### Demo: AWS Tools for PowerShell

#### Prerequisites

To follow along with this demo, you will need to verify that your system has Windows PowerShell 5.1 or later, or PowerShell Core 6.0 or later.

#### Verifying your PowerShell version

Open PowerShell ISE by selecting the Windows icon and typing PowerShell. After the PowerShell ISE pops up as an option, select the arrow next to it, then select **Run as administrator**.

```
$PSVersionTable
```

#### Installing AWS Tools for PowerShell on Windows

You can install the modularized version of AWS Tools for PowerShell, AWS.Tools, on computers that are running Windows with Windows PowerShell 5.1, or PowerShell Core 6.0 or later. 

**Note**: AWSPowerShell is installed by default on all Windows-based AMIs.

#### Installing AWS.Tools on Windows (Option 1)

One option for installing **AWS.Tools** is by using the cmdlets in the **AWS.Tools** package. The **AWS.Tools.Installer** module streamlines the installation and update of other AWS.Tools modules. The **AWS.Tools.Installer** requires, automatically downloads, and installs an updated version of **PowerShellGet**.

The **AWS.Tools.Installer** module automatically keeps your module versions in sync. When you install or update to a newer version of one module, the cmdlets in the **AWS.Tools.Installer** automatically update all of your other **AWS.Tools** modules to the same version.

#### Installing AWS.Tools on Windows (Option 2)

Another installation option is to download the modules from [AWS.Tools.zip](https://sdk-for-net.amazonwebservices.com/ps/v4/latest/AWS.Tools.zip) and extract them in one of the module folders. You can discover your module folders by displaying the value of the **$PSModulePath** environment variable.

After entering the **$PSModulePath** variable, you should have an output similar to the following:

```
PS> $PSModulePath
C:\Users\UserName\Documents\WindowsPowerShell\Modules;
C:\Windows\system32\WindowsPowerShell\v1.0\Modules;
C:\Program Files\WindowsPowerShell\Modules

PS>
```

#### Installing AWS.Tools.Installer on Windows using the Install-Module cmdlet

After starting a PowerShell session, run the following command at the PS> prompt:

```
PS> Install-Module -Name AWS.Tools.Installer
```

If you are notified that the repository is untrusted, it asks you if you want to install anyway. Enter y to allow PowerShell to install the module. To avoid the prompt and install the module without trusting the repository, you can run the command with the -Force parameter.

```
PS> Install-Module -Name AWS.Tools.Installer -Force
```

If you receive a prompt stating "NuGet provider is required to continue", select **Yes**. You will not receive a notification that the installation is complete, but you will be returned to the command line without errors.

#### Installing AWS.Tools modules

After it's complete, you can install the module for each AWS service that you want to use by using the **Install-AWSToolsModule** cmdlet. For example, the following command installs the Amazon EC2 and Amazon S3 modules:

```
PS> Install-AWSToolsModule AWS.Tools.EC2,AWS.Tools.S3 -CleanUp
```

This command also installs any dependent modules that are required for the specified module to work. For example, when you install your first AWS.Tools service module, it also installs **AWS.Tools.Common**. This is a shared module required by all AWS service modules. It also removes older versions of the modules and updates other modules to the same newer version.

#### Scoping AWS Tools installations

By default, the previous command installs modules into the **%USERPROFILE%\Documents\WindowsPowerShell\Modules** folder. To install the AWS Tools for PowerShell for all users of a computer, run the following command in a PowerShell session with administrator privileges:

```
PS> Install-AWSToolsModule [ModuleName] -Scope [UserScope]
```

For example, the following command installs the IAM module to the **%ProgramFiles%\WindowsPowerShell\Modules** folder that is accessible by all users:

```
PS> Install-AWSToolsModule AWS.Tools.IdentityManagement -Scope AllUsers
```

#### Enabling script execution

You must enable PowerShell script execution to load the AWS Tools for PowerShell modules. To enable script execution, you will need to run the Set-ExecutionPolicy cmdlet and set a policy of RemoteSigned. You will need administrator rights for PowerShell to accomplish this task.

While running PowerShell with administrator privileges, enter the following command:

```
PS> Set-ExecutionPolicy RemoteSigned
```

Confirm **Yes** in the pop-up.

#### Verifying module installation

```
PS> Get-Module -ListAvailable
```

You should see **AWS.Tools.Installer** listed as an available module.

#### Updating your AWS Tools for PowerShell on Windows

Periodic updates are necessary for software, including AWS Tools for PowerShell. It is a best practice to update the version you are running locally at a regular interval.

To update or upgrade your AWS.Tools modules to the latest version, run the following command:

```
PS> Update-AWSToolsModule -CleanUp
```

This command updates all of the currently installed AWS.Tools modules and, after a successful update, removes other installed versions. The removal is accomplished by adding **-CleanUp**  to the command.

#### Updating installations that used a downloaded ZIP file

If you installed by using a downloaded ZIP file, do the following:

1. Download the most recent version from the AWS Tools for PowerShell website. Compare the package version number in the downloaded file name with the version number you get when you run the Get-AWSPowerShellVersion cmdlet.
2. If the download version is a higher number than the version you have installed, close all AWS Tools for Windows PowerShell consoles.
3. Install the newer version of the AWS Tools for Windows PowerShell.

### [Lab: Using the AWS CLI in Windows to Interact With AWS](./W08Lab01-AWSCLIInWindowsToInterectAWS.md)

### Knowledge Check

#### Which AWS Tools for PowerShell package is considered a legacy version?

* AWSPowerShell

Wrong answers:

* AWSPowerShell.NetCore
* AWS.Tools
* AWS.Tools.S3

#### How compatible are AWS Tools for PowerShell with cross-platform environments, such as Linux and macOS?

* They are fully compatible.

Wrong answers:

* They are only compatible with Windows.
* Compatibility depends on the specific AWS service.
* They support Linux but not macOS.

#### Which of the following commands installs AWS.Tools modules?

* Install-AWSToolsModule

Wrong answers:

* Set-ExecutionPolicy
* Update-AWSToolsModule -CleanUp
* Get-Module -ListAvailable

The Set-ExecutionPolicy cmdlet changes PowerShell execution policies. Use Update-AWSToolsModule -CleanUp to update or upgrade AWS.Tools modules. Use Get-Module -ListAvailable to verify whether AWS Tools for Windows PowerShell is installed.

### Summary

#### AWS Tools for PowerShell

The AWS Tools for Powershell are a set of modules built on the AWS SDK for .NET. A module refers to a collection of cmdlets, functions, and scripts that work together to provide specific functionality related to AWS services. Benefits of AWS Tools for PowerShell include the following:

* Streamlined automation
* Enhanced productivity
* Flexible credential management
* Cross-platform compatibility
* Open source availability
* Modular architecture

#### AWS Tools for PowerShell packages

##### AWS.Tools

AWS.Tools introduces a modularized approach to AWS Tools for PowerShell, so you can selectively load only the necessary service modules. This version is ideal for users who want a tailored, hands-on experience with AWS resource management.

##### AWSPowerShell.NetCore

AWSPowerShell.NetCore consists of a single module that contains support for all AWS services. You can install this version on the same computer operating systems and versions as AWS.Tools. This version is appropriate for users who prefer a single, convenient-to-install module, and are not concerned about module size.

##### AWSPowerShell

This version of AWS Tools is compatible only with Windows computers that are running Windows PowerShell versions 2.0 through 5.1. This legacy version is appropriate for users that are running older versions of PowerShell and are not able to upgrade.

## Scripting with PowerShell

### Pre-assessment

#### What does the -Online parameter do when you use it with the Get-Help cmdlet?

* Opens the online documentation for the cmdlet

Wrong answers:

* Opens a PowerShell repository of modules and scripts
* Facilitates online collaboration for script development
* Downloads the latest help files from the internet

The **-Online** parameter opens the online documentation for the specific cmdlet in the default web browser.

#### Which symbol is used to declare a variable in PowerShell?

* $

Wrong answers:

* @
* #
* %

The **$** symbol is used to declare variables in PowerShell.

Use **@** for arrays, **#** for comments, and **%** for mathematical operations.

#### What does the -eq operator check for in PowerShell conditional statements?

* Equality

Wrong answers:

* Probability
* Greater than
* Less than or equal to

#### Which method is used to find the number of elements of a PowerShell array? 

* $array.Count

Wrong answers:

* $array.GetCount
* $array.Size
* $array.Total

### Getting Started with PowerShell

#### New-Item cmdlet

```
New-Item -ItemType Directory -Path "C:\Users\Administrator\MyFiles\"
```

#### Creating a new PowerShell script file .ps1

```
New-Item -ItemType File -Path "C:\Users\Administrator\MyFiles\practice.ps1"

```

#### Running a script

```
.\script.ps1
```

### PowerShell help

```
Get-Help <CmdletName>
```

```
Get-Help Get-Process
```

#### -Detailed or -Full parameter

```
Get-Help Get-Process -Detailed
```

#### Search help for a keyword

```
Get-Help -Name Keyword
```

#### -Online parameter to open the online documentation for PowerShell

```
Get-Help Get-Process -Online
```

## PowerShell Fundamentals

### PowerShell variables

PowerShell variable names are not case-sensitive. For instance, the following two variable names refer to the same variable.

```
$myVariable

$MyVariable
```

### Write-Host cmdlet to output text to the console

```
# Variable to store car type
$carType = "SUV"

#Display the car type
Write-Host  "Car Type: $carType"
```

### Arrays

```
# Creating an array of car models
$carModels = "Sedan", "SUV", "Convertible"

#Accessing array elements
 $firstModel = $carModels[0]
Write-Host "First car model: $firstModel"
```

### Hashtables

A hashtable is a collection of key-value pairs that give you the ability to store and retrieve data based on unique keys. You declare them using the **@{}** syntax. For example, you use **$myHashtable = @{ Key = 'Value' }** to create a hashtable with a key named **Key** and a corresponding value **Value**.

```
# Creating a hashtable of car wash prices
$carWashPrices = @{
    "Basic" = 10
    "Premium" = 20
    "Deluxe" = 30
}

# Accessing values using keys
$basicPrice = $carWashPrices["Basic"]
Write-Host "Price for Basic wash: $basicPrice"
```

### Functions

```
function MyFunction {
      # Function body
  }
```

### Passing arguments to function call

In this example, you define a function called **StartCarWash**. The function takes the **$CarType** parameter, which represents the type of car being washed. Next, you display a message that indicates the type of car being washed. Finally, you call the function and provide a value for the **$CarType parameter**. The parameter passed to Write-Host is the string **Washing $CarType**. When you are using **double quotes** to create a string, you can refer to variables right inside the string.  A string created from **single quotes won't substitute** variables.

```
function StartCarWash {
    param (
        [string]$CarType
    )
        Write-Host "Washing $CarType."
    }
StartCarWash -CarType "Sedan"
```

### Loops

#### For loops

```
# Define an array of car types
$cartypes = "sedan", "SUV", "truck", "convertible"
# For loop to wash each car
for ($i = 0; $i -lt $cartypes.Length; $i++) {
    $currentcar = $cartypes[$i]
    Write-Output "Washing $currentcar."
}
```

#### While loop

**While** loops continue iterating as long as a specified condition holds true. This is useful when you don't know the number of iterations in advance.

```
# Example: Wash cars until the water runs out
$waterSupply = 1000  # Assume 1000 gallons of water
while ($waterSupply -gt 0) {
    Write-Output "Washing Car, Water Remaining: $waterSupply gallons"
    $waterSupply -= 50  # Simulate water consumption
}
```

#### Until loops in PowerShell

Until loops in PowerShell

Contrary to some other scripting languages, PowerShell does not have a native **until** loop. However, you can achieve the same effect using the **while** loop by negating the condition.

### Conditional Statements

Conditions are essential for decision-making in scripts. You can control the flow of your script, based on whether certain conditions are met.

#### If statements

```
# Car wash example
$weather = "sunny"
if ($weather -eq "sunny") {
    Write-Host "It's a good day for a car wash!"
}
```

#### If-else statements

```
# Car wash example
$weather = "rainy"
if ($weather -eq "sunny") {
    Write-Host "It's a good day for a car wash!"
} else {
    Write-Host "It's raining. Maybe another day."
}
```

#### Else if

```
# Car wash example
$weather = "cloudy"
if ($weather -eq "sunny") {
    Write-Host "It's a good day for a car wash!"
} elseif ($weather -eq "cloudy") {
    Write-Host "The weather is okay. You can still have a car wash."
} else {
    Write-Host "It's not the best weather for a car wash."
}
```

### Demo: Scripting with PowerShell - create an Amazon S3 bucket and verify its AWS Region

#### Creating a new S3 bucket

```
PS> New-S3Bucket  -BucketName  psdemo123  -Region  us-east-1
```

#### Verifying the Region

You can verify that your new bucket was created in the correct Region by using the **Get-S3BucketLocation** command or through the AWS Management Console.

The following command can be used to view the location of the S3 bucket you've just created:

```
PS> Get-S3BucketLocation  -BucketName  psdemo123
```

#### Creating a key pair

To deploy an EC2 instance, you will need a key pair. For this demo, you will create a new key pair and name it **PSDemoKeyPair**. To create this, begin by creating a PowerShell variable. The variable name will be **$PSDemoKeyPair**, and should match the following:

```
PS> $PSDemoKeyPair = New-EC2KeyPair  -KeyName PSDemoKeyPair
```

#### Viewing the structure of the output object

The object produced by the $PSDemoKeyPair variable can be piped into the Get-Member cmdlet, so you can view the object's structure. The command should appear as follows:

```
PS> $PSDemoKeyPair | Get-Member
```

#### Viewing key values

You can also view key values like KeyName, KeyFingerprint, and KeyMaterial by piping the **$PSDemoKeyPair** variable into the **Format-List** cmdlet.

In the attached example, you can see the output of the following command:

```
PS> $PSDemoKeyPair | Format-List KeyName, KeyFingerprint, KeyMaterial
```

This command line is telling PowerShell to list the KeyName, KeyFingerprint, and KeyMaterial objects that are output by piping the **$PSDemoKeyPair** variable into the Format-List cmdlet.

#### Storing the private key

Now that you have generated a private key to use with your EC2 instance, you will need to store it. To store your private key to a file, pipe the **KeyMaterial** member of the **$PSDemoKeyPair** to the **Out-File** cmdlet. You can accomplish this by appending the **$PSDemoKeyPair** variable as follows:

```
PS> $PSDemoKeyPair.KeyMaterial | Out-File -Encoding ascii PSDemoKeyPair.pem
```

The output of this variable is then piped into the **Out-File** cmdlet. You are also telling PowerShell to encode the output file using **-Encoding ascii**, in addition to assigning the **PSDemoKeyPair.pem** file name.

#### Creating a security group for your EC2 instance

Now that you have created a key pair to use with your EC2 instance, you will create a security group for your EC2 VPC. This is accomplished using the **New-EC2SecurityGroup** cmdlet. You can capture this process in a new variable labeled **$groupid**.

```
PS> $groupid = New-EC2SecurityGroup `
-VpcId "vpc-da0025a4xxxxxxxxx" `
-GroupName "PSDemoSecurityGroup" `
-GroupDescription "EC2-VPC from PowerShell" 
```

As shown in the table, you will use the **New-EC2SecurityGroup** cmdlet, specify the VpcId, assign a group name, and provide a group description.

**Note:** to retrieve the VPC ID that you are working with, enter the **Get-EC2Vpc** cmdlet. Copy the VPC ID to your clipboard or to a separate document.

#### Verifying your security group creation

Now that you have created your security group, verify that it was created successfully. Using the **Get-EC2SecurityGroup** cmdlet, you can view all the security groups in your account. This is where the description you previously entered is helpful, as it assists you in locating the new security group in what can be a long list of existing groups.

#### Finding an AMI using PowerShell

You have created a key pair and a security group; now it's time to pick the AMI. Select an Amazon Linux 2023 image to deploy.

By using the **Get-SSMLatestEC2Image** cmdlet and specifying the parameter **-Path ami-amazon-linux-latest**, you can retrieve the entire list of EC2 AMIs available. Select the image ID you want to deploy and copy it to your clipboard or another file.

#### Launching an EC2 instance in a VPC

Using the **New-EC2Instance cmdlet**, you can specify a number of parameters to successfully launch an instance. The commands contained in the following snippet will launch a single **t2-micro** instance in the specified private subnet using an Amazon Linux 2023 AMI.

```
PS> New-EC2Instance `    
-ImageId ami-0a3c3a20c09d6f377 `    
-MinCount 1 -MaxCount 1 `    
-KeyName PSDemoKeyPair `    
-SecurityGroupId sg-xxxxxxxx `    
-InstanceType t2.micro `    
-SubnetId subnet-xxxxxxxx
```

After running the command, the instance will move into a state of pending, but should transition to a running state shortly thereafter. You can view the details of your instance using the **Get-EC2Instance** cmdlet.

#### Cleaning up

#### Removing your S3 bucket

If you had any files in your S3 bucket, you would need to run the **Remove-S3Object** cmdlet to delete each object. As such, your bucket should still be empty for this demo, so you can run the **Remove-S3Bucket** cmdlet with the **-BucketName** parameter. The command to accomplish this task is as follows:

```
PS> Remove-S3Bucket -BucketName psdemo123
```

#### Removing your private key pair and security group

The private key pair can be removed using the **Remove-EC2KeyPair** cmdlet. The following command will accomplish this task:

```
PS> Remove-EC2KeyPair -KeyName PSDemoKeyPair
```

The security group can be removed using the following command:

```
PS> Remove-EC2SecurityGroup -GroupName myPSSecurityGroup
```

You can verify that the security group has successfully been removed by running the **Get-EC2SecurityGroup** cmdlet.

#### Removing your EC2 instance

To remove the EC2 instance, use the **Remove-EC2Instance** command. This command, paired with the **-InstanceId** parameter, will terminate and remove the targeted EC2 instance.

```
PS> Remove-EC2Instance -InstanceId i-xxxxxxxxxx
```
### [Lab: Using the AWS Tools for Windows PowerShell to Automate Windows](./W08Lab02-AWSToolsToAutomateWindows.md)

### Knowledge Check

#### Which parameter is used to access detailed help information for a PowerShell cmdlet?

* -Detailed

Wrong answers:

* -Info
* -Help
* -Description

**-Detailed** parameter extended details about a cmdlet, including parameter descriptions and examples.

#### What is the purpose of a PowerShell variable?

* To store and retrieve data

Wrong answers:

* To create loops
* To comment on code
* To perform mathematical calculations

Creating loops is the purpose of constructs like for, not variables. Comments provide documentation in code. Mathematical calculations are performed using operations, not variables.

#### Which loop structure is used when PowerShell repeats a block of code, as long as a specified condition is true?

* while

Wrong answers:

* for
* until
* if

A **while** loop is used to repeat a block of code, as long as a specified condition is true. 

A **for** loop is used for a specified number of iterations, and an **if** loop is used for conditional statements. PowerShell does not have a native **until** loop.

#### Which conditional statement is used to test multiple conditions in a sequence?

* elseif

Wrong answers:

* if/then
* if/else
* while

The **if/then** conditional statement is a basic conditional statement for a single condition. The **if/else** conditional statement handles two conditions, but does not test multiple conditions sequentially. A **while** loop is a loop construct, not a sequential conditional statement.

### Summary

#### Creating PowerShell scripts

* How to use the **New-Item** cmdlet to create files, directories and other items.
* How to run a script using the .\ prefix followed by the script name.
* How to get basic help for a cmdlet using the **Get-Help** cmdlet. For more detailed information, use the **-Detailed** or **-Full** parameter.
* How to search for cmdlets related to a specific keyword using the **-Name** parameter.
* How to use **-Online** to open the online documentation (if you have an internet connection).

#### PowerShell fundamentals

Bash and PowerShell share several fundamental elements to help you manage and manipulate data effectively. To learn more, expand each of the following seven categories.

##### Variables

PowerShell variables serve as containers for storing and manipulating data within scripts and commands. To declare a variable, use $ followed by a name, such as **$myVariable**. Variables can store various types of data, including strings, integers, arrays, and much more. PowerShell variable names are not case-sensitive.

##### Arrays

An array is a collection of values you store in a single variable. Each value in an array is assigned an index, starting from zero.

##### Hashtables

A hashtable is a collection of key-value pairs. You can store and retrieve data based on unique keys. You declare them using the **@{}** syntax. For example, you use **$myHashtable = @{ Key = 'Value' }** to create a hashtable with a key named **Key** and a corresponding value **Value**.

##### Functions

You can use functions to encapsulate a set of instructions into a reusable block of code. In PowerShell, you define functions using the **function** keyword followed by the function name and a pair of curly braces that enclose the function body.

##### Loops

The **for** loop in PowerShell is similar to its counterparts in other languages. With **for** loops, you can iterate a specific number of times, and you can use it when the number of iterations is known beforehand.

**While** loops, on the other hand, continue iterating as long as a specified condition holds true. This is useful when you don't know the number of iterations in advance.

##### Conditionals

Conditionals are essential for decision-making in scripts. You can control the flow of your script based on whether certain conditions are met. The if statement is the most basic form of a conditional statement. You can run a block of code if a specified condition is true. 

The **if-else** statement extends the **if** statement by providing an alternative block of code to run when the condition is false.

With the **else if** statement, you can test multiple conditions in a sequence. If the first condition is false, it moves on to the next condition, and so on.

## Error Handling and Troubleshooting with PowerShell

### Pre-assessment

#### What does PowerShell do when an error occurs if $ErrorActionPreference is set to SilentlyContinue?

* It silently continues running the script.

Wrong answers:

* It displays error messages.
* It stops the script.
* It pauses the script and prints an error message.

When set to SilentlyContinue, PowerShell continues running the script without displaying error messages.

SilentlyContinue does not display error messages, stop the script, or pause the script and print an error message.

#### What is the primary purpose of the finally block?

* To specify code that will always run

Wrong answers:

* To create conditional statements
* To handle errors
* To call variables

You use the finally block to specify code that will always run, whether an error occurs or not. 

#### Which construct is commonly used for implementing retry logic?

* try and catch blocks

Wrong answers:

* If statements
* until loops
* while loops

You often implement retry logic using try and catch blocks to catch and handle exceptions that might occur while running script.

If statements alone are not sufficient for implementing retry logic. until and while loops are not designed for implementing retry logic.

### Error Handling in PowerShell

PowerShell uses exit codes to indicate the success or failure of a command or script. Exit codes are integer values returned by commands. An exit code of '0' indicates success, while a non-zero value indicates an error or failure.

### Conditional execution

In PowerShell, $? provides an effective way to check if a command ran successfully or encountered an error. $? is crucial for error handling and conditional execution of commands based on the success or failure of preceding commands. In the following example, you use $? to check for errors and write output messages indicating command success or failure.

```
Get-Content "NonexistentFile.txt"

if ($?) {
    Write-Host "Command succeeded."
} else {
    Write-Host "Command failed."
}
```

### Controlling scripts response to errors

**$ErrorActionPreference** is a variable that determines how PowerShell responds to non-terminating errors. You can control the behavior of error handling within your scripts. The value of **$ErrorActionPreference** can be set to different preferences, influencing whether errors are silently ignored, displayed, or treated as terminating errors. The values you can use for **$ErrorActionPreference** include the following:

* **Stop** makes all errors terminating. If an error occurs, PowerShell will stop running the script or command.
* **Continue** makes non-terminating errors visible, but the script continues to run. This is the default value of **$ErrorActionPreference**.
* **SilentlyContinue** suppresses non-terminating errors. The errors are not displayed, and the script continues running.
* **Inquire** prompts the user for action on each non-terminating error.

The following example sets **$ErrorActionPreference** to **Inquire** to prompt the user for action on errors.

```
$ErrorActionPreference = 'Inquire'
# Command that may fail
Get-Content "NonexistentFile.txt"
# Check if the last command succeeded using $?
if ($?) {
    Write-Host "Command succeeded."
} else {
    Write-Host "Command failed."
}
```

### Exception Handling Statements

In PowerShell, error handling usually involves the use of **try**, **catch**, **finally**, and **exit** statements.

* **try** blocks encapsulate code prone to errors.
* **catch** blocks manage error responses.
* **finally** runs code whether an exception occurs in the try block.
* **exit** stops the script with a specific exit code upon encountering an issue.

### Try and catch

The **try** and **catch** blocks are fundamental techniques for gracefully handling exceptions in PowerShell scripts. These blocks allow encapsulation of code that might generate errors, enabling the script to respond to unexpected issues. Syntax usually includes a **try** block containing code that might cause an error, and a **catch** block that specifies the code to run if an error occurs. The **catch** block only runs if there's a terminating error. If the **try** block runs correctly, it skips over the catch.

```
try {
   # Code that may generate error
}
catch {
   # Code to handle the error
}
```

In the following example, the try block attempts to perform a division by zero, causing an error. The catch block catches the error and displays a custom error message along with the actual error message using the $_ variable. The $_ variable represents the current exception object.

```
try {
    $result = 10 / 0 # This division by zero will cause an error
    Write-Host "Result: $result"
}
catch {
   Write-Host "An error occurred: $_"
}
```

### Finally

You use the **finally** block to specify code that runs regardless of whether an exception happened in the **try** block. You often use **finally** for cleanup operations or tasks that need to run regardless of the error status. The **finally** block is optional. Following is an overview of the syntax of using a **finally** block.

```
try {
   # Code that may generate an error
}
catch {
   # Code to handle the error
}
finally {
   # Code that always runs
}
```

The following example demonstrates how to handle errors gracefully using **try**, **catch**, and **finally**.

In this script, a **try** block intentionally generates an error by dividing 10 by 0. This causes the **catch** block to run, which displays an error message indicating that an error has occurred. Finally, the **finally** block always runs, regardless of whether an error occurred, and displays a message to indicate that the code has finished running.

```
try {
  # Intentionally induce an error by dividing by zero
  $result = 10 / 0
  Write-Host "Result: $result"
}
catch {
  # Handle the error
  Write-Host "An error occurred: $_"
}
finally {
  # Code that always runs, for cleanup or logging
  Write-Host "Finally block: This always runs, even after an error or exit."
}
```

### Exit

The **exit** command can be used within **try/catch** or **try/catch/finally** statements to explicitly terminate the execution of a script when an exception occurs, based on a specific exit code. Typically, exit codes will be placed within the **catch** block; however, if you need to perform cleanup before exiting, it is a good practice to move the exit command to the finally block to ensure that the cleanup code executes, regardless of whether an exception occurred.

```
try {
   # Code that may generate an error
}
catch {
   # Exit with an error exit code
    exit 1
}
```

The previous example shows how to insert an **exit** command within a **catch** block, along with an **exit** code of 1, which will signal a general error or exception.

**Exit** codes are numerical values that indicate the success or failure of a script. **Exit** code 0 signals successful execution, **exit** code 1 is used to signal general errors, and any **exit** code greater than 1 can represent specific error conditions defined by the developer or application.

### Retries and Backoff

### Retries

A retry is the process of re-attempting an operation multiple times to increase the chances of success when transient errors occur.

In the following example, you intentionally cause an error. The **while** loop is set to retry the operation up to a maximum of **$MaxAttempts** times. Inside the **try** block, you attempt an operation. If successful, the **break** statement exits the loop immediately. If the operation fails, the **catch** block runs, logging the error and initiating a delay. The loop continues until the maximum number of attempts is reached or the operation is successful.

```
$MaxAttempts = 3
$Attempt = 1

while ($Attempt -le $MaxAttempts) {
    try {
        # Attempt a connection to the application server
        $result = Invoke-RestMethod https://localhost:8088/info
        break  # Exit the loop if the operation is successful
    }
    catch {
        Write-Host "Attempt $Attempt failed: $_"
        $Attempt++
        Start-Sleep -Seconds 2  # Add a delay before the next attempt
    }
}
if ($Attempt -gt $MaxAttempts) {
    Write-Host "Operation failed after $MaxAttempts attempts."
}
```

#### Using the break statement

You use the **break** statement to end a loop prematurely, causing a script to jump out of a loop and continue with the next line of code after the loop. In the previous example, if the operation in the try block is successful, the **break** statement is run, causing an immediate exit from the loop.

### Exponential backoff

Exponential backoff is a strategy that introduces increasing delays between successive retry attempts to reduce the load on systems during periods of high demand.

In this example, you include an initial delay and exponential backoff. After each failed attempt, the **catch** block introduces an increasing delay before the next attempt, providing a more gradual approach to retries.

```
$MaxAttempts = 3
$Attempt = 1

while ($Attempt -le $MaxAttempts) {
    try {
        # Attempt a connection to the application server
        $result = Invoke-RestMethod https://localhost:8088/info
        break  # Exit the loop if the operation is successful
    }
    catch {
        Write-Host "Attempt $Attempt failed: $_"
        $Attempt++
        Start-Sleep -Seconds (2 * $Attempt)  # Exponential backoff
    }
}
if ($Attempt -gt $MaxAttempts) {
    Write-Host "Operation failed after $MaxAttempts attempts."
}
```

### Logging

### Logging to stdout and stderr

In PowerShell, you can use the different streams **stdout** (standard output) and **stderr** (standard error) to handle regular output and error messages. These streams give you the ability to direct different kinds of messages to different locations. You can then organize and handle different types of messages appropriately, whether for user feedback, logging, or error management.

The following example redirects **stdout** and **stderr** messages to separate log files:

* The **Write-Output** cmdlet logs a standard message to a file called **stdout_log.txt**.
* The **Write-Error** cmdlet writes an error message to a file named **stderr_log.txt**.
* For the last two lines of code, the pipeline operator | takes the output from the left command and uses it for input for the command on the right.
* You use the **Out-File** command to append output to a file. You use the **-Append** parameter to append the message to the existing contents of the log file instead of overwriting it.
* Note the use of the redirection operator **2>&1** to redirect the standard error to the same location as the standard output.

```
$stdoutLog = "stdout_log.txt"
$stderrLog = "stderr_log.txt"
Write-Output "This is a standard output message." | Out-File -Append $stdoutLog
Write-Error "This is an error message." 2>&1 | Out-File -Append $stderrLog
```

### Logging functions

Custom logging functions can enhance the maintainability and extensibility of your scripts. With custom logging, you can control where log messages are directed, the format of those messages, and any additional actions you'd like to take when logging events. The following is an example of a basic logging function that writes messages to a log file.

In this example, you define a **Write-Log** function that takes a message, a log file path, and a log level as parameters. You construct a log entry with a timestamp, log level, and log message. Finally, the script demonstrates the use of the **Write-Log** function with different log messages and levels.

```
function Write-Log {
    param(
        [string]$Message,
        [string]$LogFile = "script_log.txt",
        [string]$LogLevel = "INFO"
    )
    $Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $LogEntry = "[$Timestamp] [$LogLevel] $Message"
    # Output to stdout
    Write-Output $LogEntry
    # Output to log file
    Add-Content -Path $LogFile -Value $LogEntry
}
# Example Usage:
Write-Log -Message "Script started."
Write-Log -Message "Processing data." -LogLevel "DEBUG"
Write-Log -Message "An error occurred!" -LogLevel "ERROR"
Write-Log -Message "Script completed."
```

#### Logging levels

Common levels on PowerShell include **INFO**, **WARNING**, **ERROR**, and **DEBUG**. Adjusting the logging level can control the verbosity of the logs.

### Log rotation

You use log rotation to manage log files by limiting their size or quantity. Using log rotation ensures efficient use of storage space and makes it more convenient to analyze and maintain logs. In PowerShell, you can implement log rotation using a custom function that checks the size of a log file and rotates it when it reaches a specific threshold. The following is an example of a basic log rotation function. In this example, the script checks for the size of the current log file and rotates it if it exceeds the specified size.

```
$LogFilePath = "script_log.txt"
$MaxLogSizeMB = 1
if ((Get-Item $LogFilePath).length -gt ($MaxLogSizeMB * 1KB)) {
    $TimeSeconds = [int64](Get-Date -UFormat %s)
    Rename-Item $LogFilePath -NewName "script_log_$TimeSeconds.txt"
    Write-Output "Log rotated." $LogFilePath
}
```

### Centralized logging

Centralized logging involves aggregating log data from multiple sources into a central repository or service. This streamlines log analysis, monitoring, and troubleshooting, especially in environments with multiple servers or distributed systems. Some solutions that centralize log management include Amazon CloudWatch, Splunk, and many more.

Following is a basic example of logging to a remote server using the System Logging Protocol (syslog). Syslog is a protocol that allows computer systems to send logs to a central location.

```
$syslogserver = "syslog.example.com"
$syslogport = 514
$syslogmessage = "Log message to be sent to syslog server"
Write-Host $syslogmessage | Send-Udpmessage -RemoteAddress $syslogserver -RemotePort $syslogport
```

### [Lab: Troubleshooting the AWS Tools for Windows PowerShell in Windows Environments](./W08Lab03-TroubleshootingAWSTools.md)

### Knowledge Check

#### What is the default value of $ErrorActionPreference?

* Continue

Wrong answers:

* Stop
* Inquire
* Ignore

The default value of **$ErrorActionPreference** is Continue, which means PowerShell continues running the script on error.

#### What is the purpose of the try block?

* To specify code that might generate an error

Wrong answers:

* To define a block of code that will always run
* To run code after an error occurs
* To create a loop

#### How can exponential backoff be implemented in PowerShell?

* By using a random delay between retries

Wrong answers:

* By using a fixed delay between retries
* By always retrying automatically between retries
* By not using any delay between retries

Exponential backoff uses a random, increasing delay between retries exponentially to avoid overwhelming a system that might be experiencing issues. 

### Summary

#### Conditional execution

* $? provides an effective way to check if a command ran successfully or encountered an error. $? is crucial for error handling and conditional execution of commands based on the success or failure of preceding commands.
* **$ErrorActionPreference** is a variable that determines how PowerShell responds to non-terminating errors. You can control the behavior of error handling within your scripts. The value of **$ErrorActionPreference** can be set to different preferences, influencing whether errors are silently ignored, displayed, or treated as terminating errors.

#### Try, catch, and finally

In PowerShell, error handling usually involves the use of **try**, **catch**, **finally**, and **exit** statements.

* **try** blocks encapsulate code prone to errors.
* **catch** blocks manage error responses.
* **finally** runs code whether an exception occurs in the try block.
* **exit** terminates the script with a specific exit code upon encountering an issue.

#### Retries and backoff

A **retry** is the process of re-attempting an operation multiple times to increase the chances of success when transient errors occur.

**Exponential backoff** is a strategy that introduces increasing delays between successive retry attempts to reduce the load on systems during periods of high demand.

#### Logging to stdout and stderr

You can use the different streams **stdout** (standard output) and **stderr** (standard error) to handle regular output and error messages. Using these streams, you can direct different kinds of messages to different locations. You can organize and handle different types of messages appropriately, whether for user feedback, logging, or error management.
