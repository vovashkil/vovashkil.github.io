# DevOps 1 Part 3

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to repo's main [README.md](../../../README.md)

## Understanding IaC

### Pre-assessment

#### What is Infrastructure as Code (IaC)?

* A practice of managing and provisioning infrastructure through code

Wrong answers:

* A programming language for web development
* An AWS storage service
* An AWS service to manage and provision infrastructure through code

IaC is a practice of managing and provisioning infrastructure through code.

IaC is not a programming language itself but is implemented using languages such as YAML or JSON to define infrastructure configurations. IaC is not an AWS service.

#### Which principle of IaC emphasizes the declaration of the desired state of infrastructure? 

* Declarative

Wrong answers:

* Imperative
* Procedural
* Descriptive

A declarative approach declares the desired outcome. Instead of explicitly outlining the sequence of steps the infrastructure needs to reach the final result, the declarative approach shows what the final result looks like. The automation tool interprets and enforces this configuration and determines the necessary actions to reach the specified state.

#### Which AWS service do you use to define IaC using programming languages such as Python and Java? 

* AWS CDK

Wrong answers:

* AWS CloudFormation
* Amazon CodeCommit
* AWS SDK

With AWS CDK, you achieve faster deployment by using expressive programming languages for defining infrastructure, such as Python, Java, and .NET.

While AWS CloudFormation is a tool for infrastructure as code, it uses declarative JSON or YAML templates, not programming languages. AWS CodeCommit is a source control repository service. AWS SDK (Software Development Kit) are libraries for various programming languages to interact with AWS programmatically but are not specific for defining infrastructure.

### Introduction to IaC

Infrastructure as code (IaC) is a methodology that you use in DevOps that involves managing and provisioning computing infrastructure through code. You use this code to automate infrastructure management, so you can focus on designing and improving your applications instead of managing infrastructure.

* **Imperative approach**. The focus is on specifying the exact sequence of commands and procedures required for the infrastructure to reach the desired state or the final result. For example, an imperative approach is usually suited for sequential tasks like software deployment.
* **Declarative approach**. The declarative approach shows what the final result looks like. The automation tool interprets and enforces this configuration and determines the actions necessary to reach the specified state. AWS CloudFormation is an example of an IaC service that uses the declarative approach.

The choice between imperative and declarative approaches offers flexibility: imperative for detailed control, and declarative for specifying outcomes without outlining every step.

### Benefits of IaC

* **Automation and efficiency**. IaC automates the provisioning and configuration of infrastructure, reducing the need for manual intervention. Automation in processes saves time, minimizes errors, and facilitates rapid, consistent deployments.
* **Reusability ans speed**. IaC templates facilitate the reuse of predefined configurations, which saves time and promotes best practices. You can customize templates for different projects to promote standardization and accommodate project-specific requirements.
* **Scalability and flexibility**. With IaC, you scale infrastructure to accommodate changing workloads or business requirements. By implementing IaC, you also have flexibility in defining and modifying infrastructure to adapt to evolving needs.
* **Collaboration and productivity**. IaC fosters collaboration between development and operations teams by providing a common language and process for infrastructure management. Shared code repositories and collaborative workflows encourage communication and joint efforts.

### IaC in DevOps

#### Infrastructure automation

Through code-based infrastructure, teams can define the desired state of their infrastructure. For example, you can use tools like CloudFormation for infrastructure automation by providing a declarative syntax to specify resources, their configurations, and dependencies.

#### Version control and collaboration

Incorporating IaC into version-control systems brings transparency and traceability to your infrastructure management. Version control allows teams to track changes, roll back to previous states, and collaborate seamlessly. This version-controlled approach mitigates configuration drift, where inconsistencies arise between different environments over time. By treating infrastructure code as part of the software development process, teams can use familiar version-control workflows, branching strategies, and pull requests for effective collaboration and code review.

#### Consistency and reproducibility

By defining infrastructure through code, you can mirror development, testing, and production environments to ensure that what works in one environment can be reliably replicated in another. This consistency reduces the likelihood of deployment issues caused by environmental differences. Your team can predictably roll out changes, updates, and new releases, knowing that the same codebase will result in the same infrastructure configuration across various stages of the development pipeline.

### CloudFormation Overview

You can use CloudFormation to build applications with AWS products, such as the following, without creating or configuring the underlying infrastructure:

* Amazon Elastic Compute Cloud (Amazon EC2)
* Elastic Load Balancing (ELB)
* Amazon Route 53

1. **CloudFormation template**. With CloudFormation, you declare all your resources and dependencies in a template file. You can author your CloudFormation template with any code editor. You can check it into a version-control system such as GitHub or AWS CodeCommit. And you can review files before deploying. CloudFormation is available in all AWS Regions, and you pay only for the resources that you use.
2. **AWS CloudFormation**. CloudFormation is an API wrapper. When you create an Amazon EC2 instance in the AWS Management Console wizard, you initiate an API call to the Amazon EC2 service. The information that you enter through the wizard is passed on as parameters. CloudFormation calls those same APIs. What you define in your CloudFormation template is organized as an API call to the service, just like the wizard. CloudFormation manages the dependencies and relationships.
3. **Stack**. CloudFormation templates define a collection of resources as a single unit called a stack. CloudFormation creates and deletes all member resources of the stack together, and manages all dependencies between the resources for you.

### CloudFormation stacks

All resources in a stack are defined by the stack’s CloudFormation template. You can manage a collection of resources by creating, updating, or deleting stacks. For example, a stack can include all resources required to run a web application, including a web server, database, and networking rules. If you no longer require that web application, you can delete the stack, and all its related resources are deleted.

As an example, CloudFormation template broken into three stacks and paired with AWS resources. Resources include Lambda, AWS Batch, DynamoDB, Amazon Redshift, AWS Service Catalog, Amazon EMR, Step Functions.

CloudFormation treats the stack resources as a single unit. They must all be created or deleted successfully for the stack to be created or deleted. If a resource can't be created, CloudFormation rolls the stack back until all resources are created. If a resource can't be deleted, any remaining resources are retained until the entire stack can be successfully deleted. You can create cross-stack references that let you share outputs from one stack with another stack.

### CloudFormation templates

ACloudFormation template is a JSON or YAML formatted text file. You can save these files with any extension, such as .json, .yaml, .template, or .txt.

CloudFormation uses these templates as blueprints for building your AWS resources. For example, in a template, you can describe an Amazon EC2 instance, such as the instance type, the Amazon Machine Image (AMI) ID, block device mappings, and its Amazon EC2 key pair name. Whenever you create a stack, you also specify a template that CloudFormation uses to create whatever you described in the template.

### CloudFormation template sections

The following example shows a CloudFormation YAML template structure and all its possible sections. Templates include several major sections. The Resources section is the only required section. Some sections in a template can be in any order; however, as you build your template, it might be helpful to use the logical ordering of the following list because values in one section might refer to values from a previous section.

1. **AWSTemplateFormatVersion**. The format version declares the version of the CloudFormation template that you are using.
2. **Description**. The description provides human-readable text describing the purpose of the template.
3. **Parameters**. Parameters define input values that you can provide during stack creation.
4. **Mappings**. Mappings define conditional resource configuration based key-value pairs that you specify.
5. **Conditions**. Conditions control whether certain resources are created or how they are configured.
6. **Transform**. Transforms specify the version of AWS Serverless Application Model (AWS SAM) to use, if required.
7. **Resources**. Resources specify the AWS resources that should be created or managed by the CloudFormation stack.
8. **Outputs**. Outputs define values that you can export from the stack for reference or use in other stacks.

#### Additional resources

For more information about template creation and capabilities, see [Template Anatomy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html).

### Examples

#### Example JSON CloudFormation template

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "A sample template",
  "Resources": {
    "MyEC2Instance": {
      "Type": "AWS::EC2::Instance",
      "Properties": {
        "ImageId": "ami-0ff8a91507f77f867",
        "InstanceType": "t2.micro",
        "KeyName": "testkey",
        "BlockDeviceMappings": {
          "DeviceName": "/dev/sdm",
          "Ebs": {
            "VolumeType": "io1",
            "Iops": 200,
            "DeleteOnTermination": false,
            "VolumeSize": 20
          }
        }
      }
    }
  }
}
```

#### Example YAML CloudFormation template

```
AWSTemplateFormatVersion: 2010-09-09
Description: A sample template
Resources:
  MyEC2Instance:
    Type: 'AWS::EC2::Instance'
    Properties:
      ImageId: ami-0ff8a91507f77f867
      InstanceType: t2.micro
      KeyName: testkey
      BlockDeviceMappings:
        DeviceName: /dev/sdm
        Ebs:
          VolumeType: io1
          Iops: 200
          DeleteOnTermination: false
          VolumeSize: 20
```

### [Lab: Using AWS CloudFormation](./W11Lab01-AWSCloudFormation.md)

### AWS CDK

AWS Cloud Development Kit (AWS CDK) is an open-source software development framework for defining cloud infrastructure as code. It operates on a construct-based model, where cloud application developers define reusable components that represent AWS resources and assemble them into stacks for deployment. AWS CDK simplifies infrastructure management by providing a higher-level abstraction over AWS CloudFormation templates. AWS CDK creates ready-to-use CloudFormation templates from CDK stacks.

Code that you write using the AWS CDK is converted to CloudFormation templates. CloudFormation provisions these templates as stacks.

With AWS CDK, cloud application developers can use common code development practices. It offers tools to check for potential problems and identify code differences, and bootstrapping resources needed for deployment.

### Benefits of AWS CDK

#### Rapidly incorporating and deploying components that meet your security, compliance, and governance requirements

#### Familiar languages

You can achieve faster deployment by using expressive programming languages for defining infrastructure, such as Python and Java. For example, you can incorporate features such as objects, loops, and conditions to improve the ease with which you can define your infrastructure.

#### Abstracted complexity

AWS CDK simplifies the definition of AWS resources with high-level constructs. You can define high-level abstractions, share them, and publish them to your team, company, or community.

#### Integrated workflow

AWS CDK seamlessly integrates with your preferred integrated development environments (IDEs), providing a unified workflow for both application and infrastructure code. This integrated workflow ensures a consistent and cohesive development experience, fosters collaboration, and reduces context-switching between different tools.

### Core framework of AWS CDK

Three basic components make up the core framework of an AWS CDK project.

1. **Constructs**. Constructs are the basic building blocks that you use to define AWS resources. Constructs are reusable, self-contained components that represent individual AWS resources or groups of resources. AWS CDK includes the AWS Construct Library, which contains constructs representing AWS resources. This library includes constructs that represent all the resources available on AWS. For more information, see [Constructs](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) in the AWS Cloud Development Kit Developer Guide.
2. **Stacks**. A stack is a unit of deployment in AWS CDK that represents a collection of AWS resources. You create a stack from a set of constructs. Stacks permit you to manage and provision a group of related resources together. Stacks can include constructs that define everything from simple resources to entire application architectures. For more information, see [Stacks](https://docs.aws.amazon.com/cdk/latest/guide/stacks.html) in the AWS Cloud Development Kit Developer Guide.
3. **Apps**. Apps are the highest-level construct that represents your entire cloud application. Apps provide a way to define and deploy multiple stacks together, ensuring consistency and maneagability. For more information, see [Apps](https://docs.aws.amazon.com/cdk/v2/guide/apps.html) in the AWS Cloud Development Kit Developer Guide.

#### Example architecture

A cloud application developer interacts with AWS CDK and its three main components (app, stack, and construct) to synthesize a CloudFormation template. Then they deploy AWS resources for their organization's users. In this example, the cloud application developer created a solution that includes Amazon Virtual Private Cloud (Amazon VPC), Elastic Load Balancing (ELB), and Amazon Elastic Container Service (Amazon ECS) services.

### [Lab: Introduction to AWS Cloud Development Kit](./W11Lab02-AWSCloudDevelopmentKitCDK.md)

### Knowledge Check

#### What is a stack in AWS Cloud Development Kit (AWS CDK)? 

* A unit of deployment that represents a collection of AWS resources

Wrong answers:

* A high-level construct that represents your entire cloud application
* A reusable, self-contained component that represents AWS resources
* A file that can be bundled into AWS CDK libraries and apps

A stack is a unit of deployment in AWS CDK that represents a collection of AWS resources. Stacks permit you to manage and provision a group of related resources together.

Apps are the highest-level construct that represents your entire cloud application. Constructs are reusable, self-contained components that represent individual AWS resources or groups of resources. Assets are files, directories, or Docker images that can be bundled into AWS CDK libraries and apps.

#### What is AWS CloudFormation?

* An AWS service for defining and provisioning infrastructure as code

Wrong answers:

* An AWS machine learning service
* An AWS managed source control repository
* An AWS cloud-based integrated development environment (IDE)

AWS CloudFormation is an AWS service for defining and provisioning infrastructure as code.

CloudFormation is not an AWS machine learning service. AWS CodeCommit is a managed source control repository. AWS Cloud9 is a cloud-based IDE that lets you write, run, and debug your code with just a browser.

#### What is the purpose of the Mappings component in an AWS CloudFormation template? 

* To define conditional resource configuration based on key-values

Wrong answers:

* To define values that you can export from the stack
* To declare the version of the CloudFormation template that you are using
* To describe the purpose of the template

Mappings define conditional resource configuration based key-value pairs that you specify. For example, if you want to set values based on a Region, you can create a mapping that uses the Region name as a key and contains the values that you want to specify for each specific Region.

Outputs define values that you can export from the stack for reference or use in other stacks. The format version declares the version of the CloudFormation template that you are using. The description provides human-readable text describing the purpose of the template.

### Summary

#### Introduction to IaC

Infrastructure as code (IaC) involves using code to define and provision infrastructure resources, such as servers, networks, operating systems, and storage. IaC controls these virtualized resources by treating configuration files like source code files. You can use it to manage infrastructure in a codified, repeatable way.

IaC configuration management tools use different language specifications. You can develop IaC similar to application code in Python or Java. You also write the IaC in an integrated development environment (IDE) with built-in error checking. And you can maintain it under source control with commits at each code change. IaC files are included as part of the wider codebase.

#### Benefits of IaC

* Automation and efficiency
* Reusability and speed
* Scalability and flexibility
* Collaboration and productivity

#### Introduction to CloudFormation

You can use AWS CloudFormation to build applications with AWS products without creating or configuring the underlying infrastructure. With CloudFormation, you declare all your resources and dependencies in a template file. CloudFormation templates define a collection of resources as a single unit called a stack. You can manage a collection of resources by creating, updating, or deleting stacks.

#### CloudFormation templates

A CloudFormation template is a JSON or YAML formatted text file. You can save these files with any extension, such as .json, .yaml, .template, or .txt. Templates include several major sections. The Resources section is the only required section. Other sections in a CloudFormation template include the following:

* Format version
* Description
* Parameters
* Mappings
* Conditions
* Transform
* Resources
* Outputs

#### Introduction to AWS CDK

AWS Cloud Development Kit (AWS CDK) is an open-source software development framework for defining cloud infrastructure as code. AWS CDK simplifies infrastructure management by providing a higher-level abstraction over CloudFormation, translating constructs into CloudFormation templates during deployment. Benefits of AWS CDK include the following:

* You can achieve faster deployment by using expressive programming languages such as Python.
* AWS CDK simplifies the definition of resources with high-level constructs.
* AWS CDK seamlessly integrates with your preferred IDEs.

#### Core framework of AWS CDK

The following components make up the framework of an AWS CDK project:

* Constructs are the basic building blocks that you use to define AWS resources.
* A stack is a unit of deployment that represents a collection of AWS resources.
* Apps are the highest-level construct that represents your entire cloud application.

## Software Development Practices

### Pre-assessment

#### Which environment in DevOps hosts the application for end users?

* Production

Wrong answers:

* Development
* Staging
* Testing

The production environment is the *live* environment where the application is hosted for end users.

#### Which branching model in continuous integration and continuous delivery (CI/CD) involves developers building and testing features locally in a feature branch before merging into the main branch?

* Trunk-based development

Wrong answers:

* Shift-left
* Pull request workflow
* Environment parity

In a trunk-based workflow, developers build and test features locally in a feature branch and then merge those changes into the main branch. The main branch is then built to the development, pre-production, and production environments, sequentially. Unit and integration tests occur between each environment.

#### What is a pull request in software development?

* A request made by a developer to merge code changes into a repository

Wrong answers:

* A request made by a project manager to see the latest changes to the code
* A request made by an end user for new functionality in the software
* A request made by a developer to copy a code repository to a local workstation

Pull requests provide a way for repository users to review potential changes to a repository before merging those changes into the repository.

### Environments in Software Development

#### Development

Developers primarily use their local laptops or desktops to run their development environments. This is typically where the integrated development environment (IDE) is installed, where unit tests are run, where source code is checked in, and so on.

Using a source code repository such as CodeCommit, you can find information about a repository and clone it to your computer. This creates a local repository where you can make changes and then push them to the repository. You can work from the command line on your local machine. Alternately, you can use a GUI-based editor, such as AWS Cloud9, Visual Studio, or Eclipse, or any IDE that integrates Git credentials.

In addition to the source code repository, teams often use additional tools, including issue tracking, project tracking, code quality analysis, collaboration, content sharing. Most of the time, those tools are provided as web applications. Like any other classic web application, they require a server to run, and frequently a relational database. The web components can be installed on Amazon Elastic Compute Cloud (Amazon EC2), and the database uses Amazon Relational Database Service (Amazon RDS) for data storage.

#### Testing

There are many software tools and frameworks available for automating the process of running tests. Testing involves provisioning infrastructure resources, initializing the resources with a sample dataset, deploying the software to be tested, orchestrating the test runs, and collecting results.

Test environments should be identical between test runs; otherwise, it is more difficult to compare results.

One challenge is to have enough resources to deploy the complete application with all the different servers or services that it might require. Another challenge is to initialize the test environment with the right software and the right data over and over.

#### Staging

The final functional tests are run in the staging environment before the application is released to production.

The staging environment should mirror the eventual production environment. The staging environment could be a static environment that is pre-made for testing. Or you could provision and configure a dynamic environment with committed infrastructure and configuration code for testing and deploying the application code.

#### Production

The production environment is the *live* environment where the application is hosted for end users.

### Problems with inconsistent environments

As an example, two developers are working on a web application that uses MongoDB for its database. One of them does most of her development on a Linux machine running MongoDB 4.2. the other is on a Windows laptop and uses MongoDB 4.0 for local testing. When the 1st adds new database aggregation functions that are only present in MongoDB 4.2, everything seems to work fine on his/her machine during development. But the other gets errors saying those aggregation functions are undefined.

Environment inconsistencies like this can lead to wasted time, bugs that are hard to diagnose, and assumptions that end up failing in production. Defining and sticking to consistent development, testing, and production environments helps to prevent these kinds of problems.

### Importance of consistent environments

When working with multiple environments in a CI/CD pipeline, it’s important that each environment is as similar as possible. Code developed in one environment should run in another environment. Likewise, testing in one environment should still be accurate when testing the same code in another environment.

### Benefits of using consistent environments

#### Reproducibility

Inconsistent environments can lead to bugs that only happen in certain environments. This makes them hard to trace and fix. Having a consistent environment makes it easier to reproduce bugs or issues, because you know the code is running in the same context every time. Consistent environments make debugging easier.

#### Smoother team workflow

When the whole team uses the same environment, code that any team member writes will work the same way for everyone else. This prevents surprises when pulling new code or deploying to production.

#### Portability

Code developed to run in a consistent, standardized environment is more portable across different machines, servers, or platforms. You avoid dependencies on the peculiarities of any one system.

#### Easier onboarding

New developers can quickly get set up and productive if they can clone a standard environment. This prevents the need to figure out unknown system dependencies and configurations.

#### Streamlined deployment

Pushing code from a consistent development environment to a production or testing environment is less error-prone when you know that the environments closely match. This can help avoid unexpected runtime failures.

### Best practices for managing environments

You can standardize and automate the process for setting up local development environments using managed services, IaC, and scripted automation. This approach permits environments to be reliably replicated across different systems and teams, and ensures uniformity. Setting up a consistent local environment helps to eliminate issues with something working on one machine but not another.

Consider the following best practices for creating consistent environments:

* Create a baseline configuration for your local development environment that mirrors the production setup as closely as possible.
* All IaC and scripts should be version controlled, so that any changes are tracked, and can be rolled back if necessary.
* Create documentation on how to set up and troubleshoot provisioned environments.
* Regularly review and update the baseline configuration to keep it aligned with changes in the production environment.

### Automated Testing

### Testing and DevOps

With frequent code check-ins, you can close the feedback loop with quality by having a good testing strategy as part of your CI/CD pipeline. Keeping a robust pipeline ensures that you can continue to deliver quality products and features faster.

Tests help find issues early in the development phase, when fixes are less costly than later during the project.

Tests come in many forms: unit tests, performance tests, user acceptance tests, or integration tests. All tests require IT resources to run. Test environments change frequently and are different from project to project. As a result, test environments might require different IT infrastructure or have varying capacity needs. Though adding software features at a rapid pace is a good practice, ensuring that the features adhere to the right level of quality is achieved by continuous testing.

**Quality of a software product is everyone's responsibility.**

#### Example development lifecycle with testing integrated

 -> Develop -> Test -> Build -> Test -> Deploy -> Test -> Release -> Test ->

Development lifecycle with testing taking place between the develop, build, deploy, and release phases.

### Testing scenarios in the CI/CD pipeline

#### Continuous Integration

1. Development
 1.1. Unit tests
 1.2. Static code analysis
2. Build
 2.1. Integration testing
 2.2. Component testing.
 2.3. Regression testing.

#### Continuous Delivery and Deployment

3. Stage
 3.1. System testing.
 3.2. Performance testing.
 3.3. Load testing.
 3.4. Compliance testing.
 3.5. User acceptance testing.
4. Production
 4.1. A/B testing.
 4.2. Canary analysis.

#### Development phase

Developers perform unit tests to test code changes and new features. This is usually done on a developer’s machine after coding is complete. It is also a good practice to run a static code analysis on the code changes. This means analyzing the code without running it, sometimes with the help of automated tools, with the goal of detecting bugs, security vulnerabilities, and coding errors.

#### Build phase

The build phase is an appropriate phase to test for integration between different components and individual components themselves. This is also a good time to test whether the code committed by a developer breaks any existing features. This is called regression testing.

#### Stage phase

A staging environment is a replica of the production environment. A complete system test is performed at this stage. UI, backend logic, and API are tested extensively. Performance testing tests the application performance under a particular workload. Types of performance tests include load tests, stress tests, and spike tests. User acceptance testing is also performed at this stage to prepare for production deployment. Compliance testing is done to test for industry-specific regulatory compliance.

#### Production phase

In the production phase, a strategy, such as A/B testing or canary analysis, is used to test the new application version. In A/B testing, the new application version is deployed to a small percentage of production servers and tested for user feedback. Depending on how well the new application is received by the users, the deployment is gradually increased to span all production servers.

### Unit Testing

Unit testing is the process where you test the smallest functional unit of code. Software testing helps ensure code quality, and it's an integral part of software development. It's a software development best practice to write software as small, functional units and then write a unit test for each code unit.

You can first write unit tests as code. Then run that test code automatically every time that you make changes in the software code. This way, if a test fails, you can quickly isolate the area of the code that has the bug or error.

Unit testing enforces modular thinking paradigms and improves test coverage and quality. Automated unit testing helps provide more time for you and your team to concentrate on coding.

For example, an application built with a user interface and a collection of interconnected microservices. Microservices are an architectural and organizational approach to software development where software is composed of small, independent services that communicate over well-defined APIs. Each microservice is made up of functions. A unit in a unit test is an individual function or small collection of functions that make up a block of code.

A *unit test* is a block of code that verifies the accuracy of a smaller, isolated block of application code, typically a function or method. The unit test is designed to check that the block of code runs as expected, according to the developer’s theoretical logic behind it. The unit test is only capable of interacting with the block of code using inputs and captured asserted (true or false) output.

A single block of code can also have a set of unit tests, known as test cases. A complete set of test cases covers the full expected behavior of the code block, but it’s not always necessary to define the full set of test cases.

When a block of code requires other parts of the system to run, you can’t use a unit test with that external data. The unit test must run in isolation. Other system data, such as databases, objects, or network communication, might be required for the code’s functionality. If that's the case, you should use data stubs instead. It’s easiest to write unit tests for small and logically simple blocks of code. A *data stub* is a simulated object that stands in for real data while running a test. Data stubs permit developers to test units in isolation without requiring dependencies on external systems or data stores.

### Unit testing strategies

### Basic techniques to ensure coverage of all test cases

#### Logic checks

Does the system perform the right calculations and follow the right path through the code, given a correct, expected input? Are all paths through the code covered by the given inputs?

#### Boundary checks

For the given inputs, how does the system respond? How does it respond to typical inputs, edge cases, or inputs that are not valid?

For example, consider a scenario in which you expect an integer input between 3 and 7. How does the system respond when you use a 5 (typical input), a 3 (edge case), or a 9 (not valid)?

#### Error handling

When there are errors in inputs, how does the system respond? Is the user prompted for another input? Does the software crash?

#### Object-oriented checks

If the state of any persistent objects is changed by running the code, is the object updated correctly?

### Benefits of unit testing

#### Efficient bug discovery

If there are any input, output, or logic-based errors within a code block, your unit tests help you catch them before the bugs reach production. When code changes, you run the same set of unit tests—alongside other tests such as integration tests—and expect the same results. If tests fail (also called broken tests) it indicates regression-based bugs.

Unit testing also helps finds bugs faster in code. Your developers don’t spend a large amount of time on debugging activities. They can quickly pinpoint the exact part of the code that has an error.

#### Documentation

It's important to document code to know exactly what that code is supposed to be doing. That said, unit tests also act as a form of documentation.

Other developers read the tests to see what behaviors the code is expected to exhibit when it runs. They use the information to modify or refactor the code. Refactoring code makes it more high performing and well composed. You can run the unit testing again to check that code works as expected after changes.

### Unit testing and DevOps

Unit testing in DevOps is continuous, comprehensive, and collaborative, and provides fast feedback to support continuous delivery of software. It facilitates reliable, rapid releases while giving developers confidence that changes will not introduce regressions.

Traditional approaches to software development might focus unit testing only on critical components. In DevOps, there is a greater emphasis on having comprehensive unit test coverage across the entire codebase. Unit tests in DevOps run much more frequently, often on every code commit as part of continuous integration. In traditional development, unit tests might only be run before major releases.

Unit tests can be automated to run on every code change as part of the CI/CD pipeline. They make up part of the test suite alongside integration testing.

### Shift-Left Approach to Software Testing

The traditional approach to testing involves separate quality assurance (QA) and development teams. Testing is seen as a separate phase at the end of the development lifecycle. Tests are manually written and run by the QA team right before major releases.

This traditional approach has several key disadvantages, including the following:

* Testing happens too late, leading to defects discovered late in the process. This makes them costly to fix.
* Testing is slow and done manually. There is limited test automation.
* Tests have limited scope and coverage. Critical areas might be missed.
* There is siloed knowledge between development and QA teams. Collaboration is limited.
* There is no culture of building quality in from the start.

The traditional testing approach does not work with DevOps because DevOps relies on fast feedback loops and continuous testing to facilitate continuous delivery. In DevOps, tests are automated to keep pace with rapid changes. Test coverage is broad across the codebase, and there is strong collaboration between development, QA, and operations teams. DevOps fosters a culture of quality with testing responsibility across roles.

The traditional siloed and manual testing approach cannot keep up with the release velocity and automation needed for DevOps and continuous delivery environments.

#### Shift-left approach

During the DevOps lifecycle, there are multiple opportunities to test cloud applications. The *shift-left approach* refers to integrating testing earlier in the software development lifecycle. The shift-left approach means to move testing to as far left in the lifecycle as possible, to catch bugs as early as possible. It is much easier and less costly to fix on a local developer machine than it is to patch in production.

**Best time to catch bugs is during development. Shift testing left as far as possible. Worst time to catch bugs is deployment.**

At the very left of the DevOps cycle is where developers perform the traditional software testing responsibilities, such as unit tests. With cloud applications, there is also a responsibility at this stage to ensure that there are no security, configuration, or compliance vulnerabilities. Developers and subsequent peer reviewers looking at the code can do this manually; but in this way, it is hard to catch every piece of bad code or misconfigured resource. After deployment, potential security risks are now live. Without proper monitoring, these misconfigurations can go undetected, with potentially dire consequences if exploited.

By following the shift-left process, software teams can help prevent undetected security issues and bugs when they build an application. The modern DevOps workflow continues to shift left towards the developer and their practices to achieve the following goals:

* Drive accountability among developers for the security of their code.
* Empower development teams to remediate issues up front and at their own pace.
* Improve risk management by providing early visibility of potential security issues through early feedback loops.

#### Tools for shift-left testing

You can use AWS developer tools to help provide continual early feedback. For example, Amazon Q Developer can provide actionable security findings and best practices as you write your code.

You can integrate Amazon CodeGuru Reviewer with your code repository to initiate a code scan when you submit a pull request. CodeGuru Reviewer uses program analysis and machine learning to help detect potential defects in your Java and Python code, and provides recommendations to improve the code. CodeGuru Reviewer helps detect security vulnerabilities, secrets, resource leaks, concurrency issues, incorrect input validation, and deviation from best practices for using AWS APIs and SDKs.

You can also configure the AWS CodeBuild deployment with third-party tools, such as Bandit for Python, to help detect security issues in your Python code. CodeGuru Reviewer and CodeBuild write back the findings of the code scans to the pull request to provide a single common place for developers to review the findings that are relevant to their specific code updates.

Additionally, there are several tools that can scan CloudFormation templates and detect infringements against security best practices, such as cfn_nag, AWS CloudFormation Guard, and Trend Micro Cloud One Conformity. These can be run from the command line on a developer’s machine, inside the IDE, or during a git commit.

### Using a Trunk-Based Workflow

Trunk-based development is a branching strategy and a version-controlled management practice. Developers make code changes through frequent, small commits to a single shared branch, known as a trunk, in the source code repository.

*Trunk-based* workflow has replaced the *Gitflow* branching model, in which development and release branches are separated by a release schedule. The challenge of the Gitflow approach is that developers often wait until a feature is finished before merging its branch into the shared main branch. This delay can cause the application environments to fall out of sync.

#### Challenges in Gitflow branching model

* Delays developing a feature can cause the application environments to fall out of sync.
* When these environments are out-of-sync, it requires more effort and collaboration to merge the branches.
* If branches deviate from the shared main branch, it can cause potential update conflicts.
* Dealing with defects in the production environment can be difficult in Gitflow since Developers can't just merge their current code into production because it might expose unfinished features.
* To fix bugs in production, Gitflow uses hotfixes - quick patches created from the release branch that are deployed straight into the pre-production and production environments. These hotfix branches then get merged into the development branch so that the code is up-to-date. Managing all of these extra branches makes the development process more complicated.

#### Trunk-based development

* Developers typically merge their code changes directly to a shared trunk every day. This shared trunk is always in a releasable state. Regardless of individual actions within their local repositories, developers must merge their code at least once each day.
* Developers can continually observe and respond to the changes made by their teammates in a version-controlled environment. This practice also drives continuous collaboration around the quality and condition of the codebase.
* Trunk-based development is also more streamlined than Gitflow because it relies on the main branch as the source of fixes and releases. In trunk-based development, the main branch is always stable, without issues, and ready to deploy.
* The key advantage lies in providing the team with enhanced flexibility and control over the software delivery process to end users.

In a trunk-based workflow, developers build and test features locally in a feature branch, and then merge those changes into the main branch.

Short-lived branches are used to commit changes and then they are merged with the main (or trunk) branch. The branches are merged frequently and do not persist after they are merged.

In this workflow, all environments are operating the same code base. There is no need for a hotfix branch for the upper environments because you can implement changes in the main branch without exposing unreleased features. The main branch is always assumed to be stable, free of defects, and ready to release. This helps you integrate it as a source for a CI/CD pipeline, which can automatically test and deploy your code base through all environments in your pipeline.

After each merge, the main branch is then built to the development, staging, and production environments, sequentially. Unit and integration tests occur between each environment.

The following are some best practices for trunk-based development:

* Maintain a single mainline branch (trunk) that serves as the source of truth for the codebase. All work should branch from and merge back to the trunk.
* Keep the trunk releasable at all times. Anything going into the trunk should be complete, tested, and functional enough to release if necessary.
* Use short-lived feature branches off of the trunk for any work in progress. Merge back frequently, at least daily.
* Use pull requests and code reviews before merging anything into the trunk. This provides quality control.
* Run a full CI/CD pipeline on every trunk commit. It should build, test, scan, and validate each change.
* Fix issues quickly if anything breaks in the trunk. The team should maintain a policy of reversing problematic commits.
* Automate merges to the trunk after approvals, and delete old feature branches after they are merged. Don't accumulate stale branches.
* Release directly from the trunk on a regular schedule, such as weekly or biweekly. The contents of the trunk are the next release.
* Communicate changes going into the trunk. Keep the team aware of what's happening.
* Provide access and merge ability to the trunk for the entire team, so that everyone contributes to the mainline.
* Maintain well-defined coding standards and architecture for the trunk. Refactor as needed.
* Use small atomic commits for easier reviewing and reverting back if needed.

### AWS CodeCommit pull requests

### Typical workflow for a pull request

Pull requests provide a way for repository users to review, comment on, and interactively iterate on code changes.

In AWS CodeCommit, a pull request is a mechanism for proposing and discussing changes to the codebase in a repository. You and other repository users can review, comment on, and merge code changes from one branch to another. You can use pull requests to collaboratively review code changes for minor changes or fixes, major feature additions, or new versions of your released software.

* You are working in a repo and want to work on a new feature for an upcoming version of a product. You create a feature 1 branch so that you can keep your work separate from the production- ready code. You start writing code, make commits, and push the new feature code into this feature 1 branch. You now want your coworkers to review the code for quality before merging these changes into the default branch. This default branch is called main branch.
* Create a pull request. The pull request contains the comparison between your feature 1 branch and the main branch.
* Other repo users will review your code and changes, and they will add comments and suggestions. With these comments and suggestions, you might update your code in the feature 1 branch multiple times in response to comments. Your changes are incorporated into the pull request every time you push them to the feature 1 branch in CodeCommit.
* When you and your reviewers are satisfied, you or one of your reviewers can merge your code back to the main branch and close the pull request.

#### Workflow example in CodeCommit console

* In **Repositories**, choose the name of the repository where you want to create a pull request.
* In the navigation pane, choose **Pull requests**.
* Choose **Create pull request**.
* In **Create pull request**, **Source** dropdown menu, choose the branch that contains the changes you want reviewed.
* In **Destination** dropdown menu, choose the branch where you intend to merge your code changes when the pull request is closed.
* Choose **Compare**. A comparison runs on the two branches, and the differences between them are displayed. An analysis is also performed to determine whether the two branches can be merged automatically when the pull request is closed.
* Review the comparison details and the changes to be sure that the pull request contains the changes and commits you want reviewed. If not, adjust your choices for the source and destination branches, then choose **Compare** again.
* Green lines with plus signs are the new lines of code you added to the feature1 branch. Red line with the minus sign is the line you deleted from the feature1 branch.
* When you are satisfied with the comparison results for the pull request, in **Title**, enter a short but descriptive title for this review. This is the title that appears in the list of pull requests for the repository.
* In **Description**, enter details about this review and any other useful information for reviewers.
* Choose **Create pull request**.

Other repo users can now review your code and changes. In this demo, let’s take a look at how others can review your code. Note that this demo uses a different AWS Identity and Access Management, or IAM, user to simulate the reviewer’s view.

* In **Repositories**, choose the name of the repository.
* In the navigation pane, choose **Pull requests**.
* By default, a list of all open pull requests is displayed. Choose the open pull request you want to review.
* In the pull request, choose **Changes**.
* You can add comments to the pull request in different ways. The following are some examples:
 * If you want to add a general comment for the entire pull request, in **Comments on changes**, in **New comment**, enter a comment, and then choose **Save**.
 * If you want to add a comment to a changed line in the pull request, go to the line you want to comment on. Choose the comment icon that appears for that line, enter a comment, and then choose **Save**.

After others have reviewed and commented on your pull request, you can review these comments and start making the suggested changes. To review the list of review comments, go to the **Activity** tab or the **Change** tab. The **Activity** tab shows the history of the pull request, including commits and comments.

The **Changes** tab shows the comments for the latest commit. It’s because comments on previous commits might be associated with lines that have changed or been removed in the current commit. Comments for previous commits are available to view and reply to in the **Activity** tab.

Now you are ready to address the comments made by the reviewers. If you are no longer pointing to the feature1 branch, check out the feature1 branch by running the following command:

```
git checkout feature1
```

Edit the source code in your favorite IDE and make the changes to address the comments.  After saving the changes, commit and push to the CodeCommit feature1 branch as you did previously with the following commands:

```
git commit -am "updated based on review comments"
git push origin feature1
```

In these commands, **-am** is a power user shortcut that combines the **-a** and **-m** options. **-a** is an option that commits a snapshot of all changes in the working directory. This only includes modifications to tracked files. **-m** is an option that immediately creates a message for the commit.

With the **-am** combination, it immediately creates a commit of all the staged changes and takes an inline commit message.

Now that you’ve fixed the code issues, you will want to respond to the review comments. In the CodeCommit console, check that your latest commit appears in the pull request **Commits** tab. You now have a pull request consisting of more than one commit.

To reply to comments on a commit, in **Changes** or **Activity**, choose **Reply**. You can reply with text and emojis. You can react and view the names of your reviewers.

At this stage, your code has been committed and you’ve updated your pull request comments, so you are ready for a final review and merging a pull request.

One of the reviewers that own the main branch provides the final review on the code changes and comments you made. If they are approved, merging a pull request is next. After the status of a pull request is changed to **Merged**, it no longer appears in the list of open pull requests. A merged pull request is categorized as closed. It cannot be changed back to Open, but users can still comment on the changes and reply to comments. Let’s take a look how to merge a pull request in the CodeCommit console. Merging can be done by you or one of the reviewers.

#### To merge a pull request:

* In **Repositories**, choose the name of the repository.
* In the navigation pane, choose **Pull requests**.
* By default, a list of all open pull requests is displayed. Choose the open pull request you want to merge.
* Choose **Merge**.
* In the pull request, choose between the available merge strategies. Merge strategies that cannot be applied appear greyed out. If no merge strategies are available, you can choose to manually resolve conflicts in the CodeCommit console, or you can resolve them locally using your Git client.

In this case, the **three-way merge** is used. You will review the automatically generated commit message and modify it if you want to change the information. Add your name and email address for the commit history.

Choose **Merge pull request** to complete the merge. Now, when you go back to the main branch, you will notice the changes have been merged. And if you go back to Pull requests, there is no result to display because the pull request has been closed.

Pull requests are used as a collaboration tool between team members, and they help you to review potential changes to a repository before merging those changes into the repository.

1. **Commits to feature branch**. You want to work on an updated version of an application. To keep your work separate from production code during development, you create a new feature branch. You write code, make commits, and push the updated code to the feature branch that you created. The commits are not yet merged into the main branch.
2. **Pull request**. When your updates are ready for review, you create a pull request for this branch. The pull request contains a comparison between your working branch and the original branch of the code. Other users review the updated code and add comments and suggestions. Additionally, automated testing can be integrated to add comments to the pull request.
3. **Additional commits**. You incorporate the feedback and update the code according to the comments. Changes are incorporated into the pull request every time you push the updated code to the branch.
4. **Merge**. When the feedback is addressed and code updates are approved (if required), you merge the feature and main branches and close the pull request.
5. **Deletion**. After merging commits with the main branch, you can choose to delete the feature.

Commenting is an integral part of the pull request process, and is used to collaborate between the developers and the reviewer. Reviewers add comments and questions to a pull request during the review process, and developers respond to these with explanations. Pull request comments can be added to the overall pull request, a file within the pull request, or a line within a file.

When creating a pull request, you can create an approval rule and specify a pool of users who can provide approval.

When users comment on pull requests using CodeCommit, AWS Identity and Access Management (IAM) usernames are associated with comments to indicate who authored them. Comments provide a record of the discussion.

### Knowledge Check

#### In software development, what is the staging environment used for?

* Running final tests before deploying to production

Wrong answers:

* Developing and writing new code
* Storing backups of the production environment
* Providing users a preview of upcoming changes

In the staging environment, the final functional tests are run before the application is released to production.

#### What is the shift-left approach to software testing?

* Testing software earlier in the development lifecycle, as code is developed

Wrong answers:

* Testing software later in the development lifecycle, closer to deployment
* Automating more tests to run faster
* Testing by end users

The shift-left approach involves moving testing earlier into the software development lifecycle. This means starting testing activities like unit testing and integration testing sooner, during code development rather than after. The goal is to detect defects and issues earlier, which reduces cost and time to fix compared to finding issues later in development or production.

#### What is unit testing?

* Testing an individual component or module of code in isolation from the rest of the system

Wrong answers:

* Running automated tests on the fully integrated system
* Collecting data from end users to determine if the application is working as expected
* Testing how well the production system handles expected and unexpected user loads

Unit testing is the process where you test the smallest functional unit of code.

### Summary

#### Environments in software development

An environment refers to the hardware, software, data, and configurations that a software system runs on.

The following are the primary environment types:

* **Development**: Where developers write and test code locally
* **Testing**: Automates running tests on cloned environments
* **Staging**: Final tests before releasing to production
* **Production**: Live environment for end users

Consistent environments make debugging easier, facilitate faster onboarding, reduce surprises, and streamline deployment.

#### Automated testing

DevOps permits rapid delivery of new features while maintaining quality through continuous testing as part of the CI/CD pipeline.

##### Development phase

In the development phase, developers perform unit tests and static code analysis.

##### Build phase

In the build phase, integration and regression testing occurs.

##### Stage phase

In the stage phase, full system, performance, user acceptance, and compliance testing occurs.

##### Production phase

In production, new versions are tested with a small percentage of users first through A/B or canary testing, before full deployment.

#### Unit testing

Unit testing is the process of testing the smallest functional pieces of code, typically functions or methods. It helps ensure code quality and is an integral part of software development best practices.

Unit tests are written to test code in isolation, without external dependencies. Data stubs can be used when external data is required.

Unit testing strategies include logic checks, boundary checks, error handling, and object-oriented checks.

Benefits of unit testing include efficient bug discovery, documentation, modularization, and increased confidence in code changes.

Overall, unit testing improves test coverage, saves debugging time, and permits developers to refactor code with confidence. It's considered a software development best practice.

#### Shift-left approach to software testing

The shift-left approach in DevOps refers to moving testing earlier in the software development life cycle to catch bugs and issues as early as possible. It is easier and cheaper to fix bugs earlier on rather than after deployment.

Developers perform testing like unit tests at the start of the DevOps cycle. They should also check for security, configuration, and compliance issues at this stage before code is deployed.

The shift-left approach aims to achieve the following goals:

* Make developers accountable for writing secure code
* Let developers fix issues early on
* Provide early feedback on potential security risks

AWS tools like Amazon Q Developer and Amazon CodeGuru can provide feedback on security as code is written. Other tools can scan CloudFormation templates to detect security risks.

The key goals are to prevent undetected issues and empower developers to find and fix problems early in the process before deployment.

#### Trunk-based development

The following is a summary of the key points about trunk-based development workflows:

* Developers build features in local feature branches, then merge into a main branch.
* The main branch is built through development, pre-production, and production environments, with tests between.
* All environments use the same main codebase. No hotfix branches are needed.
* The main branch is always releasable, stable, and defect-free. This is good for CI/CD.

#### AWS CodeCommit pull requests

Pull requests let users review, discuss, and iterate on proposed code changes before merging them into a repository.

Pull requests go through a lifecycle. Changes are committed to a feature branch, a pull request is opened comparing the feature branch to the destination branch, and team members review and comment. And when it is approved, the pull request is merged into the destination branch.

Commenting is an integral part of the process, facilitating collaboration between developers and reviewers. Comments can be added to the overall pull request, specific files, or lines of code.

Approval rules can be set to specify required approvers before merging.

A typical workflow involves creating a feature branch, developing and committing changes, opening a pull request for review, incorporating feedback by additional commits, and finally merging after approval.

### Additional Resources

#### [AWS Cloud Development Kit (AWS CDK) v2](https://docs.aws.amazon.com/cdk/v2/guide/home.html)

#### [Code Coverage Reports](https://docs.aws.amazon.com/codebuild/latest/userguide/code-coverage-report.html)

#### [What Is Unit Testing?](https://aws.amazon.com/what-is/unit-testing/)

#### [Implement an Early Feedback Loop with AWS Developer Tools to Shift Security Left ](https://aws.amazon.com/blogs/security/implement-an-early-feedback-loop-with-aws-developer-tools-to-shift-security-left/)

#### [Working with Pull Requests in AWS CodeCommit Repositories](https://docs.aws.amazon.com/codecommit/latest/userguide/pull-requests.html)

#### [10 Ways to Build Applications Faster with Amazon Q Developer](https://aws.amazon.com/blogs/devops/10-ways-to-build-applications-faster-with-amazon-codewhisperer/)
