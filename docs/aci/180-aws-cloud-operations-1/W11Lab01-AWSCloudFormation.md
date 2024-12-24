# Using AWS CloudFormation

## Lab overview

In this lab, you gain hands-on experience with an AWS CloudFormation template. You modify a CloudFormation template and use the AWS Command Line Interface (AWS CLI) and AWS Management Console to create a stack. You then detect drift in the stack and perform a stack update.

In this lab, you have been tasked with creating an environment for a development team. The development team has asked for an Apache web server with HTTP access. The requirements document that you have been provided asks for a dedicated virtual private cloud (VPC), a single public subnet, and a small Amazon Elastic Compute Cloud (Amazon EC2) instance. You use your AWS Cloud9 environment to modify an existing CloudFormation template to meet the requirements of the development team. You modify the template to use the CloudFormation change set, and detect drift functionality.

Objectives
By the end of this lab, you will be able to do the following:

Build AWS CloudFormation templates in YAML to define infrastructure resources.
Modify a CloudFormation stack to provision infrastructure and review the outputs.
Detect changes made to your resources and generate drift reports.
Use CloudFormation change sets to update your infrastructure.
Prerequisites
This lab requires the following:

Access to a computer with Microsoft Windows, Mac OS X, or Linux (Ubuntu, SuSE, or Red Hat)
A modern internet browser such as Chrome or Firefox
Experience using CloudFormation and editing JSON and YAML files
An understanding of basic cloud operations and familiarity with navigating the AWS Management Console
Duration
This lab requires approximately 45 minutes to complete.

Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Command: A command that you must run.
 Expected output: A sample output that you can use to verify the output of a command or edited file.
 Note: A hint, tip, or important guidance.
 Additional information: Where to find more information.
 CAUTION: Information of special interest or importance (not so important to cause problems with the equipment or data if you miss it, but it could result in the need to repeat certain steps).
 WARNING: An action that is irreversible and could potentially impact the failure of a command or process (including warnings about configurations that cannot be changed after they are made).
 Refresh: A time when you might need to refresh a web browser page or list to show new information.
 Copy edit: A time when copying a command, script, or other text to a text editor (to edit specific variables within it) might be easier than editing directly in the command line or terminal.
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
Lab environment
The lab architecture depicting a user making changes to the AWS CloudFormation template and with those changes updating the AWS environment.

Image depicts: An AWS CloudFormation template that builds a simple Amazon Virtual Private Cloud (Amazon VPC) environment and deploys a web server with a web page. The user manually modifies an Amazon EC2 Security Group and uses the Detect drift command to detect the change. Lastly, the user creates a change set to update the Security Group with the expected values.

Task 1: Connecting to the AWS Cloud9 IDE
In this task, you connect to the AWS Cloud9 integrated development environment (IDE).

AWS Cloud9 development environments come prepackaged with the AWS CLI and tooling for over 40 programming languages. Next, you verify that the AWS CLI is installed.

Task 1.1: Exploring the lab contents
To open the AWS Cloud9 environment, copy the Cloud9Environment URL value to the left of these instructions and paste it into a new browser tab.
In the AWS Cloud9 environment, the left pane is the file tree. It shows a list of all files that are currently available and open in the editor.

You have been provided with three CloudFormation templates to work with.

In the AWS Cloud9 file tree pane, choose the templates folder to expand it and see the CloudFormation templates.
Within the templates folder, there is an incomplete CloudFormation template named lab1.yaml. You make changes to this template.

Within the help subfolder, there are two complete CloudFormation templates:

The task2-solution.yaml template to use as a reference to verify your Task 2 solutions

The task4-solution.yaml template to use as a reference to verify your Task 4 solution

The lower pane includes three tabs: a bash terminal located at the bottom, a welcome tab, and the Immediate tab. You work in the bash terminal for this step.

 Note: When the AWS Cloud9 environment is first launched, a bash script clones an AWS CodeCommit repository that contains the AWS CloudFormation templates that you use for this lab.

 Expected output: This is an example output only.


AWSLabsUser-hfRtqbnX2oKVNR5xSqAaQZ:~/environment $ /tmp/git-cloning-runner-1665674232684-080250367781.sh
Cloning into '/home/ec2-user/environment/templates'...
remote: Counting objects: 5, done.
Unpacking objects: 100% (5/5), 6.87 KiB | 6.87 MiB/s, done.

Navigate to your cloned repository by typing "cd /home/ec2-user/environment/templates" to start working with "https://git-codecommit.us-east-1.amazonaws.com/v1/repos/lab1"

To set your display name run "git config --global user.name YOUR_USER_NAME"
To set your display email run "git config --global user.email YOUR_EMAIL_ADDRESS"
Task 1.2: Verifying that the AWS CLI is installed in the AWS Cloud9 environment
 Command: To verify that the AWS CLI is installed and to display its version, run the following command in bash terminal window:

aws --version
 Expected output: Your version might be newer.


aws-cli/2.13.3 Python/3.11.4 Linux/4.14.320-242.534.amzn2.x86_64 exe/x86_64.amzn.2 prompt/off
Task 1.3: Exploring the basics of a CloudFormation template
In the left pane, from the templates folder, right-click the lab1.yaml file and choose Open.
The file opens in the top pane in a tab next to the AWS Cloud9 Welcome tab. Scroll through the file and note that it includes four sections: Description, Parameters, Resources, and Outputs. Resources is the only required section in an AWS CloudFormation template; all other sections are optional.

The sections included in your template serve the following purpose:

Description: A text string that describes the template

Parameters: Values to pass to your template at runtime (when you create or update a stack)

Resources: Specifies the stack resources and their properties

Outputs: Describes the values that are returned as stack properties after the stack has successfully completed

In the next task, you modify the Parameters, Resources, and Outputs for the lab1.yaml template.

Task 2: Modifying a CloudFormation template
In this task, you use AWS Cloud9 to modify a CloudFormation template, and use that template to create a CloudFormation stack.

AWS CloudFormation provides a common language to model and provision resources in your cloud environment. You code your infrastructure with the CloudFormation template language, in either YAML or JSON format. Both YAML and JSON are data serialization languages but with different features. CloudFormation only processes JSON; templates formatted as YAML are converted to JSON when the stack creation is initiated.

For this lab, you use YAML to code the CloudFormation templates.

Task 2.1: Adding a parameter to the template
In this task, you update a parameter named InstanceType in the lab1.yaml template in the AWS Cloud9 environment.

Parameters in YAML are generally formatted as follows:


Parameters:
  InstanceTypeParameter:
    Description: Enter t2.micro, m1.small, or m1.large. Default is t2.micro.
    Type: String
    Default: t2.micro
    AllowedValues:
      - t2.micro
      - m1.small
      - m1.large
    ConstraintDescription: Must be a valid EC2 instance type.
In the Parameters section, find the label named InstanceType that has been created as a placeholder. Configure the parameter with the following settings to match the sample structure below:
Label: InstanceType
Description: WebServer EC2 instance type
Type: String
Default: t2.nano
AllowedValues: t2.nano,t2.micro,t2.small
ConstraintDescription: must be a valid EC2 instance type.
 Expected output: Once you are finished adding the values, it should look like the following:


  InstanceType:
    Description: WebServer EC2 instance type
    Type: String
    Default: t2.nano
    AllowedValues:
      - t2.nano
      - t2.micro
      - t2.small
    ConstraintDescription: must be a valid EC2 instance type.
Task 2.2: Adding a resource to the template
In this task, you add a resource named Route to the lab1.yaml template in the AWS Cloud9 environment.

Resources such as a Route, NetworkAcl, or InternetGateway follow a general format and have a Properties section that defines the specifics of the object or service declared in the template. In general, all resources have the following properties. For example:


  RouteTable:
    Type: 'AWS::EC2::RouteTable'
    DependsOn: VPC
    Properties:
      VpcId: !Ref VPC
      Tags:
        - Key: Application
          Value: !Ref 'AWS::StackId'
In the Resources section, find the label named Route that has been created as a placeholder. Configure the resource with the following settings to match the sample structure below:
Label: Route
Type: AWS::EC2::Route
DependsOn: VPC, AttachGateway
Properties:
RouteTableId: !Ref RouteTable
DestinationCidrBlock: 0.0.0.0/0
GatewayId: !Ref InternetGateway
 Expected output: Once you are finished adding the values, it should look like the following:


  Route:
    Type: 'AWS::EC2::Route'
    DependsOn:
      - VPC
      - AttachGateway
    Properties:
      RouteTableId: !Ref RouteTable
      DestinationCidrBlock: 0.0.0.0/0
      GatewayId: !Ref InternetGateway
Task 2.3: Adding an output to the template
In this task, you add an output named AppURL to the Outputs section of the lab1.yaml template in the AWS Cloud9 environment.

Outputs in YAML are generally formatted like the following example:


  MySecurityGroup:
    Description: Application instance's security group name
    Value: 
        !GetAtt 
          - InstanceSecurityGroup
          - GroupId
In the Outputs section, find the label named AppURL that has been created as a placeholder. Ensure that the output entry matches the following settings to match the sample structure below:
Logical ID: AppURL
Description Newly created application URL
Value: !Sub 'http://${WebServerInstance.PublicIp}'
 Expected output: Once you are finished adding the values, it should look like the following:


  AppURL:
    Description: Newly created application URL
    Value: !Sub 'http://${WebServerInstance.PublicIp}'
 Consider: The !Sub function substitutes variables in an input string with values that you specify. In your templates, you can use this function to construct commands or outputs that include values that aren’t available until you create or update a stack.

When you have completed editing the file, save your changes.

From the File menu, choose Save.
 Note: The task1-solution.yaml template in the help folder is a complete and usable copy of the template that you updated. If you have trouble or need help with syntax formatting, use the task2-solution.yaml template to identify your error or copy and paste between the documents as needed.

Validate the template by running the following command:

aws cloudformation validate-template --template-body file://~/environment/templates/lab1.yaml
 Congratulations! You have successfully created a CloudFormation template.

Task 3: Using the stack’s CloudFormation template to provision an infrastructure
For this task, you launch the stack creation process from the AWS CLI and review all the resources created on the CloudFormation console.


Task 3.1: Using the lab1.yaml template to run the create-stack command
In this task, you run the create-stack command to initiate a stack creation from the CLI.

 Command: In the AWS Cloud9 terminal, ensure that you are in the templates folder by running the following command:

cd ~/environment/templates
 Expected output:

None, unless there is an error.

 Command: From the terminal, to launch the stack creation process using inline parameters to match the template definition, run the following command:

 aws cloudformation create-stack --stack-name Lab1 --parameters ParameterKey=InstanceType,ParameterValue=t2.micro --template-body file://lab1.yaml
 Expected output:


{
    "StackId": "arn:aws:cloudformation:ca-central-1:350214907448:stack/Lab1/7f733ee0-bf54-11ec-aa09-0244448197b2"
}
The create-stack command calls the specified CloudFormation template and initiates a stack creation. The InstanceType parameter tells CloudFormation what size Amazon EC2 instance to deploy.

Successfully running the create-stack command returns a StackId at the command line.

 Note: If your stack creation fails, refer to the troubleshooting steps: Troubleshooting a stack CREATE_FAILED message

Task 3.2: Verifying the status of the stack
In this task, you query the status of the stack creation process by running the describe-stacks command in the CLI and viewing the process in the console.

 Command: In the terminal, run the following command:

aws cloudformation describe-stacks --stack-name Lab1
 Expected output:


{
    "Stacks": [
        {
            "StackId": "arn:aws:cloudformation:ca-central-1:167386515113:stack/Lab1/caa48f10-4dcd-11ed-9527-0251a4035624",
            "StackName": "Lab1",
            "Description": "AWS CloudFormation Simple Infrastructure Template VPC_Single_Instance_In_Subnet: This template will show how to create a VPC and add an EC2 instance with an Elastic IP address and a security group.",
            "Parameters": [
                {
                    "ParameterKey": "InstanceType",
                    "ParameterValue": "t2.micro"
                },
                {
                    "ParameterKey": "VPCCIDR",
                    "ParameterValue": "10.199.0.0/16"
                },
                {
                    "ParameterKey": "PUBSUBNET1",
                    "ParameterValue": "10.199.10.0/24"
                },
                {
                    "ParameterKey": "LatestAmiId",
                    "ParameterValue": "/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2",
                    "ResolvedValue": "ami-064687fa05edcd686"
                }
            ],
            "CreationTime": "2022-10-17T03:45:41.824Z",
            "RollbackConfiguration": {},
            "StackStatus": "CREATE_IN_PROGRESS",
            "DisableRollback": false,
            "NotificationARNs": [],
            "Outputs": [
                {
                    "OutputKey": "URL",
                    "OutputValue": "http://13.234.178.84",
                    "Description": "Newly created application URL"
                }
            ],
            "Tags": [],
            "EnableTerminationProtection": false,
            "DriftInformation": {
                "StackDriftStatus": "NOT_CHECKED"
            }
        }
    ]
}
 Note:

The describe-stacks command returns a large amount of information to the terminal. It presents information on every resource defined by your template. It also presents the current status in the build process and specific attributes of the resource that are available at the time that you run the describe-stacks command. The AWS CloudFormation dashboard presents the same information, but in a friendlier format.

It takes CloudFormation a few minutes to complete the create-stack process.

 Command: To query the status of the stack creation process, from the terminal, run the following command:

aws cloudformation describe-stacks --stack-name Lab1 --query "Stacks[0].StackStatus"
 Expected output:

A CREATE_COMPLETE status code indicates the completion of the stack creation process.

Return to the AWS Management Console browser tab to view the status in the console.

On the console, in the search box, search for and choose CloudFormation.

In the list of stacks, locate Lab1. Note the status of your Create Stack job.

Task 3.3: Reviewing the stack resources created
In this task, you review the Lab1 stack and explore the Stack Info, Events, Resources, and Outputs generated from the stack creation in the console.

On the CloudFormation console, explore the stack events. Select the stack and explore the information available on each tab: Stack Info, Events, Resources, and Outputs.

On the Resources tab, a list of resources defined in the template are created. Identify some key resources you have created. Each resource has a unique Logical ID, Physical ID, Type, and Status.

The following resources should be created:
AttachGateway
IPAddress
InboundHTTPNetworkAclEntry
InboundNetworkAclEntry
InboundResponsePortsNetworkAclEntry
InstanceSecurityGroup
InternetGateway
NetworkAcl
OutBoundHTTPNetworkAclEntry
OutBoundHTTPSNetworkAclEntry
OutBoundResponsePortsNetworkAclEntry
Route
RouteTable
Subnet
SubnetNetworkAclAssociation
SubnetRouteTableAssociation
VPC
WebServerInstance
When the status of the Create Stack job shows CREATE_COMPLETE, open the Outputs tab.

From the AppURL row, copy and paste the URL shown in the Value column in a new browser tab.

A webpage displaying a time-out error is expected to appear with the following message: This site can’t be reached.

 Note: The Public IP cannot be accessed at this time due to a Security Group restriction defined in the template. In the next task, this is fixed by modifying the Security Group resource.

 Congratulations! You have successfully provisioned a simple infrastructure using a CloudFormation template and identified a limitation in the Security Group resource.

 Note: If you encounter an error, see the Troubleshootin section at the bottom of this lab.

Task 4: Detecting drift in a CloudFormation stack
In this task, you use AWS CloudFormation to detect changes that CloudFormation didn’t make. Make a change to your environment, instruct CloudFormation to detect any drift and then view the results.

Users can change resources outside of AWS CloudFormation. Drift detection can be used to identify stack resources that have been modified outside of AWS CloudFormation management.

Task 4.1: Modifying your environment
In this task, you modify the security group rules in the EC2 console.

At the top of the AWS Management Console, in the search bar, search for and choose EC2.

On the EC2 console, in the navigation pane, choose Security Groups and select the security group for your simple infrastructure.

 Hint: To select the correct Security Group, refer to the Lab-1 CloudFormation stack Outputs and locate the one that has a matching value.

On the Inbound rules tab, choose Edit inbound rules.

On the Edit inbound rules page, on the listed Security group rule ID modify the Source parameter by selecting My IP from the dropdown menu.

Choose Save rules .

 Expected output:

Inbound security group rules successfully modified on security group…

Task 4.2: Verifying the AppURL is working
In this task, you verify the changes made to the security group have allowed you to access the previously unreachable webpage.

Return to the AWS Management Console, use the AWS search bar to search for CloudFormation and then choose the service from the list of results.

Locate the Lab1 stack in the console view.

On the Outputs tab, launch the URL shown in a new browser tab.

When loaded, a webpage is displayed with the following message: Congratulations, you have successfully deployed a simple infrastructure using AWS CloudFormation.

 Note: Notice that changing the source IP address on the Security Group allowed traffic into the webpage URL. Modifying template resources via the console is a quick-fix but not a best practice.

Task 4.3: Generating a drift report
In this task, you identify and detect the drift in the template via the AWS Management console.

Return to the CloudFormation - Stack Lab 1 browser tab.

In the stack details pane, choose the Stack actions dropdown menu and then choose Detect drift.

 Note: Wait until AWS CloudFormation completes the drift detection operation. Refresh the page to view the changes.

With your stack selected, from the Stack actions dropdown menu, select View drift results.

In the Resource drift status section, select the radio button: InstanceSecurityGroup resource that has the status of  MODIFIED.

Select View drift details to learn more about what resources that changed.

By using drift detection, you can detect whether a stack’s actual configuration differs from its expected configuration. A resource is considered to have drifted if any of its actual property values differ from the expected property values. This includes if the property or resource has been deleted. In this lab, you manually changed a resource value. The most direct manner to address this drift is to manually modify the resource back to the expected value. If the change is due to the deployment of another stack, rollback the changes of the other stack. A last resort and the most destructive is to delete your stack and redeploy it.

Task 4.4: Verifying the AppURL is working via the CLI
In this task, you identify and detect the drift in the template via the Cloud9 CLI.

Return to the AWS Cloud9 terminal to review the details of the stack drift detection operation using AWS CLI.

 Command: In the AWS Cloud9 terminal, enter the AWS CLI CloudFormation describe-stack-resource-drifts command with the following parameters:

–stack-name [Paste the stack name here]
–stack-resource-drift-status-filters MODIFIED DELETED
 Command: Copy and paste the describe-stack-resource-drifts command:


aws cloudformation describe-stack-resource-drifts --stack-name Lab1 --stack-resource-drift-status-filters MODIFIED DELETED
In the results, look for the Resource Type SecurityGroup and then look for the PropertyDifferences. The results should mirror the drift information that was displayed on the AWS CloudFormation dashboard.

 Expected output:


******************************
**** This is OUTPUT ONLY. ****
******************************

{
    "StackResourceDrifts": [
        {
            "StackId": "arn:aws:cloudformation:ca-central-1:866205660680:stack/Lab1/8550eec0-77f5-11ed-96ae-0a8916d020f2",
            "LogicalResourceId": "InstanceSecurityGroup",
            "PhysicalResourceId": "sg-0ac8f08ddbd30c839",
            "ResourceType": "AWS::EC2::SecurityGroup",
            "ExpectedProperties": "{\"GroupDescription\":\"Enable HTTP via port 80\",\"SecurityGroupIngress\":[{\"CidrIp\":\"1.1.1.1/32\",\"FromPort\":80,\"IpProtocol\":\"tcp\",\"ToPort\":80}],\"VpcId\":\"vpc-0172e787ed9d66d8e\"}",
            "ActualProperties": "{\"GroupDescription\":\"Enable HTTP via port 80\",\"SecurityGroupIngress\":[{\"CidrIp\":\"52.94.133.131/32\",\"FromPort\":80,\"IpProtocol\":\"tcp\",\"ToPort\":80}],\"VpcId\":\"vpc-0172e787ed9d66d8e\"}",
            "PropertyDifferences": [
                {
                    "PropertyPath": "/SecurityGroupIngress/0/CidrIp",
                    "ExpectedValue": "1.1.1.1/32",
                    "ActualValue": "52.94.133.131/32",
                    "DifferenceType": "NOT_EQUAL"
                }
            ],
            "StackResourceDriftStatus": "MODIFIED",
            "Timestamp": "2022-12-09T19:17:49.495000+00:00"
        }
    ]
}
 Congratulations! You have successfully detected a drift in the CloudFormation template.

Task 5: Using a change set to update the stack
In the previous task, you manually changed a resource value. The best practice to change the environment is through the template updates. Template updates can be done by using a change set.

In this task, you modify the Security Group resource to the expected value in the template. You edit the lab1 template modifying the SecurityGroupRules, review those changes as part of the Change Set, and then implement the changes to the environment.

Task 5.1: Modifying the Security Group Rules
Earlier in Task 3, the InstanceSecurityGroup was modified outside of the CloudFormation template. In this task, a change is made in the template for the stack to implement the modification when creating.

In the AWS Cloud9 Environment pane, open the context menu for lab1.yaml file you edited earlier and choose Duplicate.

Rename the duplicate file lab1-CS.yaml, and open the file in the AWS Cloud9 editor.

Modify the InstanceSecurityGroup resource to allow access to the AppURL:

Under the SecurityGroupIngress property value, note the CidrIP listed as 1.1.1.1/32.

To make the webpage accessible, change the CidrIP value to 0.0.0.0/0.

Save the file.

 Note: For hints and tips, and to validate the edits that you have made to the lab1-CS.yaml template, refer to the task4-solution.yaml template.


Task 5.2: Creating the change set
In this task, you run the create-change-set command to create a change set for the lab1.yaml template.

 Command: In the AWS Cloud9 terminal, ensure that you are in the templates folder by running the following command:

cd ~/environment/templates
 Expected output:

None, unless there is an error.

 Command: From the terminal, run the following command to launch the stack change set process:

aws cloudformation create-change-set --stack-name Lab1 --change-set-name Lab1ChangeSet --parameters ParameterKey=InstanceType,ParameterValue=t2.micro --template-body file://lab1-CS.yaml
 Expected output:


******************************
**** This is OUTPUT ONLY. ****
******************************

{
    "Id": "arn:aws:cloudformation:ca-central-1:350214907448:changeSet/Lab1ChangeSet/b62f9a0f-bd5e-4988-9016-bba2c46f351b",
    "StackId": "arn:aws:cloudformation:ca-central-1:350214907448:stack/Lab1/7f733ee0-bf54-11ec-aa09-0244448197b2"
}
After the change set is processed, AWS CloudFormation returns a StackId and Id. To see the changes that you have staged, return to the CloudFormation browser tab.

 Note: If your change set creation fails, refer to the troubleshooting steps: Troubleshooting a changeset creation failure

Task 5.3: Reviewing the changes
In this task, you review the details of the change set in the console.

Choose Lab1 from the top of the drift results window to return to your stack.

On the Change sets tab, select Lab1ChangeSet. Review the details of the change-set in the Changes tab.

Task 5.4: Running the change set
In this task, you run the change set created using the console.

In the Lab1ChangeSet window, verify that the changes are as expected for the InstanceSecurityGroup resource.

At the top right of the page, choose Execute change set..

A pop-up window prompts you to choose how to handle resources in the event of a stack failure.

With the default Roll back all stack resources chosen, select Execute change set..

 Note: Wait for 1 minute and refresh to see the change in the stack status.

Wait for the stack update to complete and the Status to change to UPDATE_COMPLETE.
Lab1ChangeSet is no longer available, and there is a new entry under Last executed change set.

Select the Change set id and review the information.
Status as CREATE_COMPLETE
Execution Status as EXECUTE_COMPLETE
Task 5.5: Verifying the AppURL is working
In this task, you access the AppURL link to ensure the security group change made is successfully implemented.

Return to the Your Environments browser tab, return to the Lab1 stack console view.

On the Outputs tab, launch the URL shown in a new browser tab.

When loaded, a webpage is displayed with the following message: “Congratulations, you have successfully deployed a simple infrastructure using AWS CloudFormation”.

Appendix

Troubleshooting a stack CREATE_FAILED message
 CAUTION: If your stack creation fails, the AWS CloudFormation console provides detailed information that you can use to identify the cause of the stack creation failure. Use that information to correct your template. When you have corrected the issue, use the following command to delete the failed stack.

Return to the AWS Cloud9 terminal and run the following command:

 WARNING: The following command is destructive in nature. Only run this command as part of debugging a failed CloudFormation stack creation.


aws cloudformation delete-stack --stack-name Lab1
Return to the AWS CloudFormation dashboard to observe your stack deletion. When the delete-stack command has completed, return to task 3.1 and rerun the create-stack command.

 WARNING: If your stack deletion fails and you cannot roll back your changes successfully, bring your issue to the attention of a lab support technician or your instructor.

To re-create the stack, return to Task 3.1.


Troubleshooting a change set creation failure
 CAUTION: If your change set creation fails, the AWS CloudFormation console provides detailed information that you can use to identify the cause of the failure. Use that information to correct your template and deploy the change set again.

 Command: When you have corrected the issue, use the following command to delete your change set:

aws cloudformation delete-change-set --change-set-name Lab1ChangeSet --stack-name Lab1
Return to the AWS CloudFormation dashboard to observe your change set deletion. When the delete-change-set has completed rerun the execute-change-set command.
 WARNING: If your stack deletion fails and you cannot roll back your changes successfully, bring your issue to the attention of a lab support technician or your instructor.
To create the change set, return to Task 5.2.

Conclusion
 Congratulations! You have successfully done the following:

Built AWS CloudFormation templates in YAML to define infrastructure resources.
Modified a CloudFormation stack to provision infrastructure and review the outputs.
Detected changes made to your resources and generate drift reports.
Used CloudFormation change sets to update your infrastructure.
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End lab and then confirm that you want to end your lab.

Additional resources
For more information, see Template Anatomy in the AWS CloudFormation User Guide.

For more information on drift, see Detecting Unmanaged Configuration Changes to Stacks and Resources.