# Week 6: AWS Elastic Beanstalk Python Support

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to repo's main [README.md](../../../README.md)

## Review of Elastic Beanstalk

### Pre-assessment

#### What is AWS Elastic Beanstalk?

* A service for deploying and scaling web applications

Wrong answers:

* A database service for structured data
* A machine learning service for predictions
* A storage service for files and objects

#### AWS Elastic Beanstalk supports all of the following programming languages, except one. Which is the programming language that is not supported?

* C/C++

Wrong answers:

* Python
* Java
* Node.js

##### Explanation

* The most common web development languages and frameworks are supported by AWS Elastic Beanstalk, such as Java, .NET, PHP, Node.js, Python, Ruby, Go, and Docker.

* C/C++ is not supported on Elastic Beanstalk, although, C/C++ could be deployed inside Docker containers that you create.

#### How does AWS Elastic Beanstalk simplify the deployment of applications?

* By automatically handling details like resource provisioning, load balancing, scaling, and application health monitoring

Wrong answers:

* By providing a graphical interface to manually configure underlying resources
* By letting you write infrastructure as code to define resources
* By giving you root access to Amazon EC2 instances running the application

## Benefits and Concepts of Elastic Beanstalk

### Elastic Beanstalk

AWS Elastic Beanstalk is a service that provides an environment to deploy, scale, and manage applications on AWS. With Elastic Beanstalk, developers can quickly upload applications and services without worrying about the infrastructure that runs those applications. Elastic Beanstalk automatically scales compute resources, balances loads, and monitors application health.

To use Elastic Beanstalk, you create an application and package it in a source bundle. You then upload the bundle to Elastic Beanstalk and provide some information about the application. Elastic Beanstalk automatically launches an environment and creates and configures the AWS resources needed to run your code. After your environment is launched, you can then manage your environment and deploy new application versions.

By handling infrastructure provisioning, application version deployment, capacity provisioning, load balancing, scaling, and application health monitoring, Elastic Beanstalk reduces management complexity and operational costs for developers. This lets developers focus on writing code rather than managing infrastructure. Elastic Beanstalk supports a variety of programming languages, including Python, Java, .NET, Node.js, PHP, Ruby, Go, and Docker. It also integrates with developer tools such as AWS CodePipeline to support continuous deployment.

#### [AWS Elastic Beanstalk Features](https://aws.amazon.com/elasticbeanstalk/details/)

### Key benefits

* **Quick deployment**: Get Python applications up and running quickly without manually setting up servers or infrastructure. Just upload code, and Elastic Beanstalk handles deployment.
* **Auto scaling**: Elastic Beanstalk scales Python application instances up and down to meet demand. This handles spikes in traffic without intervention.
* **Multiple environments**: Create different environments like development, test, and production for application lifecycle management.
* **Code focus**: Focus on writing code rather than infrastructure. Elastic Beanstalk handles all the servers, load balancing, and monitoring.
* **Pricing**: There is no additional charge for Elastic Beanstalk. You only pay for the underlying AWS resources that your application consumes.

### Typical use cases

Elastic Beanstalk is commonly used for web applications, API backends, and simple queue or batch processing tasks.

Typical use cases include the following:

* Quickly deploy Python web applications without managing the underlying infrastructure.
* Host Python Web Server Gateway Interface (WSGI) and Flask applications. Elastic Beanstalk provides preconfigured Python platforms that support popular Python web frameworks.
* Deploy machine learning models and Python data-processing scripts as web services with very little configuration.
* Select Elastic Beanstalk as the deployment destination of continuous integration and continuous delivery (CI/CD) pipeline builds. AWS CodePipeline supports Elastic Beanstalk and a deployment action.

Elastic Beanstalk boosts developer productivity by reducing time spent on infrastructure management.

### Concepts

Your application needs several compute, storage, and networking resources. Elastic Beanstalk makes it possible for you to manage these resources by grouping them as environments. To learn more about key Elastic Beanstalk concepts, expand each of the following categories.

#### Application

An Elastic Beanstalk **application** is a logical collection of Elastic Beanstalk components, including environments, versions, and environment configurations. In Elastic Beanstalk, an application is conceptually similar to a folder.

#### Application version

In Elastic Beanstalk, an **application version** refers to a specific, labeled iteration of deployable code for a web application. An application version points to an Amazon Simple Storage Service (Amazon S3) object that contains the deployable code, such as a Java WAR file. An application version is part of an application.

Applications can have many versions, and each application version is unique.

#### Environment

An **environment** is a collection of AWS resources running an application version. Each environment runs only one application version at a time. However, you can run the same application version or different application versions in many environments simultaneously.

#### Environment tier

The **environment tier** designates the type of application that the environment runs, and determines what resources Elastic Beanstalk provisions to support it. For example, an application that serves HTTP requests runs in a web server environment tier.

There are two types of environment tiers:

* **Web server environment**: Run a website, web application, or web API that serves HTTP requests.
* **Worker environment**: Run a worker application that processes long-running workloads on-demand or performs tasks on a schedule.

#### Environment configuration

An **environment configuration** identifies a collection of parameters and settings that define how an environment and its associated resources behave. When you update an environment’s configuration settings, Elastic Beanstalk automatically applies the changes to existing resources or deletes and deploys new resources (depending on the type of change).

#### Saved configuration

A **saved configuration** is a template that you can use as a starting point for creating unique environment configurations.

#### Platform

A **platform** is a combination of an operating system, programming language runtime, web server, application server, and Elastic Beanstalk components. You design and target your web application to a platform.

To work with Elastic Beanstalk, you have to pick an **AWS Region**, like **us-east-2**. You start by creating an application as a placeholder. You need to give it a name, like **pets-app**. When you have an application, you need at least one **environment**. For instance, two environments exist, called **pets-env-blue** and **pets-env-green**. Each environment has its own **configuration** and **platform**. Each environment also points to a specific **application version**. If **pets-env-blue** is your production environment, you can use **pets-env-green** for testing. You can upgrade both the platform and the application version to perform some testing before using it as your new production environment. Next time, **pets-env-blue** becomes the test environment. This is called blue-green deployment, and it is fully supported by Elastic Beanstalk.

## Elastic Beanstalk Web Server Environment Architecture

### Web server environment

A **web server environment** tier is made of components including a load balancer and several Amazon Elastic Compute Cloud (Amazon EC2) instances.

As you create a new web server environment, Elastic Beanstalk provisions networking, compute, and security resources for you.

An **Application Load Balancer (ALB)** from the Elastic Load Balancing (ELB) service routes all the incoming HTTP requests. Clients do not call the load balancer's URL directly, as in **abcd-1234.us-west-2.elb.amazonaws.com**. Instead, Elastic Beanstalk registers a Canonical Name Record (CNAME) in DNS. That record maps one domain name to the load balancer's URL. It acts as an alias record, so clients can call, for instance, **pets-app.elasticbeanstalk.com**. Note that you can reconfigure the CNAME to point to a different ALB in a different environment, which allows blue-green deployments.

The load balancer routes the requests to an Amazon EC2 Auto Scaling group. The group includes instances whose quantity dynamically grows and shrinks based on the traffic load. Adding and removing servers is called horizontal scaling.

Each **EC2 instance** is provisioned by Elastic Beanstalk with a predefined **platform** based on the environment configuration. A stack of software is available for a certain type of web application to run. It can support a particular Python version, for instance.

Each **EC2 instance** has an Elastic Beanstalk process running. It is called a **host manager**. It acts as an agent running commands locally. The Elastic Beanstalk service acts as a controller and calls the local host manager to deploy a new version of an application on that EC2 instance. The host manager is also called to patch the platform. In addition, the host manager has an important role related to monitoring and reporting. It aggregates events and metrics, monitors the application logs for critical errors, monitors the application server part of the platform, and rotates and exports logs to Amazon S3.

### Security

The EC2 instances' network interfaces are protected by a firewall called a **security group**. By default, Elastic Beanstalk allows inbound HTTP traffic in the security group. This is exactly what is needed for an HTTP request routed by the load balancer to arrive at one of the instances and be handled by your web application. This default configuration is appropriate when your load balancer terminates HTTPS. Externally, the connection between the clients and the load balancer is secure. Internally, the connection between the load balancer and the instance is not encrypted. Instead, end-to-end encryption requires the use of configuration files to modify the software running on the instances and to modify the security group to allow secure connections. In that case, the instances would terminate HTTPS.

Your application can make use of other AWS services. Using such APIs requires credentials. The provisioned instances have an instance profile with an **AWS Identity and Access Management (IAM) role**. A role lists the policies to perform actions against the different AWS services.

An IAM role defines what actions are allowed and denied from these instances.

### Persistent storage

Amazon EC2 instances are managed by Elastic Beanstalk. They are instantiated and terminated automatically. It means that whatever your application is storing on the local file system will be lost when the instance disappears. Application data and application logs must be stored externally to Elastic Beanstalk to make them persistent.

Your application can make use of several storage and database services. But for such integration to work properly, extra policies are required in the IAM role attached to the instances.

An Elastic Beanstalk application can make use of an external AWS service to persist data. Amazon S3, Amazon EFS, Amazon CloudWatch, Amazon DynamoDB and Amazon RDS can be integrated.

The integration between your Elastic Beanstalk application and AWS services can be applied at different levels.

* **Built-in Amazon S3 integration** – You can configure your Elastic Beanstalk environment to enable application log rotation and to publish logs automatically to Amazon S3 after they are rotated. This is performed by the **host manager**. The bucket name is preprovisioned and is called **elasticbeanstalk-<region>-<account-id>**.
* **Built-in Amazon CloudWatch integration** – Elastic Beanstalk installs a **CloudWatch log agent** with the default configuration settings on each instance that it creates. You can enable instance log streaming to Amazon CloudWatch Logs. From CloudWatch, subscription filters can be created to stream logs to AWS Lambda or Amazon Kinesis.
* **Elastic Beanstalk resource creation** – Configuration files under the **.ebextensions** folder of your project are used to declare extra AWS resources that must be created automatically when an environment is created. You can declare an Amazon DynamoDB table and an Amazon Elastic File System (Amazon EFS) file system. For the latter, the file system is automatically mounted to the EC2 instances. Note that these extra resources are not tied to your environment's lifecycle. They are not deleted when you terminate your environment because they might contain important customer data.
* **AWS SDK for Python** – Your application can programmatically use the Software Development Kit (SDK) to make calls to the AWS service APIs. Any service can be called, so the possibilities are endless.
* **Framework integration** – Instead of directly coding with the SDK, your application could be based on a framework that has built-in support for some AWS services. For instance, Django allows you to store application media files on Amazon S3 through configuration. This is an easier approach in terms of integration and maintenance.

## Using Elastic Beanstalk with the CLI

### CLI purpose and usage

Elastic Beanstalk provides a command line interface (EB CLI) to create, manage, and monitor environments. The EB CLI integrates with Git to support version control and deployment of applications. To use the EB CLI, first install it on your local machine, and then initialize the EB CLI to integrate it with your AWS account.

After initialization, you can create environments, deploy applications, manage environments, and monitor logs right from the CLI. For example, you can use commands like eb init, eb create, and eb deploy to manage environments. With the EB CLI, you can work with Elastic Beanstalk from your local terminal.

Key benefits are version control integration and streamlined environment management without switching between the CLI and console.

#### [Using the Elastic Beanstalk Command Line Interface](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3.html)

### Installation

The Elastic Beanstalk dedicated CLI can be installed into your IDE with the following command. You install a Python package called **awsebcli**. Installing this package makes the **eb** command available in your terminal.

```bash
pip install awsebcli
```

All **eb** commands should be run in the top-level directory of the Python project (the parent directory of the **.ebextensions** folder). This identifies which application you are deploying to Elastic Beanstalk.

### Common CLI commands and options

The EB CLI provides commands for creating, configuring, and monitoring Elastic Beanstalk environments.

Some common commands include the following.

* **eb init** - Initializes your directory with Elastic Beanstalk. This sets up your environment for creating new applications and environments.
* **eb create** - Creates a new environment and deploys an application version to it. You specify options like AWS Region, environment name, solution stack, and instance type.
* **eb status** - Shows health and status information about your environment. This allows you to monitor your environment.
* **eb deploy** - Deploys your application source bundle to the environment. This updates the environment with your latest code.
* **eb config** - Modifies an environment's configuration settings. For example, you can adjust auto scaling, swap solution stacks, or update environment variables.
* **eb terminate** - Terminates and deletes a running environment. Use this to permanently delete an environment and terminate associated resources.

### Knowledge Check

#### How does AWS Elastic Beanstalk simplify application version management over time?

* By allowing you to roll back to previous versions

Wrong answers:

* By maintaining multiple environments for each version
* By automatically incrementing version numbers
* By storing application artifacts in Amazon S3

#### Which tool can you use to deploy a Python application to AWS Elastic Beanstalk from the command line?

* EB CLI

Wrong answers:

* AWS CloudFormation
* AWS CodeDeploy
* AWS CodePipeline

#### Which AWS services can you use along with AWS Elastic Beanstalk?

* Amazon RDS 

Wrong answers:

* AWS Lambda
* Amazon SageMaker
* AWS Fargate

Amazon RDS can be used as a relational database service and integrates with AWS Elastic Beanstalk.

#### A Django application is about to be deployed on AWS Elastic Beanstalk. Which CLI command can be used to setup a new environment and install the current application version to it?

* eb create

Wrong answers:

* eb deploy
* eb init
* eb status

### Summary

You learned about the key concepts and benefits of using AWS Elastic Beanstalk to deploy and manage web applications. Key topics included deploying and managing applications without worrying about the infrastructure. This module also covered automatically scaling application resources based on demand, and Elastic Beanstalk support for popular programming platforms such as Java, .NET, PHP, Node.js, Python, Ruby, Go, and Docker.

You learned about the Elastic Beanstalk Command Line Interface (EB CLI), and common eb commands for operations like creating environments, deploying code, monitoring environments, and terminating environments. 

With Elastic Beanstalk, you can focus more on coding applications and less on managing servers. Continue to the next topic to learn about deploying Python applications with Elastic Beanstalk.

## Elastic Beanstalk Python Platform and Tools

### Pre-assessment

#### A Python application deployed in Elastic Beanstalk is using the AWS SDK to read from an Amazon DynamoDB table. Which mechanism is used to allow this action?

* Attach the corresponding IAM policy to the EC2 instance profile

Wrong answers:

* Add an outbound rule to the Elastic Beanstalk security group
* Use an IAM user and password in the code
* Configure the Amazon DynamoDB table

For the code to work, the EC2 instances running the Python application need to have an instance profile with an IAM role. That role must include an IAM policy that allows the read action on the Amazon DynamoDB table resource.

#### Which Python platform versions are supported by AWS Elastic Beanstalk?

* A list of specific Python platform versions

Wrong answers:

* All existing Python platform versions
* Only Python 3.9
* Only Python 3.11

For more information, visit the [Python-based supported platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-supported.html#platforms-supported.python).

#### Which file do you include in your Python application source bundle to specify application dependencies installed by AWS Elastic Beanstalk?

* requirements.txt

Wrong answers:

* config.yml
* .ebextensions
* setup.py

The requirements.txt file lists the Python dependencies for your application that Elastic Beanstalk will install when building the applications environment.

## Using Elastic Beanstalk with the SDK for Python

You can use the AWS SDK for Python (Boto3) in your Python application to call AWS services, such as Amazon DynamoDB and Amazon S3. You programmatically access these services through a client interface instead of making direct calls to service endpoints. In this section, you will focus on how to use the SDK in Elastic Beanstalk.
