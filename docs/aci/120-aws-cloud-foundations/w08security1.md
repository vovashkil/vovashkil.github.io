###### back to AWS Cloud Institute repo's root [aci.md](../aci.md)
###### back to repo's main [README.md](../../../README.md)
# Security 1
## Using AWS to Support a Strong Security Strategy
### Pre-assessment
#### Who is responsible for ensuring that a customer's Amazon EC2 instance is properly patched?
An **AWS customer** is responsible for all the security settings in an EC2 instance because it is a service they are implementing. This includes patching and network access.

#### Which part of the Security pillar ensures that systems and services in your workload are protected against unintended and unauthorized access and potential vulnerabilities?
**Infrastructure protection.**

The other parts of the Security pillar do the following:
* **Identity and access management**: Ensures that only authorized and authenticated users can access resources.
* **Detective controls**: Ensures that there is a means to identify potential security threats or incidents.
* **Data protection**: Ensures that data is protected at rest and in transit using encryption methods.

#### Which of the seven security design principles recommends knowing which workloads are deployed and operational?
**Maintain traceability**.

The other security design principles do the following:
* **Apply security at all layers**: This refers to applying a defense-in-depth approach with other security controls, such as using strong application authentication and ensuring that users come from a trusted network path.
* **Automate security best practices**: This refers to using things like APIs and tools to ensure that routine security tasks occur on a recommended schedule and decrease the chance for human error.
* **Minimize your attack surface**: This refers to setting up a system that decreases the chances of an unprotected device or service as attacks occur.

### Shared Responsibility Model
To illustrate the shared responsibility model, let’s use an example where a company uses Amazon S3 to store data. Its AWS environment also includes EC2 instances and an Amazon Relational Database Service instance. These resources run a MySQL database, which is deployed inside a virtual private cloud. One EC2 instance hosts a web server, and the web application that runs on it uses the database to store application data.

In this example, AWS is responsible for protecting the global infrastructure, which contains the physical servers that host the virtual machines and storage hardware. These virtual machines and storage hardware host the S3 bucket, EC2 instances, and database instances. AWS is also responsible for the security of the physical networking infrastructure that ensures that these components can be accessed. 

AWS manages the security of the hypervisor layer that hosts the EC2 instances. The hypervisor is the host operating system that runs the EC2 instances, which are virtual machines running guest operating systems. You (the customer) are responsible for managing the guest OS that runs on the EC2 instances, including Microsoft Windows or Linux OS updates and security patches.

You are also responsible for managing any application software or utilities that you install. Additionally, you are responsible for the configuration of the security groups that control network access to each EC2 instance and to the RDS database instance. You are also responsible for configuring security on the S3 bucket and the objects that you store in it. For example, you could use one or more of the security features that AWS provides. By default, S3 Block Public Access is turned on, Amazon S3 access control lists, ACLs, are turned off, and AWS provides encryption at the server level.

#### Security OF the cloud
The AWS Global Infrastructure is designed and managed according to security best practices and a variety of security compliance standards. Read on for how this shows in the AWS Perimeter, Environmental, Infrastructure, and Data layers. 

#### Perimeter Layer
AWS data center physical security starts at the Perimeter Layer. 

##### Buildings
AWS data centers are housed in nondescript, undisclosed facilties. 

##### Surveillance
Professional security staff use video surveillance, intrusion detection, access log monitoring systems, and other electronic means. Entrances are secured with devices that sound alarms if a door is forced or held open.

##### Principle of least privilege
AWS limits access to preapproved areas and only provides data center access and information to employees and contractors who have a legitimate business need for such privileges.

##### Employee scrutinization
Only AWS employees who routinely need access are given permissions to relevant areas of the facility based on job function. If an employee doesn’t have an ongoing business need to be at a data center, they must go through the visitor process. They must have an escort assigned throughout the duration of their visit.

#### AWS carefully chooses its data center locations to mitigate environmental risks, such as flooding, extreme weather, and seismic activity. AWS takes the following into consideration:
* Customers who require high availability and performance can deploy their applications across multiple Availability Zones in the same AWS Region for fault tolerance and low latency. 
* To mitigate and prepare for the unexpected, AWS tests its business continuity plan regularly with drills that simulate different scenarios. 
* Companies generally use 77 percent fewer servers and 84 percent less power in the AWS Cloud compared to their own traditional data centers. They also tap into a 28-percent cleaner mix of solar and wind power.

#### Infrastructure Layer
Components such as backup power equipment, the heating, ventilation, and air conditioning (HVAC) system, and fire suppression equipment are all part of the Infrastructure Layer. They help protect servers and, ultimately, your data. 

##### Fire detection
Automatic fire detection and suppression equipment reduces the risk of fire-related accidents. Smoke detection sensors are in all data center environments, mechanical and electrical spaces, chiller rooms, and generator equipment rooms.

##### Monitoring
AWS monitors electrical, mechanical, and life support systems. Preventive maintenance is performed regularly. 

##### Climate control
Climate control is used to maintain a constant operating temperature for servers and other hardware. This prevents overheating and reduces the possibility of service outages.

##### Power
Electrical systems are fully redundant and maintainable without impact to operations. Uninterruptible power supply units provide backup power for critical and essential loads, and generators provide backup power for the entire facility.

#### Data Layer
Even though protecting your data is ultimately your responsibility in the cloud, AWS takes extra precautions to protect the media that your data lives on. AWS takes the following into consideration: 
* Storage devices are decommissioned by using National Institute of Standards and Technology Special Publication 800-88 (NIST 800-88) techniques to destroy customer data. NIST 800-88 is a government document providing guidance about how to erase data on storage media, also called media sanitization.
* AWS is audited by external auditors who inspect our data centers and confirm that we follow established rules to obtain our security certifications.
* AWS servers can notify employees of any attempts to remove data. In the unlikely event of a breach, the server is automatically deactivated.

### IT Controls
The shared responsibility model extends to IT controls. IT controls provide ways to configure and design resources or systems to **mitigate** or **address** specific issues. Just as the responsibility to operate the IT environment is shared between AWS and a customer, so is the management, operation, and verification of IT controls.

#### Inherited IT controls
These are controls that customers inherit fully from AWS. The customer does not need to take any action on them. These IT controls are physical and environmental. Some examples are as follows:
* Maintaining the physical security of data centers
* Selecting data center locations to mitigate the impact of flooding
* Providing data centers with redundant networking and power

#### Shared IT controls
With shared IT controls, AWS provides the requirements for the infrastructure, and the customer provides the requirements for their implementation of a service. Some examples are as follows:
* **Patch management**: AWS is responsible for patching the infrastructure, but customers are responsible for patching guest OSs and applications.
* **Awareness and training**: AWS trains AWS employees, but the customer must train their own employees.

#### Customer IT controls
These are controls the customer must take action on with the application they are deploying in an AWS service. Some examples are as follows:
* **Service and communications protection**: This might require a customer to set up their service in a specific way to reduce vulnerabilities or set up access control lists (ACLs) to secure their data.
* **Zone security**: This might require a customer to route or zone their data within specific security environments.

### AWS Security Pillar
#### AWS Well-Architected Framework
The AWS Well-Architected Framework shows the pros and cons of different decisions while building systems on AWS. By using the Well-Architected Framework, you will learn architectural best practices for designing and operating reliable, secure, efficient, and cost-effective systems in the cloud. The Well-Architected Framework provides a way for you to consistently measure your architectures against best practices and identify areas for improvement. AWS believes having well-architected systems greatly increases the likelihood of business success.

The Well-Architected Framework is based on six pillars.

##### Operational excellence
The operational excellence pillar focuses on running and monitoring systems to deliver business value and continually improving processes and procedures.

##### Security
The security pillar focuses on protecting information and systems. 

##### Reliability
The reliability pillar focuses on the ability to prevent and quickly recover from failures to meet business and customer demand.

##### Performance efficiency
The performance efficiency pillar focuses on using IT and computing resources efficiently.

##### Cost optimization
The cost optimization pillar focuses on avoiding unneeded costs.

##### Sustainability
The sustainability pillar is based on recommendations and strategies to use when designing cloud architectures that maximize efficiency and reduce waste.

### Security pillar
The security pillar signifies the ability to protect information, systems, and assets while delivering business value through risk assessments and mitigation strategies. The security pillar is made up of five different areas for security in the cloud. All AWS security services can be categorized by these five areas. 

#### Identity and access management
Identity and access management are key parts of a security program. They ensure that only authorized and authenticated users can access your resources and that these users do so only in a manner that you intend.

#### Detective controls
You can use detective controls to identify a potential security threat or incident. Detective controls are an essential part of governance frameworks and can be used to support threat identification and response efforts. 

#### Infrastructure protection
Infrastructure protection ensures that systems and services within your workload are protected against unintended and unauthorized access and potential vulnerabilities.

#### Data protection
Data protection means protecting data at rest and in transit by way of encryption methods and access control and also classifying data based on levels of sensitivity.

#### Incident response
Even with extremely mature preventive and detective controls, your organization should still put processes in place to respond to and mitigate the potential impact of security incidents.

### Seven Security Design Principles
The security pillar includes the ability to protect data, systems, and assets to take advantage of cloud technologies to improve the security of AWS accounts. Included in the pillar is an overview of design principles, best practices, and questions. 

#### Implement a strong identity foundation
An organizational security culture should be built on the principles of least privilege and strong authentication. Grant access to data and other resources to only the people who really need that access. You can start by denying access to everything and granting access as needed based on job roles. Enforcing a separation of duties with appropriate authorization for each interaction with your AWS resources is a security best practice.

#### Maintain traceability
With AWS, you can monitor, alert, and audit actions and changes to your environment in real time. AWS provides native logging and services that you can use to provide greater visibility in near real time for occurrences in your environment. By knowing which workloads are deployed and operational, you can audit and ensure that an environment is operating at standard security governance levels.

#### Apply security at all layers
Instead of focusing on the protection of a single outer layer, apply a defense-in-depth approach with other security controls. This approach means applying security to all layers, such as your network, application, and data store. For example, you might have strong authentication requirements for applications. In addition, ensure that users come from a trusted network path and require access to the decryption keys to process encrypted data.

#### Automate security best practices
AWS offers purpose-built security tools that automate many of the routine tasks security experts normally spend time on. Security engineering and operations functions can be automated using a comprehensive set of APIs and tools. Using popular software development methods that you already have in place, you can fully automate and deliver identity management, network and data security, and monitoring capabilities.

#### Protect data in transit and at rest
Safeguarding data is a critical part of building and operating information systems. AWS provides services and features that give you several options to protect your data at rest and in transit. These options include fine-grained access controls to objects and creating and controlling the encryption keys used to encrypt your data. They also include selecting appropriate encryption methods, validating integrity, and appropriately retaining data. Creating mechanisms to protect data in transit, such as using virtual private network (VPN) and TLS connections, is also a security best practice.

#### Minimize your attack surface
Generally, a cyberattack ends for one of two reasons: the attackers exhaust themselves and give up, or the attackers achieve their goal. Be ready to scale and absorb the attack and minimize or remove the possibility of an unprotected device. With these techniques, you can also absorb larger volumes of application layer attacks.

#### Prepare for security events
Even with mature preventive and detective controls, you should still put processes in place to respond to and mitigate the potential impact of security incidents. Put tools and access to services in place ahead of a security incident. Then, routinely practice incident response through game days. This helps you ensure that your architecture can accommodate timely investigation and recovery. In AWS, there are several different approaches to consider when addressing incident response. 

### Knowledge Check
#### Who is responsible for securing the backup power for an AWS data center?
**AWS is responsible for all the operations of its data centers.**

#### Which part of the security pillar ensures that only authorized and authenticated users can access resources and that these users do so only in the intended manner?
**Identity and access management**.

Other parts of the security pillar do the following:
* **Detective controls**: Ensure that there is a means to identify potential security threats or incidents.
* **Data protection**: Ensures that data is protected at rest and in transit using encryption methods. 
* **Infrastructure protection**: Ensures that systems and services in your workload are protected against unintended and unauthorized access and potential vulnerabilities.

#### Which of the seven security design principles recommends using a comprehensive set of APIs and tools?
**Automate security best practices**.

The other design principles include the following details:
* **Apply security at all layers**: This refers to applying a defense-in-depth approach with other security controls, such as using strong application authentication and ensuring that users come from a trusted network path.
* **Using traceability**: This refers to setting up monitoring, alerting, and auditing actions so you are aware of changes in an AWS environment.
* **Minimize your attack surface**: This refers to setting up a system that decreases the risk of an unprotected device or service if an attack occurs.

### Summary
* AWS operates, manages, and controls security of the cloud.
* The customer is responsible for the management of what they put in the cloud.
* This separation of control extends to IT controls. However, there are some controls that both AWS and the customer are responsible for in different contexts. For example, AWS is responsible for patching infrastructure, and the customer is responsible for patching instances.

#### Securing the cloud at several layers

##### Perimeter Layer
The Perimeter Layer is where physical security starts. It encompasses implementing proper surveillance, enacting the principle of least privilege, and examining if employees need access to a location persistently or only temporarily as a guest.

##### Environmental Layer
AWS carefully chooses their data center locations to mitigate environmental risks, such as flooding, extreme weather, and seismic activity. 

##### Infrastructure Layer
The Infrastructure Layer includes things like backup power equipment, HVAC systems, and fire suppression equipment that helps protect servers that hold customer data.

##### Data Layer
AWS decommissions media storage devices according to NIST 800-88 standards. It has third-party audits to inspect its data centers for compliance and deactivates servers automatically in the very unlikely event that they are removed from their location.

#### Security pillar
One of the six pillars of the Well-Architected Framework is security. The security pillar includes the following areas:
* Identity and access management
* Detective controls
* Infrastructure protection
* Data protection
* Incident response

#### Seven security design principles
Within the security pillar is a set of seven design principles that help customers protect their data, systems, and assets. Those principles are as follows:
1. Implement a strong identity foundation
2. Enable traceability
3. Apply security at all layers
4. Automate security best practices
5. Protect data in transit and at rest
6. Minimize your attack surface
7. Prepare for security events

## Implementing a Strong Identity Foundation
### Pre-assessment
#### Which AWS service provides single sign-on to AWS accounts?
**AWS IAM Identity Center (successor to AWS Single Sign-On)**

* IAM provides a method for applying fine-grained access to AWS.
* Amazon Cognito provides access to web and mobile applications.
* AWS RAM makes possible the secure sharing of resources in an AWS account with all the roles and users in that same account, or with other AWS accounts.

#### Which AWS Identity and Access Management (IAM) feature would you use to delegate temporary security credentials to services?
**Roles**.

* Access control lists provide the ability to manage access to buckets and objects. 
* An IAM group is a group of IAM users that share common characteristics and to which specific permissions are applied.
* A security group acts as a virtual firewall for your EC2 instances to control incoming and outgoing traffic.

#### Where does an AWS Identity and Access Management (IAM) credential in Amazon Cognito obtain its privileges from?
**The IAM role that it is mapped to**.

### Revisiting Authentication and Authorization
Identity and access management are key parts of an information security program. They ensure that only authorized and authenticated users are able to access your resources and that they do so only in a manner that you intend. By using identity and access management, you define who has access to which resources and outline what can be done to those resources. In this section, you will learn about a few of the AWS services that deal with identity and access management.

#### AUTHENTICATION
* Who is requesting access to the AWS account and the resources in it?
* It’s important to establish the identity of the requester through credentials.
* The requester could be a person or an application; IAM calls them principals.

#### AUTHORIZATION
* After the requester has been authenticated, what should they be allowed to do?
* IAM checks for policies that are relevant to the request to determine whether to allow or deny the request.

### Authentication and authorization recap
To understand the fundamental aspects of authentication and authorization, think about online banking.

Imagine that you are a customer for a bank that allows you to access your account information online, and you need to pay a bill. Should any customer with that bank be able to log in to their system and access your account? Of course not.

Before the bank allows you to access your account, the bank must ensure that the person who is accessing the account is you. The bank wants to authenticate that you are who you claim to be. At the most basic level, this usually involves requiring a username and a password known only to you.

Now that you are authenticated into your account, you want to pay a bill. Can you pay your bill using the money in some other customer's account? No. You only have the ability to access your own accounts. This is authorization.

### Federating Users in AWS
Identity federation is a system of trust between two parties for the purpose of authenticating users and conveying information needed to authorize their access to resources. In this system, an identity provider (IdP) is responsible for user authentication, and a service provider, such as a service or an application, controls access to resources. 

#### Trust
A trust relationship is configured between the IdP and the service provider. The service provider trusts the IdP to authenticate users and relies on the information provided by the IdP about the users.

#### Identity provider
After authenticating a user, the IdP returns a message, called an assertion. The assertion contains the user's sign-in name and other attributes that the service provider needs to establish a session with the user and to determine the scope of resource access.

#### Service provider
The service provider receives the assertion from the user, validates the level of access requested, and sends the user the necessary credentials to access the desired resources.

#### Access granted
With the right credentials from the service provider, the user now has direct access to the requested resources through an established session.

AWS offers different solutions for federating employees, contractors, and partners (workforce) to AWS accounts and business applications. AWS has similar solutions for adding federation support to customer-facing web and mobile applications. AWS supports commonly used open identity standards, including SAML 2.0, OpenID Connect (OIDC), and OAuth 2.0.

### Identity federation use cases:
#### Fine-grained access to AWS
AWS Identity and Access Management

#### Single sign-on to AWS accounts and centrally managed access to resources
AWS IAM Identity Center

#### Access to web and mobile applications
Amazon Cognito

### AWS Identity and Access Management
"IAM is like a command center that can control the what and the who in your account." Marcio Morales - Senior AWS Solutions Architect

#### Ways to access an IAM account
##### USERNAME AND PASSWORD
A password policy is a set of rules that define the type of password that an IAM user can set. You should define a password policy for all of your IAM users to enforce strong passwords and regular changing of passwords. Password requirements are similar to those found in most secure online environments. 

##### MULTI-FACTOR AUTHENTICATION
Multi-factor authentication (MFA) is an additional layer of security for accessing AWS services. With this authentication method, more than one authentication factor is checked before access is granted. This consists of a username and password and the single-use code from the MFA device. AWS Command Line Interface (AWS CLI) also supports MFA. 

##### USER ACCESS KEYS
Users need their own access keys to make programmatic calls to AWS using the AWS CLI, the AWS SDKs, or direct HTTPS calls using the APIs for individual AWS services. Access keys are used to digitally sign API calls made to AWS services. Each access key credential is composed of an access key ID and a secret key. Each user can have two active access keys, which is useful when you need to rotate the user's access keys or revoke permissions. 

**Protecting account access is the bedrock of a strong security system. This starts with activating MFA on root user accounts as you did when you created your AWS account.**

#### Users and groups
The careful management of access credentials is the foundation of how resources in the cloud are secured. Every interaction you make with AWS is authenticated. When you open an AWS account, the identity that you begin with has access to all AWS services and resources in that account. You use this identity to establish less-privileged users and role-based access in IAM. IAM is a centralized mechanism for creating and managing individual users and their permissions with your AWS account.

An IAM group is a collection of users. With groups, you can specify permissions for similar types of users. For example, if you have a group named Developers, you can give that group the types of permissions that developers typically need. This can be considered a form of role-based access control. Create groups that reflect organization roles, not action commonality.

**Create IAM groups that reflect organization positions, not technical commonality. AWS provides a list of permissions(opens in a new tab) based on certain organization roles.**

#### Roles
You can use IAM roles to delegate access to users, applications, or services that normally don't have access to your organization's AWS resources. You can assume a role to obtain temporary security credentials that you can use to make AWS API calls. Consequently, you don't have to share long-term credentials or define permissions for each entity that requires access to a resource. When you assume a role, it's like putting on a different hat. Each role comes with specific access permissions, and by assuming each role, you take on the access permissions of that role.

##### Role use cases
###### Amazon EC2 access to resources
If an application running on an Amazon Elastic Compute Cloud (Amazon EC2) instance needs access to AWS resources, it can be provided a role that will temporarily grant access and permissions on that resource.

###### AWS services making calls on your behalf
If there is an AWS service that needs to call other services on your behalf or create and manage resources in your account, it can be provided a role that grants similar permissions as your AWS user account to that resource.

#### IAM Roles Anywhere
**IAM Roles Anywhere** provides a secure way for workloads such as servers, containers, and applications that run outside of AWS to obtain temporary AWS credentials. The workloads can use the same IAM policies and roles that exist for native AWS applications to access AWS resources. Using IAM Roles Anywhere eliminates the need to manage long-term credentials for workloads running outside of AWS.

#### Featured use case

#### [IAM Access Analyzer](https://aws.amazon.com/blogs/security/iam-access-analyzer-makes-it-simpler-to-author-and-validate-role-trust-policies/) 
This IAM resource provides many tools to help set, verify, and refine permissions. One part—policy validation—helps to author secure and functional policies that grant the intended permissions. Read this use case to learn about authoring a role trust policy. 

### AWS IAM Identity Center for User Federation
So far, you have seen how IAM can help federate users from one organization into AWS accounts and applications. In addition to authenticating users and resources, organizations also need to manage these accounts. With AWS IAM Identity Center (successor to AWS Single Sign-On), you can centrally manage federated access to multiple AWS accounts and business applications. And you can provide users with single sign-on access to all their assigned accounts and applications from one place.

IAM Identity Center can be used for identities in the Identity Center directory, an existing Microsoft Active Directory (see glossary), or an external IdP. IAM Identity Center provides the following benefits:
* It has built-in integration with business cloud applications, such as Salesforce, Box, GitHub, and Office 365.
* It has a built-in directory for user and group management. It can serve as an IdP to authenticate users to applications compatible with IAM Identity Center, the AWS Management Console, and SAML 2.0-compatible cloud-based applications.
* It integrates with AWS services, such as AWS Organizations.
* You can log the AWS CloudTrail service in with all sign-in and administrative activities for auditing. You can send its logs to security information and event management (SIEM) solutions (see glossary) such as Sumo Logic to analyze them.
* It has the AWS access portal for users to sign in with their existing corporate credentials and access all of their assigned accounts and applications from one place.
* You can use AWS CLI v2 to access AWS resources through IAM Identity Center. This has the benefit of providing short-term credentials to your users to more safely access your resources.

#### Glossary
##### Microsoft Active Directory
Microsoft Active Directory centralizes the storage of information about objects on a network for convenient access. A common use case is centralizing email addresses that live on an email server.

##### Security information and event management solutions
SIEM solutions are tools that provide an overview of an organization's information security status. These tools provide functions such as real-time visibility into information security systems and event log management and consolidation.

#### Getting started with IAM Identity Center
##### Activate IAM Identity Center
When you open the IAM Identity Center console for the first time, you are prompted to activate IAM Identity Center before you can start managing it. After it's activated, IAM Identity Center is granted the necessary permissions to create IAM service-linked roles in any of the AWS accounts within your AWS organization. IAM Identity Center creates these roles later during the process of setting up single sign-on (SSO) access to your AWS accounts. 

##### Connect to your identities
The next step is to choose a directory, which determines where IAM Identity Center looks for users and groups that need access. By default, you get an IAM Identity Center user directory for quick and convenient user management.

Optionally, you can also connect to your on-premises Active Directory or a SAML 2.0 IdP. 

##### Grant access
Then you can grant users in your directory access to one or more AWS consoles for specific AWS accounts in your AWS organization. Access can also be granted to AWS and SAML applications.

##### Grant access in the IAM Identity Center user portal
Then users see only the AWS account icon (for example, Development) that they've been assigned from within their user portal. When they choose the icon, they can then choose which IAM role they want to use when signing in to the AWS Management Console for that AWS account.

#### AWS access through permission sets
An IAM Identity Center permission set is a collection of administrator-defined policies that IAM Identity Center uses to determine a user's effective permissions to access a given AWS account. Permission sets can contain either AWS managed policies or custom policies. Permission sets are provisioned to the AWS account as IAM roles and are presented to users as such. You can assign more than one permission set to a user. Users who have multiple permission sets must choose one of the roles when they sign in to the AWS access portal.

##### Diagram explanation
Diagram showing two permission sets: set 1 with only AWS managed policies and set 2 with AWS managed and custom policies. They feed into IAM Identity Center and then user A pulling permission set 1 and user B being able to see both but only use one at a time.

It is important to note that permission sets are used only for AWS accounts. Permission sets are not used to manage access to cloud applications. Permission sets ultimately get created as IAM roles in a given AWS account, and trust policies allow users to assume the role through IAM Identity Center.

### Mobile and Web Application Authentication with Amazon Cognito
With Amazon Cognito, you can add user sign-up, sign-in, and access controls to your web and mobile applications. You can define roles and map users to different roles so your application can access only the resources that are authorized for each user. User sign-in can be done either by a third-party identity provider or directly through Amazon Cognito.

1. First, a user authenticates against a user pool on Amazon Cognito, which assigns tokens to the user.
2. Next, the user exchanges those tokens for temporary IAM credentials from the identity pool. These credentials' privileges are based on the IAM role that is mapped to the group that the user belongs to.
3. Finally, the user accesses AWS services and resources, like an Amazon DynamoDB table, with credentials that they received. 

Enterprise identity providers and social sign-in providers, such as Facebook, Google, and Amazon, return the tokens through SAML 2.0. An Amazon Cognito user pool is a user directory that manages the overhead of handling these tokens. After a successful user pool sign-in, your web or mobile application will receive user pool tokens from Amazon Cognito. These tokens can then be used to retrieve AWS credentials through Amazon Cognito identity pools. These credentials allow your application to access other AWS services and you don’t have to embed long-term AWS credentials in your application.

#### Featured use case

##### [Configuring Duo multi-factor authentication](https://aws.amazon.com/blogs/security/how-to-configure-duo-multi-factor-authentication-with-amazon-cognito/)

Read this use case to see how one MFA tool, Duo, can be integrated into mobile and web application authentication workflows. 

### Additional AWS Services for Identity and Access Management
The following AWS services can also be used to protect credentials, supply user federation, and centrally manage and secure multiple AWS accounts.

#### AWS Directory Service
AWS Directory Service is a managed service offering that provides directories that contain information about your organization, including users, groups, computers, and other resources. As a managed offering, AWS Directory Service is designed to reduce management tasks, thereby allowing you to focus more of your time and resources on your business.

#### AWS Resource Access Manager
AWS Resource Access Manager (AWS RAM) permits the secure sharing of resources in an AWS account with all the roles and users in that same account, or with other AWS accounts.

Using AWS RAM, you can centrally manage resources like the following: 

* Private certificate authorities*
* Amazon EC2 instances
* Licensing codes 

*A certificate authority or certification authority is something that stores, signs, and issues digital certificates that validate the ownership of a public key by the named subject of the certificate.

### IAM Policies
Policies grant permissions to actions and resources for authenticated entities.

At its heart, a policy is a JSON document that uses the IAM policy grammar(opens in a new tab). When you attach a policy to an IAM entity, such as a user, group, or role, the policy grants permissions to that entity.

When IAM access control policies are created or edited using the AWS Management Console, AWS automatically examines them to ensure that they comply with the IAM policy grammar. If AWS determines that a policy is not in compliance with the grammar, it prompts you to fix the policy.

#### IAM request context
To talk about IAM policies, you first need to understand the three main pieces of logic that define what is in the policy and how the policy works. These pieces make up the request context that is authenticated by IAM and authorized accordingly. You can think of these items as the subject, verb, and object of a sentence.

##### Principal
**Subject**

User, role, external user, or application that sent the request, and the policies associated with that principal

##### Action
**Verb**

What the principal is attempting to do

##### Resource
**Object**

AWS resource object upon which the actions or operations are performed

#### Identity-based policies
You manage access in AWS by creating policies and attaching them to IAM identities or AWS resources. An identity-based policy is an object in AWS that when associated with an IAM identity, defines its permissions. In identity-based policies, the principal is what the policy is applied to, so there is no principal field. Principals only exist in resource-based policies where the policy is attached to the resource and specifies the principals that it applies to.

AWS evaluates these policies when a principal entity (IAM user or role) makes a request. Permissions in the policies determine whether the request is allowed or denied. Most policies are stored in AWS as JSON documents.

There are three types of identity-based policies. 

##### AWS managed
AWS managed policies are managed and created by AWS. They can be attached to multiple users, groups, and roles.

##### Customer managed
Customer managed policies in their AWS account can provide more precise control than AWS managed policies. They can be attached to multiple users, groups, and roles.

##### Inline
Inline policies are embedded directly into a user, group, or role and are generally **not recommended by AWS**. These are useful if you want to maintain a strict 1:1 relationship between a policy and the principal.

**If you are new to using policies, AWS recommends that you start by using AWS managed policies.**

#### IAM policy example
The following is a simple example of an IAM identity-based policy granting access to an Amazon Simple Storage Service (Amazon S3) bucket.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ListObjectsInBucket",
            "Effect": "Allow",
            "Action": "s3:ListBucket",
            "Resource": [
                "arn:aws:s3:::myBucket"
            ]
        },
        {
            "Sid": "AllObjectsActions",
            "Effect": "Allow",
            "Action": "s3:*Object",
            "Resource": [
                "arn:aws:s3:::myBucket/*"
            ]
        }
    ]
}
```

##### Statement
The Statement element is the main element for a policy. It can contain a single statement or an array of individual statements. Each individual statement block must be enclosed in curly braces { }.

##### Statement ID (Sid)
The Sid element is optional and provides a brief description of the policy statement.

There are two Sids for this code: ListObjectsInBucket and AllObjectsActions.

##### Effect
The Effect element specifies whether the statement will explicitly allow or deny access.

There are two Effects for this code. The first, for the Sid ListObjectsInBucket, is Allow. The second, for the Sid AllOjectsActions is Allow.

##### Action
The Action element describes the type of action or actions that should be allowed or denied. 

There are two Actions in this code. For the Sid ListObjectsInBucket, the Action is s3:ListBucket. The Action for the Sid AllowObjectsActions has an asterisk, which is a wildcard. This means that any Amazon S3 action ending in Object will be allowed. Some examples include GetObject and PutObject.

##### Resource
The Resource element specifies the object or objects that the policy statement covers. 

There are two Resources for this code. For the Sid ListObjectsInBucket, it is arn:aws:s3:::mybucket. For the Sid AllObjectsActions, it is arn:aws:s3:::myBucket/*.

#### Granting policies
In IAM, access is denied unless expressly granted with a policy. To use a policy to control access in AWS, you must first understand how IAM grants access. When you use the AWS API, the AWS CLI, or the AWS Management Console to take an action, such as creating a role or activating an IAM user access key, you send a request for that action.

1. IAM checks that the user (the principal) is authenticated into the system. 
2. Then IAM confirms that the user is authorized by checking all the policies attached to your user. 
3. During authorization, IAM verifies that the requested actions are allowed by the policies.
4. IAM also checks any policies attached to the resource that the user is trying to access.

These policies are known as the **resource-based policies**. If the identity-based policy allows a certain action but the resource-based policy does not, the result will be a deny. AWS authorizes the request only **if each part of your request is allowed by the policies**.

By default, all requests are denied. An explicit allow overrides this default, and an explicit deny overrides any allows. After your request has been authenticated and authorized, AWS approves the actions in your request. Then those actions can be performed on the related resources within your account.

### Policy conditions
IAM allows you to add conditions to your policy statements. The condition element is optional and lets you specify conditions for when a policy is in effect. In the condition element, you build expressions in which you use condition operators (equal, less than, and so on) to match the condition keys and values in the policy against keys and values in the request.

```
"Condition" : { "{condition-operator}" : { "{condition-key}" : "{condition-value}" }}
```

For example, the following condition can be added to an Amazon S3 bucket policy to further restrict access to the bucket. In this case, the condition includes the StringEquals operator to ensure that only requests made by JohnDoe will be allowed.

```
"Condition" : { "StringEquals" : { "aws:username" : "JohnDoe" }}
```

Here's another example. This example uses the IpAddress condition operator and the aws:SourceIP condition key. In this scenario, the request must come from the IP range 203.0.113.0 to 203.0.113.255 so that the desired action to be allowed.

```
"Condition": {"IpAddress": {"aws:SourceIp": "203.0.113.0/24"}}
```

There are various different condition keys available, depending on your use case. You can have multiple conditions in a single policy, which are evaluated using a logical AND. An upcoming section will cover them in more detail.

A complete list of available condition operators can be found on the [IAM JSON Policy Elements: Condition Operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html) page.

#### Principle of least privilege
Security is the practice of protecting your intellectual property from unauthorized access, use, or modification. One of the most important aspects of information security within an organization is confidentiality. Confidentiality refers to limiting information access and disclosure to authorized users and preventing access by unauthorized people. An organizational security culture should be built on the principle of least privilege and strong authentication.

##### Grant access as needed.
Grant access to data and resources only to the people who truly need it.

##### Establish separation of duties.
Use appropriate authorization for each interaction that a user will have with data or resources. You can do this by defining the actions that can be taken on specific resources under specific conditions.

##### Avoid long-term credentials.
Using temporary credentials that are acquired dynamically will decrease the chance of a malicious attack.

It’s more secure to start with a minimum set of permissions and grant additional permissions as needed. To define the correct set of permissions, you must do some research to determine what access is needed to accomplish a specific task. You will need to find out things like the following:
* Who or what specifically should be allowed to perform an action?
* How often should they or it be able to perform this action?

For example, perhaps developers should be allowed to create EC2 instances in production environments but not stop or delete the instances. Instead of granting all permissions related to the lifecycle of instance creation, it is best practice to only grant creation permissions.

### Policy Evaluation Overview
AWS evaluates policies when an IAM principal (user or role) makes a request, regardless of if it is from the AWS Management Console, the AWS CLI, or the AWS API.

#### Identity-based policies
Identity-based policies are managed or inline policies attached to IAM identities (users, groups to which users belong, or roles). They control what actions an identity can perform, on which resources, and under what conditions.

#### Resource-based policies
These are inline policies that are attached to AWS resources. The most common examples of resource-based policies are S3 bucket policies and IAM role trust policies. Resource-based policies grant permissions to the principal that is specified in the policy. So the principal policy element is required. 

Resource-based policies grant permission to principals or accounts (same or different accounts).
The following resource-based policy is attached to an S3 bucket. According to the policy, only the IAM user carlossalzar can access this bucket.

```
{
       "Version" : "2012-10-17"
       "Statement" : [
           {
               "Effect":  "Allow",
               "Action":  "s3:*",
               "Principal":  {  "AWS" :    "arn:aws:iam::111122223333:user/carlossalazar" },
               "Resource":  "*"
               }
       ]
}
```

#### Permissions boundaries
A permissions boundary sets the maximum permissions that an identity-based policy can grant to an IAM entity. The entity can perform only the actions that are allowed by both its identity-based policies and its permissions boundaries. Resource-based policies that specify the user or role as the principal are not limited by the permissions boundary.

* Permission boundary policies restrict permissions for the IAM entity attached to it.

Consider the following example. Assume that one of your IAM users should be allowed to manage only Amazon S3, Amazon CloudWatch, and Amazon EC2. To enforce this rule, you can use the customer-managed policy enclosed in the square to set the permissions boundary for the user. Then add the condition block below to the IAM user's policy. The user can never perform operations in any other service, including IAM, even if it has a permissions policy that allows it.

```
{
       "Version": "2012-10-17",
       "Statement":  [
               {
                       "Effect" : "Allow",
                       "Action": [
                               "s3:*",
                               "cloudwatch:*",
                               "ec2:*"
                       ],
                       "Resource":   "*"
               }  ]        }

"Condition":  {StringEquals" :  {"iam:PermissionsBoundary":
                                    "arn:awsLiam::123456789012:policy/<policyname>"}}
```

#### AWS Organizations service control policies
AWS Organizations is a service for grouping and centrally managing AWS accounts. If you activate all features in an organization, you can apply service control policies (SCPs) to any or all of your accounts. SCPs specify the maximum permissions for an account, or a group of accounts, called an organizational unit (OU).

These policies restrict permissions for entities in an AWS account, including AWS account root users.
The following diagram illustrates the following:

An organizational root AWS management account
Three parent organizational units (OUs), each containing additional child OUs or AWS accounts
Two of the parent OUs with organization-level boundaries restricting permissions for those entire OU child objects
Flow diagram of restricting access using AWS Organizations service control policies.

#### Access control lists
Use access control lists (ACLs) to control which principals in other accounts can access the resource to which the ACL is attached. ACLs are supported by Amazon S3 buckets and objects. They are similar to resource-based policies although they are the only policy type that does not use the JSON policy document structure. ACLs are cross-account permissions policies that grant permissions to the specified principal. ACLs cannot grant permissions to entities within the same account.

**This is not a recommended control.**

#### Session policies
A session policy is an inline permissions policy that users pass in the session when they assume the role. The permissions for a session are the intersection of the identity-based policies for the IAM entity (user or role) used to create the session and the session policies. Permissions can also come from a resource-based policy. Session policies limit the permissions that the role or user's identity-based policies grant to the session. 

* Session policies restrict permissions for assumed roles and federated users.

### Guardrails and grants
Some policies are used as guardrails to restrict permissions, and others are used to grant permissions. Using a combination of different policy types not only improves your overall security posture but also minimizes the impact of an incident if one happens.

#### Guardrail policies
* SCPs
* Permissions boundaries
* Session policies

#### Grant policies
* Identity-based policies
* Resource-based policies
* ACLs

### Explicit and implicit denies
A request results in an explicit deny if an applicable policy includes a Deny statement. An implicit denial occurs when there is no applicable Deny statement but also no applicable Allow statement. Because an IAM user, role, or federated user is denied access by default, they must be explicitly allowed to perform an action. Otherwise, they are implicitly denied access.

**If policies that apply to a request include an Allow statement and a Deny statement, the Deny statement wins over the Allow statement. The request is explicitly denied.**

### Lab
#### EC2-Admin-Policy
```
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Action": [
				"ec2:Describe*",
				"ec2:StartInstances",
				"ec2:StopInstances",
				"cloudwatch:DescribeAlarms"
			],
			"Resource": [
				"*"
			],
			"Effect": "Allow"
		}
	]
}
```

#### AmazonEC2ReadOnlyAccess
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "ec2:Describe*",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "elasticloadbalancing:Describe*",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "cloudwatch:ListMetrics",
                "cloudwatch:GetMetricStatistics",
                "cloudwatch:Describe*"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "autoscaling:Describe*",
            "Resource": "*"
        }
    ]
}
```

#### AmazonS3ReadOnlyAccess 
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:Get*",
                "s3:List*",
                "s3:Describe*",
                "s3-object-lambda:Get*",
                "s3-object-lambda:List*"
            ],
            "Resource": "*"
        }
    ]
}
```

### Knowledge Check
#### Which AWS service provides fine-grained access control?
**AWS Identity and Access Management (IAM)**

* IAM Identity Center provides single sign-on to AWS accounts.
* Amazon Cognito provides access to web and mobile applications.
* AWS RAM makes possible the secure sharing of resources in an AWS account with all the roles and users in that same account, or with other AWS accounts.

#### Which AWS Identity and Access Management (IAM) feature would you use to specify permissions for similar types of users?
**IAM groups.**

* You can use access control lists to manage access to buckets and objects.
* With roles, you can delegate temporary security credentials to users and resources.
* Security groups act as a virtual firewall for your Amazon EC2 instances to control incoming and outgoing traffic.

#### What can a single AWS IAM Identity Center permission set contain?
**Both AWS managed and customer managed policies.**

### Summary
#### Authentication and authorization
Authentication is concerned with who or what is requesting access to an AWS account and its associated resources.

After authentication, authorization is concerned with what can be performed in the AWS account and its associated resources.

#### Identity federation
AWS offers three services for identity federation:
* IAM for fine-grained access control
* IAM Identity Center for single sign-on capabilities for AWS accounts and centrally managed resources
* Amazon Cognito for access to web and mobile applications

#### IAM functionality
IAM accounts can be accessed three ways: 
* with a username and password, 
* with multi-factor authentication, 
* and with user access keys. 

Within an IAM account, there are the following:
* Groups, which allow you to specify permissions for similar types of users and then group them together
* Roles, which are a temporary way to assign users, applications, or services that normally don't have access to your organization's AWS resources.

### Additional Resources
#### [AWS and SAML](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-console-saml.html)
SAML 2.0 is an open federation standard that allows an identity provider (IdP) to authenticate users and pass identity and security information about them to a service provider (SP), typically an application or service. F

#### [AWS and OIDC](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html)
With OpenID Connect (OIDC) 1.0, clients can validate and obtain basic information about the identity of users based on authentication performed by an authorization server.

#### [AWS and OAuth 2.0](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-controlling-access-to-apis-oauth2-authorizer.html)
OAuth 2.0 focuses is an industry-standard authorization protocol that provides authorization for things like web and desktop applications, mobile devices, and IoT devices. For more information on how AWS ues this protocol, choose the OAUTH 2.0 button.

#### [AWS and Microsoft Active Directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html)
AWS Directory Service for Microsoft Active Directory, also referred to as AWS Managed Microsoft AD, is powered by Windows Server 2019. It helps manage and organize network permissions and resources from a central location.

## Maintaining Traceability in AWS
### Pre-assessment
#### A customer wants to run automated security checks to ensure that their environment is aligned with industry benchmarks. Which AWS service should they use?
**AWS Security Hub**.

The other services do the following:
* **Amazon Detective:** Analyzes and visualizes security data to investigate potential security issues.
* **Amazon GuardDuty:** Protects AWS accounts with intelligent threat detection.
* **Amazon Inspector:** Automates vulnerability management and continuously scans AWS workloads for software vulnerabilities and unintended network exposure.

#### A customer wants to monitor their multi-Region environment for threats using Amazon GuardDuty. How do they set up this service?
**They need to set it up for every Region they are in.**

Amazon GuardDuty is a regionally based threat detection managed service.

#### Which AWS service does Amazon Macie scan for personally identifiable information?
**Amazon S3.**

Amazon Macie only scans Amazon S3 buckets and their objects.

### Understanding Monitoring
Monitoring is the act of collecting, correlating, aggregating, and analyzing the transmission of data in an environment's network, infrastructure, and applications. The goal is to detect, investigate, and remediate problems as quickly as possible. 

AWS identifies threats by continuously monitoring the network activity and account behavior in your cloud environment. With detective controls, you can maintain the security of your cloud environment. You can use detective controls to identify a potential security threat or incident. Detective controls are also important as a part of legal or compliance obligations and as part of a governance framework. In this section, you will learn about AWS services used in monitoring. 

### Monitoring for security
The shared responsibility model requires you to monitor and manage your environment at the OS and higher layers. You probably already do this on premises or in other environments, so you can adapt your existing processes, tools, and methodologies for use in the cloud. Security monitoring starts by answering the following questions: 
* What are the key performance indicators? 
* How should you measure them? 
* What are the thresholds for these metrics? 
* What is the escalation process?

### AWS services for detective controls
AWS provides a suite of services that will monitor and combat threats through: 
* Unified security and compliance
* Managed threat detection
* Application security analysis
* The ability to investigate potential security issues

The subtopics in this section will cover the following services so you can understand their purpose and how they integrate into the larger AWS ecosphere:
* Amazon CloudWatch
* AWS Security Hub
* Amazon GuardDuty
* Amazon Inspector
* Amazon Macie
* AWS CloudTrail

### Monitoring Your Network with CloudWatch
#### Monitoring your AWS resources
Imagine you are a network engineer, and your organization is migrating to AWS. You are tasked with configuring the hybrid network between your organization's on-premises location and AWS. To do this, you need to add the new requirements to your current on-premises network design. You also need to ensure that the hybrid network is optimized and that all configurations are correct. Part of ensuring that your changes are optimized is to define in your design how to monitor the performance of the new components and services.

One of the core AWS services you can use is Amazon CloudWatch.

#### CloudWatch metrics
Metrics are snapshots of a point in time for your resources and applications. By collecting metrics over a period of time, you can create filters that show trends in performance and establish a baseline. You can also configure alarms that are activated when a metric crosses an established threshold to help troubleshoot. 

Metrics provide data in one of the following two ways:
* They indicate a point within a range (for example, percentage of total capacity).
* They provide a quantitative measurement, such as total packet-per-second (PPS).

The CloudWatch home page automatically displays metrics about most AWS services you use. You can use it to do the following:
* Gain system-wide visibility using custom dashboards to display metrics of your choice about your network performance, resource utilization, application performance, and operational health
* Create alarms that monitor metrics and send notifications. Alarms can also be configured to automatically make changes to the resources you are monitoring when a threshold is breached. For example, using CloudWatch alarms, you can monitor the NetworkPacketsIn and NetworkPacketsOut for an EC2 t3.micro instance with a network capacity up to 5 Gbps. Then, use this data to determine whether to launch a larger instance size, or additional instances, to handle increased load.

**Tracking and monitoring your metrics aids both operational excellence and cost optimization. You can react to data, not just aggregate it. For example, you can use the data to stop underused instances to save money.**

#### CloudWatch features
##### Diagram explanation
This diagram shows an Amazon cloud with the following:
* One region containing Amazon CloudWatch 
* A data center with EC2 instances that have Amazon CloudWatch agents installed on them

##### Metrics
The first part of CloudWatch is metrics. You can collect metrics, monitor metrics, and perform actions based on metrics. Metrics are a collection of data points that indicate the state of AWS resources, applications, and on-premises resources over a period of time. You can use metrics to configure alarms, observe performance trends, and identify network changes. CloudWatch automatically collects metrics in a time-ordered structure related to AWS services, products, and applications you consume. 

##### CloudWatch Logs
The second part of CloudWatch is Amazon CloudWatch Logs. It helps centrally collect, monitor, and create actions based on vended logs, AWS service logs, and custom logs data. Through CloudWatch Logs, you can ingest logs from AWS services, such as CloudTrail or VPC Flow Logs. Using the CloudWatch agent, you can ingest logs from systems outside AWS. You can supply your own logs or custom application and system metrics, such as memory usage, transaction volumes, or error rates, for CloudWatch to monitor.

##### EventBridge
The third part of CloudWatch is Amazon EventBridge. You can create an event, which will perform an action when that event occurs. Events can be based on a service, schedule, or alarm. 

CloudWatch is designed to collect data from AWS services, ingest that data, and manage that data as metrics. Through alarms, you can use the data to take actions, such as sending notifications or scaling up your compute environment when your load increases.

##### Alarms
CloudWatch can alert in real time using CloudWatch alarms to initiate notifications and actions from any metric logged.

Each part of CloudWatch, including metrics, logs, and events, can be filtered to create a CloudWatch alarm. Depending on how you create the alarm, you can then take an action based on that alarm.

##### CloudWatch agent
Some CloudWatch metrics are not collected by default. The CloudWatch agent must be installed on Amazon EC2 instances and on-premises servers.

#### Monitoring plan
Using CloudWatch to collect monitoring data can help resolve failures. Not all data might be useful. In fact, CloudWatch collects so much data that it can be overwhelming. It can be helpful to take the time to understand which information you need to meet your monitoring goals and requirements. Before you start configuring CloudWatch, consider creating a monitoring plan.

#### Monitoring plan preparation
Ask the following questions:
* What are your goals for monitoring?
* Which resources will you monitor?
* How often will you monitor these resources?
* Which monitoring tools will you use?
* Who will perform the monitoring tasks?
* Who should be notified when something goes wrong?

#### The steps needed for monitoring
##### Step 1: Create a monitoring plan and goals
The first step is to establish a monitoring plan to track your goals. Ask the following questions:
* What is your account strategy? 
* What is your end goal?

The next step is to determine which metrics need monitoring.

##### Step 2: Define metrics
After you establish your monitoring goals and plan to measure the success of meeting those goals, the next step is to decide which metrics to monitor. Ask the following questions:
* Which resources will you monitor?
* Which metrics can track the progress of your goals?

The next step is to establish a baseline for the defined metrics.

##### Step 3: Establish a baseline
After you define the metrics to monitor and establish a baseline for the defined metrics, ask yourself the following question:
* How often will you monitor these resources?

For example, establish a baseline for normal network performance in your environment. Follow these steps:
1. Identify and analyze the traffic traversing your network to understand optimized patterns and trends.
2. Measure the overall network usage and performance at various times and under different changes in traffic. Monitor top protocols, traffic components, packets sizes, and so on.
3. Use network performance baselines for comparison to identify changes in traffic that might indicate a drift from the normal performance patterns and identify performance anomalies. 

Setting a network baseline also provides early indicators that application and network demands are pushing near the available capacity. When performance falls outside your established baseline, a CloudWatch alarm can alert you to the drift. Then, devise a plan of action and methods to address the alerts.

Next, after defining metrics to monitor and establishing the baseline, ask the following questions:
* Which monitoring tools will you use?
* Who will perform the monitoring tasks?
* Who should be notified when something goes wrong?

##### Step4: Monitor using CloudWatch
You can use CloudWatch to collect and process raw data into readable, near real-time metrics. For example, CloudWatch can help do the following:
* It can monitor the physical AWS Direct Connect connections and virtual interfaces. For more information, see [What is AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html).
* It can monitor AWS Transit Gateway Network Manager to centrally manage your networks that are built around transit gateways. For more information, see [AWS Transit Gateway Network Manager](https://aws.amazon.com/transit-gateway/network-manager/).

CloudWatch data is retained for a 15 month period. With access to historical metric data, you gain a better perspective on how your network, application, or service is performing over time.

Amazon VPC publishes data points to CloudWatch in your global network for the following:
* Registered transited gateways (BytesIn, BytesOut, PacketsIn, PacketsOut)
* Associated Site-to-Site VPN connections (TunnelDataIn, TunnelDataOut, TunnelState) 
* VPC peering connections (awsRegion, vpcPeeringConnectionId, accepterVPCInfo, requesterVPCInfo)
* On-premises resources (BytesIn, BytesOut, VPCTunnelDown). 
* VPC Flow Logs metrics (For more information, see [Publish flow logs to CloudWatch Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-cwl.html).)

Again, you can set alarms that watch for certain thresholds in your environment and send notifications or take actions when those thresholds are met. Remember to configure alerts and alarms in CloudWatch and ask the following question:
* Who should be notified when something goes wrong?

##### Step 5: Use alarms and notifications
Using CloudWatch, you can programmatically create custom automation based on events and schedules. 

For example, being proactive by building automation to handle abuse events and taking the initial steps to minimize the events' impact to your network is best practice. Ask the following question:
* Who should be notified when something goes wrong?

CloudWatch events can be configured to call an Amazon SNS topic that runs one or more Lambda functions when one or more metrics cross their set threshold. This improves time to resolution and helps gain efficiencies.

#### CloudWatch metrics boundaries
Some CloudWatch metrics are not collected by default. The full range of CloudWatch metrics requires extra configuration and authorization because of the AWS shared responsibility model. Here, CloudWatch metrics need a CloudWatch agent installed to collect metrics for your Amazon EC2 instances and your on-premises servers. 

With the unified CloudWatch agent, you can collect internal system-level metrics and logs from Amazon EC2 instances and on-premises servers. You can store and view the metrics collected by the CloudWatch agent with any other CloudWatch metrics.  

Amazon EC2 defines network maximums at the instance level to ensure a high-quality networking experience, including consistent network performance across instance sizes. 

##### Bandwidth capability
Each EC2 instance has a maximum bandwidth for aggregate inbound and outbound traffic, based on instance type and size. Some instances use a network I/O credit mechanism to allocate network bandwidth based on average bandwidth usage. Amazon EC2 also has maximum bandwidth for traffic to Direct Connect and the internet.

##### Packet-per-second (PPS) performance
Each EC2 instance has a maximum PPS performance based on instance type and size.

##### Connections tracking
The security group tracks each connection established to ensure that return packets are delivered as expected. There is a maximum number of connections that can be tracked per instance.

##### Link-local service access
Amazon EC2 provides a maximum PPS per network interface for traffic to services such as the following:
* Domain Name System (DNS) service
* Instance metadata service (IMDS)
* Amazon Time Sync Service

When the PPS for an instance exceeds its maximum, AWS queues the extra packets for delivery at a later time. If the queue reaches its capacity, packets might be dropped. To minimize the risk of losing packets and data, monitoring when network traffic exceeds the service maximums is important. Establishing CloudWatch alarms to activate when network performance metrics near their maximum will inform you, in real time, about possible network performance issues.

### Monitoring for Compliance and Best Practices with Security Hub
AWS Security Hub provides customers with a comprehensive view of their security state within AWS and their compliance with security standards and best practices. Security Hub centralizes and prioritizes security findings from across AWS accounts, services, and supported third-party partners. It helps customers analyze their security trends and identify the highest priority security issues. 

Security Hub continuously aggregates data from the following:
* Amazon GuardDuty
* Amazon Inspector
* AWS Systems Manager
* AWS Health
* AWS Config
* AWS Firewall Manager
* AWS Identity and Access Managment Access Analyzer
* Amazon Macie
* Integrated AWS Partner Network (APN) solutions

Security Hub also conducts automated security checks and then makes it possible to investigate findings and respond to and remediate problems.

### Monitoring for Threats with GuardDuty
Amazon GuardDuty is a **regional-based** threat detection **managed service** that continuously monitors AWS environments for known and unknown threats. It uses multiple techniques, such as machine learning (ML), anomaly detection, and integrated threat intelligence to identify indicators of compromise. After it's implemented, GuardDuty immediately starts analyzing account and network activity. Threat intelligence is pre-integrated into the service and is continuously updated and maintained.

GuardDuty continuously monitors the following for compromise, anomalous behavior, and malware:
* Amazon Simple Storage Service (Amazon S3)
* Container workloads
* Instance workloads
* Accounts and users

### Monitoring EC2 Instances with Amazon Inspector
Amazon Inspector is an automated security assessment service that helps you test the network accessibility of your Amazon EC2 instances. It also helps you test the security state of your applications running on the instances. Instances with unnecessary access points increase an environment's attack surface.

Amazon Inspector uses automated workflows to continuously scan and assess applications for vulnerabilities or deviations from best practices. All findings are aggregated in the Amazon Inspector console, routed to Security Hub, and pushed through EventBridge to automate workflows, such as ticketing.  

After it is implemented, Amazon Inspector provides automated workload discovery and continual scanning. Findings are compared to a maintained vulnerability database to provide near real-time results that are contextualized. Then, they are fed back into Amazon Inspector or the following services for ticketing and remediation:
* Security Hub
* EventBridge
* Amazon Elastic Container Registry (Amazon ECR)
* AWS Partner services

### Monitoring for Sensitive Data with Macie
Macie is a security service that uses machine learning to automatically discover, classify, and protect sensitive data in AWS. Macie recognizes sensitive data, such as personally identifiable information (PII) or intellectual property. It provides you with dashboards and alerts that give visibility into how this data is being accessed or moved.

Macie is a fully managed service that continuously monitors data access activity for anomalies. It generates detailed alerts when it detects the risk of unauthorized access or inadvertent data leaks. Macie is available to protect data stored in Amazon S3.

### Auditing and Reporting with CloudTrail
#### Using CloudTrail for audits
The cash register, one of the world's first self-auditing devices. The principle is simple: trust but verify. You have your entire store being run by a clerk that you trust, but you want to make sure that the cash in the drawer matches the actual sales. So, every transaction then is recorded and tabulated, so, at the end of the day, you know exactly what should be there. 

Being able to audit transactions in IT is a critical element in most compliance structures. But in a physical data center, there are so many places where a human can, even by accident, make changes without any record of that change getting recorded. At AWS, that problem goes away because everything is programmatic. 

Introducing AWS CloudTrail, the comprehensive API auditing tool. The engine is simple, every request made to AWS, it doesn't matter if it's to launch an EC2 instance or add a row to a DynamoDB table or change a user's permissions. Every request gets logged in the CloudTrail engine. The engine records exactly who made the request, which operator, when did they send the API call? Where were they? What was their IP address? And what was the response? Did something change? And what is the new state? Was the request denied?

From an auditing perspective, well, this is fabulous. So, imagine that you're dealing with an auditor who is checking to make sure that nobody from the outside can access your database. That's a good thing. Well, okay, you build a security group that locks out external traffic. But remember that a root-level administrator still has permissions to change those settings, right? 

Well, so how do you prove to the auditor that the security group settings never changed? The answer is CloudTrail. And then CloudTrail can save those logs indefinitely in secure S3 buckets. In addition, with tamper-proof methods like Vault Lock, you then can show absolute provenance of all of these critical security audit logs.

#### Keeping records with CloudTrail
CloudTrail is turned on by default on an AWS account and records API calls for that account. The recorded information includes the identity of the API caller, the time of the API call, the source IP address of the API caller, and more. You can think of CloudTrail as a trail of breadcrumbs (or a log of actions) that someone has left behind them.

Recall that you can use API calls to provision, manage, and configure AWS resources. With CloudTrail, you can view a complete history of user activity and API calls for your applications and resources. 

Events are typically updated in CloudTrail within 15 minutes after an API call. You can filter events by specifying the time and date that an API call occurred. You can also filter by the user who requested the action, the type of resource that was involved in the API call, and more.

#### Example: CloudTrail log file
##### Who made the request?
The following log file example shows that an AWS Identity and Access Management (IAM) user named Alice performed some kind of action. 

```
{
       "Records":{[
                "eventVersion": "1.0",
                "userIdentity" : {
                            "type": "IAMUser",
                            "principalID": "EX_PRINCIPAL_ID",
                            "arn": "arn:aws:iam: :123456789012:user/Alice",
                            "acountID": "123456789012",
                            "accessKeyID": "EXAMPLE_KEY_ID",
                            "userName": "Alice"
             },
```

i##### When did Alice perform the action and from where?
The next part of the code verifies the following information:
* Date the request was made: 2018-03-06 (March 6, 2018)
* Event that happened: Instances stopped
* AWS Region where the event happened: us-west-2
* Source IP address from where the request was made: 205.251.233.176
* Method used to make the request: ec2 api

```
"eventTime":  "2018-03-06T21:0159z: ,
                "eventSource":  "ec2.amazonaws.com"
                "eventName":  "StopInstances"
                "awsRegion":  "us-west-2"
                "sourceIPAddress":  "205.251.233.176"
                "userAgent":  "ec2-api-tools 1.6.12.2"
```

##### What happened?
The next part of the code shows which resource was affected. An EC2 instance with the ID "i-ebeaf9e2" was the resource in this request. The previous and current state of the instance indicate that instance was successfully stopped.

```
"requestParamaters": {
                "instancesSet":{
                         "items:" [{
                                     "instanceID": "i-ebeaf9e2"
               }]
          },
         "force": false
      },
"responseElements": {
                "instancesSet":{
                         "items:" [{
                                     "instanceID": "i-ebeaf9e2"
                                    "currentState": {
                                              "code": 64,
                                              "name": "stopping" },
                                    "previousState": {
                                              "code": 16,
                                              "name": "running" },
          }]
      },
```

#### Activating CloudTrail Insights
In CloudTrail, you can also turn on AWS CloudTrail Insights. With this optional feature, you can use CloudTrail to automatically detect unusual API activities in your AWS account. 

For example, CloudTrail Insights might detect that a higher number of EC2 instances than usual have recently launched in an account. You can then review the full event details to determine which actions you need to take next.

### Knowledge Check
#### A customer wants to analyze and investigate potential security threats in the AWS Management Console. Which service should they use?
**Amazon Detective.**

The other options do the following:
* **Amazon GuardDuty**: Protects AWS accounts with intelligent threat detection.
* **Amazon Inspector**: Automates vulnerability management and continuously scans AWS workloads for software vulnerabilities and unintended network exposure.
* **AWS Security Hub**: Runs automated security checks to ensure that their environment is aligned with industry benchmarks.

#### Which service should a customer use to test the network accessibility of Amazon EC2 instances?
**Amazon Inspector**: Automates vulnerability management and continuously scans AWS workloads for software vulnerabilities and unintended network exposure.

The other options do the following:
* **Amazon Detective**: Analyzes and visualizes security data to investigate potential security issues.
* **AWS Security Hub**: Analyzes and investigates potential security threats in the AWS Management Console.
* **Amazon GuardDuty** is a regional-based threat detection managed service.

#### Which AWS service should be used in conjunction with Amazon Inspector to assess multiple accounts?
**AWS Organizations.**

The other options do the following:
* **AWS Control Tower**: Orchestrates multiple AWS services while maintaining the security and compliance needs. 
* **AWS CloudTrail**: Monitors and records account activity across AWS infrastructure.
* **AWS Systems Manager**: Secures end-to-end management of resources on AWS, on premises, and on other clouds.

### Summary
Monitoring is the act of collecting, correlating, aggregating, and analyzing the transmission of data in an environment's network, infrastructure, and applications. The goal is to detect, investigate, and remediate problems as quickly as possible.

#### Security Hub
Security Hub provides customers with a comprehensive view of their security state in AWS and their compliance with security standards and best practices. Security Hub centralizes and prioritizes security findings from across AWS accounts, services, and supported third-party partners. It helps customers analyze their security trends and identify the highest-priority security issues.

#### Amazon GuardDuty
Amazon GuardDuty is a regional-based threat detection managed service that continuously monitors AWS environments for known and unknown threats. It uses multiple techniques, such as machine learning, anomaly detection, and integrated threat intelligence to identify indicators of compromise. After it's turned on, it immediately starts analyzing account and network activity. Threat intelligence is pre-integrated into the service and is continuously updated and maintained.

#### Amazon Inspector
Amazon Inspector is an automated security assessment service that tests the network accessibility of EC2 instances and deviations from best practices.  It also tests the security state of its  applications. Unnecessary access points increase an environment's attack surface. All findings are aggregated in the Amazon Inspector console, routed to Security Hub, and pushed through EventBridge to automate workflows, such as ticketing.  

#### Macie
Macie is a fully managed security service that uses machine learning to automatically discover, classify, and protect sensitive AWS data in S3 buckets. It recognizes looks for data such as personally identifiable information or intellectual property. Then makes dashboards and alerts showing how the data is accessed or moved. It monitors data access activity for anomalies.

## Applying Security at All Layers
### Pre-assessment
#### Which infrastructure layer serves as the space where information is stored and managed?
**Data tier** is where information is stored and managed.

* **Presentation tier** is where end users interact with an application.
* **Application tier** acts as the intermediary between the presentation tier and the data tier.
* **The session tier** provides the mechanism for opening, closing and managing a session between end-user application processes.

#### Which networking feature can be used to group instances based on security and operational needs?
**Subnet routing** groups instances and AWS resources based on security and operational needs. 

* **Security groups** act as a virtual firewall for to control inbound and outbound traffic.
* **Network access control lists** are an optional layer of security that control traffic at the subnet level.
* **Computer firewalls** control inbound and outbound traffic locally on a computer based on organizational and security settings.

#### Which AWS Shield Advanced integration provides 24/7 access to the Shield Response Team?
When combined with AWS Shield Advanced, **AWS WAF** provides 24/7 access to the AWS Shield Response Team.

* When combined with AWS Shield Advanced, **AWS Firewall Manager** provides cost protection against distributed denial of service (DDoS)-related spikes in protected resources.
* AWS Global Accelerator and ELB are protected resources.

### Understanding the Layers
This topic will cover the infrastructure layer, which should primarily live in the data and application tiers. The application layer is generally protected through the following:
* A strong identity foundation, such as password policies and using the principle of least privilege
* Good architecture best practices, such as using a design like the three-tier architecture design, which separates the end user from the data

#### Presentation tier
This tier is where the end user interacts, generally using a graphic user interface. This tier, often called the frontend, is often developed using a combination of HTTP, JavaScript, and CSS for web applications. Desktop applications can be written in many languages.

#### Application tier
This tier, also called the logic tier, is the heart of an application. It acts as the intermediary between the presentation tier—what the end user sees—and the data tier, where information is processed. 

The application tier is generally built using developer languages such as Python.

#### Data tier
This tier, often called the backend, is where information is stored and managed. This is where services such as Amazon Aurora and Amazon DynamonDB are implemented.

### Secure Services at the Infrastructure Layer
#### Protection through isolation: Amazon Virtual Private Cloud (Amazon VPC)
Infrastructure protection ensures that systems and resources within your workloads are protected against unintended and unauthorized access and other potential vulnerabilities. By using Amazon Virtual Private Cloud (Amazon VPC), you can isolate your AWS resources in the cloud. With a virtual private cloud (VPC), you can launch resources into a virtual network that you've defined and that closely resembles a traditional network that you would operate in your own data center.

Here we have the most common VPC features that provide a defense-in-depth approach for your resources. 

##### Subnet routing
You can use subnets to group instances and AWS resources based on your security and operational needs. You can have all instances launched in a subnet receive a public IPv4 address, an IPv6 address, or both. With a subnet, you can also configure routing for your network. With routing, you can specify targets for your resources and whether they can be reached through the internet.

##### Network access control lists
To further add a layer of security within your VPC, you can configure network access control lists (ACLs). A network ACL is an optional layer of security for your VPC that acts as a firewall for controlling traffic at the subnet level. Your VPC automatically comes with a modifiable default network ACL. By default, it allows all inbound and outbound IP traffic. To control traffic, you need to add ALLOW and DENY rules for specific IP addresses, protocols, and ports.

##### Security groups
These act as a virtual firewall for to control inbound and outbound traffic. When you launch an instance in a VPC, there must be a a security group. One set of rules that controls inbound traffic to it, and a separate set of rules that controls outbound traffic. Security groups are stateful (see glossary). No inbound traffic is allowed until you configure inbound rules to your desired security group. Traffic can be restricted by IP protocol, service port, and source and destination IP addresses.

* **Stateful**. Stateful refers to the ability to remember specific details of a user, such as its profile, preferences, and actions. 

#### Application and OS security: AWS Systems Manager
Securing your network and making sure that all your servers are hardened and properly patched are some of the tasks required in infrastructure security. AWS Systems Manager includes capabilities that help you automate management tasks such as the following:
* Collecting system inventory
* Applying operating system patches
* Maintaining up-to-date antivirus definitions
* Configuring operating systems and applications at scale

Systems Manager helps keep your systems compliant with your defined configuration policies.

##### Systems Manager features
##### Automation
Safely automate common and repetitive IT operations and management tasks across AWS resources.

##### Inventory
Collect information such as applications, files, and updates about your instances and the software installed on them. 

##### Patch Manager
Deploy software patches automatically across large groups of Amazon Elastic Compute Cloud (Amazon EC2) or on-premises instances.

##### Paramater Store
This is a centralized store to manage your configuration data, whether plaintext data such as database strings or secrets such as passwords. 

##### Run Command
Manage instances remotely at scale without logging in to automate common administrative tasks across groups of instances.

##### State Manager
Manage Windows and Linux EC2 instances with a browser-based interactive shell or CLI, without the need for things such as SSH key management.

**AWS Systems Manager provides a tool to help with automating operations with things like patch deployment, deploying automation scripts to your instances, and a lot more. Doing these sorts of tasks manually, one instance at a time, is like inviting the elusive creatures that cause you to get paged at 3 AM directly into your metaphorical server room. Through the use of Systems Manager, you can push patches and scripts to be run on an instance, or group of instances, in an automated fashion to avoid logging directly into a production box to make those changes.** – Morgan Willis, Senior AWS Technical Trainer

### Centralizing Security Management with AWS Firewall Manager
AWS Firewall Manager is a security management tool that facilitates configuring your AWS WAF rules across your accounts. With Firewall Manager, security administrators of large organizations can write company-wide rules from one place and enforce them across applications protected by AWS WAF. They can get central visibility of attacks against their Application Load Balancers and Amazon CloudFront infrastructure.

With AWS Firewall Manager, customers can apply a single set of rules to multiple accounts, centralize compliance tracking and reporting for those accounts, and push findings to AWS Security Hub. Firewall Manager is compatible with the following:
* AWS WAF
* AWS Network Firewall
* AWS Shield
* Amazon Route 53 Resolver DNS Firewall
* Security groups
* Third-party firewalls§

### Filtering Traffic with AWS WAF
AWS WAF helps protect your web applications from common web exploits that could affect application availability, compromise security, or consume excessive resources. AWS WAF gives you control over which traffic to allow or block by defining customizable web security rules. 

AWS WAF protects web applications from common exploits and can be applied to the following:
* Amazon CloudFront
* Application Load Balancers
* Amazon API Gateway
* AWS AppSync

AWS WAF rules block and filter traffic. They are created by AWS, AWS Marketplace sellers, and customers. Amazon CloudWatch can be used in conjunction with AWS WAF to compile metrics. Firewall Manager can manage multiple AWS WAF deployments.

#### [Anomaly detection with AWS WAF](https://aws.amazon.com/blogs/security/how-to-improve-visibility-into-aws-waf-with-anomaly-detection/)
Using Amazon Lookout for Metrics and AWS WAF to automatically detect anomalies. Lookout for Metrics uses machine learning (ML) to detect and diagnose anomalies within business and operational data. 

### Protecting Against DDoS Attacks with AWS Shield
AWS Shield is a managed distributed denial of service (DDoS) protection service that safeguards applications running on AWS. A DDoS attack is an attack in which multiple compromised systems attempt to flood a target, such as a network or web application, with traffic. A DDoS attack can prevent legitimate users from accessing a service and can cause the system to crash due to the overwhelming traffic volume.

AWS provides two levels of protection against DDoS attacks: 
* AWS Shield Standard is active by default.
* AWS Shield Advanced is a subscription-based service. It provides tailored protection such as custom mitigations, insights, and 24/7 access to the AWS Shield Response Team for more advanced DDoS attacks.

### Knowledge Check
#### Which networking feature acts as a virtual firewall for instances in Amazon VPC, controlling their inbound and outbound traffic?
**Security groups**.

#### A customer wants to deploy multiple AWS WAF deployments for their web applications. Which AWS offering should they use in conjunction with AWS WAF?
**AWS Firewall Manager**.

* AWS AppSync helps customers develop applications faster with serverless GraphQL and Pub/Sub APIs.
* Amazon CloudFront distributes static and dynamic content quickly and reliably at high speeds.
* Application Load Balancer distributes incoming application traffic to multiple targets.

#### Which AWS service helps protect applications running on AWS from distributed denial of service (DDoS) attacks?
**AWS Shield**.

* AWS Systems Manager provides secure end-to-end management for resources on AWS, on premises, and on other clouds.
* Amazon VPC provides full control over a virtual networking environment, including resource placement, connectivity, and security. 
* AWS WAF protects applications and APIs against bots and exploits that consume resources, skew metrics, or cause downtime.

### Summary
Security should be applied at all layers. There are three layers within a three-tier architecture:
* The data tier is often called the backend. It is where data is stored, processed, and managed using services like Amazon Aurora and Amazon DynamoDB.
* The application tier is often called the logic tier. It is built using languages like Python. This tier acts as the intermediary between the backend and the frontend.
* The presentation tier is often called the frontend. This is the graphical user interface that end users interact with. It is often created using a combination of HTTP, JavaScript, and CSS for web applications.

#### AWS services
The following AWS services that help establish security at the infrastructure layer.

| Service | Amazon Virtual Private Cloud (Amazon VPC) | AWS WAF | AWS Shield | AWS Firewall Manager |
| ------- | ----------------------------------------- | ------- | ---------- | -------------------- |
| Purpose | Protect resources from unauthorized and unintended access by isolating cloud resources using feature such as security groups, subnets, and ACLs. | Protect web applications from common web exploits that could affect application availability, compromise security, or consume excessive resources.  | Create safeguards to protect resources against DDoS attacks. | Centralize management of firewall rules, making it possible to create company-wide rules from one place and enforce across applications. |

## Automating Security Best Practices
### Pre-assessment
#### Which of the following options is an example of an AWS Trusted Advisor security check?
**Exposed access keys**. 

The other options do the following:
* **Amazon EBS overprovisioned volumes** is a *cost optimization check*.
* **DynamoDB write capacity** is a *service limits check*.
* **VPN tunnel redundancy** is a *fault tolerance check*.

#### Which feature or service would a developer use to review information about their responsibility for complying with regulatory standards?
**AWS Artifact Reports**.

The other options do the following:
* **Audit Manager**: Maps compliance requirements to AWS usage data with prebuilt and custom frameworks and automated evidence collection. 
* **CloudTrail**: Monitors and records account activity across AWS infrastructure. 
* **Signer**: Validates code against a digital signature to confirm the code is unaltered and from a trusted publisher.

#### Which feature or service can automatically detect unusual API activities?
**AWS CloudTrail Insights**.

The other options do the following:
* **AWS Artifact Agreements**: Contains different types of agreements to address the needs of customers who are subject to specific regulations, such as the Health Insurance Portability and Accountability Act (HIPAA).
* **Audit Manager**: Maps compliance requirements to AWS usage data with prebuilt and custom frameworks and automated evidence collection. 
* **Identity and Access Management Access Analyzer**: Helps streamline permissions management throughout each step of the cycle.

### Automating Security Evaluations with AWS Trusted Advisor
AWS Trusted Advisor can help improve the security of an AWS environment by suggesting foundational security best practices curated by security experts. Examples include identifying Amazon Relational Database Service (Amazon RDS) security group access risk, exposed access keys, and unnecessary Amazon Simple Storage Service (Amazon S3) bucket permissions.

Trusted Advisor scans customer AWS infrastructure and compares it to AWS best practices in five categories, including security. It then recommends actions.

#### [Trused Advisor security check](https://docs.aws.amazon.com/awssupport/latest/user/security-checks.html)

### Automating Compliance with AWS Artifact and AWS Config
For every industry, there are specific standards that need to be upheld, and you will be audited or inspected to ensure that you have met those standards. For example, for a coffee shop, the health inspector will come by and check that everything is up to code and sanitary. Similarly, you could be audited for taxes to see that you have run the back office correctly and have followed the law. You rely on documentation, records and inspections to pass audits and compliance checks as they come along. 

You will need to devise a similar way to meet compliance and auditing in AWS. Depending on what types of solutions you host on AWS, you will need to ensure that you are up to compliance for whatever standards and regulations your business is specifically held to. If you run software that deals with consumer data in the EU, you would need to make sure that you're in compliance with GDPR, or if you run healthcare applications in the US, you will need to design your architectures to meet HIPAA compliance requirements. 

Whatever your compliance need is, you will need some tools to be able to collect documents, records and inspect your AWS environment to check if you meet the compliance regulations that you're under. The first thing to note is, AWS has already built out data center infrastructure and networking following industry best practices for security, and as an AWS customer, you inherit all the best practices of AWS policies, architecture, and operational processes. 

AWS complies with a long list of assurance programs that you can find online. This means that segments of your compliance have already been completed, and you can focus on meeting compliance within your own architectures that you build on top of AWS. The next thing to know in regard to compliance and AWS, is that the Region you choose to operate out of, might help you meet compliance regulations. If you can only legally store data in the country that the data is from, you can choose a Region that makes sense for you and AWS will not automatically replicate data across Regions. 

You also should be very aware of the fact that you own your data in AWS. As shown in the AWS shared responsibility model, you have complete control over the data that you store in AWS. You can employ multiple different encryption mechanisms to keep your data safe, and that varies from service to service. So, if you need specific standards for data storage, you can devise a way to either reach those requirements by building it yourself on top of AWS or using the features that already exist in many services. For a lot of services, enabling data protection is a configuration setting on the resource. 

AWS also offers multiple whitepapers and documents that you can download and use for compliance reports. Since you aren't running the data center yourself, you can essentially request that AWS provides you with documentation proving that they are following best practices for security and compliance. 

One place you can access these documents is through a service called AWS Artifact. With AWS Artifact, you can gain access to compliance reports done by third parties who have validated a wide range of compliance standards. Check out the AWS Compliance Center in order to find compliance information all in one place. It will show you compliance enabling services as well as documentation like the AWS Risk and Security Whitepaper, which you should read to ensure that you understand security and compliance with AWS. 

To know if you are compliant in AWS, please remember that we follow a shared responsibility. The underlying platform is secure, and AWS can provide documentation on what types of compliance requirements they meet, through services like AWS Artifact and whitepapers. But, beyond that, what you build on AWS is up to you. You control the architecture of your applications and the solutions you build, and they need to be built with compliance, security, and the shared responsibility model in mind.

#### AWS Artifact
Depending on a company’s industry, it might need to uphold specific standards. An audit or inspection will ensure that the company has met those standards.

AWS Artifact is a service that provides on-demand access to AWS security and compliance reports and select online agreements. AWS Artifact consists of two main sections: 
* AWS Artifact Agreements 
* and AWS Artifact Reports.

##### AWS Artifact Agreements
Suppose that your company needs to sign an agreement with AWS regarding your use of certain types of information throughout AWS services. You can do this through AWS Artifact Agreements. 

In AWS Artifact Agreements, you can review, accept, and manage agreements for an individual account and for all your accounts in AWS Organizations. Different types of agreements are offered to address the needs of customers who are subject to specific regulations, such as the Health Insurance Portability and Accountability Act (HIPAA).

##### AWS Artifact Reports
Next, suppose that a member of your company’s development team is building an application and needs more information about their responsibility for complying with certain regulatory standards. You can advise them to access this information in AWS Artifact Reports.

AWS Artifact Reports provide compliance reports from third-party auditors. These auditors have tested and verified that AWS is compliant with a variety of global, regional, and industry-specific security standards and regulations. AWS Artifact Reports remains up to date with the latest reports released. You can provide the AWS audit artifacts to your auditors or regulators as evidence of AWS security controls. 

#### AWS Customer Compliance Center
The Customer Compliance Center contains resources to help you learn more about AWS compliance. For more information, see [Customer Compliance Center](https://aws.amazon.com/compliance/customer-center/).

In the Customer Compliance Center, you can read customer compliance stories to discover how companies in regulated industries have solved various compliance, governance, and audit challenges.

You can also access compliance whitepapers and documentation on topics such as the following:
* AWS answers to key compliance questions
* An overview of AWS risk compliance
* An auditing security checklist

Additionally, the Customer Compliance Center includes an auditor learning path designed for individuals in auditing, compliance, and legal roles. They can learn more about how their internal operations can demonstrate compliance using the AWS Cloud.

**It is important to remember that AWS has a wide array of services that perform very different functions. Because of this, compliance requirements vary from service to service.**

#### AWS Config
AWS Config continuously monitors and records your AWS resource configurations for compliance purposes. AWS Config conformance packs provide a general-purpose compliance framework. They are designed to help you create security, operational, or cost-optimization governance checks using AWS Config managed or custom rules and remediation actions. 

The basis of a well-architected multi-account AWS environment is AWS Organizations, an AWS service you can use to centrally manage and govern multiple accounts. When you combine Organizations with the capabilities of AWS Config, you can efficiently manage and automate configuration compliance at scale for hundreds of member accounts.

### Knowledge Check
#### Which of the following is an example of an AWS Trusted Advisor security check?
**Amazon S3 bucket permissions**.

The other options do the following:
* **Amazon EBS underprovisioned volumes** are a *performance* check.
* **Auto Scaling group resources** are a *fault tolerance* check.
* **Low utilization Amazon EC2 instances** are a *cost optimization* check.

#### Which statement best describes the AWS relationship with the overall compliance of a customer's application built using AWS services?
**The customer can use whitepapers and documentation found in the Customer Compliance Center. However, they are ultimately responsible for their application's compliance.**

#### Which piece of information does AWS CloudTrail not provide?
**Who wrote the API call taking place**.

### Summary
#### Trusted Advisor security checks
These checks compare implemented AWS infrastructure against AWS security best practices and then make recommended actions.

#### AWS Artifact
AWS has a wide array of services that perform very different functions. Because of this, compliance requirements vary from service to service. Customers can use the [Customer Compliance Center](https://aws.amazon.com/compliance/customer-center/), which contains the following information: 
* Customer compliance stories that can be used to discover how other companies in regulated industries have met their guidelines.
* Whitepapers and documentation for various topics, such as answers to key compliance questions, auditing security checklists, and an overview of AWS risk compliance.
* Auditor learning paths that can be used by individuals on a customer's auditing, compliance and legal teams.

#### CloudTrail
This service is activated by default and records all API calls for an AWS account. It provides information such as the following:
* Who or what is making a request
* When the request happened
* Where the request came from
* What happened because of the request

#### AWS CloudTrail Insights
This is a feature of CloudTrail. When activated, it will automatically detect unusual API activities in an AWS account.

## Protecting Data in Transit and at Rest
### Pre-assessment
#### Which AWS service could be used to encrypt credit card information being sent to an AWS customer?
**AWS Certificate Manager (ACM)**.

* **AWS CloudHSM** provides FIPS single-tenant validated encryption for data that is being stored.
* **AWS KMS** provides FIPS multi-tenant validated encryption for data that is being stored.
* **AWS Secrets Manager** supports the rotation and securing of secrets such as API keys and database credentials.

#### Which AWS service provides Federal Information Processing Standards (FIPS) validated multi-tenant encryption for stored data?
**AWS Key Management Service (AWS KMS)**.

* **AWS CloudHSM** provides FIPS-validated single-tenant encryption for data that is being stored.
* **ACM** provides encryption for data that is being sent through AWS based websites and applications.
* **AWS Secrets Manager** supports the rotation and securing of secrets such as API keys and database credentials.

#### Which AWS service could be used by AWS Lambda to retrieve the password of a database created using Amazon RDS?
**AWS Secrets Manager**.

* **Amazon Aurora** provides a global-scale relational database service built for the cloud with full MySQL and PostgreSQL compatibility. 
* **AWS KMS** provides FIPS multi-tenant validated encryption for data that is being stored.
* **Amazon RDS** provides fully managed, open-source relational databases, not secrets management.

### Encrypting Data with AWS
AWS provides services that help you protect your data, accounts, and workloads from unauthorized access. AWS data protection services provide encryption and key management and secure data while in transit. In this section, you will learn about AWS services for data protection.

#### Protection at rest
Data at rest represents any data that persists, or is stored, for any duration of time. This includes things like the following: 
* Block storage
* Object storage
* Databases
* Archives

Implementing encryption and appropriate access controls helps protect your data at rest and reduces the risk of unauthorized access. When encrypting data, you have two options: 
* Client-side encryption: Data is encrypted before sending it to AWS.
* Server-side encryption: AWS encrypts data after it has been received by the service.

#### Protection in transit
Data in transit is any data that gets transmitted from one system to another. This includes the following:
* Communication between resources within an environment
* Communication between services
* Communication between services and end users

By providing the appropriate level of protection for data in transit, the confidentiality and integrity of that data is protected. These are some of the ways that AWS provides this kind of encryption:
* End-to-end encryption when communicating with AWS APIs through the use of HTTPS endpoints using TLS (see glossary) for communication
* Web-based workloads with TLS encryption using AWS services to generate, deploy, and manage public and private certificates
* IPsec (see glossary) and virtual private network (VPN) connectivity into AWS being used to facilitate the encryption of traffic

#### Glossary
##### SSL/TLS
Secure Sockets Layer/Transport Layer Security (SSL/TLS) creates an encrypted channel between a web server and web client that protects data in transit from being eavesdropped on. 

##### IPsec
IPsec is a set of communication rules or protocols for setting up secure connections over a network. Internet Protocol (IP) is the common standard that determines how data travels over the internet. IPsec adds encryption and authentication to make the protocol more secure. For example, it scrambles the data at its source and unscrambles it at its destination. It also authenticates the source of the data. 

### Encrypting Data in Transit and Securing Messages with AWS Certificate Manager (ACM)
AWS Certificate Manager (ACM) handles the complexity of creating and managing public SSL/TLS certificates for AWS based websites and applications. ACM can also be used to issue private SSL/TLS X.509 certificates that identify users, computers, applications, services, servers, and other devices internally. 

X.509 certificates are a standard certificate used for many internet protocols.

ACM provisions and manages public and private TLS certificates and integrates with the following:
* Elastic Load Balancing (ELB)
* Amazon CloudFront
* Amazon API Gateway
* AWS Nitro Enclaves

#### What is SSL/TLS?
SSL is an encryption-based internet security protocol. It is the predecessor to the more modern encryption method TLS. Both SSL and TLS provide encryption for data between a client and web server.

A common use case where you can see SSL/TLS in action is when you use a website that requires HTTPS instead of HTTP. You can tell when a website does this because if you type http://<website name> into a browser, as the site appears, the address bar will change the http to https. Continuing with the website example, if a website did not use SSL/TLS, any information sent between a computer and that web server would be in plaintext. If that information was intercepted by a hacker in the process, they could then read the data. This includes things like passwords, credit card data, health information, or emails.

With SSL/TLS, if that information was intercepted in transit, it would be jumbled and could not be understood. So how does this process work?

First, a client's browser contacts a web server in a TCP handshake. Next, the TLS process starts. During this, on the client side, the client SSL or TLS sends a hello message that lists its cryptographic information such as its SSL or TLS version. And it lists the cipher suites that it supports, in order of preference. Cipher suites are a set of algorithms that help secure a network connection.

The message also contains a random byte string that is used in later computations. The server’s SSL or TLS responds with its own hello message. This message contains the cipher suite it will use, the session ID, another random byte string, and a public key. If a digital certificate is required for client authentication, the server will also send a client certificate request that includes a list of types of certificates it has.

At this point, the messages sent back and forth are asymmetrically encrypted. Next, the client SSL or TLS verifies the digital certificate. The client SSL or TLS sends the random byte string. This string makes it possible for the client and server to compute the secret key that will be used for encrypting the data they pass to each other. This random byte string is then encrypted with the server’s public key. If the server SSL or TLS sent a client certificate request, the client needs to send another encrypted random byte string with the client's private key and the client’s digital certificate, or a no digital certificate alert. Although this alert is only a warning, it does cause the handshake to fail if client authentication is required.

The server SSL or TLS verifies the client's certificate. The client SSL or TLS sends the server a finished message encrypted with the secret key that it made with the client. This signals that the client side of the handshake is finished. The server SSL or TLS then responds with its own finished message, also encrypted with the secret key. This signals that its side of the handshake is finished as well. For the rest of the session, the client and server can communicate using their shared key, making this now symmetrically encrypted.

#### How ACM helps with secure data in transit 
ACM is one of the controls that can be used to protect data in transit to reduce the risk of unauthorized access or loss. It accomplishes this by storing digital certificates and securely rotating them at specified timed intervals and applying strict access control. This helps accomplish the following:
* Protecting and securing website: SSL/TLS provides encryption for sensitive data in transit and authentication using certificates to establish the identity of a site and to secure connections between browsers, applications, and that site. ACM provides a convenient way to provision and manage these certificates so that a website or application is configured to use the SSL/TLS protocol. 
* Improving site uptime: ACM helps manage the challenges of maintaining SSL/TLS certificates, including certificate renewals, so customers do not have to worry about expiring certificates.

#### How ACM helps manage certificates
ACM also stores and rotates certificates at timed intervals, which can help ensure that companies are securing their messages.

When a public certificate is requested, ACM generates a public/private key pair. For imported certificates, the customer generates the key pair. The public key becomes part of the certificate. ACM stores the certificate and its corresponding private key, and uses AWS Key Management Service (AWS KMS) to help protect the private key.

### Encrypting Data at Rest with AWS KMS and AWS CloudHSM
A hardware security module (HSM) is a computing device that processes cryptographic operations and provides secure storage for cryptographic keys.

#### AWS Key Management Service (AWS KMS)
AWS Key Management Service (AWS KMS) is a fully managed, FIPS-validated (see glossary), multi-tenant (see glossary) solution. With AWS KMS, customers can use symmetric keys (see glossary) for encryption and decryption of data. Asymmetric key pairs (see glossary) can be used to validate digital signatures for signing operations. AWS KMS is integrated with all major AWS services, so it can help with things like the following:
* Providing logs of all key usage to help meet regulartory and compliance needs
* Controlling access to services and customer content

With AWS KMS, customers choose the specific levels of access control that they need for their keys. For example, they could specify which IAM users and roles are able to manage keys. Alternatively, they could temporarily disable keys so that they are no longer in use by anyone. The keys are centrally located and never leave AWS KMS.

AWS KMS has an SDK that allows customer applications to access the service through an API.

AWS KMS creates and controls encryption keys. They are monitored by AWS CloudTrail and Amazon CloudWatch and integrated with services like the following:
* Amazon Elastic Compute Cloud (Amazon EC2)
* Amazon Simple Storage Service (Amazon S3)
* Amazon Elastic Block Store (Amazon EBS)

#### Glossary
##### FIPS-validated
Federal Information Processing Standards (FIPS) validation means that a security solution, including hardware and software, are tested and approved by an independent laboratory accredited by National Institute of Standards and Technology (NIST). NIST works with businesses of all sizes to advance and standardize the way that they measure science, standards, and technology.

##### Multi-tenant
A multi-tenant architecture uses a shared infrastructure to provide access to a software as a service (SaaS) solution to multiple customers.

##### Symmetric and asymmetric key pairs
**Symmetric encryption** uses the same secret key to perform both the encryption and decryption processes.

**Asymmetric encryption**, also known as public-key encryption, uses two keys, a public key for encryption and a corresponding private key for decryption. 

#### AWS CloudHSM
AWS CloudHSM is a FIPS-validated, fully managed single-tenant (see glossary) solution that is used for adhering to strict key management requirements. In CloudHSM, the customer controls the following:
* Scaling
* Availability
* Performance
* Key access

CloudHSM is used to manage the HSMs that generate and store encryption keys. HSMs are created and managed in CloudHSM, including creating users and setting their permissions. You also create the symmetric keys and asymmetric key pairs that the HSM stores. 

Customers can use the CloudHSM SDK to integrate into their own applications using industry-standard APIs, making it so they never have to leave their own environments to perform cryptographic actions.

CloudHSM is an isolated HSM environment where keys can be provisioned and managed. It can be accessed by the AWS Management Console and command line interface (CLI). It can integrate with a customer's own applications. Amazon CloudWatch and AWS CloudTrail provide logging.

#### Glossary
##### Single-tenant
A single-tenant architecture provides each customer with a distinct software instance running on infrastructure that is not shared with other users. Customers can choose this solution for the extra security that it provides.

**A customer would choose CloudHSM instead of AWS KMS if they must have their hardware security modules completely separate from any other entities. In these instances, each HSM is on its own security domain, which isolates it from any other customer. A use case example would be federal organizations that have highly sensitive data.**

### Encrypting Secrets with AWS Secrets Manager
AWS Secrets Manager is a secrets management service that helps protect access to applications, services, and IT resources. With this service, customers can rotate, manage, and retrieve database credentials, API keys, and other secrets throughout their life cycle. 

Secrets Manager stores credentials, API keys, tokens, and other secrets such as AWS Lambda secrets that are rotated on a schedule. It can integrate with many services, both AWS and third party, without hardcoding secrets in plaintext.

Monitoring and audit compliance can be automated using CloudTrail and CloudWatch respectively.

#### Featured use case
##### [Database credentials to Lambda functions](https://aws.amazon.com/blogs/compute/securely-retrieving-secrets-with-aws-lambda/)
Use case to see how AWS Secrets Manager can be used to secure database credentials sent to Lambda functions. These functions will then use the credentials to connect and query the backend database service Amazon RDS, without hardcoding the secrets.

### Knowledge Check
#### A government AWS customer is required to store their data in a single-tenancy architecture. Which AWS service should they use?
**AWS CloudHSM**.

* ACM provides encryption for data that is being sent through AWS based websites and applications. 
* AWS KMS provides FIPS multi-tenant validated encryption for data that is being stored.
* AWS Secrets Manager makes possible the rotation and securing of secrets such as API keys and database credentials.

#### Which service would provide authentication and encryption for data being sent by SSL/TLS?
**AWS Certificate Manager (ACM)**.

* AWS CloudHSM provides FIPS single-tenant validated encryption for data that is being stored.
* AWS KMS provides FIPS multi-tenant validated encryption for data that is being stored.
* AWS Secrets Manager makes possible the rotation and securing of secrets such as API keys and database credentials.

#### Which AWS service could be used to rotate the certificate used by another AWS service?
**AWS Secrets Manager**.

* AWS KSM provides FIPS multi-tenant validated encryption for data that is being stored.
* AWS CloudHSM provides FIPS single-tenant validated encryption for data that is being stored.
* AWS KMS provides FIPS multi-tenant validated encryption for data that is being stored.

### Summary
* AWS has services that help customers protect data, accounts, and workloads from unauthorized access. 
* Data has two main states: at rest, which is data stored or persistent for any duration of time, and in transit from one system to another, such as communication between services or between services and end users.

#### AWS Certificate Manager (ACM)
This AWS service protects data in transit, manages public SSL/TLS certificates, and can issue private SSL/TLS certificates.

#### AWS Key Management Service (AWS KMS)
This AWS service protects data at rest in a FIPS-validated, multi-tenant solution.

#### AWS CloudHSM
This AWS service protects data at rest in a FIPS-validated, single-tenant solution.

#### AWS Secrets Manager
This AWS service is a secrets management service that helps protect access to applications, services, and IT resources. 

## Minimizing Your Attack Surface
### Pre-assessment
#### Which AWS service can help decrease the attack surface of compute resources?
**Amazon Inspector**.

* ACM provisions, manages, and deploys public and private SSL/TLS certificates for use with AWS services and internal connected resources.
* Amazon Detective uses prebuilt data aggregations, summaries, and context to quickly analyze and determine the nature and extent of possible security issues.
* Amazon Macie uses machine learning and pattern matching to discover and protect sensitive data.

#### Which Amazon VPC use case requires using Amazon VPC Network Access Analyzer?
**Identify unintended network access to AWS resources.**.

#### Which AWS service can help decrease the attack surface of AWS Lambda functions?
**Amazon Inspector**.

* ACM provisions, manages, and deploys public and private SSL/TLS certificates for use with AWS services and internal connected resources.
* Amazon Detective uses prebuilt data aggregations, summaries, and context to quickly analyze and determine the nature and extent of possible security issues.
* Amazon Macie uses machine learning and pattern matching to discover and protect sensitive data.

### Vulnerabilities That Can Increase Your Attack Surface
The attack surface refers to any part of an application that is visible externally to end users or could be reached through other methods such as social engineering or human error.

These are some types and examples of vulnerabilities:
* **Network vulnerabilities**: These can include poorly configured firewalls or open and unprotected wireless access.
* **OS vulnerabilities**: This includes things like unsupported operating systems and systems not up to date on their patches. Out-of-date operating systems are not just on end-user computers. They are also in the hardware or virtualized hardware that run applications, such as Amazon Elastic Compute Cloud (Amazon EC2) instances. 
* **Process**: A weak password can create an easy back door into the application and data tiers.
* **Design**: Poorly designed applications can have vulnerabilities built into them. If access to a database is visible in external-facing code, it's easy for unauthorized access to occur.
* **Coding**: The use of open-source code can create unintended consequences such as default read access in containers.
* **End-of-service life**: If a service such as Lambda no longer supports a runtime environment (see glossary), the customer must migrate their applications to a supported runtime environment.

#### Glossary
##### Runtime environment
A runtime environment is a subsystem or software platform that lives on the system that a program was built on, as well as the systems that it is meant to be run on. An example of this is Adobe Flash Player, which has been deprecated due to vulnerabilities.

### Ways to Decrease the Attack Surface
#### Analyzing network access: Network Access Analyzer
Network Access Analyzer is a resource within Amazon Virtual Private Cloud (Amazon VPC) that identifies unintended network access to resources on AWS. It can be used to specify network access requirements and to identify potential network paths that do not meet those requirements. This feature helps address the fact that AWS environments are dynamic with evolving security mandates, network designs, and AWS networking service inclusion.

Each change introduces new connectivity models, which can render all previous manual validation efforts obsolete.

#### Decreasing the attack surface in compute resources: Amazon Inspector
Amazon Inspector automatically detects if a vulnerability has been patched or remediated. When it is detected, Amazon Inspector automatically changes the state of the finding to Closed without manual intervention.

By highlighting areas that have not been remediated or patched in compute resources, Amazon Inspector highlights attack surfaces.

#### Decreasing the attack surface of Lambda functions
In addition to scanning server-based compute resources, Amazon Inspector scans serverless AWS Lambda functions. Amazon Inspector scans Lambda functions and layers initially upon deployment and automatically rescans them when there are changes in the workloads. An example would be when a Lambda function is updated or when a new Common Vulnerabilities and Exposures (CVE) is published by MITRE corporation. The MITRE corporation is a United States non-profit organization that manages federally funded research and development centers. These centers support a variety of US government agencies in fields such as aviation, defense, healthcare, homeland security, and cybersecurity.

### Knowledge Check
#### Which AWS service or feature should be used to ensure that Amazon EC2 instances are properly patched?
**Amazon Inspector**.

* Amazon Detective quickly analyzes and determines the nature and extent of possible security issues.
* IAM Access Analyzer analyzes AWS CloudTrail logs to identify actions and services that have been used by an IAM entity.
* Amazon VPC Network Access Analyzer identifies unintended network access to resources on AWS.

#### When does Amazon Inspector scan AWS Lambda functions?
**When a new CVE is published by MITRE**.

Amazon Inspector scans Lambda functions and layers initially upon deployment and automatically rescans them when there are changes in the workloads. An example would be when a Lambda function is updated or when a new CVE system is published by the MITRE corporation.

#### Which Amazon VPC use case requires using Amazon VPC Network Access Analyzer?
**Specifying access requirements**.

### Summary
#### Things that can increase the attack surface
* Network vulnerabilities 
* OS vulnerabilities
* Weak processes
* Poorly designed applications
* Open-source code
* System and service deprecation

#### Network Access Analyzer
Network Access Analyzer is an Amazon VPC resource that identifies unintended network access to resources on AWS. It can be used to specify network access requirements and to identify potential network paths that do not meet those requirements.

#### Amazon Inspector
By highlighting areas that have not been remediated or patched in compute resources, Amazon Inspector highlights attack surfaces. 

#### Lambda functions
Amazon Inspector also scans Lambda functions and layers initially upon deployment and automatically rescans them when there are changes in the workloads, for example, when a Lambda function is updated or when a new CVE is published by MITRE.

## Preparing for Security Events
### Pre-assessment
#### Which AWS support group or service provides help with a distributed denial of service (DDoS) attack?
**AWS Shield Advanced**.

* AWS Managed Services provides ongoing management of AWS infrastructure.
* AWS Support provides tiered 24/7 support and access to customer service, AWS documentation, whitepapers, and support forums.
* AWS Trust & Safety Team provides support for abuse reports, and sends those reports to an AWS customer's security point of contact.

#### Which AWS service or feature would alert AWS Security Hub of public or cross-account access to resources?
**AWS Identity and Access Management (IAM) Access Analyzer**.

* AWS Config can contain rules for automatic remediation of noncompliant resources using AWS Systems Manager within a single AWS account.
* AWS CloudFormation can be used to quickly create a clean room to conduct deeper investigations.
* AWS Step Functions can be used to design and run workflows that stitch together services such as AWS Lambda and AWS CloudFormation to respond to an incident in the cloud.

#### An Amazon EC2 instance has been compromised. Which AWS service has a feature that can be used to create a copy of that EC2 instance?
**Amazon Elastic Block Store (Amazon EBS)**.

Amazon EBS has a feature called an Amazon EBS snapshot, which creates a copy of resources like EBS volumes, EC2 instances, boot volumes, and on-premises block data.

### Incident Response
Incident response is the methodology that an organization uses to respond to and manage an incident, such as a security breach or cyberattack.

Incident response (IR) consists of an organized approach to responding to and recovering from an incident. Even with extremely mature preventive and detective controls in place, an organization should have IR processes established. These processes help mitigate the potential impact of security incidents. IR is a system of people, processes, and technology used to prepare for, detect, contain, and recover from a suspected cybersecurity incident or compromise.

#### People fit into IR as follows: 
* As members of a security program, we create an incident response plan so that we can effectively respond to security events within our AWS accounts.
* The security operations center (SOC) has a clear process and procedure for anyone to submit a possible security incident.
•

#### Processes fit into IR as follows: 
* An SOC person needs to integrate AWS into their overall incident response plan, so they can respond to threats across their organization.
* An SOC analyst needs to define security assertions for their organization's cloud environment.
* An SOC analyst has a defined playbook to turn on out-of-band communication and operations for incident response.
* An SOC has a defined decision tree with other teams and their stakeholders for incident response operations.
•

#### Technology fits into IR as follows: 
* An IR team has appropriate access to perform incident response duties before an event occurs.
* An SOC analyst needs to augment and enrich findings from Amazon GuardDuty, so they can accurately determine the response required.
* An SOC analyst needs to understand how to analyze AWS CloudTrail logs so they can respond to events.

### What do incidents look like in the cloud?
Some common incident types in cloud environments include the following:

| Incident | What Happens |
| -------- | ------------ |
| Unauthorized access | Access to your resources through an IP address, user, or system that is unauthorized |
| Compliance variance | Data or resources configured in a way that violates your compliance policies |
| Service disruption | Users or systems cannot access resources in your environment |
| Unauthorized resources | Resources created in your environment that are unauthorized or unexpected |
| Privilege escalation | Attempts to gain elevated access to resources that are normally protected from an application or user or attempts to gain access to your system or network for an extended period of time |
| Persistence | Attempts to establish an access mechanism to permit future access to resources |
| Excessive permissions | Resources that have overly permissive access control mechanisms or permissions |
| Information exposure | Anomalous or unauthorized access to sensitive data |
| Credentials exposure | Unauthorized access to AWS specific credentials |

### Foundation of incident response
All AWS users within an organization should have a basic understanding of security incident response processes. The foundation of a successful incident response program in the cloud is to educate, prepare, simulate, and iterate, which are described as follows:
* Educate your SOC and IR staff about cloud technologies and how your organization intends to use them. Work with other teams to establish expected baseline operations and use that knowledge to identify deviations from normal operations.
* Prepare your IR team to detect and respond by activating detective capabilities and ensuring appropriate access to the necessary tools or services. Prepare runbooks—both manual and automated—to ensure reliable and consistent responses.
* Simulate both expected and unexpected security events in your cloud environment to understand the effectiveness of your preparation. Rehearse incident response and recovery frequently. Run simulated incident response events—game days—for different threats that involve key staff and management. Use lessons learned from running game days as part of a feedback loop to improve your processes.
* Iterate on the outcome of your simulation to increase the scale of your response posture, reduce delays, and further reduce risk.

| How is IR in the cloud different than traditional incident response? | How is it the same? |
| -------------------------------------------------------------------- | ------------------- |
| It adds an additional layer—the control plane. | The process for performing incident response remains the same. |
| It contains additional logs and artifacts to understand and analyze. | Subject matter expertise is still critical for effective response. |
| It offers much more scalable methods for response and attacks. | Logs and endpoints still have to be monitored, acquired, and analyzed. |

### AWS support for IR
* **AWS Managed Services (AMS)** provides ongoing management of AWS infrastructure so you can focus on applications. AMS automates common activities, such as change requests, monitoring, patch management, security, and backup services. AMS provides full-lifecycle services to provision, run, and support your infrastructure.

As an infrastructure operator, AMS takes responsibility for deploying a suite of security detective controls. It provides a 24/7 first line of response to alerts using a follow-the-sun model. The follow-the-sun model is a workflow used by many global companies. Workloads are passed from offices in different time zones to increase coverage. When an alert is generated, AMS follows a standard set of automated and manual runbooks to ensure a consistent response. These runbooks are shared with AMS customers during onboarding, so they can develop and coordinate response with AMS. AMS encourages the joint operation of security response simulations with customers to develop operational muscle before a real incident occurs.

* **AWS Support** offers a range of plans that provide access to tools and expertise that support the success and operational health of your AWS solutions. All support plans provide 24/7 access to customer service, AWS documentation, whitepapers, and support forums. If you need technical support and more resources to help with your AWS environment, you can select a support plan that best aligns with your AWS use case.

* **The AWS Trust & Safety (T&S) team** sends abuse reports to the security contact on the customer's account. If there is no security contact listed, the T&S team contacts the email address listed on their account. If the customer receives a report, they should review the abuse notice to see which content or activity was reported. Logs that implicate abuse are included along with the abuse report, as provided by the reporter. The customer must also reply directly to the abuse report and explain how they are preventing the abusive activity from recurring in the future. If the customer does not respond to an abuse notice within 24 hours, AWS might block their resources or suspend their AWS account.

* **AWS Shield Advanced** gives you 24/7 access to the AWS Shield Response Team, as discussed in previous topics.

### AWS Security Hub
Security Hub is a fully managed service. It provides you with a comprehensive view of your security state in AWS with the security industry standards and best practices. Security Hub collects security data from across AWS accounts, services, and supported third-party Partner products. It helps you analyze your security trends and identify the highest-priority security issues. This lets you view the current status of the security and compliance checks to spot trends, identify potential issues, and take the necessary remediation steps. 

### Security Hub integration
Security Hub automatically collects and ingests findings from AWS Partner integrations and certain AWS services such as the following:
* Amazon GuardDuty
* Amazon Inspector
* AWS Firewall Manager
* AWS Identity and Access Management (IAM) Access Analyzer
* Amazon Macie
* AWS Config
* Patch Manager, a capability of AWS Systems Manager

Security Hub uses a standard data format, eliminating the need for time-consuming data conversion efforts. A finding is a potential security issue. For example, IAM Access Analyzer integration with Security Hub sends findings to Security Hub when policies permit public or cross-account access to resources. Security Hub automatically activates this integration if you are already using IAM Access Analyzer. 

Another example is the Firewall Manager integration with Security Hub, which sends the following four types of findings to Security Hub:
* Resources that are not properly protected by AWS WAF rules
* Resources that are not properly protected by AWS Shield Advanced
* Shield Advanced findings that indicate a DDoS attack is underway
* Security groups that are used incorrectly

Security Hub generates prebuilt dashboards, which provide summaries of key security and compliance status and trends. This simplifies the process of monitoring and visualizing security issues.

### Security Hub insights
With Security Hub insights, you can correlate and group security findings to help identify higher priority findings faster. Security Hub provides more than 100 insights out of the box to get you started. In addition to default insights provided by AWS and AWS Partners, you can create your own insights to track issues that are unique to your environment. 

The Security Hub dashboard shows a trending snapshot of your top security insights prioritized by severity. You can also create a my favorites insights group that contains your top insights from AWS and AWS Partners. When you drill down on the security findings from insights, you can view additional details, including resource and finding details, remediation recommendations, and annotations. Some examples of insights are Amazon Elastic Compute Cloud (Amazon EC2) instances that have missing security patches and Amazon Simple Storage Service (Amazon S3) buckets with stored credentials or public write or read permissions.

### Use case: Threat response automation
Security Hub can be used to automate response and threat remediation tasks.

#### Security findings
Security Hub sends security findings as custom events to Amazon EventBridge events. Using EventBridge rules, you can determine the response type.

#### Rule
If the event is associated with a rule, it might activate a response. In this scenario, you have a yellow rule for one type of finding and a red rule for another type of finding. Using *yellow* or *red* are just examples of ways to represent organizational risk and help simplify the responses.

#### Yellow alarm response
If the rule associated to a yellow alarm is activated, an AWS Lambda function is invoked to act on the recommendation and remediate the finding. A Lambda function can be created for every possible existing remediation recommendation.

#### Red alarm response
If the rule associated to a red status is activated, the finding is published to an Amazon Simple Notification Service (Amazon SNS) topic. The Amazon SNS topic notifies the security operations team and indicates that the situation might require human intervention.

#### Protected messaging
With message data protection for Amazon SNS, the security team can de-identify data within a message payload in real time though data redaction, or masking. This is useful to the security team when incident messages are sent, but it can be used more broadly throughout an environment.

##### Diagram explanation
Process showing AWS Security Hub sending security events to Amazon EventBridge, rule application, and then routing to either AWS Lambda for automated remediation or Amazon SNS, which sends a message to a security engineer.

### AWS solutions: Security Hub Automated Response and Remediation
The AWS Security Hub Automated Response and Remediation solution is an add-on that works with Security Hub. It provides predefined response and remediation actions based on industry compliance standards and best practices for security threats. It helps Security Hub customers resolve common security findings and improve their security posture in AWS.

With this solution, you can access remediation playbooks supporting the Center for Internet Security (CIS) AWS Foundations Benchmark v1.2.0, AWS Foundational Security Best Practices v1.0.0, and Payment Card Industry Data Security Standard (PCI DSS) v3.2.1.

#### Detect
Security Hub collects events and data from other AWS services. These items are analyzed against security standards, such as CIS AWS Foundations Benchmark. Exceptions are asserted as findings in the Security Hub console. New findings are sent as Amazon CloudWatch logs.

#### Ingest
Two EventBridge event rules are deployed for each supported control by the solution. One rule matches the custom action event, or user-initiated remediation. The other rule, turned off by default, matches the real-time finding event.

Customers can use the Security Hub custom action menu to initiate automated remediation. Or after careful testing, they can turn on automatic triggering per remediation.

#### Remediate
Using cross-account IAM roles, the automated remediation uses the AWS API to perform the tasks needed to remediate findings. All playbooks in this solution call Lambda functions. Some Lambda functions perform remediation directly. Others use documents from Automation, a capability of AWS Systems Manager.

#### Log
The playbook logs the results, sends a notification to an Amazon SNS topic, and updates the Security Hub finding. An audit trail of actions is maintained in the finding notes, such as workflow status and details on remediation performed.

##### Diagram explanation
Process showing Security Hub detecting events and data and passing it to EventBridge. From there, incidents are remediated using Lambda functions and sometimes Step Functions to stitch together workflows. Results are passed to Amazon SNS, which then updates Security Hub. 

### Incident Response in AWS
#### Automating incident response with APIs
In AWS, APIs can automate many of the routine tasks that must be performed during incident response. For example, using a single command can isolate an instance by changing the security groups associated with the instance. 

#### Creating snapshots: Amazon EBS snapshots
Forensics often requires capturing the disk image as it was during the time of an attack. This makes it so that security teams can find the vulnerabilities that were exploited and track the path that an attacker took.

Amazon Elastic Block Store (Amazon EBS) provides snapshots for resources such as EBS volumes, EC2 instances, boot volumes, and on-premises block data. 

EBS data and boot volumes as well as non-EBS volumes can have snapshots. This can be automated using Amazon Data Lifecycle Manager (Amazon DLM). These volumes can then be restored by launching an EC2 instance.

#### Operating in a clean room: AWS CloudFormation
AWS CloudFormation can be used to quickly create a new, trusted environment in which to conduct deeper investigation. CloudFormation can deploy preconfigured instances in an isolated environment that contains all the necessary tools that forensic teams need to determine the cause of the incident.

#### Creating serverless workflows with AWS Step Functions: AWS Step Functions
AWS Step Functions can coordinate multiple AWS services into serverless workflows so that applications can be built and updated quickly. Workflows are made up of a series of steps, with the output of one step acting as the input into the next. Step Functions can be used to design and run workflows that stitch together services such as AWS Lambda and AWS CloudFormation to respond to an incident in the cloud.

#### Incident response using AWS Config
AWS Config can be used to automate detection and incident responses. You can create rules within AWS Config for automatic remediation of noncompliant resources using AWS Systems Manager within a single AWS account. Additionally, AWS Config stores current and historical configurations that can help determine the root cause of an incident.

#### Incident response using Amazon Detective
Amazon Detective can analyze trillions of events from multiple data sources. It automatically creates a unified, interactive view of your resources, users, and the interactions between them. This helps you to drill down into relevant historical activities and quickly determine the root cause.

#### Featured use case
##### [Investigate VPC flow with Amazon Detective](https://aws.amazon.com/blogs/security/investigate-vpc-flow-with-amazon-detective/)
Many AWS customers need enhanced insight into IP network flow. Amazon Detective can help with this.

### Knowledge Check
#### Which AWS support group or service provides help with application abuse reports such as spam?
**AWS Trust & Safety (T&S) team**

* AMS provides ongoing management of AWS infrastructure.
* Shield Advanced provides 24/7 access to the AWS Shield Response Team.
* AWS Support provides tiered 24/7 support and access to customer service, AWS documentation, whitepapers, and support forums.

#### Which AWS service or feature would alert AWS Security Hub of resources that are not properly protected by AWS Shield Advanced?
**AWS Firewall Manager**.

* AWS Config can contain rules for automatic remediation of noncompliant resources using AWS Systems Manager within a single AWS account.
* AWS CloudFormation can be used to quickly create a clean room to conduct deeper investigations.
* AWS Step Functions can be used to design and run workflows that stitch together services such as AWS Lambda and AWS CloudFormation to respond to an incident in the cloud.

#### Which AWS service can be added to an AWS Security Hub workflow to notify a security operations team of a remediation issue that might require human intervention?
**Amazon Simple Notification Service (Amazon SNS)**.

* EventBridge ingests data from customers' applications, software as a service (SaaS) applications, and AWS services, and routes that data to targets.
* Amazon SQS sends, stores, and receives messages between software components.
* AWS Step Functions can be used to design and run workflows that stitch together services such as AWS Lambda and AWS CloudFormation to respond to an incident in the cloud.

### Summary
Incident response (IR) is a system of people, processes, and technology used to prepare for, detect, contain, and recover from a suspected cybersecurity incident or compromise.

The following AWS services and features can be used as part of an IR workflow:

#### Amazon EBS snapshots
Amazon EBS provides snapshots for resources such as EBS volumes, EC2 instances, boot volumes, and on-premises block data.

#### AWS CloudFormation
This AWS service can be used to quickly create a clean room that can be used for deeper investigations.

#### AWS Step Functions
This AWS service can be used to link multiple AWS services together to run IR workflows.

#### AWS Config
This AWS service can be used to automate detection and incident response through the implementation of rules.

## Assessment
### 1. A company has implemented Amazon CloudWatch to centralize logs of events and resource states. Those logs are then analyzed for anomalies that might indicate threat. Which AWS Security Pillar does this security measure reflect?
* **Detective controls**
* Incident response
* Infrastructure protection
* Data protection

The correct answer is **Detective controls**.
* Detective controls: CloudWatch is a part of the first phase of detective control implementation. Detective controls ensures there is a means to identify a security threat or incident.
* Infrastructure protection: Ensures that systems and services within a customer's workload are protected aqainst unintended and unauthorized access and potential vulnerabilities.
* Data protection: Ensures there is means for protecting data at rest and data in transit through encryption methods, access control, and data classification.
* Incident response: Ensures there are systems and processes in place to respond to and mitigate the potential impact of security incidents.

### 2. A company uses Amazon EC2 instances to host a web server. Who is responsible for the infrastructure that runs the EC2 instances and the patching of the EC2 instances, according to the shared responsibility model?
* The customer is responsible for infrastructure and AWS is responsible for patching.
* **AWS is responsible for the infrastructure and the customer is responsible for patching.**
* The customer is responsible for both infrastructure and patching.
* AWS is responsible for both the infrastructure and patching.

In the shared responsibility model, AWS is responsible for global infrastructure (Security OF the cloud) that runs AWS services, and customers are responsible for the guest operating system (0S) that is on the EC2 instances (Security IN the cloud).

### 3. Amazon RDS for Oracle is a fully managed database. Who is responsible for ensuring the database is properly patched, according to the shared responsibility model?
* Both the customer and AWS are responsible.
* The customer is responsible.
* It depends on which license model is used.
* **AWS is responsible**.

Because this service is fully managed, AWS is responsible for database management tasks, such as hardware provisioning, software patching, setup, configuration, and backups.

### 4. AWS offers a solution that automates protection using AWS CloudFormation and AWS WAF rules designed to filter common web-based attacks. Which AWS Security Pillar does this security measure reflect?
* Incident response
* Data protection
* Detective controls
* **Infrastructure protection**

The correct answer is **Infrastructure protection**.
* **Infrastructure protection**: Implementing this solution ensures that systems and services within the customer's workload are protected against unintended and unauthorized access and potential vulnerabilities.
* **Detective controls**: Ensures there is a means to identify a security threat or incident.
* **Data protection**: Ensures there is a means for protecting data at rest and data in transit.
* **Incident response**: Ensures there are systems and processes in place to respond to and mitigate the potential impact of security incidents.

### 5. Which feature can be paired with Amazon Cognito credentials to reduce the risk of account takeover?
* User access keys
* Any of the above would work
* Multi-factor authentication
* Amazon EC2 key pairs

The correct answer is **Multi-factor authentication**. Adding multi-factor authentication reduces the risk of user account takeover and password theft. User access keys and Amazon EC2 key pairs are not compatible with Amazon Cognito.

### 6. A software developer would like to create scripts to automate actions within AWS services using the AWS CLI. Which methods do they have for authenticating? (Select TWO.)
* Amazon EC2 key pairs
* A username and password
* **Multi-factor authentication**
* **User access keys**
* Certificate-based authentication

The correct answers are **User access keys** and **Multi-factor authentication**. Username and password only provide access to the AWS Management Console. Amazon EC2 key pairs only provide access to EC2 instances. Certificate-based authentication is used with TLS/SSL.

### 7. A customer wants to use an external identity provider (IdP) to federate their users onto AWS software developer services and GitHub (a code repository). Which AWS service could they use to accomplish this?
* **AWS IAM ldentity Center**
* Amazon Cognito
* AWS ldentity Access Management (IAM)
* AWS Directory Service

The correct answer is **AWS IAM ldentity Center**.
* AWS IAM Identity Center helps customers securely create or connect workforce identities and manage their access centrally across AWS accounts and applications.
* IAM applies fine-grained access control and central account management.
* Amazon Cognito helps customers implement customer identity and access management (CIAM) into their web and mobile applications.
* AWS Directory Service makes it so customers can run directory-aware workloads in the AWS Cloud, including SharePoint and custom .NET and SQL Server-based applications.

### 8. A company is starting a new project involving highly sensitive information. One of the project's requirements is that only a consistent subset of the project team should be able to alter any of the project documents. Which AWS ldentity Access Management (|AM) feature should be used to implement this requirement?
* Users
* Roles
* **Groups**
* Security groups

The correct answer is **Groups**.
* With qroups, the company can specify permissions for similar types of users.
* With roles, the company can delegate temporary access to users, applications, or services that normally don't have access to the organization's AWS resources.
* Users are individual accounts people use to access AWS resources.
* Security groups are used to control incoming and outgoing traffic.

### 9. Which kind of access does the following AWS ldentity Access Managemnent (|AM) policy provide?
```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "FullAccess",
      "Effect": "Allow",
      "Action": ["s3:*"],
      "Resource": ["*"]
    }
  ]
}
```
* **Explicit allow**
* Implicit deny
* Implicit allow
* Explicit deny

The correct answer is **Explicit allow**. The effect, which specifies an explicit allow or deny, is set to Allow.

### 10. Review the file log. Which statement best describes the action that took place?
```
{ "Records": [{
    "eventVersion": "1. 0",
    "userIdentity": {
        "type": "IAMUser",
        "principalId" : "EX PRINCI PAL ID",
        "arn" : "arn:aws:iam: :123456789012 : user/Alice",
        "accountId" : "123456789012",
        "accessKeyId" : "EXAMPLE KEY ID",
        "userName": "Alice"
    },
    "eventīime": "2023-03-06T21:01:592"
    "eventSource": "ec2. ama zonaws. com",
    "eventName": "StopInstances",
    "awsRegion": "us-east-2",
    "sourceIPAddress": "205.251.233.176",
    "userAgent" : "ec2-api-tools 1.6.12.2",
    "requestParameters": {
        "instancesSet": {"items": [{"instanceId": "i-ebeaf9e2"}]},
        "force": false
    },
    "responseElements" : {"instancesSet": {"items": [{
        "instanceId": "i-ebeaf9e2",
        "currentState": {
               "code": 64,
               "name": "stopping"
        },
```

* An AWS ldentity Access Management (AM) user, Alice, stopped an Amazon EC2 instance unsuccessfully on March 6, 2023 at 21:01:59Z.
* An AWS ldentity Access Management (|AM) user, Alice, was denied access to stop an Amazon EC2 instance on March 6, 2023 at 21:01:592.
* **An AWS ldentity Access Management (IAM) user, Alice, stopped an Amazon EC2 instance successfully on March 6, 2023 at 21:01:59Z.**
* An AWS Ildentity Access Management (lIAM) user, Alice, launched an Amazon EC2 instance unsuccessfully on March 6, 2023 at 21:01:59Z.

The correct answer is **IAM user Alice stopped an Amazon EC2 instance successfully on March 6, 2023 at 21:01:59Z.**

* The "username" defines the IAM user is "Alice"
* The "eventName" defines the event that happened was "Stoplnstances"
* The "eventTime" defines this took place on March 6, 2023 at 21:01:59Z
* The "currentState" "name" defines the instance is "stopping"
* The "previousState" "name" defines that prior to this action, the instance was "running"

### 11. Which of the following features or services should a customer integrate with AWS Security Hub to monitor the access users and resources have across multiple accounts?
* Amazon Inspector
* Network Access Analyzer
* AWS Config
* **AWS ldentity Access Management (AM) Access Analyzer**

The correct answer is **IAM Access Analyzer**.
* IAM Access Analyzer helps customers streamline permissions management throughout each step of the cycle.
* AWS Config is a service that continually assesses, audits, and evaluates the configurations and relationships of resources on AWS, on premises, and on other clouds.
* Amazon Inspector is an automated vulnerability management service that continually scans AWS workloads for software vulnerabilities and unintended network access.
* Network Access Analyzer is a feature that identifies unintended network access to the customner's resources on AWS.

### 12. Which type of log for Amazon VPC traffic can be ingested into Amazon CloudWatch for monitoring?
* **Amazon VPC Flow logs**
* Only Amazon CloudWatch logs can be ingested
* AWS ldentity Access Management (|AM) Access Analyzer logs
* Amazon VPC Network Access Analyzer logs

The correct answer is **Amazon VPC Flow logs**. Amazon CloudWatch can ingest Amazon CloudWatch logs, AWS CloudTrail logs, and Amazon VPC Flow logs.

### 13. Who can create an AVWS WAF policy?
* Only AWS and AWS Marketplace sellers
* **AWS, customers, and AWS Marketplace sellers**
* **Only AWS**
* **Only customers**

The correct answer is **AWS, customers, and AWS marketplace sellers**.
AWS WAF rules are created by AWS, AWS Marketplace sellers, and customers to block and filter traffic. Amazon CloudWatch can be used in conjunction with AWS WAF to compile metrics. AWS Firewall Manager manages multiple AWS WAF deployments.

### 14. Which kind of traffic behavior does the default network access control list (network ACL) allow in Amazon VPC?
* Inbound traffic is set to ALLOW and outbound traffic is set to DENY.
* **Both inbound and outbound traffic are set to ALLOW.**
* Both inbound and outbound traffic are set to DENY.
* Inbound traffic is set to DENY and outbound traffic is set to ALLOW.

The correct answer is **Both Inbound and outbound traffic are set to ALLOW**. VPC automatically comes with a modifiable default network ACL. By default, it allows all inbound and outbound traffic. To control traffic, add ALLOW and DENY rules for specific IP addresses, protocols, and ports.

### 15. An AWS customer uses several AWS Lambda functions that access an Amazon Relational Database Service (Amazon RDS) database. Which service should they use to manage the database passwords?
* AWS Key Management Service (AwS KMS)
* AWS Certificate Manager (ACM)
* **AWS Secrets Manage**
* AWS CloudHSM

The correct answer is **AWS Secrets Manager**.
* AWS Secrets Manager provides the rotation and securing of secrets such as API keys and database credentials.
* ACM provides encryption for data that is sent through AWS websites and applications.
* AWS CloudHSM provides FIPS-validated, single-tenant-validated encryption for data that is being stored.
* AWS KMS provides FIPS-validated, multi-tenant-validated encryption for data that is being stored.

### 16. A customer needs a solution to encrypt data in transit sent while customers order products from a catalog. Which AWS service could provide the required features?  
* AWS CloudHSM
* AWS Key Management Service (AWS KMS)
* **AWS Certificate Manager (ACM)**
* AWS Secrets Manager

The correct answer is **AWS Certificate Manager (ACM)**.  
* ACM provides encryption for data that is sent through AWS websites and applications.
* AWS CloudHSM provides FIPS-validated, single-tenant-validated encryption for data that is being stored.
* AWS KMS provides FIPS-validated, multi-tenant-validated encryption for data that is being stored.
* AWS Secrets Manager provides the rotation and securing of secrets such as API keys and database credentials.

### 17. A company stores all their employee training records that are over five years old in Amazon S3 Glacier Deep Archive buckets. Prior to uploading the records, they are encrypted by a third-party software. Which kind of encryption is used with this AWS storage method?
* In use encryption
* In transit encryption
* **Client-side encryption**
* Server-side encryption

The correct answer is **Client-side encryption**.
* Client-side encryption: Data is encrypted before sending it to AWS.
* Server-side encryption: AWS encrypts data after it has been received by the service.

### 18. Which AWS website provides compliance information to customers?
* The Documentation site
* The AWS re:Post website
* **The Customer Compliance Center**
* The Architecture Center

The correct answer is **Customer Compliance Center**.
* The Customer Compliance Center contains resources to learn more about AWS compliance.
* The Architecture Center provides reference architecture examples and diagrams.
* The AWS re:Post is an AWS-managed community where experts review answers and author articles to help with AWS technical questions.
* The Documentation site provides access to technical documentation on AWS services.

### 19. How do AWS services affect the compliance requirements that a company must meet?
* Compliance requirements change depending on the product family.
* Compliance requirements are only important if the company uses specific services.
* **Compliance requirements vary from service to service.**
* There is no variation between the compliance requirements from service to service.

The correct answer is **Compliance requirements vary from service to service**. It is important to remember that AWS has a wide array of services that perform very different functions. Because of this, compliance requirements vary from service to service.

### 20. Who creates the checks used by AWS Trusted Advisor for security checks?
* AWS customers
* All of the above
* AWS Partners
* **AWS security experts**

The correct answer is **AWS security experts**.

For security, AWS Trusted Advisor can help improve the security of an AWS environment by suggesting foundational security best practices curated by security experts.

### 21. Which AWS service or resource can be used to analyze network access to determine if there are unintended resource exposures?
* AWS WAF
* AWS Firewall Manager
* **Amazon VPC Network Access Analyzer**
* Amazon Route 53 Readiness Check

The correct answer is **Amazon VPC Network Access Analyzer**.

* Amazon VPC Network Access Analyzer is a resource within Amazon VPC that identifies unintended network access to resources on AWS.
* AWS Firewall Manager provides a security management service that customers use to centrally configure and manage firewall rules across their accounts and applications in AWS Organizations.
* AWS Web Application Firewall is a web application firewall that helps protect apps and APIs against bots and exploits that consume resources, skew metrics, or cause downtime.
* With Amazon Route 53 Readiness Check, customer can check the resources in their applications for readiness to fail over.

### 22. What is an example of a process-based vulnerability?
* An unpatched operating system
* Poorly configured firewalls
* **A weak password policy**
* Retaining outdated runtimes

The correct answer is **A weak password policy**.

* Retaining outdated runtimes is an example of a deprecation vulnerability.
* An unpatched operating system (0S) is an example of an OS vulnerability.
* Poorly confiqured firewalls are examples of network vulnerabilities.

### 23. Which kind of incident is an example of resources with overly permissive access control permissions?
* Unauthorized resources
* Unauthorized access
* **Excessive permissions**
* Privilege escalations

The correct answer is **Excessive permissions**.

* Excessive permissions are when resources have overly permissive access control mechanisms or permissions.
* Privilege escalation is when a resource or person attempts to gain elevated access to resources that are normally protected from an application or user or attempts to gain access to the system or network for an extended period of time.
* Unauthorized access is when a resource or person attempts to access resources through an IP address, user, or system, that is unauthorized.
* Unauthorized resources are when resources created in the environment are unauthorized or unexpected.

### 24. What are some examples of incident response automation in AWS? (Select TW0.)
* Using tags and resource groups to organize and regularly patch Amazon EC2 instances with Patch Manager
* Defining an AWS CloudFormation template to deploy production infrastructure reliably and consistently
* Using the AWS CLI to update resource configurations
* **Creating rules within AWS Config for automatic remediation of non-compliant resources using AWS Systems Manager within a single AWS account**
* **Creating an AWS Lambda function that is activated by an Amazon EventBridge rule, for isolatinga potentially compromised instance by changing the security groups associated with the instance**

The correct answers are **Creating rules within AWS Config for automatic remediation of non-compliant resources using AWS Systems Manager within a single AWS account** and **Creating a Lambda function that is triggered by an Amazon EventBridge rule, for isolating a potentially compromised instance by changing the security groups associated with the instance**.

* Using tags and resource groups to organize and regularly patch EC2 instances is a preventive security control.
* Using AWS CloudFormation templates and infrastructure as code (IaC) helps to maintain security compliance and ensures resources are consistently deployed.
* Using the AWS CLI to update resource configurations is a manual task, this is not an example of incident response automation.

### 25. To help with an incident response investigation, a security team created Amazon Elastic Block Store (Amazon EBS) snapshots of several Amazon EBS data volumes. How will they be accessed after the snapshots are created?
* **They will be accessed from Amazon EC2 instances.**
* They will be accessed from Amazon Elastic File System (Amazon EFS) mounts.
* They will be accessed from Amazon S3 buckets.
* They will be accessed from Amazon Elastic Container Service (Amazon ECS) containers.

The correct answer is **They will be accessed from EC2 instances**.
* Snapshots of Amazon EBS volumes are restored by launching them from Amazon EC2 instances.
* Amazon EFS mounts are the targets for Amazon EFS, which is a serverless, shared file system.
* Amazon S3 buckets provide object storage but no launching mechanism.
* Amazon ECS is a fully managed container orchestration service that simplifies the deployment, management, and scaling of containerized applications.
