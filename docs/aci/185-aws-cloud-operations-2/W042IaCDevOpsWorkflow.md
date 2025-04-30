# Week 4: IaC: IaC as Part of a DevOps Workflow

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to [AWS Cloud Operations 2](./aws-cloud-operations-2.md)
* back to repo's main [README.md](../../../README.md)

## IaC as a Part of a DevOps Workflow

### Pre-assessment

#### Which statement best describes how infrastructure as code (IaC) fits into the DevOps workflow?

* IaC enables the automation of infrastructure provisioning and configuration as part of continuous integration and continuous delivery (CI/CD).

Wrong answers:

* IaC is used to manually provision and configure infrastructure resources.
* IaC is only used for testing and compliance purposes, not for actual infrastructure deployment.
* IaC is a separate process that is independent of the DevOps workflow.

##### Explanation

IaC allows infrastructure resources to be defined and managed using code, which can be integrated into the continuous integration and delivery pipeline. This enables infrastructure to be provisioned, configured, and deployed automatically as part of the DevOps workflow, ensuring consistency and reducing manual effort.

The other options are incorrect because of the following:

* Infrastructure as code is meant to automate and codify infrastructure provisioning and configuration, not do it manually.
* Infrastructure as code enables automated deployment of infrastructure resources in addition to testing and compliance checking.
* Infrastructure as code is an integral part of the DevOps methodology, enabling infrastructure management through the same workflows as application code.

#### What is a key responsibility of application developers when writing and maintaining infrastructure as code (IaC) templates?

* Defining the infrastructure resources required for their applications and encoding them in IaC templates

Wrong answers:

* Ensuring that the IaC templates meet the organization's General Data Protection Regulation (GDPR) requirements
* Collaborating with physical infrastructure teams to define and maintain the IaC templates
* Manually provisioning and configuring the infrastructure resources based on the IaC templates

##### Explanation

Application developers have the best understanding of the infrastructure requirements for their applications. By encoding these requirements in IaC templates, developers can ensure that the infrastructure meets the application's needs and can be consistently provisioned and configured.

The other options are incorrect because of the following:

* Meeting GDPR requirements is related to data privacy compliance, not a core responsibility of application developers when working with infrastructure as code templates.
* IaC templates are typically defined and maintained by the application teams themselves, without necessarily collaborating with separate physical infrastructure teams.
* The purpose of IaC is to automate and codify infrastructure provisioning and configuration, not do it manually based on the templates.

#### Which statement best describes the collaboration between application developers and infrastructure teams when working with infrastructure as code (IaC)?

* There is a high need for coordination and collaboration between application developers and infrastructure teams to ensure successful implementation of IaC.

Wrong answers:

* Application developers work independently on IaC templates, and infrastructure teams are responsible for deploying and managing the infrastructure.
* Infrastructure teams define and maintain all IaC templates, and application developers have no involvement in the process.
* Application developers and infrastructure teams work in silos, with minimal coordination or collaboration required.

##### Explanation

The successful implementation of IaC requires close collaboration between application developers and infrastructure teams. Developers must define the infrastructure requirements, while infrastructure teams must ensure that the IaC templates meet organizational standards and can be deployed and managed effectively.

The other options are incorrect for the following reasons:

* They suggest a siloed approach without coordination between the two teams, which goes against successful implementation of IaC.
* They exclude application developers from the IaC process, which requires collaboration between both teams for successful implementation.
* They contradict the need for high coordination and collaboration between the two teams, as stated in the correct option.

## IaC as Part of a DevOps Workflow

### IaC and the DevOps workflow

Infrastructure as code (IaC) is a practice that involves the use of code to automate the provisioning, deployment, and management of servers, networks, and databases. Rather than relying on manual processes, IaC employs code to perform these tasks, ensuring consistency, repeatability, and scalability across various infrastructure components.

This code can be written in the programming language that you feel most comfortable with through the use of the AWS Cloud Development Kit (AWS CDK).

### Role of IaC in DevOps

#### Reproducible configurations

IaC enables reproducible infrastructure configurations that can be version-controlled, tracked, and collaborated on. It ensures consistent provisioning across environments, reducing human error and ensuring compliance with standards.

#### Seamless integration

IaC seamlessly integrates with continuous integration and continuous delivery (CI/CD) pipelines, allowing infrastructure and application changes to be coordinated and tested together. It facilitates infrastructure testing and enables faster, more reliable deployments.

#### Setup environments

IaC allows DevOps teams to quickly provision and configure consistent environments for development, testing, and production using code. This includes setting up virtual machines, containers, networks, and other resources in a repeatable manner.

IaC provides a common language for both developers and operations. Changes can be reviewed in a transparent manner, which fosters better collaboration in a DevOps environment.

### Version control

Version control is done differently when using IaC principles.

#### Version control without IaC

Without IaC, version control is limited to application code and configuration management. Infrastructure changes are often made manually through the AWS Management Console or AWS Command Line Interface (AWS CLI), making it challenging to track and reproduce changes consistently across different environments (for example, development, staging, and production). It is also difficult to automate the creation and deployment of infrastructure.

Furthermore, developing specifications for physical and virtual infrastructure often requires a lot of time and multiple teams.

#### Version control with IaC

When using IaC with version control, you can manage your entire AWS infrastructure as code. Version control systems provide several benefits, including the following:

* Detailed history of changes made to your infrastructure code, allowing you to track who made what changes and when
* Branching and merging using repositories like Amazon CodeCatalyst to manage different versions of the infrastructure code
* Deployment process using continuous integration and continuous deployment (CI/CD) pipelines, ensuring consistent and repeatable deployments across environments
* Ability to roll back to previous versions of the infrastructure code, if needed, minimizing the impact of issues or failures

Performing version control with IaC provides the ability to perform code reviews on deployment changes before they are applied. This adds an extra layer of safety to deployments and keeps infrastructure costs low. For example, a team working on a project can designate a group of trusted reviewers to ensure that all infrastructure changes are approved by engineers who are familiar with the implications of an infrastructure change on stability and cost.

Additionally, defining infrastructure in configuration files gives engineers a straightforward and agreed-upon view of the intended state of the system. If multiple members of a large engineering team were to make all of their infrastructure changes at the command line or in the AWS Management Console, it would quickly become unmaintainable.

With IaC version control and code reviews, multiple engineers must agree that the proposed infrastructure change is correct, and they must have done their due diligence to look for potential issues before approving.

### Continuous integration/continuous delivery

Continuous integration/continuous delivery (CI/CD) is the use of continuous processes for the publishing of new versions of code. For CI/CD to work, you first need to have your code stored in a centralized repository, such as Amazon CodeCatalyst or Git.

The process of CI/CD follows a workflow similar to the following graphic.

![CI/CD Workflow Flowchart](./images/W04Img010IaCCiCdFlowchart.png)

#### Continuous Integration

With CI, each time a change is made to your code, an automated process is triggered that compiles, builds, tests, and packages the code.

This automated process produces feedback for the developer(s) who made the change who can review and iterate on their code.

#### Continuous Delivery

CD is an extension of CI as it relates to IaC in that it takes code that has gone through an automated review process and then puts that code through a process in preparation for a live deployment.

Once approved, code is then deployed to the production environment using a tool like AWS CodePipeline or a third-party CI/CD tool.

Infrastructure deployments are monitored and capture logs are audited, and they include a plan to roll back to a previous state or recover from failures during the deployment and delivery process.

### [Lab 1: Deploying Infrastructure as Code with AWS CodePipeline](./labs/W040Lab1DeployingIaCUsingAwsCodePipeline.md)

In this lab, you will use AWS CodePipeline to deploy infrastructure as code (IaC) using an AWS CloudFormation template. This lab includes steps for building out a CloudFormation template, creating a CodePipeline by pulling source code from a code repository, and finally, creating and updating a CloudFormation stack.

In this lab, you will perform the following tasks:

* Create a CloudFormation template
* Configure an AWS CodePipeline
* Modify an infrastructure stack by updating the CloudFormation template
* Push the modified stack to the source code repository

### Developer Responsibilities in Writing and Maintaining IaC Templates
