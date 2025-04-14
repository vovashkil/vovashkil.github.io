# Week 1: DevOps 2: Automate Testing with AWS CodeBuild

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to [AWS Cloud Operations 2](./aws-cloud-operations-2.md)
* back to repo's main [README.md](../../../README.md)

## DevOps 2: Automate Testing with AWS CodeBuild

### Pre-assessment

#### Which source repositories are supported by AWS CodeBuild? (Select TWO.)

* Amazon CodeCatalyst
* GitHub

Wrong answers:

* AWS CodePipeline
* Amazon Elastic Container Registry
* Amazon CodeGuru

##### Explanation

The source repositories supported by CodeBuild include Amazon CodeCatalyst, GitHub, Bitbucket, and Amazon Simple Storage Service (Amazon S3). CodeBuild can use webhooks and integrations to connect to common Git-based sources, like GitHub and Bitbucket, to automatically initiate builds on source code changes. Amazon S3 and CodePipeline support packaging code for convenient use in CodeBuild.

The other options are incorrect because of the following reasons:

* CodePipeline is a service for automating software release pipelines, not a source code repository. CodeBuild integrates with CodePipeline, but CodePipeline is not a source repo.
* Amazon Elastic Container Registry (ECR) is a fully managed container registry that offers high-performance hosting. It is not a source code repository.
* CodeGuru is a service that provides code reviews and recommendations, but it is not a source code repository that CodeBuild can directly pull code from.

#### Which of the following describes testing that verifies that an application is meeting the specified requirements and performs the expected actions?

* Functional testing

Wrong answers:

* Integration testing
* Performance testing
* Unit testing

##### Explanation

These tests often involve simulating user interactions with the application and validating the outputs. AWS CodeBuild makes it easy to incorporate functional tests into the build pipeline, ensuring that the application is continuously tested for correct functionality.

The other options are incorrect because of the following reasons:

* Integration testing identifies issues that might arise when individual units are combined into a complete system. It focuses on verifying that different components of the application work together correctly.
* Performance testing focuses on evaluating an application's performance characteristics, such as response times, throughput, and scalability.
* Unit testing helps catch bugs early in the development process and ensures that individual pieces of the application are functioning as expected. This refers to testing individual components or units of the application in isolation.

#### Which of the following is NOT a benefit of AWS CodeBuild?

* Manual deployments

Wrong answers:

* Continuous integration
* Flexible build environments
* Fully managed service

##### Explanation

AWS CodeBuild automatically sets up the test environment based on the programming language and framework used in the application. It provides preconfigured build environments for various runtimes, making it possible to focus on writing the tests without having to worry about the underlying infrastructure.

The other options are incorrect because they accurately describe benefits of CodeBuild.

## AWS CodeBuild

AWS CodeBuild is a fully managed continuous integration service that compiles source code, runs tests, and produces ready-to-deploy software packages.

With CodeBuild, you don’t need to provision, manage, and scale your own build servers. You specify the location of your source code and choose your build settings, and CodeBuild will run your build scripts for compiling, testing, and packaging your code.

![CodeBuild Diagram](./images/W01Img020CodeBuildDiagram.png)

Diagram depicting workflow using AWS services: Public source code repositories feed into AWS CodeBuild which compiles code, runs tests, generates artifacts without retaining source/credentials. Integrates with AWS Secrets Manager for secure environment, ECR for container images, KMS for encryption keys, VPC for network isolation. Final stages are storing artifacts on Amazon S3 and monitoring with Amazon CloudWatch.

A "build" refers to the process of converting source code into a runnable software application. This process typically includes compiling the code, running tests to ensure it works correctly, and packaging it into a deployable format. The "build" is an essential step in software development to ensure that the code is functional and ready for deployment.

### AWS CodeBuild Benefits

#### Scalability

![CodeBuild Scalability Slide](./images/W01Img032CodeBuildScalability.png)

#### Managed Builds

![CodeBuild Managed Builds Slide](./images/W01Img034CodeBuildManagedBuilds.png)

#### Flexible Build Environments

![CodeBuild Flexible Build Environments Slide](./images/W01Img036CodeBuildFlexibleBuildEnvironments.png)

#### Continuous Integration

![CodeBuild Continuous Integration Slide](./images/W01Img038CodeBuildContinuousIntegration.png)

#### Security and Compliance

![CodeBuild Security and Compliance Slide](./images/W01Img040CodeBuildSecurityCompliance.png)

### Using CodeBuild

CodeBuild is a fully managed continuous integration service that compiles source code, runs tests, and produces ready-to-deploy artifacts, such as Docker images. CodeBuild fits squarely into the CI/CD landscape by providing a scalable and configurable build environment that can be seamlessly integrated with other AWS services like CodePipeline, Amazon Elastic Container Registry (ECR), and AWS Lambda to create end-to-end CI/CD workflows.

1. Prepare your source code

    Store your application's source code in an AWS CodeCatalyst repository, an Amazon S3 bucket, or a third-party repository like GitHub or Bitbucket.

2. Create a buildspec.yml file

    This file defines the build instructions - the commands to run, the build environment to use, and any output artifacts to produce.

3. Create a CodeBuild project

    In the AWS Management Console, define a CodeBuild project that points to your source code location and uses the buildspec.yml file.

4. Start a build

    Initiate a build by pushing new code to your source repository, using the AWS CLI, or integrating with other AWS services like CodePipeline.

5. Monitor and troubleshoot

    Use the CodeBuild console, CloudWatch logs, and build reports to monitor your builds and debug any issues.

By using the benefits of AWS CodeBuild, development teams can significantly accelerate their software delivery lifecycle. The on-demand scalability and automated provisioning of build environments facilitates developers to spend more time coding and testing, instead of managing build infrastructure. With the configurable build specifications, teams can quickly iterate on their build and test processes, and the tight integration with other AWS services streamlines the overall CI/CD workflow.

### Types of Testing in AWS CodeBuild

AWS CodeBuild is a fully managed continuous integration (CI) service provided by Amazon Web Services (AWS). It compiles source code, runs tests, and produces software packages that are ready to deploy. One of the key features of CodeBuild is its support for various types of testing to ensure the quality and reliability of your application.

#### Unit Testing

Unit tests help catch bugs early in the development process and ensure that individual pieces of the application are functioning as expected. This refers to testing individual components or units of the application in isolation. CodeBuild makes it easy to integrate unit tests into the build process, allowing you to automatically run the tests as part of every build.

#### Integration Testing

Integration testing focuses on verifying that different components of the application work together correctly. This type of testing helps identify issues that may arise when individual units are combined into a complete system. CodeBuild provides the ability to run integration tests as part of the build process, helping to catch integration-related bugs before the application is deployed.

#### Functional Testing

Functional tests verify that the application is meeting the specified requirements and performing the expected actions. These tests often involve simulating user interactions with the application and validating the outputs. CodeBuild makes it easy to incorporate functional tests into the build pipeline, ensuring that the application is continuously tested for correct functionality.

#### Performance Testing

Performance testing focuses on evaluating the application's performance characteristics, such as response times, throughput, and scalability. By running performance tests as part of the build process, you can identify and address performance issues before they impact the end-users.

AWS CodeBuild provides a flexible platform for running a wide variety of testing as part of your build process. Each of these testing types plays a crucial role in ensuring the quality and reliability of your application. By using the capabilities of AWS CodeBuild, you can automate these tests as part of your continuous integration and delivery (CI/CD) workflow, helping to catch issues early and deliver high-quality software faster.

### [Lab: Using AWS CodePipeline for Unit Testing](./labs/W010Lab2CodePipelineForUnitTesting.md)

After you update the application, you commit the changes and push the updates to the PresidentsApp code repository. The Presidents-Pipeline is invoked again. After the unit test completes successfully, the application update is deployed using CodeDeploy. Finally, you verify that the application calculates the ages correctly.

In this lab, you will perform the following tasks:

* Verify that the unit test passes.
* Update the Presidents application to calculate the ages of the presidents by using the relative delta type.
* Push changes to the PresidentsApp code repository.
* Verify that the application calculates the ages correctly after the pipeline finishes the new unit testing and deployment stages.

### Knowledge Check

#### How can AWS CodeBuild be configured to perform application testing?

* Configure unit testing using a specified testing framework

Wrong answers:

* Configure a fully automated pipeline for continuous integration and continuous deployment (CI/CD)
* Configure static application testing on the build environment
* Configure Virtual Studio for automated machine learning (ML) application testing

##### Explanation

 With AWS CodeBuild, users can configure unit testing using a specified testing framework. The service supports various programming languages, such as Java, Node.js, Python, and Ruby. Users can create custom build workflows and specify the unit testing framework along with the required dependencies.

The other options are incorrect because of the following reasons:

* Although CI/CD pipelines involve testing, the question specifically asks about configuring CodeBuild for application testing, not the full pipeline setup.
* Static application testing only covers static testing, whereas the question asks about application testing in general, which can include dynamic testing, as well.
* Virtual Studio for automated ML application testing is unrelated.

#### What is the purpose of the buildspec.yml file in AWS CodeBuild?

* Defines the build environment and build steps

Wrong answers:

* Configures the AWS CodeBuild service
* Specifies the application's runtime dependencies
* Activates the CodeBuild build project

##### Explanation

The buildspec.yml file is used to define the build environment and the build steps to be carried out in an AWS CodeBuild project. It specifies the commands to be run, the artifacts to be produced, and other build-related configurations.

The other options are incorrect because of the following reasons:

* The buildspec.yml file does not configure the overall CodeBuild service itself. The CodeBuild service is configured through the AWS Management Console, AWS Command Line Interface (AWS CLI), or AWS CloudFormation templates.
* The buildspec.yml file does not specify runtime dependencies for the application. Those would typically be listed in a separate file, like package.json for Node.js apps or requirements.txt for Python apps.
* The buildspec.yml file does not activate the CodeBuild project build. The build is activated by pushing code commits to the associated AWS CodeCommit repository, by updating the Amazon Simple Storage Service (Amazon S3) input bucket, or manually running the build through the AWS Management Console or AWS CLI.

#### How does AWS CodeBuild perform application testing?

* Automatically after building the application

Wrong answers:

* Manually with manual tests
* By running automated tests on the compile code only
* By running automated tests on the compile code, deployment infrastructure, and built assets

##### Explanation

AWS CodeBuild inherently integrates with the necessary tools required to run automated tests on the build assets, as well as the deployment code and infrastructure. Then, it can perform holistic application testing.

The other options are incorrect because of the following reasons:

* AWS CodeBuild is designed to automate the build and testing process, not rely on running tests manually.
* AWS CodeBuild can run automated tests on both the compiled code and other stages of the build process, not only the compiled code.
* AWS CodeBuild focuses on building and testing the application code, whereas testing deployment infrastructure and built assets is typically handled by other services, like AWS CodePipeline or AWS CodeDeploy.

### Summary

#### Review of AWS CodeBuild

AWS CodeBuild is a fully managed build service that compiles source code, runs tests, and produces software packages that are ready for deployment. It supports a wide range of programming languages and build tools, so developers can effortlessly integrate it into their existing build and test workflows. One of the key features of AWS CodeBuild is its ability to perform application testing. It can run various types of tests, including unit tests, integration tests, and end-to-end tests, as part of the build process. The test results are captured and reported back to the developer, providing valuable insights into the quality of the application.

#### Types of Testing in AWS CodeBuild

AWS CodeBuild is a fully managed build system that operates as a service, meaning you don't need to invest in setting up, configuring, and maintaining specialized server/compute infrastructures to serve as your build environment. CodeBuild can automatically select from multiple AWS regions to run your builds and uses AWS security controls to protect your repositories and builds. Here are the types of testing supported by AWS CodeBuild:

* **Unit tests** – Unit tests are run against individual units of code (functions, methods, or classes) to check their correctness.
* **Integration tests** – These tests confirm that the system works correctly in its integration, that is, in its complete form. This type of testing is run against the integration points (that is, the communicate between systems or database access).
* **End-to-end tests** – In relative terms, these tests are similar to integration tests, but they go one step further. Your system is exposed to complete end-user scenarios and interactions.
* **Documentation Automated tests** – These tests aim to validate your code against written functional and non-functional requirements by checking the code documentation (comments and code comments & docstrings in Python).

#### Configure AWS CodeBuild for Application Testing

To effectively perform application testing using AWS CodeBuild, it's essential to follow a systematic setup process.

1. Create a build project in the CodeBuild console, choose your source code repository, and select a build image that contains your desired test tools and runtimes.
2. In the buildspec.yml file, define the build commands that will install dependencies, run tests, and produce test reports like JUnit XML files.
3. Set up test report uploading in the CodeBuild project config under "Reports" - this sends the test reports to an S3 bucket after each build.
4. Optionally enable build badges, alerts, and notifications like Amazon Simple Notification Service (Amazon SNS) topics so you're notified of build outcomes.
5. Start your build to launch the defined test workflow, then check the console, S3 bucket and notifications to see if tests passed or failed and review the detailed test reports.
