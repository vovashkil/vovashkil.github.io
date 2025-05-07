# Week 4: IaC: IaC Tools

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to [AWS Cloud Operations 2](./aws-cloud-operations-2.md)
* back to repo's main [README.md](../../../README.md)

## IaC Tools

### Pre-assessment

#### What is the AWS Cloud Development Kit (AWS CDK)?

* A framework for defining and deploying AWS infrastructure using familiar programming languages

Wrong answers:

* A low-level AWS service for provisioning and managing AWS resources
* A graphical user interface (GUI) for managing AWS resources
* A tool for monitoring and troubleshooting AWS resources

##### Explanation

The other options are incorrect because of the following reasons:

* AWS CDK is not a low-level service.
* AWS CDK is not a graphical user interface.
* AWS CDK is primarily used for defining and deploying infrastructure, not for monitoring or troubleshooting AWS resources.

#### What is Terraform?

* An open-source infrastructure as code (IaC) tool that supports multiple cloud providers

Wrong answers:

* A cloud provider-specific tool for managing infrastructure resources
* A programming language specifically designed for infrastructure provisioning
* A graphical user interface (GUI) for managing cloud resources across different providers

##### Explanation

The other answers are incorrect because of the following reasons:

* Terraform is not specific to any one cloud provider. It supports multiple cloud providers.
* Terraform itself is not a programming language. It uses its own configuration language called HashiCorp Configuration Language (HCL).
* Terraform is a command-line tool, not a graphical user interface.

#### Which statement best describes the difference between imperative and declarative models in the context of infrastructure as code (IaC)?

* Declarative models define the desired state of infrastructure, while imperative models specify step-by-step instructions to achieve a particular configuration.

Wrong answers:

* Imperative models define the desired state of infrastructure, while declarative models specify step-by-step instructions to achieve a particular configuration.
* Imperative models are used for provisioning cloud resources, while declarative models are used for on-premises infrastructure.
* Declarative models are specific to a particular cloud provider, while imperative models can work across multiple providers.

##### Explanation

The other options are incorrect because of the following:

* The definitions of imperative and declarative models are switched.
* Both imperative and declarative models can be used for both cloud and on-premises infrastructure.
* Declarative models are not specific to any one provider. They can work across multiple providers, just like imperative models.

### Common Components and Requirements of an IaC Tool

An imperative approach is giving step-by-step instructions to accomplish what you want, and the declarative approach is describing what you want from a big picture perspective.

#### Imperative Approach

Defines a series of step-by-step instructions or commands that need to be executed in a specific order to achieve the desired state of your infrastructure. These instructions describe the actions to be taken, such as creating, modifying, or deleting resources.

Imperative IaC tools include Bash scripts, Ansible playbooks (ad hoc tasks), and the AWS Command Line Interface (AWS CLI).

The imperative approach affords more control over how the desired state of infrastructure should be achieved. This control sometimes comes at the cost of having highly complex infrastructure files.

#### Declarative Approach

Focuses on defining the desired end state of your infrastructure, without specifying the exact steps to reach that state. You describe the desired configuration, and the IaC tool determines the necessary actions to achieve that state.

Declarative approaches generally result in simple and more maintainable infrastructure files, and they are often preferred for this reason when you don't need precise control over the deployment process. This approach can significantly reduce the cost of maintaining a complex infrastructure file.

Examples of declarative IaC tools include Terraform, AWS CloudFormation, and Kubernetes manifests.

### Resource pooling, software-defined intelligence, and a unified API

IaC requires three elements to function—resource pooling, software-defined intelligence, and a unified API.  

* **Resource pooling** means having access to a pool of computing resources—like virtual machines, databases, and load balancers—that can be easily provisioned on-demand. AWS provides this by offering a vast range of resources that can be quickly allocated, as needed.
* **Software-defined intelligence** means that the cloud services and resources can be controlled and managed through code and APIs. AWS services are designed to be software-defined, so you can use tools like AWS CloudFormation or Terraform to define your infrastructure using code or configuration files.
* **A unified API** allows you to interact with and manage different cloud services consistently. AWS provides a unified API that lets you provision and manage resources across various services, like Amazon Elastic Compute Cloud (Amazon EC2), Amazon Relational Database Service (Amazon RDS), and Amazon Simple Storage Service (Amazon S3), using a single interface or configuration file.

By combining resource pooling, software-defined intelligence, and a unified API, IaC helps you define and manage your entire infrastructure as code, making it easier to automate deployments, ensure consistency, and quickly scale and update your resources, as needed.

### Manual scripting in IaC

While CloudFormation provides a consistent way to manage infrastructure, manual scripting might be necessary to handle specific requirements or complex configurations not easily achievable through IaC alone. By integrating manual scripting into the IaC workflow and following best practices, teams can strike a balance between automation and flexibility while maintaining control over their infrastructure. This could involve writing custom scripts or using scripting languages, like Python or Bash, to interact with cloud provider APIs or perform additional configuration steps.

For instance, say that a team needs a Bash script to deploy some application code to their provisioned EC2 instances. To do this, the team might require a Python script to run SQL commands, and initialize the database schema and seed data in the Amazon RDS instance.

However, manual scripting introduces risks, like human errors, and challenges in maintaining an audit trail of infrastructure changes.

In order to mitigate risk, you can follow the steps listed below.

* Store and version your scripts alongside your CloudFormation templates.
* Implement error handling and logging in your scripts.
* Automate script execution as part of the AWS CloudFormation deployment process. 
* Document your scripts thoroughly.

By integrating scripting into the IaC workflow and following best practices, teams can strike a balance between automation and flexibility while maintaining control over their infrastructure.

## AWS and Third-Party IaC Tools

### AWS CloudFormation

AWS CloudFormation allows you to define and provision AWS resources in a declarative manner using templates. The templates are written in JSON or YAML format, and they describe the desired state of an infrastructure.

1. **Template creation**

    Create a CloudFormation template that defines the AWS resources that you want to provision, such as EC2 instances, Amazon Virtual Private Cloud (Amazon VPCs) resources, security groups, load balancers, and more. The template specifies the configuration parameters, dependencies, and relationships between resources.

2. **Template validation**

    Before deploying the resources, CloudFormation validates the template to ensure that its syntax is correct and the specified resources and configurations are valid.

3. **Resource provisioning**

    Once the template is validated, CloudFormation creates or updates the specified resources in the correct order, based on the defined dependencies. It handles the creation, configuration, and management of resources in a consistent and repeatable manner.

4. **Resource management**

    After the resources are provisioned, CloudFormation continues to manage them throughout their lifecycle. You can update the stack by modifying the template and applying the changes, or delete the stack to remove all the provisioned resources.

### AWS CDK

The AWS Cloud Development Kit (CDK) is an open-source software development framework that allows developers to define and provision cloud infrastructure resources using familiar programming languages, like TypeScript, Python, Java, and C#, instead of writing infrastructure definitions in JSON or YAML format.

As with AWS CloudFormation templates, the AWS CDK allows developers to use high-level programming languages to define their infrastructure as code.

The advantages of the AWS CDK:

1. **Abstraction**

    The AWS CDK provides a higher level of abstraction, allowing developers to define infrastructure resources using constructs and patterns that are more expressive and easier to understand than low-level resource definitions.

2. **Integration with CI/CD**

    The AWS CDK can be easily integrated into continuous integration and continuous delivery (CI/CD) pipelines, enabling automated infrastructure provisioning and updates.

3. **Reusability**

    The AWS CDK supports modular and composable infrastructure definitions, enabling developers to create and share reusable components and patterns across projects and teams.

4. **Testing and validation**

    The AWS CDK is based on programming languages, so developers can use existing testing frameworks and practices to validate their infrastructure definitions before deployment.

### Terraform

Terraform by HashiCorp, an AWS DevOps Competency Partner, is an infrastructure as code (IaC) tool similar to AWS CloudFormation that allows developers to create, update, and version their AWS infrastructure.

Terraform has a comprehensive set of features, including the following:

* Friendly custom syntax, as well as support for JSON.
* Visibility into changes before they happen.
* Built-in graphing feature to visualize the infrastructure.
* Understanding of resource relationships. One example is that failures are isolated to dependent resources while non-dependent resources still get created, updated, or destroyed.
* Open source project with a community of thousands of contributors who add features and updates.
* Ability to break down configurations into smaller chunks for better organization, reuse, and maintainability.

### [Lab 2: Building a Serverless API with AWS Application Composer]()

In this lab, you gain hands-on experience using AWS Application Composer by creating a serverless application.  

In this lab, you will perform the following tasks:

* Use AWS CloudFormation to create a serverless application infrastructure, including an Amazon API Gateway REST API, an Amazon DynamoDB table, and AWS Lambda functions
* Implement create, read, update, and delete (CRUD) operations on the DynamoDB table using the AWS SDK for Python (Boto3)
* Confirm the successful creation, reading, and deletion of items in the DynamoDB table through the API Gateway endpoints
* Manage the lifecycle of the CloudFormation stack, including deletion of the stack and all of its provisioned resources

### Knowledge Check

#### Which statement accurately describes the imperative approach in the context of infrastructure as code (IaC)?

* It specifies step-by-step instructions to configure and manage infrastructure resources.

Wrong answers:

* It defines the desired end state of the infrastructure, and the IaC tool handles the steps to achieve that state.
* It is the preferred approach for IaC tools because it provides more control over the provisioning process.
* It is cloud provider-specific and cannot be used across multiple cloud platforms.

##### Explanation

The other options are incorrect because of the following reasons:

* The option describes the declarative approach, not the imperative approach.
* While imperative models do provide more control over the steps, declarative approaches are often preferred for their simplicity and ease of use.
* The imperative approach is not inherently cloud provider-specific and can be used across multiple cloud platforms.

#### How can a developer mitigate risks associated with manual scripting? 

* Document scripts thoroughly

Wrong answers:

* Store scripts locally
* Avoid error handing and logging in the scripts
* Run scripts one at a time for monitoring and evaluation

##### Explanation

The other options are incorrect because of the following:

* Storing scripts locally does not mitigate risks associated with manual scripting. In fact, it can increase risks by making scripts harder to manage and versions harder to control.
* Proper error handling and logging are essential for troubleshooting and auditing scripts, which helps mitigate risks associated with manual scripting.
* Running scripts one at a time does not effectively mitigate risks associated with manual scripting because it still relies heavily on manual intervention and lacks automation, which can introduce consistency issues and increase the potential for mistakes.

#### What scripting language is supported by the AWS Cloud Development Kit (AWS CDK)?

* TypeScript

Wrong answers:

* Perl
* SQL
* Ruby

##### Explanation

The other options are incorrect because the AWS CDK does not support Perl, SQL, or Ruby.

### Summary

#### IaC as part of a DevOps workflow

In this topic, you learned about infrastructure as code (IaC) as part of a DevOps workflow. This included the following:

* Examined the common components and requirements of IaC tools.
* Explored AWS and third-party IaC tools, including AWS CloudFormation, AWS Cloud Development Kit (AWS CDK) , and Terraform.
* Learned about the relevance of IaC resource pooling, software-defined intelligence, and unified APIs.
* Explored the relevance and differences between declarative and imperative models.
