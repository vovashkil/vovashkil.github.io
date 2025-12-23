# Deploying Containers on AWS Fargate Using Amazon ECS and Amazon ECR

* back to AWS Cloud Institute repo's root [aci.md](../../aci.md)
* back to [AWS Cloud Fundamentals 2](../aws-cloud-fundamentals-2.md)
* back to repo's main [README.md](../../../../README.md)

## Lab overview

* ECR Container URI: 323017510454.dkr.ecr.us-west-2.amazonaws.com/url-checker:latest

In this hands-on lab, you learn how to build, deploy, and run containerized applications on Amazon Web Services using Amazon Elastic Container Service (Amazon ECS), Elastic Container Registry (Amazon ECR), and Fargate.

You walk through the steps to set up an ECS cluster, define task definition, and launch containers on Fargate. Fargate is a serverless compute engine for containers that allow you to run containers without having to manage any Amazon Elastic Compute Cloud instances.

This demonstrates the automation and scalability of running containers in AWS without provisioning or managing servers. You gain the foundational knowledge to containerize your applications and deploy them on ECS using ECR and Fargate.

The skills you learn enable you to easily build, deploy, and scale containerized applications in AWS. Experience with core AWS container services serve as the building blocks for running modern microservices architectures.

Objectives
By the end of this lab, you should be able to the following:

Locate the container image in Amazon Elastic Container Registry (Amazon ECR).
Author task definitions to describe your application containers.
Create an Amazon Elastic Container Service (Amazon ECS) cluster to run tasks and services.
Add the containerized tasks to the cluster on Fargate.
Technical knowledge prerequisites
This lab requires the following:

Basic knowledge of Amazon ECR for storing and retrieving Docker container images
Familiarity with Amazon ECS concepts like clusters, tasks, task definitions, and services
Duration
This lab requires approximately 60 minutes to complete.

Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Expected output: A sample output that you can use to verify the output of a command or edited file
 Note: A hint, tip, or important guidance.
 Task complete: A conclusion or summary point in the lab
Start lab
To launch the lab, at the top of the page, choose Start Lab.

 Caution: You must wait for the provisioned AWS services to be ready before you can continue.

To open the lab, choose Open Console .

You are automatically signed in to the AWS Management Console in a new web browser tab.

 Warning: Do not change the Region unless instructed.

Common sign-in errors
Error: Choosing Start Lab has no effect
In some cases, certain pop-up or script blocker web browser extensions might prevent the Start Lab button from working as intended. If you experience an issue starting the lab:

Add the lab domain name to your pop-up or script blocker’s allow list or turn it off.
Refresh the page and try again.
Services used in this lab
Amazon Elastic Container Registry
Amazon Elastic Container Registry (Amazon ECR) is a fully managed container registry offering high-performance hosting, so you can reliably deploy application images and artifacts anywhere.

Amazon Elastic Container Service
Amazon Elastic Container Service (ECS) is a fully managed container orchestration service that helps you to more efficiently deploy, manage, and scale containerized applications. It deeply integrates with the AWS environment to provide an easy-to-use solution for running container workloads in the cloud and on premises.

AWS Fargate
AWS Fargate is a technology for Amazon ECS that allows you to run containers without having to manage the underlying EC2 instances. With Fargate, you no longer have to provision, configure, or scale clusters of virtual machines to run containers. This removes the overhead of infrastructure management and allows you to focus on building and operating your applications. Fargate helps scale containerized workloads easily and cost-effectively.

Task 1: Locate the container image in Amazon ECR
In this task, you locate the container image in Amazon Elastic Container Registry (ECR) to be used for your application. This image has already been built and pushed to ECR as part of the pre-provisioned environment. Locate the image URI referenced when creating your task definition in an upcoming step.

At the top of the AWS Management Console, in the search bar, search for and choose Elastic Container Registry.

Notice the url-checker repository available.

To access the images in the repository, select the url-checker link.

Notice an image with the image tag latest.

To access the image details, select the latest link.

Record the URI of the image in a text editor of your choice. You reference this in the following task.

The URI should be similar to:

AccountID.dkr.ecr.us-west-2.amazonaws.com/url-checker:latest

 Task complete: You have successfully located the container image in ECR. You now have the image URI needed to reference this image when creating your task definition. You use this URI in the next step as you define the task and container details.

Task 2: Create a task definition
In this task, you create an ECS task definition. The task definition specifies details about a containerized application like the Docker image, CPU and memory requirements, environment variables, and network settings. Task definitions make it easy to deploy and update containers predictably.

At the top of the AWS Management Console, in the search bar, search for and choose Elastic Container Service.

From the left navigation, select Task definitions.

Select Create new task definition .

On the Create new task definition page,

In the Task definition configuration section:

For Task definition family, enter url-checker.
In the Infrastructure requirements section:

For Launch type, verify that AWS Fargate is selected.

In the Task size sub-section:

For CPU, use the dropdown menu and select .5 vCPU.
For Memory, use the dropdown menu and select 1 GB.
In the Container - 1 section, under Container details:

For Name, enter url-checker.
For Image URI, paste the URI copied earlier to the text editor.
In the Logging - optional section, verify that Use log collection is selected. This writes the results of the container log to Amazon Cloudwatch.

In the Docker configuration - optional section:

Under Command, enter:

https://aws.amazon.com,https://expired.badssl.com,https://self-signed.badssl.com

 Note: By providing the URLs in this section, the URLs are being passed as command-line arguments to the application when the task is launched. This allows the application to know which URLs to check.

Leave all other settings at the defaults.

Choose Create.

 Expected output:  Task definition successfully created message is displayed at the top of the page.

 Task complete: You have successfully created the task definition for your containerized application. Defining the task definition is an important step in deploying scalable containerized services on AWS. The task definition allows you to reliably run and manage your containers.

Task 3: Create an Amazon ECS cluster
In this task, you create an ECS cluster. An ECS cluster provides the infrastructure needed to run your containerized tasks and services. When using Fargate, the cluster automatically provisions the underlying compute resources needed to run your containers.

From the left navigation, select Clusters.

Choose Create cluster.

In the Cluster name field, type lab-cluster-fargate.

In the Infrastructure section, verify that AWS Fargate (serverless) is selected.

At the bottom of the page, choose Create.

 Expected output: The message Cluster creation is in progress displays at the top of the page. It may take a few minutes for the cluster to create. Once the creation of the cluster completes, a message displays  Cluster lab-cluster-fargate has been created successfully and the cluster is now listed.

 Task complete: You have successfully created the ECS cluster. You now have the infrastructure in place to run your containerized workloads. Defining the cluster is a crucial step in being able to deploy containers using Amazon ECS and Fargate.

Task 4: Create and configure an ECS Service
In this task, you create a service that will maintain and run your url-checker application. The url-checker application will run on ECS using the infrastructure previously created. The ECS task definition previously created contains the configuration for the url-checker application. The cluster previously created provides the compute infrastructure to deploy the url-checker application.

Choose the lab-cluster-fargate link.

From the cluster page, select the Services tab.

Choose Create.

In the Compute configuration section:

For Compute options choose Launch type.
Ensure FARGATE is selected for Launch type.
In the Deployment configuration section:

For Task definition family, select url-checker from the drop-down menu. The LATEST revision is chosen.
For Service name, enter url-checker-service.
In the Networking section:

For VPC, choose Lab VPC from the drop-down menu.

For Security group, choose Create a new security group. This will then ask for the following values:

In the Security group name field, enter URLCheckerAppSecurityGroup.
In the Security group description field, enter My URL Checker Security Group.
For Type, choose HTTP from the drop-down menu.
For Source, choose Anywhere from the drop-down menu.
Verify Public IP is turned on.

Leave everything else on this page at default.

Choose Create.

The provisioning of the service begins.

Task 5: Monitor the service and view results
In this task, you verify the service is running and view the application output.

On the cluster page, select the Services tab.

Choose the url-checker-service link.

You may need to click the refresh  button for the link to appear.

Choose the Tasks tab.

Note: You will notice a task being created and run. Its status will change from PENDING to RUNNING to STOPPED.

Once the task has STOPPED, choose the task ID to view details.

Note: You may notice a message stating “Essential container in task exited”. This is expected behavior as our application is designed to run once and exit.

Choose the Logs tab to view the application output.

 Expected output: The CloudWatch logs show the output from a containerized application called url-checker that is checking URLs and logging the results.

The logs show the timestamp, the URL checked along with the response code if successful or the error if there was an issue, and the container name. This provides visibility into the application’s execution and logs any errors encountered while checking URLs.

 Task complete: You have successfully created an ECS service powered by Fargate. In this lab you created a task definition, ECS cluster, and added a task to the cluster. By leveraging Fargate, you were able to run containers easily without provisioning any servers. Great job completing this hands-on lab and learning how to use ECS and Fargate to deploy containerized workloads.

### Conclusion

You now have successfully done the following:

* Located the container image in Amazon ECR
* Authored a task definition to describe your application containers
* Created an Amazon ECS cluster to run tasks and services
* Added the containerized tasks to the cluster on Fargate

### End lab

Follow these steps to close the console and end your lab.

29. Return to the **AWS Management Console**.
30. At the upper-right corner of the page, choose **AWSLabsUser**, and then choose **Sign out**.
31. Choose **End Lab** and then confirm that you want to end your lab.

### Additional resources

* [What is Amazon Elastic Container Service?](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html)
* [What is Amazon Elastic Container Registry?](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html)
