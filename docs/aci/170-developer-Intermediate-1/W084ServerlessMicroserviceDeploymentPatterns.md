# Week 8: Serverless Applications – Microservice Deployment Patterns

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to repo's main [README.md](../../../README.md)

## Microservice Deployment Patterns

### Pre-assessment

#### Which statement about serverless microservice deployments is true?

* Serverless deployments abstract away the underlying infrastructure, such as servers and operating systems, and handle deployment tasks like scaling and provisioning automatically.

Wrong answers:

* Serverless deployments communicate directly through the local hypervisor to reduce network connectivity issues.
* Serverless deployments are used for small workloads that don't require a lot of CPU, memory, or storage usage.
* Serverless uses services such as AWS Fargate to scale up and down as needed.

#### Which deployment type uses lightweight virtualization to bundle code and dependencies, providing a more controlled and isolated environment for running applications?

* Container deployments

Wrong answers:

* Serverless deployments
* Physical on-premises deployments
* Thin-client deployments

##### Explanation

* **Container deployments** use lightweight virtual machines (VMs) that bundle code and dependencies, providing a more controlled and isolated environment for running applications.

The other options are incorrect because of the following reasons:

* Serverless deployments are a cloud computing model that allows developers to build and run applications without managing servers
* Thin-client deployments are normally used for desktop virtualization, shared services, or browser-based computing.
* Physical on-premises deployments are when an organization's software applications run on computers and servers located within the organization's physical premises.

#### Which use case is the MOST appropriate for serverless deployments?

* The application's requirements are dynamic and change frequently, requiring the services to scale dynamically.

Wrong answers:

* The application needs to be run from different locations or offline.
* The application requires many libraries and other dependencies.
* The application's traffic is predictable.

##### Explanation

The other options are incorrect because of the following reasons:

* Serverless deployments are not ideal when the application needs to be run from different locations or offline.
* The application requires many libraries and other dependencies is a more appropriate use case for a microservice deployment.
* The application's traffic is predictable is a more appropriate use case for reserved and provisioned capacity planning options.

## Serverless and Container-Based Deployments

### Serverless and container-based deployments

Serverless deployments abstract away the underlying infrastructure, such as servers and operating systems, and handle deployment tasks like scaling and provisioning automatically. Containers, on the other hand, were created to package and run applications in a predictable and repeatable way across multiple environments. Instead of recreating the environment, you packaged the application to run on all types of physical or virtual environments.

Serverless deployments pair well with event-driven applications, such as those that respond to form submissions, image processing, and Internet of Things (IoT) sensor events. With containers, you have more control over which features and software are deployed within a container image. For instance, you can deploy WordPress with containers, but not to AWS Lambda.

#### Serverless services

Some of the serverless services offered by AWS include the following:

* **AWS Lambda** is an event-based compute service that lets you run code without provisioning or managing servers.
* **Amazon Simple Storage Service (Amazon S3)** is an object storage service offering industry-leading scalability, data availability, security, and performance. 
* **Amazon DynamoDB** is a fully managed NoSQL database service that offers fast and predictable performance with seamless scalability.
* **Amazon API Gateway** is a fully managed service that makes it convenient to create, publish, monitor, and scale APIs. It provides a range of features, including API documentation, request and response validation, caching, and security. API Gateway supports RESTful and WebSocket APIs.
* **Amazon Simple Queue Service (Amazon SQS)** is a highly scalable, reliable, and fully managed message queuing service. You can store and retrieve messages in a distributed manner, making it suitable for use in distributed systems and applications.

#### Container services

Container-based services offered by AWS include the following

* **Amazon Elastic Container Service (Amazon ECS)** runs multiple containerized applications on a single Amazon Elastic Compute Cloud (Amazon EC2) instance or a fleet of EC2 instances. Amazon ECS can automatically scale your applications based on demand. 
* **Amazon Elastic Kubernetes Service (Amazon EKS)** runs Kubernetes applications in a highly available, scalable, and managed manner. Amazon EKS can also automatically scale your Kubernetes clusters based on demand.
* **AWS Fargate** runs containerized applications without provisioning or managing servers. Fargate is used with both Amazon ECS and Amazon EKS.

* [Serverless on AWS](https://aws.amazon.com/serverless/)

### When to choose serverless or container-based 

The serverless deployment method is suitable for applications that have bursty or unpredictable workloads, such as real-time analytics and IoT applications. It is also suitable for applications that require frequent deployments, because it can eliminate the need for manual infrastructure setup by using infrastructure as code (IaC).

The container-based deployment method uses containers to package and deploy applications at scale. Containers provide isolation and security, and they can be conveniently scaled up or down, based on the application's needs. Container-based deployments are suitable for applications that require high levels of scalability, reliability, and performance, such as web applications and applications that require complex dependencies.

### Serverless Microservices

Serverless microservices offer many benefits that can help organizations build, deploy, and manage scalable, flexible, and cost-effective cloud applications in the following ways:

* **Pay per use**: Eliminates the need to provision and manage servers, because the underlying infrastructure is managed by the cloud provider.
* **Scalability**: Effortlessly scales applications up or down based on demand. This means that applications can handle increased traffic or spikes in workload without requiring manual intervention or infrastructure changes.
* **Microservices architecture**: Promotes modularity, scalability, and flexibility. With microservices, teams can build and deploy independent services that communicate with each other through well-defined APIs, making it more convenient to manage and maintain complex applications.
* **Continuous delivery**: Empowers developers to continuously integrate their services, automate testing, and deploy them with a single click, promoting a DevOps culture and continuous improvement.
* **Cost optimization**: Optimizes cloud spending by eliminating the need to provision and manage infrastructure for idle services.
* **Focus on business value**: Allows organizations to focus on building and delivering business value, rather than managing infrastructure. With this shift in focus, developers can spend more time on writing code and less time on operational tasks, leading to increased efficiency and productivity.
* **Resilience and fault tolerance**: Allows applications to continue to operate, even in the event of infrastructure failures.
* **Continuous innovation**: Helps organizations to quickly prototype and experiment with new ideas and technologies. With serverless microservices, developers can quickly spin up new services, test them in production, and iterate on their ideas without the need for lengthy infrastructure setups.

### Architectural pattern for microservices with Lambda

In a serverless microservice architecture, each of the application components are decoupled and independently deployed and operated. An API created with Amazon API Gateway acts like the front door for your application, accepting API calls from API consumers. The requests are sent to the serverless compute service, AWS Lambda, where your application logic lives, and functions are subsequently launched by Lambda.

Your team can use these services to decouple and fragment your environment to the level of granularity desired.

![Sample architectural pattern for microservices with Lambda](./images/W08Img070LambdaMiscroservicesPattern.png)

In general, a microservices environment can introduce the following difficulties:

* Repeated overhead for creating each new microservice
* Issues with optimizing server density and usage
* Complexity of running multiple versions of multiple microservices simultaneously
* Proliferation of client-side code requirements to integrate with many separate services

The serverless microservices pattern lowers the barrier for the creation of each subsequent microservice (API Gateway even allows for the cloning of existing APIs and using Lambda functions in other accounts). Optimizing server usage is no longer relevant with this pattern.

Finally, API Gateway provides programmatically generated client SDKs in several popular languages to reduce integration overhead.

### Knowledge Check

#### Which deployment type is suitable for applications that have bursty or unpredictable workloads, such as real-time analytics or Internet of Things (IoT) applications?

* Serverless deployments

Wrong answers:

* Container deployments
* Physical, on-premises deployments
* Thin-client deployments

#### Which feature is not a benefit of serverless Microservices?

* User-controlled OS patching

Wrong answers:

* Pay-per-use
* Continuous delivery
* Scalability

##### Explanation

OS updates do not have to be installed with serverless microservices. Serverless microservices are ephemeral. This means they are short-lived and dynamically created as needed, rather than running continuously on a persistent server. This eliminates the need for manual OS updates and maintenance.

The other options are incorrect because of the following reasons:

* Pay-per-use is a benefit because the customer only pays for what they use.
* Continuous delivery is a benefit due to the dynamic response time serverless microservices offer.
* Scalability is a benefit due to the scalability of microservices based on demand.

#### Choose the serverless services offered by AWS (Select THREE.)

* AWS Fargate
* AWS Lambda
* Amazon DynamoDB

Wrong answers:

* Amazon EC2
* Amazon WorkSpaces
* Amazon Lightsail

##### Explanation

The other options are incorrect because

* Amazon Elastic Compute Cloud (EC2) is not serverless because it requires managing underlying virtual server instances.  
* Amazon WorkSpaces is not serverless since it provides persistent virtual desktops that require managing dedicated underlying server resources.
* Amazon Lightsail is not serverless as it provides virtual private servers that require managing dedicated compute resources.

### Summary

* Which serverless and container services are available from AWS
* How to articulate when serverless or container services should be used
* How to explain some of the benefits of serverless microservices

## Serverless Microservices with AWS Lambda

### Pre-assessment

#### What is the name of the AWS SDK for Python?

* Boto3

Wrong answers:

* AWS Serverless Application Model (SAM)
* AWS Cloud Development Kit (CDK)
* Java Development Kit

#### Which method in function code processes events?

* Lambda function handler

Wrong answers:

* Python command
* Invoke command process
* Bash interpreter

##### Explanation

The Lambda function handler is the method in function code that processes events. When a function is invoked, Lambda runs the handler method.

The other options are incorrect because of the following reasons:

* Python command used to invoke Lambda functions from within they Python script file.
* Invoke command process is the way Lambda invokes synchronous and asynchronous functions.
* Bash interpreter is used for interpreting Bash scripts.

#### Which methods are used for creating an AWS Lambda application? (Select THREE.)

* AWS Serverless Application Repository
* AWS CloudFormation
* AWS CLI and AWS Serverless Application Model (AWS SAM) CLI

Wrong answers:

* Amazon EC2 console
* Amazon S3
* Amazon DynamoDB
* Amazon Elastic Transcoder

## Developing a Python Lambda Function

You can run Python code in Lambda. Lambda provides runtimes for Python that run your code to process events. Your code runs in an environment that includes the AWS SDK for Python (Boto3), with credentials from an AWS Identity and Access Management (IAM) role that you manage.
