# Auditing Your AWS Resources with AWS Systems Manager and AWS Config

## Lab overview

In this lab, you set up processes for AWS Config and Inventory, a capability of AWS Systems Manager, in an environment with Amazon Elastic Compute Cloud (Amazon EC2) instances. AWS Config and Systems Manager are services that aid a CloudOps engineer in monitoring and remediating compliance tasks.

Services used in this lab
AWS Systems Manager gives you visibility and control of your infrastructure on Amazon Web Services (AWS). It provides a unified user interface so that you can view operational data from multiple AWS services. Systems Manager uncomplicates resource and application management, shortens the time to detect and resolve operational problems, and lets you manage your infrastructure securely at scale.

AWS Config helps you streamline compliance auditing, security analysis, change management, and operational troubleshooting of your AWS resources. AWS Config continually monitors and records your AWS resource configurations and automatically evaluates the recorded configurations against your desired configuration. With AWS Config you can do the following:

Review changes in configurations.
Dive into detailed resource configuration histories.
Review relationships between AWS resources.
Determine overall compliance with your defined configurations and internal guidelines.
Objectives
By the end of this lab, you will be able to do the following:

Set up Inventory, a capability of AWS Systems Manager, for an AWS infrastructure.
Use AWS Systems Manager to securely log in to Amazon EC2 instances.
Set up AWS Config for an AWS infrastructure.
Use AWS Config to audit AWS resources for organizational-level compliance.
Use Inventory to view the metadata on your managed instances.
Prerequisites
This lab requires the following:

Access to a computer with Wi-Fi and Microsoft Windows, macOS, or Linux (Ubuntu, SUSE, or Red Hat)
An internet browser such as Chrome, Firefox, or Microsoft Edge
A text editor
Scenario
You are a newly hired AWS Cloud Operations Administrator. You are assisting your company’s transition to the cloud. As part of the transition, the company wants you to employ Systems Manager to aid in the management of AWS Cloud resources. You have been asked to verify that sessions from Fleet Manager, a capability of AWS Systems Manager, can interact with managed EC2 instances. Next, you need use AWS Config to create an automated system to audit for any EC2 instances that are not managed by Systems Manager. Finally, you need to explore the use of Systems Manager as a centralized way to view the inventory for any managed EC2 instance.

In this lab, you set up AWS Systems Manager components and AWS Config services for the AWS lab environment. The Systems Manager service is used to manage a fleet of EC2 instances, securely connect to any EC2 instance, and collect inventory of instance metadata and installed applications. The AWS Config service is used to create compliance rules at an organizational level. A common use case is to combine both AWS Config and Systems Manager to automate remediation actions against those rules. However, in this lab, it will be used to perform only an audit of specific resources in the lab environment.

Duration
This lab requires approximately 60 minutes to complete.

Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Command: A command that you must run
 Expected output: A sample output that you can use to verify the output of a command or edited file
 Note: A hint, tip, or important guidance
 Additional information: Where to find more information
 CAUTION: Information of special interest or importance (not so important to cause problems with the equipment or data if you miss it, but that could result in the need to repeat certain steps)
 Knowledge check: An opportunity to check your knowledge and test what you have learned
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
Task 1: Setting up Inventory
In this task you set up Inventory to perform an audit of the metadata associated with EC2 instances within your account. You can configure Inventory on all your managed nodes, even those in different Regions. Note that Inventory collects only metadata from your managed nodes. Inventory doesn’t access proprietary information or data stored on your compute resources.

In this task, you set up the Inventory function within Systems Manager so that you can later review its results in Task 5.

On the AWS Management Console, in the search box, search for and choose Systems Manager.

In the left navigation pane, from the  Node Management submenu, choose Inventory.

Choose the Setup Inventory button at the top of the page.

In the Targets section, select the button next to Manually selecting instances. This will give you the opportunity to choose a selection of nodes within your account.

In the expanded menu, select the App Server and Web Server check boxes .

Leave the default values for the remainder of the options.

Choose the Setup Inventory button.

 Expected output: A banner message like the following appears at the top of the page:  Setup inventory request succeeded

Task 2: Using Session Manager, a capability of AWS Systems Manager
In this task, you review the EC2 instances in your account that you can manage through Fleet Manager, and start a terminal session using the Session Manager functionality within Systems Manager. You then perform a high-level inventory of the Amazon EC2 entities in your account through the AWS Command Line Interface (AWS CLI).

 Note: Other ways to start a session with managed EC2 instances include using the AWS CLI or the Amazon EC2 console.

In the left navigation pane, from the  Node Management submenu, choose Fleet Manager.
Fleet Manager helps you remotely manage your nodes running on AWS or on premises.

Choose the Web Server Node ID link.

Choose the Node actions  dropdown button, choose Connect  , and choose Start terminal session .

A terminal for the EC2 instance opens in a new browser tab. The instance ID of the EC2 instance that you are connected to appears on the top banner.

 Command: In the command prompt of the terminal, run the following command: netstat -a | grep http
 Expected output:


sh-4.2$ netstat -a | grep http
tcp        0      0 ip-10-0-0-201.us-:46290 52.94.177.133:https     ESTABLISHED
tcp        0      0 ip-10-0-0-201.us-:49414 52.119.171.223:https    ESTABLISHED
tcp        0      0 ip-10-0-0-201.us-:49400 52.119.171.223:https    ESTABLISHED
tcp        0      0 ip-10-0-0-201.us-:42132 52.94.177.115:https     ESTABLISHED
sh-4.2$
 Command: Run this command in the terminal:

# Get region
AZ=`curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone`
export AWS_DEFAULT_REGION=${AZ::-1}

# List information about EC2 instances
aws ec2 describe-instances --output table
This command uses the AWS CLI to provide information about EC2 instances in the Region and provides you with another method that you can use to quickly review the information about the entities in your AWS account.

After you have reviewed the returned information, you can safely end the session to the EC2 instance.

Choose the Terminate button.

From the Terminate session pop-up window, choose the Terminate button.

Close the browser window that hosted the session.

Task 3: Enabling AWS Config and creating a rule
In this task you enable AWS Config and create a rule to check EC2 instance compliance.

On the AWS Management Console, in the search box, search for and choose Config.

Choose the Get started button.

In the General settings section, select the following options:

 Record all current and future resource types supported in this region

 Include globally recorded resource types

 Create AWS Config service-linked role

Choose Next.

The AWS Managed Rules page of the AWS Config setup opens.

In the search field, enter ec2-instance-managed-by-systems-manager.

Select the ec2-instance-managed-by-systems-manager check box . The rule will highlight when selected.

Choose the Next button.

 Expected output: The Review page of the AWS Config setup opens.

Choose Confirm.
AWS Config finishes the setup process and the AWS Config Dashboard page opens.

Choose Rules from the main AWS Config left navigation pane.
 CAUTION: There is also a Rules entry under the Aggregators listing in the navigation pane. You do not want the Rules listing underneath Aggregators. You want the one above it. You might need to expand the navigation bar by selecting the menu icon  in the left corner.

 Additional information: The initial setup process for AWS Config is now complete. Additionally, you added one compliance rule, ec2-instance-managed-by-systems-manager, to AWS Config during the setup process. This AWS Config rule scans for any EC2 instances in the infrastructure and the Detective compliance column displays Evaluating… while the scan is in progress. When the scan has finished, AWS Config returns a compliance report that lists the compute resources that are and are not currently managed by AWS Systems Manager.

Choose ec2-instance-managed-by-systems-manager from the Rules section.
 Expected output:
In time, your compliance status will show your two EC2 instances as Compliant as the AWS Config and AWS Systems Manager services sync. However, the compliance status of any one AWS Config rule in this lab is not critically important and does not block you from completing all other tasks in the lab. You can proceed to the next task and return later to check your AWS Config rule compliance status. If your AWS Config rule returns a result of No resources in scope, you must wait up to 5 minutes for the EC2 instance to synchronize with AWS Config and re-evaluate the ec2-instance-managed-by-systems-manager AWS Config rule.

It takes several minutes for AWS Config to synchronize with Systems Manager about the compliance status of managed EC2 instances. It is okay to periodically choose the refresh button  from the console until there is a change in the Compliance column. The compliance status for the ec2-instance-managed-by-systems-manager rule changes from Noncompliant resource(s) to Compliant when the status is synchronized between the services.

Task 4: Creating an AWS Config rule to audit user IAM permissions
In this task, you add an additional AWS Config rule to the lab environment. AWS Config scans for compliance with the rule of AWS Identity and Access Management (IAM) resources within your infrastructure. Then you examine the results of the AWS Config rule scan.

Choose the Add Rule button.
The Specify rule type page opens.

In the AWS Managed Rules section, enter iam-user-no-policies-check into the rule search box.

Select the radio button  next to iam-user-no-policies-check.

Choose the Next button.

All default settings on this page work for this lab.

Choose the Next button.

Choose the Save button.

You have added a new AWS Config rule to your infrastructure that scans for IAM users with attached inline policies. The newly added Config rule immediately begins a scan to evaluate the compliance of IAM resources.

 Note: In this case, you should not expect these resources to become compliant. If you choose the resources in the scope of this rule and view their Configuration Item, you will see they have policies attached. You do not need to remediate any noncompliant resource in this lab. In this lab scenario, the task was to use AWS Config rules to verify if any company user has inline IAM policies attached.

You have now set up more than one rule for AWS Config by using the web console. In your personal AWS environment, the creation of AWS Config rules can be automated by using either AWS CloudFormation or one of the AWS SDKs.

Task 5: Exploring inventory collected by Systems Manager
In this task, you explore the inventory of an installed application on the EC2 instances. This inventory was created by the Systems Manager command documents that ran during the task named the Setup Systems Manager task.

On the AWS Management Console, in the search box, search for and choose Systems Manager.

In the left navigation pane, from the  Node Management submenu, choose Inventory.

 Expected output: The Inventory Dashboard opens.

Locate the Top 5 Applications section on the dashboard.

 Knowledge check: What are the top five applications installed on the managed EC2 instances and what versions are they?

Locate the Corresponding managed instances section on the dashboard.

Choose the link to the instance ID for one of the managed EC2 instances.

 Expected output: An AWS Systems Manager details page for the EC2 instance opens.

Locate the Corresponding managed instances section (towards the bottom of the page).

 Knowledge check: What is the IP address for this EC2 instance? What platform type of Amazon EC2 instance is this node?

In the Details pane, choose the Tags link.

 Knowledge check: Which tags are associated with this EC2 instance?

In the Details pane, choose the Inventory link.

Enter bind-utils into the inventory search box and press Enter.

 Knowledge check: Which version of the package is installed on this EC2 instance? What architecture is it for?

In the Details pane, choose the Associations link.

 Knowledge check: When was the last SSM document run on this EC2 instance? What was the name of that SSM document?

In the Details pane, choose the Patches link.

 Knowledge check: If there are no patches found, why might this be?

If you did find patches applied to an instance, the information listed in this section includes answers to these questions: How many patches have been applied to this EC2 instance since it was launched? Did any of the patches encounter an error while updating? Is any further patching currently required?

In the Details pane, choose the Configuration compliance link.

 Knowledge check: Is this EC2 instance out of compliance with any of the patches?

Conclusion
 Congratulations! You now have successfully done the following:

Set up Inventory, a capability of AWS Systems Manager, for an AWS infrastructure.
Used AWS Systems Manager to securely log in to Amazon EC2 instances.
Set up AWS Config for an AWS infrastructure.
Used AWS Config to audit AWS resources for organizational-level compliance.
Used Inventory to view the metadata on your managed instances.
Additional resources
For more information about Systems Manager requirements, see Setting Up AWS Systems Manager in the AWS Systems Manager User Guide.

End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End lab and then confirm that you want to end your lab.