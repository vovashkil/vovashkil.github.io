# Introduction to AWS CodeDeploy

## Lab overview

In this lab, you deploy a sample service application to two Amazon Elastic Compute Cloud (Amazon EC2) instances that have already been configured through the lab template. Use AWS CodeDeploy to push software onto a fleet of Amazon EC2 instances and have the software automatically deployed, registered, and started.

Objectives
By the end of this lab, you will be able to do the following

Use CodeDeploy to make systematic deployments to a fleet of Amazon EC2 instance servers.
Verify if the CodeDeploy agent is installed and running on a Windows server.
Create a deployment application and group in CodeDeploy.
Review and prepare a deployment package to be installed by CodeDeploy.
Monitor deployment status and deployment targets in CodeDeploy.
Prerequisites:
Basic knowledge of how to navigate through the AWS Management Console
Familiarity with using a text editor to edit scripts
Duration
This lab requires 45 minutes to complete.

Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Command: A command that you must run
 Expected output: A sample output that you can use to verify the output of a command or edited file
 Note: A hint, tip, or important guidance
 Additional information: Where to find more information
 CAUTION: Information of special interest or importance (not so important to cause problems with the equipment or data if you miss it, but that could result in the need to repeat certain steps)
 WARNING: An action that is irreversible and could potentially impact the failure of a command or process (including warnings about configurations that cannot be changed after they are made)
 Copy edit: A time when copying a command, script, or other text to a text editor (to edit specific variables within it) might be easier than editing directly in the command line or terminal
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
Lab architecture

Diagram: This diagram depicts the architecture components that have been or are deployed in this lab. This includes an Amazon Simple Storage Service (Amazon S3) bucket, AWS CodeDeploy, the HeartBeat Deployment application, a CodeDeploy deployment group named HeartBeat Deployment Group, and two EC2 instances named HeartBeat Application.

Task 1: Reviewing the existing environment
In this task, you review the existing environment that is preconfigured for you.

Task 1.1: Reviewing Amazon EC2 instance servers
In this task, you use the AWS Management Console to verify that two Windows EC2 instances have been configured, and review the configuration.

On the AWS Management Console, in the search box, search for and choose EC2.

On the Resources page, Instances (running) indicates the instances that have been launched and are running. To see a list of running instances, choose the Instances (running) link.

Three instances are listed and are in the Running state. Two of these instances are named HeartBeat-Instance.

 Note: These two EC2 instances are used as the deployment targets with the CodeDeploy agent in later steps.

Ensure that the Status check for both of these instances have been completed to verify that the instances are configured and ready to be used.
 Expected status output:

2/2 checks passed

You do not need to do anything further with the instances at this time. You can now continue to the next steps.

 Congratulations! You have successfully verified that two EC2 instances are configured and running.

Task 1.2: Verifying that the CodeDeploy agent is running
In this task, you verify that the AWS CodeDeploy agent is installed and running on the two HeartBeat-Instance instances.

AWS CodeDeploy agent

The CodeDeploy agent is a software package that, when installed and configured on an instance, makes it possible for that instance to be used in CodeDeploy deployments.

Ensure that you are still on the Instances page. Select one of the instances named Heartbeat-Instance.

Choose Connect.

Choose the Session Manager tab. Choose Connect.

 Note: If there is a warning or an error, wait a few minutes and try again.

The browser opens a new tab where a Windows PowerShell command line interface (CLI) opens. Use Windows PowerShell to verify that the HeartBeat service is running as expected after the deployment.

 Note: If there is no command prompt, refresh the page.

 Command: In the Windows PowerShell CLI, run the following command:

powershell.exe -Command Get-Service -Name codedeployagent
 Expected output:


Status   Name               DisplayName
------   ----               -----------
Running  codedeployagent    CodeDeploy Host Agent Service
Task 1.3: Reviewing permissions for the CodeDeploy service role
In this task, you verify that a service role for AWS CodeDeploy is already created.

For CodeDeploy, a service role is used to identify instances that it can deploy applications to or perform operations on. A service role can also be used to set Amazon CloudWatch alarms and publish Amazon Simple Notification Service (Amazon SNS) notifications related to deployments.

On the AWS Management Console, in the search box, search for and choose IAM.

In the left navigation pane, from the Access management dropdown menu, choose Roles.

Scroll to locate the CodeDeployServiceRole role.

Choose the CodeDeployServiceRole, and ensure that the managed policy is attached to it.

On the Permissions tab, view the policies attached to the role.

Expand AWSCodeDeployRole and view the AWS managed policy statement.

 Congratulations! You have successfully verified that the environment is set up. Now you are ready to configure the AWS CodeDeploy service to handle the deployments.

Task 2: Creating a CodeDeploy application and deployment group
In this task, you configure AWS CodeDeploy to deploy the application. You use the CodeDeploy console to create an application and deployment group as the target where CodeDeploy deploys the software.

Task 2.1: Creating a deployment application
In this task, you use CodeDeploy to create a deployment application.

On the AWS Management Console, in the search box, search for and choose CodeDeploy.
 WARNING: Make sure to use the AWS Region that matches the AwsRegionName or AWSRegionCode value from the navigation pane to the left of these instructions.

In the navigation pane, choose Deploy > Applications.

Choose Create application.

On the Create application page, configure the following values:

For Application name, enter HeartBeatProduction-App.
For Compute platform, choose EC2/On-premises.
Choose Create application.
 Expected service output:

Application created

In order to create a new deployment, you must first create a deployment group.

Task 2.2: Creating a deployment group
In this task, you use CodeDeploy to create a deployment application group to identify your application instances tagged by the name HeartBeat-Instance.

On the Applications Dashboard page, choose Create deployment group.
On the Create deployment group page, configure the following options:

In the Deployment group name section, for Enter a deployment group name, enter HeartBeatProduction-App-Group.

In the Service role section, for Enter a service role, choose CodeDeployServiceRole.

For Deployment type, select In-place.

In the Environment configuration section, configure the following values:

Select Amazon EC2 instances.

In the Tag group 1 section, make the following selections:

For Key, choose Name.

For Value - optional, choose HeartBeat-Instance.

 Note: Notice that two instances are selected as unique matched instances. The selection means that they qualify as targets for this deployment group, based on the Name tag that matches HeartBeat-Instance.

In the Deployment settings section, verify that CodeDeployDefault.AllAtOnce is chosen.

In the Load balancer section, clear the Enable load balancing check box. You do not need a load balancer to manage the traffic for this lab.

Accept the defaults for the remaining options.

Choose Create deployment group.

 Expected service output:

Success

Deployment group created

 Congratulations! The CodeDeploy application and deployment group are created. You are now ready to deploy the software to the target instances.

Task 3: Reviewing the application bundle to be deployed
CodeDeploy requires an application to deploy. You are provided with a sample application to use for this lab. In this task, you use AWS Cloud9 to download and prepare the code bundle for distribution to the Windows EC2 instances that you launched earlier in this lab.

The sample application is a Windows application service called Heartbeat. It writes a heartbeat message to a log file periodically and also writes details about its running state as it transitions from stopped to running and back to stopped again. During deployment, the CodeDeploy agent uses the mappings and hooks in the appspec.yml file to determine which scripts and files to use from the revision to deploy to the EC2 instance.

Task 3.1: Connecting to the AWS Cloud9 IDE
In this task, you connect to the AWS Cloud9 integrated development environment (IDE).

To open the AWS Cloud9 environment, copy the Cloud9Environment URL value to the left of these instructions, and paste it into a new browser tab.
Task 3.2: Reviewing the source code
In this task, you review the source code in the AWS Cloud9 IDE.

 Note: The code is available to you in the ~/environment/CodeDeployHeartbeatDemo/HeartBeat-App folder path. HeartBeat is the application that you are configuring CodeDeploy to manage the deployment of to your Amazon EC2 fleet.

In the environment pane on the left side of the AWS Cloud9 IDE, expand CodeDeployHeartbeatDemo > Heartbeat-App and locate the appspec.yml file.
Task 3.3: Reviewing the appspec.yml file
In this task, you review the appspec.yml file.

The appspec.yml file outlines each of the source files that are contained in the .zip archive and specifies the destination on the target EC2 instance where the file should be stored. This implementation only uses two lifecycle hooks - ApplicationStop and AfterInstall - however, you can use more if required by your use case. For this lab, PowerShell scripts (also included in the .zip file archive) is used to stop the Windows service and unregister it (if it is already installed). After all the files are copied, it registers the service, starts the service, and moves the wintail helper into place to assist with watching the log file.

To open the appspec.yml file, double-click the file, or right-click to open the context menu and choose Open.

Review the contents of the appspec.yml file. It has the following contents:


version: 0.0
os: windows
files:
  - source: Heartbeat.dll
    destination: c:\HeartbeatService
  - source: HeartbeatService.exe
    destination: c:\HeartbeatService
  - source: HeartbeatService.exe.config
    destination: c:\HeartbeatService
  - source: log4net.dll
    destination: c:\HeartbeatService
  - source: Logger.dll
    destination: c:\HeartbeatService
  - source: wintail.exe
    destination: c:\temp

hooks:
  ApplicationStop:
    - location: uninstall.ps1
      timeout: 30
  AfterInstall:
    - location: install.ps1
      timeout: 30
    - location: copywintail.ps1
      timeout: 30
 Congratulations! The CodeDeploy application and deployment group are created. You are now ready to deploy the software to the target instances.

Task 4: Deploying the application bundle
In this task, you prepare the application bundle to distribute and deploy the application revision to the configured EC2 instances.

Task 4.1: Pushing the application to an archive file
CodeDeploy requires that deployment artifacts are stored in an Amazon S3 bucket. In this task, you use the AWS Command Line Interface (AWS CLI) to create the bucket.

 Note: You access the AWS CLI by using the terminal pane in the AWS Cloud9 IDE.

 Copy edit: Copy the following command into a text editor, and replace the YOUR_INITIALS and YOUR_POSTAL_CODE placeholder values with your own:

bucketName=heartbeat-codedeploy-artifacts-YOUR_INITIALS-YOUR_POSTAL_CODE
 Note: Bucket names cannot contain uppercase letters, so use lowercase letters for your initials.

 Example:


bucketName=heartbeat-codedeploy-artifacts-mpu-31092
In the AWS Cloud9 terminal pane, run the updated command to create the bucketName variable.
 Expected output:

None, unless there is an error.

 Note: You can verify the variable by running: echo $bucketName

 Command: To create a new S3 bucket using the newly created variable, run the following command:

aws s3 mb s3://$bucketName
 Expected output:


make_bucket: heartbeat-codedeploy-artifacts-mpu-31092
 Caution: If you receive an error that the bucket name is unavailable, create the variable again with some extra characters after your initials and then try to create the bucket again.

Task 4.2: Deploying the application to CodeDeploy targets
In this task, you deploy the Heartbeat application to the target EC2 instances from the revision stored in the S3 bucket.

 Note: The implementation files are in the AWS Cloud9 environment, so you need to bundle these and push them to Amazon S3. The AWS CLI CodeDeploy tool includes a helper that accomplishes this for you.

Use the AWS Cloud9 IDE terminal window to complete the following steps.

 Command: In the AWS Cloud9 terminal window, to ensure that you are in the CodeDeployHeartbeatDemo folder, run the following command:

cd ~/environment/CodeDeployHeartbeatDemo
 Expected output:

None, unless there is an error.

 Note: To complete the rest of the steps in this task, you must remain at the CodeDeployHeartbeatDemo directory level.

 Command: To bundle up the files, push the revision to the S3 bucket that you created in the previous step, and register the information with CodeDeploy, run the following command:

aws deploy push --application-name HeartBeatProduction-App --source HeartBeat-App --s3-location s3://$bucketName/HeartBeat-App.zip
 Expected output:


To deploy with this revision, run:
aws deploy create-deployment --application-name HeartBeatProduction-App --s3-location bucket=heartbeat-codedeploy-artifacts-mpu-31092,key=HeartBeat-App.zip,bundleType=zip,eTag=162ab7baf9c7497941c4c7aca50fee0e --deployment-group-name <deployment-group-name> --deployment-config-name <deployment-config-name> --description <description>
 Note: This uses the same bucketName variable that you created earlier to store the artifact revisions. If you have issues, you can use the echo $bucketName command to confirm that the variable is correct…

 Command: To deploy the application revision from the Amazon S3 bucket that you created earlier to the target EC2 instances, run the following command:

aws deploy create-deployment --application-name HeartBeatProduction-App --deployment-group-name HeartBeatProduction-App-Group --deployment-config-name CodeDeployDefault.AllAtOnce --description "Initial Deployment" --s3-location bucket=$bucketName,key=HeartBeat-App.zip,bundleType=zip
 Note: This command creates a deployment associated with the following using the application revision named HeartBeat-App.zip in the S3 bucket that you created earlier:

Application named CodeDeployHeartbeatDemo
Deployment configuration named CodeDeployDefault.AllAtOnce
Deployment group named HeartBeat-Deployment
 Consider: The deployment configuration specifies the number or percentage of instances that must remain available at any time during a deployment. In the previous command, the deployment-config-name value is the same as the predefined name used while creating the deployment group. However, you can override this by choosing a custom or another predefined configuration.

 Expected output: You should see an output similar to the following:


{
    "deploymentId": "d-VAGGPWO9O"
}
Task 4.3: Monitoring deployment status
In this task, you monitor the deployment by using the AWS CodeDeploy console.

Navigate back to the CodeDeploy console. In the left navigation pane, choose Deploy > Deployments.

In the Deployment history pane, choose the name of the deployment that matches the deploymentId that was returned from the AWS CLI call.

In the Deployment lifecycle events, you can view the two EC2 instances that have been tagged and are part of the deployment group. Both of them have a status of In Progress. This is because you used the deployment configuration CodeDeployDefault.AllAtOnce in your CLI call. This instructs CodeDeploy to deploy the update to all servers at the same time.

The status changes to Succeeded once complete and you have the option to view the events.

To show the events for the instances as they are deployed, choose View events when it appears:
Succeeded event statuses from EC2.

Image: Depicts the status of the EC2 instances as they are deployed.

Task 4.4: Reviewing the deployment targets
In this task, you verify that CodeDeploy successfully deployed the HeartBeat application to the deployment targets. You use Session Manager to access the EC2 instances, and review that the HeartBeat application is installed and the service is running.

On the AWS Management Console, in the search box, search for and choose EC2.

In the navigation pane, choose Instances.

Select one of the instances named Heartbeat-Instance.

Choose Connect.

Confirm that the Session Manager tab is selected. Choose Connect.

In a new browser tab, a Windows PowerShell CLI opens. Use Windows PowerShell to verify that the HeartBeat service is running as expected after the deployment.

 Command: In the Windows PowerShell CLI, enter the following command:

Service “AWSHeartbeat*”
 Expected output:


Status   Name               DisplayName
------   ----               -----------
Running  AWSHeartbeatSer... AWS Heartbeat Demo Service
 Note: If the expected output is not returned, rerun the command without the filter. Running Service command returns all running services sorted alphabetically. Scroll through the list of services to find the AWSHeartbeat service.

To view that the service is running correctly, you must review the log output.

 Command: Run the following command in the Windows PowerShell CLI:

Content C:\Logs\HeartBeatService.log -last 10
 Expected output:


[INFO]11/09 19:46:29 - Heartbeat - Deploy has Worked on Tuesday! Iteration 87
[INFO]11/09 19:46:30 - Heartbeat - Deploy has Worked on Tuesday! Iteration 88
[INFO]11/09 19:46:31 - Heartbeat - Deploy has Worked on Tuesday! Iteration 89
[INFO]11/09 19:46:32 - Heartbeat - Deploy has Worked on Tuesday! Iteration 90
[INFO]11/09 19:46:33 - Heartbeat - Deploy has Worked on Tuesday! Iteration 91
[INFO]11/09 19:46:34 - Heartbeat - Deploy has Worked on Tuesday! Iteration 92
[INFO]11/09 19:46:35 - Heartbeat - Deploy has Worked on Tuesday! Iteration 93
[INFO]11/09 19:46:36 - Heartbeat - Deploy has Worked on Tuesday! Iteration 94
[INFO]11/09 19:46:37 - Heartbeat - Deploy has Worked on Tuesday! Iteration 95
[INFO]11/09 19:46:38 - Heartbeat - Deploy has Worked on Tuesday! Iteration 96
By using this approach, you can readily deploy an application to a large fleet of EC2 instances. Or you can update an application with a new version, a task that would be error prone and time consuming to do manually.

 Note: Keep this tab or window open.

 Congratulations! You have successfully deployed the application bundle to the CodeDeploy target EC2 instances, and monitored and confirmed that the application was installed on the HeartBeat instances.

Task 5: Using CodeDeploy to redeploy applications
In this task, you take a modified version of the Heartbeat service and then redeploy it. This demonstrates the service stop, uninstall, install, and start processes defined in the appspec.yml file.

Task 5.1: Deploying the new changes
In this task, you deploy the new changes to the HeartBeat Instances.

Return to your AWS Cloud9 IDE.

 Command: To switch to the Updated-HeartBeat-App folder, run the following command in the AWS Cloud9 terminal window:


cd ~/environment/Updated-HeartBeat-App
 Expected output:

None, unless there is an error.

 Command: To confirm that your bucketName variable is still active, run the following command:

echo $bucketName
 Expected output:


******************************
**** This is OUTPUT ONLY. ****
******************************

heartbeat-codedeploy-artifacts-mpu-31092
 Note: If the variable doesn’t match the bucket name that you created in Task 4, run the updated bucketName=heartbeat-codedeploy-artifacts-YOUR_INITIALS-YOUR_POSTAL_CODE command again to match the name of the bucket that you created.

 Command: To bundle the files, push the revision to the S3 bucket that you created earlier, and register the information with CodeDeploy, run the following command:

aws deploy push --application-name HeartBeatProduction-App --source HeartBeat-App --s3-location s3://$bucketName/HeartBeat-App.zip
 Expected output:


******************************
**** This is OUTPUT ONLY. ****
******************************

To deploy with this revision, run:
aws deploy create-deployment --application-name HeartBeatProduction-App --s3-location bucket=heartbeat-codedeploy-artifacts-mpu-31092,key=HeartBeat-App.zip,bundleType=zip,eTag=7e6cb76c9e6a40f8dcde8672226a0dd9 --deployment-group-name <deployment-group-name> --deployment-config-name <deployment-config-name> --description <description>
 Command: To create a new deployment, issue the following command:

aws deploy create-deployment --application-name HeartBeatProduction-App --deployment-group-name HeartBeatProduction-App-Group --deployment-config-name CodeDeployDefault.AllAtOnce --description "Updated Deployment" --s3-location bucket=$bucketName,key=HeartBeat-App.zip,bundleType=zip
 Expected output:


{
    "deploymentId": "d-ENKAUKD4B"
}
 Note: This creates another deployment of the updated bundle to the EC2 instances.

Task 5.2: Reviewing the deployment targets
In this task, you monitor and review the deployment targets to ensure that the new changes were successfully deployed.

Monitor the progress of the deployment from the AWS CodeDeploy console that was performed in Task 4.3.

Return to the EC2 Heartbeat-Instance SSM tab.

 Command: In the Windows PowerShell CLI, enter the following command:


Content C:\Logs\HeartBeatService.log -last 10
 Expected output:


******************************
**** This is OUTPUT ONLY. ****
******************************

[INFO]11/09 19:52:13 - Heartbeat Service - Updated!!! Iteration 22
[INFO]11/09 19:52:14 - Heartbeat Service - Updated!!! Iteration 23
[INFO]11/09 19:52:15 - Heartbeat Service - Updated!!! Iteration 24
[INFO]11/09 19:52:16 - Heartbeat Service - Updated!!! Iteration 25
[INFO]11/09 19:52:17 - Heartbeat Service - Updated!!! Iteration 26
[INFO]11/09 19:52:18 - Heartbeat Service - Updated!!! Iteration 27
[INFO]11/09 19:52:19 - Heartbeat Service - Updated!!! Iteration 28
[INFO]11/09 19:52:20 - Heartbeat Service - Updated!!! Iteration 29
[INFO]11/09 19:52:21 - Heartbeat Service - Updated!!! Iteration 30
[INFO]11/09 19:52:22 - Heartbeat Service - Updated!!! Iteration 31
 Note: If different results are returned, rerun the command. Deployment times are quick but not instantaneous.

This exercise demonstrated how straightforward it is to update a large fleet of EC2 instances with a new version of a Windows service, a task that would be error prone and time consuming to do manually.

 Congratulations! You have successfully taken a modified version of the Heartbeat service and redeployed it.

Conclusion
 Congratulations! You now have successfully done the following:

Used CodeDeploy to make systematic deployments to a fleet of Amazon EC2 instance servers
Verified if the CodeDeploy agent is installed and running on a Windows server
Created a deployment application and group in CodeDeploy
Reviewed and prepared a deployment package to be installed by CodeDeploy
Monitored deployment status and deployment targets in CodeDeploy
Additional resources
For more information about AWS CodeDeploy, see What Is CodeDeploy?
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End lab and then confirm that you want to end your lab.