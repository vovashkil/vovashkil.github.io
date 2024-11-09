# Creating AWS Systems Manager Parameters

## Lab Overview

This lab creates two parameters in Parameter Store, a capability of AWS Systems Manager and use these parameters to create an EC2 instance through AWS CloudFormation.

Objectives
By the end of this lab, you will be able to do the following:

Create parameters in Parameter Store.
Create a CloudFormation stack using parameters in Parameter Store.
Duration
This lab requires 60 minutes to complete.

Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Expected output: A sample output that you can use to verify the output of a command or edited file.
 Note: A hint, tip, or important guidance.
Start lab
To launch the lab, at the top of the page, choose Start lab.
 You must wait for the provisioned AWS services to be ready before you can continue.

To open the lab, choose Open Console.
You are automatically signed in to the AWS Management Console in a new web browser tab.

 Do not change the Region unless instructed.

Common sign-in errors
Error: You must first sign out


If you see the message, You must first log out before logging into a different AWS account:

Choose the click here link.
Close your Amazon Web Services Sign In web browser tab and return to your initial lab page.
Choose Open Console again.
Error: Choosing Start Lab has no effect
In some cases, certain pop-up or script blocker web browser extensions might prevent the Start Lab button from working as intended. If you experience an issue starting the lab:

Add the lab domain name to your pop-up or script blocker’s allow list or turn it off.
Refresh the page and try again.
Lab environment
A CloudFormation template which creates an EC2 instance has been provided for you.

Services used in this lab
AWS Systems Manager Overview
AWS Systems Manager is a powerful unified interface from AWS that provides you with the ability to centrally manage your AWS resources.

Parameter Store, a capability of AWS Systems Manager, provides secure, hierarchical storage for configuration data management and secrets management. You can store data such as passwords, database strings, Amazon Machine Image (AMI) IDs, and license codes as parameter values. You can store values as plain text or encrypted data. You can reference Systems Manager parameters in your scripts, commands, SSM documents, and configuration and automation workflows by using the unique name that you specified when you created the parameter.

Task 1: Create Parameters in Systems Manager Parameter Store
In this task, you store the custom values for instance-type and ami-id in the parameter store.

At the top of the AWS Management Console, in the search bar, search for and choose Systems Manager. This redirects you to the Amazon Systems Manager service page where you see detailed information about the service.

In the navigation pane on left, select Parameter Store under the Application Management section.

Choose Create parameter. This redirects you to the Create parameter page.

Configure the following options to store instance type as a parameter value. Leave any items not mentioned at their default setting:

For Name, Enter /ec2/instance-type
For Type, Select string
For Data type, Select text
For Value, Enter t3.micro
Choose Create parameter

 Expected output This message is displayed at the top of the screen Create parameter request succeeded!

On the same page, choose Create parameter again. This redirects you to the Create parameter page.

Configure the following options to store AMI ID as a parameter value. Leave any items not mentioned at their default setting:

For Name, Enter /ec2/ami-id
For Type, Select string
For Data type, Select aws:ec2:image
For Value, Enter ami-0f3769c8d8429942f
Choose Create parameter

 Expected output This message is displayed at the top of the screen Your parameter is being created. We are validating the parameter value against the data type. The parameter might not be available right away. Check your notifications in Amazon CloudWatch for information about any failures.

 Note: The above message indicates that it takes couple of minutes for the parameter to be created.

 Task complete: You have successfully stored custom values for instance-type and ami-id in the parameter store.

Task 2: Create a CloudFormation stack using parameters in Parameter Store
In this task, you deploy an AWS CloudFormation template that creates a EC2 instance using Systems Manager parameters.

Choose the following link and download the template to your computer: lab-ec2.yaml

Open the above downloaded file in a text editor.

 Expected output:


Parameters:
  InstanceType:
    Type: 'AWS::SSM::Parameter::Value<String>'
    Default: /ec2/instance-type

  ImageId: 
    Type: 'AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>'
    Default: /ec2/ami-id

Resources:
  InstanceWithParameters:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: !Ref ImageId
      InstanceType: !Ref InstanceType
      Tags:
        - Key: Name
          Value: Test-Instance
 Note: The above template has two parameters InstanceType and ImageId. Cloudformation retrieves the two from the Parameter Store.

At the top of the AWS Management Console, in the search bar, search for and choose CloudFormation.
 Expected output: You will be redirected to the CloudFormation stacks service page where you see detailed information about the service.

Choose Create stack, choose With new resources (standard) and configure the following:

Create stack

Select  Template is ready
Select  Upload a template file
Choose Choose file and select the lab-ec2.yaml file you downloaded
Choose Next
Specify stack details

Stack name: lab-ec2

Parameters: The two parameter values ImageId and InstanceType have been defined in the template and hence are automatically populated in this section. After completion of the stack, it will launch an EC2 instance with instance type t3.micro and AMI type of Amazon Linux 2023, which you defined in the Parameter Store earlier in Task 1.

Choose Next

Configure stack options

Choose Next
Review lab-ec2

Choose Submit
AWS CloudFormation now uses the template to generate a stack of resources.

In the Events tab, wait for the Status to change to  CREATE_COMPLETE.
 Note: Choose the refresh  icon every 15 seconds to update the display if necessary.

Now, examine the resources that were created.

Choose the Resources tab.
You see a EC2 instance created by the template.

 Note: If the list is empty, choose the refresh  icon to update the list.

Choose Physical ID link. This opens a new tab which shows the EC2 instance details.

Select  Test-Instance

In the Details tab, scroll down to observe that the Instance type is set to t3.micro. Scrolling down further, you can also observe that the AMI ID is set to ami-0f3769c8d8429942f.

 Note: These are the same values which you stored in Parameter Store.

 Task complete: You have successfully deployed an AWS CloudFormation template that creates a EC2 instance using Systems Manager Parameters.

Conclusion
You successfully done the following:

Created default values in Parameter Store.
Created CloudFormation Stack using Systems Manager Parameter template.
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End lab and then confirm that you want to end your lab.

Additional Resources
For more information about AWS Systems Manager Parameter store, see AWS Systems Manager Parameter store.
For more information about AWS CloudFormation Parameters, see AWS CloudFormation Parameters.