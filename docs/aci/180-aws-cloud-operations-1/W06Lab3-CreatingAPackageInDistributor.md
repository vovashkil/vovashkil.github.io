# Creating a Package in Distributor, a Capability of AWS Systems Manager

## Lab Overview

In this lab, you use Distributor, a capability of AWS Systems Manager, to create the Amazon CloudWatch agent custom package. And you use Run Command, also a capability of AWS Systems Manager, to install this package.

Objectives
By the end of this lab, you will be able to do the following:

Use Distributor to create a custom package.
Use Run Command to install the custom package.
Duration
This lab requires 30 minutes to complete.

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
The following diagram shows the basic architecture of the lab environment:

'Architecture diagram'

Image description: The preceding diagram depicts the flow from Systems Manager Distributor to instances in a public subnet.

Services used in this lab
AWS Systems Manager Overview
AWS Systems Manager is a powerful unified interface from AWS that provides you with the ability to centrally manage your AWS resources.

Distributor, a capability of AWS Systems Manager, helps you package and publish software to AWS Systems Manager managed nodes.

Task 1: Create custom package using Distributor
In this task, you create custom package which installs AWS CloudWatch agent using Distributor.

In a production environment you may want to consider using the Amazon owned AmazonCloudWatchAgent package. Amazon owned packages are maintained and updated by Amazon. The CloudWatch agent is used as a simple example to learn the process that can be used for any package.

Choose the following link and download the cloudwatch agent file to your computer: AWS Cloudwatch Agent

 Additional information: This will download the AWS CloudWatch agent RPM package for Amazon Linux on x86 64bit processors. An RPM file contains everything needed to install an application using the yum package manager on your instances.

At the top of the AWS Management Console, in the search bar, search for and choose Systems Manager. This redirects you to the Amazon Systems Manager service page where you see detailed information about the service.

In the navigation pane, choose Distributor preceding Node Management section.

Choose Create package . This redirects you to the Create package page.

Configure the following options:

For title of the box, keep the Simple radio button selected

For details, in the Name box, enter: cloudwatchagent

For the location section, keep the Choose a bucket name from a list radio button selected.

In the S3 bucket name dropdown, choose the bucket name with cloudwatch from the dropdown menu.

 Note: This is the S3 bucket where you store the cloudwatch agent package.

For S3 key prefix, enter cloudwatchagent

In the Upload software section, choose Add software and upload the cloudwatch agent file you downloaded at the start of this task.

For Target platform, choose amazon from the dropdown list.

For Architecture, choose x86_64 from the dropdown list.

 Note: If you expand Scripts you can see that distributor has already provided the appropriate installation script. Observe that the install script uses the yum package manager with a reference to the file you just added.

 Note: If you expand Manifest you will see the mapping of target platform (amazon in this lab), platform version, and architecture (x86_64 in this lab) to the zip file you uploaded. If you had requirements to also install on an Ubuntu platform you would be able to upload a zip file for Ubuntu, and reference this file in a ubuntu key in the packages.

Choose Create package

 Expected output A pop up window appears and after a few minutes a success message saying that the upload is complete.

You are now re-directed to the cloudwatchagent package details page. Please wait until the Status of the package is changed to Active.
 Task complete: You have successfully created custom package for cloudwatch agent using Distributor.

Task 2: Install custom package using Run Command
Now that you have your custom package uploaded to your S3 bucket along with the manifest. Distributor gives you 2 quick options to deploy your package. You can either install on a schedule or install one time. Installing on a schedule automatically prepares a State Manager Association with the pre-defined Document of AWS-ConfigureAWSPackage and the name of your custom package as a parameter. Install one time does the same preparation but uses Run Command.

In this task, you install the cloudwatch agent package using the Install one time option which uses Run Command.

In the navigation pane, choose Distributor preceding Node Management section.

Choose Owned by me tab.

Select the radio button next to cloudwatchagent.

Choose Install one time . This will pre-populate the Run Command with all of the necessary configuration items to run against the instances you choose.

 Note: Run Command uses the Amazon Managed command document - AWS-ConfigureAWSPackage to run the package you created.

In the Target selection section, select Choose instances manually

 Note: In complex production environments with thousands of instances, the recommended approach would be to select targets by Specifying a tag. In this approach, you give the same tag name for each resource, and SSM systematically applies the configuration for every resource identified by that tag.

Select the two instances with name Test-Instance that will get the new Distributor package applied.

In the Output options section, clear the Enable an S3 bucket box.

Keep everything else as default and choose Run . You are now redirected to the to the Run Command progress for the distributor package deployment.

Choose Refresh  button, until the Command status section shows Overall status as Success.

Under Targets and Outputs section, select the radio button next to any instance ID.

Select View Output

In Step 2 - Command description and status section, expand the Output section.

Scroll to the bottom of the output log and you can see the successfully installed message as follows:

 Expected output


Installed:

amazon-cloudwatch-agent-1.300028.4b233-1.x86_64

Complete!

Successfully installed cloudwatchagent Auto-Generated-1700679952331
 Task complete: You have successfully configured a Distributor package with custom software, used Run Command to deploy the package to a Managed Instance.

Conclusion
You successfully done the following:

Created custom package using Distributor.
Installed custom package using Run Command.
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End lab and then confirm that you want to end your lab.

Additional Resources
For more information about AWS Systems Manager Distributor, see AWS Systems Manager Distributor
For more information about AWS Systems Manager Run Command, see AWS Systems Manager Run Command