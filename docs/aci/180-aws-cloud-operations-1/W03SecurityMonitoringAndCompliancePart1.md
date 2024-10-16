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
