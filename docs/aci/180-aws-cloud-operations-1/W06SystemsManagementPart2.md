# Systems Management Part 2

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to repo's main [README.md](../../../README.md)

## Application Management

### Pre-assessment

#### Which capabilities of AWS Systems Manager belong to the application management category? (Select TWO.)

* Parameter Store
* Application Manager

Wrong answers:

* Session Manager
* State Manager
* Distributor

#### Which capability of AWS Systems Manager provides a way to group AWS resources to operate as a unit?

* Application Manager

Wrong answers:

* AWS AppConfig
* Inventory
* Fleet Manager

Application Manager provides infrastructure teams a way to organize AWS compute resources into logical groups. AWS AppConfig provides a way to manage application deployments to AWS. Inventory and Fleet Manager are capabilities that belong to node management.

#### Which capability of AWS Systems Manager could an application developer use for custom configuration and secrets management?

* Parameter Store

Wrong answers:

* AWS AppConfig
* Systems Manager Agent (SSM Agent)
* Automation

The SSM Agent is what runs on each Amazon Elastic Compute Cloud (Amazon EC2) instance that connects to AWS Systems Manager. Automation and AWS AppConfig provide different capabilities.

### What is Application Manager?

Application management is the category of Systems Manager capabilities that help organizations logically organize their AWS resources around applications. It also provides a way to configure and manage applications running on AWS.

The capabilities of Systems Manager that relate to application management are Application Manager, AWS AppConfig, and Parameter Store.

Detecting and investigating issues for applications running on AWS is an arduous, time-consuming endeavor, especially when the resources supporting the application are not well organized. By default, teams conducting an investigation into application issues must first identify which resources are involved. Afterward, they interact with multiple management consoles, which show various metrics and logs of those different AWS resources. To help teams in these cases, AWS created Application Manager, a capability of AWS Systems Manager.

### Application Manager dashboard

Application Manager aggregates operations information from multiple AWS services and Systems Manager capabilities to a single AWS Management Console. In Application Manager, an application is a logical group of AWS resources that identify and report in a specified context. This logical group can represent different versions of an application, ownership boundaries for operators, or developer environments, to name a few.

### How Application Manager works

#### Sources for Application Manager

Application Manager automatically imports and displays resources in your AWS account. These are based on a CloudFormation stack, an AWS Resource Group, an AWS Launch Wizard deployment, and more.

Application Manager also provides a way to manually create applications from predefined tagged resources, for example.

#### AWS Resources

Application Manager automatically displays AWS resources in a predefined application category.

Application Manager integrates with Amazon EC2 to display information about  instances in the context of an application. Application Manager displays instance state, status, and Amazon EC2 Auto Scaling health for a selected application in a graphical format.

#### Operational Metrics

Application Manager integrates with Amazon CloudWatch to provide real-time operational metrics for an application. You can view metrics specific to each individual AWS resource without the need to look at a separate dashboard in CloudWatch.

#### Application Logs

Application Manager integrates with Amazon CloudWatch Logs to provide log data in the context of an application without having to leave Systems Manager.

#### AWS Resource Cost

Application Manager is integrated with AWS Cost Explorer through a Cost widget. The Cost widget in Application Manager shows cost data for any application component.

#### Operational Alarms

In addition to operational metrics, you can view alarms for AWS resources running a particular application. Alarm thresholds must be configured to ensure they show up on the dashboard. You can view alarms at each component level.

### Benefits of Application Manager

Application Manager reduces the time it takes for DevOps engineers to detect and investigate issues with AWS resources. To do this, Application Manager displays many types of operations information in the context of an application in one console. Application Manager also reduces the time it takes to remediate issues by providing runbooks that perform common remediation tasks on AWS resources.

### What is AWS AppConfig?

AWS AppConfig, a capability of AWS Systems Manager, focuses on managing application feature flags and dynamic configurations. With AppConfig feature flags and dynamic configurations, software developers can quickly and securely adjust application behavior in production environments without full code deployments. With feature flags, you can gradually release new capabilities to users, and measure the impact of those changes before fully deploying the new capabilities to all users. With operational flags and dynamic configurations, you can update block lists, allow lists, throttling limits, logging verbosity, and perform other operational tuning to quickly respond to issues in production environments.

#### Method 1: Configuration change – Common method

Application developers commonly decouple application configuration from their software. Whatever the method, application configuration is included in the commit alongside the software code. When finally deployed, the configuration is loaded when the application initializes. The configuration of the application remains static until it restarts or is updated.

Any update to the application configuration goes through the deployment cycle regardless of zero code changes. The cost of this method is the lengthy deployment time for any application configuration change, in addition to a service disruption to restart the application.

1. Commit
2. Build
3. Test
4. Deploy

#### Method 2: Configuration change – Dynamic method

Dynamic configuration involves the application polling an independent configuration management system for any configuration changes. These are configuration values that an application developer anticipates will need to be changed in the future or might vary according to specific system conditions. Those conditions could be known or unknown.

An application must be designed and developed to use the dynamic configuration method. This means the code must include logic to handle any configuration changes at any time. Additionally, service disruptions should not occur when implementing configuration changes.

An application developer uploads a configuration document to AppConfig. The application change is validated and staged in AppConfig. At the designated time, the configuration document is released to the application. At the the next polling interval, the application consumes the new configuration data without restarting.

#### What are feature flags?

Feature flags empower developers to release new end-user capabilities nearly instantly without requiring the operational risk and time cost of a full application redeployment. As a requirement, the application must include the feature flags method in both the design and development phases. The application must be able to handle functionality changes during runtime, without deploying new code.

A new feature flag is staged in a feature flag control mechanism. For examples, during a controlled rollout of a feature, Audience A immediately receives access to the feature, while Audience B continues to use the application without the new feature. Eventually, all users will get access to the feature.

### How AWS AppConfig works

#### Configuration profile

A configuration profile includes a Uniform Resource Identifier (URI) that enables AWS AppConfig to locate your configuration data in its stored location and a profile type. AWS AppConfig supports two configuration profile types: feature flags and freeform configurations.

#### Feature Flag

Feature flag configuration profiles store their data in the AWS AppConfig hosted configuration store and the URI is  "hosted".

#### Freeform configuration

For freeform configuration profiles, you can store your data in the AWS AppConfig hosted configuration store, or any AWS service that integrates with AWS AppConfig.

#### Configuration sources

You can store your configuration data in AppConfig directly or you can use other AWS services that integrate with AppConfig as a source. Those services include the following:

* Amazon Simple Storage Service (Amazon S3)
* AWS Secrets Manager
* AWS Systems Manager Parameter Store
* AWS CodePipeline
* AWS Systems Manager document store

#### Environment

An environment is a logical grouping of targets, such as applications in a Beta or production environment, AWS Lambda functions, or containers.

#### Configuration polling

You configure AWS AppConfig Agent to run on the same server as the application. The agent polls AWS AppConfig for configuration updates. To retrieve the data, the target application makes an HTTP call to the AppConfig Agent running on the same server.

### AWS AppConfig benefits

#### Reduce unexpected downtime for your customers

AWS AppConfig reduces application downtime by helping you to create rules to validate your configuration. Configurations that aren't valid can't be deployed. AWS AppConfig provides the following two options for validating configurations:

For syntactic validation, you can use a JSON schema. AWS AppConfig validates your configuration by using the JSON schema to ensure that configuration changes adhere to the application requirements.

For semantic validation, AWS AppConfig can call an AWS Lambda function that you own to validate the data within your configuration.

#### Quickly deploy changes across a set of targets

AWS AppConfig streamlines the administration of applications at scale by deploying configuration changes from a central location. AWS AppConfig supports configurations stored in the AWS AppConfig hosted configuration store, Systems Manager Parameter Store, Systems Manager documents, and Amazon S3. You can use AWS AppConfig with applications hosted on EC2 instances, AWS Lambda, containers, mobile applications, or IoT devices.

Targets don't need to be configured with the Systems Manager SSM Agent or the IAM instance profile required by other Systems Manager capabilities. This means that AWS AppConfig works with unmanaged instances.

#### Update applications without interruptions

AWS AppConfig deploys configuration changes to your targets at runtime without a heavyweight build process or taking your targets out of service.

#### Control deployment of changes across your application

When deploying configuration changes to your targets, AWS AppConfig helps you to minimize risk by using a deployment strategy. With deployment strategies, you can slowly roll out configuration changes to your fleet. If you experience a problem during the deployment, you can roll back the configuration change before it reaches the majority of yours hosts.

### AWS AppConfig use cases

AppConfig supports the following use cases, which cover a broad spectrum of customer needs:

* **Feature flags and toggles:** Safely release new capabilities to your customers in a controlled environment. Instantly roll back changes if you experience a problem.
* **Application tuning:** Carefully introduce application changes, while testing the impact of those changes with users in production environments.
* **Allow list or block list:** Control access to premium features or instantly block specific users without deploying new code.
* **Centralized configuration storage:** Keep your configuration data organized and consistent across all of your workloads. You can use AWS AppConfig to deploy configuration data stored in the AWS AppConfig hosted configuration store, AWS Secrets Manager, Systems Manager Parameter Store, or Amazon S3.

### What is Parameter Store?

Configuration data management is a shared requirement for both infrastructure management and application development. Configuration data could include environment variables, tags, or metadata, all of which are stored in plain text. Configuration data also includes secret information, such as passwords, API keys, or software licenses, all of which require a layer of security for storage and management. Parameter Store, a capability of AWS Systems Manager, provides secure, hierarchical storage for configuration data management and secrets management. Parameter Store also provides centralized access to configuration data.

### How Parameter Store works

#### Create parameter

IT staff, whether an operations member or application developer, can use Parameter Store to host configuration data for their respective work. They must have the appropriate IAM permission (for example, PutParameter) to store parameters. Common IT practice is to provide IAM permissions to systems that programmatically manage parameters in Parameter Store.

#### Configuration data

You can store any kind of plain text data in a Parameter Store parameter. For non-secret data, you have two types to choose from: String and StringList. A String parameter consists of any block of text you enter. A StringList parameter contains a comma-separated list of values or an array of items.

AWS highly recommends that only non-sensitive data are stored in either type of parameter.

#### Pull parameter data

With the appropriate IAM permission (GetParameter, GetParameters), a number of AWS services, an application, or a user can pull the parameter values from the Parameter Store.

AWS services than can access Parameter Store parameters include the following:

* AWS CloudFormation
* Amazon EC2
* AWS Secrets Manager
* AWS Lambda

#### AWS KMS integration

Storing secret data in a parameter involves encrypting the parameter value. Parameter Store integrates with AWS Key Management Service (AWS KMS) for data value encryption. You have the option to use either a symmetric AWS managed key or a customer managed key for encryption.

#### Secret data

The parameter type for storing secret data in a secured manner is SecureString. Examples of this type of data include passwords, applications secrets, and confidential configuration data.

Users and programs must have IAM permissions to use both the AWS KMS key and Parameter Store to retrieve and decrypt the SecureString contents.

#### Application credentials

In example case of an application pulling a parameter that holds sensitive information (for example, database connection string). The parameter is a SecureString type. The application has the appropriate IAM permissions to pull and decrypt the parameter value.

### Accessing Parameter Store value programmatically

#### [Boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

#### [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html)

### Benefits of Parameter Store

* Use a secure, scalable, hosted secrets management service with no servers to manage.
* Improve your security posture by separating your data from your code.
* Store configuration data and encrypted strings in hierarchies and track versions.
* Control and audit access at granular levels.
* Store parameters reliably because Parameter Store is hosted in multiple Availability Zones in an AWS Region.

### Parameter Store and AWS Secrets Manager

Parameter Store provides secure, hierarchical storage for configuration data management and secrets management. You can store data, such as passwords, database strings, and license codes as parameter values.

AWS Secrets Manager provides a similar function when managing and storing secret data. However, Secrets Manager also provides the means to rotate data automatically, where Parameter Store does not. Secrets Manager integrates with Parameter Store, which means you can reference secrets you've stored in Secrets Manager as parameters.

AWS recommends that if you need to rotate your secret data automatically, then use AWS Secrets Manager for your data. To streamline how you access your configuration management, you could use the same GetParameter and GetParameters API operations for both Parameter Store parameters and secrets stored in Secrets Manager.

### [Lab: Create a Systems Manager Parameter](./W06Lab1-SystemsManagerParameterStore.md)

### Knowledge Check

#### What is the feature flags method?

* A way to add or remove application functionality without redeploying code.

Wrong answers:

* A means to dynamically change application configuration while the application is live.
* A way to notify application users of new capabilities to their accounts.
* A capability of AWS AppConfig to notify AWS customers of new features.

The feature flags method provides a way to add or remove application functionality without the need to deploy new code. AWS AppConfig provides a way to dynamically change an application configuration while it is live, but it's not a feature flag. A way to notify application users of new capabilities to their accounts is a result of a feature flag activation. AWS AppConfig could notify AWS customers of new features, but that would be a result of activating a feature flag.

#### How could an application developer integrate an application with Parameter Store?

* The application could pull configuration data from Parameter Store parameters.

Wrong answers:

* The application could store customer data into Parameter Store values.
* The application could store temporary, computational data in Parameter Store.
* The application could pull workload assignments from Parameter Store parameters.

An application stores customer data into a separate datastore, such as a Amazon Relational Database Service (Amazon RDS) database, not Parameter Store. An application wouldn't use Parameter Store for temporary, computational data, but rather RAM or a storage device. An application pulls workload assignments from a message queue, such as Amazon Simple Queue Service (Amazon SQS).

#### Which purpose does Application Manager serve?

* It provides a way to manage customer applications from a single console.

Wrong answers:

* It is used to create, manage, and deploy application configurations.
* It provides hierarchical storage for secrets management and configuration data management.
* It provides a customizable operations dashboard that reports information about deployed resources into an AWS account.

AWS AppConfig is used to create, manage, and deploy application configurations. Parameter Store provides hierarchical storage for secrets management and configuration data management. Systems Manager Explorer provides a customizable operations dashboard that reports information about deployed resources into an AWS account.

### Summary

* Application management on AWS
* The capabilities of AWS Systems Manager used for application management and their benefits
* The functionality and benefits of Parameter Store for an application developer

Application management on AWS involves both application delivery and configuration. Application delivery ranges from investigating and remediating infrastructure running applications to deploying applications and features. The benefits of using Systems Manager for application configuration management depends on decoupling the application code from its configuration. In this way, both system operators and application developers can shorten deployment times to various environments. Furthermore, the application can run in those environments without custom coding.

#### Application management

Systems Manager has three capabilities that help manage applications running in AWS. Those capabilities are as follows:

* Application Manager
* AWS AppConfig
* Parameter Store

### Additional Resources

#### [AWS Systems Manager Application Management](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-application-management.html)

#### [Learn to Use AWS AppConfig Feature Flags](https://catalog.us-east-1.prod.workshops.aws/workshops/2ee2fc71-0618-479c-86dd-1d5fb168eb20/en-US)

#### [Parameter Store Lab](https://mng.workshop.aws/ssm/capability_hands-on_labs/parameterstore.html)

## Change Management

### Pre-assessment

#### Which capability of AWS Systems Manager is used to request a change to an AWS resource?

* Change Manager

Wrong answers:

* Automation
* Change Calendar
* Maintenance Windows

Change Manager provides the means for creating  change requests and performing approved changes. The other capabilities are part of the change request process.

#### Which component of a change request in Change Manager makes the authorized resource changes?

* Automation runbooks

Wrong answers:

* One of the approvers of the change request
* Notification options
* Change Calendar

Approvers review change requests and either approve or disapprove of the request. Notification options notify approvers of a new change request. The Change Calendar indicates when a change can and cannot be made.

#### In Systems Manager, what is used to schedule a disruptive change to AWS resources in a specified period of time?

* Maintenance windows

Wrong answers:

* Change Calendar events
* Automation
* Change Manager

Change Calendar events either block or allow changes to AWS resources. Automation makes changes to AWS resources, but does not provide a way to schedule those changes. Change Manager provides an approval workflow for change requests.

### What is Change Manager?

Change management provides the ability to request, prioritize, authorize, approve, schedule, and implement changes to AWS resources. The first change management capability of Systems Manager is Change Manager.

The capabilities of Systems Manager that relate to change management are 

* Change Manager,
* Automation,
* Change Calendar,
* and Maintenance Windows.

All these capabilities help you manage and apply changes to your infrastructure running in AWS.

Making changes to any application or its supporting infrastructure includes the risk of downtime or service disruption. To mitigate against foreseen and unforeseen service disruption, organizations employ a change management process, especially in a production environment. Change management has mechanisms that organize the people and processes involved in making changes. At AWS, Change Manager, a capability of AWS Systems Manager, is an enterprise change management framework for requesting, approving, implementing, and reporting on operational changes to your application configuration and infrastructure.

Use Change Manager for managing changes to both AWS resources and on-premises resources. With Change Manager, you can use pre-approved change templates to help automate change processes for your resources and help avoid unintentional results when making operational changes. Change Manager also helps you safely implement changes while avoiding schedule conflicts with important business events.

### How Change Manager works

#### Change template

A change template is a collection of configuration settings in Change Manager that define such things as required approvals, available runbooks, and notification options for change requests.

Foe example, a change requester uses a change template to create a custom change request. The requester must provide all the details required to create the change request.

#### Change request

A change request is a request in Change Manager to run an Automation runbook that updates one or more resources in your AWS or on-premises environments. It is created using a change template. When creating a change request, one or more approvers in your organization or account must review and approve the request. Without the required approvals, the runbook workflow, which applies the changes you request, isn't permitted to run.

#### SNS notification

If the requested change requires manual approvals, Change Manager notifies the designated approvers through an Amazon SNS notification that a change request is ready for their review. You can designate approvers for change requests in the change template, or let users designate approvers in the change request itself.

#### Change Calendar check

When a requested change is approved, the Change Manager first determines whether the request conflicts with other scheduled business activities. If a conflict is detected, Change Manager can block the change or require additional approvals before starting the runbook workflow.

#### Make requested change

When it's time to implement an approved change, Change Manager runs the Automation runbook that is specified in the associated change request. Only the operations defined in approved change requests are permitted when runbook workflows run. This approach helps you avoid unintentional results while changes are being implemented.

### Benefits of Change Manager

* **Reduce risk of service disruption and downtime:** Change Manager can make operational changes safer by ensuring that only approved changes are implemented when a runbook workflow runs. You can block unplanned and unapproved changes. Change Manager helps you avoid the types of unintentional results caused by human error that require costly hours of research and backtracking.
* **Get detailed auditing and reporting on change histories:** Change Manager provides accountability with a consistent way to report and audit changes made across your organization, the intent of the changes, and details about who approved and implemented them.
* **Avoid schedule conflicts or violations:** Change Manager can detect schedule conflicts, such as holiday events or new product launches, based on the active Change Calendar for your organization. You can allow runbook workflows to run only during business hours, or allow them only with additional approvals.
* **Adapt change requirements to your changing business:** During different business periods, you can implement different change management requirements. For example, during end-of-month reporting, tax season, or other critical business periods, you can block changes or require director-level approval for changes that could introduce unnecessary operational risks.
* **Centrally manage changes across accounts:** Through its integration with AWS Organizations, Change Manager makes it possible for you to manage changes throughout all of your OUs from a single delegated administrator account. You can turn on Change Manager for use with your entire organization or with only some of your OUs.

### What is Automation?

Manually running administrative tasks in a development environment usually requires minimal time and effort to complete. If downtime occurs because of manual administration tasks, then the impact is non-critical. In a production environment, manually running administrative tasks poses a high risk because of possible human error or amount of effort and time to complete those tasks. For example, manually applying software updates across thousands of Amazon EC2 instances within a 2-hour time period is impractical for several reasons. Automating administration tasks is the preferred method.

Automation, a capability of AWS Systems Manager, streamlines common maintenance, deployment, and remediation tasks for AWS services like Amazon EC2, Amazon Relational Database Service (Amazon RDS), Amazon Redshift, Amazon Amazon S3, and many more.

### How Automation works

#### Sources

AWS provides predefined runbooks to help organizations get started with Automation. An Automation user could deploy those runbooks or use them as a template for their own custom runbooks. Additionally, a user can run Automation runbooks when appropriate.

Amazon EventBridge supports Automation as a target type in EventBridge rules. This means that you can activate runbooks when certain events occur or on a schedule within your AWS environment.

#### Runbook

Automation runbooks are versatile in their capability to perform various actions across multiple AWS services and managed EC2 instances.  A runbook is a list of operational steps that the Automation service performs on your behalf. Runbooks support both Python and PowerShell to provide the capabilities of programmatic scripting.

You can set your runbooks to deliver operational output into Amazon CloudWatch Logs.

#### AWS services

Runbooks perform operational tasks within managed EC2 instances. For example, applying updates or restarting an operating system. Additionally, runbooks also perform operational tasks on other AWS services through making calls to any AWS API. Some of those services include the following:

* Amazon RDS
* Amazon S3
* Amazon Redshift

### Automation runbook

AWS provides predefined runbooks for organizations to use directly or as templates.

Automation runbooks are versatile to ensure they can accommodate the automation needs of organizations. You can create runbooks for common operations, and reference those runbooks during an automation. This action can streamline your runbooks by removing the need to duplicate steps across similar runbooks. For example, your organization needs to run software updates on various tagged groups of EC2 instances in stages. You could create two runbooks in a parent-child relationship with the parent runbook used to initiate a rate control automation of the child runbook.

The following code block shows how to create an AMI of an Amazon EC2 instance, then copy it to another Region. The purpose of this kind of runbook is for backup and recovery. The runbook presented in the code block is written in YAML and has embedded Python code. The Python code handles copying the AMI to another Region, while what's written in YAML creates and confirms the availability of the AMI.

```
---
    description: Custom Automation Backup and Recovery Example
    schemaVersion: '0.3'
    assumeRole: "{{ AutomationAssumeRole }}"
    parameters:
      AutomationAssumeRole:
        type: String
        description: "(Required) The ARN of the role that allows Automation to 
          perform the actions on your behalf. If no role is specified, Systems 
          Manager Automation uses your IAM permissions to use this runbook."
        default: ''
      InstanceId:
        type: String
        description: "(Required) The ID of the EC2 instance."
        default: ''
    mainSteps:
    - name: createImage
      action: aws:executeAwsApi
      onFailure: Abort
      inputs:
        Service: ec2
        Api: CreateImage
        InstanceId: "{{ InstanceId }}"
        Name: "Automation Image for {{ InstanceId }}"
        NoReboot: false
      outputs:
        - Name: newImageId
          Selector: "$.ImageId"
          Type: String
      nextStep: verifyImageAvailability
    - name: verifyImageAvailability
      action: aws:waitForAwsResourceProperty
      timeoutSeconds: 600
      inputs:
        Service: ec2
        Api: DescribeImages
        ImageIds:
        - "{{ createImage.newImageId }}"
        PropertySelector: "$.Images[0].State"
        DesiredValues:
        - available
      nextStep: copyImage
    - name: copyImage
      action: aws:executeScript
      timeoutSeconds: 45
      onFailure: Abort
      inputs:
        Runtime: python3.8
        Handler: crossRegionImageCopy
        InputPayload:
          newImageId : "{{ createImage.newImageId }}"
        Script: |-
          def crossRegionImageCopy(events,context):
            import boto3
    
            #Initialize client
            ec2 = boto3.client('ec2', region_name='us-east-1')
            newImageId = events['newImageId']
    
            ec2.copy_image(
              Name='DR Copy for ' + newImageId,
              SourceImageId=newImageId,
              SourceRegion='us-west-2'
            )
```

#### [Additional Runbook Examples](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-document-examples.html) section in the *AWS Systems Manager User Guide*

### Benefits of Automation

#### Scripting support in runbook content

Using the *aws:executeScript* action, you can run custom Python and PowerShell functions directly from your runbooks. This provides you greater flexibility in creating your custom runbooks because you can complete various tasks that other Automation actions don't support, all within the same runbook. You also have greater control over the logic of the runbook. You could also use the *aws:invokeLambdaFunction* for additional supported runtime languages that aren't supported in a runbook.

#### Run automations from a centralized location

Administrators can run automations on resources across multiple accounts and Regions from the Systems Manager console.

#### Enhanced operations security

Administrators have a centralized place to grant and revoke access to runbooks. Using only AWS Identity and Access Management (IAM) policies, you can control which individual users or groups in your organization can use Automation and which runbooks they can access.

#### Automate common IT tasks

Automating common tasks can help improve operational efficiency, enforce organizational standards, and reduce operator errors. For example, you can use the *AWS-UpdateCloudFormationStackWithApproval* runbook to update resources that were deployed by using an AWS CloudFormation template. The update applies a new template. You can configure the Automation to request approval by one or more users before the update begins.

#### Safely perform disruptive tasks in bulk

Automation includes features like rate controls so you can control the deployment of an automation across your fleet by specifying a concurrency value and an error threshold. 

#### Streamline complex tasks

Automation provides predefined runbooks that streamline complex and time-consuming tasks, such as creating golden AMIs. For example, you can use the *AWS-UpdateLinuxAmi* and *AWS-UpdateWindowsAmi* runbooks to create golden AMIs from a source AMI. Using these runbooks, you can run custom scripts before and after updates are applied. You can also include or exclude specific software packages from being installed.

#### Define constraints for inputs

You can define constraints in custom runbooks to limit the values that Automation will accept for a particular input parameter. For example, allowedPattern will only accept values for an input parameter that match the regular expression you define. If you specify allowedValues for an input parameter, only the values you've specified in the runbook are accepted.

### [Lab: Resize Amazon EC2 Instances With Automation](./W06Lab2-ResizeEC2WithAutomation.md)

### What is Change Calendar?

Managing when authorized changes occur in any IT environment is a top priority. As such, the capability to view, approve, or block when authorized changes occur is a requirement for any change management system. With Change Calendar, a capability of AWS Systems Manager, you can set up date and time ranges when actions you specify (for example, in Systems Manager Automation runbooks) might be performed in your AWS account. In Change Calendar, these ranges are called events. When you create a Change Calendar entry, you're creating a Systems Manager document of the type ChangeCalendar. In Change Calendar, the document stores iCalendar 2.0 data in plaintext format. Events that you add to the Change Calendar entry become part of the document.

Two types of Change Calendar entries:

* DEFAULT_OPEN
* DEFAULT_CLOSED

#### DEFAULT_OPEN

**DEFAULT_OPEN** means the Change Calendar is open by default. All actions can run by default, except during calendar events. During events, the state of a DEFAULT_OPEN calendar is CLOSED and events are blocked from running.

This means that no changes can occur during that event. Any other proposed change event that is requested to occur during the scheduled maintenance event will be denied.

#### DEFAULT_CLOSED

**DEFAULT_CLOSED** means the Change Calendar is closed by default. All actions are blocked by default, except during calendar events. During events, the state of a DEFAULT_CLOSED calendar is OPEN and actions are permitted to run.

This means that changes can occur during that event. Any changes set to occur before or after the scheduled maintenance event will be denied.

### How Change Calendar works

1. **Change calendar**. The Change Calendar is in the OPEN configuration. All scheduled events on this calendar will set the calendar to CLOSED during the event's time frame.
2. **Proposed event A**. Proposed event A is set to occur during a time when the Change Calendar's status is set to CLOSED. As such, the Change Calendar will deny all specified actions of the proposed event. All scheduled events have priority to complete their actions during their allotted time.
3. **Proposed event B**. Proposed event B requests time when the Change Calendar's status is set to OPEN. The change calendar approves the proposed event and blocks any change requests during the scheduled time for proposed event B.

### Benefits of Change Calendar

* **Review changes before they're applied:** A Change Calendar entry can help ensure that potentially destructive changes to your environment are reviewed before they're applied.
* **Apply changes only during appropriate times:** Change Calendar entries help keep your environment stable during event times. For example, you can create a Change Calendar entry to block changes when you expect high demand on your resources during a conference or public marketing promotion, for example. A calendar entry can also block changes when you expect limited administrator support, such as during vacations or holidays. You can use a calendar entry to allow changes except for certain times of the day or week when there is limited administrator support to troubleshoot failed actions or deployments.
* **Get the current or upcoming state of the calendar:** You can run the Systems Manager GetCalendarState API operation to show you the current state of the calendar, the state at a specified time, or the next time that the calendar state is scheduled to change.
* **EventBridge support:** This Systems Manager capability is supported as an event type in Amazon EventBridge rules.

### What is Maintenance Windows?

Whether application or the infrastructure running applications, regular maintenance must happen, preferably when downtime or reduced capacity is acceptable. For example, updating system drivers, patching operating systems, or, even software updates often disrupts services that a system is providing. Maintenance Windows, a capability of AWS Systems Manager, helps you define a schedule for when to perform these type of potentially disruptive actions. With Maintenance Windows, you can schedule actions on numerous other AWS resource types, such as Amazon S3 buckets, Amazon SQS queues, and AWS KMS keys.

With Maintenance Windows, you can schedule and automate various tasks that include the following:

* Install or update applications.
* Apply patches.
* Install or update SSM Agent.
* Run PowerShell commands and Linux shell scripts by using a Run Command task.
* Build AMIs, boot-strap software, and configure nodes by using an Automation task.
* Run AWS Lambda functions that invoke additional actions, such as scanning your nodes for patch updates.
* Run AWS Step Functions state machines to perform tasks. These tasks could include removing a node from an Elastic Load Balancing (ELB) environment, patching the node, and then adding the node back to the ELB environment.

A best practice for Maintenance Windows is to integrate it with Change Calendar. A major benefit for this integration includes assurance that no other scheduled changes occur during the maintenance window. And, conversely, a maintenance window won't occur during a scheduled change or blocked-out period on a Change Calendar.

### How Maintenance Windows works

1. **Create a maintenance window**. When you create a maintenance window, you must specify how often the maintenance window runs by using a Cron or rate expression. Each maintenance window has a schedule, a maximum duration, a set of registered tasks, and a set of registered targets. Registered targets are the nodes or other AWS resources that are acted upon. For example, a maintenance window can include an Automation runbook as a registered task.
2. **Enter a maintenance window**. At the designated time, the maintenance window becomes active. The Automation runbook runs on the designated AWS resources.
3. **Check Change Calendar**. The Automation runbook includes logic to confirm that the specified Change Calendar is open for the duration of the maintenance window. If the Change Calendar is blocked, then the Automation runbook could send a notification to the appropriate IT staff to confirm how to proceed. A member from the IT staff could manually approve or deny proceeding with the Automation.
4. **Change Calendar is open**. The change requester may create a change request to ensure the maintenance window occurs at the designated time and that there are no other blockers. The Automation runbook is clear to proceed with the maintenance.

### Benefits of Maintenance Windows

* **Schedule and automate maintenance events:** Maintenance Windows provides control over when and how maintenance occurs in your AWS resources. You have the option of choosing between AWS action resources or creating your own automation steps. When you integrate maintenance windows with Change Calendar, you benefit from a comprehensive change management process.
* **Apply maintenance events to Amazon EC2 instances and beyond:** Maintenance Windows provides you the means to schedule and automate changes to other AWS resources, not just EC2 instances. As previously mentioned, other services include Amazon S3, Amazon SQS, and AWS KMS.
* **More powerful than running scripts:** Maintenance Windows goes beyond just automating script deployment to operating systems. It provides you with ways to deliver the required changes with your AWS resources. For example, you could include AWS Lambda functions or StepFunction state machines to carry out sophisticated logic or actions. This ensures your AWS resources are ready to accept planned changes before they are made.

### Knowledge Check

#### Which capability of AWS Systems Manager streamlines common maintenance, deployment, and remediation tasks for AWS services?

* Automation

Wrong answers:

* Change Manager
* Maintenance Windows
* Change Calendar

Automation performs operational tasks across many AWS services. These other services use Automation runbooks to carry out their specified tasks.

#### What scripting languages does Automation support? (Select TWO.)

* Python
* PowerShell

Wrong answers:

* Bash
* JavaScript
* Rust

Automaton runbooks support both Python and PowerShell scripts. At this time, the Bash and JavaScript scripting languages are not supported. Rust is a programming language and is not supported.

#### What is a maintenance window?

* It is a scheduled time for performing potentially disruptive actions on managed Amazon Elastic Compute Cloud (Amazon EC2) instances.

Wrong answers:

* It is a way to deploy automated solutions at scale.
* It is a framework for requesting, approving, implementing, and reporting on operational changes to applications and infrastructure.
* It is a way to set up date and time ranges for when actions might occur within an AWS account.

Change Manager is a framework for requesting, approving, implementing, and reporting on operational changes to applications and infrastructure. Change Calendar is a way to set up date and time ranges for when actions might occur within an AWS account. Automation is a way to deploy automated solutions at scale.

### Summary

* Change management on AWS
* The Systems Manager capabilities for change management and their benefits
* How each change management capability integrates with each other to provide a comprehensive change management service on AWS

Change management on AWS aims to provide a comprehensive framework for organizations wanting to minimize downtime and service disruptions when implementing changes to their AWS environments. All the change management capabilities of Systems Manager integrate with each other to provide a change management solution for AWS customers. Application development and system operations teams must coordinate how changes occur both to running applications and the infrastructure supporting them.

#### Change management

Systems Manager has four capabilities that help manage changes to AWS resources and applications. Those capabilities are as follows:

* Change Manager
* Automation
* Change Calendar
* Maintenance Windows

### Additional Resources

#### [AWS Systems Manager Change Management](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-actions-and-change.html)

#### [Using AWS Systems Manager Change Calendar to Prevent Changes During Critical Events](https://aws.amazon.com/blogs/mt/using-aws-systems-manager-change-calendar-to-prevent-changes-during-critical-events/)

#### [Maintenance Window Lab](https://mng.workshop.aws/ssm/use-case-labs/inventory_patch_management/maintwindow.html)

#### [Using AWS Systems Manager Automation Documents to Deploy a .NET Application on AWS](https://youtu.be/JBB__HbwFtQ?si=inbyJwup9PMIoS_m)

## Node Management

### Pre-assessment

#### What is node management?

* The process of monitoring, maintaining, and provisioning nodes in a distributed system, like a cluster or cloud.

Wrong answers:

* The process of managing user access and permissions on a computer network.
* The process of routing network traffic between nodes in a mesh network.
* The process of designing and laying out components in a flowchart diagram.

Within AWS,  AWS Systems Manager provides the capabilities for accessing, managing, and configuring your managed nodes.

#### Which are some of the capabilities of Node Management in AWS Systems Manager? (Select THREE.)

* Define and maintain consistent operating system (OS) configurations.
* Remove shell to manage Amazon Elastic Compute Cloud (Amazon EC2) instances, edge devices, on-premises servers, and virtual machines (VMs).
* Automate the process of patching managed instances.

Wrong answers:

* Centrally manage parameters.
* Schedule and run scripts.

Node Management provides multiple capabilities for managing EC2 instances, on-premises servers, or VMs in a hybrid environment, in addition to other types of AWS resources. You can apply patches, manage inventory, manage sessions, and so forth.

#### A cloud application developer has been told that the webserver used by an Amazon Elastic Compute Cloud (Amazon EC2) hosted application needs to be updated. What is a node management topic that would apply?

* How to provision and configure compute nodes

Wrong answers:

* Best practices for security and access control
* How to monitor resource usage on nodes
* Strategies for scaling nodes up and down

Cloud application developers should have competency in provisioning, monitoring, managing, securing, and optimizing the nodes that run cloud applications.

### Node Management on AWS

Node management is the processes and tools used to deploy, configure, monitor, maintain, update, and troubleshoot the nodes that run applications and services in a distributed computing environment.

### Benefits of node management

Node management is critical for delivering robust, scalable applications and services. Learning how to handle routine node management tasks through automated tools empowers cloud application developers to focus on writing and maintaining application code. The additional benefit for application developers is spending less time focusing on maintaining underlying infrastructure.

* It provides monitoring capabilities like tracking CPU, memory usage, and disk space (Fleet Manager) for each node running an application. Cloud application developers can use these insights to fine-tune the application.
* It facilitates quick replacement of failed nodes, which ensures high availability of the overall application. Cloud application developers don't have to worry about underlying infrastructure failures.

### Node management on AWS

AWS Systems Manager provides various capabilities for accessing, managing, and configuring your managed nodes. A *managed node* is any machine configured for Systems Manager.

AWS Systems Manager has a suite of capabilities for node management. They include

* Fleet Manager,
* Compliance,
* Inventory,
* Session Manager,
* Run Command,
* State Manager,
* Patch Manager,
* and Distributor.

#### Fleet Manager

With Fleet Manager, you can streamline your remote server management process. Fleet Manager helps you to conveniently manage and troubleshoot your fleet of servers running on AWS and on-premises. You can drill down to individual servers to perform a variety of system administration tasks. These include disk and file exploration, log management, Windows Registry operations, and user management, without needing to remotely connect to your VMs.

#### Compliance

You can use Compliance to scan your fleet of managed instances for patch compliance and configuration inconsistencies. You can collect and aggregate data from multiple AWS accounts and Regions, and then drill down into specific resources that aren’t compliant.

#### Patch Manager

Patching your own servers and instances can be challenging, in terms of time consumption, task repetition, errors, downtime, and compliance issues. Patch Manager automates the process of patching managed nodes with both security-related updates and other types of updates.

Using Patch Manager, you can deploy patches by automating the following tasks:

* Choose whether the patch policy will **Scan** the specified targets or **Scan and install** patches on the specified targets.
* Select a schedule. Patch Manager integrates with Maintenance Windows, a capability of AWS Systems Manager. You can create maintenance windows for a specific time to apply patches on specified targets.
* Select the patch baseline. Choose the default patch baseline defined for each OS supported by AWS or a custom patch baseline.
* Specify the target group, either within a single account or across your organization and OUs.

#### Inventory

AWS Systems Manager Inventory provides visibility into your AWS computing environment. You can use Inventory to collect metadata from your managed nodes. The gathered data gives you the ability to manage application assets, track licenses, monitor file integrity, and discover applications not installed by a traditional installer.

### Use cases

#### Fleet Manager

**Problem:** AnyCompany is developing a suite of cloud-focused applications that will be deployed across multiple AWS accounts and Regions. The development team needs an efficient way to provision and manage EC2 instances to run these applications during the development and testing phases. Manually launching and configuring EC2 instances is time-consuming and does not allow for automation or scaling.

**Solution:** AnyCompany can use Amazon Fleet Manager to centrally manage a fleet of EC2 instances that run AnyCompany's applications. Fleet Manager allows EC2 instances to be deployed and managed across multiple AWS accounts and Regions from a central interface. It enables automation around instance provisioning, configuration, and lifecycle management. They can scale the fleet up and down on-demand, monitor fleet usage, and optimize costs.

#### Compliance

**Problem:** A startup is building a new cloud-focused application that will run on AWS infrastructure. As part of their security and compliance requirements, they need to ensure the application servers are configured according to industry best practices and internal policies. Misconfigurations could lead to security vulnerabilities or availability issues. Manually checking and enforcing configuration compliance across a dynamic fleet of servers will be very challenging.

**Solution:** AWS Systems Manager Compliance allows defining a compliance policy with required configuration rules. It can then continuously scan the fleet of EC2 instances to check if they comply with the policy. Any violations are reported for remediation. Compliance integrates with AWS Config to track resource configuration changes. This allows the startup to enforce and validate compliance of their cloud environment as per their security and regulatory needs.

#### Inventory

**Problem:** A cloud application development company manages a large fleet of EC2 instances across multiple AWS accounts and Regions. The developers need visibility into the software, applications, and configurations running across this diverse environment. It is difficult for them to track what is installed where and ensure consistency as they rapidly deploy new instances. This lack of centralized inventory makes it challenging to manage their environment efficiently.

**Solution:** AWS Systems Manager Inventory can help solve this issue by providing centralized visibility into the deployed software, applications, and configurations across EC2 instances. Developers can use Inventory to scan instances and collect metadata about installed packages, services, and network configurations. This inventory data can then be queried through the AWS Management Console or APIs to gain insights into the fleet. Inventory integrates with other AWS services like Patch Manager and State Manager to take actions across the fleet based on the inventory data. This improves efficiency and consistency for managing a dynamic, scalable cloud environment.

#### Patch Manager

**Problem:** Example Corp is a mid-sized company with over 500 Amazon EC2 instances across multiple AWS accounts and Regions. Keeping these instances patched and secure is becoming an operational burden for their small IT team. They are spending significant time and effort trying to track patch compliance across their fleet, scheduling patch deployments, and verifying that patches were applied successfully.

Example Corp needs an automated way to patch their EC2 instances that can scale across Regions and accounts. Their team can then focus less on patch management and more on strategic initiatives that drive business value.

**Solution:** AWS Systems Manager Patch Manager could be used to help Example Corp automatically patch their EC2 instances. Patch Manager integrates with AWS SSM documents that contain instructions for patching various operating systems. Example Corp can create patching baselines that define which patches should be installed on their instances. These baselines can be applied across AWS accounts and Regions. SSM documents simplify the process of keeping AMIs patched and enable Patch Manager to patch at scale.

Using Patch Manager and SSM documents, Example Corp can automatically deploy operating system and software patches across their Amazon EC2 fleet. This removes the burden of manual patch tracking and deployment from their team. They gain visibility into patch compliance and can focus on more strategic efforts.

### What is State Manager?

State Manager is a secure and scalable configuration management service that automates the process of keeping your Amazon EC2 and hybrid infrastructure in a state that you define.

#### Features of State Manager

* **State Manager associations:** State Manager helps you keep your AWS resources in a state that you define and reduce configuration drift. To do this, State Manager uses associations. An *association* is a configuration that you assign to your AWS resources. The configuration defines the state that you want to maintain on your resources.
* **Flexible scheduling options:** State Manager offers options for scheduling when an association runs: immediate or delayed processing, or cron and rate expressions.
* **Multiple targeting options:** State Manager supports targeting AWS resources by using tags, AWS Resource Groups, individual node IDs, or all managed nodes in the current AWS Region and AWS account.
* **Amazon S3 support:** With State Manager, you can store the command output from association runs in an Amazon S3 bucket of your choice.  
* **EventBridge support:** State Manager is supported as both an event type and a target type in Amazon EventBridge rules.

### How does State Manager work?

State Manager is for any AWS customer who wants to improve the management and governance of their AWS resources and reduce configuration drift. State Manager uses SSM documents (for example, Automation and Run Command documents) to define your desired configurations.

As a cloud application developer, you might be responsible for authoring these documents and specifying things like what packages, files, and settings your application needs. The key is understanding how to author effective SSM documents and use State Manager for post-deployment configuration and maintaining the state of cloud environments.

1. **Choose or create an automation document.** Determine the state you want to apply to your managed instances and choose or create an SSM document. The document defines the actions that Systems Manager performs on your managed instances. Systems Manager includes preconfigured documents that you can use by specifying parameters at runtime. Documents use JSON or YAML, and they include steps and parameters that you specify.
2. **Associate your instance with the document.** Associate your managed instances with the SSM document.
3. **Specify a schedule for the state.** When creating the association, define the schedule for how often to apply the configured state.
4. **Output data to Amazon S3. (Optional)** Write the output of the commands to an Amazon S3 bucket when you create an association.

### Benefits of State Manager

By using pre-configured SSM documents, State Manager offers benefits for managing your nodes. With State Manager, you can do the following:

* Bootstrap nodes with specific software at start-up.
* Download and update agents on a defined schedule, including the SSM Agent.
* Configure network settings.
* Join nodes to a Microsoft Active Directory domain.
* Run scripts on Linux, macOS, and Windows managed nodes throughout their lifecycle.

### Demo: State Manager

With State Manager, you can define desired configurations, associate them to resources, automatically detect and fix drift, and provide compliance reporting.

State Manager is the service that we use to keep managed nodes in a state that you define.

We do that by first creating an association. Let's give the association a name: server-configuration. And next, I need to select an SSM document. I'm going to use a command document. There it is, AWS-RunShellScript. When I select that, I'm going to be prompted for the parameters for that document. This document is going to run commands on my instance. So one of the parameters that I need to pass is a list of commands.

My desired state is to switch off the SSH Daemon on this instance. So I'm going to paste in here the command that I use to disable that service. OK, I have my command in place. Now I need to choose my targets.

Which instances would I like this run on? And I can do that by specifying the tags. I would like to run this on all the instances tagged with application equals ProjectX. I add that.

I have the choice of running this on a schedule. I'm going to select no schedule because I would like State Manager to decide when this needs to be run, when a change to state happens, or a new instance matching the type of group that we have up here.

I'm going to leave all the other settings as the default and create my association. I already see there is an execution and a success. If I look at my association on the execution history that is already run once, that particular execution currently has no targets found. If we turn on a new instance that matches my targets, then we will see an execution happen. I already have that ready to go here. I have a web server instance configured and way down the bottom there. I'm associating this with a role that is going to authenticate the request that the SSM agent will make on the instant.

This is what allows the SSM Agent to communicate back to the service and find the commands that it needs to run.

If I go right back up to the top, I need to add an additional tag so that we match our targets. Application, ProjectX, and I'm ready to launch that instance. That is going to take a little while to launch. Let's come back to this when it has started.

We are back that did not take long at all actually. I'm looking at my association and again, if I go from my association to the Execution history, I can see it has run on a single target. That was the instance that I just turned on that matched on the tag.

If I have a look at the output, there we go, in the output it says that it has removed the SSHD service. The instance is now in my desired state.

What would happen if I changed my mind of my desired state? I would also like to remove the utility wget on my instance. So to change my desired state, I return back to my association and I edit the parameters that contains the commands that I would like to run on the instance. This is currently disabling SSHD. Let's paste in the command to remove the wget utility. OK. There we go. My desired state is now, I would like to remove the SSHD and I would also like to remove the utility wget.

I'm going to save my changes. There has now been a change to state. We can see the status of the association is currently pending. If I now look inside the association and on the execution history, we see a new execution ID that has run Version 2 of the association. That's the association that we just updated.

Let's dive into this. It has run on our single instance. And if I look inside the output, I see this message here that is telling me that it has removed the utility wget. OK.

So my desired state, initially, I wanted to remove SSHD. We turned on an instance that matched the targets. We saw that run. We had a change of mind, our desired state changed. We'd also like to remove the wget utility. We updated the command parameters and then we saw the execution run again on the instance to get our instance into the state that we want.

### What is Session Manager?

Session Manager, a capability of AWS Systems Manager, provides a way to connect to and manage your Amazon EC2 instances or your hybrid instances. You can use a web browser-based shell or the AWS Command Line Interface (AWS CLI). Session Manager provides a secure connection on your web browser, eliminating the need to open inbound ports on your managed nodes.

### Use and benefits of Session Manager

Session Manager provides secure, auditable shell access for a cloud application developer to troubleshoot, deploy, and manage applications in the cloud.

#### Centralized access control to instances using IAM policies

Administrators have a single place to grant and revoke access to instances. Using only IAM policies, you can control which individual IAM users or groups in your organization can use Session Manager, and which instances they can access.

#### No open inbound ports and no need to manage bastion hosts or SSH keys

Leaving inbound SSH ports and remote PowerShell ports open on your instances greatly increases the risk of entities running unauthorized or malicious commands on the instances. Session Manager helps improve your security posture by making it possible to close these inbound ports. It also frees you from managing SSH keys and certificates, bastion hosts, and jump boxes.

#### One-click access to instances from the console and AWS CLI

Using the AWS Systems Manager console or Amazon EC2 console, you can start a session with a single click. Using the AWS CLI, you can also start a session that runs a single command or a sequence of commands. Because permissions to instances are provided through IAM policies instead of SSH keys or other mechanisms, the connection time is greatly reduced.

#### Port forwarding

Redirect any port inside your remote instance to a local port on a client. Next, connect to the local port and access the server application running inside the instance.

#### Cross-platform support for both Windows and Linux

Session Manager provides both Windows and Linux support from a single tool. For example, you don't need to use an SSH client for Linux instances or a Remote Desktop Protocol (RDP) connection for Windows instances.

#### Logging and auditing session activity

To meet operational or security requirements in your organization, you might need to provide a record of the connections made to your instances and the commands that were run on them. You can also receive notifications when an IAM user in your organization starts or ends session activity.

Capabilities are integrated with AWS CloudTrail, Amazon S3, Amazon CloudWatch Logs, Amazon EventBridge, and Amazon Simple Notification Service (Amazon SNS).

### How does Session Manager work?

Session Manager works by using SSM Agent installed on your managed instances. When you start a session, Session Manager authenticates your credentials and permissions. It then establishes an encrypted connection between your local machine and SSM Agent on the instance. You can then securely run commands and scripts on the instance using your web browser or AWS CLI.

Session Manager requires the following configuration information:

* Configure your instances to use Session Manager.
* Assign user IAM policies to control instance access.
* Specify account options for sessions logs.
* Start a session on your instances by launching bash or shell terminal.

### Demo: Session Manager

From the AWS console, we will go to EC2, and from EC2, we will take a look at our running instances.

So we can see we have a couple. One is a Linux machine and a Windows server. I'm going to select the Windows server first. Right click on it and select connect.

So traditionally, you had the ability to use RDP for connecting to a Windows machine. However, now you also have the option to select Session Manager to connect to your instance.

So we are going to select Session Manager and click connect. And once connected, we can see that we logged on to the machine using a Powershell shell and we can begin administering this instance.

Now, if we went back to the EC2 console, selected the Linux machine and connected, we are going to select Session Manager again, and connect, we can see that it's also a shell. It's a bad shell in this case.

Now, you can also connect to Session Manager from the Systems Manager console. So let's go there.

We will select Systems Manager. Now we will select Session Manager. And we can see that we have two active connections, one to the instance running Windows and one to the instance running Linux.

If we wanted to start another connection, what we could do is start a connection and then specify the instance that we wanted to connect to. Session Manager is just as easy to use from the AWS CLI if you have the additional optional plugging installed.

So if I go to the AWS CLI, I will go and execute AWS SSM, which is a name space, start a session, and then specify a target that I have permissions to connect. So I will click enter. This will initiate a connection and it will tell me that I'm connected. So now what we're gonna do is we're gonna type in a few commands and this is going to allow us to audit what were the commands that I entered.

So for example, let's say I wanted to change the password for the administrator account. I can do net user administrator Password 1234! hit enter. Ok. So that command completed successfully.

Now, I should be able to see both in S3 and CloudWatch Logs, this particular command and also the result of that command. Now, before we go and take a look at the logs, let's terminate our connection.

So if we go back to the Session Manager console and click on the Session history tab, you can see that there are a few different connections that were generated. Now, there's one in particular that we're gonna audit. Let's see, it's the one from Cindy. So what we will do is we will open both the S3 log and the CloudWatch Logs log to view the activity.

Let's take a look at CloudWatch first. So we can see the connection activity here in CloudWatch. If we expand this item, we can see a lot more details about the connection. So we can see that net user password was successfully entered and that we also terminated the connection after setting the password.

If we went to S3, we could also see that same activity in the form of a log, but we would have to download the file and view the contents of that file to be able to see what was in that log. Both are usable, applicable. It really depends on what your requirements are for the auditing.

For example, if you wanted to create Cloudwatch Events that sent you a notification once a particular pattern of an event took place. So for example, sudo in Linux, if somebody sudos, you can create a pattern that will monitor that activity and then send a notification to either you or your security team when sudo has been entered into a session.

So let's take a look at how this would be configured. If we go to preferences back in Session Manager and go to edit, we can see that there are a few different options for us to enable.

The ones that we care about for the moment is the S3 bucket where we specify the bucket name where our logs will be stored. We can define whether a bucket is encrypted or not, so that way that encryption is handled appropriately.

Also, Cloudwatch. So you specify the cloud log group that all of the session events or activity should be sent to. In my case, I'm sending it to Session Manager sessions. And the same as with a bucket, you can also define whether the data should be encrypted or not.

There are other settings that can be set to leverage additional Session Manager functionality. For example, on Linux instances, you can define what user, either a role or an IAM user, will use when connecting using Session Manager.

So if we enable the setting here, and we specified a particular user, every connection will make use of that user when using Session Manager. If I leave this blank and I go to Identity and Access Management, and for example, let's find my developer, Cindy. And if we take a look at Cindy's settings, we can define a tag with a key name SSMSessionRunAs and then the tag value will be Cindy. Now, Cindy has to be a user within the operating system that I can use for Session Manager.

So let's go back to Session Manager. And what we're gonna do is we're going to say yes, save to settings.

Once the settings are set, what I will do is create a connection to my Linux instance using Session Manager. So I will hit enter.

Now, this particular session is configured to use Cindy, that IAM role Cindy.

So if I take a look at who I'm connected as from Session Manager, we will see that the local user, Cindy, is associated with my connection. Now, this particular user does not have administrative privileges. So this is also beneficial because you can restrict the level of access a user can have for Session Manager.

### What is Run Command?

Using Run Command, you can remotely and securely manage the configuration of your managed nodes. With Run Command, you can automate common administrative tasks and perform one-time configuration changes at scale.

### Benefits of Run Command

With Run Command, developers can conveniently automate and scale application management tasks across large fleets of instances.
Deploy applications to EC2 instances: Run Command can be used to deploy applications, update config files, and install dependencies across hundreds of EC2 instances with just one command.

* **Automate post deployment tasks:** After deploying an application, cloud application developers can use Run Command to run scripts that configure the instances, verify the deployments, and initiate health checks.
* **Restart applications:** Quickly restart applications on multiple instances when needed.
* **Launch maintenance tasks:** Run scripts to clean up logs, update certificates, and rotate access keys on a schedule.
* **Install software dependencies:** Install languages, frameworks, and packages needed for the application without manually accessing each instance remotely.
* **Fetch deployment logs:** Use the output capability to aggregate logs from all instances to debug issues in one place.
* **Validate deployments:** Run integration and smoke tests on the newly deployed application across the fleet.
* **Remediate issues:** Fix configuration drifts or update vulnerable software versions across the fleet.

### Demo: Run Command

From the Systems Manager console, go to the **Run Command** section. Select **Run command** and  select **AWS-RunShellScript**, which is for platform type Linux. Enter command to execute. In my case, it is to install Apache, a web server. Now, this is a service that is being installed against a set of web servers.

You can also specify a directory, if necessary. You can specify a time out.

Next, target the instances. You can specify them manually or using a resource group or via tags.

Select Name as the key and Web Server as the value.

The rate control let you make sure that you only target x percentage of the resources at the same time. And if there's no issues, then you can proceed with doing the rest.

Do 25 percent, and the error threshold will be 1. So if you encounter one error during the execution, the execution will stop. This will prevent the application from being negatively impacted any further, if you do run into problems.

The output can be also logged to S3. And also there can be SNS notifications set up for any execution, either success or failure. Skip that configuration at the moment.

Select Run and we will wait for the execution to complete. There are five resources that match the target, which was the tag, and only one of them is currently in progress. So only one of them will be targeted initially and then additional ones will be targeted once you know for a fact that there are no issues with this script.

Apache was successfully installed on all of the instances you targeted.

You can use this approach for autoscaling groups. You can use this approach for hundreds, for thousands of servers, array control very, very important in this scenario. And you can also create the same run instantiations via the CLI or the SDKS.

### Run Command use case

1. Set up proper IAM roles and permissions for the instances they want to manage.
2. Make sure those instances have the SSM Agent installed and configured.
3. Test running basic commands on one instance before deploying across a fleet.
4. Configure logging so they can monitor and debug command results.
5. Use targeting to control which instances will run the commands.

### AWS Systems Manager Distributor

Distributor helps customers who want to create new software packages or deploy existing software packages. This includes deploying AWS published packages to multiple Systems Manager managed instances at one time.

### Benefits of Distributor

Distributor gives cloud application developers more control, automation, and visibility for application and package management across distributed systems. It complements Run Command for app deployment and management.

* **One package, many platforms:** When you create a package in Distributor, the system creates an SSM document. A package is a collection of installable software or assets that include a .zip file of software per target operating system platform or a JSON-formatted manifest file that describes the package contents. You can attach .zip files to this document. When you run Distributor, the system processes the instructions in the SSM document and installs the software package in the .zip file on the specified targets. Distributor supports multiple operating systems, including Windows, Ubuntu Server, Debian server, and Red Hat Enterprise Linux.
* **Control package access across groups of managed instances:** You can use Run Command or State Manager to control which of your managed nodes get a package and which version of that package. Managed nodes can be grouped by instance or device IDs, AWS account numbers, tags, or AWS Regions. You can use State Manager associations to deliver different versions of a package to different groups of instances.
* **Many AWS agent packages included and ready to use:** Distributor includes many AWS agent packages that are ready for you to deploy to managed nodes.
* **Automate deployment:** Use State Manager to schedule packages for automatic deployment on target managed nodes when those machines are first launched to keep your environment current.

### Distributor use case

Example Corp is a software company that develops and sells a cloud-based application to customers. Their development team frequently needs to deploy new builds and updates of the application to test environments for quality assurance. Currently, the developers manually deploy each new build to multiple test environments, which is time consuming and error prone.

Example Corp is looking for a way to automate and streamline the deployment of application builds to their test environments. They need a solution that can deploy builds faster, with less effort, and in a consistent repeatable manner.

#### How can AWS Systems Manager Distributor help Example Corp?

Distributor could be used to automate deployments of the application builds to their test environments. Developers can define and schedule deployments that will automatically push new builds out to multiple AWS compute environments. Distributor handles deploying builds in a reliable and repeatable way without requiring manual work by developers.

It gives Example Corp the ability to standardize and scale their application deployments across test environments.

### [Lab: Create a Package in Systems Manager Distributor](./W06Lab3-CreatingAPackageInDistributor.md)

### Knowledge Check

#### What is a capability of node management using AWS Systems Manager? (Select THREE.)

* Track resource inventory and system configurations across Amazon Elastic Compute Cloud (Amazon EC2) instances.
* Automate patch management across fleets of Amazon Elastic Compute Cloud (Amazon EC2) instances.
* Monitor operational metrics and compliance status of managed instances.

Wrong answers:

* Schedule routine backups of instance storage volumes.
* Monitor operating system and application logs for troubleshooting.

Node management within AWS Systems Manager provides automation, insights, and control to manage your infrastructure at scale. This includes both cloud and on-premises servers. It helps streamline operational management.

#### Which task would a cloud application developer use Session Manager to complete?

* Connecting to Amazon Elastic Compute Cloud (Amazon EC2) instances without opening inbound ports

Wrong answers:

* Managing configuration changes across a development environment
* Controlling application deployment across AWS Regions
* Running commands across multiple servers using Run Command

Session Manager provides secure and auditable node management without the need to open inbound ports, maintain bastion hosts, or manage Secure Shell (SSH) keys.

#### What is a benefit of using Run Command?

* It remotely and securely manages the configuration of managed instances.

Wrong answers:

* It provides a central place to view and track operational data from multiple AWS services.
* It provides a visualization of resources with interactive maps.
* It monitors and troubleshoots applications.

Run Command remotely and securely manages the configuration of managed nodes. With Run Command, developers can conveniently automate and scale application management tasks across large fleets of Amazon EC2 instances.

### Summary

#### Node management in AWS

Systems Manager provides robust capabilities to perform tasks like inventory tracking, configuration management, patching automation, and running commands at scale across nodes.

As a cloud application developer, it is important to understand these capabilities and other AWS capability integrations. Even if you are not hands-on with some of these capabilities, others in your organization will be.

#### Fleet Manager

Fleet Manager provides centralized visibility and control to securely manage fleets of instances at scale. It helps ensure consistency, security, and compliance across hybrid or cloud-based server infrastructure through automation and policy enforcement.

#### Compliance

Compliance makes it more convenient to assess, monitor and remediate configuration compliance against security best practices and regulations across your AWS resources.

#### Inventory

Inventory provides visibility into your Amazon EC2 and on-premises computing environment. It does this by collecting metadata such as OS, software installed, network configurations, running processes, and services from your managed instances.

#### Patch Manager

Patch Manager automates the process of patching managed instances with both OS and software patches. It also provides scheduling patching.

#### State Manager

State Manager defines and maintains consistent OS configurations, such as installing patches, joining domains, installing software, and more.

#### Session Manager

Session Manager provides secure and auditable instance management without needing SSH access or bastion hosts.

#### Run Command

Run Command remotely and securely manages a fleet of EC2 instances by automating common administrative tasks at scale. Commands can run on one or thousands of instances simultaneously.

#### Distributor

Distributor provides centralized control and automation over software deployment across your infrastructure. It helps ensure consistent patching and configuration of applications across a fleet of servers and instances.

### Additional Resources

#### [AWS Systems Manager Node Management](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-instances-and-nodes.html)

#### [Remotely Run Commands on an EC2 Instance with AWS Systems Manager](https://aws.amazon.com/getting-started/hands-on/remotely-run-commands-ec2-instance-systems-manager/?ref=gsrchandson&amp;id=itprohandson)

#### [Node Management](https://docs.aws.amazon.com/whitepapers/latest/aws-systems-manager-operational-capabilities/node-management.html)

#### [Streamline Server Fleet Management with AWS Systems Manager Fleet Manager](https://aws.amazon.com/blogs/mt/streamline-server-fleet-management-aws-systems-manager-fleet-manager/)

#### [Manage Distribution of Software Packages With AWS Systems Manager Distributor](https://youtu.be/AvQWkfgEQI8?si=ZTYAR5marIlIm5Kk)
