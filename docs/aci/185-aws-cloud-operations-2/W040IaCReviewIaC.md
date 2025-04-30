# Week 4: IaC: Review of Infrastructure as Code

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to [AWS Cloud Operations 2](./aws-cloud-operations-2.md)
* back to repo's main [README.md](../../../README.md)

## IaC: Infrastructure as Code

### Pre-assessment

#### What is infrastructure as code (IaC)?

* Practice of managing and provisioning infrastructure through code

Wrong answers:

* Programming language for web development
* AWS storage service
* AWS service for managing and provisioning infrastructure through code

##### Explanation

The other options are incorrect because IaC is not a programming language itself but is implemented using languages such as YAML or JSON to define infrastructure configurations. Also, IaC is not an AWS service.

#### Which approach to IaC emphasizes defining the desired state of infrastructure?

* Declarative

Wrong answers:

* Imperative
* Procedural
* Descriptive

##### Explanation

A declarative approach declares the desired outcome. Instead of explicitly outlining the sequence of steps needed for the infrastructure to reach the final result, the declarative approach shows what the final result looks like. The automation tool interprets and enforces this configuration and determines the necessary actions to reach the specified state.

The remaining options are incorrect because procedural and descriptive are not approaches to IaC, and the Imperative approach describes defining infrastructure elements individually, not the ultimate desired state of infrastructure.

#### Which AWS service do you use to define IaC using programming languages such as Python and Java? 

* AWS Cloud Development Kit (AWS CDK)

Wrong answers:

* AWS CloudFormation
* AWS CodeCatalyst
* AWS SDKs

##### Explanation

With AWS CDK, developers achieve faster deployment by using expressive programming languages for defining infrastructure, such as Python, Java, and .NET.

The other options are incorrect for the following reasons:

* While AWS CloudFormation is a tool for infrastructure as code, it uses declarative JSON or YAML templates, not programming languages.
* AWS CodeCatalyst is a source control repository service.
* AWS SDKs are libraries for various programming languages to interact with AWS programmatically, but they are not specifically used for defining infrastructure.

## Define Infrastructure as Code

### IaC involves using code to define and provision infrastructure resources

* servers
* networks
* operating systems
* storage

### IaC approaches

* imperative - gives orders
* declarative - specifies a desired state

### IaC and AWS

* **AWS CDK**

    AWS CDK is an open source software development framework that allows developers to define and provision cloud application resources as code, using familiar programming languages.

    Languages supported are TypeScript, Python, Java, and .NET. Developers can use their existing integrated development environment (IDE) and features like autocomplete and in-line documentation to accelerate the development of infrastructure.

* **AWS CDK for Kubernetes**

    AWS CDK for Kubernetes (CDK8s) is an open source software development framework for defining Kubernetes applications using general-purpose programming languages. 

    Once an application is defined in a programming language, CDK8s will convert the application description into pre-Kubernetes YAML. The YAML file can then be consumed by any Kubernetes cluster running anywhere.

* **AWS CDK for Terraform**

    AWS CDK for Terraform (CDKTF) is a framework that enables developers to use programming languages like TypeScript, Python, Java, or C# to define infrastructure as code, instead of writing Terraform configurations in HashiCorp Configuration Language (HCL). It provides a set of constructs and abstractions that map directly to Terraform providers and resources, allowing developers to use their existing programming skills and tooling to manage infrastructure.

    The key benefit of CDKTF is that it allows developers to access the powerful capabilities of Terraform, while benefiting from the flexibility, maintainability, and tooling that comes with using a programming language. This can make infrastructure as code more accessible and easier to manage, especially for teams already familiar with the programming languages.

* **AWS Cloud Control API**

    AWS Cloud Control API is a new AWS capability that introduces a common set of create, read, update, delete, and list (CRUDL) APIs to help developers manage their cloud infrastructure in an easy and consistent way.

    The Cloud Control API common APIs allow developers to uniformly manage the lifecycle of AWS and third-party services.

* **AWS CloudFormation**

    AWS CloudFormation is a service that enables developers to create AWS resources in an orderly and predictable fashion. Resources are written in text files using JSON or YAML format.

* **AWS Serverless Application Model (AWS SAM)**

    AWS SAM is an open source framework used for building serverless applications on AWS. It provides a simplified way to define and deploy AWS Lambda functions, Amazon API Gateway, and other serverless resources using YAML or JSON templates. AWS SAM is considered an IaC tool, as it allows developers to define and manage the infrastructure for their serverless applications in a declarative manner.

### IaC in DevOps

#### Infrastructure Automation

Through code-based infrastructure, teams can define the desired state of their infrastructure. For example, you can use tools like CloudFormation for infrastructure automation by providing a declarative syntax to specify resources, their configurations, and dependencies.

#### Version Control and Collaboration

Incorporating IaC into version-control systems brings transparency and traceability to your infrastructure management. Version control allows teams to track changes, roll back to previous states, and collaborate seamlessly. This version-controlled approach mitigates configuration drift, where inconsistencies arise between different environments over time. By treating infrastructure code as part of the software development process, teams can use familiar version-control workflows, branching strategies, and pull requests for effective collaboration and code review.

#### Consistency and Reproducibility

By defining infrastructure through code, you can mirror development, testing, and production environments to ensure that what works in one environment can be reliably replicated in another. This consistency reduces the likelihood of deployment issues caused by environmental differences. Your team can predictably roll out changes, updates, and new releases, knowing that the same codebase will result in the same infrastructure configuration across various stages of the development pipeline.

### Knowledge Check

#### A company wants to use infrastructure as code to manage the resources for a new application. Which AWS service should they use?

* AWS CloudFormation

Wrong answers:

* AWS Elastic Beanstalk  
* AWS OpsWorks
* AWS CodeDeploy

##### Explanation

AWS CloudFormation provides infrastructure as code capabilities by allowing resources to be provisioned and managed through templates. This enables automation and consistency.

The other options are incorrect for the following reasons:

* AWS Elastic Beanstalk provides automatic scaling and load balancing but does not directly provide infrastructure as code capabilities.
* AWS OpsWorks provides configuration management but does not directly provide infrastructure as code capabilities.
* AWS CodeDeploy enables automated deployments but does not directly provide infrastructure as code capabilities.

#### Which of the following best describes infrastructure as code?

* Infrastructure as code is the process of managing infrastructure through machine-readable definition files rather than physical hardware configuration.

Wrong answers:

* Infrastructure as code is the process of manually configuring infrastructure components like servers, networks, and firewalls.
* Infrastructure as code is the process of securing infrastructure components like servers, networks, and firewalls.
* Infrastructure as code is the process of monitoring infrastructure performance and availability.

##### Explanation

The other options are incorrect because they describe infrastructure monitoring, security, and the traditional manual infrastructure creation process, not IaC.

#### What is a key benefit of infrastructure as code for application developers?

* It allows infrastructure to be provisioned and configured along with application code deployments.

Wrong answers:

* It eliminates the need to write application code.
* It removes the need for operations teams to manage infrastructure.
* It provides built-in infrastructure security capabilities.

##### Explanation

The other options are incorrect because operations teams still manage the infrastructure, albeit through code rather than manual processes, IaC does not eliminate the need for application code, and IaC itself does not provide built-in security capabilities.

### Summary

#### General review of IaC

IaC uses code to define and provision infrastructure resources, such as servers, networks, operating systems, and storage. IaC controls these virtualized resources by treating configuration files like source code files, and it can be used to manage infrastructure in a codified, repeatable way.

There are different IaC configuration management tools, and you can develop IaC similar to application code in Python or Java. Finally, you can write IaC code in an IDE with built-in error checking, and you can maintain it under source control with commits at each code change.

#### Benefits of IaC

Some of the central benefits of IaC over other approaches to managing your infrastructure.

* **Automation**: IaC enables the automation of infrastructure provisioning, configuration, and deployment processes. This automation reduces the risk of human error, saves time, and increases efficiency.
* **Compliance and governance**: IaC allows developers to enforce compliance and governance policies by embedding them into the code that defines the infrastructure.
* **Consistency and repeatability**: IaC allows developers to define their infrastructure in code, ensuring that their environments are consistently provisioned and configured across different environments (for example, development, staging, and production).
* **Disaster recovery and backup**: With IaC, developers can quickly re-create their infrastructure in case of a disaster or data loss by simply running the code again.
* **Scalability**: IaC makes it easier for developers to scale their infrastructure up or down by simply modifying the code and applying the changes. This is particularly useful in cloud environments where resources can be provisioned and deprovisioned on-demand.
* **Version control**: Since infrastructure is defined as code, it can be stored in a version control system like AWS CodeCatalyst or Git. This allows developers to track changes, collaborate with team members, and roll back to previous versions if needed.
