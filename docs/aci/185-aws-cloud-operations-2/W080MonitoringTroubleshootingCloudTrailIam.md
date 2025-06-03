# Week 8: Monitoring and Troubleshooting: Troubleshooting with AWS CloudTrail and IAM

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to [AWS Cloud Operations 2](./aws-cloud-operations-2.md)
* back to repo's main [README.md](../../../README.md)

## Troubleshooting Methodology

### Pre-assessment

#### Why is a structured approach to troubleshooting essential?

* It yields more predictable results and facilitates continuity.

Wrong answers:

* It ensures that every problem is solved in the same way.
* It provides for creative and impromptu problem solving.
* It focuses solely on theoretical causes.

##### Explanation

A structured approach ensures consistency in problem-solving. When everyone follows the same systematic steps, it becomes more efficient to track progress, hand off tasks, and maintain continuity. Predictable results are crucial for efficient troubleshooting.

The other options are incorrect because of the following:

* Although consistency is important, the primary benefit is predictability, not rigid adherence to a single-solution method.
* Creativity is valuable, but structured methods provide a foundation for effective troubleshooting.
* Structured approaches consider practical causes, not just theory.

#### What is the key benefit of using a systematic troubleshooting method?

* It narrows down possible causes systematically.

Wrong answers:

* It speeds up the resolution process.
* It ensures that all team members are involved.
* It eliminates the need for documentation.

##### Explanation

Systematic methods help eliminate potential causes step by step. By narrowing down the possibilities, developers can focus on relevant areas and reach a resolution faster.

The other options are incorrect because of the following:

* Although systematic methods can lead to faster resolution, the primary benefit is narrowing down causes.
* Involving team members is important, but it’s not the primary benefit of systematic troubleshooting.
* Documentation remains essential even with systematic methods.

#### What should be the first step in the troubleshooting process?

* Collect relevant information.

Wrong answers:

* Apply the chosen solution.
* Evaluate the outcomes.
* Document the entire process.

##### Explanation

Collecting relevant information is important because it provides the foundation for effective troubleshooting. Understanding symptoms, context, and potential causes helps developers to proceed systematically and efficiently. After collecting the necessary information, developers can move to identifying and addressing the root cause of the issue. A well-structured troubleshooting process starts with thorough data collection.

The other options are incorrect because of the following:

* Applying a solution comes after identifying the root cause of the problem. Jumping straight to solution without understanding the issue can lead to ineffective troubleshooting.
* Evaluating outcomes occurs after implementing a solution to verify its effectiveness. It’s not the first step.
* Although documentation is essential, it typically happens after the troubleshooting process. It helps maintain records and aids future reference but is not the initial step.

### Troubleshooting Methodology and Structured Approach

#### Troubleshooting methodology

1. Troubleshooting starts with identifying the problem.

    You begin by gathering information from users or from system alerts to begin to understand the nature of the issue. You define symptoms, error messages, and any recent changes to the system.

2. Isolate the cause.

    Try to narrow down the possible causes by testing components of the system. This might involve checking software configurations, network connections, and user accounts.

3. Develop hypotheses.

    Based on the gathered information, you formulate one or more hypotheses about the root cause of the problem. You should prioritize the hypotheses based on likelihood and potential impact.

4. These hypotheses guide your investigation, as you test and experiment to confirm or eliminate each one. This could involve running diagnostic tools, analyzing log files, or simulating user actions to reproduce the issue.

5. Identify the cause. Implement the necessary changes or fixes to resolve the problem. This might involve applying patches, reconfiguring settings, or replacing faulty hardware.

6. Verify that your solution resolves the issue and restore the system to normal operation. You also test functionality and monitor for any recurring problems.

7. Document your findings, the steps you took, and the implementation solution. Sharing your insights helps others and improves the troubleshooting process.

Troubleshooting isn’t just about fixing problems; it’s also about learning from them. Each issue you solve adds to your knowledge and experience, and it makes you better equipped to handle future challenges.

By following a structured troubleshooting methodology, you can effectively identify and resolve system issues. This minimizes downtime and helps ensure that your systems run smoothly.

#### Breakdown of key steps

The following breakdown provides a detailed overview of the key steps involved in a general troubleshooting methodology. By understanding and applying these steps, you can effectively diagnose and resolve a wide range of problems.

1. **Identifying the problem**

    The first step you need to remember in any troubleshooting process is to understand the problem. So, what does this involve?

    This involves gathering information about the issue and understanding the symptoms.

    For example, you encounter a problem where the web application is not loading for users. This might be identified by user reports or through monitoring tools that indicate the application is not responding.

2. **Isolating the cause**

    After you identify the problem, you move on to isolate the cause. This involves identifying the specific component or system that is causing the problem. This might involve checking different components, such as the application server, database server, network, or even the application code itself.

    For example, you might check the server logs, database logs, and network traffic to determine if there are any anomalies.

3. **Developing the hypothesis**

    Based on the information collected in the previous steps, you develop a hypothesis about what might be causing the problem.

    For example, if the server logs indicate that the server is running out of memory, you might hypothesize that the server needs more memory to handle the load.

4. **Testing the hypothesis**

    This step involves creating and running a test plan to confirm or disprove your hypothesis.

    For example, if the hypothesis is that the server is running out of memory, you might monitor the server's memory usage in real time by using cloud monitoring tools, such as Amazon CloudWatch.

    You might also simulate a high load situation by increasing the traffic to the application with load testing tools and then observe how the memory usage changes. If the memory usage consistently reaches the limit during the high load, it confirms the hypothesis.

5. **Planning and implementing the solution**

    Before implementing the solution, it's important to have a clear plan of action. You should outline the steps to implement the solution, identify potential risks and their mitigation strategies, and prepare a rollback plan if the solution doesn't work as expected.

    For example, the plan might include the following:

    * **Identifying the solution**: You research different server sizes and their memory capacities. This might involve comparing different cloud service providers or different server configurations within the same provider.
    * **Acquiring necessary approvals and resources**: Depending on the organization, this might involve getting budget approval for the additional cost. It might also involve getting approval from the IT department for the potential downtime during the server resizing.
    * **Preparing for the implementation**: You then schedule a maintenance window during off-peak hours to minimize the impact on users. You inform related personnel about the planned downtime and the expected improvements after the solution is implemented.
    * **Assessing potential risks and mitigation**: You identify potential risks, such as data loss or extended downtime, and plan for their mitigation. This might involve backing up the server or having a rollback plan to revert to the original server size in case of issues.
    * **Implementing the solution**: After the plan is in place, you implement the solution. This involves resizing the server to a larger size with more memory. Most cloud service providers provide for resizing servers without data loss, but you should have a backup just in case.

6. **Verifying the solution and system functionality**

    After you implement the solution, it's important to verify that the solution resolved the problem and the system is functioning correctly.

    For example, you might monitor the server's memory usage under load testing. This ensures that the server no longer runs out of memory and the web application loads for users.

7. **Documenting the findings**

    The final step in the troubleshooting process is to document the findings. It involves recording all the details about the problem, the steps you took to diagnose and resolve it, and the final outcome. This is an important step because it helps with the following:

    * **Knowledge sharing**: You can share the document with other team members. This enhances the collective knowledge of the team. This is particularly useful in larger organizations where similar problems might occur in different departments or locations.
    * **Future reference**: If the same problem occurs in the future, this document can serve as a valuable reference. It can help diagnose and resolve the problem efficiently. As a result, you can save time and resources.

    In the example of the cloud-based web application, the document might include the following:

    * **A detailed description of the initial problem**: The web application is not loading for users.
    * **The steps taken to diagnose the problem**: The developer checks server logs, database logs, and network traffic.
    * **The hypothesis developed**: The server is running out of memory.
    * **The tests conducted to confirm the hypothesis**: The developer monitors the server's memory usage under load testing.
    * **The solution implemented**: The developer upgrades the server to a larger size with more memory.
    * **The outcome after implementing the solution**: The web application is loading properly for users.

    You can store this document in a centralized knowledge base or ticketing system for convenient access and reference. Remember, the goal of the document is not only to record what was done but also to provide valuable insights for future troubleshooting efforts.

#### Benefits of a structured troubleshooting approach

A structured troubleshooting approach is important and more beneficial than an ad-hoc approach for the following reasons:

* **Efficiency**: With a structured approach, you can systematically narrow down the cause of a problem, which saves time and resources. In contrast, an ad-hoc approach might involve trying random solutions until something works. This can be time-consuming and inefficient.
* **Repeatability**: With a structured approach, you can follow the same steps each time a similar problem occurs. This makes it convenient for different people to troubleshoot the same issue and ensures consistency in problem-solving. An ad-hoc approach might not be repeatable or consistent.
* **Knowledge building**: A structured approach involves documenting each step of the troubleshooting process. This helps teams learn from past experiences. An ad-hoc approach might not involve documentation, which can lead to loss of knowledge.
* **Risk management**: A structured approach often involves steps for risk assessment and mitigation. This ensures that the troubleshooting process doesn't inadvertently cause additional problems. An ad-hoc approach might not consider potential risks, which might lead to future issues.
* **Problem prevention**: By following a structured troubleshooting approach, you can often identify and address underlying issues that might cause future problems. An impromptu approach might only address the immediate problem without considering underlying issues.

##### Example of a structured troubleshooting approach

Consider an example related to a company's cloud storage system. Suppose the company frequently runs out of storage space, and this causes disruption in their operations. An ad-hoc approach might involve purchasing additional storage whenever the system runs out. Although this solves the immediate problem, it doesn't prevent the issue from recurring and doesn't address the underlying cause.

A structured troubleshooting approach would involve the following:

* **Identifying the problem**: Monitoring alerts indicate that the storage capacity is reaching its limit every month, disrupting the company's workflow.
* **Isolating the cause**: You analyze storage reports and audit logs to determine that outdated files are not being archived or deleted efficiently. This leads to excessive storage usage.
* **Developing and testing a hypothesis**: You hypothesize that the storage issue is because of the absence of automated data archiving and deletion. You test this by implementing an automated system for a subset of data to determine if it resolves the problem.

The problem prevention benefit in this scenario might involve implementing a new data management policy that includes regular archiving and deletion of old, unnecessary files. This solves the immediate issue and also helps prevent the problem from recurring in the future.

Additionally, the company might implement a monitoring system to track storage usage and alert the team when usage approaches the limit. With this proactive method, the team can address the issue before it becomes a problem, so they can prevent disruptions in operations.

### Using Troubleshooting Methodology in Cloud Infrastructure

In this section, you review how to use a troubleshooting methodology to diagnose three common issues related to cloud infrastructure. By addressing these common issues with a systematic troubleshooting approach, organizations can minimize disruptions, enhance security posture, and optimize cloud spending to achieve their business objectives effectively.

#### Downtime

Imagine that a company is running a critical web application on a cloud platform. Users suddenly report that they are unable to access the application, resulting in a loss of revenue and productivity. How can you troubleshoot this issue?

##### Identify the problem

Users report that they can't access the critical web application.

##### Isolate the cause

Perform the following steps:

* **Check service status**: Verify if the cloud provider has reported any service disruptions or outages on their status page.
* **Review monitoring alerts**: Check for any alerts or notifications from your monitoring system indicating issues with the infrastructure components, such as servers, databases, or networking.

##### Develop a hypothesis

The application might be experiencing issues because of a server outage or network connectivity issue.

##### Test the hypothesis

Perform the following steps:

* **Check server health**: Verify if the servers hosting the application are responsive and functioning properly.
* **Test network connectivity**: Ensure that there are no network issues preventing users from accessing the application. For example, you can use the ping command to check if the server is reachable. You can use the traceroute command to identify the network path and determine where the packets are getting lost.

##### Plan and implement the solution

If the servers are down, you can restart them. If the issue is related to resource constraints, consider scaling up or adding additional resources to handle the increased demand. You can also use a load balancer to distribute traffic across multiple servers. If one server fails, traffic is automatically redirected to operational servers.

If there are network issues, troubleshoot and resolve connectivity issues. Depending on the results of your network diagnostics, you might need to update security group rules to allow traffic or adjust network access control lists (network ACLs). You can also use a content delivery network (CDN) to cache and deliver content from servers located around the world. This helps users access your application even if there is a network issue at one location.

##### Verify the solution and system functionality

Confirm that users can access the application without any further issues.

##### Document the findings

Document the root cause of the downtime, actions taken to resolve it, and any preventive measures implemented to avoid similar issues in the future.

#### Security breach

Imagine a company database that contains sensitive customer information is compromised, leading to a data breach. Customer data is leaked online, resulting in reputational damage and potential legal consequences. How can you troubleshoot this issue?

##### Identify the problem

Sensitive customer data has been compromised, leading to a data breach. You should immediately isolate affected systems and contain the spread of the breach to prevent further unauthorized access.

##### Isolate the cause

Investigate how the breach occurred, such as through vulnerabilities in the application, misconfigured security settings, or compromised credentials.

Analyze system logs and use intrusion detection tools to identify the source and method of the breach. Determine which vulnerabilities were exploited and which systems or data were affected.

##### Develop a hypothesis

The breach might have occurred because of unpatched software vulnerabilities in the application. 

##### Test the hypothesis

Perform the following steps:

* **Conduct a security assessment**: Scan the application and infrastructure for known vulnerabilities and security weaknesses.
* **Review access logs**: Check for any suspicious activity indicating unauthorized access to the system.

##### Plan and implement the solution

Perform the following steps:

* **Patch vulnerable software**: Apply security patches and updates to address known vulnerabilities in software and infrastructure components.
* **Strengthen access controls**: Review and strengthen access controls, authentication mechanisms, and least privilege principles to limit access to sensitive data and resources.
* **Implement encryption**: Encrypt sensitive data at rest and in transit to protect it from unauthorized access, even if perimeter defenses are breached.

##### Verify the solution and system functionality

Monitor system logs and security alerts for any signs of continued unauthorized access.

##### Document the findings

Document the root cause of the security breach, actions taken to remediate it, and any additional security measures implemented to prevent future breaches. This might include implementing robust logging, monitoring, and auditing mechanisms to detect and respond to security incidents in real time.

#### Cost overruns

Imagine a company migrates its infrastructure to the cloud to achieve cost savings. However, the company experiences unexpectedly high bills because of inefficient resource usage and lack of cost management controls. How can you troubleshoot this issue?

##### Identify the problem

Cloud spending is higher than expected, which leads to budget overruns.

##### Isolate the cause

Analyze cloud usage and spending patterns to identify the main cost elements, such as underused resources, data transfer fees, or premium service usage.

##### Develop a hypothesis

Cost overruns might be because of inefficient resource usage and lack of cost management controls.

##### Test the hypothesis

Perform the following steps:

* **Review resource usage**: Analyze resource usage metrics to identify opportunities for optimization.
* **Check for unused resources**: Identify and remove or delete any underused or idle resources.

##### Plan and implement the solution

Perform the following steps:

* **Rightsize resources**: Adjust resource allocations based on actual usage patterns and workload requirements.
* **Implement cost controls**: Set up budget limits, alerts, and quotas to prevent overspending.
* **Implement tagging and cost allocation**: Tag resources with meaningful metadata and implement cost allocation mechanisms to track spending by department or project for accountability and cost transparency.

##### Verify the solution and system functionality

Monitor cloud spending and compare it to the budget to ensure that costs are within acceptable limits.

##### Document the findings

Document the main cost drivers, actions taken to optimize costs, and any cost management measures implemented to maintain budget discipline.

#### Developing a Troubleshooting Plan

A troubleshooting plan details the procedures and resources required to diagnose and resolve issues in an effective and time-saving manner.

##### Scenario

Consider this scenario: You have an Amazon Elastic Compute Cloud (Amazon EC2) instance that is not accessible through Secure Shell (SSH) and the website this instance hosts is down. 

Think about how you would develop a troubleshooting plan using the troubleshooting methodology. These steps include the following:

1. Identify the problem.
2. Isolate the cause.
3. Develop a hypothesis.
4. Test the hypothesis.
5. Plan and implement the solution.
6. Verify the solution and system functionality.
7. Document the findings.

##### Example response

###### Step 1: Identify the problem

Users report they can't access an Amazon EC2 instance through SSH and the website it hosts is down. The error message might be Connection time out or Connection refused.

###### Step 2: Isolate the cause

Isolate whether the issue is with the EC2 instance itself, the network, or the application running on the instance. You can use CloudWatch to monitor your resources and applications. It collects data in the form of logs, metrics, and events. CloudWatch provides you with a unified view of AWS resources.

###### Step 3: Develop a hypothesis

You will establish a theory of probable cause. Possible causes could be the following:

* The EC2 instance is not running.
* The security group rules are not configured correctly.
* The SSH keys are incorrect.
* The web server software (such as Apache web server) is not running.

###### Step 4: Test the hypothesis

Now, you can test the theory to determine the cause. To learn more, expand each of the following categories:

* **Check the instance status**

  You can use the following general steps to check the instance status:

  * Log in to the AWS Management Console.
  * Navigate to the Amazon EC2 dashboard.
  * Check the status of the instance. It should be in the **Running state**.

* **Verify the security group rules**

  You can use the following steps to check the security group rules:

  * In the Amazon EC2 dashboard, navigate to **Security Groups** under **Network & Security**.
  * Select the security group associated with your instance and check the inbound rules. There should be rules allowing inbound SSH traffic (port 22) and HTTP/HTTPS traffic (port 80 and port 443) from your IP address or from everywhere (0.0.0.0/0).

* **Confirm the correct SSH private key file**

  Ensure you are using the correct private key file (.pem) that corresponds to the key pair selected when the instance was launched.

* **Check the web server logs**

  If you have access to the instance, check the logs of web server software (such as Apache). The location of these logs can vary, but the common location is **/var/log/apache2/** for Apache.

###### Step 5: Establish a plan of action and implement the solution

The plan of action based on the theory you tested in step 4 could include the following:

* **If the instance is not running**: Navigate to the Amazon EC2 dashboard, select the **instance**, and choose **Instance state**, **Start instance**.
* **If the security group rules are incorrect**: Navigate to **Security Groups**, select the security group, choose **Edit inbound rules**, and add rules to allow SSH and HTTP/HTTPS traffic.
* **If the wrong SSH key is being used**: You will need to find the correct private key file. If you lost your SSH key pair, you can replace it with different methods. For example, by editing user data or using AWS Systems Manager to recover your lost key pair. For more information, see [How can I connect to my Amazon EC2 instance if I lost my SSH key pair after its initial launch?](https://repost.aws/knowledge-center/user-data-replace-key-pair-ec2)
* **If the web server software is not running**: If you have access to the instance, you can try starting the web server software. For example, if the instance is using Apache as the server software, the start web server command could be ```sudo service apache start```.

If the issue still isn't resolved after implementing the solution, it's time to escalate. This might involve contacting AWS Support, reaching out to a more experienced team member, or seeking help from online communities. 

###### Step 6: Verify full system functionality

After implementing the solution, try to connect to the EC2 instance through SSH again and check if the website it hosts is accessible.

* **Connect to the Amazon EC2 instance through SSH**

  You can connect to your EC2 instance by using SSH from your local machine. The following is an example command.

  ```ssh -i /path/to/your/key.pem ec2-user@ec2-xx-xx-xx-xx.compute-1.amazonaws.com```

  In this command:

  * ```/path/to/your/key.pem``` is the path to your private key file.
  * **ec2-user** is the default username for Amazon Linux AMI. If you are using a different Amazon Machine Image (AMI), the username might be different.
  * **ec2-xx-xx-xx-xx.compute-1.amazonaws.com** is the public DNS name of your EC2 instance. You can find it in the Amazon EC2 dashboard in the AWS Management Console.

  If the SSH connection is successful, you should be logged into your EC2 instance.

* **Check if the web server is running**

  After you are logged into your EC2 instance, you can check if the web server software such as Apache is running. The following is an example command for Apache:

  ```sudo service apache2 status```

  If the web server is running, you should see a message indicating that it's active (running).

* **Check if the website is accessible**

  Finally, you can check if the website hosted by the EC2 instance is accessible. You can open a web browser on your local machine and navigate to the public DNS name of your EC2 instance. The public DNS name is the same one used in the SSH command. You should be able to see your website.

If you can use SSH to connect to the EC2 instance, and the web server is running with the website accessible, then the problem is solved. If not, you might need to revisit the previous steps or escalate the issue.

###### Step 7: Document the findings, actions, outcomes, and lessons learned

The final step of the troubleshooting plan is to document the issue, the steps taken to resolve it, and the final outcome. Any lessons learned should also be documented for future reference. With this documentation, you can review and improve the process of developing and using the troubleshooting plan.

This involves evaluating the effectiveness, efficiency, time, cost, quality, and safety of the process. You can also identify the strengths and weaknesses of the process, such as tools, knowledge, or techniques used. In addition, seeking feedback and suggestions from those involved or affected by the process can be beneficial.

By doing so, you can use the lessons learned and best practices to enhance future troubleshooting plans and optimize the overall process.

#### Additional Sources

* [Troubleshooting connecting to your instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/TroubleshootingInstancesConnecting.html)
* [Troubleshooting resources](https://docs.aws.amazon.com/awssupport/latest/user/troubleshooting.html)

### Knowledge Check

#### What should be the first step when troubleshooting issues in a cloud application? 

* Review monitoring dashboards.

Wrong answers:

* Check application logs.
* Restart the application.
* Contact AWS Support.

##### Explanation

The first step when troubleshooting cloud application issues should be to review monitoring dashboards and metrics. Cloud platforms provide monitoring dashboards that give an overview of resource utilization, request rates, and errors. Reviewing the dashboards will help identify if there are any anomalies or spikes in errors that could be causing problems.

The other options are incorrect because of the following:

* Checking application logs is not the best first step. Although logs provide detailed tracebacks, they take time to sift through. It is better to start with a high-level view from monitoring.
* Restarting the application might help resolve transient issues, but restarting the application without investigating first can make troubleshooting more difficult.
* Contacting support prematurely can slow down troubleshooting. It should only be done if the issue cannot be diagnosed or resolved with available troubleshooting tools.

#### A developer is troubleshooting a network issue reported by a user. The user complains that they cannot access the company’s internal server. The developer has identified the problem as a network connectivity issue. What should be their next step in the troubleshooting process?

* Establish a theory of probable cause.

Wrong answers:

* Test the solution.
* Document findings.
* Escalate to higher support levels.

##### Explanation

In this scenario, after identifying and isolating the problem (network connectivity issue), the developer should establish a theory of probable cause. This involves formulating a hypothesis based on available data and researching to support their theory.

The other options are incorrect because of the following:

* Testing the solution comes after formulating the theory.
* Documenting findings is essential but not the immediate next step.
* Escalation should occur if the issue persists or requires specialized expertise.

#### A global company is having intermittent outages with its cloud-based application because of overloaded servers. Which strategy would be MOST effective in mitigating these issues?

* Use a load balancer to distribute network traffic across multiple servers.

Wrong answers:

* Implement a single robust server to handle all network traffic.
* Store all data in one central location and use advanced compression techniques for global access.
* Implement a Regional server model with each server handling traffic for its designated Region.

##### Explanation

Using a load balancer can help distribute network traffic and prevent any single server from becoming a point of failure.

The other options are incorrect because of the following:

* Although a robust server can handle significant traffic, it still presents a single point of failure. If it fails, the entire system experiences downtime.
* Storing all data in one central location can lead to high latency for users who are geographically distant from the location. It can also become a single point of failure, even with advanced compression techniques.
* Although a Regional server model can help reduce latency, it does not address the issue of a single point of failure in each Region. If the server for a particular Region fails, all users in that Region would experience downtime.

### Summary

#### Troubleshooting methodology

The following key steps are involved in troubleshooting issues in cloud infrastructure:

1. **Identify the problem**: The first step involves gathering information about the issue and understanding the symptoms.
2. **Isolate the cause**: The second step involves identifying the specific component or system that is causing the problem.
3. **Develop the hypothesis**: Based on the information you gathered in the previous steps, the third step is to develop a hypothesis about what might be causing the problem.
4. **Test the hypothesis**: The fourth step involves creating and running a test plan to confirm or disprove your hypothesis.
5. **Plan and implement the solution**: The fifth step involves having a clear plan of action before implementation. Outline the steps needed to implement the solution, potential risks, and their mitigation strategies, and a rollback plan in case the solution doesn't work as expected. After the plan is in place, the solution can be implemented.
6. **Verify the solution and system functionality**: The sixth step involves verifying that the solution has resolved the problem and checking that the system is functioning correctly.
7. **Document the findings**: The final step involves recording all the details about the problem, the steps you took to diagnose and resolve it, and the final outcome.

#### Benefits of a structured troubleshooting approach

A structured troubleshooting approach is important and more beneficial than an impromptu approach for the following reasons:

* Efficiency
* Repeatability
* Knowledge building
* Risk management
* Problem prevention

## Troubleshooting with CloudTrail

### Pre-assessment

#### What is the primary purpose of AWS CloudTrail?

* To track user activity and API usage across an AWS infrastructure

Wrong answers:

* To monitor network traffic in Amazon VPCs
* To store and retrieve data at any scale
* To analyze the performance of web applications

##### Explanation

CloudTrail is designed to log, continuously monitor, and retain account activity related to actions across an AWS infrastructure.

The other options are incorrect because of the following:

* CloudTrail is not primarily used for monitoring network traffic. VPC Flow Logs can be used for this task.
* CloudTrail is not a storage service. Amazon S3 can be used for this task.
* CloudTrail doesn’t analyze the performance of web applications. Amazon CloudWatch can be used for this task.

#### Which information from an AWS CloudTrail log file can be used to identify the source of an API call? 

* sourceIPAddress

Wrong answers:

* eventName
* eventSource
* userAgent

##### Explanation

The **sourceIPAddress** field in a CloudTrail log file provides the IP address that the request was made from, which can be used to identify the source of an API call.

The other options are incorrect because of the following:

* The **eventName** field provides the action that was performed, not the source of the API call.
* The **eventSource** field is the service that the request was made to, not the source of the API call.
* The **userAgent** field provides the agent through which the request was made, not the source of the API call.

#### What is the default retention period for AWS CloudTrail logs stored in the Amazon S3 bucket configured for the trail?

* Indefinitely

Wrong answers:

* 30 days
* 90 days
* 180 days

##### Explanation

CloudTrail logs are kept indefinitely by default.

The other options are incorrect because they are not the default retention period for CloudTrail logs. However, developers can use the Amazon S3 object lifecycle management rules to define their own retention policy to better meet the business and auditing needs.

### CloudTrail Review

CloudTrail is a service that facilitates operational and risk auditing, governance, and compliance of an AWS account.

#### CloudTrail Key Functionalities

##### Event recording

Actions taken by a user, role, or an AWS service are recorded as events in CloudTrail. These events include actions taken in the AWS Management Console, AWS Command Line Interface (AWS CLI), and AWS SDKs and APIs.

##### Event history

The **Event history** provides a viewable, searchable, downloadable, and immutable record of the past 90 days of management events in an AWS Region. You can search events by filtering on a single attribute. You automatically have access to the Event history when you create your account.

##### CloudTrail Lake

AWS CloudTrail Lake is a managed data lake for capturing, storing, accessing, and analyzing user and API activity on AWS for audit and security purposes. You can keep the event data in an event data store for up to 3,653 days (about 10 years) if you choose the **One-year extendable retention** pricing option, or up to 2,557 days (about 7 years) if you choose the **Seven-year retention** pricing option.

##### Trails

Trails capture a record of AWS activities, delivering and storing these events in an Amazon S3 bucket, with optional delivery to Amazon CloudWatch Logs and Amazon EventBridge. You can input these events into your security monitoring solutions.

##### Auditing, security monitoring, and troubleshooting

CloudTrail helps track your resources and user activity. It also detects security issues. CloudTrail records these user activities and API calls across AWS services as events. It enhances the security and governance of your cloud environment.

These events help you answer the question of *Who did what, where, and when?*

#### Event types

An event in CloudTrail is the record of an activity in an AWS account. There are three types of CloudTrail events: 

* management events
* data events
* Insights events

##### Management events

Management events provide information about management operations that are performed on resources in your AWS account. These are also known as control plane operations. Management events can also include non-API events that occur in your account. For example, when a user signs in to your account, CloudTrail logs the **ConsoleLogin** event.

The following example shows a single log record of a management event. In this event, an IAM user named **Mary_Major** ran the **aws cloudtrail start-logging** command to call the CloudTrail **StartLogging** action to start the logging process on a trail named **myTrail**. The **startLogging** action in CloudTrail initiates the recording of AWS API calls and related events for a specified trail. When this action is run, CloudTrail begins capturing and logging events to the designated S3 bucket and other configured destinations. This facilitates monitoring and auditing of AWS account activities.

```json
{
    "eventVersion": "1.09",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "EXAMPLE6E4XEGITWATV6R",
        "arn": "arn:aws:iam::123456789012:user/Mary_Major",
        "accountId": "123456789012",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "userName": "Mary_Major",
        "sessionContext": {
            "attributes": {
                "creationDate": "2024-07-19T21:11:57Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2024-07-19T21:33:41Z",
    "eventSource": "cloudtrail.amazonaws.com",
    "eventName": "StartLogging",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.0",
    "userAgent": "aws-cli/2.13.5 Python/3.11.4 Linux/4.14.255-314-253.539.amzn2.x86_64 exec-env/CloudShell exe/x86_64.amzn.2 prompt/off command/cloudtrail.start-logging",
    "requestParameters": {
        "name": "myTrail"
    },
    "responseElements": null,
    "requestID": "9d478fc1-4f10-490f-a26b-EXAMPLE0e932",
    "eventID": "eae87c48-d421-4626-94f5-EXAMPLEac994",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "eventCategory": "Management",
    "tlsDetails": {
        "tlsVersion": "TLSv1.2",
        "cipherSuite": "ECDHE-RSA-AES128-GCM-SHA256",
        "clientProvidedHostHeader": "cloudtrail.us-east-1.amazonaws.com"
    },
    "sessionCredentialFromConsole": "true"
}
```

This log shows that the IAM user initiated the **StartLogging** action with AWS CLI from the IP address 192.0.2.0 on July 19, 2024, at 21:33:41 UTC. The action was performed on the trail named **myTrail** in the us-east-1 Region. The session did not use multi-factor authentication (MFA) and the request was made from AWS CloudShell. This log entry helps track who started the logging process, when, and from where, providing important audit and security information.

##### Data events

Data events provide information about the resource operations performed on or in a resource. These are also known as data plane operations. Data events are often high-volume activities. One example of data events is Amazon S3 object-level API activity such as **GetObject**, **DeleteObject**, and **PutObject** API operations.

Data events are not logged by default when you create a trail or event data store. To record CloudTrail data events, you must explicitly add the supported resources or resource types for which you want to collect activity.

The following example shows a single log record of a data event for the Amazon Cognito **GetCredentialsForIdentity** action.

```json
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "Unknown"
    },
    "eventTime": "2024-01-19T16:55:08Z",
    "eventSource": "cognito-identity.amazonaws.com",
    "eventName": "GetCredentialsForIdentity",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.4",
    "userAgent": "aws-cli/2.7.25 Python/3.9.11 Darwin/21.6.0 exe/x86_64 prompt/off command/cognito-identity.get-credentials-for-identity",
    "requestParameters": {
        "logins": {
            "cognito-idp.us-east-1.amazonaws.com/us-east-1_aaaaaaaaa": "HIDDEN_DUE_TO_SECURITY_REASONS"
        },
        "identityId": "us-east-1:1cf667a2-49a6-454b-9e45-23199EXAMPLE"
    },
    "responseElements": {
        "credentials": {
            "accessKeyId": "ASIAIOSFODNN7EXAMPLE",
            "sessionToken": "aAaAaAaAaAaAab1111111111EXAMPLE",
            "expiration": "Jan 19, 2024 5:55:08 PM"
        },
        "identityId": "us-east-1:1cf667a2-49a6-454b-9e45-23199EXAMPLE"
    },
    "requestID": "659dfc23-7c4e-4e7c-858a-1abce884d645",
    "eventID": "6ad1c766-5a41-4b28-b5ca-e223ccb00f0d",
    "readOnly": false,
    "resources": [{
        "accountId": "111122223333",
        "type": "AWS::Cognito::IdentityPool",
        "ARN": "arn:aws:cognito-identity:us-east-1:111122223333:identitypool/us-east-1:2dg778b3-50b7-565c-0f56-34200EXAMPLE"
    }],
    "eventType": "AwsApiCall",
    "managementEvent": false,
    "recipientAccountId": "111122223333",
    "eventCategory": "Data"
}
```

This log entry reveals a data event where the **GetCredentialsForIdentity** action was performed on the Amazon Cognito Identity service (cognito-identity.amazonaws.com) on January 19, 2024. The request was made from IP address 192.0.2.4 by using the AWS CLI. This resulted in temporary AWS credentials being issued for the identity ID us-east-1:1cf667a2-49a6-454b-9e45-23199EXAMPLE. The **userIdentity** type is marked as **Unknown**, likely because of the nature of the anonymous or unauthenticated request. The action involved retrieving credentials associated with an Amazon Cognito Identity Pool, as indicated by the resource Amazon Resource Name (ARN) provided in the log. This log helps track credential retrieval activities and is crucial for security monitoring and auditing purposes.

##### Insights events

CloudTrail Insights events capture unusual API call rate or error rate activity in your AWS account by analyzing CloudTrail management activity. Insights events provide relevant information, such as the associated API, error code, incident time, and statistics, that help you understand and act on unusual activity. For example, they can detect when a user disables CloudTrail logging, deletes security groups, or makes an unusually high number of API calls.

There are two events logged to show unusual activity in CloudTrail Insights: a start event and an end event.

The following example shows a single log record of a starting Insights event that occurred when the Application Auto Scaling API **CompleteLifecycleAction** was called an unusual number of times. For Insights events, the value of **eventCategory** is **Insight**. An **insightDetails** block identifies the event state, source, name, Insights type, and context, including statistics and attributions.

```json
{
   "eventVersion": "1.08",
   "eventTime": "2024-07-10T01:42:00Z",
   "awsRegion": "us-east-1",
   "eventID": "55ed45c5-0b0c-4228-9fe5-EXAMPLEc3f4d",
   "eventType": "AwsCloudTrailInsight",
   "recipientAccountId": "123456789012",
   "sharedEventID": "979c82fe-14d4-4e4c-aa01-EXAMPLE3acee",
   "insightDetails": {
       "state": "Start",
       "eventSource": "autoscaling.amazonaws.com",
       "eventName": "CompleteLifecycleAction",
       "insightType": "ApiCallRateInsight",
       "insightContext": {
           "statistics": {
               "baseline": {
                   "average": 9.82222E-5
               },
               "insight": {
                   "average": 5.0
               },
               "insightDuration": 1,
               "baselineDuration": 10181
           },
           "attributions": [{
               "attribute": "userIdentityArn",
               "insight": [{
                   "value": "arn:aws:sts::123456789012:assumed-role/CodeDeployRole1",
                   "average": 5.0
               }, {
                   "value": "arn:aws:sts::123456789012:assumed-role/CodeDeployRole2",
                   "average": 5.0
               }],
               "baseline": [{
                   "value": "arn:aws:sts::123456789012:assumed-role/CodeDeployRole1",
                   "average": 9.82222E-5
               }]
           }, {
               "attribute": "errorCode",
               "insight": [{
                   "value": "null",
                   "average": 5.0
               }],
               "baseline": [{
                   "value": "null",
                   "average": 9.82222E-5
                    }]
                }]
            }
   },
   "eventCategory": "Insight"
}
```

### Activity: Differentiate event types

#### You are using CloudTrail for auditing and monitoring your AWS account. One day, you notice an activity in your AWS account. The activity is related to an S3 bucket in your account where a file named **project-data.txt** was accessed. Which type of AWS CloudTrail event does this activity most likely correspond to?

* Data event

Wrong answers:

* Management event
* Insights event

##### Explanation

Thi activity is most likely a data event. Data events provide visibility into resource operations performed on or within a resource. This includes Amazon S3 object-level API activity, such as GetObject, DeleteObject, and PutObject API operations in S3 buckets.

#### You are using CloudTrail for auditing and monitoring your AWS account. One day, you notice an unusual activity in your AWS account. The activity is related to an unusually high number of API calls being made within a short period of time. Which type of AWS CloudTrail event does this activity most likely correspond to?

* Insights event

Wrong answers:

* Management event
* Data event

##### Explanation

This activity is most likely an Insights event. Insights events help identify unusual activity in your account. Foe example, they can detect an unusually high number of API calls are made, which might indicate a potential security issue.

### Analyzing CloudTrail Log Files for Potential Security Incidents

#### Glossary

* **Brute force attacks**

  A brute force attack is a hacking method that uses trial and error to crack passwords, login credentials, and encryption keys. It is a simple yet reliable tactic for gaining unauthorized access to individual accounts and organizations' systems and networks.

#### Example 1: Unauthorized access attempt

```json
{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "AIDAJDPLRKLG7UEXAMPLE",
        "arn": "arn:aws:iam::123456789012:user/Alice",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "userName": "Jane"
    },
    "eventTime": "2024-05-06T20:45:04Z",
    "eventSource": "ec2.amazonaws.com",
    "eventName": "StartInstances",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "205.251.233.182",
    "userAgent": "ec2-api-tools 1.6.12.2",
    "errorCode": "UnauthorizedOperation",
    "errorMessage": "You are not authorized to perform this operation.",
    "requestParameters": {"instancesSet": {"items": [{"instanceId": "i-abc12345"}]}},
    "responseElements": null
}
```

##### What's happening?

This log file shows an unauthorized attempt by the user **Jane** to start an Amazon EC2 instance (**i-abc12345**). The **errorCode** and **errorMessage** fields indicate that the operation was not successful because of a lack of proper permissions.

This could be a sign of a compromised account or an insider threat. The security team should investigate the incident and verify if Jane's credentials were compromised. Then, they should take necessary actions such as resetting the credentials and reviewing IAM policies.

#### Example 2: Security group modification

```json
{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "Root",
        "principalId": "123456789012",
        "arn": "arn:aws:iam::123456789012:root",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "userName": "Root"
    },
    "eventTime": "2024-05-16T23:50:04Z",
    "eventSource": "ec2.amazonaws.com",
    "eventName": "AuthorizeSecurityGroupIngress",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "198.51.100.1",
    "userAgent": "signin.amazonaws.com",
    "requestParameters": {
        "groupId": "sg-12341234",
        "ipPermissions": {
            "items": [
                {
                    "ipProtocol": "tcp",
                    "fromPort": 22,
                    "toPort": 22,
                    "ipRanges": {"items": [{"cidrIp": "0.0.0.0/0"}]}
                }
            ]
        }
    },
    "responseElements": null
}
```

##### What is happening?

This log file shows that the root user has modified a security group (sg-12341234) to allow ingress traffic on TCP port 22 (SSH) from all IP addresses (0.0.0.0/0).

This could potentially expose the resources associated with this security group to SSH brute force attacks. The security team should review this change, and if it's not in line with the security policies, they should revert the change and restrict the ingress rules to trusted IP ranges.

This log file also indicates a compromised root user. Remember, you do not use the root user for day-to-day activities.

#### Example 3: Deletion of CloudTrail log

```json
{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "AIDAJDPLRKLG7UEXAMPLE",
        "arn": "arn:aws:iam::123456789012:user/Bob",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "userName": "John"
    },
    "eventTime": "2024-06-10T21:00:04Z",
    "eventSource": "cloudtrail.amazonaws.com",
    "eventName": "DeleteTrail",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "198.51.100.2",
    "userAgent": "aws-cli/1.16.266 Python/3.7.4 Darwin/18.7.0 botocore/1.13.2",
    "requestParameters": {"name": "MyTrail"},
    "responseElements": null
}
```

##### What is happening?

This log file shows that the user **John** has deleted a CloudTrail trail named **MyTrail**.

This could be an attempt to hide malicious activities. The security team should investigate why the trail was deleted and why John could delete the trail in the first place. If it was not an authorized action, they should recreate the trail, review IAM policies, and consider enabling MFA for sensitive operations.

#### Example 4: Brute force attack

```json
{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "AIDAJDPLRKLG7UEXAMPLE",
        "arn": "arn:aws:iam::123456789012:user/Charlie",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "userName": "Pat"
    },
    "eventTime": "2024-06-26T21:15:04Z",
    "eventSource": "signin.amazonaws.com",
    "eventName": "ConsoleLogin",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "198.51.100.3",
    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "errorCode": "FailedAuthentication",
    "errorMessage": "Failed authentication",
    "additionalEventData": {
        "LoginTo": "https://console.aws.amazon.com/console/home",
        "MobileVersion": "No",
        "MFAUsed": "No"
    },
    "responseElements": {
        "ConsoleLogin": "Failure"
    }
}
```

##### What is happening?

The log file shows a failed console login attempt by the user **Pat**. If you see a high number of such failed login attempts in a short period from the same IP address or for the same user, it could indicate a brute force attack.

The security team should investigate the incident. They should verify if Pat's credentials were compromised and take necessary actions. These actions could include resetting the credentials, enabling MFA, and blocking the suspicious IP address if necessary. It's also recommended to review IAM policies and ensure that they follow the principle of least privilege.

### CloudTrail Integration

CloudTrail, Amazon S3, CloudWatch, and AWS Lambda can be integrated to provide a comprehensive logging and alerting system.

#### Enabling CloudTrail

CloudTrail is enabled on your AWS account when you create it. For an ongoing record of activity and events in your account, you create a trail. You can create trails for a single AWS Region or for all Regions. Trails record the log file in each Region, and CloudTrail can deliver the log files to a single, consolidated S3 bucket. 

#### Configuring Amazon S3

After creating the trail, all your management events will now be logged to an Amazon S3 bucket and can be further analyzed. By default, S3 buckets and objects are private. To deliver log files to an S3 bucket, CloudTrail must have the required permissions. For more information, see [Amazon S3 Bucket Policy for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/create-s3-bucket-policy-for-cloudtrail.html).

Remember that data events are not logged by default when you create a trail or event data store. To record CloudTrail data events, you must explicitly add each resource type for which you want to collect activity. For more information, see [Creating a Trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.html) and [Create an event data store for CloudTrail events with the console](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-event-data-store-cloudtrail.html).

#### Using Lambda

You can detect data exfiltration by collecting activity data on Amazon S3 objects through object-level API events recorded in CloudTrail.

You can use the bucket notification feature and direct Amazon S3 to publish object-created events to Lambda. Whenever CloudTrail writes logs to your S3 bucket, Amazon S3 can then invoke your Lambda function by passing the Amazon S3 object-created event as a parameter. The Amazon S3 event provides information, including the bucket name and key name of the log object that CloudTrail created. Your Lambda function code can read the log object and process the access records logged by CloudTrail.

For example, you might write Lambda function code to notify you if a specific API call was made in your account.

#### Integrating with CloudWatch

CloudTrail integrates with the CloudWatch service to publish the API calls being made to resources or services in AWS accounts. The published event has invaluable information that can be used for compliance, auditing, and governance of your AWS accounts.

You can configure CloudTrail with CloudWatch Logs to monitor your trail logs and be notified when specific activity occurs.

1. Configure your trail to send log events to CloudWatch Logs.
2. Define CloudWatch Logs metric filters to evaluate log events for matches in terms, phrases, or values. For example, you can monitor for **ConsoleLogin** events.
3. Assign CloudWatch metrics to the metric filters.
4. Create CloudWatch alarms that are invoked according to thresholds and time periods that you specify. You can configure alarms to send notifications when alarms are invoked so that you can take action.
5. You can also configure CloudWatch to automatically perform an action in response to an alarm.

When you configure your trail to send events to CloudWatch Logs, CloudTrail sends only the events that match your trail settings. For example, if you configure your trail to log data events only, your trail sends data events only to your CloudWatch Logs log group. CloudTrail supports sending data, Insights, and management events to CloudWatch Logs.

#### Scenario

What the processes might be for you to integrate CloudTrail with these AWS services to automate log management and analysis processes.

AnyCompany is a tech startup and has recently migrated its infrastructure to AWS. They are keen on maintaining high security standards. They want to monitor and alert on unauthorized access attempts to their AWS resources. Here is how they can use CloudTrail, Amazon S3, CloudWatch, and Lambda for their use case.

1. **Set up CloudTrail**

    AnyCompany first sets up CloudTrail and creates a trail in their AWS account. This service records all the API calls made in their account and delivers the log files to an S3 bucket. This is an important step because it provides visibility into user activity and actions taken within their AWS environment.

    The logs include details like the identity of the caller, the time of the API call, the source IP address of the caller, the request parameters, and the response elements returned by the AWS service.

2. **Configure Amazon S3**

    After setting up CloudTrail, AnyCompany configures an Amazon S3 bucket to receive the log files from CloudTrail. They enable event notifications on this bucket. These notifications are in the form of messages sent to a target whenever certain events occur.

    In this case, the target is a Lambda function and the event is the delivery of a new log file.

3. **Create a Lambda function**

    AnyCompany then writes a Lambda function that gets invoked through receiving the event notification from the S3 bucket. This function reads the CloudTrail log file, parses it, and looks for any unauthorized access attempts.

    For example, they might look for events where the **errorCode** field is **AccessDeined** or **UnathorizedOperation**.

4. **Set up Amazon SNS**

    If the Lambda function identifies a specific event such as an error or unauthorized access attempt, it can publish a message to an Amazon Simple Notification Service (Amazon SNS) topic. Amazon SNS is a web service that coordinates and manages the delivery or sending of messages to subscribing endpoints or clients. In this case, the endpoint could be an email or a mobile device.

5. **Set up CloudWatch Logs and alarms**

    AnyCompany configures CloudTrail to send logs to CloudWatch Logs. Then, they can create metric filters to extract values from the log events, which are data points for CloudWatch metrics.

    For example, they might create a metric filter to search for and count the occurrence of the term **UnauthorizedOperation** in the log events. After the metric filters are set up, they can create a CloudWatch alarm that gets invoked when the metric reaches a certain threshold.

    When the alarm condition is met, it changes state from **OK** to **ALARM**, and sends a message to an Amazon SNS topic. AnyCompany can use this setup to monitor their AWS environment for specific events and react accordingly.

6. Summary

    With all these setups, AnyCompany can maintain a high level of security in their AWS environment. They can monitor their log, receive alerts for unauthorized access attempts, and take immediate actions to mitigate any potential threats. The process can be customized based on specific needs and use cases.

### Best Practices for Securing and Managing CloudTrail

Securing and managing CloudTrail trails involves several best practices. Two of best practice categories:

* detective security best practices
* preventative security best practices

#### Detective security best practices

Detective security best practices means that you implement the measures to identify and detect security threats in your AWS environments. These practices are crucial for identifying vulnerabilities, anomalies, and potential threats that could compromise the system. Here are some key points.

##### Creating a trail and applying trails to all AWS Regions

Although CloudTrail provides 90 days of event history information for management events in the CloudTrail console without creating a trail, it is not a permanent record, and it does not provide information about all possible types of events. For an ongoing record, and for a record that contains all the event types you specify, you must create a trail. These log files are delivered to an S3 bucket that you specify.

To help manage your CloudTrail data, consider creating one trail that logs management events in all AWS Regions, and then creating additional trails that log specific event types for resources, such as an S3 bucket activity or Lambda functions.

By logging events in all AWS Regions, you ensure that all events that occur in your AWS account are logged, regardless of which AWS Region they occurred in. This includes logging global service events, which are logged to an AWS Region specific to that service. If an AWS Region is added after you create a trail that applies to all Regions, that new Region is automatically included, and events in that Region are logged. This is the default option when you create a trail in the CloudTrail console.

##### Validating CloudTrail log file integrity

Validated log files are invaluable in security and forensic investigations. A validated log file helps you assert positively that the log file itself has not changed, or that particular user credentials performed specific API activity.

The CloudTrail log file integrity validation process uses industry standard algorithms: SHA-256 for hashing and SHA-256 with RSA for digital signing.

When you enable log file integrity validation, CloudTrail creates a hash for every log file that it delivers. Every hour, CloudTrail also creates and delivers a file that references the log files for the last hour and contains a hash of each. This file is called a digest file. CloudTrail signs each digest file using the private key of a public and private key pair. After delivery, you can use the public key to validate the digest file. CloudTrail uses different key pairs for each AWS Region.

![Partial screenshot (Additional settings section) of AWS CloudTrail console.](./images/W08Img010TroubleshootingCloudTrailTrail.png)

Log file validation setting is enabled in the CloudTrail console when you create a trail.

The digest files are delivered to the same Amazon S3 bucket associated with your trail as your CloudTrail log files. If your log files are delivered from all Regions or from multiple accounts into a single S3 bucket, CloudTrail will deliver the digest files from those Regions and accounts into the same bucket.

The digest files are put into a folder separate from the log files. With this separation of digest files and log files, you can enforce granular security policies. It also permits existing log processing solutions to continue to operate without modification. Each digest file also contains the digital signature of the previous digest file if one exists. The signature for the current digest file is in the metadata properties of the digest file S3 object.

Digest files are delivered to an S3 bucket location that uses the following syntax.

```config
s3://s3-bucket-name/optional-prefix/AWSLogs/aws-account-id/CloudTrail-Digest/
region/digest-end-year/digest-end-month/digest-end-date/
aws-account-id_CloudTrail-Digest_region_trail-name_region_digest_end_timestamp.json.gz
```

Imagine a scenario where a company suspects unauthorized access to their AWS resources. During the investigation, the security team relies on validated CloudTrail log files to determine if any unauthorized API activity occurred. They use the log file integrity validation feature to confirm that the log files have not been tampered with, ensuring that the recorded activities are accurate. CloudTrail's process of creating hash values for each log file and generating hourly digest files helps the team verify the authenticity of the logs. By checking these digest files, the team can also ascertain whether any log files were deleted or if no logs were generated during specific periods. This comprehensive validation process is crucial for their forensic analysis and compliance auditing, providing confidence in the integrity of their security investigation. 

##### Integrating with CloudWatch Logs

You can use CloudWatch Logs to monitor and receive alerts for specific events captured by CloudTrail. The events sent to CloudWatch Logs are those configured to be logged by your trail, so make sure you have configured your trail or trails to log the event types (management events or data events) that you are interested in monitoring.

For example, you can monitor key security and network-related management events, such as failed AWS Management Console sign-in events.

##### Using Amazon GuardDuty

Amazon GuardDuty is a threat detection service that helps you protect your accounts, containers, workloads, and the data within your AWS environment. By using machine learning (ML) models, and anomaly and threat detection capabilities, GuardDuty continuously monitors different log sources. This helps identify and prioritize potential security risks and malicious activities in your environment.

For example, say that there are some credentials created exclusively for an EC2 instance through an instance launch role. GuardDuty will detect potential credential theft if those credentials are used from another AWS account.

##### Using AWS Security Hub

Monitor your usage of CloudTrail as it relates to security best practices by using AWS Security Hub. Security Hub uses detective security controls to evaluate resource configurations and security standards to help you comply with various compliance frameworks.

* [AWS CloudTrail controls](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudtrail-controls.html)

#### Preventative security best practices

Preventative security best practices are proactive measures taken to prevent security breaches and attacks. These practices aim to strengthen the system against potential threats before they occur. Here are some key points.

##### Logging to a dedicated and centralized Amazon S3 bucket

CloudTrail log files are an audit log of actions taken by an IAM identity or an AWS service. The integrity, completeness, and availability of these logs are crucial for forensic and auditing purposes. By logging to a dedicated and centralized S3 bucket, you can enforce strict security controls, access, and segregation of duties. This centralized bucket is often in an isolated logging account to help prevent tampering. 

##### Encrypting CloudTrail log files with AWS KMS keys

By default, the log files delivered by CloudTrail to your bucket are encrypted by using server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS). If you don't enable SSE-KMS encryption, your logs are encrypted using SSE-S3 encryption.

To use SSE-KMS with CloudTrail, you create and manage an AWS KMS key. You attach a policy to the key that determines which users can use the key for encrypting and decrypting CloudTrail log files. The decryption is seamless through Amazon S3. When authorized users of the key read CloudTrail log files, Amazon S3 manages the decryption, and the authorized users can read log files in an unencrypted form.

This approach has the following advantages:

* You can create and manage the AWS KMS key encryption keys yourself.
* You can use a single AWS KMS key to encrypt and decrypt log files for multiple accounts across all Regions.
* You have control over who can use your key for encrypting and decrypting CloudTrail log files. You can assign permissions for the key to the users in your organization according to your requirements.
* Amazon S3 automatically decrypts the log files for requests from users authorized to use the AWS KMS key. Because of this, SSE-KMS encryption for CloudTrail log files is backward-compatible with applications that read CloudTrail log data.
* You have enhanced security.

**The AWS KMS key that you choose must be created in the same AWS Region as the S3 bucket that receives your log files. For example, if the log files will be stored in a bucket in the US East (Ohio) Region, you must create or choose an AWS KMS key that was created in that Region. To verify the Region for an S3 bucket, inspect its properties in the Amazon S3 console.**

With this feature, to read log files, the following permissions are required:

* A user must have Amazon S3 read permissions for the bucket that contains the log files.
* A user must also have a policy or role applied that allows decrypt permissions by the AWS KMS key policy.

Enabling server-side encryption encrypts the log files but not the digest files with SSE-KMS. Digest files are encrypted with Amazon S3 managed encryption keys (SSE-S3).

**If you are using an existing S3 bucket with an S3 Bucket Key, CloudTrail must be allowed permission in the key policy to use the AWS KMS actions GenerateDataKey and DescribeKey. If cloudtrail.amazonaws.com is not granted those permissions in the key policy, you cannot create or update a trail.**

##### Adding a condition key to the default Amazon SNS topic policy

When you configure a trail to send notifications to Amazon SNS, CloudTrail adds a policy statement to your SNS topic access policy that allows CloudTrail to send content to an SNS topic. As a security best practice, it's recommended to add an **aws:SourceArn** (or optionally **aws:SourceAccount**) condition key to the CloudTrail policy statement. This helps prevent unauthorized account access to your SNS topic.

##### Implementing least privilege access to Amazon S3 buckets where you store log files

CloudTrail sends log events to an S3 bucket that you specify. These log files contain an audit log of actions taken by IAM identities and AWS services. The integrity and completeness of these log files are crucial for auditing and forensic purposes. To help ensure that integrity, you should adhere to the principle of least privilege when creating or modifying access to any S3 bucket used for storing CloudTrail log files.

You can take the following steps:

1. Review the [Amazon S3 bucket policy](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/create-s3-bucket-policy-for-cloudtrail.html) for any buckets where you store log files and adjust it if necessary to remove any unnecessary access. This bucket policy will be generated for you if you create a trail using the CloudTrail console but can also be created and managed manually.
2. As a security best practice, be sure to manually add an **aws:SourceArn** condition key to the bucket policy.
3. If you are using the same S3 bucket to store log files for multiple AWS accounts, follow the guidance for [receiving log files for multiple accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html).
4. If you are using an organization trail, make sure you follow the guidance for [organization trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html), and review the example policy for an S3 bucket for an organization trail in [Creating a trail for an organization with the AWS CLI](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-an-organizational-trail-by-using-the-aws-cli.html).

##### Enabling MFA delete on the Amazon S3 bucket where you store log files

When you configure MFA, attempts to change the versioning state of a bucket or delete an object version in a bucket require additional authentication. This way, even if a user acquires the password of an IAM user with permission to permanently delete S3 objects, you can still prevent operations that could compromise your log files.

##### Configuring object lifecycle management on the Amazon S3 bucket where you store log files

The CloudTrail trail default is to store log files indefinitely in the S3 bucket configured for the trail. You can use the Amazon S3 object lifecycle management rules to define your own retention policy to better meet your business and auditing needs. For example, you might want to archive or delete log files after a certain amount of time has passed. Doing so can help save costs.

##### Limiting access to the AWSCloudTrail_FullAccess policy

Users with the **AWSCloudTrail_FullAccess** policy can disable or reconfigure the most sensitive and important auditing functions in their AWS accounts. This policy is not intended to be shared or applied broadly to IAM identities in your AWS account. Limit the application of this policy to as few individuals as possible, those you expect to act as AWS account administrators.

* [IAM for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/security-iam.html)

### CloudTrail Lake

Imagine you are responsible for monitoring and auditing AWS activity across multiple accounts and Regions. AWS CloudTrail Lake becomes invaluable because it provides a centralized, long-term repository for all CloudTrail logs. This provides detailed analysis and querying of historical data. By using CloudTrail Lake, you can efficiently investigate security incidents, track user activity, and ensure compliance with regulatory requirements. You can use the advanced query capabilities to sift through vast amounts of log data to pinpoint specific actions and events quickly. This powerful tool streamlines complex forensic investigations and enhances your ability to maintain a secure and compliant AWS environment.

CloudTrail Lake aggregates, immutably stores, and queries ingested events, offering a managed data lake for your organization. A data lake is a centralized repository that you can use to store all your structured and unstructured data at any scale. You can store your data as-is, without having to first structure the data, and run different types of analytics.

You can choose AWS activities such as actions logged by CloudTrail or historical configuration items recorded by AWS Config. You also have the option of activities such as AWS Audit Manager evidence or events from non-AWS sources. Your organization can use these events for auditing, security investigations, and operational investigations. CloudTrail Lake also offers support for CloudTrail Insights that helps you identify unusual operational activity in your AWS accounts such as spikes in resource provisioning or bursts of AWS Identity and Access Management (IAM) actions.

In addition, CloudTrail Lake dashboards provide out-of-the-box visibility and top insights from your audit and security data directly within the CloudTrail Lake console.

CloudTrail Lake integrates data collection, storage, preparation, and analysis within one platform, which streamlines workflows. With immutable event data storage and flexible retention periods, CloudTrail Lake helps you meet your compliance requirements.

![Example of CloudTrail Lake dashboard. For more information, see the image captions.](./images/W08Img012TroubleshootingCloudTrailLakeDashboard.png)

This CloudTrail Lake dashboard example shows the data that was being queried. The following sections are displayed in the example: **Account activity**, **Top errors**, **Most active regions**, **Top services**, **Most throttled events**, and **Top users**.

#### What problems does CloudTrail Lake solve?

CloudTrail Lake provides a mechanism that assists during auditing. It also identifies and helps during the investigation of security incidents and operational issues. With CloudTrail Lake, you can monitor, store, and validate activity events for authenticity and accordance with internal policies. Furthermore, you can analyze CloudTrail Lake with Amazon Athena. You can then visualize the data with Amazon QuickSight or Amazon Managed Grafana by using Lake query federation for compliance, cost, and usage reporting. CloudTrail Lake helps perform retrospective investigations by answering who made what configuration changes to resources. This information is helpful when investigating security incidents such as data exfiltration or unauthorized access to your AWS environment.

You can also use the curated CloudTrail Lake dashboards to get an overview of anomalous behavior in your account including the type of Insights generated on your accounts or the source of these Insights.

With CloudTrail Lake, you can do the following:

* Store events for up to 10 years to perform retrospective investigations.
* Modernize audit log management and meet audit requirements.
* Verify that user activity is in accordance with internal and external policies.
* Streamline security and operations.
* Investigate noncompliant changes.
* Perform historical asset inventory analysis on configuration items.
* Investigate operational issues in near real time.

#### Benefits of CloudTrail Lake

##### Storage and monitoring

CloudTrail Lake is a data Lake for auditing, security, and operational investigations. It automatically stores your events, including management events, data events, and configuration items from AWS Config, within the lake. You must first enable an AWS Config recording to ingest configuration items in CloudTrail Lake.

##### Immutable and encrypted activity logs

By default, CloudTrail encrypts all events in an event data store. When configuring an event store, you can choose to use your own AWS KMS key. Doing so will incur AWS KMS costs for encryption and decryption.

After you associate an event data store with an AWS KMS key, the AWS KMS key cannot be removed or changed. CloudTrail Lake grants read-only access to prevent changes to log files. Read-only access means that events are automatically immutable. You can verify the integrity of data in exported query results using CloudTrail query results integrity validation.

This feature uses industry standard algorithms—SHA-256 for hashing and SHA-256 with RSA for digital signing—to make it computationally infeasible to modify, delete, or forge CloudTrail query result files without detection.

##### Insights and analytics

You can run SQL-based queries on activity logs for auditing within the lake. CloudTrail Lake supports CloudWatch metrics. CloudWatch provides information about the amount of data ingested into your event data store during the last hour and throughout its retention period.

With the Lake query federation feature, you can use Athena to query your activity logs in CloudTrail Lake and visualize them by using QuickSight and Amazon Managed Grafana.

##### Multi-source

You can consolidate activity events from AWS and non-AWS sources, such as internal applications and SaaS applications running in the cloud or on premises. You don’t need to maintain multiple log aggregators and reporting tools. You can find and add partner integrations to start receiving activity events from these applications in a few steps using the CloudTrail console.

For sources other than the available partner integrations, customers can use CloudTrail Lake APIs to set up their own integrations and push events to CloudTrail Lake.

##### Multi-Region

CloudTrail Lake helps capture and store events from multiple AWS Regions.


##### Multi-account

You can also use CloudTrail Lake to store events from an organization in AWS Organizations in an event data store, including events from multiple Regions and accounts. Additionally, you can designate up to three delegated administrator accounts to create, update, query, or delete CloudTrail Lake event data stores at the organization level.

#### How CloudTrail Lake works

CloudTrail Lake helps you aggregate, immutably store, and query your activity logs for auditing, security investigation, and operational troubleshooting. Here is a summary of how it works:

* **Aggregation**: CloudTrail Lake supports the collection of events from multiple AWS Regions and AWS accounts. You can have a centralized view of all the events happening across your AWS environment.
* **Immutable storage**: The events are stored in an immutable manner, meaning they can't be modified or deleted. This ensures the integrity of your audit logs and helps meet compliance requirements.
* **Querying**: You can run SQL queries across multiple event data stores. This helps you analyze the events and identify patterns or anomalies. The platform also includes sample queries that are designed to help users get started with writing queries for common scenarios. For example, you can identify records of all activities completed by a user to help accelerate security investigations.
* **Dashboards and troubleshooting**: CloudTrail Lake dashboards provide visibility and top insights from data. Auditing and compliance engineers can use the CloudTrail Lake dashboards to track the progress of compliance mandates. Security engineers can closely track sensitive user activities such as deletion of trails or repeated access denied errors. Cloud operation engineers can get visibility to issues such as top service throttling errors from the curated dashboard.

#### Use cases for CloudTrail Lake

##### Performing audit

CloudTrail Lake helps monitor, store, and validate activity events for authenticity and enhanced security posture. You can analyze CloudTrail Lake with Athena and visualize using QuickSight or Amazon Managed Grafana using Lake query federation for compliance, cost, and usage reporting.

##### Investigating security incidents

CloudTrail Lake helps analyze unauthorized access or compromised user credentials by answering who made what configuration changes to the resources associated with security incidents.

##### Operational investigation

CloudTrail Lake helps investigate operational issues such as an unresponsive Amazon EC2 instance or a resource with denied access.

#### Notes about CloudTrail Lake

##### CloudTrail Lake event data stores

CloudTrail Lake aggregates events into event data stores, which are immutable collections of events based on criteria that you select by applying advanced event selectors. CloudTrail Lake converts existing events in row-based JSON format to Apache ORC format for fast retrieval of data. With integrations, you can log events to your event data stores from over a dozen AWS Partners.

##### CloudTrail Lake queries

You can save CloudTrail Lake queries for future use and view the results of queries for up to 7 days. When you run queries, you can save the query results to an S3 bucket. CloudTrail Lake also provides a feature to delegate admin privileges to one of the linked accounts that teams use to query data from the organizational event data store.

### [Lab: Monitoring and Troubleshooting Amazon EC2 Workloads with Detective Controls](./labs/W080Lab1TroubleshootingEc2DetectiveControl.md)

In this lab, you have an opportunity to explore monitoring tools for your Amazon EC2 workloads, as well as apply troubleshooting steps to correct issues affecting your current workloads.

In this lab, you will perform the following tasks:

* Describe the methodology for troubleshooting Amazon EC2 issues.
* Describe the monitoring tools available and their functionality.
* Implement AWS monitoring tools for a given workload.
* Troubleshoot scenarios and issues affecting Amazon EC2 workloads.

### Knowledge Check

#### Which type of event in AWS CloudTrail logs could directly indicate a potential security incident? 

* A high number of failed login attempts

Wrong answers:

* Creation of a new Amazon S3 bucket
* An API call to list all AWS Identity and Access Management (IAM) users
* An increase in data transfer rates

##### Explanation

A high number of failed login attempts indicates a brute force attack, which is a potential security incident. Brute force attacks are attempts to gain access to a system by systematically trying all possible combinations of passwords or encryption keys until the correct one is found.

The other options are incorrect because of the following:

* Creating a new bucket is a common and normal activity that happens frequently. It does not directly indicate a potential security incident.
* An API call to list all IAM users is a common administrative task and does not directly indicate a security incident. However, if this call is made frequently or by unauthorized users, it might require further investigation.
* An increase in data transfer rates could be because of a variety of reasons, including increased usage of the applications or services. It does not directly indicate a security incident.

#### Which AWS service can be used in conjunction with AWS CloudTrail to monitor API activity and send alerts based on defined metrics?

* Amazon CloudWatch

Wrong answers:

* Amazon S3
* Amazon Simple Notification Service (Amazon SNS)
* Amazon Simple Queue Service (Amazon SQS)

##### Explanation

CloudTrail uses CloudTrail integration with Amazon CloudWatch Logs to send events containing API activity in an AWS account to a log group. CloudTrail events that are sent to CloudWatch Logs can activate alarms according to the defined metric filters.

The other options are incorrect because of the following:

* Amazon S3 can store CloudTrail logs, but it does not provide monitoring and alerting capabilities.
* Amazon SNS coordinates and manages the delivery or sending of messages to subscribing endpoints or clients. It does not provide monitoring capabilities.
* Amazon SQS is a fully managed queuing service that can be used to decouple and scale microservices. It does not provide monitoring and alerting capabilities.

#### What is the purpose of log file validation in AWS CloudTrail?

* To ensure the integrity of the log files

Wrong answers:

* To encrypt the log files
* To compress the log files
* To delete the log files

##### Explanation

To determine whether a log file was modified, deleted, or unchanged after CloudTrail delivered it, users can use CloudTrail log file integrity validation. This makes it computationally infeasible to modify, delete, or forge CloudTrail log files without detection.

The other options are incorrect because of the following:

* Encryption is handled by AWS KMS.
* Compression is handled by the service generating the logs.
* Deletion is handled by the user or by lifecycle policies.

### Summary

#### Reviewing what CloudTrail is

There are three types of CloudTrail events: management events, data events, and Insights events.

##### Management events

Management events provide information about management operations that are performed on resources in your AWS account, also known as control plane operations.

##### Data events

Data events provide information about the resource operations performed on or in a resource, also known as data plane operations.

##### Insights events

Insights events provide relevant information, such as the associated API, error code, incident time, and statistics, that help you understand and act on unusual activity.

#### Analyzing CloudTrail log files for security incidents

Knowing how to read CloudTrail log files helps identify possible security issues. This ensures actions against threat can be taken quickly, and further keep the cloud resources safe. There are a couple of potential security incidents that can be identified:

* Unauthorized access attempt
* Security group modification
* Deletion of CloudTrail log
* Brute force attack (where you notice a high volume of failed login attempts in a short period)

#### CloudTrail integration with other AWS services

You can integrate other services such as Amazon S3, CloudWatch, and Lambda with CloudTrail to automate log management and analysis processes.

##### CloudTrail

CloudTrail is enabled on your AWS account when you create it. For an ongoing record of activity and events in your account, you create a trail.

##### Amazon S3

After creating the trail, all your management events will be logged to an S3 bucket. Data events are not logged by default when you create a trail or event data store. To record CloudTrail data events, you must explicitly add each resource type for which you want to collect activity.

##### Lambda

You can use the bucket notification feature and direct Amazon S3 to publish object-created events to Lambda. Whenever CloudTrail writes logs to your S3 bucket, Amazon S3 can then invoke your Lambda function by passing the Amazon S3 object-created event as a parameter. The Amazon S3 event provides information, including the bucket name and key name of the log object that CloudTrail created. Your Lambda function code can read the log object and process the access records logged by CloudTrail.

##### CloudWatch

CloudTrail integrates with the CloudWatch service to publish the API calls being made to resources or services in AWS accounts. The published event has invaluable information that can be used for compliance, auditing, and governance of your AWS accounts.

You can configure CloudTrail with CloudWatch Logs to monitor your trail logs and be notified when specific activity occurs.

#### Best practices for securing and managing CloudTrail

There are two best practice categories: detective security best practices and preventative security best practices.

##### Detective security best practices

The following are some keys points of detective security best practices:

* Create a trail and apply trails to all AWS Regions.
* Validate CloudTrail log file integrity.
* Integrate with CloudWatch Logs.
* Use GuardDuty.
* Use Security Hub.

##### Preventative security best practices

The following are some keys points of preventative security best practices:

* Log to a dedicated and centralized S3 bucket.
* Encrypt CloudTrail log files with AWS KMS keys.
* Add a condition key to the default Amazon SNS topic policy.
* Implement least privilege access to S3 buckets where you store log files.
* Enable MFA delete on the S3 bucket where you store log files.
* Configure object lifecycle management on the S3 bucket where you store log files.
* Limit access to the **AWSCloudTrail_FullAccess** policy.

#### CloudTrail Lake

CloudTrail Lake is a managed data lake for storing and analyzing log data from AWS and non-AWS sources. It offers long-term immutable storage, queries with Athena, and out-of-the-box dashboards. Key functionalities and benefits include the following:

* Store logs for up to 10 years for auditing and investigations.
* Get visibility into user activity across AWS services.
* Identify unusual activity with CloudTrail Insights.
* Meet audit and compliance requirements.
* Perform security investigations and troubleshoot issues.
* Analyze logs with Athena and visualize with QuickSight or Amazon Managed Grafana.
* Modernize log management with a centralized data lake.
* Inventory analysis and asset tracking using configuration data.

## Troubleshooting in IAM

### Pre-assessment

#### What does the **Effect** element in an AWS Identity and Access Management (IAM) policy statement specify?

* It specifies whether the policy allows or denies access.

Wrong answers:

* It specifies the AWS service to which the policy applies.
* It specifies whether the resources that the policy covers.
* It specifies the conditions under which the policy is in effect.

##### Explanation

It specifies whether the policy allows or denies access.

The other options are incorrect because of the following:

* The AWS service to which the policy applies is typically specified in the **Action** element.
* The resources that the policy covers are typically specified in the **Resource** element.
* The conditions under which the policy is in effect are typically specified in the **Condition** element.

#### Which action should a developer take if an IAM user receives an Access Denied error?

* Update the IAM policy.

Wrong answers:

* Modify the user’s password.
* Review the user’s recent activity.
* Reboot the Amazon EC2 instance.

##### Explanation

When an IAM user encounters an *Access Denied error*, it often indicates that the user’s permissions are insufficient for the requested action. To resolve this, review the associated IAM policy such as policy permission, resource ARNs, and conditions.

The other options are incorrect because of the following:

* Password modifications are unrelated to access errors. Passwords control authentication, not authorization.
* Although reviewing activity logs is essential for security, it doesn’t directly resolve the “Access Denied” error. The issue lies in the policy.
* Rebooting the Amazon EC2 instance won’t address IAM policy-related errors. It’s not the right solution.

#### There are two policies attached to an AWS Identity and Access Management (IAM) user. Policy A allows Amazon S3 read access, and Policy B denies Amazon S3 write access. What will be the effective permissions for the user?

* The user will have read access to Amazon S3.

Wrong answers:

* The user will have both read and write access to Amazon S3.
* The user will have write access to Amazon S3.
* The user will have no access to Amazon S3.

##### Explanation

Deny always takes precedence over allow in IAM policies. Because Policy B explicitly denies Amazon S3 write access, the user will have read access that is allowed by Policy A, but not write access.

The other options are incorrect because Policy B prevents write access.

### IAM Policies

#### Purpose of IAM policies

IAM policies are documents that define permissions for an IAM identity, such as IAM users, IAM groups, or IAM roles. You can use IAM policies to specify who can access which resources, and what actions they can perform on those resources. By using IAM policies, you can enforce security best practices, adhere to compliance requirements, and restrict access to sensitive resources. Therefore, you can mitigate risks associated with unauthorized access.

#### Structure of IAM policies

IAM policies are written in JavaScript Object Notation (JSON) format. Each policy document contains one or more policy statements, which define the permissions. Let's review these main components of a statement.

##### Effect

The "Effect" element specifies whether the statement allows or denies access.

The effect can be Allow or Deny. By default, users don't have permission to use resources and API actions, so all requests are denied. An explicit allow overrides the default. An explicit deny overrides any allows.

##### Principal

The **"Principal"** element specifies the entity (user, role, account, service, or federated user) that is allowed or denied access to a resource. The principal is a key component in defining who the policy applies to and is used primarily in resource-based policies.

The **"Principal"** element is required in only some circumstances. If you create a resource-based policy, you must indicate the principal to which you would like to allow or deny access. If you are creating an IAM permissions policy to attach to a user or role, you cannot include this element.

##### Action

The **"Action"** element defines the action (or API operations) that the policy allows or denies. Actions are specified with AWS service namespaces and action names, such as **"s3:GetObject"** or **"ec2:DescribeInstances"**.

##### Resource

The **"Resource"** element specifies the AWS resources to which the actions apply. A resource is identified by its ARN, such as **"arn:aws:s3:::example-bucket/*"** for an Amazon S3 bucket.

Note that the wildcard (*) is used after the bucket name. This is to match all objects in the specified S3 bucket.

##### Condition

The **"Condition"** element is optional. This element further refines when the policy statement is applied based on specified conditions, such as time of day, IP address, or user agent.

#### Best practices for IAM policies

When using IAM policies, it's important to follow best practices to ensure effective access control and security. The following are some recommendations:

* **Follow the principle of least privilege**: Grant only the permissions necessary for users to perform their tasks.
* **Conduct regular review**: Periodically review and audit IAM policies to ensure they align with current access requirements and security standards.
* **Use IAM roles**: Assign permissions to IAM roles and then assume those roles. This is better than using long-term credentials, such as access keys.
* **Test policies**: Use the IAM policy simulator to validate the effectiveness of policies before applying them in a production environment. You will learn more about the IAM policy simulator in the later sections.

#### Evaluating IAM policies and access permissions

Imagine a company has multiple development teams. Each team requires access to specific Amazon EC2 instances for their projects. Additionally, they want to restrict access based on specific conditions, such as instance tags or IP addresses.

You should analyze IAM policies attached to IAM users to determine which EC2 instances they can access and under what conditions. Evaluate the impact of different policy elements, including conditions, on access permissions for each development team.

##### The Developer Team A uses the following policy

```json
{
      "Version": "2012-10-17",
      "Statement": [
          {
                "Effect": "Allow",
                "Action": [
                      "ec2:DescribeInstances",
                      "ec2:StartInstances",
                      "ec2:StopInstances"
            ],
                "Resource": "*",
                "Condition": {
                      "StringEquals": {
                            "ec2:ResourceTag/Team": "A"
                       }
                  }
           }
      ]
}     
```

##### The Developer Team B uses the following policy

```json
{
          "Version": "2012-10-17",
          "Statement": [
              {
                    "Effect": "Allow",
                    "Action": [
                          "ec2:DescribeInstances",
                          "ec2:StartInstances"
                      ],
                    "Resource": "*",
                    "Condition": {
                           "StringEquals": {
                                  "ec2:ResourceTag/Team": "B"
                            }
                       }
              }
          ]
}     
```

##### The Operations Team uses the following policy

```json
{
              "Version": "2012-10-17",
              "Statement": [
                    {
                          "Effect": "Allow",
                          "Action": [
                                "ec2:DescribeInstances"
                           ],
                          "Resource": "*"
                    },
                   {
                          "Effect": "Allow",
                          "Action": [
                                "ec2:StartInstances",
                                "ec2:StopInstances"
                           ],
                          "Resource": "*",
                          "Condition": {
                                "IpAddress": {
                                     "aws:SourceIp": "192.0.2.0/24"
                                  }
                            }
                    },
                    {
                          "Effect": "Deny",
                           "Action": [
                                "ec2:StartInstances",
                                "ec2:StopInstances" 
                            ],
                          "Resource": "*",
                          "Condition": {
                                "NotIpAddress": {
                                      "aws:SourceIp": "192.0.2.0/24"
                                 }
                           }
                   }
            ]
}                    
```

##### Policies explanation

In these policies, Developer Teams A and B are granted access to EC2 instances with specific conditions based on the Team tag.

The Operations Team has unrestricted access to describe, start, and stop instances, but they are denied these actions if the source IP address is not within the specified range (192.0.2.0/24).

###### Policy for Developer Team A

The policy includes the following:

* **Effect: "Allow"** indicates that the actions specified are permitted.
* **Action**: It specifies the Amazon EC2 actions allowed: **DescribeInstances**, **StartInstances**, and **StopInstances**.
* **Resource**: Wildcard **(*)** indicates that the actions are allowed on all Amazon EC2 resources.
* **Condition**: **"StringEquals"** specifies that the condition is met when the value of the specified tag key (Team) on the EC2 instance matches the specified value (A). This condition ensures that only instances tagged with *Team: A* are accessible.

###### Policy for Developer Team B

The policy includes the following:

* **Effect: "Allow"** indicates that the actions specified are permitted.
* **Action**: It specifies the Amazon EC2 actions allowed: **DescribeInstances** and **StartInstances**.
* **Resource**: **"*"** indicates that the actions are allowed on all Amazon EC2 resources.
* **Condition**: **"StringEquals"** specifies that the condition is met when the value of the specified tag key (Team) on the EC2 instance matches the specified value (B). This condition ensures that only instances tagged with *Team: B* are accessible.

###### Policy for Operations Team

The policy includes the following:

* **Effect: "Allow"** indicates that the actions specified are permitted.
* **Action**: It specifies the Amazon EC2 actions allowed: **DescribeInstances**, **StartInstances**, and **StopInstances**.
* **Resource**: **"*"** indicates that the actions are allowed on all Amazon EC2 resources.
* **Condition**: **"IpAddress"** indicates that actions are allowed when the requests originate from within the IP range (192.0.2.0/24).

This policy also includes a Deny statement.

* The **Deny** statement specifies that the actions **StartInstances** and **StopInstances** are denied.
* **Resource: "*"** indicates that the actions are denied on all Amazon EC2 resources.
* **Condition: "NotIpAddress"** specifies that the condition is met when the source IP address from which the request originates is not within the specified range (192.0.2.0/24). This condition restricts the ability to start and stop instances of requests originating from within the specified IP range (192.0.2.0/24).

These IAM policies are designed to grant specific access to EC2 instances based on tags and conditions, ensuring that only authorized users from specific teams or IP addresses can perform certain actions on Amazon EC2 resources.

### Troubleshooting Common Errors in IAM Policies

Generally, there are several indicators that can help you determine whether you should investigate the IAM policies further.

#### Access denied errors

If you or your users are getting *Access denied* errors for resources or APIs they should have access to, it likely indicates a problem with the IAM policies. The errors also occur when the required permissions are explicitly denied by one or more applicable policies. The error messages will specifically mention not being authorized or permission denied.

Most access denied error messages appear in the following format:

* User ***ARNuser*** is not authorized to perform ***action*** on ***resource*** because ***context***.

In this example:

* **ARNuser** is the ARN that doesn't receive access
* **action** is the service action that the policy denies
* **resource** is the ARN of the resource on which the policy acts

The **context** field represents additional context about the policy type that explains why the policy denied access.

#### Resources not being created

If you can't create resources like Amazon EC2 instances or Amazon S3 buckets that your IAM policies should allow, it points to a policy misconfiguration. The error messages will indicate the action is not authorized.

For example, you want to launch an EC2 instance, but you get the following error message:

"An error occurred (UnauthorizedOperation) when calling the **RunInstance**s operation: You are not authorized to perform this operation. Encoded authorization failure message encoded-message."

The **UnauthorizedOperatio**n error indicates that permissions (that defined IAM policies) that are attached to the IAM role aren't correct. Alternatively, the user that is performing the operation doesn't have the required IAM permissions to launch EC2 instances.

#### Malformed policy documents

Policies not properly formatted or invalid JSON will lead to unexpected errors. The IAM service will point out any JSON formatting errors while creating or updating the policies.

### Understanding and correcting incorrect resource ARNs

One of the most common mistakes when working with ARNs is providing an incorrect ARN syntax. This could be because of a missing section, incorrect order of sections, or incorrect values in the sections.

The general syntax of an ARN is:

```yaml
arn : partition : service : region : account-id : resource-id
```

Suppose you have an IAM policy that grants permissions to a specific Amazon S3 bucket. The policy includes the following ARN for the bucket:

```yaml
arn : aws : s3 ::: examplebucket 
```

However, when users attempt to access objects in the bucket, they receive an error message that might look something like the following:

```yaml
User: arn:aws:iam::123456789012:user/johndoe is not authorized to perform: s3:GetObject on resource: arn:aws:s3:::examplebucket/example-object.txt
```

The error message indicates the user does not have permission to access the specified resource. In this case, the problem lies in the ARN. The bucket ARN **(arn:aws:s3:::examplebucket**) only grants permissions at the bucket level, not for individual objects in the bucket. To fix this, you adjust the ARN to include the object path: 

```
arn : aws : s3 ::: examplebucket / *
```

Now that the policy will allow access to all objects in the bucket, users should be able to retrieve objects without encountering *Access denied* errors.

#### Tips for troubleshooting incorrect resource ARN errors in IAM policies

Some tips to troubleshoot incorrect ARNs include the following:

* Double check the resource ARN in the policy matches the actual resource name. Common mistakes are typos, wrong Region, wrong account ID, or wrong service name.
* If copying an example policy, make sure to update the account ID and resource names to match your actual resources. The ARNs are specific to each account and environment.
* Check for special characters in resource names. ARNs use slashes so resource names with slashes can cause issues. Best practice is to avoid special characters.
* Start with least privilege permissions and gradually increase until the policy works to narrow down issues.
* Use the IAM policy simulator to test policies before deploying. The AWS CLI has a **simulate-custom-policy** command and the AWS Management Console has a policy simulator.
* Check CloudTrail logs for the API calls made and error messages to help identify where the issue is occurring.

### Conflicting policies

Conflicting policies in IAM refers to situations where multiple policies apply to a request, and those policies have conflicting permissions.

For example, if one policy allows access to an Amazon S3 bucket and another policy explicitly denies access to the same bucket, these policies conflict. Understanding the evaluation order and the interaction between identity-based and resource-based policies is crucial for managing access control effectively.

#### Evaluation logics

How AWS evaluates policies depends on the types of policies that apply to the request context. Let's break this process down. The following flow chart is the basic version of the [policy evaluation logic flow chart](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html#policy-eval-denyallow).

![Simplified version of AWS IAM policy evaluation logic flow chart.](./images/W08Img020TroubleshootingIamPolicyEvaluation.png)

1. **Default deny**

    By default, all requests are denied. This is called an implicit deny.

    This means that if your IAM user has no policies attached and you attempt to read an Amazon S3 object, your request is implicitly denied.

2. **Explicit deny**

    If there is an explicit deny in any of the policies involved in the request, IAM denies the request.

3. **Organizations SCPs**

    When a request is made in an AWS account with Organizations service control policies (SCPs) in place, IAM first examines the SCPs to determine if the action is allowed. If the SCPs don’t allow the action, IAM denies the request.

    If there is no SCP, or if the SCP allows the requested action, the enforcement code evaluation continues.  

4. **Resource-based policy evaluation**

    Within the same account, resource-based policies impact policy evaluation differently depending on the type of principal accessing the resource, and the principal that is allowed in the resource-based policy. Depending on the type of principal, an **Allow** in a resource-based policy can result in a final decision of **Allow**, even if an implicit deny in an identity-based policy, permissions boundary, or session policy is present.

5. **Identity-based policy evaluation**

    AM then checks the policies attached to the IAM user or role that makes the request. If no policy matches the requested actions, the request is denied.

    IAM also implicitly denies the request if no identity-based policies are present.

6. **Permission boundary**

    IAM checks whether any statements in the permissions boundary would prevent the requested action. If there is, the request is denied. Otherwise, the evaluation process continues.

7. **Session policy evaluation**

    Finally, IAM checks if the request includes a session policy. A session policy is an inline permission assigned to a session principal. Session principals are users who obtain temporary access through AWS Security Token Service (STS), such as federated users, role session users, and web identity users. 

    If the session policy permits the action, then IAM grants the request. On the other hand, when no session policies are involved, IAM determines whether the principal is a role session. If it's a role session, it will allow the request.

##### A note about same-account access and cross-account access

It’s important to understand that the policy evaluation for same-account access differs from cross-account access. 

In the same-account access setting, permissions can be granted either through the resource-based policy or the identity-based policy. For example, even if an IAM user has no policies assigned, they can still be granted access to an Amazon S3 bucket if they are authorized in the bucket policy.

Similarly, an S3 bucket without a bucket policy can be accessed by an IAM user if the identity-based policy of the IAM user permits such access.

However, IAM role trust policies and AWS KMS key policies are exceptions to this logic, because they must explicitly allow access for principals.

**Remember, an explicit deny in any of these policies overrides the allow.**

##### The difference between explicit and implicit denies

A request results in an explicit deny if an applicable policy includes a **Deny** statement. If policies that apply to a request include an **Allow** statement and a **Deny** statement, the Deny statement trumps the **Allow** statement. The request is explicitly denied.

An implicit denial occurs when there is no applicable **Deny** statement but also no applicable **Allow** statement. Because an IAM principal is denied access by default, they must be explicitly allowed to perform an action. Otherwise, they are implicitly denied access.

When you design your authorization strategy, you must create policies with **Allow** statements so that your principals can successfully make requests. However, you can choose any combination of explicit and implicit denies.

##### Example of conflicting policies

The most common types of policies are identity-based policies and resource-based policies. When access to a resource is requested, AWS evaluates all the permissions granted by the policies for at least one **Allow** within the same account. An explicit deny in any of the policies overrides the allow. Let's take a look at the following example.

Assume that Carlos has the username **carlossalazar** and he tries to save a file to the **carlossalazar-logs** Amazon S3 bucket.

Also assume that the following policy is attached to the **carlossalazar** IAM user.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowS3ListRead",
            "Effect": "Allow",
            "Action": [
                "s3:GetBucketLocation",
                "s3:GetAccountPublicAccessBlock",
                "s3:ListAccessPoints",
                "s3:ListAllMyBuckets"
            ],
            "Resource": "arn:aws:s3:::*"
        },
        {
            "Sid": "AllowS3Self",
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::carlossalazar/*",
                "arn:aws:s3:::carlossalazar"
            ]
        },
        {
            "Sid": "DenyS3Logs",
            "Effect": "Deny",
            "Action": "s3:*",
            "Resource": "arn:aws:s3:::*log*"
        }
    ]
}
```

The **AllowS3ListRead** statement in this policy allows Carlos to view a list of all of the buckets in the account. The **AllowS3Self** statement allows Carlos full access to the bucket with the same name as his username. The **DenyS3Logs** statement denies Carlos access to any S3 bucket with log in its name.

Additionally, the following resource-based policy (this is called a bucket policy) is attached to the **carlossalazar** bucket.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::123456789012:user/carlossalazar"
            },
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::carlossalazar/*",
                "arn:aws:s3:::carlossalazar"
            ]
        }
    ]
}
```

This policy specifies that only the **carlossalazar** user can access the **carlossalazar** bucket.

When Carlos makes their request to save a file to the **carlossalazar-logs** bucket, AWS determines what policies apply to the request. In this case, only the identity-based policy and the resource-based policy apply. These are both permissions policies. Because no permissions boundaries apply, the evaluation logic is reduced to the following logic.

![policy evaluation flow chart for IAM user carlos.](./images/W08Img022TroubleshootingIamPolicyEvaluationExample.png)

AWS first checks for a **Deny** statement that applies to the context of the request. It finds one because the identity-based policy explicitly denies Carlos access to any S3 buckets used for logging. Carlos is denied access.

Assume that Carlos then realizes their mistake, so Carlos will now try to save the file to the **carlossalazar** bucket. AWS checks for a **Deny** statement and does not find one. It then checks the permissions policies. Both the identity-based policy and the resource-based policy allow the request. Therefore, AWS allows the request. If either of them explicitly denied the statement, the request would have been denied. If one of the policy types allows the request and the other doesn't, the request is still allowed.

**This logic applies only when the request is made within a single AWS account. For requests made from one account to another, the requester in Account A must have an identity-based policy that allows them to make a request to the resource in Account B. Also, the resource-based policy in Account B must allow the requester in Account A to access the resource. There must be policies in both accounts that allow the operation, otherwise the request fails. For more information about using resource-based policies for cross-account access, see [Cross account resource access in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html).**

#### What are some common error messages you might find?

Usually, the error message pinpoints the source of the issue.

##### Access denied when calling an IAM action

* **Error message**

    "An error occurred (AccessDenied) when calling the ListUsers operation: User: arn:aws:iam::123456789012:user/test is not authorized to perform: iam:ListUsers on resource: arn:aws:iam::123456789012:user/ because **no identity-based policy allows the iam:ListUsers action**"

* **Explanation**

    This type of error message indicates the IAM permission policies attached to the IAM user or role do not allow the required action, that is, iam:ListUsers.

* **Resolution**

    You can verify the IAM policies attached to the user or role and ensure that the required permission is allowed on the supported resource.

##### Action explicitly denied in an identity-based policy

* **Error message**

    "An error occurred (AccessDenied) when calling the ListUsers operation: User: arn:aws:iam::123456789012:user/test is not authorized to perform: iam:ListUsers on resource: arn:aws:iam::123456789012:user/ **with an explicit deny in an identity-based policy**"

* **Explanation**

    This type of error message indicates there is a managed or inline policy attached to the user or role that is explicitly denying the required permission, that is, **iam:ListUsers**.

* **Resolution**

    You should verify the IAM policies attached to the user or role and identify which policy has a matching Deny statement.

##### No resource-based policy allows the action

* **Error message**

    "User: arn:aws:iam::123456789012:user/test is not authorized to perform: kms:Decrypt on resource: arn:aws:kms:us-east-1:987654321098:key/abc3456-xyz98765-123abcdefgh because **no resource-based policy allows the kms:Decrypt action**"

* **Explanation**

    This error occurs when the resource-based policy does not provide the required permission for the user or role. Some AWS services, such as Amazon S3, AWS KMS, and Amazon SNS, support resource-based policies.

* **Resolution**

    You should verify the resource policy on the resource to ensure that it grants the required permissions. Especially in cross-account scenarios, both the identity-based policy for the IAM user or role and the resource-based policy for the cross-account resource must provide the required permission.

##### No attached permissions boundary allows the action

* **Error message**

    "An error occurred (AccessDenied) when calling the ListUsers operation: User: arn:aws:iam::123456789012:user/test is not authorized to perform: iam:ListUsers on resource: arn:aws:iam::123456789012:user/ because **no permissions boundary allows the iam:ListUsers action**"

* **Explanation**

    This type of error message indicates the permissions boundary attached to the user or role does not allow the required permission. A permissions boundary is used to set the maximum permissions an identity-based policy can grant to an IAM entity. An entity's permissions boundary permits it to perform only the actions that are allowed by both its identity-based policies and its permissions boundaries.

* **Resolution**

    You can review the permissions boundary attached to the user or role and ensure that it allows the required permission.

##### Explicit deny in an SCP

* **Error message**

"An error occurred (AccessDenied) when calling the ListUsers operation: User: arn:aws:iam::123456789012:user/test is not authorized to perform: iam:ListUsers on resource: arn:aws:iam::123456789012:user/ with an **explicit deny in a service control policy**"

* **Explanation**

    This type of error message occurs only in member accounts of AWS Organizations. It indicates that the permission is explicitly denied by a service control policy (SCP) that is associated with the member account from the management account of the organization. The SCP can also be associated with an OU to which the member account belongs.

* **Resolution**

    Contact the management account administrator to review the SCPs applied to the account and make the required changes.

##### Encoded error message

* **Error message**

    "An error occurred (UnauthorizedOperation) when calling the DescribeInstances operation: You are not authorized to perform this operation."

* **Explanation**

    Some operations on certain services, such as Amazon EC2, provide an encoded error message.

* **Resolution**

    The error message can only be decoded by authorized users or roles belonging to the same AWS account using the following AWS CLI command:

    ```shell
    aws sts decode-authorization-message --encoded-message <encoded-error-message>
    ```

    The decoded error message can help identify the source of the error. It can help determine whether it is because of an explicit deny in any of the policies or because of missing permissions.

### Troubleshooting Issues in IAM Role Assumptions, Trust Relationships, and Service-linked Roles

Role assumption is used when you want to delegate access to users, applications, or services that don't normally have access to your AWS services. For example, you might want to grant users in your AWS account access to resources they don't usually have. Or, you might want to grant users in one AWS account access to resources in another account. Role assumption is also useful when you want to allow a mobile app to use AWS resources, but you don't want to embed AWS keys within the app. Embedding AWS keys in the app can be difficult to update and there is also a potential risk where users can extract these keys.

Role assumption is a powerful tool to ensure you're adhering to the principle of least privilege, that is, you grant only the permissions necessary to perform a task.

#### Key terms and components of role assumptions

##### Trust policy and permission policy

* When an IAM user assumes an IAM role, the following two sets of permissions are involved:
A trust policy is a JSON policy document in which you define the principals that you trust to assume the role. A role trust policy is a required resource-based policy that is attached to a role in IAM. The principals that you can specify in the trust policy include users, roles, accounts, and services.
* A permission policy (managed or inline) is a policy on the IAM user that allows the user to assume the role.

##### Assume a role

Assuming an IAM role involves a temporary transfer of permissions. By assuming a role, the entity (which could be an AWS service, an application, or an IAM user) can carry out tasks and use resources with the authorized permission. This means that you don't need to make any permanent alterations to these entities' permissions.

After the session token for the assumed role has expired, the entity's additional permissions will be revoked.

When an IAM user assumes an IAM role, consider the following:

* **Same account**: If the IAM user and role are in the same account, a trust policy that explicitly trusts that specific IAM user is sufficient. The trust policy does not have to trust the root user account as a whole.
* **Separate accounts**: If the IAM user and role are in separate AWS accounts, permissions are required from both ends. The user’s permission policy must allow the user to assume the role and the role’s trust policy must also trust the user.

##### Trust relationship

A trust relationship is the state that is defined by the trust policy. When you say a role has a *trust relationship* with a service or a user, it means that the trust policy of the role allows that service or user to assume the role.

#### Troubleshooting role assumptions

Understanding how to troubleshoot role assumptions is important because you can effectively manage and secure access to your AWS resources. This ensures that the right entities have the appropriate permissions, thereby maintaining the integrity and security of your cloud environment.

The most common symptom that indicates an issue with IAM role assumptions is that you can't assume a role and receive an error message that is similar to the following:

```shell
An error occurred (AccessDenied) when calling the AssumeRole operation: Access denied
```

##### Tip 1

To allow users to assume the current role again within a role session, specify the role ARN or AWS account ARN as a principal in the role trust policy.

AWS services that provide compute resources such as Amazon EC2, Amazon Elastic Container Service (Amazon ECS), Amazon Elastic Kubernetes Service (Amazon EKS), and Lambda provide temporary credentials and automatically update these credentials.

This ensures that you always have a valid set of credentials. For these services, it's not necessary to assume the current role again to obtain temporary credentials. However, if you intend to pass session tags or a session policy, you need to assume the current role again.

##### Tip 2

When you assume a role using the AWS Management Console, AWS Security Token Service (AWS STS) API, or AWS CLI, verify the exact name of your role. Role names are case sensitive when you assume a role.

##### Tip 3

Verify that your IAM policy grants you permission to call **sts:AssumeRole** for the role that you want to assume. The **Action** element of your IAM policy must be able to call the **AssumeRole** action. In addition, the **Resource** element of your IAM policy must specify the role that you want to assume.

The **Resource** element can specify a role by its ARN or by a wildcard (*). For example, at least one policy applicable to you must grant permissions similar to the following:

```json
{
"Effect": "Allow",
"Action": "sts:AssumeRole",
"Resource": "arn:aws:iam::account_id_number:role/role-name-you-want-to-assume"
}
```

##### Tip 4

Verify that your IAM identity is tagged with any tags that the IAM policy requires. For example, in the following policy permissions, the **Condition** element requires that you, as the principal requesting to assume the role, must have a specific tag. You must be tagged with **department = HR** or **department = CS**. Otherwise, you cannot assume the role.

```json
{
"Effect": "Allow",
"Action": "sts:AssumeRole",
"Resource": "*",
"Condition": {"StringEquals": {"aws:PrincipalTag/department": [
            "HR",
            "CS"
        ]}}
```

##### Tip 5

Verify that you meet all the conditions that are specified in the role's trust policy. A **Condition** can specify an expiration date, an external ID, or that a request must come only from specific IP addresses. Consider the following example: If the current date is any time after the specified date, then the policy never matches and cannot grant you the permission to assume the role.

```json
{
"Effect": "Allow",
"Action": "sts:AssumeRole",
"Resource": "arn:aws:iam::account_id_number:role/role-name-you-want-to-assume"
"Condition": {
        "DateLessThan" : {
            "aws:CurrentTime" : "2024-05-01T12:00:00Z"
        }
    }
}
```

##### Tip 6

Verify that the AWS account from which you are calling **AssumeRole** is a trusted entity for the role that you are assuming. Trusted entities are defined as a **Principal** in a role's trust policy.

The following example is a trust policy that is attached to the role that you want to assume. In this example, the account ID with the IAM user that you signed in with must be 123456789012. If your account number is not listed in the **Principal** element of the role's trust policy, then you can't assume the role. It doesn't matter what permissions are granted to you in access policies.

Note that the example policy limits permissions to actions that occur between July 1, 2023 and July 31, 2024 (UTC), inclusive. If you log in before or after those dates, then the policy does not match, and you cannot assume the role.

```json
{
"Effect": "Allow",
"Principal": { "AWS": "arn:aws:iam::123456789012:root" },
"Action": "sts:AssumeRole",
"Condition": {
      "DateGreaterThan": {"aws:CurrentTime": "2023-07-01T00:00:00Z"},
      "DateLessThan": {"aws:CurrentTime": "2024-07-31T23:59:59Z"}
    }
```

#### Cross-account access and role assumptions

Cross-account access allows an entity in one AWS account to access resources in another AWS account. This is achieved by creating an IAM role in the account that owns the resource (or, the destination account), and allowing an entity in the other account (that is, the source account) to assume this role.

Let's do a quick review of how cross-account access works:

1. **Create an IAM role in the destination account**. The first step is to create an IAM role in the account that owns the resources you want to access. This role should have a trust policy that allows the source account (the account that needs access to the resource) to assume the role.
2. **Define permission for the role**. The role should have a permissions policy that grants access to the necessary resources in the destination account.
3. **Assume the role from the source account**. An entity in the source account can then assume the role in the destination account. This is done by calling the **sts:AssumeRole** API operation, which returns a set of temporary security credentials.
4. **Access the resources**. The entity can use these temporary credentials to make requests to AWS to access the resources in the destination account.

This setup is beneficial because you can manage permissions centrally in the destination account, instead of requiring you to distribute long-term AWS security credentials across multiple accounts. It also provides an extra extra layer of security because the credentials are temporary.

##### Troubleshooting cross-account access errors example

Let's consider a scenario where a developer named **DevUser** in a Development AWS account (account ID: **111111111111**) is trying to assume a role named **UpdateApp** in a production AWS account (account ID: **222222222222**). The **UpdateApp** role has permissions to update an Amazon S3 bucket named **EXAMPLE-PRODUCTION-APP-12345**.

However, the developer is encountering an error when trying to assume the role. How can you help the developer troubleshoot the AssumeRole error?

###### Check the trust policy

The trust policy of the **UpdateApp** role should include the Development account as a trusted entity. The policy should look like the following:

```json
{
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                          "AWS": "arn:aws:iam::111111111111:user/DevUser"
                    },
                    "Action": "sts:AssumeRole"
                }
            ]
}
```

###### Check the permissions policy of the role

The permission policy of the **UpdateApp** role should allow actions on the **EXAMPLE-PRODUCTION-APP-12345** bucket. If the policy doesn't allow these actions, **DevUser** won't be able to perform the necessary tasks even after assuming the role. The permission policy might look something like the following:

```json
{
              "Version": "2012-10-17",
              "Statement": [
                     {
                               "Effect": "Allow",
                               "Action": [
                                       "s3:PutObject",
                                       "s3:GetObject",
                                       "s3:AbortMultipartUpload",
                                       "s3:ListBucket",
                                       "s3:DeleteObject",
                                       "s3:GetObjectVersion",
                                       "s3:ListMultipartUploadParts"
                                ],
                                "Resource": 
                                        "arn:aws:s3:::EXAMPLE-PRODUCTION-APP-12345/*"
                       }
                ]
}
```

###### Check the permission of the developer

The **DevUser** must have the **sts:AssumeRole** permissions for the **UpdateApp** role. The policy should include the following statement:

```json
{
            "Version": "2012-10-17",
            "Statement": [
               {
                    "Sid": "PermissionToAssumeUpdateApp",
                    "Effect": "Allow",
                    "Action": "sts:AssumeRole",
                    "Resource": "arn:aws:iam::222222222222:role/UpdateApp"
                }
            ]
}
```

By following these steps, you should be able to identify and resolve the issue preventing **DevUser** from assuming the **UpdateApp** role.

#### Service-linked role

Service-linked roles are a unique type of IAM role that is linked directly to an AWS service. The following are some key points about service-linked roles.

##### Service-linked role categories

###### Predefined by the service

Service-linked roles are predefined by the service and include all the permissions that the service requires to call other AWS services on your behalf.

###### Creation, modification, and deletion

The linked service defines how you create, modify, and delete a service-linked role. A service might automatically create or delete the role, so you can create, modify, or delete the role as part of a process in the service. Or it might also require that you use IAM to create or delete the role.

Before you can delete the roles, you must first delete their related resources. This protects your resources because you can't inadvertently remove permission to access the resources.

For example, when you create an Amazon Relational Database Service (Amazon RDS) DB instance, Amazon RDS automatically creates a new service-linked role, if it doesn't already exist. The role is named **AWSServiceRoleForRDS** and it grants Amazon RDS the necessary permissions to call AWS service on your behalf. You can't modify this role. If you no longer need to use Amazon RDS, you can delete the service-linked role, but you must first delete all your DB instances.

###### Streamlined setup

Service-linked roles streamline the process of setting up a service because you don't have to manually add permissions for the service to complete actions on your behalf.

For example, AWS IAM Identity Center uses a service-linked role named **AWSServiceRoleForSSO**. This role grants IAM Identity Center permissions to manage AWS resources, including IAM roles, policies, and SAML IdP on your behalf.

###### Permissions

Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view, but not edit the permissions for service-linked roles. The linked service defines the permissions of its service-linked roles, and unless defined otherwise, only that service can assume the roles.

##### Usage of service-linked roles and IAM roles

Service-linked roles and IAM roles serve different purposes and are used in different scenarios. The following guidelines help you decide when to use each.

###### Service-linked roles

You can use service-linked roles in the following scenarios:

* **Delegating permission to AWS services**: Service-linked roles are ideal when you need to delegate permissions to an AWS service to create and manage AWS resources on your behalf. They provide a secure way to delegate permissions because only the linked service can assume a service-linked role.
* **Streamlining setup**: If you want to streamline the process of setting up a service, service-linked roles are a good choice. They automatically include all the permissions that the service requires, so you don't have to manually add permissions.
* **Preventing unintentional resource deletion**: Service-linked roles protect your resources because you can't unintentionally remove permission to access the resources.

###### IAM roles

You can use IAM roles in the following scenarios:

* **Delegating permissions to users or applications**: If you need to delegate permissions to a user or an application, an IAM role is a better choice. IAM roles can be assumed by anyone who has the necessary permissions. 
* **Managing permissions yourself**: If you want to manage the permissions yourself, you should use IAM roles. Unlike service-linked roles, you can edit the permissions of IAM roles.

##### Troubleshooting service-linked roles

When there are issues with a service-linked role, you might encounter the following type of errors.

###### Duplicate role name error

If you make multiple requests for the same service with the same custom suffix, the request fails with a duplicate role name error. This is because service-linked roles must have unique names within an AWS account.

To resolve this issue, use a different custom suffix for each request.

###### Unable to assume role error

If a service is unable to assume a service-linked role, it could be because of insufficient permissions or the role not being properly set up. For example, you want to use the **ecs cli** command to deploy your containers. If the service-linked role for Amazon ECS is not properly created by an admin on the AWS account, you might encounter an error with the following message:

```shell
InvalidParameterException: Unable to assume the service-linked role. Please verify that the ECS service-linked role exists. 
```

To resolve this issue, make sure you create a service-linked role for Amazon ECS as a whole. This will need to be done by an admin on the AWS account. For more information about using service-linked roles for Amazon ECS, refer to [Using Service-linked Roles for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using-service-linked-roles.html).

##### Duplicate role name error example

Let's take a look at how you can troubleshoot and avoid duplicate role name errors. Let's say you are creating a service-linked role for Amazon EC2 Auto Scaling with a custom suffix: **myCustomSuffix**. You want to create this service-linked role manually with AWS CLI, and you use the following command:

```shell
aws iam create-service-linked-role --aws-service-name autoscaling.amazonaws.com --custom-suffix myCustomSuffix 
```

If you run the same command again, you will get a duplicate name error because a service-linked role with the same name (**AWSServiceRoleForAutoScaling_myCustomSuffix**) already exists in your account.

To resolve this, you can use a different custom suffix when creating the service-linked role:

```shell
aws iam create-service-linked-role --aws-service-name autoscaling.amazonaws.com --custom-suffix myNewCustomSuffix 
```

This will create a new service-linked role with a unique name (**AWSServiceRoleForAutoScaling_myNewCustomSuffix**), and you can avoid the duplicate role name error.

```text
Remember to have the necessary permissions to create service-linked roles in your IAM policy. The iam:CreateServiceLinkedRole action allows service-linked role creation.

Not all AWS services support the --custom-suffix parameter.
```

### Tools and Services for Troubleshooting and Auditing IAM

#### IAM Access Analyzer

Imagine the following scenario. At AnyCompany, the security team was concerned about potential overexposure of sensitive financial data. Using AWS Identity and Access Management Access Analyzer, they discovered that several Amazon S3 buckets containing customer information were accessible from external accounts due to misconfigured policies. The team quickly identified and resolved these vulnerabilities, ensuring that only authorized internal services could access the data. IAM Access Analyzer also provided continuous monitoring, alerting the team of any future policy changes that might inadvertently expose resources. This proactive approach not only tightened security but also ensured compliance with financial regulations, saving the company from potential data breaches and costly penalties. The ability to visualize and understand resource policies in a single view greatly enhanced the team's efficiency in maintaining a secure AWS environment.

IAM Access Analyzer helps you identify the resources in your organization and accounts, such as S3 buckets or IAM roles, shared with an external entity. This lets you identify unintended access to your resources and data, which is a security risk. IAM Access Analyzer identifies resources shared with external principals by using logic-based reasoning to analyze the resource-based policies in your AWS environment.

For each instance of a resource shared outside of your account, IAM Access Analyzer generates a finding. Findings include information about the access and the external principal granted to it. You can review findings to determine if the access is intended and safe or if the access is unintended and a security risk. In addition to helping you identify resources shared with an external entity, you can use IAM Access Analyzer findings to preview how your policy affects public and cross-account access to your resource before deploying resource permissions. The findings are organized in a visual summary dashboard. The dashboard highlights the split between public and cross-account access findings, and provides a breakdown of findings by resource type.

![IAM Access Analyzer dashboard example](./images/W08Img030TroubleshootingIamAccessAnalyzerDashboard.png)

1. **Active findings**

    The **Active findings** section includes the number of active findings for public access and the number of active findings that provide access outside of the account or organization.

    You can choose a number to list all of the active findings of each type, such as public access or access outside of the organization.

2. **Findings overview**

    The **Findings overview** section includes a breakdown of the type of active findings. 

    If you choose the **View all active findings** link, you can get a complete list of active findings for the analyzer's account or organization.

3. **Primary resource types with active findings**

    The **Primary resource types with active findings** section includes a breakdown of the primary resource types with active findings.

    This information helps you prioritize findings for the primary resources first, for example, Amazon S3, Amazon DynamoDB, and AWS KMS.

    This is not an exhaustive list of every resource type. Your analyzer might have active findings for resource types not listed in this section.

##### Identifying unused access granted to IAM users and roles

IAM Access Analyzer helps you identify and review unused access in your AWS organization and accounts. IAM Access Analyzer continuously monitors all IAM roles and users in your AWS organization and accounts and generates findings for unused access. The findings highlight unused roles, unused access keys for IAM users, and unused passwords for IAM users. For active IAM roles and users, the findings provide visibility into unused services and actions.

###### Unused roles

These are roles with no access activity within the specified usage window.

###### Unused IAM user access keys and passwords

These are credentials belonging to IAM users that make it possible for them to access your AWS account.

###### Unused permissions

Service-level and action-level permissions that weren't used by a role within the specified usage window. IAM Access Analyzer uses identity-based policies attached to roles to determine the services and actions that those roles can access.

IAM Access Analyzer supports the review of unused permissions for all service-level permissions.

The findings for both external access and unused access analyzers are organized into a visual summary dashboard. The dashboard highlights your AWS accounts that have the most findings and provides a breakdown of findings by type.

IAM Access Analyzer reviews the last accessed information for all roles in your AWS organization and accounts to help you identify unused access. IAM action last accessed information helps you identify unused actions for roles in your AWS accounts.

##### Validating policies against AWS best practices

You can validate your policies against IAM policy grammar and AWS best practices using the basic policy checks provided by IAM Access Analyzer policy validation. You can create or edit a policy using the AWS CLI, AWS API, or JSON policy editor in the IAM console. You can view policy validation check findings that include security warnings, errors, general warnings, and suggestions for your policy. These findings provide actionable recommendations that help you author policies that are functional and conform to AWS best practices.

##### Validating policies against your specified security standards

You can validate your policies against your specified security standards using the IAM Access Analyzer custom policy checks. You can create or edit a policy using the AWS CLI, AWS API, or JSON policy editor in the IAM console. Through the console, you can check whether your updated policy grants new access compared to the existing version. Through AWS CLI and AWS API, you can also check specific IAM actions that you consider critical are not allowed by a policy. These checks highlight a policy statement that grants new access. You can update the policy statement and re-run the checks until the policy conforms to your security standard.

##### Generating policies

IAM Access Analyzer also analyzes your CloudTrail logs to identify actions and services that have been used by an IAM entity (user or role) within your specified date range. It then generates an IAM policy that is based on that access activity. You can use the generated policy to refine an entity's permissions by attaching it to an IAM user or role.

#### IAM policy simulator

You might find that your IAM policies will need to be tested to better understand what is being applied, what levels of access users have, and how to troubleshoot when things go wrong.

With the IAM policy simulator, you can test and troubleshoot identity-based policies, IAM permissions boundaries, AWS Organizations SCPs, and resource-based policies. The policy simulator does not make an actual AWS service request, so you can safely test requests that might make unwanted changes to your live AWS environment. The only result returned is whether the requested action would be allowed or denied.

![Example of IAM policy simulator.](./images/W08Img032TroubleshootingIamPolicySimulator.png)

The IAM policy simulator shows there are two actions being tested. One is for AWS Amplify UI Builder: **DeleteForm** action. The other one is for Amazon S3: **CreateBucket action**. Both actions are implicitly denied.

Here are some common use cases for the IAM policy simulator:

* Test identity-based policies that are attached to IAM users, user groups, or roles in your AWS account. If more than one policy is attached to the user, user group, or role, you can test all the policies, or select individual policies to test. You can test which actions are allowed or denied by the selected policies for specific resources.
* Test and troubleshoot the effect of permissions boundaries on IAM entities. You can only simulate one permissions boundary at a time.
* Test the effects of resource-based policies on IAM users that are attached to AWS resources, such as S3 buckets, SQS queues, SNS topics, or S3 Glacier vaults. To use a resource-based policy in the policy simulator for IAM users, you must include the resource in the simulation. You must also select the check box to include that resource's policy in the simulation.
* If your AWS account is a member of an organization in AWS Organizations, then you can test the impact of SCPs on your identity-based policies.
* Test new identity-based policies that are not yet attached to a user, user group, or role by typing or copying them into the policy simulator. These are used only in the simulation and are not saved. You can't type or copy a resource-based policy in the policy simulator.
* Test identity-based policies with selected services, actions, and resources. For example, you can test to ensure that your policy allows an entity to perform the **ListAllMyBuckets**, **CreateBucket**, and **DeleteBucket** actions in the Amazon S3 service on a specific bucket.
* Simulate real-world scenarios by providing context keys, such as an IP address or date, that are included in **Condition** elements in the policies being tested.
* Identify which specific statement in identity-based policy results in allowing or denying access to a particular resource or action.

```text
By default, console users can test policies that are not yet attached to a user, user group, or role by typing or copying those policies into the policy simulator. These policies are used only in the simulation and do not disclose sensitive information. API users must have permissions to test unattached policies. You can allow console or API users to test policies that are attached to IAM users, user groups, or roles in your AWS account.
```

##### Permissions required for using the IAM policy simulator console

You can allow users to test policies that are attached to IAM users, user groups, or roles in your AWS account. To do so, you must provide your users with permissions to retrieve those policies. To test resource-based policies, users must have permission to retrieve the resource's policy.

###### Allowing console users to simulate policies for users

You will include the following actions in your policy:

* **iam:GetGroupPolicy**
* **iam:GetPolicy**
* **iam:GetPolicyVersion**
* **iam:GetUser**
* **iam:GetUserPolicy**
* **iam:ListAttachedUserPolicies**
* **iam:ListGroupsForUser**
* **iam:ListGroupPolicies**
* **iam:ListUserPolicies**
* **iam:ListUsers**

###### Allowing console users to simulate policies for user groups

You will include the following actions in your policy:

* **iam:GetGroup**
* **iam:GetGroupPolicy**
* **iam:GetPolicy**
* **iam:GetPolicyVersion**
* **iam:ListAttachedGroupPolicies**
* **iam:ListGroupPolicies**
* **iam:ListGroups**

###### Allowing console users to simulate policies for roles

You will include the following actions in your policy:

* **iam:GetPolicy**
* **iam:GetPolicyVersion**
* **iam:GetRole**
* **iam:GetRolePolicy**
* **iam:ListAttachedRolePolicies**
* **iam:ListRolePolicies**
* **iam:ListRoles**

To test resource-based policies, users must have permission to retrieve the resource's policy.

###### Allowing console users to test resource-based policies in an Amazon S3 bucket

You will include the following actions in your policy:

* **s3:GetBucketPolicy**

For example, the following policy uses this action to allow console users to simulate a resource-based policy in a specific Amazon S3 bucket.

```json
{
        "Version": "2012-10-17",
        "Statement": [
          {
            "Effect": "Allow",
            "Action": "s3:GetBucketPolicy",
            "Resource":"arn:aws:s3:::bucket-name/*"
          }
        ]
}
```

#### CloudTrail

IAM and AWS STS are integrated with CloudTrail, a service that provides a record of actions taken by an IAM user or role. CloudTrail captures all AWS service API calls as events, including calls from the console, AWS CLI, and API tools. CloudTrail is enabled on your AWS account when you create the account. If you create a trail, you can facilitate continuous delivery of CloudTrail events to an Amazon S3 bucket. AWS services like Athena can then be used to query the logs directly from the S3 bucket. If you don't configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**.

CloudTrail can be used to answer the following common questions:

* What actions did a user take over a given period?
* For a given resource, which AWS user has taken actions on it over a given time period?
* What is the source IP address of a given activity?
* Which user activities failed because of inadequate permissions?

**CloudTrail logs sign-in events to the AWS Management Console, the AWS discussion forums, and AWS Marketplace. CloudTrail also logs successful and failed sign-in attempts for IAM users and federated users. For AWS account root users, only successful sign-in events are logged. CloudTrail does not log unsuccessful sign-in events by the root user.**

##### CloudTrail log contents

There can be dozens or even hundreds of events like the one covered in the previous example in one CloudTrail log file. The body of a CloudTrail log file contains multiple fields that help you determine the requested action and when and where the request was made.

The following table shows some important fields that you need to be aware of.

| Field | Description |
| ----- | ----------- |
| eventTime | The date and time of the event reported in UTC |
| eventType | There can be three types of events:<br>* **AwsConsoleSignin**: A user in your account (root, IAM, federated, SAML, or SwitchRole) signed in to the AWS Management Console.<br>* **AwsServiceEvent**: The called service generated an event related to your trail. For example, this can occur when another account makes a call with a resource that you own.<br>* **AwsApiCall**: A public API for an AWS resource was called. |
| eventSource  | The service that the request was made to. This name is typically a short form of the service name without spaces plus **.amazonaws.com.** For example:\* AWS CloudFormation is **cloudformation.amazonaws.com**.\* Amazon EC2 is **ec2.amazonaws.com**.\* Amazon Simple Workflow Service is **swf.amazonaws.com**.\This convention has some exceptions. For example, the **eventSource** for Amazon CloudWatch is **monitoring.amazonaws.com**. |
| eventName | The requested action, which is one of the actions in the API for that service. |
| sourceIPAddress | The IP address where the request came from. If one AWS service calls another service, the DNS name of the calling service is used. |
| userAgent | The tool or application through which the request was made, such as the AWS Management Console, the AWS SDKs, or the AWS CLI. The following are example values:<br>* **signin.amazonaws.com**: The request was made by an IAM user with the AWS Management Console.<br>* **console.amazonaws.com**: The request was made by a root user with the AWS Management Console.<br>* **lambda.amazonaws.com**: The request was made with AWS Lambda.<br>* **aws-sdk-java**: The request was made with the AWS SDK for Java.<br>* **aws-sdk-ruby**: The request was made with the AWS SDK for Ruby.<br>* **aws-cli/1.3.23 Python/2.7.6 Linux/2.6.18-164.el5**: The request was made with the AWS CLI installed on Linux. |
| errorMessage | Any error message returned by the requested service. |
| requestParameters | The parameters that were sent with the API call, which can vary depending on the type of resource or service called.

For example, in an Amazon S3 API call, you could have the bucketName and location sent as parameters. |
| resources | List of AWS resources accessed in the event. This can be the resource's ARN, an AWS account number, or the resource type. |
| userIdentity | A collection of fields that describe the user or service that made the call. These fields can vary based on the type of user or service.<br>The following values are possible types of identity:<br>* **Root**: The request was made with your AWS account credentials. If the userIdentity type is Root and you set an alias for your account, the userName field contains your account alias.<br>* **IAMUser**: The request was made with the credentials of an IAM user.<br>* **AssumedRole**: The request was made with temporary security credentials that were obtained with a role through a call to the AWS STS AssumeRole API call. This can include roles for Amazon EC2 and cross-account API access.<br>* **FederatedUser**: The request was made with temporary security credentials that were obtained through a call to the AWS STS **GetFederationToken** API. The **sessionIssuer** element indicates if the API was called with root or IAM user credentials.<br>* **AWSAccount**: The request was made by another AWS account.<br>* **AWSService**: The request was made by an AWS account that belongs to an AWS service. For example, AWS Elastic Beanstalk assumes an IAM role in your account to call other AWS services on your behalf. |

#### CloudTrail logs examples

##### Example 1: IAM API event in CloudTrail log file

```json
{
  "eventVersion": "1.05",
  "userIdentity": {
  "type": "IAMUser",
    "principalId": "AIDACKCEVSQ6C2EXAMPLE",
    "arn": "arn:aws:iam::444455556666:user/JaneDoe",
    "accountId": "444455556666",
    "accessKeyId": "AKIAI44QH8DHBEXAMPLE",
    "userName": "JaneDoe",
    "sessionContext": {
      "attributes": {
        "mfaAuthenticated": "false",
        "creationDate": "2024-07-15T21:39:40Z"
      }
    },
    "invokedBy": "signin.amazonaws.com"
  },
  "eventTime": "2024-07-15T21:40:14Z",
  "eventSource": "iam.amazonaws.com",
  "eventName": "GetUserPolicy",
  "awsRegion": "us-east-2",
  "sourceIPAddress": "signin.amazonaws.com",
  "userAgent": "signin.amazonaws.com",
  "requestParameters": {
    "userName": "JaneDoe",
    "policyName": "ReadOnlyAccess-JaneDoe-202407151307"
  },
  "responseElements": null,
  "requestID": "9EXAMPLE-0c68-11e4-a24e-d5e16EXAMPLE",
  "eventID": "cEXAMPLE-127e-4632-980d-505a4EXAMPLE"
} 
```

From this event information, you can determine that the request was made to get a user policy named **ReadOnlyAccess-JaneDoe-202407151307** for user **JaneDoe**, as specified in the **requestParameters** element. You can also see that the request was made by an IAM user named **JaneDoe** on July 15, 2024 at 9:40 PM (UTC). In this case, the request originated in the AWS Management Console, as you can tell from the **userAgent** element.

##### Example 2: Cross-account AWS STS API events in CloudTrail log entry

```json
{
  "eventVersion": "1.05",
  "userIdentity": {
    "type": "IAMUser",
    "principalId": "AIDAQRSTUVWXYZEXAMPLE",
    "arn": "arn:aws:iam::777788889999:user/JohnDoe",
    "accountId": "777788889999",
    "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
    "userName": "JohnDoe"
  },
  "eventTime": "2024-07-18T15:07:39Z",
  "eventSource": "sts.amazonaws.com",
  "eventName": "AssumeRole",
  "awsRegion": "us-east-2",
  "sourceIPAddress": "192.0.2.101",
  "userAgent": "aws-cli/1.11.10 Python/2.7.8 Linux/3.2.45-0.6.wd.865.49.315.metal1.x86_64 botocore/1.4.67",
  "requestParameters": {
    "roleArn": "arn:aws:iam::111122223333:role/EC2-dev",
    "roleSessionName": "JohnDoe-EC2-dev",
    "sourceIdentity": "JohnDoe",
    "serialNumber": "arn:aws:iam::777788889999:mfa"
  },
  "responseElements": {
    "credentials": {
      "sessionToken": "<encoded session token blob>",
      "accessKeyId": "ASIAI44QH8DHBEXAMPLE",
      "expiration": "Jul 18, 2024, 4:07:39 PM"
      },
    "assumedRoleUser": {
      "assumedRoleId": "AIDAQRSTUVWXYZEXAMPLE:JohnDoe-EC2-dev",
      "arn": "arn:aws:sts::111122223333:assumed-role/EC2-dev/JohnDoe-EC2-dev"
    },
  "sourceIdentity": "JohnDoe"
  },
  "resources": [
    {
      "ARN": "arn:aws:iam::111122223333:role/EC2-dev",
      "accountId": "111122223333",
      "type": "AWS::IAM::Role"
    }
  ],
  "requestID": "4EXAMPLE-0e8d-11e4-96e4-e55c0EXAMPLE",
  "sharedEventID": "bEXAMPLE-efea-4a70-b951-19a88EXAMPLE",
  "eventID": "dEXAMPLE-ac7f-466c-a608-4ac8dEXAMPLE",
  "eventType": "AwsApiCall", 
  "recipientAccountId": "111122223333"
}
```

The IAM user named **JohnDoe** in account 777788889999 calls the AWS STS **AssumeRole** action to assume the role **EC2-dev** in account 111122223333. The account administrator requires users to set a source identity equal to their username when assuming the role. The user passes in the source identity value of **JohnDoe**.

### Best Practices for IAM Policy Management

IAM policies control permissions for entities like users, groups, and roles in AWS. Proper management of these policies is crucial for security, compliance, and avoiding accidental over-permissions.

#### Policy versioning

When you make changes to an IAM customer managed policy, and when AWS makes changes to an AWS managed policy, the changed policy doesn't overwrite the existing policy. Instead, IAM creates a new version of the managed policy. IAM stores up to five versions of your customer managed policies. 

Version your IAM policies so you can conveniently roll back unwanted changes. This provides an audit trail and facilitates restoring previous permissions. For example, you update an IAM policy to allow additional Amazon S3 bucket access. With versioning, you can roll back and restore the previous permissions if issues arise.

#### Separation of duties

Separation of duties is a design principle where more than one person's approval is required to conclude a critical task. It's important to clearly separate roles by their duties and assign permissions based on the specific tasks that users or services need to perform. This can involve creating roles for specific applications, tasks, or teams, and assigning permissions accordingly.

For example, you can have separate groups for Developers, Testers, and Operations. Developers can't access production, Testers can't modify code, and Ops can't modify testing environments.

#### IAM policy variables

With IAM policy variables, you can define dynamic values inside policies. Variables are marked using a $ prefix followed by a pair of curly braces (**{ }**) that include the variable name of the value from the request. When the policy is evaluated, the policy variables are replaced with values that come from the conditional context keys passed in the request.

You can replace hard-coded values with variables to make reusable, dynamic policies that can adapt as needed.

For example, you can use the **${aws:username}** variable to dynamically replace itself with the IAM username of the entity invoking the request. This can be useful when you are managing a project with several developers needing access to specific AWS resources.

#### Regular policy reviews

Regularly reviewing and updating your IAM policies is important to maintain a good security measure. An audit gives you an opportunity to remove unnecessary permissions, validate that policies match business needs, and adjust for changes.

For example, you can review all user policies quarterly to remove unused permissions. You can also remove access to unused AWS services.

#### Additional best practices

The following are other best practices to keep in mind:

* Avoid using root user credentials for daily tasks.
* Attach permissions to groups instead of individual users.
* Aim for least privilege permissions.
* Use IAM roles for applications and services that need access to AWS resources.
* Use IAM Access Analyzer to generate least-privilege policies based on access activity and to validate your IAM policies to ensure secure and functional permissions.
* Use conditions in IAM policies to further restrict access.

### [Lab: Performing a Basic Audit of Your AWS Environment](./labs/W082Lab2TroubleshootingBasicAudit.md)

In this lab, you perform basic audits of core AWS resources. You use the AWS Management Console to understand how to audit the use of multiple AWS services, such as Amazon EC2, Amazon VPC, IAM Identity Center, Amazon Security Groups, CloudTrail, and CloudWatch. This lab teaches you how to extend your existing auditing objectives related to organizational governance, asset configuration, logical access controls, operating systems, databases, and application security configurations within AWS.

In this lab, you will perform the following tasks:

* Review user permissions in IAM.
* Capture audit evidence using the IAM policy simulator.
* Review Inbound and Outbound networking rules for Amazon EC2 Security Groups.
* Review Amazon VPC configurations, subnets, and Network ACLs.
* Review CloudWatch performance metrics.
* Review raw CloudTrail logs within Amazon S3.

### Knowledge Check

#### A company uses an Amazon S3 bucket to store sensitive financial data. The bucket contains confidential reports accessible by authorized employees. A developer configures both identity-based and resource-based policies to control access. The bucket policy allows the getObject action for all authenticated AWS users. However, User A’s identity-based policy explicitly denies the getObject action on the S3 bucket. What will happen if User A tries to perform the getObject action on the S3 bucket?

* The action is denied.

Wrong answers:

* The action is allowed.
* The action is conditionally allowed based on additional factors.
* The action is randomly chosen.

##### Explanation

In this scenario, the **getObject** action is denied because the identity-based policy takes precedence. The principle of least privilege ensures that permissions are not inadvertently granted.

The other options are incorrect because the explicit denial in the identity-based policy prevails. There are no additional conditions because the denial is straightforward. AWS follows deterministic evaluation; it doesn’t randomly choose between policies.

#### What is the benefit of using the AWS Identity and Access Management (IAM) policy simulator?

* It helps troubleshoot and verify IAM policy effects without making actual changes.

Wrong answers:

* It helps developers to create IAM users and groups.
* It generates AWS CloudTrail logs automatically for IAM activities.
* It provides recommendations for IAM best practices. 

##### Explanation

The IAM policy simulator is primarily used for simulating the effects of IAM policies on resources and actions without actually making changes. This helps in troubleshooting and verifying the impact of policy changes before applying them.

The other options are incorrect because they are not the main functions of the IAM policy simulator.

#### A developer is troubleshooting an issue where an Amazon EC2 instance is unable to access an Amazon S3 bucket. The instance has an AWS Identity and Access Management (IAM) role attached. What could be the problem? 

* The IAM role lacks proper permission.

Wrong answers:

* The trust relationship of the IAM role is misconfigured.
* The Amazon EC2 instance profile is missing.
* The Amazon EC2 instance and Amazon S3 bucket are in different Regions.

##### Explanation

The IAM role attached to the EC2 instance needs to have the proper Amazon S3 permissions (for example, **s3:GetObject**) to allow access to the S3 bucket. If the permissions are missing or too restrictive, the EC2 instance will not be able to access the S3 bucket even if the role is attached.

The other options are incorrect because of the following:

* A misconfigured trust relationship would prevent the EC2 instance from even assuming the IAM role.
* When an EC2 instance profile is missing, it might prevent the EC2 instance from assuming the IAM role. It would not directly cause an inability to access the S3 bucket if the role has been successfully attached.
* S3 buckets are Region-specific, but cross-Region access is possible if proper IAM permissions are set on the role. So different Regions alone would not cause the access failure.

### Summary

#### The purpose and structure of IAM policies

Using IAM policies enforces security best practices, adheres to compliance requirements, and restricts access to sensitive resources. Therefore, you can mitigate risks associated with unauthorized access.

The main components of an IAM policy statement include the following:

* **Effect**: It specifies whether the statement allows or denies access.
* **Principal**: It's required in only some circumstances. If you create a resource-based policy, you must indicate the account, user, role, or federated user to which you want to allow or deny access.
* **Action**: This defines the action (or API operations) that the policy allows or denies.
* **Resource**: This specifies the AWS resources to which the actions apply.
* **Condition**: This element is optional. This element further refines when the policy statement is applied based on specified conditions.

##### Best practices for IAM policies include the following

* Follow the principle of least privilege.
* Conduct regular review.
* Use IAM roles.
* Test policies.

#### Troubleshooting common errors in IAM policies

There are several indicators that can help you determine whether you should investigate the IAM policies further. These indicators include access denied errors, resources not being created, and malformed policy documents.

##### Incorrect resource ARNs

One of the most common mistakes when working with ARNs is providing an incorrect ARN syntax. This could be because of a missing section, incorrect order of sections, or incorrect values in the sections. Tips to troubleshoot incorrect ARNs include the following:

* Double check the resource ARN in the policy matches the actual resource name.
* Make sure to update the account ID and resource names to match your actual resources if you use the example policy from AWS.
* Check for special characters in resource names. Best practice is to avoid special characters.
* Start with least privilege permissions and gradually increase until the policy works to narrow down issues.
* Check CloudTrail logs for the API calls made and error messages.

##### Conflicting policies

Conflicting IAM policies can allow or deny access to the same resource. Explicit deny policies take precedence over allows. AWS Organizations SCPs are checked next, then resource-based policies, identity-based policies, permission boundaries, and session policies. The most restrictive policy applied determines access. Understanding this evaluation order is crucial to managing access when policies conflict.

#### Troubleshooting role assumptions and service-linked roles

The most common symptom that indicates an issue with IAM role assumptions is that you can't assume a role. Make sure you have the trust policy and permission policy set up correctly. When setting up cross-account access and role assumptions, make sure you use the following logics:

1. Create an IAM role in the account that owns the resources you want to access.
2. Define permission for the role. The role should have a permissions policy that grants access to the necessary resources in the destination account.
3. Assume the role from the source account by calling the **sts:AssumeRole** API operation, which returns a set of temporary security credentials.
4. The entity (source account) can then use these temporary credentials to make requests to AWS to access the resources in the destination account.

The linked service defines how you create, modify, and delete a service-linked role. A service might automatically create or delete the role, so you can create, modify, or delete the role as part of a process in the service. Before you can delete the roles, you must first delete their related resources. This protects your resources because you can't inadvertently remove permission to access the resources.

Service-linked roles need to have unique role names, otherwise you will encounter errors.

#### Tools and services used to troubleshoot and audit IAM

##### IAM access analyzer

IAM Access Analyzer is a service that you can use to identify the resources in your organization and accounts that are shared with an external entity. IAM Access Analyzer continuously analyzes policies to help you identify unintended access to your resources and data.

##### IAM policy simulator

You can use the IAM policy simulator to test and validate the effects of your IAM policies before deploying them. This helps identify any unintended consequences. You can test IAM policies by specifying identities, actions, resources, and conditions to simulate how the policies work.

##### AWS CloudTrail

CloudTrail is a service that tracks user activity and API usage to provide an audit trail of all the AWS API calls made within your account. This helps identify issues and monitor changes. CloudTrail records important information about each API call including the identity of the API caller, the time of the API call, and the source IP address of the API caller.

#### Best practices for managing IAM policies

##### Policy versioning

Version your IAM policies so you can conveniently roll back unwanted changes. This provides an audit trail and facilitates restoring previous permissions.

##### Separation of duties

It's important to clearly separate roles by their duties and assign permissions based on the specific tasks that users or services need to perform. This can involve creating roles for specific applications, tasks, or teams, and assigning permissions accordingly.

##### IAM policy variables

With IAM policy variables, you can define dynamic values inside policies. You can replace hard-coded values with variables to make reusable, dynamic policies that can adapt as needed.

##### Regular policy reviews

Regularly reviewing and updating your IAM policies is important to maintain a good security measure. An audit gives you an opportunity to remove unnecessary permissions, validate that policies match business needs, and adjust for changes.

##### Additional best practices

* Avoid using root user credentials for daily tasks.
* Attach permissions to groups instead of individual users.
* Aim for least privilege permissions.
* Use IAM roles for applications and services that need access to AWS resources.
* Use IAM Access Analyzer to generate least-privilege policies based on access activity and to validate your IAM policies to ensure secure and functional permissions.
* Use conditions in IAM policies to further restrict access.
