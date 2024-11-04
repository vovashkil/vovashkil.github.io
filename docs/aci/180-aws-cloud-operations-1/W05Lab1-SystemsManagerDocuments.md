# Introduction to AWS Systems Manager Documents

## Lab Overview

This lab demonstrates the use of Run Command, a capability of AWS Systems Manager. You also practice configuring a Command document.

Objectives
By the end of this lab, you will be able to do the following:

Review and modify an existing Systems Manager document.
Create your own Systems Manager document and use Run Command to run commands on a managed Amazon Elastic Compute Cloud (Amazon EC2) instance.
Duration
This lab requires 60 minutes to complete.

Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Expected output: A sample output that you can use to verify the output of a command or edited file.
 Additional information: Where to find more information.
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
An Amazon EC2 instance has been provisioned for use in this lab.

'Architecture diagram'

Image description: The preceding diagram depicts the flow from Systems Manager documents to a Webserver in a public subnet.

Services used in this lab
AWS Systems Manager Overview
AWS Systems Manager is a powerful unified interface from AWS that provides you with the ability to centrally manage your AWS resources. Core to leveraging AWS Systems Manager is the use of AWS Systems Manager documents.

An AWS Systems Manager document (SSM document) allows you to define what actions you want Systems Manager to perform on your AWS resources. Systems Manager includes many pre-configured documents that you can use by specifying parameters at runtime. Documents are written in JavaScript Object Notation (JSON) or YAML, and include steps and parameters that you define as needed.

Task 1: Reviewing and modifying an existing Systems Manager document
In this task, you review and modify an existing Systems Manager Document.

At the top of the AWS Management Console, in the search bar, search for and choose Systems Manager.
 Expected output: You will be redirected to the Amazon Systems Manager service page where you see detailed information about the service.

In the navigation pane on left, select Documents under the Shared Resources section.

Inside here you will be able to see all documents available to your account for the given AWS Region. There are five different tabs:

Owned by Amazon: Managed Documents published and maintained by AWS.
Owned by me: Custom Documents your organization has created.
Shared with me: Documents that you have been granted access to for the given AWS Region.
Favorites new: Documents that you want to add as favorite, by selecting the star icon next to the name of documents.
All documents: Display all documents available to your account for the given AWS Region.
Choose Owned by me tab, to review and modify an existing document.

Select SSM-Lab to see more detailed information about this document.

Choose Content tab to view the contents of this document.

The document content has been pre-created for you. As you can observe in the content, the runCommand section is currently creating a directory named lab. In this next step, you modify the document by creating a new version of it.
Choose Actions and select Create new version. This redirects you to create new version page.

On this page, go to the content section and replace the content with the following code block:


---
schemaVersion: "2.2"
description: "Command Document Example YAML Template"
parameters:
  Message:
    default: ""
    description: "Creating directory"
    type: "String"
mainSteps:
- inputs:
    runCommand:
    - "echo {{Message}}"
    - "mkdir /lab"
    - "touch /lab/ssm.txt"
  name: "create_directory"
  action: "aws:runShellScript"
In the above version, you are adding an extra command which creates a basic ssm.txt file in the /lab directory.
Choose Create new version
 Expected output This message is displayed at the top of the screen Update document request succeeded

 Task complete: You have successfully reviewed and modified an existing Systems Manager Document.

Task 2: Creating your own Systems Manager document
In this task, you create your own Systems Manager document which installs a basic web server and configures a hello world webpage on an EC2 instance.

Task 2.1: Creating Systems Manager document
After the previous step, you should be on the Documents page.

Choose Create document

From the drop-down options, choose Command or session. This redirects you to the Create document page.

Configure the following options. Leave any items not mentioned at their default setting:

For Name, Enter install-app

For Target type - optional, leave the value blank for now. Target Type allows you to restrict the types of resources the document can run against.

For Document type - optional, leave Command document as we will use Run command to install the package.

For Content, choose YAML and then replace the content with the following code block:


---
schemaVersion: '2.2'
description: Command Document Example Template
parameters:
  Message:
    type: String
    description: Message to be displayed
    default: ''
mainSteps:
- action: aws:runShellScript
  name: prepare_web_instance
  inputs:
    runCommand:
      - |
        sudo yum install httpd -y
        cat <<EOF > /var/www/html/index.html
        <!DOCTYPE html>
        <html>
          <head>
            <title>Web Server</title>
          </head>
          <body>
            <p>Hello World!!! {{Message}}</p>
          </body>
        </html>
        EOF
        systemctl start httpd
Choose Create document to save the document.
 Expected output This message is displayed at the top of the screen Your document was successfully created

Task 2.2: Run Systems Manager Document on an EC2 Instance
After the previous step, you should be on the Documents page.

Choose Owned by me tab. Here you can find the install-app document created in earlier task.

Select install-app to see more detailed information about this document.

To run this document, Choose Run command

This redirects you to a Systems Manager Run Command page in a new browser tab.
 Additional information: Using Run Command, a capability of AWS Systems Manager, you can remotely and securely manage the configuration of your managed nodes.

In the Target selection section, select Choose instances manually

Under Instances, select the Command Host EC2 instance

In the output options, clear Enable an S3 bucket box.

Leave the rest options as default, scroll down to bottom of page and choose Run

You are now directed to Command ID page, choose Refresh  button, until the Command status section shows Overall status as Success

This indicates that the SSM document was run successfully on the targeted EC2 instance.
To test whether the SSM document was run successfully on the targeted EC2 instance, copy and paste the WebServerEndpoint value from the list to the left of these instructions into a new browser tab.
 Expected output:

'Web Server Page

 Task complete: You have successfully created a new Systems Manager document and performed Run Command on an EC2 instance.

Conclusion
You successfully done the following:

Reviewed and modified an existing Systems Manager document.
Created your own Systems Manager document and used Run Command to run commands on a managed EC2 instance.
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End lab and then confirm that you want to end your lab.

Additional Resources
For more information about AWS Systems Manager Documents, see AWS Systems Manager Documents.
For more information about AWS Systems Manager Run Command, see AWS Systems Manager Run Command.