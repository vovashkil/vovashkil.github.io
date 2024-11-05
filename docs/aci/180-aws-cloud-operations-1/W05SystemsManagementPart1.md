# Systems Management Part 1

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to repo's main [README.md](../../../README.md)

## Pre-assessment

### What is a principle of systems management on AWS?

* Perform operations as code.

Wrong answers:

* Make large, infrequent changes.
* Don't anticipate failure.
* Change operations procedures only when failures occur.

The principles of systems management on AWS are backed by the AWS Well-Architected Framework. One of the principles is perform operations as code. The rest of the responses are the opposite of other principles of systems management on AWS. The corrected statements are as follows:

* Make frequent, small, reversible changes.
* Anticipate failure.
* Refine operations procedures frequently.

### Which AWS Systems Manager capability is part of application management?

* Parameter Store

Wrong answers:

* Automation
* Session Manager
* Incident Manager

Automation is a capability that belongs to change management. Session Manager belongs to node management. Incident Manager belongs to operations management.

### Which IT role primarily handles systems management?

* Cloud operations engineer

Wrong answers:

* Application developer
* Network administrator
* Security administrator

A cloud operations engineer is a primary role that handles systems management. However, other roles such as application developer, network administrator, and security administrator have some responsibility in systems management, too. The degree of that responsibility will vary from organization to organization.

## Systems Management on AWS

Systems management is the administration of IT systems. IT systems could be any type of IT infrastructure that facilitates business functions, but the functions are often defined by business applications. As mentioned in the video earlier in this section, systems management on AWS is an end-to-end workflow for managing AWS resources that support applications. AWS Systems Manager is a comprehensive systems management solution for AWS applications and resources.

The capabilities of Systems Manager are grouped into four categories. The capabilities within each category provide a particular type of systems management function.

### Systems Manager categories

#### Operations Management

A large part of systems management is the capability to detect, isolate, and resolve incidents with operations when they occur. Incidents could be anything from an intermittent service disruption to a major service outage. The operations management category holds various capabilities of AWS Systems Manager that detect incidents, along with dashboards to report on the status of your managed AWS resources.

The capabilities of Operations Management include Incident Manager, Explorer, OpsCenter, and Amazon CloudWatch dashboards hosted by Systems Manager.

#### Application Management

Hosting applications on AWS involves various AWS resources. Being able to logically organize those resources is a necessity for resource management. Application Management is the category of capabilities of Systems Manager for organizations to use to logically organize their AWS resources.

The capabilities of application management are: Application Manager, AWS AppConfig, and Parameter Store.

#### Change Management

Updates and configuration changes are necessary to keep your AWS resources secure and compliant. Change management provides the ability to request, prioritize, authorize, approve, schedule, and implement changes to AWS resources. Systems Manager groups its capabilities that support this type of management into the Change Management category.

The capabilities of Change Management are: Change Manager, Automation, Change Calendar, and Maintenance Windows.

#### Node Management

The capabilities of change management work seamlessly with the capabilities of node management, which are services used to support managed nodes. Managed nodes include various machine types, such as Amazon EC2 instances, AWS IoT Greengrass core devices, and even on-premises servers.

The capabilities of node management are: Fleet Manager, Compliance, Inventory, Session Manager, Run Command, State Manager, and Distributor.

### AWS Systems Manager in action moving an application to production environment

#### Create custom AMIs

Automation, a capability of AWS Systems Manager, is used by the operations team to create authorized Amazon Machine Images (AMIs).

The operations team starts this process by creating Automation runbooks, which are a list of actions to perform for the automation. Before Automation, the operations team would manually complete the steps to create a custom AMI, which is a time-consuming process.

With Automation, the operations team can use runbooks to create authorized AMIs with the latest software updates. The runbooks can run on a schedule or on-demand. The benefit is a quick deployment time for Amazon Elastic Compute Cloud (Amazon EC2) instances because there is virtually no need to apply updates.

#### Application deployment and configuration

Automation runbooks deploy the application to the target EC2 instances. The application references Parameter Store values. The benefit of pulling configuration data from Parameter Store is that the application could be configured for different environments without the need to rewrite code.

#### Application Management

Application Manager is used to logically group AWS resources into an application context.

Application Manager provides different ways to organize AWS resources. AWS tags could be used to show a logically grouped list of AWS resources.

#### Remote access

Session Manager is a capability of Systems Manager that allows remote access to the EC2 instances running an application.

Session Manager streamlines remote access management. It eliminates the need to manage remote access services, such as Secure Shell (SSH) or Remote Desktop, and open ports on the public internet. Instead, Session Manager provides remote access through a web browser.

#### Use Run Command

When it's not an option to remotely access production servers, application developers can use Run Command. Sometimes Session Manager is not an option for accessing software running on Amazon EC2 instances. Instead, Run Command provides a way to send commands to the designated EC2 instance.

### Systems management for the application developer

From the outset, systems management appears relevant to operations teams who administer the infrastructure that runs applications, and less so for application developers. In practice, though, the division between system operations and application development can be blurred. Application developers put their development skills toward operations work, and operations teams focus on providing infrastructure as a service (IaaS) for application development teams. The degree of that blur depends on various factors, including the size of IT organizations and DevOps maturity.

For example, smaller IT organizations might require application developers to take on both development and system operations responsibilities, whereas larger organizations might have an established DevOps workflow.

IT organizations within businesses must continually evolve to meet agility, speed, and automation goals in systems management. The capabilities of AWS Systems Manager are designed to help IT organizations meet their goals. To realize these goals requires applying development skills in different aspects of systems management. As an application developer, your role might involve dedicating some time to scripting Automation runbooks, for example. As you start your application developer journey, knowing how you can apply your development skills in systems management will benefit you and your organization.

### AWS Systems Manager capabilities in four catagories

1. Operations Management
 * Incident Manager
 * OpsCenter
 * Explorer
 * Amazon CloudWatch hosted by Systems Manager
2. Application Management
 * Application Manager
 * AWS AppConfig
 * Parameter Store
3. Change Management
 * Change Manager
 * Automation
 * Change Calendar
 * Maintenance Wundows
4. Node Management
 * Freet Manager
 * Compliance
 * Inventory
 * Session Manager
 * Run Command
 * State Manager
 * Patch Manager
 * Distributor

### Knowledge Check

#### Which responsibility does an application developer typically have toward systems management on AWS?

* Resolving incidents related to applications

Wrong answers:

* Managing infrastructure that supports an application
* Creating operational dashboards
* Monitoring and responding to infrastructure alerts

Application developers could also work with the operations team to develop and maintain scripts and Automation runbooks.

#### Which service category does Parameter Store, a capability of AWS Systems Manager, belong to?

* Application Management

Wrong answers:

* Change Management
* Node Management
* Operations Management

#### Which service provides a comprehensive systems management solution for AWS customers?

* AWS Systems Manager

Wrong answers:

* AWS AppConfig
* AWS Config
* Session Manager

AWS Config is a separate AWS service that integrates with Systems Manager. AWS AppConfig and Session Manager are capabilities of Systems Manager.

### Summary

* An introduction to systems management on AWS
* An application developer's role in systems management
* The categories of systems management on AWS
* The AWS tools and services available for AWS systems management
* How Systems Manager capabilities align with categories of systems management on AWS

Systems management on AWS uses a combination of operational knowledge and development skills to implement the capabilities of AWS Systems Manager. While an application developer might not have direct daily responsibilities in systems management, knowing how systems management works to support applications is crucial for their role.

#### AWS Systems Manager

Systems Manager is a comprehensive systems management solution for AWS applications and resources.

The capabilities are grouped into the following four categories:

* Operations Management
* Application Management
* Change Management
* Node Management

### Additional Resources

#### [Service Management](https://docs.aws.amazon.com/wellarchitected/latest/management-and-governance-guide/servicemanagement.html)

#### [AWS Systems Manager User Guide](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html)

#### [Introduction to AWS Systems Manager](https://youtu.be/MK4ZoCs-muo?si=rhRj5aSX8YLWymYk)

## Setting Up AWS Systems Manager

### Pre-assessment

#### What is a key requirement before getting started with AWS Systems Manager?

* An AWS account and administrator access

Wrong answers:

* An Amazon Elastic Compute Cloud (Amazon EC2) instance
* AWS Organizations enabled
* An AWS Identity and Access Management (IAM) user with the required permissions

An IAM user, Systems Manager Agent (SSM Agent), and appropriate IAM permissions are the key requirements to get started with Systems Manager. The service integrates with your existing AWS infrastructure.

#### What is Systems Manager Agent (SSM Agent) used for in AWS Systems Manager?

* To run scripts and send commands to managed instances

Wrong answers:

* To monitor Amazon CloudWatch Logs and send alerts
* To provision Amazon Elastic Compute Cloud (Amazon EC2) instances and Amazon Elastic Block Store (Amazon EBS) volumes
* To configure security groups and network access control lists (ACLs)

SSM Agent is installed on EC2 instances and servers, and allows Systems Manager to remotely manage those resources. SSM Agent runs commands, scripts, documents, and other requests sent by the Systems Manager service.

#### What is the benefit of AWS Systems Manager Quick Setup?

* It provides a way to configure core management and security capabilities across AWS resources.

Wrong answers:

* It provides a way to create a virtual private cloud (VPC) with public and private subnets.
* It enables automated patch management for Amazon Elastic Compute Cloud (Amazon EC2) instances. 
* It provides a dashboard for monitoring the health and status of AWS resources.  

Quick Setup reduces the time and effort needed to operationalize Systems Manager through best practice templates, automation, and out-of-the-box integrations. This makes it faster for organizations to gain operational visibility and control across their infrastructure.

### Prerequisites for Systems Manager

You must complete prerequisites before using Systems Manager to manage your Amazon Elastic Compute Cloud (Amazon EC2) instances, on-premises servers, and virtual machines (VMs). After these steps are complete, users in your organization can use Systems Manager to configure, manage, and access your *managed nodes*.

### Setting up for EC2 instances

1. **IAM user has permission to use the service**. Ensure that the AWS Identity and Access Management (IAM) user has permissions to use Systems Manager.
2. **Install or verify the installation of SSM Agent**. SSM Agent is preinstalled by default on some Amazon Machine Images (AMIs) provided by AWS.
3. **Create instance profile roles**. Do one or more of the following:
 * For EC2 instances, create an IAM instance profile and attach it to your servers.
 * For on-premises servers, create an IAM service role for the hybrid environment.
4. **Allow HTTP outbound traffic**. Verify that you are allowing HTTPS (port 443) outbound traffic to the Systems Manager endpoints. This allows the SSM Agent to establish communication with Systems Manager.
5. **Optional - Create VPC endpoint**. Creating VPC endpoints is optional. This is only needed in environments where there is no access to the Systems Manager endpoints.

### Getting started with AWS Systems Manager

#### Launch an instance using an AMI with SSM Agent preinstalled

1. Open the **Amazon EC2 console**.
2. From the EC2 console dashboard, in the **Launch instance** box, choose **Launch instance**, and then choose **Launch instance** from the options that appear.
3. For **Name and tags**, for **Name**, enter a descriptive name for your instance.
4. For **Application and OS Images (Amazon Machine Image)**, do the following:
 a. Choose the **Quick Start** tab, and then choose Amazon Linux. This is the operating system (OS) for your instance.
 b. For **Amazon Machine Image (AMI)**, choose a Hardware Virtual Machine (HVM) version of Amazon Linux 2.
5. For **Instance type**, from the **Instance type** list, choose the hardware configuration for your instance. Choose the *t2.micro* instance type, which is selected by default.
6. For **Key pair (login)**, for **Key pair** name, choose a key pair.
7. For **Network settings**, choose **Edit**. For **Security group name**, notice that the wizard created and selected a security group for you. You can use this security group, or alternatively, you can select a security group that you created previously using the following steps:
 a. Choose **Select existing security group**.
 b. From **Common security groups**, choose your security group from the list of existing security groups.
8. Expand the **Advanced details** section, and for **IAM instance profile**, choose the instance profile that you created when getting set up. If you did not complete this, see [Step 1: Configure Instance Permissions for Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-instance-permissions.html) in the *AWS Systems Manager User Guide*.
9. Keep the default selections for the other configuration settings for your instance.
10. Review a summary of your instance configuration in the **Summary** pane. When you're ready, choose **Launch instance**.
11. A confirmation page informs you that your instance is launching. Choose **View all instances** to close the confirmation page and return to the console.
12. On the **Instances** screen, you can view the status of the launch. It takes a short time for an instance to launch.
13. It can take a few minutes for the instance to show as managed and be ready for you to connect to it. To check that your instance passed its status checks, view this information in the **Status check** column.

#### Connect to your managed instance

1. In the AWS Systems Manager console navigation pane, choose **Fleet Manager**.
2. Choose the button next to the instance that you want to connect to using a terminal session.
3. In the **Node actions** menu, choose **Start terminal session**.
4. Select **Connect**.

#### Clean up your instance

When you're done working with the managed instance that you created, terminate it. This action effectively deletes it.

**To terminate your instance:**

1. Open the Amazon EC2 console.
2. In the navigation pane, choose **Instances**. In the list of instances, select the instance.
3. Choose **Instance state**, **Terminate instance**.
4. Choose **Terminate** when prompted for confirmation.

After your instance is terminated, it remains visible on the console briefly, and then the entry is deleted automatically. You can't remove the terminated instance from the console display yourself.

### Managed instance registration

By using managed instance registration with AWS Systems Manager, you can conveniently register and manage your Amazon EC2 instances and other machine types.

When you register an instance as a managed node, it enables AWS Systems Manager to remotely manage that instance. You can then perform tasks such as the following:

* Remotely connect to instances using Session Manager for interactive shell access.
* Automate patch management of instances using Patch Manager, a capability of AWS Systems Manager.
* View inventory and configuration details of instances using Systems Manager Inventory, a capability of AWS Systems Manager.
* Track and manage instances using Fleet Manager, a capability of AWS Systems Manager.

You can register instances like Amazon EC2, on-premises servers, Internet of Things (IoT) devices, edge devices and VMs from other cloud environments as managed nodes. The Standard tier allows registration of up to 1,000 nodes per AWS account and AWS Region.

Managed instance registration provides benefits of centralized monitoring and management of your infrastructure deployed both on AWS and on-premises.

### Common mistake use case

#### Problem

Newly launched instances are not automatically registered with Systems Manager.

When connecting to the instance with SSH and viewing the SSM Agent logs, there's an error: "Retrieve credentials produced error: no valid credentials could be retrieved for ec2 identity."

The SSM Agent is not registering the instance because the instance role doesn't have the correct permissions.

#### Solution

* Review AWS documentation to understand that new instances must have an IAM role with the correct permissions.
* Ensure that the instance IAM role has the appropriate SSM permission before trying to register instances. For example, attaching the AmazonSSMManagedInstanceCore policy to the role.
* Verify that the instance is registered by checking it in the Systems Manager console or describing the instance in the command line interface (CLI).
* Use AWS best practices by creating an IAM role with the required SSM permissions and attach it to EC2 instances at launch, enabling automatic registration.

New instances can be registered by the SSM Agent, the proper SSM permissions are required, and it's best to automate registration at launch using IAM roles.

### SSM Agent

AWS Systems Manager Agent (SSM Agent) is Amazon software that runs on Amazon Elastic Compute Cloud (Amazon EC2) instances, edge devices, on-premises servers, and virtual machines (VMs). SSM Agent makes it possible for Systems Manager to update, manage, and configure these resources. 

### How SSM Agent works

The agent processes requests from the Systems Manager service in the AWS Cloud, and then runs them as specified in the request. SSM Agent then sends the status and results back to the Systems Manager service by using the Amazon Message Delivery Service (service prefix: ec2messages). 

You will find the SSM Agent is already installed when you launch an EC2 instance created from an AMI with one of the following operating systems:

* Amazon Linux Base AMIs dated 2017.09 and later
* Amazon Linux 2
* Amazon Linux 2 ECS-Optimized Base AMIs
* Amazon Linux 2023 (AL2023)
* Amazon EKS-Optimized Amazon Linux AMIs
* macOS 10.14.x (Mojave), 10.15.x (Catalina), 11.x (Big Sur), and 12.x (Monterey)
* SUSE Linux Enterprise Server (SLES) 12 and 15
* Ubuntu Server 16.04, 18.04, 20.04, and 22.04
* Windows Server 2008-2012 R2 AMIs published in November 2016 or later
* Windows Server 2016, 2019, and 2022

**SSM Agent might be preinstalled on AWS managed AMIs that aren’t on this list. This typically indicates that the operating system (OS) is not fully supported by all Systems Manager capabilities.**

**SSM Agent might also be preinstalled on AMIs found in AWS Marketplace or in the Community AMIs repository, but AWS doesn’t support these AMIs.**

### Verify the status of SSM Agent

Because the SSM Agent makes it possible for Systems Manager to update, manage, and configure resources, it is recommended to check the status of SSM Agent before you try to use Systems Manager on an instance for the first time. Follow these steps to verify installation of SSM Agent on an instance:

1. After launching a new instance, wait a few minutes for it to initialize.
2. Connect to the instance using your preferred method. For example, you can use SSH to connect to Linux instances or use Remote Desktop to connect to Windows Server instances.
3. Check the status of SSM Agent by running the command for your instance's OS type. A few examples are listed in the following table:
| Operating system | Command |
| ---------------- | ------- |
| Amazon Linux | sudo status amazon-ssm-agent |
| Amazon Linux 2 and Amazon Linux 2023 | sudo systemctl status amazon-ssm-agent |
| macOS | Agent status on macOS. You can check the status by locating and evaluating the agent log file /var/log/amazon/ssm/amazon-ssm-agent.log. |
| Windows Server | Get-Service AmazonSSMAgent |
4. Evaluate the command output to learn the status of the SSM Agent.

The command output can note different statuses: the agent is installed and running, installed but not running, or the agent is not installed.

### Troubleshooting SSM Agent

Network connectivity is a common issue with SSM Agent. SSM Agent won't work if it can't communicate with the endpoints, even if you use AWS provided AMIs.

SSM Agent must allow HTTPS (port 443) outbound traffic to the following endpoints:

* ssm.*region*.amazonaws.com
* ssmmessages.*region*.amazonaws.com
* ec2messages.*region*.amazonaws.com

Your network configuration must have open internet access or you must have custom virtual private cloud (VPC) endpoints configured. If you don't plan to create a custom VPC endpoint, check your internet gateways or NAT gateways.

### Quick Setup?

Quick Setup is a capability of AWS Systems Manager that helps you to quickly configure frequently used AWS services and features with recommended best practices. You can quickly set up your instances by automating common administrative tasks, like creating required AWS Identity and Access Management (IAM) instance profile roles. It also helps with setting up operational best practices, such as periodic patch scans and inventory collection.

### The benefits of Quick Setup

#### Streamline service and feature configuration 

Quick Setup guides you through deploying operational best practices and configurations automatically.

#### Deploy configurations automatically across multiple accounts

Using Quick Setup across multiple accounts helps to ensure that your organization maintains consistent configurations.

#### Eliminate configuration drift

Configuration drift occurs whenever a user makes any change to a service or feature that conflicts with the selections made through Quick Setup. Quick Setup periodically checks for configuration drift and attempts to remediate it.

### How to get started

Quick Setup is useful for anyone looking to automate instance configuration and implement standardized and repeatable deployments. It allows for the replication of configurations at scale across EC2 environments.

#### Configure the home AWS Region

1. Open the AWS Systems Manager console.
2. In the navigation pane, choose **Quick Setup**. Note: if the AWS Systems Manager home page opens first, choose the menu icon to open the navigation pane, and then choose **Quick Setup** in the navigation pane.
3. For **Choose a home Region**, choose the AWS Region where you want **Quick Setup** to create the AWS resources used to deploy your configurations.
4. Choose **Get started**.

#### Choose your configuration

1. Choose a service or feature in the list of available **Configuration types**. A configuration type in Quick Setup is specific to an AWS service or feature. When you choose a configuration type, you choose the options that you want to configure for that service or feature. By default, configuration types help you set up the service or feature to use recommended best practices.
2. Choose **Create**.
3. After setting up a configuration, you can view details about it and its deployment status across organizational units (OUs) and Regions. You can also view State Manager association status for the configuration. In the **Configuration details** pane, you can view a detailed summary from all accounts and any detected configuration drift.

#### Set up IAM roles and permissions for Quick Setup onboarding

When using Quick Setup to deploy configurations, it uses AWS CloudFormation StackSets under the hood. With StackSets, you can create stacks across multiple accounts and Regions. Quick Setup creates these two IAM roles to enable CloudFormation StackSets to deploy resources across your AWS environment.

The execution role does the actual deployment, while the admin role can assume the execution role to grant the necessary access.

Quick Setup creates the following AWS Identity and Access Management (IAM) roles for you:

* *AWS-QuickSetup-StackSet-Local-ExecutionRole* – Grants AWS CloudFormation permissions to use any template.
* *AWS-QuickSetup-StackSet-Local-AdministrationRole* – Grants permissions to AWS CloudFormation to assume AWS-QuickSetup-StackSet-Local-ExecutionRole.

If you're onboarding a management account, the account that you use to create an organization in AWS Organizations, Quick Setup also creates the following roles for you:

* *AWS-QuickSetup-SSM-RoleForEnablingExplorer* – Grants permissions to the AWS-EnableExplorer automation runbook. The AWS-EnableExplorer runbook configures Systems Manager Explorer to display information for multiple AWS accounts and AWS Regions.
* *AWSServiceRoleForAmazonSSM* – A service-linked role that grants access to AWS resources managed and used by Systems Manager.
* *AWSServiceRoleForAmazonSSM_AccountDiscovery* – A service-linked role that grants permissions to Systems Manager to call AWS services to discover AWS account information when synchronizing data.

### [Lab: Introduction to AWS Systems Manager Documents](./W05Lab1-SystemsManagerDocuments.md)

### Knowledge Check

#### Why is AWS Systems Manager Quick Setup beneficial? 

* It provides a way to quickly configure and setup AWS services and features.

Wrong answers:

* It enables automatic backups of AWS resources.
* It provides a graphical user interface for managing AWS resources.
* It provides a way to monitor and troubleshoot AWS environment.

Quick Setup provides a way to quickly set up EC2 instances by automating common administrative tasks like creating required AWS Identity and Access Management (IAM) instance profile roles and setting up operational best practices.

#### Why is AWS Systems Manager Agent (SSM Agent) important to using AWS Systems Manager?

* It provides a way to remotely manage Amazon Elastic Compute Cloud (Amazon EC2) instances using SSM Agent.

Wrong answers:

* It provides a managed monitoring service for Amazon Elastic Compute Cloud (Amazon EC2) instances.
* It is required to use Session Manager to start Secure Shell (SSH) sessions.
* It provides a way to run commands across multiple instances using Run Command, a capability of AWS Systems Manager.

SSM Agent makes it possible for Systems Manager to update, manage, and configure these resources.

#### Which are the requirements for setting up AWS Systems Manager? (Select THREE.)

* Create an AWS Identity and Access Management (IAM) role for Systems Manager.
* Configure Session Manager permissions.
* Install AWS Systems Manager Agent (SSM Agent) on EC2 instances.

Wrong answers:

* Create a virtual private cloud (VPC) with private subnets.
* Create an AWS Identity and Access Management (IAM) user with AdministratorAccess permissions.
* Configure network security groups to allow inbound SSH access.

Setting up AWS Systems Manager requires a person to **create an IAM role to allow Systems Manager access** and **install the SSM Agent on EC2 instances** to communicate with Systems Manager. It also requires a person to **configure Session Manager permissions** to control access.

### Summary

#### Getting started with AWS Systems Manager

General setup of AWS Systems Manager requires signing up for an AWS account and creating an administrative user.

To get started setting up for EC2 instances, you need to do the following:

* Ensure the IAM user has permissions to use Systems Manager.
* Install SSM Agent.
* Create an IAM instance profile and attach it to your servers.
* Verify that you are allowing HTTPS (port 443) outbound traffic to the Systems Manager endpoints.
* Create VPC endpoints (optional).

#### Using SSM Agent with Systems Manager

SSM Agent makes it possible for Systems Manager to update, manage, and configure these resources. This is already installed when you launch an EC2 instance created from an AMI with some operating systems.

It's important to check the status of SSM Agent by running the command for your instance's operating system type. For the complete table see, [Checking SSM Agent Status and Starting the Agent](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent-status-and-restart.html) in the *AWS Systems Manager User Guide*.

#### How Quick Setup works

1. **Choose a home Region:** Quick Setup creates the AWS resources used to deploy all of your configurations in the AWS Region you specify. The home Region can’t be changed after it's chosen.
2. **Choose a configuration type:** Choose from a library of configuration types that automate common setup tasks and deploy configurations for services based on best practices.
3. **Specify configuration options:** Specify your preferred values for the options of the configuration type you chose, and which resources to target with your configuration. With Quick Setup, you can deploy configurations to a single AWS Region for your current account. Quick Setup also integrates with AWS Organizations so you can target multiple organization units (OUs) and Regions.
4. **Deploy and review:** Deploy your configuration and review the summarized results. You can use the summary page to troubleshoot failed deployments and to view more details about your configuration. The summary page also notifies you when new versions of relevant software become available, in addition to newly supported features and Regions.

### Additional Resources

#### [Setting Up AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up.html)

#### [Working With SSM Agent](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent.html)

#### [AWS Systems Manager Quick Setup](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-quick-setup.html)

#### [SSM Documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/documents.html)

## Operations Management

### Pre-assessment

#### What is AWS Systems Manager Incident Manager?

* A tool for tracking incidents and service requests

Wrong answers:

* A role responsible for managing major incidents
* A process for responding to security breaches
* A department that handles customer complaints

Incident Manager is an incident lifecycle management tool. The primary goal of Incident Manager is to facilitate the return of your AWS hosted applications to normal as quickly as possible.

#### What is the benefit of AWS Systems Manager OpsCenter?

* It provides a central place to view operational data and status across AWS accounts and Regions.

Wrong answers:

* It provides a way to group resources, view operational data, and take action on AWS resources.
* It provides a way to manage Amazon Elastic Compute Cloud (Amazon EC2) and on-premises systems using Run Command, a capability of AWS Systems Manager.
* It helps automate common IT tasks and enforce security best practices using State Manager.

OpsCenter provides a central location where operations engineers and IT professionals can manage operational work items (OpsItems) related to AWS resources.

#### What is the purpose of AWS Systems Manager Explorer?

* Managing and configuring Amazon Elastic Compute Cloud (Amazon EC2) instances

Wrong answers:

* Deploying serverless applications
* Setting up virtual private cloud (VPC) networks
* Monitoring application logs

AWS Systems Manager Explorer provides a graphical interface for viewing and managing AWS resources and applications. It allows you to visualize and control your infrastructure and applications without having to switch between different tools. Systems Manager Explorer can be used to manage EC2 instances by viewing details, connecting through Session Manager, running automation documents, updating AWS Systems Manager Agents (SSM Agents), and more.

### Operations Management on AWS

Operations management is the management and oversight of operations in a cloud computing environment. It involves managing the infrastructure, applications, data, and processes delivered through the cloud.

### Why does a cloud application developer need to know about operations management?

Operations knowledge can help you build robust, scalable, and optimized applications suited for the cloud environment, which complements your software development skills. The goal is end-to-end visibility and management of cloud-based resources and workflows to maximize efficiency, performance, reliability, and cost-effectiveness.

1. **Infrastructure**. Knowing the fundamentals of server, network, and storage infrastructure helps cloud application developers build applications that efficiently use cloud resources. They can design applications that are resilient and scalable in the cloud.
2. **Performance monitoring**. Cloud application developers should understand how to monitor application performance metrics like latency, throughput, and errors. This helps quickly identify and troubleshoot bottlenecks.
3. **Availability and reliability**. Knowledge of availability design patterns like redundancy, failover, and backup helps build fault-tolerant applications. Cloud application developers need to know techniques for achieving uptime and reliability goals.
4. **Deployments and automation**. Understanding deployment processes and infrastructure-as-code helps cloud application developers implement automated and repeatable deployments of applications to the cloud. This reduces errors and speeds up delivery.
5. **Security**. Cloud application developers should implement security best practices like encryption, access controls, and monitoring to ensure applications are secure against threats.
6. **Cost management**. Basic knowledge of cloud pricing models, resource optimization, and cost monitoring provides the ability to design cost-efficient applications. This helps reduce waste and unnecessary expenses.

### What is Operations Management in AWS?

Operations Management is a suite of capabilities within AWS Systems Manager that helps you keep track of your AWS resources across AWS Regions and accounts. These capabilities can assist in effectively managing your AWS resources.

1. Incident Manager
2. OpsCenter
3. Explorer
4. Amazon CloudWatch hosted by Systems Manager

### AWS Systems Manager Incident Manager

Incident Manager is an incident management console designed to help users mitigate and recover from incidents affecting their AWS hosted applications. An *incident* is any unplanned interruption or reduction in quality of services.

It is crucial for organizations to establish a response strategy and implement actions to prevent future incidents.

### Features of Incident Manager

Incident Manager combines user engagements, escalation, runbooks, response plans, chat channels, and post-incident analysis to help your team triage incidents faster and return your applications to normal.

#### Response plans

Create and automate response plans initiated by CloudWatch alarms or Amazon EventBridge events.

#### Runbook automation

Define runbooks through Automation to automate critical response and provide detailed steps to first responders.

#### Engagement and escalation

Automatically connect the right people for each unique incident. Engage through various contact methods and escalate through responders to ensure visibility and active participation.

#### Incident tracking

Review incident details for up-to-date information during an incident. Create and remediate follow-up items while following runbooks.

#### Active collaboration

Incident responders actively respond to incidents through integration with the AWS Chatbot client.

### Advantages of Incident Manager

Incident Manager provides cloud application developers with valuable tools for incident response, monitoring, collaboration, and testing related to their cloud-focused applications.

#### Diagnose issues efficiently and immediately

Incident Manager provides the ability to automatically collect and track the metrics related to an incident through the use of Amazon CloudWatch metrics. You can add other metrics manually to provide additional context for incident responders.

Use the Incident Manager incident timeline to display points of interest in chronological order. Responders can also use the timeline to add custom events to describe what they did or what happened. Automated points of interest include the following:

* A CloudWatch alarm or EventBridge rule creates an incident.
* Incident metrics are reported to Incident Manager.
* Responders are engaged.
* Runbook steps complete successfully.

#### Engage effectively

Incident Manager brings incident responders together through the use of contacts, on-call schedules, escalation plans, and chat channels. You define individual contacts directly in Incident Manager and specify contact preferences (email, SMS, or voice). You add contacts to on-call schedule rotations to determine who is engaged to deal with incidents during a given period. Using your defined contacts and on-call schedules, you create escalation plans to engage the necessary responders at the right time during an incident.

#### Collaborate in real time

Communication during an incident is the key to faster resolution. With an AWS Chatbot client set up to use Slack, Microsoft Teams, or Amazon Chime, you can bring together responders to directly interact with the incident and with one another. Incident Manager also displays the real-time actions of incident responders in the chat channel, which provides context to others.

#### Automate service restoration

Using Incident Manager, your responders can focus on the key tasks required to resolve an incident through the use of Automation runbooks. In Incident Manager, runbooks are a predefined series of actions taken to resolve an incident. They combine the power of automated tasks with manual steps as needed, leaving responders more available to analyze and respond to impact.

#### Prevent future incidents

Using Incident Manager post-incident analysis, your team can develop more robust response plans and effect change across your applications to prevent future incidents and downtime. Post-incident analysis also provides for iterative learning and improvement of runbooks, response plans, and metrics.

### The incident lifecycle

Incident Manager provides a step-by-step framework based on best practices of the incident lifecycle to identify and react to incidents. The phases of the incident lifecycle include alerting and engagement, triage, investigation and mitigation, and post-incident analysis.

The primary focus of Incident Manager is to help restore affected services or applications to normal as quickly as possible through a complete incident lifecycle management solution. Incident Manager provides tools and best practices for every phase of the incident lifecycle.

1. **Monitoring**. You can use Amazon CloudWatch metrics to monitor data about the performance of your applications. Amazon EventBridge events or CloudWatch alarms can automatically create an incident with response plans as the template.
2. **Response Plans**. Response plans launch related escalation plans and engagement plans to bring first responders into the incident.
3. **Incident Manager dashboard**. Simultaneously, AWS Chatbot notifies responders using a chat channel that directs them to the incident detail page. Using the chat channel and incident details, the team can communicate and triage an incident. The incident details view provides your team with runbooks, timelines, and metrics. Runbooks commonly provide investigation steps and can automatically pull data or attempt commonly used solutions. Runbooks also provide clear, repeatable steps that your team has found to be useful in mitigating incidents.
4. **Post-incident analysis**. Post-incident analysis provides the structure to help your team formulate ways to improve response and customer experience. Incident Manager facilitates potential improvements by using a set of post-incident analysis questions and action items alongside the incident timeline.

#### Incident Manager use case

Incident Manager provides a centralized console to create, monitor, and resolve incidents involving AWS resources. Key features include the following:

* Ability to track issues end-to-end from detection to resolution
* Collaboration features to engage teams and stakeholders
* Integration with other AWS services, like CloudWatch alarms and EventBridge events
* Metrics, reporting, and dashboards to analyze incident trends and optimize response

Using Incident Manager can help an operations team manage incidents like application downtime more efficiently. They would have better visibility into issues and be able to coordinate and track progress during resolutions. This would reduce mean-time-to-resolution and overall operational overhead for the team.

### AWS Systems Manager OpsCenter

OpsCenter is a central location where operations engineers and system administrators can view, track, investigate, and resolve operational work items (OpsItems) related to AWS resources. It is designed to reduce mean-time-to-resolution for issues that impact AWS resources.

#### What is an OpsItem?

An OpsItem is an AWS resource-related operational event that needs a user’s attention and, potentially, an investigation and resolution. It could be a resource-related failure, a maintenance notification, a security alert, or a performance issue. An OpsItem includes relevant information that aids with investigation and resolution of the underlying event, such as impacted resources, similar past events, and recommended runbooks. High EC2 instance CPU utilization, AWS CodeDeploy Deployment Failed, or EC2 Automation Execution failed are some examples of common OpsItems.

#### Why use OpsCenter?

OpsCenter provides visibility, automation, and insights to help cloud application developers build, monitor, and improve resilient cloud-focused applications on AWS. Knowing how to use OpsCenter is important for effective management of modern cloud applications.

Using OpsCenter, you can view contextual investigation data about each OpsItem, including related OpsItems and related resources. You can also run Systems Manager Automation runbooks to resolve OpsItems.

Each OpsItem includes the relevant information, such as name and ID of the AWS resource that generated the OpsItem, that is required to resolve an event. When you set up OpsCenter and integrate it with other AWS services, it can create OpsItems automatically. As a result, you don't have to navigate between console pages for your investigation.

#### Which services does OpsCenter integrate with?

OpsCenter integrates with multiple AWS services to diagnose and remediate issues with AWS resources. You must set up the AWS service before you integrate it with OpsCenter.

By default, the following AWS services are integrated with OpsCenter and can create OpsItems automatically:

* Amazon CloudWatch
* Amazon CloudWatch Application Insights
* Amazon EventBridge
* AWS Config
* AWS Systems Manager Incident Manager

### Examples of OpsItems

OpsCenter integrates with EventBridge so you can automatically create OpsItems to address a number of issues.

For examples of Systems Manager OpsItems that can be automatically created through Amazon EventBridge events.

#### Security issues

Security issues include alerts from AWS Security Hub.

#### Failures

Failures include the following an Amazon EC2 Auto Scaling group fails to launch an instance and a Systems Manager automation execution fails.

#### Performance issues

Performance issues include a throttling event for Amazon DynamoDB and degraded Amazon Elastic Block Store (Amazon EBS) volume performance.

#### Health alerts

Health alerts include an AWS Health alert for scheduled maintenance.

#### State changes

State changes include an EC2 instance state change from running to stopped.

### Demo: Configure EventBridge rules to create OpsItems

* Enable OpsCenter
* Create a new OpsItem
* Trigger the OpsItem by terminating an EC2 instance
* Review the output within OpsCenter

1. From the AWS Management Console, choose the search field and type Systems Manager. Under Operations Management, select OpsCenter. To access the OpsCenter console, choose the Get started button.
2. Leave the Default rules item checked and select Enable OpsCenter.
3. When you set up OpsCenter, you enable default rules in Amazon EventBridge that automatically create OpsItems. To give an example of EventBridge rules that automatically create OpsItems, the Rule named SSMOpsItems-Autoscaling-instance-launch-failure creates OpsItems when the launch of an EC2 Auto Scaling instance failed.
4. Let's create an EventBridge Rule with a target to create an OpsItem, so you can see the power of OpsCenter and its ability to aggregate data across AWS services.
5. Navigate to Amazon EventBridge. Under Get started, choose EventBridge Rule and then Create rule. In the Name, type EC2-terminate. All of the other fields will be left at the default settings. Choose Next.
 a. For Event Source, select AWS events or EventBridge partner events. Continue to scroll down to the Event pattern section. The Event source should be filled in as AWS services.
 b. In AWS service, you will select EC2. For Event Type, select EC2 Instance State-change Notification. This will create a notification when there is a change to the state of the EC2 instance.
 c. For Event Type Specification 1, select Specific states. For Specific states, select Terminated. This is the specific state we are looking for notification when the EC2 instance is terminated.
 d. For Event Type 2 Specification, choose Any instance. Now you are specifying that a notification should be triggered if any instance is terminated. Select Next.
 e. For Target 1, select AWS service. Select a target, Systems Manager OpsItem.
 f. For Execution role, you’re going to Create a new role for this specific resource. EventBridge will be using the permissions of this role to create the OpsItems. Choose Next.
 g. You will not need to create a tag. Choose Next.
 h. You can now review the rule you are creating. Scroll to the bottom, choose Create rule. 
6. Now, let’s take a look to see the new rule.
7. Navigate back to Systems Manager. Under Operations Management, select OpsCenter. Choose OpsItems, and then Configure sources. There, you will see the default list of OpsItem rules, and the new rule, EC2-terminate.
8. In order to see the OpsItem triggered, we will need to terminate an EC2 instance.
 a. Navigate to EC2. There is currently an EC2 instance running that I want to terminate. Select the instance. Go to Instance state, and select Terminate instance.
9. Now let’s navigate back to OpsCenter to review the output. In the Summary tab, you will see the OpsItems by Source and Age, Grouped by Source, EC2.
 a. Under Count, select the number or go to the OpsItem tab. I’m going to choose the OpsItems tab. Now, you will now see our event. Select the ID.
 b. You will see data regarding the event. Related resources shows the ARN of the instance you terminated. Runbooks is powerful, as it allows you to take action on the event to aid in remediation. Operational Data will show you the instance ID, the state, and the CloudWatch Event that generated it.
 c. If you scroll back to the top of the page and choose the Related resource details tab, you will see CloudWatch Metrics; resource description, which shows you an output of the metadata that is displayed in the EC2 console when the instance is running; Tags for the instance; Details from AWS Config, which might take some time to show up in OpsItems; CloudTrail logs—this is powerful because it shows you relevant events about what happened, such as who stopped the instance and when. This may take some time to populate in the console after the event occurs, as well. CloudFormation stack resources shows the relevant stack data.

### OpsCenter in action

A company is looking to gain more visibility into their AWS environment and improve operational efficiency. Currently, their IT team spends a lot of time manually gathering metrics and logs from different services, which is time-consuming. There is no centralized view to monitor overall health, track costs, or respond quickly to issues.

**Solution**

OpsCenter offers a unified view into operational health and resource utilization across multiple AWS accounts and services. Key capabilities include customizable dashboards, automated alerts, log analysis, and cost tracking. By implementing OpsCenter, the IT team would gain better visibility through centralized monitoring and save time by automating data aggregation.

### AWS Systems Manager Explorer

Systems Manager Explorer is a customizable operations dashboard that reports information about your AWS resources. It gives you an aggregated view of operations data (OpsData) for all your AWS accounts and across AWS Regions.

OpsData is operations data displayed by the Explorer dashboard. OpsData comes from a variety of sources, including EC2, OpsCenter, and Patch Manager.

### Why use Explorer?

As a cloud application developer, you will need to know how to navigate Systems Manager to monitor and troubleshoot your cloud applications or connect to application servers to troubleshoot problems or make configuration changes.

Explorer is a very useful tool to help cloud application developers manage, monitor, and operate their AWS resources and applications efficiently. Learning how to use it is a valuable skill for any cloud application developer.

While there is some overlap in functionalities between Explorer and OpsCenter, these two features also relate to each other in the following ways:

* Systems Manager OpsCenter provides a central location where operations engineers can view, investigate, and resolve OpsItems related to AWS resources.
* Explorer is a report hub where DevOps managers can view aggregated summaries of their operations data, including OpsItems.

### AWS Systems Manager Explorer in action

How Explorer can be used to conveniently visualize and manage cloud resources across accounts and Regions?

**Solution**

AWS Systems Manager Explorer can be used to centrally view and manage AWS resources, such as EC2 instances. Explorer provides a graphical interface to see resources across multiple accounts and Regions in a single view. Developer can quickly take actions like starting and stopping EC2 instances from a single location. Using Explorer, he can also visualize how resources are connected to gain insights into his application architecture.

### Amazon CloudWatch Dashboards Hosted by Systems Manager

Amazon CloudWatch dashboards are customizable home pages in the CloudWatch console that you can use to monitor your resources in a single view—even those resources that are spread across different AWS Regions. You can use CloudWatch dashboards to create customized views of the metrics and alarms for your AWS resources.

You can also create new CloudWatch dashboards directly from Systems Manager. Using CloudWatch dashboards, you can build your own custom operational dashboards to reflect the health of an application component, an application tier, or general areas of operational ownership.

With dashboards, you can create the following:

* A single view for selected metrics and alarms to help you assess the health of your resources and applications across one or more AWS Regions. You can select the color used for each metric on each graph so you can track the same metric across multiple graphs.
* An operational playbook that provides guidance for team members during operational events about how to respond to specific incidents.
* A common view of critical resource and application measurements that can be shared by team members for faster communication flow during operational events.

### Amazon CloudWatch dashboards in action

By using CloudWatch dashboards, you can create customizable dashboards to monitor resources and applications in a single view. Systems Manager can be used to publish the dashboards centrally, and securely share them across your organization.

You can build dashboards that track performance and operational health. You can do this using CloudWatch metrics and alarms from Amazon EC2, Elastic Load Balancing (ELB), and Amazon Relational Database Service (Amazon RDS). You can drill down into specific issues and set alert thresholds. Publishing the dashboards with Systems Manager will make them conveniently accessible to other team members who need to monitor the application.

### Knowledge Check

#### What is a use case for OpsCenter?

* Managing and monitoring large server environments

Wrong answers:

* Automating software deployments
* Securing network infrastructure
* Designing application architectures

OpsCenter aims to provide a unified operations console for visibility, compliance tracking, automation and general management of AWS resources. It focuses specifically on operational management of AWS workloads.

#### Why would a cloud application developer use AWS Systems Manager Explorer?

* To manage infrastructure configurations

Wrong answers:

* To visualize and access AWS resources
* To monitor application performance
* To analyze log files

AWS Systems Manager Explorer provides a graphical interface to view and manage AWS resources. These resources include Amazon Elastic Compute Cloud (Amazon EC2) instances, Amazon Elastic Container Service (Amazon ECS) clusters, AWS Lambda functions, and more. Developers can view resource configurations and relationships, and make changes to those configurations, like updating agents or setting up maintenance windows. So, a cloud developer would use Systems Manager Explorer specifically for centralized management of infrastructure configurations.

#### How does Incident Manager help cloud application developers?

* By automatically creating incidents based on CloudWatch alarms and EventBridge events

Wrong answers:

* By providing automated remediation workflows to resolve incidents quickly
* By facilitating collaboration between developers and operations teams
* By tracking application performance and usage statistics

Incident Manager gives developers observability into their applications and proactively alerts them about potential problems, which helps improve application stability, performance and uptime. Its correlation and incident management features accelerate root cause analysis and issue resolution.

### Summary

#### Operations Management on AWS

Operations Management is a suite of capabilities that helps you keep track of your AWS resources across AWS Regions and accounts. These capabilities can assist you in effectively managing your AWS resources.

As a cloud application developer, operations knowledge can help you build robust, scalable, and optimized applications suited for the cloud environment.

#### Incident Manager

Incident Manager is an incident management console designed to help users mitigate and recover from incidents affecting their AWS hosted applications.

#### Explorer

Explorer is a customizable operations dashboard. The drag-and-drop widgets automatically display actionable information about your AWS resources and an aggregated view of OpsData.

#### OpsCenter

OpsCenter provides a central location where operations engineers and IT professionals can view, investigate, and resolve OpsItems related to AWS resources.

#### CloudWatch dashboards

CloudWatch dashboards are customizable home pages in the CloudWatch console. You can access and view data from Systems Manager to centrally monitor your resources.

### Additional Resources

#### [Operations Management on AWS](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-ops-center.html)

#### [Aggregate and Resolve Operational Issues Using AWS Systems Manager OpsCenter](https://youtu.be/r6ilQdxLcqY)

#### [Improve the Visibility and Collaboration During Incident Handling in AWS Systems Manager Incident Manager](https://aws.amazon.com/blogs/mt/improve-the-visibility-and-collaboration-during-incident-handling-in-aws-systems-manager-incident-manager/)

#### [Aggregate Operational Tasks With AWS Systems Manager Explorer and OpsCenter ](https://aws.amazon.com/blogs/mt/aggregate-operational-tasks-with-aws-systems-manager-explorer-and-opscenter/)
