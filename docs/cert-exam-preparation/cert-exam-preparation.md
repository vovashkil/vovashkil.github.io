###### back to repo's main [README.md](../../README.md)
# AWS Certification Exam Preparation
## AWS Certified Solutions Architect – Professional (SAP-C02)
### Domains
1. Design solutions for organizational complexity
2. Design for new solutions
3. Continuous improvement for existing solutions
4. Accelerate workload migration and modernization

### AWS training recommendations
* [AWS  Well-Architected Foundations](https://explore.skillbuilder.aws/learn/course/external/view/elearning/108/aws-well-architected-foundations)
* [Approach  to Mainframe Migration and Modernization](https://explore.skillbuilder.aws/learn/course/external/view/elearning/14759/approach-to-mainframe-migration-and-modernization)
* [AWS  Networking Practical Approaches](https://explore.skillbuilder.aws/learn/course/external/view/elearning/10448/aws-networking-practical-approaches)
* [AWS  Migration Hub Primer](https://explore.skillbuilder.aws/learn/course/external/view/elearning/14473/aws-migration-hub-primer)
* [Digital Classroom - Architecting on AWS](https://explore.skillbuilder.aws/learn/course/external/view/elearning/17204/digital-classroom-architecting-on-aws)
* [Digital Classroom - Cloud Operations on AWS](https://explore.skillbuilder.aws/learn/course/external/view/elearning/17207/digital-classroom-cloud-operations-on-aws)

Gain hands-on experience with this self-paced lab.
* [Discovering Applications to Migrate by Using AWS Application Discovery Services (ADS)](https://explore.skillbuilder.aws/learn/course/external/view/elearning/14947/discovering-applications-to-migrate-by-using-aws-application-discovery-services-ads)

### Whitepapers
* [Security best practices for AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/best-practices.html)
* [Encryption of Data at Rest](https://docs.aws.amazon.com/whitepapers/latest/efs-encrypted-file-systems/encryption-of-data-at-rest.html)
* [Web Application Hosting in the AWS Cloud](https://docs.aws.amazon.com/whitepapers/latest/web-application-hosting-best-practices/welcome.html)
* [Practicing Continuous Integration and Continuous Delivery on AWS](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/welcome.html)
* [Microservices architecture on AWS](https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/simple-microservices-architecture-on-aws.html)
* [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)
* [Using Amazon Web Services for Disaster Recovery](https://d1.awsstatic.com/whitepapers/aws-disaster-recovery.121b65092f931567af5370b47dd12cb18866089c.pdf)
* [AWS Architecture Center architecture whitepapers](https://aws.amazon.com/whitepapers/?achp_navlib6&whitepapers-main.sort-by=item.additionalFields.sortDate&whitepapers-main.sort-order=desc&awsf.whitepapers-content-type=*all&awsf.whitepapers-global-methodology=*all&awsf.whitepapers-tech-category=*all&awsf.whitepapers-industries=*all&awsf.whitepapers-business-category=*all)
* [Fault-Tolerant Components on AWS](https://d1.awsstatic.com/whitepapers/aws-building-fault-tolerant-applications.pdf)
* [AWS Security Best Practices](https://d1.awsstatic.com/whitepapers/Security/AWS_Security_Best_Practices.pdf)
* [AWS Storage Services Overview](https://d1.awsstatic.com/whitepapers/AWS%20Storage%20Services%20Whitepaper-v9.pdf)
* [Amazon Web Services: Overview of Security Processes](https://d1.awsstatic.com/whitepapers/Security/AWS_Security_Whitepaper.pdf)
* [An Overview of the AWS Cloud Adoption Framework](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/welcome.html)

### Well-Architected Framework
#### Operational Excellence Pillar
Operational excellence is the ability to support development and run workloads effectively, gain insight into operations, and continuously improve supporting processes and procedures to deliver business value.

##### Operational excellence design principles
* Perform operations as code.
* Make frequent, small, reversible changes.
* Refine operations procedures frequently.
* Anticipate failure.
* Learn from all operational failures.

##### Operational excellence best practice areas
* Organization
* Prepare
* Operate
* Evolve

#### Security Pillar
The security pillar encompasses the ability to protect data, systems, and assets on the cloud. To operate your workload securely, you must apply overarching best practices to every area of security. 

##### Security Design Principles
* Implement a strong identity foundation.
* Turn on traceability.
* Apply security at all layers.
* Automate security best practices.
* Protect data in transit and at rest.
* Keep people away from data.
* Prepare for security events.

##### Security best practice areas
* Security foundations
* Identity and access management
* Detection
* infrastructure protection
* Data protection
* Incident response
* Application security

#### Reliability Pillar
The ability of a workload to perform its required function correctly and consistently over an expected period of time. 

##### Reliability design principles
* Automatically recover from failure.
* Test recovery procedures.
* Scale horizontally to increase aggregate workload ability.
* Stop guessing capacity.
* Manage change in automation.

##### Reliability best practice areas
* Foundations
* Workload architecture
* Change management
* Failure management

#### Performance efficiency
The performance efficiency pillar focuses on the efficient use of computing resources to meet requirements, and how to maintain efficiency as demand changes and technologies evolve.

##### Performance efficiency design principles
* Democratize advanced technologies.
* Go global in minutes.
* Use serverless architectures.
* Experiment more often.
* Consider mechanical sympathy.

##### Performance efficiency best practices areas
* Selection
* Review
* Monitoring
* Trade-offs

##### Assessment
###### What are the areas of focus for performance efficiency pillar questions? (Select THREE.)
* Selecting the right resource types for compute, storage, database, and networking.
* Reviewing your selection as AWS continues to innovate with new resource types and features.
* Making architectural trade-offs to maximize your performance efficiency.

###### What is an example of a performance efficiency best practice in compute, storage, database, and networking?
* Select the appropriate resource type.

###### What is an example of a performance efficiency best practice in trade-offs?
* Position resources or cached data closer to end users.

#### Cost optimization
A cost-optimized workload fully utilizes all resources, achieves an outcome at the lowest possible price point, and meets your functional requirements.

##### Cost optimization design principles
* Practice Cloud Financial Management.
* Adopt a consumption model.
* Measure overall efficiency.
* Stop spending money on undifferentiated heavy-lifting.
* Analyze and attribute expenditure.

##### Cost Optimization Best Practice Areas
* Practice Cloud Financial Management.
* Expenditure and usage awareness.
* Cost-effective resources.
* Management of demand and supply resources.
* Optimization over time.

##### Assessment
###### Which is an area of focus for the cost optimization pillar?
* Use cost-efficient resources.

Wrong answers:
* Use serverless computing.
* Control and understand where your money is being spent by conducting regular testing.
* Use trade-offs.

###### Which is a cost optimization best practice in expenditure awareness?
* Use AWS Cost Explorer to categorize and track AWS costs.

Wrong answers:
* Manage access by creating user policies.
* Have a third party review the spend.
* Use spend manager to reduce data transfer costs.

#### Sustainability
When building cloud workloads, the practice of sustainability is understanding the impacts of the services used, quantifying impacts through the entire workload lifecycle, and applying design principles and best practices to reduce these impacts. This module focuses on environmental impacts, especially energy consumption and efficiency, since they are important levers for architects to inform direct action to reduce resource usage.

##### Sustainability design principles
* Understand your impact
* Establish sustainability goals
* Maximize utilization
* Anticipate and adopt new, more efficient hardware and software offerings
* Use managed services
* Reduce the downstream impact of your cloud workloads

##### Sustainability best practice areas
* Region selection
* Alignment to demand
* Software and architecture patterns
* Data patterns
* Hardware and services
* Process and culture

##### Assessment
###### Which of the following are drivers for considering sustainability when improving architectures? (Select THREE.)
* Customer demand
* Performance
* Government regulations

Wrong answers:
* Competitive positioning
* Government regulations
* Cost savings
* Security

###### Which of the following is a Well-Architected sustainability design principle?
* Understand your impact

Wrong answers:
* Process and Culture
* Regional Selection
* Review cost and usage reports regularly

###### Which of the following are best practices when considering hardware patterns for sustainability? (Select THREE.)
* Use managed services.
* Use instance types with the least impact.
* Use the minimum amount of hardware to meet your needs.

Wrong answers:
* Use instance types with the lowest cost.
* Use policies to manage the lifecycle of your datasets.
* Optimize areas of code that consume the most resources.

#### AWS Well-Architected Framework Course Assessment
##### Why is the cost optimization pillar important?
* A cost-optimized workload fully utilizes all resources, achieves an outcome at the lowest possible price point, and meets your functional requirements.

Wrong answers
* It helps a company optimize for higher performance and put in place monitoring to help ensure that the architecture performance does not degrade over time.
* It is important to use computing resources efficiently to meet requirements, maintaining efficiency as demand changes and technologies evolve.
* It is important to protect data, systems, and assets to take advantage of cloud technologies that can improve security.

##### Which are design principles for the cost optimization pillar? (Select THREE.)
* Implement Cloud Financial Management (CFM).
* Analyze and attribute expenditure.
* Adopt a consumption model.

Wrong answers:
* Implement a strong identity foundation.
* Use serverless architectures.
* Apply security on all layers.


##### Which are design principles for the reliability pillar? (Select THREE.)
* Scale horizontally to increase aggregate workload availability.
* Stop guessing capacity.
* Automatically recover from failure.

Wrong answers:
* Democratize advanced technologies.
* Adopt a consumption model.
* Measure overall efficiency.

##### After using the AWS Well-Architected Tool in the review, the Improvement Plan identifies high-risk issues and medium-risk issues. What is a high-risk issue?
An architectural and operational choice that AWS has found could have a significant negative impact to a business, affecting organizational operations, assets, and individuals.

Wrong answers:
* High potential for failed architecture.
* An issue that might negatively impact business but is something minor that does not require immediate attention.
* An architectural issue that needs to be dealt with immediately and is considered an emergency.

##### All key stakeholders are in the room for an AWS Well-Architected Framework Review. What are the next steps the team should take? (Select THREE.)
* Realign on the purpose of doing the review with a blame-free approach.
* Choose a few key business goals that the team should meet from the architecture before doing the review.
* Ensure that they have the tools to encourage a brainstorming session and a dedicated place to document questions or action items.

Wrong answers:
* Ensure that there are no distractions in the room, such as notepads, whiteboards, and so on.
* Start planning logistics like ordering lunch so that stakeholders become more engaged.
* Make a list of everything that could be wrong with the proposed architecture.

##### What is the definition of the reliability pillar?
* The ability of a workload to perform its required function correctly and consistently over an expected period of time.

Wrong answers:
* Reliability has specific patterns and best practices to adopt to meet sustainability goals, anti-patterns to avoid, and terminology to help communicate with others. The pillar will also help identify targets to reduce impact and identify organizational structures necessary for long-term success.
* The optimal solution for a particular workload varies, and solutions often combine multiple approaches.
* Building and operating cost-efficient workloads helps achieve business outcomes at the lowest price point. It minimizes wasteful architecture rework and supports greater investment in new business opportunities or technology.

##### If a team thinks that they do not have the right resources to help remediate the issues identified in the AWS Well-Architected Framework Review, what are the options available for help? (Select TWO.)
* Contact an AWS account manager for additional support and guidance.
* Hire a talent agency to create a new job posting. If the team does not have an AWS account manager, or the expertise or time, they can reach out to AWS Well-Architected Partner Program members.

Wrong answers:
* Pause the launch plan until they have resources available.
* Continue the product launch, and conduct the review later.
* Contact human resources.

##### Why is the security pillar important?
* To operate your workload securely, you must apply overarching best practices to every area of security.

Wrong answers:
* Building and operating cost-efficient workloads helps achieve business outcomes at the lowest price point. It minimizes wasteful architecture rework and supports greater investment in new business opportunities or technology.
* It measures the business output of the workload and the costs associated with delivering it. Use this measure to know the gains realized from increasing output or functionality and reducing costs.
* Cloud workloads are inherently more sustainable than typical on-premises alternatives because they use more efficient technology and only use resources when needed. However, companies can modify workloads to reduce impact even further.

##### What is the definition of the performance efficiency pillar?
* Performance efficiency focuses on the efficient use of computing resources to meet requirements, and how to maintain efficiency as demand changes and technologies evolve.

Wrong answers:
* Performance efficiency measures the business output of the workload and the costs associated with delivering it. Use this measure to know the gains realized from increasing output or functionality and reducing costs.
* Performance efficiency includes the ability to run systems to deliver business value at the lowest price point.
* Performance efficiency is the ability of a workload to perform its intended function correctly and consistently when it is expected to.

##### What should a team member do before starting the AWS Well-Architected Framework Review? (Select TWO.)
* Reach out to stakeholders who should be involved in the meeting. Send information on the Well-Architected Framework and explain the benefits of performing a Well-Architected Framework Review, and then schedule it.
* Read up on the Well-Architected Framework and how to do a review.

Wrong answers:
* Immediately schedule a meeting with their engineering team.
* Schedule a 30-minute Well-Architected Framework Review meeting, and plan to explain what Well-Architected is for 5 minutes before the review.
* Make a list of everything that is wrong with their proposed architecture.

##### What is the definition of the operational excellence pillar?
* The ability to support development and run workloads effectively, gain insight into their operations, and continuously improve supporting processes and procedures to deliver business value.

Wrong answers:
* Operational excellence is the ability to protect data, networks, and databases against risk.
* Operational excellence is the ability to protect data, systems, and assets to take advantage of cloud technologies.
* Operational excellence helps a company optimize for higher performance and put in place monitoring that ensures that the performance of the architecture does not degrade over time.

##### A solutions architect intends to conduct an AWS Well-Architected Framework Review for a workload that is scheduled to go live soon. A key stakeholder emails to explain that the team is too busy to dedicate time for the review because they are working on a tight timeline before the launch. Which is the best response?
* Explain that it is better to understand potential issues before the launch. Even though they may not be able to implement all changes before going live, it will help the team create an action plan for the future.

Wrong answers:
* Explain that a review should be done in advance to provide time to identify and address issues for a smooth launch. This review will identify any potential risks that may happen during launch. If there are too many identified, the team can opt to push back the launch date.
* Push the review until after the product goes live so the team gets more time to engage.
* Escalate this to a manager to get more resources assigned to the project.

##### Which are design principles for the performance efficiency pillar? (Select THREE.)
* Experiment more often.
* Democratize advanced technologies.
* Use serverless architectures.

Wrong answers:
* Stop guessing capacity.
* Provide traceability.
* Test the recovery procedure.

##### A team finds a few high-risk issues and medium-risk issues identified in their Improvement Plan. What should they do with this information?
* Create a chart or list of all high-risk issues and medium-risk issues to help prioritize a starting point.

Wrong answers:
* Send a company-wide email explaining that they need all hands on deck to fix the identified issues.
* Fire the engineer who built part of the workload that has a high-risk issue.
* Pause the entire launch plan.

### Design solutions for organizational complexity
### Design for new solutions
### Continuous improvement for existing solutions
### Accelerate workload migration and modernization

