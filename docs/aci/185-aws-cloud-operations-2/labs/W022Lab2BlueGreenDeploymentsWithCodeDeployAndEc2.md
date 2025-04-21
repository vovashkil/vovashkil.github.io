# Creating Blue/Green Deployments with AWS CodeDeploy and Amazon EC2

## Lab overview

In this lab, you will set up a blue/green deployment strategy using AWS CodeDeploy for an existing AWS CodeCommit repository and AWS CodePipeline deployment. You will learn how to create a new deployment group, add an Application Load Balancer, and modify an existing deployment to perform blue/green deployments across two Amazon Elastic Compute Cloud (Amazon EC2) instances.

The lab’s web application uses an in-place deployment on two EC2 instances. The current issue is that every time you deploy the application, you encounter a downtime of the EC2 instances. Your goal is to implement a blue/green deployment that will avoid the downtime.

## Objectives

By the end of this lab, you should be able to do the following:

Create an AWS CodeDeploy deployment group to perform blue/green deployments.
Modify an existing AWS CodePipeline to incorporate a new blue/green deployment configuration.
Run a blue/green deployment, observe the deployment process, and verify the results.
Technical knowledge prerequisites
This hands-on lab assumes that you completed the Cloud Operations 1 (CO1) course and associated labs.

Duration
This lab requires approximately 90 minutes to complete.

Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose of each icon:

 Caution: Information of special interest or importance (not so important to cause problems with the equipment or data if you miss it, but it could result in the need to repeat certain steps).
 Command: A command that you must run.
 Expected output: A sample output that you can use to verify the output of a command or edited file.
 File contents: A code block that displays the contents of a script or file you need to run that has been pre-created for you.
 Note: A hint, tip, or important guidance.
 Task complete: A conclusion or summary point in the lab.
 Warning: An action that is irreversible and could potentially impact the failure of a command or process (including warnings about configurations that cannot be changed after they are made).
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
Amazon EC2
Amazon Elastic Compute Cloud (Amazon EC2) provides on-demand, scalable computing capacity in the AWS Cloud. Using Amazon EC2 reduces hardware costs, so you can develop and deploy applications faster. You can use Amazon EC2 to launch as many or as few virtual servers as you need, configure security and networking, and manage storage. You can add capacity (scale up) to handle compute-heavy tasks, such as monthly or yearly processes, or spikes in website traffic. When usage decreases, you can reduce capacity (scale down) again.

AWS Cloud9
AWS Cloud9 is a cloud-based integrated development environment (IDE) that lets you write, run, and debug your code with a browser. It includes a code editor, debugger, and terminal. AWS Cloud9 comes prepackaged with essential tools for popular programming languages, including JavaScript, PHP, Python, and more, so you don’t need to install files or configure your development machine to start new projects.

AWS CodeCommit
AWS CodeCommit is a fully managed source control service that hosts secure Git-based repositories. It makes it easy for teams to collaborate on code in a secure and highly scalable ecosystem. CodeCommit removes the need to operate your own source control system or worry about scaling its infrastructure. You can use CodeCommit to securely store anything from source code to binaries, and it works seamlessly with your existing Git tools.

AWS CodeDeploy
AWS CodeDeploy is a fully managed deployment service that automates software deployments to various compute services, such as Amazon EC2, Amazon Elastic Container Service (Amazon ECS), AWS Lambda, and on-premises servers. You can use CodeDeploy to automate software deployments, removing the need for error-prone manual operations.

AWS CodePipeline
AWS CodePipeline is a continuous delivery service that you can use to model, visualize, and automate the steps required to release your software. You can quickly model and configure the different stages of a software release process. CodePipeline automates the steps required to release your software changes continuously.

Task 1: Review the existing pipeline and web application
In this task, you will become familiar with the current lab environment’s infrastructure, which uses CodePipeline to deploy a web application. The application is deployed on two EC2 instances in an Auto Scaling group. There is also an Application Load Balancer that distributes the traffic to the instances.

Task 1.1: Review the existing pipeline
To begin, you will review the existing deployment pipeline for the web application to understand how the pipeline is triggered and how the deployment process works.

At the top of the AWS Management Console, in the search box, search for and choose CodePipeline.

On the Pipelines page, choose Web-App-Pipeline.

In the Source section, choose View details to open a pop-up box with the title Action execution details.

Choose the View in CodeCommit link to display the application’s code repository.

In the left navigation pane, under Repositories, choose Code.

 Note: If the left navigation pane is not visible, choose the menu icon  in the top-left corner to reveal it.

The page displays the web-app repository’s files. The deployment pipeline is triggered every time new code changes are pushed to the main branch of this repository. Later in the lab, you will make changes to the code in the AWS Cloud9 IDE and push to this repository to trigger a new deployment.

Close the current browser tab.

Close the Action execution details pop-up box, if it is open.

Ensure that the Web-App-Pipeline page is open in CodePipeline.

In the Deploy section, choose View details to open the Action execution details pop-up box.

Choose the View in CodeDeploy link. This opens a new tab with a page that displays the deployment’s details.

Find the Deployment details section, and then locate the Deployment group setting.

Under the Deployment group setting, choose the link to open the deployment group page.

In the Deployment group details section, locate the following settings:

Deployment type: In-place
Deployment configuration: CodeDeployDefault.AllAtOnce
The issue is that these deployment settings introduce a downtime of the website every time a deployment occurs. Here is why.

The In-place deployment type updates the existing instances with the new version of the application. Instead of creating new instances, it stops the application on the current instances, deploys the new version, and then restarts the application. This can lead to downtime because the application is temporarily unavailable on all instances during the deployment.
The CodeDeployDefault.AllAtOnce configuration deploys the new version of the application to all instances simultaneously. This means that all instances are updated at the same time, which can result in downtime if something goes wrong during the deployment process.
To prevent this downtime from happening, you will implement a blue/green deployment.

Task 1.2: Review the Application Load Balancer and Auto Scaling group
In this task, you will review the existing Application Load Balancer and Auto Scaling group. Understanding the existing infrastructure is crucial to avoiding misconfigurations when you make changes like a blue/green deployment.

At the top of the AWS Management Console, in the search box, search for and choose EC2.

In the left navigation pane, under Load Balancing, choose Load Balancers.

 Note: If the left navigation pane is not visible, choose the menu icon  in the top-left corner to reveal it.

Choose the web-app-alb load balancer to open the load balancer details page.

In the Listeners and rules (1) section, find and choose the web-app-alb-target-group link.

In the Registered targets (2) section, locate the instance IDs of the two instances that are registered to the target group. These are the two EC2 instances that the website is currently deployed on.

In the left navigation pane, under Auto Scaling, choose Auto Scaling Groups.

Choose web-app-asg.

In the Group details section, note that Desired capacity, Minimum capacity, and Maximum capacity are set to 2. This means that the Auto Scaling group creates two EC2 instances.

Choose the Instance management tab. The Instances (2) section displays a list of the two instances on which the website is deployed.

Keep the current tab open so you can easily return to view the instance IDs. You will reinspect these instance IDs in the next task. You can also copy the instance IDs and paste them into a text editor.

Task 1.3: Review the website
Copy the LoadBalancerUrl value that is listed to the left of these instructions, and then navigate to the URL in a new browser tab.
You will see the initial deployed version of the website. The webpage displays the Deployment number, which is currently 1, since this is the initial deployment. It also shows the EC2 Instance ID, which is the ID of the instance that the webpage is hosted on.

Choose your browser’s refresh button to reload the webpage. When you refresh the page, the EC2 Instance ID changes.

 Note: You might need to refresh the webpage a few times for this to happen.

The instance ID changes because there is an Auto Scaling group with two EC2 instances, and a load balancer that directs traffic to either of the two instances.

Reinspect the two instance IDs from the previous task to ensure that they match the instance IDs displayed on the website. This behavior demonstrates that the load balancer successfully directs traffic to either of the two instances.
 Task complete: You successfully reviewed the deployed website and the lab environment’s initial infrastructure, which includes AWS CodePipeline, an Application Load Balancer, and an Auto Scaling group.

Task 2: Configure AWS CodeDeploy for blue/green deployment
In this task, you will configure AWS CodeDeploy for a blue/green deployment. This includes creating a new deployment group, configuring its deployment settings, and adding the deployment group to the existing pipeline. A blue/green deployment creates new instances (the “green” environment) to replace the existing instances (the “blue” environment) without any downtime.

Task 2.1: Create a new deployment group
In this task, you will start by creating a new group in CodeDeploy that will manage the blue/green deployment. This group will use a different strategy than the current one, which updates all instances at once and can cause downtime. You will specify settings for the new deployment group, such as how traffic will be rerouted from the old instances to the new ones, and when to terminate the old instances after the new ones are running successfully.

At the top of the AWS Management Console, in the search box, search for and choose CodeDeploy.

In the left navigation pane, under Deploy, choose Applications.

Choose web-app.

On the web-app application page, find the Deployment groups section.

The listed deployment group is for the current in-place deployment. You will create a new deployment group for your blue/green deployment.

Choose Create deployment group.

For Deployment group name, enter blue-green-deployment-group.

For Service role, choose the only option available on the list.

 Note: This is a preexisting service role that is used for the current in-place deployment group. The service role grants AWS CodeDeploy the necessary permissions to perform deployment operations, such as managing EC2 instances and updating Auto Scaling groups. It ensures secure operations by restricting actions to only those required for the deployment process. There is no need to create a new service role, so you can reuse this service role.

For deployment type, choose Blue/green.

In the Environment configuration section, complete the following:

Choose Automatically copy Amazon EC2 Auto Scaling group.
Select web-app-asg in the list box.
In the Deployment settings section, complete the following:

For Traffic rerouting, choose I will choose whether to reroute traffic. This option gives you control over when to reroute traffic from the old instances to the new instances. It allows you to verify that the new instances are working correctly before directing user traffic to them, ensuring a seamless transition without downtime.

In the Hours list, select 1.
Ensure Days and Minutes are set to 0.
For instance termination, choose Terminate the original instances in the deployment group. By choosing to terminate the original instances, you ensure that only the new instances will be running after the deployment. This helps in resource management and cost optimization by automatically shutting down the old instances that are no longer needed.

In the Hours list, select 1.
Ensure Days and Minutes are set to 0.
For Deployment configuration, make sure CodeDeployDefault.AllAtOnce is selected. This configuration updates all new instances simultaneously, making the deployment process faster. Since the new instances are tested before traffic is rerouted, this configuration does not risk downtime, unlike an in-place deployment.

In the Load balancer section, complete the following:

For Load balancer type, select Application Load Balancer or Network Load Balancer.
In the Choose target groups list box, select web-app-alb-target-group.
Finally, choose Create deployment group.

A banner displays the message Deployment group created.

Task 2.2: Add the new deployment group to AWS CodePipeline
You will now integrate the new blue/green deployment group into the existing CodePipeline. This involves editing the deployment stage to replace the current deploy action with the new blue/green deployment action. This means that any new changes pushed to your code repository will trigger a blue/green deployment, ensuring that your application is updated with zero downtime.

In the left navigation pane, under Pipeline, choose Pipelines.

 Note: If the left navigation pane is not visible, choose the menu icon  in the top-left corner to reveal it.

Choose Web-App-Pipeline.

Choose Edit.

In the Edit: Deploy section, choose Edit stage to edit the deploy stage.

Choose X to remove current deploy action.

Choose + Add action group.

In the Edit action form, complete the following:

For Action name, enter BlueGreenDeploy. This specifies a unique name for the new deployment action in the pipeline.
For Action provider, select AWS CodeDeploy. This designates AWS CodeDeploy as the service responsible for handling the deployment action.
For Input artifacts, select SourceOutput. This selects the output from the source stage (the code repository) as the input for this deployment action.
For Application name, select web-app. This identifies the specific application in CodeDeploy that will be updated.
For Deployment group, select blue/green-deployment-group. This specifies the deployment group configured for blue/green deployment, ensuring the new strategy is used.
Choose Done.
In the Edit: Deploy section, choose Done.

 Warning: On the top of the page, choose Save to activate a Save pipeline changes confirmation pop-up box, but DO NOT choose Save in the pop-up box yet.

In the pop-up box, find the Change type and Details column. It looks like the following:

Change type	Details
Add	Pipeline Web-App-Pipeline as a target to Amazon CloudWatch Events rule - codepipeline-webapp-main-xxxxxx-rule
This means that a new Amazon CloudWatch Events rule is created that detects new commits in the CodeCommit repository to trigger the pipeline. You DO NOT want this to happen, because the pipeline already has a preexisting CloudWatch Events rule. Adding a second rule would trigger the pipeline twice.

 Warning: To prevent the creation of a duplicate CloudWatch Events rule, make sure you perform the next step.

Select the No resource updates needed for this source action change checkbox to make sure it is checked.

Choose Save.

A banner displays the message Pipeline was saved successfully.

 Task complete: You successfully created a new deployment group and added it to the pipepline.

Task 3: Run the blue/green deployment
In this task, you will make a change to the application code. Then, you will create a commit and push it to the CodeCommit repository to trigger a new deployment through the modified pipeline. Finally, you will observe the deployment process and verify that the application is deployed successfully.

Task 3.1: Make a change to the application’s repository
In this task, you will use AWS Cloud9 to create and push a new commit to your application’s CodeCommit repository.

To open the AWS Cloud9 environment, copy the Cloud9Environment URL value that is listed to the left of these instructions, and paste it into a new browser tab.

 Note: The browser displays the AWS Cloud9 environment that you will use in this lab.

In the AWS Cloud9 IDE, close the Welcome tab.

In the AWS Cloud9 IDE, open the web-app/app/index.html file.

 File contents: In the index.html file, find the following line:


<h2>Deployment number: 1</h2>
 Note: You can press Ctrl+F or Cmd+F to search for the line.

Replace the number 1 with 2, as shown here:


<h2>Deployment number: 2</h2>
Choose File, and then choose Save.

 Command: In the AWS Cloud9 terminal, to navigate to the web-app folder, run the following command:


cd web-app
 Expected output: None, unless there is an error.

 Command: In the AWS Cloud9 terminal, run the following command:


git status
 Expected output


******************************
**** This is OUTPUT ONLY. ****
******************************

modified:   app/index.html
 Command: In the AWS Cloud9 terminal, run the following command:


git add . && git commit -m 'change deployment number'
 Expected output


******************************
**** This is OUTPUT ONLY. ****
******************************

1 file changed, 1 insertion(+), 1 deletion(-)
 Command: In the AWS Cloud9 terminal, run the following command:


git push
 Expected output: You should see output similar to the following:


************************
**** EXAMPLE OUTPUT ****
************************

Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 2 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 452 bytes | 452.00 KiB/s, done.
Total 4 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Validating objects: 100%
To codecommit://web-app
xxxxxxx..xxxxxxx  main -> main
 Command: In the AWS Cloud9 terminal, run the following command:


git status
 Expected output


******************************
**** This is OUTPUT ONLY. ****
******************************

On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
Task 3.2 Observe and manage the new deployment
Now that you’ve pushed new changes to your AWS CodeCommit repository, AWS CodePipeline detects the change and automatically runs your pipeline.

At the top of the AWS Management Console, in the search box, search for and choose CodePipeline.

Choose Web-App-Pipeline.

The pipeline was triggered to run by your latest push to the CodeCommit repository, or it might take a moment for the trigger to occur.

Wait until the Deploy stage status is In progress.

In the Deploy stage section, choose View details. This opens a pop-up box titled Action execution details.

In the pop-up box, choose View in CodeDeploy to open the deployment details page.

Find the Deployment status section. This section displays the status as the deployment proceeds through Steps 1 through 4.

Wait until Steps 1 and 2 are complete and Step 3 is in progress.

Before you reroute the traffic to the newly created EC2 instances, verify that the website is running on the new instances.

Find the Deployment lifecycle events section. This section lists the original and replacement instances.

In the Instance ID column, choose the link of one of the replacement instances. This opens a new browser tab with the EC2 instances page.

In the Instance ID column, choose the link of the EC2 instance to open the instance summary page.

Find the Public IPv4 address of the EC2 instance.

Copy and paste this IP address into a new browser tab and visit the website.

 Caution: Do not choose the open address link, because that uses the https protocol, whereas the deployed website uses the http protocol.

You can see the website displaying the text Deployment number: 2. This confirms that the website has been successfully deployed on the replacement instance. Traffic is ready to be rerouted.

Copy the LoadBalancerUrl value that is listed to the left of these instructions, and paste it into a new browser tab.
The webpage displays the old Deployment number: 1. This is because traffic has not been rerouted yet. Next, you will reroute the traffic to the replacement instances.

Navigate to the CodeDeploy page for the current blue/green deployment. The page should be in one of your previous browser tabs.

Choose Reroute traffic.

A banner displays the message Traffic rerouting started.

Wait until Step 3 has succeeded and Step 4 changes its status to In progress. This can take up to 10 minutes.

Copy the LoadBalancerUrl value that is listed to the left of these instructions, and paste it into a new browser tab.

The newly deployed webpage displays the latest deployment number. The page also displays the Instance ID. This matches the ID of one of the replacement EC2 instances. You can verify this by making sure it matches the ID of the replacement instance, listed in the Deployment lifecycle events section on the deployment page.

Now that the traffic is successfully routed to the replacement instances, you can terminate the original EC2 instances.

On the deployment page, choose Terminate.

A banner displays the message Original instance termination has started.

Wait until Step 4 changes its status to Succeeded.

Finally, you will verify that the original EC2 instances are terminated.

At the top of the AWS Management Console, in the search box, search for and choose EC2.

Choose Instances (running) to navigate to the instances list.

Clear the Instance state = running filter, so you can see the terminated instances.

 Task complete: You successfully ran the blue/green deployment and verified that the original EC2 instances have been terminated.

Conclusion
 You successfully completed the following:

Created an AWS CodeDeploy deployment group to perform blue/green deployments.
Modified an existing AWS CodePipeline to incorporate a new blue/green deployment configuration.
Ran a blue/green deployment, observed the deployment process, and verified the results.
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End lab and then confirm that you want to end your lab.
