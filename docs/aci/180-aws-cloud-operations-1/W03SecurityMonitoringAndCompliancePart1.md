# Security, Monitoring, and Compliance Part 1

* **back to AWS Cloud Institute repo's root [aci.md](../aci.md)**
* **back to repo's main [README.md](../../../README.md)**

## Compliance and Regulations

### Differentiating regulations and compliance

#### Regulations

A regulation is a rule created and maintained by an authority. Many companies have regulations that are specific to their industry, such as bio-pharmaceutical, manufacturing, and educational technology. The way that regulations are created and governed varies by region or country. The following are two examples of this variation.

**In the US:** Regulations are a set of requirements created by a regulatory body; for example, the U.S. Environmental Protection Agency (EPA). The regulatory body creates the regulations in response to the creation of a law, often called an act, by a governing body; for example, the United States Congress.

**In the Europe Union:** Regulations are laws created by a European Union (EU) governing body, such as the European Parliament and the Council of the European Union.

#### Compliance

Compliance is how organizations adhere to the legal requirements, laws, and guidelines that govern their business. The requirements an organization must follow might be because of any combination of the location of their business, the location of their customers, and the industry their business is in, such as the financial or health sectors.

### Data privacy

Data privacy laws and regulations oversee how organizations manage, store, and share sensitive data related to their employees and, in many cases, their consumers.

#### FEPRA

Family Educational Rights and Privacy Act (FERPA) is a US federal law that protects the privacy of student education records and applies to all schools that receive federal funding. It gives parents specific rights to their child's education records. This protection is transferred to the student when they turn 18 years old or attend a school beyond high school.

For more information, visit the [FERPA home page](https://www2.ed.gov/policy/gen/guid/fpco/ferpa/index.html) on the U.S. Department of Education's website.

#### HIPAA

Health Insurance Portability and Accountability Act (HIPAA) is a US federal law that protects how sensitive patient information is handled and disclosed by covered entities such as healthcare providers and health plans.

For more information, visit the [HIPAA home page](https://www.hhs.gov/hipaa/index.html) on the U.S. Department of Health and Human Services website.

#### CCPA

The California Consumer Privacy Act (CCPA) gives consumers control over the personal information they give to businesses. It protects rights such as the right to know if a business collects information about them, what information they collect, how the information is shared, and the right to correct inaccurate information.

For more information, visit the [CCPA home page](https://oag.ca.gov/privacy/ccpa) on California's Department of Justice, Office of Attorney General's website.

#### GDPR

General Data Protection Regulation (GDPR) is a law in the EU that governs how the personal information of EU citizens and residents is handled, regardless of the location of the offices of the organization that collects the information.

For more information, visit the [What is GDPR](https://gdpr.eu/what-is-gdpr/) home page on the GDPR.eu website.

### Accessibility

Accessibility means that everyone who uses a product or service can receive the same benefit, regardless of any condition or disability they might have. Accessibility is about identifying barriers that exist in the environment and working to remove them. Some barriers can be removed by making sure that the environment works with any special equipment a person with a disability needs to use. The following are examples of accessibility considerations:

* Including closed captions and transcripts for audio
* Making colors readable by someone who is color blind
* Having clear titles and section headings so users can easily navigate content

In cloud application development, accessibility refers to whether a cloud application is built with consideration for disabilities that might include visual, hearing, or motor impairment. Accessibility is an important consideration for all development organizations. Some organizations might be required to follow the guidelines, depending on factors such as how it is funded or who their audience is. 

#### WCAG

The Web Content Accessibility Guidelines (WCAG) provide design and development guidance for content on the web. Although they do cover a myriad of disabilities, they are not meant to be all-encompassing. The following are some common considerations that fall under WCAG:

* Text size
* Keyboard shortcuts
* Alternative text for images
* Closed captions

For more information, visit the [Web Content Accessibility Guidelines (WCAG) 2.1](https://www.w3.org/TR/WCAG21/) homepage on the World Wide Web Consortium (W3C) website. 

### Information security

#### CIS

Regulations and guidelines related to information security govern how computer systems and applications are secured.

Center for Internet Security (CIS) provides cloud security guidance that is highly prescriptive and covers many popular vendors. These guidelines are referred to as benchmarks. 

To learn more, visit the [CIS Benchmark List](https://www.cisecurity.org/cis-benchmarks) home page on the CIS website.

#### PCI DSS

Payment Card Industry Data Security Standard (PCI DSS) was set up by the PCI Security Standards Council (PCI SSC). They provide guidelines for how payment information, such as credit card numbers, is stored and protected.

For more information, visit the [PCI DSS Quick Reference Guide](https://www.pcisecuritystandards.org/pdfs/pci_ssc_quick_guide.pdf) found on the PCI website.

#### ISO 27000 family and 9001

The International Organization for Standardization (ISO) creates international standards for a variety of industries, including information security and quality management. The ISO 27000 family of standards includes recommendations for information security management. The ISO 9001 standard focuses on quality management, including the requirement for an Information Security Management System. 

To learn more, visit the [ISO 27000 family](https://www.iso.org/standard/iso-iec-27000-family) home page and the [ISO 9001](https://www.iso.org/standard/62085.html) home page on the ISO website.

## Compliance with AWS

Security and compliance are a shared responsibility between AWS and the customer. This shared model can help relieve the customer’s operational burden. AWS operates, manages, and controls the components, from the host operating system and virtualization layer down to the physical security of the facilities in which the service operates. 

AWS is responsible for many security controls that reduce the threat surface and vulnerability of a cloud-hosted workload. However, customer responsibility is still critical to a secure environment.

The two areas of responsibility are typically categorized as security of the cloud (AWS responsibility) and security in the cloud (customer responsibility). This course will focus on how you can best secure the network components of your workload.

## Customer responsibilities

AWS customers are responsible for maintaining adequate compliance in their environment. This extends to the following:

* Understanding what workloads need to be regulated, and by which applicable standard or organization
* Discovering applicable controls or checklist items that apply to workloads
* Mitigating security risks and applying applicable controls
* Verifying that the applied controls are deployed and functionally tested against the workload

### Customer challenges

Security and compliance requirements are constantly evolving because of changes in technology, processes, and threats. Protecting and safeguarding data is made difficult by the following:

* Technology changes in size and complexity
* Resources and workforce limitations
* Evolving threats and expanding threat surfaces

Meeting these challenges depends on an organization's resources and capabilities. In general, organizations must use their resources and capabilities to manage risks. Before discussing risk, it is important to define three related concepts: vulnerabilities, threats, and risks.

## AWS compliance programs

With thousands of controls used to meet internal security requirements, AWS maps internal controls to the applicable compliance requirement. This approach to compliance can be adopted by AWS users. It is a useful starting point when considering local laws and regulations.

By using AWS, customers inherit comprehensive compliance controls to help them satisfy compliance requirements for many regulatory agencies around the globe. The IT standards that AWS complies with are broken out by the following:

* Certifications and attestations
* Laws, regulations, and privacy
* Alignments and frameworks

Compliance certifications and attestations are assessed by a third-party independent auditor and result in a certification, audit report, or attestation of compliance. These certifications, reports, or attestations are available to customers as documentation concerning the AWS inherited controls.

**Customers are not automatically compliant with all the regulations that AWS complies with. The Shared Responsibility Model means customers inherit some controls, such as physical security, by being an AWS customer. Some controls are not automatically inherited, but can be fulfilled through the capabilities of AWS services.**

### [Risk and Compliance position paper](https://docs.aws.amazon.com/whitepapers/latest/aws-risk-and-compliance/welcome.html?refid=cr_cardrams/)

## Vulnerabilities, Threats, and Weaknesses

* A **vulnerability** is a weakness in a system or application that can be exploited.
* A **threat** is a possibility for an event or act to exploit a vulnerability.
* A **risk** is the potential for loss, damage, or destruction of resources because of a threat.

### Vulnerabilities

Some vulnerabilities exist as a part of an operating system (whether it is a server, host, or network infrastructure) or application software. This type of vulnerability is referred to as Common Vulnerabilities and Exposures (CVE). The CVE program is overseen by the MITRE Corporation with funding from the Cybersecurity and Infrastructure Security Agency (CISA), part of the U.S. Department of Homeland Security.

CVEs are derived from a list of publicly disclosed computer security flaws. When we refer to a CVE, it means that there is an identified security flaw that has been assigned a CVE ID number. Security advisories issued by vendors and researchers generally mention at least one CVE ID. The CVE IDs are often used to describe the vulnerabilities addressed by security patches issued by vendors.

#### Case study: Log4Shell

In December 2021, Apache announced the Log4Shell vulnerability for its open source Java logging library, Log4j. Named Log4Shell, the vulnerability gave an attacker the ability to run arbitrary code on a vulnerable server.

A bug in the library made it possible for an attacker to give an application using Log4j a malicious payload, or piece of data. When this data was logged by Log4j, it would reconfigure the application's server to communicate with a second server that was under the attacker's control. This second server could then deliver instructions to the vulnerable application server to download and run a Java class. A Java class is used to perform actions such as the following:

* Create objects
* Define object data types
* Define Java methods

The attacker could then use these new objects, data types, and methods to take control of the server.

##### Response from AWS

Apache advised organizations such as AWS to upgrade to newer versions of Log4j, where the bug had been fixed.

##### Server changes and monitoring

Network Access Control Lists (network ACLs) can be used to block ports used for communication to the server that is under the attacker’s control. Services and features such as Amazon Inspector, Amazon GuardDuty, and VPC Flow Logs can be used to find applications inside Amazon Virtual Private Cloud (Amazon VPC) that are potentially vulnerable.

##### Application protection

AWS WAF can be used to protect your applications by detecting malicious payloads. 

##### Patching

Installing an AWS supplied hotpatch using Patch Manager, a capability of AWS Systems Manager, and the provided guidance to mitigate issues by using containerized applications.

##### [Using AWS Security Services to Protect Against, Detect, and Respond to the Log4j Vulnerability](https://aws.amazon.com/blogs/security/using-aws-security-services-to-protect-against-detect-and-respond-to-the-log4j-vulnerability/)

##### [Update for Apache Log4j2 issue](https://aws.amazon.com/security/security-bulletins/AWS-2021-006/)

### Threats

Some of the threats that are faced in traditional, on-premises data centers and enterprise environments can also manifest in the cloud. These threats may include the following:

* A distributed denial of service (DDoS) attack is an attack in which multiple compromised systems attempt to flood a target, such as a network or web application, with traffic. A DDoS attack can prevent legitimate users from accessing a service and can cause the system to crash because of the overwhelming traffic volume.
* Malware infections, such as ransomware, use encryption to hold information for ransom. A user’s or organization's critical data is encrypted so that they cannot access files, databases, or applications. The adversary demands a ransom payment to provide the private key needed to decrypt the information. According to various security research groups, ransomware has more than doubled in frequency in 2021 from the previous year.
* Misconfigurations can create a variety of vulnerabilities that result in compromise.

### Risks

Risk analysis seeks to identify, measure, and mitigate various risk exposures or hazards that your workload faces. Risk analysis is generally performed with either a quantitative or a qualitative analysis.

* Quantitative risk analysis uses mathematical models and simulations to assign monetary values to risk.
* Qualitative risk analysis relies on a person's subjective judgment to build a theoretical model of risk for a given scenario. This is often expressed based on two key factors: the likelihood and the impact of the threat being assessed.

Threats are continuously changing; new vulnerabilities are discovered every day. The increasing volume and severity of threats present significant risks to organizations with operations that depend on digital resources. A risk analysis provides you with a point-in-time snapshot. You can use this as a part of your risk-management process.

## Frameworks and Standards

Many security controls are available in AWS, and they can be implemented in a variety of ways. The options can be complex and confusing, especially when an organization must comply with multiple regulatory and legal requirements.

With a standards-based approach, organizations can benefit from the knowledge and experience of a wide range of industry best practices to secure their workloads. With the right frameworks, you can use these best practices and map security controls to your requirements. By implementing best practices through applicable frameworks, you can simplify meeting security requirements and ensure your organization is protecting the right resources with the right controls.

### New to the cloud

Organizations moving to the cloud have resources, such as the AWS CAF, to help guide them in using proven best practices. This framework provides guidance that supports each unit in the organization.

### Any cloud user

Organizations already in the cloud, and those moving to the cloud, can use the AWS Well-Architected Framework. This framework provides current architectural best practices for designing and operating reliable, secure, efficient, and cost-effective workloads in the cloud. It provides a way for organizations to consistently measure their workloads against best practices and identify areas for improvement.

### Additional requirements

Cloud users must implement lifecycle risk management that connects business and mission objectives to cybersecurity activities, based on applicable security requirements. These requirements are driven by industry and operational standards, geopolitical regulations, and additional variables, such as available technology.

## Considerations for AnyCompany

* As an international e-commerce company, AnyCompany collects electronic payments from their customers. As a result, they must consider data privacy regulations, such as the CCPA and GDPR, if they have customers from California or any country in the European Union.
* Additionally, they will need to follow the PCI Security Council's standards for processing electronic payments.
* Because they use cloud technology and have information technology infrastructure, they will have to consider the following:
 * CIS benchmarks
 * ISO 27000 family and ISO 9001 standards
* As an organization, AnyCompany has employees. If they offer benefits, such as health insurance plans, or in they store any employee health information, they must be compliant with HIPAA.

## Knowledge Check

### Which of these is NOT an item that cloud monitoring can help with?

* Tracking the lifecycle of sensitive documents in a filing cabinet

Wrong answers:

* Tracking the lifecycle of sensitive documents in an Amazon S3 bucket
* Detecting when someone tries to access a resource without proper permissions
* Detecting when someone downloads a document and then sends it to someone else

### What is the difference between compliance and regulations in the European Union (EU)?

* Regulations are legal acts issued by the EU. Compliance is the set of actions that an organization takes to follow those legal acts and industry-specific guidelines.

Wrong answers:

* A regulation is a set of requirements issued by the EU in response to a law created by a governing body. Compliance is the set of actions that an organization takes to follow those requirements, laws, and industry-specific guidelines.
* Compliance is a set of requirements issued by the EU in response to a law created by a governing body. A regulation is the set of actions that an organization takes to follow those requirements, laws, and industry-specific guidelines.
* Compliance is a legal act issued by the EU. A regulation is the set of actions that an organization takes to follow that legal act and industry-specific guidelines.

### Which law governs data privacy of students in the US?

* Family Educational Rights and Privacy Act (FERPA)

Wrong answers:

* General Data Protection Regulation (GDPR)
* Stop Hacks and Improve Electronic Data Security Act (SHIELD Act)
* Digital Services Act (DSA)

* GDPR governs how the personal data of residents within the EU is collected, used, and transmitted.
* The SHIELD Act is a regulation in New York state that governs how its residents are protected from data breaches of their personal information.
* The DSA is an EU regulation focused on illegal and harmful content on large digital platforms.

## Summary

### Regulations and compliance

### Regulations

A regulation is a rule created and maintained by an authority. Many companies have regulations that are specific to their industry, such as bio-pharmaceutical, manufacturing, and educational technology. The way that regulations are created and governed varies by region or country. 

### Compliance

Compliance is how organizations adhere to the legal requirements, laws, and guidelines that govern their business. The requirements an organization must follow might be because of any combination of the location of their business, the location of their customers, and the industry their business is in, such as the financial or health sectors.

**Security and compliance are a shared responsibility between AWS and the customer. This shared model can help relieve the customer’s operational burden.**

### AWS compliance programs

With thousands of controls used to meet internal security requirements, AWS maps internal controls to the applicable compliance requirement. This approach to compliance can be adopted by AWS users. It is a useful starting point when considering local laws and regulations.

By using AWS, customers inherit comprehensive compliance controls to help them satisfy compliance requirements for many regulatory agencies around the globe. The IT standards AWS complies with are broken out by the following:

* Certifications and attestations
* Laws, regulations, and privacy
* Alignments and frameworks

### Vulnerabilities, threats, and weaknesses

These terms are often used interchangeably and incorrectly. It is important to understand how each of these terms should be used, what links them, and what sets them apart. The following is a way to differentiate them:

* A vulnerability is a weakness.
* A threat is a possibility for an event or act to exploit a vulnerability.
* A risk is the potential for loss, damage, or destruction of resources because of a threat.

### Standards and frameworks

With standards-based approach, organizations can benefit from the knowledge and experience of a wide range of industry best practices to secure their workloads. With the right frameworks, you can use these best practices and map security controls to your requirements. By implementing best practices through applicable frameworks, you can simplify meeting security requirements and ensure your organization is protecting the right resources with the right controls.

## AWS Tools for Monitoring and Responding

AWS has many services and features that monitor applications and accounts for compliance and security issues. This module will dive deeper into how to use the following services:

* CloudWatch stores AWS account and resource metrics.
* CloudTrail helps audit an account's security posture.
* EventBridge can automate security processes using AWS Lambda and other AWS security services.
* AWS Config can aid security governance and enforce compliance.

### Amazon CloudWatch

**Why this product matters to a cloud application developer:** CloudWatch can help you monitor, optimize, and maintain the performance and reliability of an application built on AWS.

**What is it:** CloudWatch is your gateway to monitor AWS resources and applications. It collects and tracks metrics so you are always up-to-date on what is happening within your account and applications.

The CloudWatch home page is a real-time dashboard that automatically displays metrics about every AWS service you use. You can also create custom dashboards to display metrics about your custom applications and to display custom collections of metrics that you choose.

You can create alarms that watch metrics and send notifications or automatically make changes to the resources you are monitoring when a threshold is breached. For example, you can monitor the CPU usage and disk reads/writes of your Amazon Elastic Compute Cloud (Amazon EC2) instances. Then, you can use this data to determine whether you should launch additional instances to handle the increased load. You can also use the data to stop under-used instances to save money.

With CloudWatch, you gain system-wide visibility into resource utilization, application performance, and operational health.

### AWS CloudTrail

**Why this product matters to a cloud application developer:** Having insight into what is happening within an AWS account, including the services used in an application, is crucial for the security of that application. Additionally, the information it collects can help cloud application developers analyze an application's operations and troubleshoot issues. With CloudTrail, you can see who is doing what, when it is being done, and if something looks suspicious. You can search and filter the logs it creates.

**What is it:** CloudTrail is like an AWS account's guardian. Its sole purpose is to record and store actions. It keeps a watchful eye on what is happening in the account. The information it gathers can be used for operational and risk auditing, governance, and compliance of your AWS account. 

In most instances, if someone does something in an AWS account—whether by a user, role, or an AWS service, CloudTrail records it as an event. These events can occur anywhere in the account, such as the AWS Management Console, the AWS Command Line Interface (AWS CLI), or through AWS SDKs and APIs. Currently, two AWS services or events are **not** supported by CloudTrail - **AWS Import/Export** and **Amazon VPC endpoint policy-specific events**.

There is no action required to enable CloudTrail. It is active in an AWS account when the account is created. When activity occurs in your AWS account, that activity is recorded in a CloudTrail event. CloudTrail does this in three ways:

* **Event history:** The event history is a record of the last 90 days of management events in an AWS Region. This record is viewable, searchable, downloadable, and immutable. There are no CloudTrail charges for viewing the event history.
* **AWS CloudTrail Lake:** CloudTrail Lake is a giant data lake that captures all AWS activity, even API activity. The events are aggregated into data stores and cannot be changed. You can search and analyze this data, and it can be kept for a long time—7 years (2557 days).

You can create an event data store for a single AWS account or multiple AWS accounts by using AWS Organizations. You can import any existing CloudTrail logs from your Amazon Simple Storage Service (Amazon S3) buckets into an existing or new event data store. You can also visualize top CloudTrail event trends with CloudTrail Lake dashboards.

There is one big caveat for the data lake: cost. For CloudTrail Lake, you pay for ingestion and storage together, where the billing is based on the amount of uncompressed data ingested during the month. When you run queries in CloudTrail Lake, you pay based on the amount of data scanned. 

* **Trails:** Trails capture a record of AWS activities. You can create trails for a single AWS account or multiple AWS accounts by using AWS Organizations. You can log Insights events to analyze your management events for anomalous behavior in API call volumes and error rates. These events are delivered and stored in Amazon S3 buckets. They can also be delivered to Amazon CloudWatch Logs and EventBridge. You can also use Amazon Athena to search and analyze the logs CloudTrail creates. You can deliver one copy of your ongoing management events to your Amazon S3 bucket at no charge from CloudTrail by creating a trail; however, there are Amazon S3 storage charges. In addition to using trails with AWS services, you can input these events into your security monitoring solutions.

Visibility into your AWS account activity is a key aspect of security and operational best practices. You can use CloudTrail to view, search, download, archive, analyze, and respond to account activity across your AWS infrastructure. You can identify who or what took which action, what resources were acted on, when the event occurred, and other details to help you analyze and respond to activity in your AWS account.

You can integrate CloudTrail into applications using the API, automate trail or event data store creation for your organization, check the status of event data stores and trails you create, and control how users view CloudTrail events.

### Amazon EventBridge

**Why this product matters to a cloud application developer:** EventBridge provides a means to build applications in a completely different way—using event-driven architecture that requires little coding. Event-driven architecture makes it so applications can scale and change in compartmentalized ways.

**What is it:** EventBridge is a serverless service that uses events to connect application components. Each event is like a puzzle piece, and EventBridge helps put them together to create super flexible applications. This flexibility, where an application's architecture is based on components creating and responding to events, is referred to as a loosely coupled system.

EventBridge takes events from various sources such as AWS services, third-party software, and in-house-built apps. They then can send the events to other parts of an application based on rules. To do this, EventBridge handles events in two ways.

* **Event buses:** Think of these as actual buses. They can pick up multiple events and deliver each of those events somewhere along the route. Because of this, event buses are well-suited for routing events from many sources to many targets.
* **Pipes:** EventBridge Pipes are a more direct line for events. They are intended for point-to-point integrations. Each pipe receives events from a single source and delivers them to single targets.

Pipes and event buses are often used together. A common use case is to create a pipe with an event bus as its target; the pipe sends events to the event bus, which then sends those events to multiple targets. For example, you could create a pipe with an Amazon DynamoDB stream for a source and an event bus as the target. The pipe receives events from the DynamoDB stream and sends them to the event bus, which then sends them to multiple targets according to the rules you've specified on the event bus.

The events that EventBridge routes can be archived, replayed, and reprocessed; further helping strengthen an application's security posture. If you can see what happens when something goes wrong, you can fix it more easily!

### AWS Config

**Why this product matters to a cloud application developer:** AWS Config helps cloud application developers manage and maintain the configurations of AWS resources. With this ability, developers can streamline operations and create more secure applications.

**What is it:** AWS Config is like a plane flying over your AWS account and surveying the land. It can tell you where things are and how they are set up. AWS Config does this in several key ways.

* It helps you keep track of the configuration of each AWS resource.
* It provides a historical record of what is changed in a resource configuration, who changed it, and when it was changed.
* It helps enforce standards for your infrastructure. This is super important when it comes to security and compliance.
* Rules can be set up in AWS Config to automatically remediate resource configurations that are not in compliance with an organization's standards.

An AWS resource is an entity you can work with in AWS, such as an Amazon EC2 instance, an Amazon Elastic Block Store (Amazon EBS) volume, a security group, or an Amazon VPC.

## Knowledge Check

### Which AWS service monitors API activity within an AWS account?

* AWS CloudTrail

Wrong answers:

* Amazon CloudWatch
* Amazon EventBridge
* AWS Config

* CloudWatch collects and visualizes real-time logs, metrics, and event data in automated dashboards to streamline your infrastructure and application maintenance.
* EventBridge facilitates the development of event-driven applications at scale across AWS, existing systems, or software as a service (SaaS) applications.
* AWS Config continually assesses, audits, and evaluates the configurations and relationships of your resources in AWS, on premises, and in other clouds. It can also enforce compliance.

### Which tasks can an organization perform with Amazon EventBridge? (Select TWO.)

* They can create and replay an archive of events in an application.
* They can route events based on how they match a rule.

Wrong answers:

* They can download a record of events over the last 90 days within an application.
* They can create a trail that logs management events. It does not include data or Amazon CloudWatch Logs Insights events.
* They can automate trail or event data store creation for your organization.

* The following action is performed in Amazon CloudWatch:
 * Download a record of events over the last 90 days within an application.
* The following actions are performed in AWS CloudTrail:
 * Create a trail that logs management events. It does not include data or CloudWatch Logs Insights events.
 * Automate trail or event data store creation for your organization.

### Which AWS service can use rules to evaluate resources and enforce compliance?

* AWS Config

Wrong answers:

* AWS CloudTrail
* Amazon CloudWatch
* Amazon EventBridge

* CloudWatch collects and visualizes real-time logs, metrics, and event data in automated dashboards to streamline your infrastructure and application maintenance.
* EventBridge facilitates the development of event-driven applications at scale across AWS, existing systems, or software as a service (SaaS) applications.
* CloudTrail monitors and records account activity across your AWS infrastructure, giving you control over storage, analysis, and remediation actions.

### Summary

AWS has many tools that monitor applications and accounts for compliance and security issues. To learn more about four of them, select each of the following flashcards.

#### CloudWatch

CloudWatch monitors AWS resources and the applications you run on AWS in real time. CloudWatch collects and tracks metrics, which are variables that can be measured for resources and applications.

CloudWatch alarms can watch metrics and send notifications. They can also automatically make changes to the resources you are monitoring when a threshold is breached. CloudWatch has a default dashboard on its homepage and also allows for the creation of custom dashboards.

#### CloudTrail

CloudTrail provides operational and risk auditing, governance, and compliance for an AWS account. Actions taken by a user, role, or an AWS service are recorded as events in CloudTrail. 

Events include actions taken in the AWS Management Console, AWS Command Line Interface (AWS CLI), and AWS SDKs and APIs. CloudTrail is active in an AWS account upon creation and does not require any manual setup. CloudTrail provides the following three ways to record an event: event history, CloudTrail Lake, and trails.

#### EventBridge

EventBridge is a serverless service that uses events to connect application components. Event-driven architecture is a style of building loosely coupled software systems that work together by emitting and responding to events. Event-driven architecture can help boost the agility of teams by helping them build reliable, scalable applications.

#### AWS Config

AWS Config provides a detailed view of the configuration of AWS resources in your AWS account. This includes how the resources are related to one another and how they were configured in the past so you can see how the configurations and relationships change over time.

An AWS resource is an entity you can work with in AWS, such as an EC2 instance, an EBS volume, a security group, or an Amazon VPC.

## Using CloudWatch

### Pre-assessment

#### What is a name-value pair that is part of the identity of a metric called?

* Dimensions

Wrong answers:

* Resolution
* Namespace
* Unit

* Resolution refers to the granularity of a metric. It can be either a high-resolution (a granularity of 1 second) or a standard resolution (a granularity of 1 minute).
* Namespaces are containers for CloudWatch metrics. Metrics in different namespaces are isolated from each other so that metrics from different applications are not mistakenly aggregated into the same statistics.
* Units are how metrics are measured. Example units include bytes, seconds, counts, and percentages.

#### Which type of data collection requires that the Amazon CloudWatch agent must be installed first?

* Host-level metrics

Wrong answers:

* CPU metrics
* Network utilization metrics
* Disk performance metrics

There are some internal system metrics, such as memory utilization, that Amazon EC2 does not send to CloudWatch by default. To collect host-level metrics and logs, the CloudWatch agent must be installed. The other options are incorrect because they do not require agent installation.

#### What kind of Amazon CloudWatch alarm goes off only if all conditions of a rule are met?

* Composite alarm

Wrong answers:

* Metric alarm
* High-resolution alarm
* Percentile-based alarm

* Metric alarms watch a single CloudWatch metric or the result of a math expression based on CloudWatch metrics. The alarm performs one or more actions based on the value of the metric or expression relative to a threshold over a given number of time periods.
* A high-resolution alarm is a type of metric alarm and can be set with a granularity of 10 seconds or 30 seconds.
* Percentile-based alarms are a type of metric alarm where you can specify what to do when there is not enough data for a good statistical assessment. You can choose to have the alarm evaluate the statistic anyway and possibly change the alarm state. Or you can have the alarm ignore the metric while the sample size is low and wait to evaluate it until there is enough data to be statistically significant.

### Security and compliance benefits of CloudWatch

* **Log monitoring:** With CloudWatch, you can centrally collect and monitor log data from your AWS resources, servers, and applications. This helps with security monitoring, troubleshooting issues, and compliance auditing.
* **Alarming:** You can create alarms in CloudWatch that activate notifications or scaling actions when certain thresholds are met. This is useful for security monitoring to alert you of potential issues.
* **PCI and ISO compliance:** CloudWatch tools and features help organizations achieve and maintain PCI DSS and ISO 27001 compliance standards. Things like log monitoring, user activity tracking, and configuration changes support compliance.
* **Infrastructure monitoring:** Detailed monitoring of your AWS infrastructure components aids security monitoring to detect issues and support compliance audits.
* **Sarbanes-Oxley Act (SOX) compliance:** CloudWatch logging and monitoring assists with SOX compliance requirements around control procedures, auditing, and security. SOX compliance requires businesses operating in the US to follow standards for financial reporting, electronic record logging and auditing, monitoring for system breaches, and safeguarding data.
* **Security groups and access control lists (ACLs):** You can use CloudWatch metrics and alarms to monitor metrics from VPC logs. These metrics can provide insight into activity against AWS security groups and ACLs and alert on potential malicious behavior.

Many AWS services provide functions that overlap throughout AWS Well-Architected Framework's security pillar. The following are the four main types of security controls:

* **Preventative controls:** These controls are designed to prevent an event from occurring. 
* **Proactive controls:** These controls are designed to prevent the creation of noncompliant resources.
* **Detective controls:** These controls are designed to detect, log, and alert after an event has occurred.
* **Responsive controls:** These controls are designed to drive remediation of adverse events or deviations from your security baseline.

Detective controls are often used to support legal or compliance obligations for threat identification and response efforts. One such service is CloudWatch.

#### Metrics

CloudWatch provides a time-ordered set of data points called metrics. These are used to monitor and publish application or business activity data. Many AWS services offer metrics at no cost, while others offer detailed monitoring or custom metrics with charges. You can add metric data points in any order and at any rate. Each data point includes a time stamp and unit of measure.

When using metrics in CloudWatch, the four main things you should consider are resolution, frequency, alarms, and cost.

#### Namespaces

A namespace is a container for CloudWatch metrics that isolates metrics from those belonging to different applications or services. Each namespace must have a valid ASCII name containing 255 characters or less. The namespace must be specified when publishing data points to CloudWatch. AWS namespaces typically follow the convention of using "/" and then a service name, like AWS/EC2. 

#### Dimensions

A dimension is a name-value pair that is part of the identity of a metric. You can assign up to 30 dimensions to a metric and use them to filter the results that CloudWatch returns.

When you retrieve statistics, you must specify the same values for the namespace, metric name, and dimension parameters that were used when the metrics were created. You can also specify the start and end times for CloudWatch to use for aggregation.

#### Resolution

The resolution of a metric refers to its granularity, or the time interval between measurements. A metric's resolution can be standard or high-resolution. Standard resolution metrics have a granularity of 1 minute.

When you publish a high-resolution metric, it is stored with a resolution of 1 second. You can read and retrieve it with a period of 1, 5, 10, 30, or any multiple of 60 seconds. High-resolution metrics provide more immediate insight into your application's activity, but every **PutMetricData** call for a custom metric is charged.

#### Statistics

Statistics are the result of data aggregation over a fixed time frame using specific dimensions and units. Statistics can be produced using custom data or by other AWS services, and are available in CloudWatch.

#### Percentiles

Percentiles can be used to gain better insight into how metric data is distributed. For example, you can watch the 95th percentile of CPU usage to find EC2 instances with an abnormally high load. 

As you would when using the other CloudWatch statistics (Average, Minimum, Maximum, and Sum), you can monitor your system and applications using percentiles. As long as you publish the raw, unsummarized data points for your custom metric, percentile statistics are accessible for custom metrics.

#### Alarms

Alarms are automated procedures that start based on changes to a specific metric over a predetermined period. They perform actions such as notifying an Amazon Simple Notification Service (Amazon SNS) topic. You can analyze alarms in dashboards.  

You should set the alarms to a period longer than or equal to the metric's resolution. Both regular alarms with 60-second intervals and high-resolution alarms with intervals of 10 seconds or 30 seconds are available for high-resolution metrics. There is a higher cost for high-resolution alarms.

### CloudWatch Metrics to Monitor for Security and Compliance

Metrics provide data in one of the following ways:

* They indicate a point within a range (for example, percentage of total capacity).
* They provide a quantitative measurement, such as total packets per second (PPS).

The metrics you choose to monitor for security and compliance will depend on your organization's industry and goals.

#### Indicators of compromise

Indicators of compromise (IoC) are largely similar in cloud environments to how they are in traditional IT environments. Alerting on anomalies helps recognize potential malware, malicious activities, or other indicators of a compromised system. Some of the types of anomalies that might be recognized through the use of CloudWatch alarms include the following:

* Abnormal Amazon EC2 CPU utilization
* Significant or sudden increases in database reads
* HTML response sizes
* Mismatched port-application traffic
* Unusual DNS requests
* Unusual outbound network traffic
* Anomalies in privileged user account activity
* Geographical irregularities (source or destination of traffic)
* Unusually high traffic at irregular hours
* Multiple, repeated, or irregular login attempts
* System average uptime

#### ELB and CloudWatch metrics

The logs provide detailed information about requests sent to Elastic Load Balancing (ELB). For example, the following metrics can signal malicious activities:

* **HTTPCode_ELB_5XX_Count** can be used to alarm about an increase of 500 range errors.
* **AnomalousHostCount** measures the number of hosts detected with anomalies.

You can also use CloudWatch ELB metrics and alarms to monitor for abnormal traffic spikes or volumes, which can help detect possible DDoS attacks or other security events.

Additionally, metrics and alarms can track SLA compliance indicators like request latency, error rates, and availability. They can notify teams if SLAs are at risk. In regulated industries like healthcare and finance, being able to provide audit trails and evidence of monitoring and alarms is often a compliance requirement.

##### [Improving availability](https://aws.amazon.com/blogs/networking-and-content-delivery/improving-availability-with-application-load-balancer-automatic-target-weights/)

#### Application Load Balancer and CloudWatch metrics

ELB publishes data points to CloudWatch for your load balancers and your targets. With CloudWatch, you can retrieve statistics about those data points as metrics. For example, you can monitor the total number of healthy targets for a load balancer over a specified period. Each data point has an associated time stamp and an optional unit of measurement.

ELB reports metrics to CloudWatch only when requests are flowing through the load balancer. If requests are flowing through the load balancer, ELB measures and sends its metrics in 60-second intervals. If no requests are flowing through the load balancer, or it has no data for a metric, the metric is not reported.

### CloudWatch agent

The CloudWatch agent is installed on hosts to collect host-level metrics, logs, and traces from EC2 instances and on-premises servers. With the unified agent, you can do the following:

* Collect internal system-level metrics from EC2 instances across operating systems. The metrics can include in-guest metrics and the metrics for EC2 instances. For information about the additional metrics that can be collected, visit [Metrics Collected by the CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/metrics-collected-by-CloudWatch-agent.html).
* Collect system-level metrics from on-premises servers. These can include servers in a hybrid environment and servers not managed by AWS.
* Retrieve custom metrics from your applications or services using the **StatsD** and **collectd** protocols. **StatsD** is supported on both Linux servers and servers running Windows Server. **collectd** is supported only on Linux servers.
* Collect logs from EC2 instances and on-premises servers, running either Linux or Windows Server.

You can store and view the metrics that you collect with the CloudWatch agent in CloudWatch as you can with any other CloudWatch metrics. The default namespace for metrics collected by the CloudWatch agent is **CWAgent**, although you can specify a different namespace when you configure the agent. Metrics collected by the CloudWatch agent are billed as custom metrics, which you will learn more about in the next section.

#### [CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html)

### Publishing custom metrics

With CloudWatch, you can publish your custom metrics using the AWS CLI or API. When the metrics are in CloudWatch, you can view them in the dashboard with metrics created by AWS services. Custom metrics can have a standard or high resolution.

1. Use the **PutMetricData** API to create the custom metric.
2. Use Python to create custom metric.
3. Publish the custom metric to the CloudWatch dashboard.

#### Some limits for publishing custom metrics

1. Each **PutMetricData** request is limited to 1 MB in size for HTTP POST requests.
2. Each request is limited to 1,000 or fewer different metrics.
3. Values are limited to the range of negative two to the 360th degree and positive two to the 360th degree.
4. Special values such as infinity and negative infinity are not supported.
5. You can have up to 30 dimensions per metric to help you clarify the metric's purpose.
6. You can specify data with timestamps up to 2 hours before the current date and time, and 2 weeks after the current date and time.
7. After you have created a custom metric, it can take up to 15 minutes for the metric to appear in calls to **ListMetrics**.

#### How CloudWatch stores metric data

1. CloudWatch stores metric data as a series of data points
2. You can also publish aggregated sets of data points called statistic sets.
3. Although you can publish data points with very granular timestamps, CloudWatch aggregates them to a minimum granularity of 1 second. It records various statistics like the average, maximum, minimum, and number of samples within each period.
4. If you need percentile statistics, CloudWatch requires raw data points to calculate them.
5. You can publish percentile statistics by using statistic sets or by using specific conditions.
6. When dealing with sporadic data, you can publish zeros for periods with no associated data. This is useful for tracking the total number of data points. You can also include data points with the value of 0 in statistics like minimum and average.

If you no longer need to publish a custom metric, change your application's code to stop using the PutMetricData API. Metrics cannot be deleted, but they automatically expire after 15 months if no new data is published to them. Data points older than 15 months expire on a rolling basis. As new data points come in, data older than 15 months is dropped.

AWS services do not support high-resolution metrics. Some services, however, can send detailed metrics to CloudWatch. For more information, see [Basic and detailed monitoring](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-metrics-basic-detailed.html) documentation page.

## Using CloudWatch Alarms

### Using CloudWatch anomaly detection

When you turn on anomaly detection for a metric, CloudWatch applies statistical and machine learning algorithms. These algorithms continuously analyze the metrics of systems and applications, determine normal baselines, and surface anomalies with minimal user intervention.

The algorithms generate an anomaly detection model. The model generates a range of expected values that represent normal behavior. With this feature, you can create anomaly detection alarms based on a metric's expected value. This type of metric alarm doesn't have a static threshold. Instead, the alarm compares the metric's value to the expected value based on the anomaly detection model. You can initiate an alarm when a metric value is above or below the band of expected values.

Anomaly detection algorithms account for the seasonality and trend changes of metrics. The seasonality changes could be hourly, daily, or weekly, as shown in this example.

### Alarm actions

You can specify what actions an alarm takes when it changes state between the OK, ALARM, and INSUFFICIENT_DATA states. These security-related actions, or others, might include one or many of the following:

* Notify one or more people by sending a message to an Amazon SNS topic.
* Perform Amazon EC2 actions (for alarms based on Amazon EC2 metrics).
* Perform actions to scale an Auto Scaling group.
* Initiate a Lambda function.
* Create OpsItems in OpsCenter, a capability of AWS Systems Manager, or Incident Manager, capability of AWS Systems Manager, when the alarm goes into ALARM state.

### Types of alarms

You can create two types of alarms: metric and composite.

#### Metric alarms

These alarms watch a single CloudWatch metric or the result of a math expression based on CloudWatch metrics. The alarm performs one or more actions based on the result, such as sending a notification to an Amazon SNS topic, performing an Amazon EC2 action or an Amazon EC2 Auto Scaling action, or creating an OpsItem or incident in Systems Manager.

A metric alarm has the following possible states:

* **OK:** The metric or expression is within the defined threshold.
* **ALARM:** The metric or expression is outside the defined threshold.
* **INSUFFICIENT_DATA:** The alarm has just started, the metric is not available, or not enough data is available for the metric to determine the alarm state.

#### Composite alarms

With composite alarms, you can combine multiple alarms into alarm hierarchies. This reduces alarm noise by initiating once when multiple alarms are initiated at the same time. You can use this to provide an overall state for a grouping of resources such as an application, AWS Region, or Availability Zone.

Currently, composite alarms only support the following actions:

* Notify SNS topics
* Create OpsItems in OpsCenter
* Create incidents in Incident Manager

With composite alarms, you can add logic and group alarms into a single high-level alarm, initiated when the underlying conditions are met. This means you can introduce intelligent decisions and minimize false positives.

Composite alarms are created using one or more alarm states combined with Boolean operators AND, OR, and NOT and constants TRUE and FALSE. A composite alarm is initiated when its expression evaluates to be TRUE.

### OpsCenter and CloudWatch

OpsCenter provides a central location to manage operational work items, called OpsItems, related to AWS resources. When used with Cloudwatch monitoring, you can automate and streamline security incident response processes.

This capability is unlocked when you set up OpsCenter. During this process, you can enable CloudWatch to automatically create OpsItems based on common alarms. You can create an alarm or edit an existing alarm to create OpsItems in OpsCenter.

When you configure a CloudWatch alarm to create OpsItems, CloudWatch creates a new service-linked IAM role called **AWSServiceRoleForCloudWatchAlarms_ActionSSM**. When an alarm starts, it creates an OpsItem with a title like "CloudWatch alarm - 'alarm_name' is in ALARM state".

### Using the combination of OpsCenter and CloudWatch

You could use the combination of OpsCenter and CloudWatch to gain increased observability and manageability over the security of your applications. The following are some examples of this:

* You could use OpsCenter and CloudWatch alarms to quickly identify and troubleshoot security issues with their cloud applications. Because OpsCenter integrates with CloudWatch alarms and events, you can view and manage the security alarms related to your applications. 
* You could view CloudWatch metrics and logs for application resources like EC2 instances, load balancers, and databases in the OpsCenter console. This would give you a centralized place to monitor the security of your applications.
* You could correlate CloudWatch metrics, logs, and events from various AWS services with OpsCenter to troubleshoot issues or monitor the security of your applications.

### Service quotas and CloudWatch

You can create CloudWatch alarms to notify you when you're close to a quota value threshold. Setting an alarm can help alert you if you need to request a quota increase.

Monitoring is an essential component of security operations. Monitoring AWS resources using CloudWatch alarms can alert you if a specific metric reaches a threshold that you specify. You can then specify what happens when an alarm transitions to the ALARM state from any other state. In addition to having AWS services perform an action, you could also specify that CloudWatch Events runs a custom script when an alarm transitions to the ALARM state.

## [Security Monitoring with Amazon CloudWatch Alarms](./W03Lab1.md)

## Using CloudWatch Logs

With the Amazon CloudWatch Logs service, you can collect and store logs from your resources, applications, and services in near real time. There are three main categories of logs: vended logs, logs published by AWS services, and custom logs.

### Vended logs

These are published by AWS services on your behalf. For a list of available vended logs, visit [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/) and scroll to Vended logs.

### Logs published by AWS services

Currently, more than 30 AWS services publish logs to CloudWatch. They include Amazon API Gateway, Lambda, CloudTrail, and many others.

### Custom logs

These are logs from your application and on-premises resources.

CloudWatch Logs Agents are available for Linux and Windows operating systems (within or outside AWS). CloudWatch logs can be delivered to other AWS services, such as the following:

* Export data to Amazon S3 for analytics
* Stream to Amazon OpenSearch Service or Lambda

You can use CloudWatch Logs to monitor, store, and access your log files from EC2 instances, CloudTrail, Amazon Route 53, and other sources.

With CloudWatch Logs, you can centralize the logs from all of your systems, applications, and AWS services in a single, highly scalable service. You can then easily view them, search for specific error codes or patterns, filter them based on specific fields, or archive them securely for future analysis. You can use CloudWatch Logs to see all of your logs, regardless of their source, as a single and consistent flow of events ordered by time.

CloudWatch Logs also supports querying your logs with a powerful query language, auditing and masking sensitive data in logs, and generating metrics from logs using filters or an embedded log format.

CloudWatch Logs supports two classes of log groups. Log groups in the *CloudWatch Logs Standard log* class support all CloudWatch Logs features. Log groups in the *CloudWatch Logs Infrequent Access log* class incur lower charges and support a subset of the Standard class capabilities.

The visibility, audit trails, alerts, log analysis, and data retention provided by CloudWatch Logs are all helpful for maintaining security and demonstrating compliance with regulations. They help in the following ways:

* **Logging and monitoring:** With CloudWatch logs, you can centrally collect logs and metrics from your applications, operating systems, and services. This provides visibility into user activity and system events that can help identify potential security issues or non-compliant behavior.
* **Audit trails:** The logs provide detailed audit trails that document information, such as user activity, resource access, and service changes. These audit trails can help demonstrate compliance with regulations around data access, system changes, and more.
* **Alarming:** You can set CloudWatch alarms to notify you when certain thresholds are met in your metrics. This can alert you to spikes in errors, unauthorized access attempts, or other anomalous activity that can indicate a security threat.
* **Log analysis:** CloudWatch Logs integrates with services like Athena, Lambda, and Amazon CloudSearch. You can analyze and query your log data to identify security incidents and compliance violations. This gives you the ability to perform audits and forensic analysis.
* **Data retention:** With CloudWatch Logs, you can persistently store critical log data for as long as needed to meet regulatory requirements. This provides evidence of compliance over time.
* **Encryption:** Logs can be encrypted at rest and in transit to meet security and compliance needs like HIPAA, PCI, or Federal Risk and Authorization Management Program (FedRAMP).

## Activity: CloudWatch Alarm and Logs Use Case

### Knowledge Check

#### Which statement best describes Amazon CloudWatch Logs?

* CloudWatch Logs monitors, stores, and accesses your log files from Amazon EC2 instances, AWS CloudTrail, Amazon Route 53, and other sources.

Wrong asnwers:

* CloudWatch Logs monitors a single CloudWatch metric and then sends notifications when the metric is above or below a threshold.
* CloudWatch Logs is a customizable home page in the CloudWatch console that you can use to monitor your resources in a single view.
* CloudWatch Logs continually streams CloudWatch metrics to a destination of your choice with near real-time delivery and low latency.

* CloudWatch alarms monitor a single CloudWatch metric and then send notifications when the metric is above or below a threshold.
* CloudWatch dashboards are customizable home pages in the CloudWatch console that you can use to monitor your resources in a single view.
* CloudWatch metric streams continually stream CloudWatch metrics to a destination of your choice with near real-time delivery and low latency.

#### Which use case would be best addressed by an Amazon CloudWatch alarm?

* To quickly detect high Amazon EC2 CPU utilization and notify an administration team

Wrong answers:

* To provision new AWS resources from a template
* To monitor API traffic and send notifications for unauthorized access
* To periodically create backups of AWS resources in case of system failure

* With AWS CloudFormation, new AWS resources can be provisioned from a template.
* AWS CloudTrail monitors API traffic and sends notifications for unauthorized access.
* AWS Backup periodically creates backups of AWS resources in case of system failure.

#### Which solution should an organization use to monitor multiple accounts in a single place in Amazon CloudWatch?

* Setting up a CloudWatch cross-account observability dashboard

Wrong answers:

* Setting up a CloudWatch overview dashboard
* Setting up a CloudWatch cross-service dashboard
* Setting up a CloudWatch recent alarms dashboard

### Summary

#### Metrics

Metrics represent a time-ordered set of data points published to CloudWatch. Think of metrics as variables to monitor and the data points as values of those variables over time. For example, the CPU usage of an EC2 instance is a metric. That’s what you’re being asked to create an alarm for. AWS services often provide metrics for resources at no charge. You can enable detailed monitoring for some resources for a fee, or you can publish your custom application metrics. 

Metrics can help track anomalies that might be IoCs. The following are some examples:

* Abnormal Amazon EC2 CPU utilization
* Significant or sudden increase in database reads
* HTML response rates
* Mismatch port-application traffic
* Unusual DNS requests
* Unusual outbound network traffic
* Anomalies in privileged user account activity
* Geographical irregularities (source or destination of traffic)
* Unusually high traffic at irregular hours
* Multiple, repeated, or irregular login attempts
* System average uptime

#### Namespaces

Namespaces serve as a container for metrics. Metrics within different namespaces are kept separate from each other so you don't mistakenly mix data from different applications or resources. There is no default namespace, which means you need to specify a namespace for each data point you publish to CloudWatch. Namespaces must have valid ASCII characters, be 255 characters or fewer, and contain at least one non-whitespace character. AWS namespaces typically follow a naming convention like "AWS/service," for example, "AWS/EC2" for Amazon EC2 metrics.

#### Dimensions

Dimensions help identify metrics. They are name-value pairs that are part of the identity of a metric. You can assign multiple dimensions to a metric. Each dimension represents a specific characteristic of the metric, and they help you categorize and filter metrics. For example, you can use dimensions to get statistics for a specific EC2 instance by specifying the InstanceId dimension when searching for metrics. AWS services attach dimensions to metrics they send to CloudWatch.

#### Resolution

Resolution in CloudWatch refers to how finely detailed, or granular, the metrics are. There are two types—standard and high resolution. Standard resolution metrics have a 1-minute granularity, which is suitable for most use cases. High-resolution metrics can have a 1-second granularity, which provides more immediate insights. When you publish a metric, you can choose whether to use standard or high resolution. Remember, high-resolution metrics can lead to increased costs.

#### Statistics

Statistics refer to the aggregation of metric data over specific time periods. They include information like average, minimum, maximum, sum, and percentiles. These statistics are based on the data points collected by your metrics. They are calculated within the time periods you specify. For example, the alarm you need to create is based on CPU usage.

#### Percentiles

Use percentiles to understand the distribution of metric data. For instance, the 95th percentile indicates that 95 percent of the data is lower than that value and 5 percent is higher. Percentiles are useful for spotting outliers or unusual patterns in your data. For example, monitoring the 95th percentile of CPU utilization can help identify instances with unusually heavy loads. 

#### Alarms

Alarms are used to automatically start actions based on metric values over time. You can create alarms to watch a specific metric and take action, like sending notifications to SNS topics or running scaling policies when the metric crosses a predefined threshold. Alarms are designed to react to sustained state changes, not just brief fluctuations. You set the monitoring period for an alarm, which should align with the metric's resolution. Alarms are a powerful way to automate responses to critical changes in your AWS resources.

* **Metric alarms:** These alarms watch a single CloudWatch metric or the result of a math expression based on CloudWatch metrics. A metric alarm can be set to OK, ALARM, or INSUFFICIENT_DATA.
* **Composite alarms:** With composite alarms, you can combine multiple alarms into an alarm hierarchy. This reduces alarm noise by indicating once when multiple alarms are initiated at the same time.

#### Logs

With the CloudWatch Logs service, you can collect and store logs from your resources, applications, and services in near real time. There are three main categories of logs: vended logs, logs published by AWS services, and custom logs.

#### Lab recap

In the Security Monitoring with Amazon CloudWatch Alarms lab, you performed the following tasks:

* Created an Amazon SNS notification.
* Configured a CloudWatch alarm.
* Stress tested an EC2 instance.
* Confirmed that an Amazon SNS email was sent.
* Created a CloudWatch alarm.

## CloudTrail

### Pre-assessment

#### What happens to an existing all-Regions trail if a new Region launches?

* The new Region is automatically added to the trail.

Wrong answers:

* The all-Regions trail must be deleted and recreated.
* The new Region must be manually added to the existing trail.
* A new single-Region trail must be created.

If a Region is added after a trail that applies to all Regions is created, the new Region is automatically included, and events in that Region are logged. Creating a trail in all Regions is a recommended best practice to capture activity in all Regions in an account. Because of this, an all-Regions trail is the default option when creating a trail in the AWS CloudTrail console.

#### Which AWS CloudTrail feature provides a managed data lake for capturing, storing, accessing, and analyzing user and API activity on AWS for audit and security purposes?

* AWS CloudTrail Lake

Wrong answers:

* Event history
* Trails
* Amazon CloudWatch Logs

CloudTrail Lake is a managed data lake for capturing, storing, accessing, and analyzing user and API activity on AWS for audit and security purposes.

The other options are incorrect for the following reasons:

* Event histories provide a viewable, searchable, downloadable, and immutable record of the past 90 days of management events in an AWS Region.
* Trails capture a record of AWS activities, delivering and storing these events in an Amazon S3 bucket with optional delivery to CloudWatch Logs and Amazon EventBridge.
* CloudWatch Logs are an optional delivery point for CloudTrail trails.

#### Which of these can be used to access AWS CloudTrail trails? (Select THREE.)

* AWS CloudTrail console
* AWS CloudTrail API
* AWS Command Line Interface (AWS CLI)

Wrong answers:

* Amazon CloudWatch dashboard
* Amazon EventBridge console
* AWS Step Functions console

## CloudTrail Deep Dive

### Security and compliance benefits of CloudTrail

* **Security analysis:** Perform security analysis and detect user behavior patterns by ingesting CloudTrail API call history into log management and analytics solutions, such as CloudWatch Logs, CloudWatch Events, Athena, OpenSearch Service, or another third-party solution.
* **Compliance aid:** CloudTrail facilitates compliance with internal policies and regulatory standards by providing a history of API calls in your AWS account.
* **Automated remediation:** Detect data exfiltration by collecting activity data on Amazon S3 objects through object-level API events recorded in CloudTrail. After data is collected, use other AWS services, such as EventBridge and Lambda, to initiate response procedures.

### CloudTrail destinations

* CloudTrail records API calls in your account and delivers a log file to your selected destination (S3 bucket or CloudWatch Log).
* (Optional) Receive a notification when CloudTrail publishes new log files to your S3 bucket with Amazon SNS.
* Multiple AWS Partners offer integrated solutions to analyze log files.

**CloudTrail typically delivers logs within an average of about 15 minutes of an API call. This time is not guaranteed.**

### CloudTrail events

An event in CloudTrail is the record of an activity in an AWS account. This activity can be an action taken by an IAM identity or service that is monitorable by CloudTrail. CloudTrail events provide a history of both API and non-API account activity made through the AWS Management Console, AWS SDKs, AWS CLI tools, and other AWS services.

#### Management events

Management events provide information about management operations that are performed on resources in your AWS account. These are also known as control plane operations. Example management events include the following:

* Configuring security (for example, AWS Identity and Access Management AttachRolePolicy API operations)
* Registering devices (for example, Amazon EC2 CreateDefaultVpc API operations)
* Configuring rules for routing data (for example, Amazon EC2 CreateSubnet API operations)
* Setting up logging (for example, CloudTrail CreateTrail API operations)

Management events can also include non-API events that occur in your account. For example, when a user signs in to your account, CloudTrail logs the ConsoleLogin event. For more information, see Non-API events captured by CloudTrail. 

#### Data events

Data events provide information about the resource operations performed on or in a resource. These are also known as data plane operations. Data events are often high-volume activities. The following table shows the data event types available for trails and event data stores. The resources.type column shows the resources.type value that you would specify to include data events of that type in your trail or event data store.

For trails, you can use basic or advanced event selectors to log data events for S3 buckets and bucket objects, Lambda functions, and DynamoDB tables. You can use only advanced event selectors to log the data event types shown in the remaining rows. For event data stores, you can use only advanced event selectors to include data events. Data events are not logged by default when you create a trail or event data store.

To record CloudTrail data events, you must explicitly add the supported resources or resource types for which you want to collect activity. Additional charges apply for logging data events.

#### CloudTrail Insights events

CloudTrail Insights events capture unusual API call rates or error rates in an AWS account by analyzing CloudTrail management activity. Insights events are logged when CloudTrail detects significant deviations from typical API usage or error rate patterns. Insights events provide information like the associated API, error code, timeframe, and statistics to understand the unusual activity. Insights events are disabled by default and must be explicitly enabled on a trail logging management events. Insights events incur additional charges. 

Examples of activities that might generate Insights events include:

* Your account typically logs no more than 20 Amazon S3 deleteBucket API calls per minute, but your account starts to log an average of 100 deleteBucket API calls per minute. An Insights event is logged at the start of the unusual activity, and another Insights event is logged to mark the end of the unusual activity.
* Your account typically logs 20 calls per minute to the Amazon EC2 AuthorizeSecurityGroupIngress API, but your account starts to log zero calls to AuthorizeSecurityGroupIngress. An Insights event is logged at the start of the unusual activity, and 10 minutes later, when the unusual activity ends, another Insights event is logged to mark the end of the unusual activity.
* Your account typically logs less than 1 AccessDeniedException error in 7 days on the IAM API, DeleteInstanceProfile. Your account starts to log an average of 12 AccessDeniedException errors per minute on the DeleteInstanceProfile API call. An Insights event is logged at the start of the unusual error rate activity, and another Insights event is logged to mark the end of the unusual activity.

Additional charges apply for logging CloudTrail Insights events. 

### CloudTrail event history

CloudTrail event history provides a viewable, searchable, downloadable, and immutable record of the past 90 days of CloudTrail management events in an AWS Region. You can use this history to gain visibility into actions taken in your AWS account in the AWS Management Console, AWS SDKs, AWS CLI tools, and other AWS services. You can customize your view of event history in the CloudTrail console by selecting which columns are displayed.

### Trails

A trail is a configuration that enables the delivery of CloudTrail events to an S3 bucket, CloudWatch Logs, and EventBridge. You can use a trail to filter the CloudTrail events you want to be delivered, encrypt your CloudTrail event log files with an AWS Key Management Service (AWS KMS) key, and set up Amazon SNS notifications for log file delivery. 

#### Organization trail

A trail can be configured to deliver all CloudTrail events from an organization to an S3 bucket, CloudWatch Logs, and EventBridge.

Creating an organization trail helps you define a uniform event-logging strategy for the organization. When you create an organization trail, a trail with the name that you give it will be created in every AWS account that belongs to the organization.

Users with CloudTrail permissions in member accounts can see this trail (including the trail ARN) when they log into the CloudTrail console from their AWS accounts. They can also see the trail when they run AWS CLI commands such as describe-trails (although member accounts must use the ARN for the organization trail, and not the name, when using the AWS CLI). However, users in member accounts will not have sufficient permissions to delete the organization trail, turn logging on or off, change what types of events are logged, or otherwise alter the organization trail in any way.

### Monitoring with CloudTrail

#### CloudWatch Logs

CloudTrail uses CloudTrail integration with CloudWatch Logs to send events containing API activity in your AWS account to a log group. CloudTrail events that are sent to CloudWatch Logs can activate alarms according to the metric filters you define.

You can optionally configure alarms to send notifications or make changes to the resources that you are monitoring based on log stream events that your metric filters extract. Using CloudWatch Logs, you can also track CloudTrail events alongside events from the operating system, applications, or other AWS services that are sent to CloudWatch Logs.

#### EventBridge

EventBridge is an AWS service that delivers a near real-time stream of system events that describe changes in AWS resources. You can deliver events that you are subscribed to on your trail to EventBridge. 

When you create a rule with the EventBridge console, choose either the *AWS API Call via CloudTrail* detail-type to deliver CloudTrail data and management events, or the *AWS Insight via CloudTrail detail-type* to deliver Insights events.

To record events with a detail-type value of AWS Insight via CloudTrail, you must have an active trail that is logging Insights events.

#### CloudTrail workflow

CloudTrail is turned on when you create your AWS account. When activity occurs in your AWS account, that activity is recorded in a CloudTrail event. With CloudTrail being turned on by default, you can log into CloudTrail and review your Event History. In this view, not only do you see the last 7 days of events, but you can also select a specific event to view more information about it. 

To access your CloudTrail log files directly or archive them for auditing purposes, past the 7-day window, you can create a specific trail and specify the S3 bucket for log file delivery. By creating a trail (as opposed to just viewing the default CloudTrail information), you can deliver events to CloudWatch Logs and CloudWatch Events for further action.

1. **Capture**.
Record activity in AWS services as CloudTrail events. CloudTrail captures actions made directly by a user or on behalf of a user by an AWS service.

For example, an AWS CloudFormation CreateStack call can result in additional API calls to Amazon EC2, Amazon EBS, or other services.
2. **Store**.
CloudTrail delivers events to the CloudTrail console, S3 buckets, and optionally, CloudWatch **Logs.
3. **Act**.
Use CloudWatch alarms and events to take action when important events are detected.
4. **Review**.
View recent events in the CloudTrail console or analyze log files with Athena.
5. **Support**.
Use the CloudTrail data collection to support compliance auditing, operational troubleshooting, security analysis, and automated compliance remediation.

## Working with CloudTrail Logs

### How are logs created?

CloudTrail logs record API calls made to your AWS account and writes them to log files in JSON format. The logs files are stored in an S3 bucket. To view the log files, go to the Amazon S3 console and navigate to the bucket where CloudTrail is configured to store logs. 

Locate the log files. Download a log file and open it in a text editor or JSON viewer. The file contains JSON objects for each API call. Look at the **eventVersion** field to identify the version of the log. The **eventTime** field shows when the API call occurred.

### CloudTrail log file name format

CloudTrail uses the following file name format for the log file objects that it delivers to Amazon S3 buckets:

```
AccountID_CloudTrail_RegionName_YYYYMMDDTHHmmZ_UniqueString.FileNameFormat 
```

* The **YYYY**, **MM**, **DD**, **HH**, and **mm** are the digits of the year, month, day, hour, and minute when the log file was delivered. Hours are in 24-hour format. The **Z** indicates that the time is in UTC.
* The 16-character **UniqueString** component of the log file name is there to prevent the overwriting of files. It has no meaning, and log processing software should ignore it.
* **FileNameFormat** is the encoding of the file. Currently, this is json.gz, which is a JSON text file in compressed gzip format.

**A log file delivered at a specific time can contain records written at any point before that time.**

#### Example CloudTrail log file name

```
111122223333_CloudTrail_us-east-2_20150801T0210Z_Mu0KsOhtH1ar15ZZ.json.gz
```

## [Lab: Enabling Traceability Through CloudTrail](./W03Lab2.md)

## [Lab: Monitoring and Alerting With CloudTrail and CloudWatch](./W03Lab3.md)

## Activity: CloudTrail Use Cases

### Knowledge Check

#### Which of these is an option for storing AWS CloudTrail logs?

* In Amazon S3 buckets

Wrong answers:

* In an Amazon CloudWatch dashboard
* In an Amazon RDS instance
* In an Amazon Elastic File System (Amazon EFS) store

#### Which statement best describes how AWS CloudTrail enhances an organization’s security?

* CloudTrail detects unauthorized API access attempts.

Wrong answers:

* CloudTrail performs security best practice checks, aggregates alerts, and provides automated remediation.
* CloudTrail analyzes and visualizes security data to investigate potential security issues.
* CloudTrail continually audits AWS usage to simplify risk and compliance assessment.

#### Which statement best describes the purpose of AWS CloudTrail?

* CloudTrail tracks and provides a historical record of API activity and user actions.

Wrong answers:

* CloudTrail assesses resource configurations for compliance.
* CloudTrail manages Amazon RDS instances.
* CloudTrail monitors Lambda functions.

### Summary

### CloudTrail destinations

* CloudTrail records API calls in your account and delivers a log file to your selected destination (S3 bucket or CloudWatch Log).
* (Optional) Receive a notification when CloudTrail publishes new log files to your Amazon S3 bucket with Amazon SNS.
* Multiple partners offer integrated solutions to analyze log files.

### CloudTrail events

An event in CloudTrail is the record of an activity in an AWS account. This activity can be an action taken by an IAM identity or service that is monitorable by CloudTrail. CloudTrail events provide a history of both API and non-API account activity made through the AWS Management Console, AWS SDKs, CLI tools, and other AWS services. The following are the three types of events:

* Management events provide information about management operations that are performed on resources in your AWS account. These are also known as control plane operations.
* Data events provide information about the resource operations performed on or in a resource. These are also known as data plane operations. Data events are often high-volume activities. The following table shows the data event types available for trails and event data stores. The **resources.type** column shows the **resources.type** value that you would specify to include data events of that type in your trail or event data store.
* CloudTrail Insights events capture unusual API call rates or error rates in an AWS account by analyzing CloudTrail management activity. Insights events are logged when CloudTrail detects significant deviations from typical API usage or error rate patterns. Insights events provide information like the associated API, error code, time frame, and statistics to understand the unusual activity. Insights events are disabled by default and must be explicitly enabled on a trail that is logging management events. Insights events incur additional charges. 

### CloudTrail Trails

A trail is a configuration that enables the delivery of CloudTrail events to an S3 bucket, CloudWatch Logs, and EventBridge. You can use a trail to filter the CloudTrail events you want to be delivered, encrypt your CloudTrail event log files with an AWS KMS key, and set up Amazon SNS notifications for log file delivery.

### CloudTrail log files

CloudTrail logs record API calls made to your AWS account and write them to log files in JSON format. The logs files are stored in an S3 bucket. To view the log files, go to the Amazon S3 console and navigate to the bucket where CloudTrail is configured to store logs. 

Locate the log files. Download a log file, and open it in a text editor or JSON viewer. The file contains JSON objects for each API call. Look at the eventVersion field to identify the version of the log. The eventTime field shows when the API call occurred.

### Lab recaps

#### In the Enabling Traceability Through CloudTrail lab, you performed the following tasks:

* Applied granular logging.
* Improved granular control of communication.
* Improved granular network-based controls.
* Evaluated detailed logging capabilities.

#### In the Monitoring and Alerting With CloudTrail and CloudWatch lab, you performed * the following tasks:

* Analyzed event details in the CloudTrail event history.
* Created a trail in CloudTrail with CloudWatch logging enabled.
* Created an SNS topic and an email subscription to it.
* Created CloudWatch metric filters and CloudWatch alarms.
