# DevOps 1 Part 1

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to repo's main [README.md](../../../README.md)

## Defining DevOps

DevOps is the combination of **cultural philosophies**, **practices**, and **tools** that increase an organization’s ability to deliver applications and services at high velocity.

## AWS DevOps toolchain

1. **Code**. Code refers to the initial stage where developers write, commit, and manage their code in a repository. Source control manages code versioning and collaboration. You can manage versioning and collaboration of code with tools such as AWS CodeCommit.
2. **Build, configure, deploy**. This stage involves preparing the code for deployment by building it, configuring it for the target environment, and deploying it to the chosen AWS service. Different environments at this stage include development and testing, quality assurance, and production for live user experience. Supporting services at this stage include: AWS CodePipeline, AWS CloudFormation, AWS CodeDeploy, AWS OpsWorks, AWS Identity and Access Management (IAM), and AWS Secrets Manager.
3. **Platform**. Platform represents the underlying infrastructure where your application runs, using services such as Amazon Elastic Kubernetes Service (Amazon EKS), AWS Elastic Beanstalk, and Amazon Elastic Compute Cloud (Amazon EC2).
4. **Monitor**. This stage involves monitoring your infrastructure and your application's performance and health using tools such as Amazon CloudWatch.

## DevOps Overview

DevOps is a set of practices that aims to automate and improve the collaboration between software development (Dev) and IT operations (Ops). By implementing these practices, you deliver new application features and improved services to customers at a higher velocity.

### Benefits of DevOps

1. **Flexibility**. DevOps promotes **flexibility** in adapting to evolving requirements. The continuous feedback loop and iterative development help teams to respond promptly to changes in business needs or technological advancements.
2. **Innovation**. By breaking down silos and encouraging collaboration, DevOps encourages an innovation-friendly culture. Teams are more likely to experiment with new ideas, technologies, and approaches, fostering a culture of continuous improvement.
3. **Speed**. DevOps facilitates high velocity, fostering innovation, adapting to market changes efficiently, and driving business results more effectively. Microservices and continuous delivery empower teams to take ownership of services and release updates swiftly.
4. **Reliability**. With DevOps, you ensure the quality of application updates and infrastructure changes, to provide rapid delivery while maintaining a positive user experience. Continuous integration and continuous delivery practices, along with monitoring and logging, help validate changes in real time.
5. **Scalability**. Use DevOps to operate and manage infrastructure and development processes at scale. Automation and consistency assist in efficiently managing complex or changing systems and reducing risk. Infrastructure as code facilitates repeatable and efficient management of environments.
6. **Collaboration**. DevOps fosters effective teamwork by emphasizing values like ownership and accountability. Collaboration between developers and operations teams reduces inefficiencies and saves time, eliminating handover periods and enabling code that considers its operational environment.
7. **Security**. DevOps permits quick movements while retaining control and compliance. Automated compliance policies, fine-grained controls, and configuration management techniques, such as infrastructure as code and policy as code, ensure security without sacrificing speed.

### Roles in DevOps

1. **User experience specialist**. The user experience specialist’s focus is on quality assurance tied to the customer experience. This role ensures that all features in the final product meet specifications and that the product is user friendly.
2. **Software developer**. Software developers usually take on an expanded role that encompasses writing code, unit testing, deployment, and ongoing monitoring. This role typically ensures that code aligns with business requirements. Software developers are also responsible for monitoring and maintaining product performance.
3. **Security engineer**. Security engineers partner with software developers in ensuring overall security and regulation compliance of the product. They are also responsible for integrating security recommendations during product development.
4. **Automation engineer**. Automation engineers are responsible for automating systems within a DevOps framework. This role identifies, designs, and implements strategies for automating manual tasks.
5. **Project manager (or product manager)**. Project managers manage products and applications from development through deployment. They are responsible for tracking progress using key metrics.

### The role of a cloud application developer in DevOps

A cloud application developer plays a key role in the DevOps environment by working closely with DevOps teams to build, deploy, and optimize applications specifically tailored for cloud environments. This contributes to the overall efficiency and reliability of the development and deployment processes. The following are some of the responsibilities that the cloud application developer role often includes:

* Collaborating with software developers to design and deploy stable and efficient applications.
* Ensuring that applications use cloud scalability and performance optimization.
* Using microservice architectures for developing and deploying applications.
* Integrating code changes into the pipeline, automating testing, and facilitating continuous deployment to the cloud.
* Partnering with software engineers to address vulnerabilities and ensure that security measures are embedded in the application design.

### DevOps Best Practices

#### DevOps Culture

* People oer process over tools

#### Collaboration

* Cross-functional teams and shared responsibility

1. Continuous integration (CI). Developer -> Shared codebase -> Automated checks -> Developer. Continuous integration is a software development practice in which developers regularly merge their code changes into a central repository. Then, automated builds and tests are run to ensure the stability of the codebase.
2. Continuous delivery (CD). Provision -> **Deploy** -> Monitor. Continuous delivery is a software development practice in which code changes are automatically built, tested, and prepared for a release to production. It expands upon continuous integration by deploying all code changes to a testing environment, production environment, or both, after the build stage.
3. Microservices. Breaking down to a small parts implementing a single business service. The microservices architecture is a design approach to build a single application as a set of small services.
4. Infrastructure as code (IaC). Infrastructure is provisioned and managed using **code** and **software development techniques**, such as version control and continuous integration.
5. Monitoring and observability. The monitoring and logging practice involves monitoring metrics and logs to see how application and infrastructure performance impacts the user experience for the product.
 5.1. Logs provide time-series data detailing the system or application's operation.
 5.2. Traces follow the logical flow with the application.
 5.3. Metrics include details like CPU and RAM usage, disk space, and network connectivity.
6. Security. Shift security left - to the early stages of planning and coding.
7. **Communication and collaboration**. Increased communication and collaboration in an organization is one of the key cultural aspects of DevOps. The use of DevOps tooling and automation of the software delivery process establishes collaboration by physically bringing together the workflows and responsibilities of development and operations.

### AWS Services and Tools for Different Practices

#### Version control

* **AWS CodeCommit** is a version control service that permits you to privately store and manage Git repositories in the AWS Cloud.
* Widely adopted for version control, **Git** makes it possible for you to track changes, collaborate seamlessly, and maintain code repositories efficiently. You will learn more about Git later in this module. (Non-AWS tool)

#### Continuous integration and continuous delivery (CI/CD)

* **AWS CodePipeline** is a continuous delivery service that helps you model, visualize, and automate the steps required to release your software.
* **AWS CodeBuild** is a fully managed build service that compiles your source code, runs unit tests, and produces artifacts that are ready to deploy.
* **AWS CodeDeploy** is a deployment service that developers use to automate the deployment of applications to instances and to update the applications as required.
* **Amazon CodeCatalyst** is a service you use to quickly build and deploy cloud applications on AWS. To learn more about this service, see the Amazon CodeCatalyst(opens in a new tab) product page.
* **AWS Cloud9** is a cloud-based integrated development environment (IDE) that you use to write, run, and debug code.
* An open-source automation server, **Jenkins** facilitates continuous integration and delivery by automating building, testing, and deployment processes. (Non-AWS tool)

#### Microservices

* **Amazon Elastic Container Service (Amazon ECS)** is a highly scalable, fast container management service that simplifies running, stopping, and managing Docker containers on a cluster of Amazon EC2 instances.
* **AWS Lambda** lets you run code without provisioning or managing servers. Lambda takes care of everything required to run and scale your code with high availability. You can set up your code to automatically run from other AWS services or call it directly from any web or mobile application.
* **Docker** is a containers tool. Use Docker for the packaging and deployment of microservices in isolated containers, to ensure consistency across different environments. (Non-AWS tool)
* **Kubernetes** is an orchestration tool for containerized applications. Kubernetes automates the deployment, scaling, and management of microservices. (Non-AWS tool)

#### Infrastructure as code (IaC)

* **AWS CloudFormation** helps you create and provision AWS infrastructure deployments predictably and repeatedly. With CloudFormation, you can use a template file to create and delete a collection of resources together as a single unit (a stack).
* **AWS Elastic Beanstalk** helps you quickly deploy and manage applications in the AWS Cloud without worrying about the infrastructure that runs those applications. Elastic Beanstalk automatically handles the details of capacity provisioning, load balancing, scaling, and application health monitoring.
* **AWS Systems Manager** provides a unified user interface so that you can view operational data from multiple AWS services and helps you automate operational tasks across your AWS resources.
* **AWS Config** provides a detailed view of the resources associated with your AWS account. This includes how they are configured, how they are related to one another, and how the configurations and their relationships have changed over time.
* **Terraform** is an IaC software tool that provides a consistent command line interface (CLI) workflow to manage cloud services at scale. (Non-AWS tool)

#### Monitoring and logging

* **Amazon CloudWatch** provides a reliable, scalable, and flexible monitoring solution to monitor your AWS resources and the applications that you run on AWS in real time.
* **AWS CloudTrail** monitors your AWS deployments in the cloud by getting a history of AWS API calls for your account. This includes API calls made by using the AWS Management Console, the AWS SDKs, the command line tools, and higher-level AWS services.
* **AWS X-Ray** analyzes the behavior of your distributed applications by providing request tracing, exception collection, and profiling capabilities. 
* **AWS App Mesh** monitors and controls microservices that are running on AWS.
* **Prometheus** is an open-source monitoring and alerting tool designed for scalability and availability. (Non-AWS tool)

#### Security

* **AWS Identity and Access Management (IAM)** is a web service for securely controlling access to AWS services. With IAM, you can centrally manage users, security credentials such as access keys, and permissions that control which AWS resources users and applications can access.
* **Amazon GuardDuty** is a threat detection service that continuously monitors for malicious activity and unauthorized behavior across your AWS environment. 
* **AWS Key Management Service (AWS KMS)** is an encryption and key management service scaled for the cloud. AWS KMS keys and functionality are used by other AWS services, and you can use them to protect data in your own applications that use AWS.
* **Amazon Inspector** is a security vulnerability assessment service that helps improve the security and compliance of your AWS resources. It automatically assesses resources for vulnerabilities or deviations from best practices, and then produces a detailed list of security findings prioritized by level of severity.
* **AWS Security Hub** provides you with a comprehensive view of your security state in AWS, and helps you assess your AWS environment against security industry standards and best practices.

### Knowledge Check

#### Which sentence best describes DevOps?

* DevOps is a practice that improves collaboration between developers and operations teams.

Wrong answers:

* DevOps is a software tool that you use for deploying code.
* DevOps aims to completely automate infrastructure and remove operations teams.
* DevOps is a role for an engineer who can both develop and manage infrastructure.

DevOps is about processes, culture, and practices to improve collaboration, communication, and integration between developers and operations.

DevOps is not a specific tool, but rather a methodology. DevOps relies on collaboration between developers and operations teams to improve speed and quality.

#### Which response is considered one of the three pillars of observability?

* Logs

Wrong answers:

* Services
* Security
* Events

The three pillars of observability are logs, traces, and metrics. Logs, generated by various system components and applications, provide time-series data detailing the system or application’s operation.

#### Which sentence describes the Git tool?

* It helps you tracks changes, collaborate seamlessly, and maintain code repositories.

Wrong answers:

* It packages and deploys microservices in isolated containers.
* It is an open-source monitoring and alerting tool.
* It is a tool for securely controlling access to AWS services.

Widely adopted for version control, Git permits you to track changes, collaborate seamlessly, and maintain code repositories efficiently.

You use Docker for the packaging and deployment of microservices in isolated containers. Prometheus is an open-source monitoring and alerting tool designed for scalability and availability. AWS Identity and Access Management (IAM) is a tool for securely controlling access to AWS services.

### Summary

#### Introduction to DevOps

DevOps, short for Development and Operations, is a cultural, practical, and tool-driven approach aiming to enhance collaboration between development and IT operations. It breaks down silos, emphasizing automation throughout the software development lifecycle. DevOps incorporates principles from agile development, continuous integration, and continuous delivery. It addresses challenges in traditional software development, such as monolithic architectures, by introducing practices like microservices. DevOps promotes continuous improvement through automation, streamlining tasks, and improving software release reliability. Embracing DevOps leads to faster delivery, enhanced collaboration, and improved software quality.

#### Benefits of DevOps

With a focus on simplicity, flexibility, and automation, DevOps offers the following benefits:

* Flexibility
* Innovation
* Speed
* Reliability
* Scalability
* Collaboration
* Security

#### Roles in DevOps

In DevOps, the following roles contribute to the development and deployment process:

* User experience specialist
* Software developer
* Security engineer
* Automation engineer
* Project manager (or product manager)

The following are some of the responsibilities of a cloud application developer role in a DevOps environment:

* Collaborating with software developers to design and deploy stable and efficient applications.
* Ensuring that applications use cloud scalability and performance optimization.
* Using microservice architectures for developing and deploying applications, aligning with DevOps principles.
* Integrating code changes into the pipeline, automating testing, and facilitating continuous deployment to the cloud.
* Partnering with software engineers to ensure that security measures address vulnerabilities and are embedded in the application design.

#### DevOps best practices

DevOps best practices center around fostering a collaborative culture and emphasizing human collaboration over processes and tools. The goal is to create an environment where teams can openly address and adapt processes that are not working effectively.

1. **Collaboration**. Collaboration is a priority, with a focus on breaking down traditional silos between development and operations.
2. **CI/CD**. The approach to DevOps includes continuous integration (CI) and continuous delivery (CD) to ensure regular integration, automated builds, and tests for maintaining a deployable codebase.
3. **Microservices**. Microservices architectures involve breaking down monolithic applications into independent services to enhance flexibility and collaboration. Infrastructure as code (IaC) automates manual processes and settings, and uses code for resource provisioning and management.
4. **Monitoring and logging**. Monitoring and logging are crucial in DevOps, providing real-time insights into application and infrastructure performance through logs, traces, and metrics.
5. **Security**. Security is integrated throughout the development lifecycle, with a shift-left approach, automated testing tools, and continuous monitoring for real-time threat response.

#### AWS services and tools for different practices

* **Version control:** AWS CodeCommit, Git
* **Continuous integration and continuous delivery (CI/CD):** AWS CodePipeline, AWS CodeBuild, AWS CodeDeploy, Amazon CodeCatalyst, AWS Cloud9, Jenkins
* **Microservices:** Amazon Elastic Container Service (Amazon ECS), AWS Lambda, Docker, Kubernetes
* **Infrastructure as code (IaC):** AWS CloudFormation, AWS Elastic Beanstalk, AWS Systems Manager, AWS Config, Terraform
* **Monitoring and logging:** Amazon CloudWatch, AWS CloudTrail, AWS X-Ray, AWS App Mesh, Prometheus
* **Security:** AWS Identity and Access Management (IAM), Amazon GuardDuty, AWS Key Management Service (AWS KMS), Amazon Inspector, AWS Security Hub

## Code Repositories

### Pre-assessment

#### Which AWS service can be used to host private Git repositories?

* AWS CodeCommit

Wrong answers:

* AWS CodeBuild
* AWS CodeDeploy
* AWS CodePipeline

CodeCommit is a secure, highly scalable, managed source control service that hosts private Git repositories.

#### What is a benefit of using version control systems for code development?

* Multiple developers can work on the same codebase simultaneously.

Wrong answers:

* Writing over older versions of code saves on storage costs.
* Developers can work directly on code in the production environment.
* It eliminates the need for a code repository.

Version control systems provide essential benefits for tracking changes, facilitating collaboration, and maintaining integrity and availability of the code history. Multiple developers can work on the same codebase simultaneously without overriding each other's changes.

#### How does AWS CodeCommit provide a way to work on different versions of files without impacting the main branch?

* Developers can create branches to separate work on different versions before merging.

Wrong answers:

* Developers can work directly on the main branch and quickly roll back mistakes.
* Developers commit to creating code that does not negatively impact the main branch.
* CodeCommit eliminates the need for a main branch.

With CodeCommit, you can create branches for your repository to separate work on a new or different version of files without impacting work in the main branch. The main branch is usually the production version while new features are developed on separate branches.

### Version Control Systems

The following are the primary goals of version control:

* Maintain a history of source code changes and enable tracking back to previous versions.
* Allow multiple developers to collaborate on the same codebase by merging their changes.
* Support creating separate branches to isolate new-feature development or experiments.
* Roll back to earlier, stable versions if needed.
* Maintain information about who made each change, when, and why.
* Prevent corruption and overwriting of source code files.
* Enable experimental development and branching without impacting stable mainline code.

Popular version control systems used in software development include Git, Apache Subversion (SVN), Mercurial, and Perforce.

## Types of Version Control Systems

### Centralized version control systems

Centralized version control systems have a single remote server of versioned data with individual users operating locally against copies of that data’s version history. Developers commit their changes directly to that central server repository. Commits are snapshots of the contents and changes to the contents of your repository. Every time that a user commits and pushes a change, that information is saved and stored.

All the files and commit history information are stored in a central server, but working on a single central server means more chances of having a single point of failure. Centralized version control systems offer few offline access features. A developer has to connect to the version control system server. The single point of failure, security, maintenance, and scaling a centralized infrastructure are the major concerns for any organization.

Subversion (SVN) and Perforce are examples of centralized version control systems.

#### SVN

Subversion (also known as SVN) is an open-source, centralized version control system. SVN maintains a single central repository that contains all files and historical revisions. Developers check out a working copy from this central repository. Changes made to the working copy are committed back to the central repository. This provides version tracking and maintains a history of changes.

SVN implements branching and merging to support concurrent development between multiple developers. It uses atomic commits so that changes happen as an atomic transaction. This means that either all the changes in the commit will be applied successfully or, if any error occurs, then none of the changes will be applied.

SVN does not use distributed repositories, meaning that developers must be online and connected to the server to access the codebase. The central repository acts as a single source of truth for the codebase and its history. Due to the centralized nature, SVN does not work offline and is less flexible for advanced distributed workflows.

#### Perforce

Perforce is a centralized version control system designed for large-scale software development teams. It uses a client-server architecture with a central server storing all versioned files and their change history. Developers use a Perforce client to connect to the server. Perforce supports file versioning, branching and merging, workspace management, and additional features similar to other version control systems.

The centralized server model provides strict control and oversight suitable for large regulated organizations. But it lacks the flexibility of distributed version control systems like Git.

### Distributed version control systems

Distributed version control systems address the concerns and challenges of centralized systems. In a distributed version control system, you don’t just check out the latest snapshot of the files. Instead, you fully mirror the repository, including its full history. If any server fails, and these systems are collaborating using that server, you can copy any of the client repositories back up to the server to restore it. Every clone is a full backup of all the data.

Git and Mercurial are examples of distributed version control systems.

#### Git

Git is a distributed, open-source version control system that you can use to store code, track revision history, merge code changes, and revert to an earlier code version when needed.

Git stores your source code and its full development history locally in a repository that works with Git. You can create a copy of your source code, known as a branch, which you can then work on in parallel to the main version.

When you are ready, you can commit changes to save your progress. Or you can merge your branch back into the main version. Every time you commit, Git takes a snapshot of your work and compares it to previous versions with a viewable operation called a diff. If there's been a change from previous commits, Git stores a new snapshot in the repository.

#### Mercurial

Mercurial is a free and open-source distributed version control system for software development. Like Git, Mercurial is a distributed version control system, meaning that developers have local copies of the full repository with complete history and version tracking abilities. It provides features like atomic commits, branching, tagging, reverting changes, merging between branches, and multiple workflow models like centralized, distributed, or third-party integration.

### Benefits of using Git for version control

Git solves many problems of older systems like SVN and provides a fast, distributed, and advanced workflow. These advantages have made Git the most widely adopted version control system for modern software teams.

#### Speed

Git is fast and efficient compared to older systems like SVN. Operations like committing, branching, and merging are optimized for performance. This can make developers more productive.

#### Distributed model

Git repositories are distributed across all clones, unlike centralized systems like SVN. Developers can commit, branch, and merge, even when offline. This facilitates better collaboration across distributed teams.

#### Tool ecosystem

Git is integrated with many source control services like GitHub, GitLab, Bitbucket, and AWS CodeCommit. This provides developers with powerful collaboration capabilities and hosting options.

#### Ubiquity

Git is the most used version control system today. Most developers are already familiar with it. This makes it easy for teams to adopt it and collaborate with other teams using Git.

#### Open source

Git is open source. The source code is actively maintained by a large community of developers who continuously improve it.

## Code Repositories

A code repository and a version control system work together to track changes to source code over time. The code repository is where all the revision history and collaborative information is stored by the version control system. The version control system provides tools to manipulate the repository. Together, they facilitate version control of source code.

A repository, or repo, is centralized digital storage that developers use to make and manage changes to an application’s source code. Developers can use a repo to track code changes, simultaneously edit files, and efficiently collaborate on the same project from any location. Repos are important because they make it possible for software development teams to implement multiple changes to a software’s program code without compromising the main source code. And teams can introduce new features or bug fixes without affecting the production version of the application.

For businesses, repos provide several benefits. Developers can use repos to work on new features rapidly without affecting the stability of the live application. Additionally, developers can introduce changes and resolve potential issues rapidly. Organizations can also coordinate application development tasks among developers who work remotely.

### Common code repositories

#### AWS CodeCommit

CodeCommit is an online code versioning system that you can use to host private Git repositories securely. CodeCommit integrates with your existing Git-based tools to form a seamless continuous integration and continuous delivery (CI/CD) pipeline.

CodeCommit has the advantage of being integrated with other AWS services. Integrated services include AWS Key Management Service (AWS KMS), Amazon CloudWatch Events, Amazon Simple Notification Service (Amazon SNS), and AWS Identity and Access Management (IAM). This integration means that in response to CodeCommit events (like PUSH, MERGE REQUEST), you can invoke Lambda functions that can perform custom actions, for example, Slack notifications.

CodeCommit stores your repositories in Amazon Simple Storage Service (Amazon S3) and Amazon DynamoDB, both durable and highly available services.

#### GitHub

GitHub is a development and collaboration platform built on Git that developers can use to build and share software. It provides an integrated platform for continuous integration and development, a nonlinear workflow for collaboration, and in-depth monitoring and auditing for administrators. It provides a graphical UI that makes using the repository functions straightforward.

GitHub has also become an online open-source community for developers. Developers can connect with peers by joining a discussion, offering help, and contributing their expertise in public projects on GitHub.

#### GitLab

GitLab is a complete DevOps platform, delivered as a single application. GitLab provides project planning, source code management, CI/CD, and monitoring features. As the name suggests, GitLab is based on the Git version control system.

## Introduction to AWS CodeCommit

CodeCommit is a fully managed source control service that hosts secure Git-based repositories. Teams can use CodeCommit to collaborate on code in a secure and highly scalable environment.

### Features of CodeCommit

#### Fully managed service

CodeCommit eliminates the need to host, maintain, back up, and scale your own source control servers. The service automatically scales to meet the growing needs of your project.

#### Security

CodeCommit automatically encrypts your files in transit and at rest. CodeCommit is integrated with IAM, so you can customize user-specific access to your repositories.

#### High availability

CodeCommit has a highly scalable, redundant, and durable architecture. The service is designed to keep your repositories highly available and accessible.

#### Collaboration on code

CodeCommit helps you collaborate on code with teammates through pull requests, branching, and merging. You can implement workflows that include code reviews and feedback by default, and control who can make changes to specific branches.

#### Faster development cycle

CodeCommit keeps your repositories close to your build, staging, and production environments in the AWS Cloud. You can transfer incremental changes instead of the entire application, so you can increase the speed and frequency of your development lifecycle.

#### Ability to use your existing code

CodeCommit supports all Git commands and works with your existing Git tools. You can keep using your preferred development environment plugins, CI/CD systems, and graphical clients with CodeCommit.

### Versioning in CodeCommit compared to Amazon S3

Amazon S3 is a service that you can use to store objects in Amazon S3 buckets. Versioning is an optional feature that you can enable on S3 buckets. It allows you to keep multiple versions of an object in the same bucket.

When versioning is enabled, Amazon S3 will preserve old versions of objects instead of overwriting them when new uploads occur with the same object key. Each version of an object has a unique version ID assigned by Amazon S3. The latest version is marked as the current version. Older versions are not deleted but remain accessible using the version ID unless explicitly deleted. Deleted objects can also be restored by using the version ID.

Each commit in CodeCommit repository is assigned a unique ID that allows you to reference that point-in-time version of the code. You can view, retrieve, and restore past versions of your repository using commit IDs. When you commit a change to a repository, you can add a comment to explain what you changed and why.

With CodeCommit, you can create branches for your repository to separate work on a new or different version of files without impacting work in the default branch. Branching and merging strategies can be used to work on parallel streams of development. Different versions of code can exist on different branches.

#### Default branch

When you create your first commit, a default branch is created for you.  This default branch is the one used as the base or default branch in local repositories (repos) when users clone the repository. If you add the first file to your repository by using the CodeCommit console, the AWS Command Line Interface (AWS CLI), or one of the SDKs, the name of that default branch is main. This branch is usually the production version while new features are developed on separate branches.

#### New branch

You can create branches for your repository to separate work on a new or different version of files without impacting work in the default branch.

#### Commits

Commits are snapshots of the contents and changes to the contents of your repository. Every time that a user commits and pushes a change, that information is saved and stored. So, too, is information that includes who committed the change, the date and time of the commit, and the changes made as part of the commit.

#### Merging two branches

Merging applies the changes to a branch together with another branch. You can compare the two branches first to view the differences before merging.

You can use the CodeCommit console to compare branches in a CodeCommit repository. Comparing branches helps you quickly view the differences between a branch and the default branch, or view the differences between any two branches.

You can revert, or roll back, changes by checking out a previous commit ID on a branch. This lets you return to an older working version.

### [Lab: Working with AWS CodeCommit](./W09Lab01-AWSCodeCommit.md)

### Knowledge Check

#### Which open-source version control system can AWS CodeCommit be used to host private repositories from?

* Git

Wrong answers:

* Mercurial
* Subversion (SVN)
* GitHub

CodeCommit is an online code versioning system that you can use to host private Git repositories securely. CodeCommit integrates with your existing Git-based tools to form a seamless continuous integration and continuous delivery (CI/CD) pipeline.

#### What is a quality of a distributed version control system, like Git, that makes it different from a centralized version control system, like Subversion (SVN)?

* Developers make a local clone of the complete repository, including its full history.

Wrong answers:

* Developers check out a file from a central repo. It remains locked until checked in.
* Developers must be connected to a central server to access the codebase.
* Developers commit changes directly to a central server repository.

In a distributed version control system, you don’t just check out the latest snapshot of the files; rather, you fully mirror the repository, including its full history. If any server dies, and these systems are collaborating using that server, you can copy any of the client repositories back up to the server to restore it. Every clone is a full backup of all the data.

#### When committing a change to a repository in AWS CodeCommit, how can developers efficiently communicate what changes they made and why they made the changes?

* Developers can add a comment when committing a change.

Wrong answers:

* Set up an AWS Lambda function to send notifications using Amazon Simple Notification Service (Amazon SNS).
* By default, Amazon Comprehend interprets the changes and emails a summary to developers.
* It is best practice to log changes in a spreadsheet kept in a shared storage space, such as Amazon S3.

When developers commit a change to a repository, they can add a comment to explain what was changed and why.

Setting up an AWS Lambda function for communicating changes or logging changes in a spreadsheet is cumbersome and inefficient. Amazon Comprehend is a service that analyzes text stored in an Amazon S3 data lake.

### Summary

#### Version control strategies and benefits

Version control refers to the practice of tracking and managing changes to source code over time. With version control and a clear audit trail, it’s possible to know who made changes and why those changes were made.

Here is a summary of the key points:

* Version control systems track changes to files over time, which is useful for collaborative projects with multiple contributors. Developers can manage different versions of code and files.
* Version control takes snapshots of files as developers make edits. It saves these snapshots so that they can be recalled later if needed.
* Without version control, conflicts can arise when multiple developers edit the same files. Manual communication and file sharing becomes difficult.
* Branching allows for separate lines of development to work on features or fixes without affecting the main codebase. Changes are merged back when work is complete.
* Key benefits of version control include creating workflows, working with file versions and descriptions, synchronizing versions across developers, and maintaining an edit history.

#### Version control systems

Version control is a practice that tracks and manages changes to source code over time. It provides a way for developers to collaborate on the same codebase, create separate branches for new feature development, and roll back to earlier stable versions if needed. It also maintains a history of changes, who made them, when, and why, preventing corruption and overwriting of source code files.

Centralized version control systems have a single remote server of versioned data with individual users operating locally against copies of that data’s version history. Popular centralized version control systems include Subversion (SVN) and Perforce.

With a distributed version control system, the repository is mirrored and worked on locally, including its full history. Git and Mercurial are popular examples of distributed version control systems.

#### Code repositories

You can use a code repository, or repo, to store, manage, and track changes to a codebase. Developers can create separate branches to work on features without affecting the main code. Changes can then be merged back. Multiple developers can contribute concurrently, with the repository tracking who made what changes.

Common code repositories include AWS CodeCommit, GitHub, and GitLab.

#### Introduction to AWS CodeCommit

CodeCommit is a fully managed source control service that hosts secure Git-based repositories. CodeCommit repositories have built-in version control using Git. All changes are tracked as commits with unique IDs.

### Additional Resources

#### [What Is Git?](https://aws.amazon.com/devops/source-control/git/)

#### [What Is Repo? ](https://aws.amazon.com/what-is/repo/)
