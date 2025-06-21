# Week 11: Monitoring and Troubleshooting: Tracing

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to [AWS Cloud Operations 2](./aws-cloud-operations-2.md)
* back to repo's main [README.md](../../../README.md)

## VPC Reachability Analyzer

### Pre-assessment

#### What is the purpose of VPC Reachability Analyzer?

* Determines whether a destination resource is reachable from a source resource without sending actual traffic

Wrong answers:

* Monitors and analyzes network traffic flows in a virtual private cloud (VPC)
* Automatically fixes network connectivity issues between resources
* Provisions and configures networking resources like subnets and route tables

##### Explanation

Reachability Analyzer is a service that can examine network connectivity between two endpoints in a VPC without sending any packets or actual traffic.

The other options are incorrect because of the following:

* Reachability Analyzer does analyze network configurations. However, it does not monitor or analyze actual network traffic flows.
* Reachability Analyzer does not automatically fix connectivity issues. It only analyzes and identifies potential configuration problems that might be causing connectivity issues.
* Reachability Analyzer does not provision or configure networking resources like subnets or route tables. It analyzes the existing configurations of these resources to determine potential connectivity between endpoints.

#### What should a cloud engineer do to quickly resolve connectivity issues caused by misconfigurations in their virtual private cloud (VPC)?

* Use VPC Reachability Analyzer to identify any blocking components between source and destination resources.

Wrong answers:

* Review VPC Flow Logs to identify and analyze network traffic patterns.
* Configure and manage VPC connectivity using AWS Transit Gateway Network Manager.
* Delete the VPC and create a new one from scratch.

##### Explanation

Reachability Analyzer is a network configuration analysis tool for VPCs. It can perform a reachability analysis between a source resource and a destination resource. If there is a network misconfiguration, Reachability Analyzer provides information about the component(s) blocking the path.

The other options are incorrect because of the following:

* VPC Flog Logs capture information about IP traffic going to and from network interfaces in a VPC. Flow logs do not directly resolve connectivity issues.
* Transit Gateway Network Manager helps monitor and manage global network resources. It does not directly resolve connectivity issues caused by misconfigurations in a VPC.
* Deleting the VPC and creating a new one should be considered a last resort. It can be time-consuming and might result in data loss or disruption of services.

#### What is the first step when using VPC Reachability Analyzer?

* Verify that the source and destination resources meet requirements.

Wrong answers:

* Create the path.
* Analyze the path.
* View path analysis results.

##### Explanation

The first step when using Reachability Analyzer is to verify that the source and destination resources meet the requirements for the analysis. They must be resources that can connect to a network, such as Amazon EC2 instances, internet gateways, VPC endpoint services, or IP addresses.

The other options are incorrect because of the following:

* Creating the path is the second step after verifying that the source and destination meet requirements.
* Analyzing the path is the third step. It comes after first verifying the resources meet requirements and then creating the path.
* Viewing the path analysis results is the last step.

#### Which requirement must be met for VPC Reachability Analyzer to be able to analyze the connectivity between a source and destination resource?

* They must be in the same AWS Region.

Wrong answers:

* They must be in the same Availability Zone.
* They must be in the same AWS account.
* They must be in the same virtual private cloud (VPC).

##### Explanation

For Reachability Analyzer to check that two resources can connect, the source and destination resources must be in the same Region.

The other options are incorrect because of the following:

* The source and destination resources are not required to be in the same Availability Zone.
* The source and destination resources can belong to different AWS accounts in the same organization from AWS Organizations.
* The source and destination resources must be in the same VPC or in VPCs that are connected through a VPC peering connection or a transit gateway.

### Network Troubleshooting

#### Network issues and their causes

Some types of problems are common across networks. Expand each of the following categories to learn more.

##### Connectivity problems

This is when devices or systems can't connect to the network or the internet. Causes can include faulty cables, misconfigured network settings, or issues with network hardware like routers or switches.

##### Slow network performance

When the network is running slowly, it can make tasks like browsing the web or transferring files frustratingly slow. Common causes include too many devices on the network, bandwidth limitations, or network congestion.

##### Hardware failures

Network hardware like routers, switches, or cables can sometimes fail because of age, physical damage, or manufacturing defects, causing network disruptions.

##### Configuration errors

Incorrectly configured network settings, such as IP addresses, routing tables, or firewall rules, can prevent devices from communicating properly on the network.

##### Software issues

Problems with network software, like outdated drivers or application bugs, can also cause network issues.

#### Network troubleshooting techniques

A consistent troubleshooting technique can help with identifying and resolving network issues. A systematic approach helps make sure that every potential cause is considered and evaluated methodically and efficiently, instead of relying on guesswork or trial-and-error.

A consistent troubleshooting approach typically consists of three overall steps:

1. Gather information
2. Isolate the problem
3. Resolve the issue

___

#### Structured network troubleshooting technique

1. **Gather information: Define the problem**

    In this stage, you work to identify the problem or issue you're experiencing.

    Ask questions like the following:

    * What is the problem I am seeing?
    * What does the error or failure look like?
    * What is failing to connect?

2. **Gather information: Identify failure patterns**

    Then, determine if the issue occurs consistently or intermittently.

    Ask questions like the following:

    * Does it always fail, or does it work sometimes?
    * If it doesn't always fail, why does it work sometimes?

3. **Gather information: Compare good scenarios against bad scenarios**

    Analyze the differences between when the issue occurs and when it doesn't.

    Ask questions like the following:

    * What is the difference between when it does connect and doesn't connect?
    * Why is it only happening for some requests?

4. **Gather information: Understand assumptions**

    Examine the underlying assumptions and how the system or components are expected to work.

    Ask questions like the following:

    * How do Application Load Balancer health checks work?
    * What does the health check do, and why would it fail?
    * How does the web application server connect to the API server?

5. **Gather information: Use observability tools**

    Use available monitoring, logging, and tracing tools to gather more information and identify affected components.

    If necessary, identify ways to gain more visibility into the system or components involved.

    Ask questions like the following:

    * Is there any instrumentation that will help to narrow down the cause?
    * Are there any other AWS services, features, or logs that can help diagnose failed connectivity?
    * Does the application have instrumentation in AWS X-Ray?

6. **Isolate the problem: Process of elimination**

    Systematically rule out potential causes by testing different scenarios or components.

    Ask questions like the following:

    * Is there a way to confirm or rule out the various causes?
    * If I have the working and failing Amazon Simple Storage Service (Amazon S3) URI, what can I check next?
    * Does the problem occur when using a different client or application?

7. **Isolate the problem: Divide and conquer (50/50 method)**

    Divide and conquer as a problem-solving strategy means breaking down the problem into smaller parts and isolating the root cause. In network troubleshooting more specifically, it refers to the idea of selecting a layer and testing its health. Then you move up or down the OSI layers based on the observed results, instead of working bottom-up or top-down. This makes it possible for you to identify the faulty layer by verifying the proper functioning of layers above and below.

    Ask questions like the following:

    * What if I bypass the load balancer and make a request directly to the target? Do I still see the problem?
    * Can I isolate the problem by testing network-level connectivity between two components?
    * Does the issue still occur if I bypass the firewall or security appliance?

8. **Isolate the problem: Identify network configurations**

    Examine network configurations, such as security groups, network access control lists (network ACLs), and route tables, that could affect connectivity.

    Ask questions like the following:

    * What are some reasons that a connection from an Amazon Elastic Compute Cloud (Amazon EC2) instance to another host in another virtual private cloud (VPC) might fail? Security groups? Network ACLs? Route tables?
    * Which tools can help me to identify and troubleshoot any network misconfigurations?

9. **Resolve the issue: Fix and retest**

    After the root cause is identified, research and implement the necessary changes.

    Retest the system to ensure the issue is resolved.

10. **Resolve the issue: Document process and solution**

    Document how you were able to troubleshoot the issue. This should include your findings from the information gathering stage, how you isolated the problem, and how the issue was resolved.

    You might not reference this documentation again yourself, but others on your team might find it helpful in the future.

#### Troubleshooting networks on AWS

AWS provides networking services and components that you can use to create and manage virtual networks in the cloud. Understanding these components is important for troubleshooting network-related issues on AWS.

1. **Virtual private cloud (VPC)**

    A  **VPC** is a logically isolated virtual network in the AWS Cloud. You can launch AWS resources, and control inbound and outbound traffic.

2. **Subnet**

    A **subnet** is a subdivision of a VPC IP address range. You can create multiple subnets in a VPC and assign resources to specific subnets. They can be public or private.

3. **Route table**

    A **route table** contains a set of rules, called routes, that determine where network traffic from your subnet or gateway is directed.

4. **Internet gateway**

    An **internet gateway** is a horizontally scaled, redundant, and highly available VPC component that you can use to communicate between your VPC and the internet. It enables resources in your public subnets to connect to the internet if the resource has a public IP address.

5. **Network access control list (network ACL)**

    A **network ACL** allows or denies specific inbound or outbound traffic at the subnet level. You can use the default network ACL for your VPC, which allows all inbound and outbound traffic. You can also create a custom network ACL for your VPC to add an additional layer of security to your VPC.

6. **Security group**

    A **security group** controls the traffic that is allowed to reach and leave the resources that it is associated with. For example, after you associate a security group with an EC2 instance, it controls the inbound and outbound traffic for the instance.

7. **Elastic network interface (ENI)**

    An **elastic network interface** (also referred to as a network interface) is a logical networking component in a VPC that represents a virtual network card.

8. **Transit gateway**

    A **transit gateway** is a network transit hub that you can use to interconnect your VPCs and on-premises networks.

9. **VPC peering connection**

    A **VPC peering connection** is a networking connection between two VPCs that you can use to route traffic between them using private IP addresses. Instances in either VPC can communicate with each other as if they are in the same network. You can create a VPC peering connection between your own VPCs, or with a VPC in another AWS account. The VPCs can be in different Regions (also known as an inter-Region VPC peering connection).

___

#### Common networking issues on AWS

Most applications use many AWS services and resources deployed across multiple AWS accounts, VPC environments, and AWS Regions. When you deploy your services in VPCs, you might need to configure VPC connectivity to different destinations on the internet and private and hybrid networks. \

1. **Connectivity**

    Connectivity issues refer to problems where resources in your AWS environment are unable to communicate with each other or with external networks.

    For example, you might have an EC2 instance in a subnet of your VPC that you're unable to connect to from your local machine. This could be because of a missing or incorrect internet gateway or NAT gateway configuration. This would prevent the instance from accessing the internet or being accessed from outside the VPC. Verifying your VPC and subnet configurations, including configuring for internet access, can help you to avoid and troubleshoot connectivity issues.

2. **Firewalls**

    Security groups act as virtual firewalls for your EC2 instances, controlling inbound and outbound traffic. Network ACLs act as virtual firewalls for your VPC subnets. Misconfigured security group rules or network ACLs can lead to connectivity issues or security vulnerabilities.

    For example, you might have an EC2 instance running a web server, but you find you're unable to access the website from the internet. Upon checking the security group rules, you realize that the inbound rule allowing HTTP (port 80) traffic is missing or incorrectly configured.

3. **Route tables**

    Route tables determine where network traffic is directed in your VPC. Incorrect or missing route entries can prevent resources from communicating with each other or with external networks.

    For example, imagine that you want to set up a peering connection between two VPCs. However, the connection cannot be established because the subnet associated with one VPC does not have a route to the peered subnet. Analyze the route table entries to make sure that resources from one VPC can communicate with other network components.

4. **Network performance**

    Network performance issues can manifest as slow data transfer speeds, high latency, or packet loss, impacting the overall performance of your applications and services.

    For example, imagine that you have an Amazon EC2 instance running a database server, and you're experiencing slow query response times. Upon investigation, you find that the instance is running in a subnet with a high network traffic load, causing network congestion and performance degradation.

    Proactively monitoring network performance metrics can help you avoid any issues.

#### AWS network troubleshooting tools

To identify and resolve connectivity issues, you need data on VPC components that enable connectivity. These components can include internet gateways, security groups, network ACLs, subnets, route tables, and more. Compiling all this information in one place can be challenging, making it time consuming to troubleshoot network problems. Doing all of this in a timely manner is critical when these connectivity issues can cause application downtime, slow down deployments, or compromise security.

AWS provides tools and services that can help with troubleshooting network issues. These tools include VPC Flow Logs, Traffic Mirroring, and VPC Reachability Analyzer.

1. **VPC Flow Logs**

    With **VPC Flow Logs**, you can capture information about the IP traffic going to and from network interfaces in your VPC. Flow log data can be published to Amazon S3 or Amazon CloudWatch Logs. Flow logs can be used for troubleshooting purposes, such as determining why traffic is not reaching a particular instance. They also can be used as a security tool to monitor the traffic that is reaching your instance.

2. **Traffic Mirroring**

    **Traffic Mirroring** is an Amazon VPC feature that you can use to copy network traffic from a network interface of Amazon EC2 instances. You can then send the traffic to out-of-band security and monitoring appliances for content inspection, threat monitoring, and troubleshooting.

3. **Reachability Analyzer**

    **Reachability Analyze**r is a configuration analysis tool that you can use to perform connectivity testing between a source resource and a destination resource in your VPCs. When the destination is reachable, Reachability Analyzer produces hop-by-hop details of the virtual network path between the source and the destination. When the destination is not reachable, Reachability Analyzer identifies the blocking component. For example, paths can be blocked by configuration issues in a security group, network ACL, route table, or load balancer.

### [Lab: Troubleshooting Website Reachability Behind a Load Balancer](./labs/W110Lab1TroubleshootingWebReachabilityBehindLoadBalancer.md)

A web server is currently running behind an Application Load Balancer. Users are reporting that they are not able to reach the website running on Amazon EC2 instances behind the load balancer.

Your goal is to troubleshoot and fix all the misconfigured issues so that users can access the website. You should still be able to use the load balancer DNS name while ensuring the solution still works if one of the instances is down.

In this lab, you will perform the following tasks:

* Examine the current configuration of the Application Load Balancer and the website running on EC2 instances behind the Application Load Balancer.
* Troubleshoot and identify the issues in the existing configuration, which are preventing users from accessing the website.
* Remediate the configuration so that users can access the website behind the Application Load Balancer and ensure the solution is highly available.

### Reachability Analyzer Functionality and Use Cases

Imagine you are expanding your network design into AWS and deploying a more complex network architecture. A more complex architecture can mean that it takes longer to resolve network connectivity issues caused by misconfiguration. As you update your network design and configure your expanded network, you must verify that each part has been set up correctly.

For example, you might need to ensure that an internet gateway has been created and attached to your VPC. You also might need to check that security groups are configured for outbound traffic. You might need to verify that an elastic IP address is associated with your Amazon EC2 instances. Your network design can help you troubleshoot and diagnose any issues that arise in this process. Your network design document can also help you follow the path of configurations. However, these processes can take additional time.

AWS provides a service called Reachability Analyzer, which can be integrated into your network design process. Reachability Analyzer helps with troubleshooting network issues by verifying connectivity between a source resource and destination resource by using automated reasoning. All resource configurations that can affect the connectivity of your network are inspected to determine if the network flow is possible. This includes components like security groups, routes, firewalls, and so on.

To use Reachability Analyzer, the source and destination resources must be in the same AWS Region. These resources must also be in the same VPC or in VPCs that are connected through a VPC peering connection or a transit gateway. The source and destination resources can belong to different AWS accounts in the same organization from Organizations.

Reachability Analyzer supports the following AWS resource types as sources and destinations:

* Instances
* Internet gateways
* Network interfaces
* Transit gateways
* Transit gateway attachments
* VPC endpoint services
* VPC endpoints
* VPC peering connections
* VPN gateways

Reachability Analyzer also supports IP addresses as destinations.

Reachability Analyzer analyzes all possible paths through your network without having to send any traffic through the network. It looks at the configuration of all resources in your VPCs to determine what network flows are feasible.

#### Using Reachability Analyzer

Troubleshooting your network connectivity issues within a VPC can be time-consuming. Your environment can quickly scale to involve 12 or more AWS services that support routing, protocol, security, access controls, and gateways, all in the support of managing internal and external traffic to servers and services within your environment.

**VPC Reachability Analyzer** provides an easy way to examine network connectivity between two endpoints within your VPC without sending any packets. VPC Reachability Analyzer looks at the configurations of all the resources between the designated endpoints and then determines if it is possible to pass network traffic between them.

For example, imagine you're supporting an environment with two VPCs in the same Region, one dedicated to production and another for development. As part of the development testing process, your development team has asked you to establish a transit gateway peering connection between the two environments. The development team's goal is to enable replication of real-world production data into the development environment to support beta product testing.

To support this change, you update the security groups in each VPC that manage communication for the involved servers. Next, you update the transit gateway peering connection with a route to allow traffic between the production and development database servers.

After these changes are in place, you can use VPC Reachability Analyzer to validate your changes. In this example, because we are looking at the network flow path between two VPCs, you need to repeat the analysis for the second VPC.

##### How it works

1. Configure VPC Reachability Analyzer to analyze the path between the production server and the transit gateway. Note that we are using the ARN for the production server as the source, and the ARN for the transit gateway as the destination. After you initialize the analysis process, results will not take long.
2. VPC Reachability Analyzer will show the results under the Reachability status on the analysis panel. The Reachability status results will indicate any configuration problems between the two endpoints.
3. The Analysis Explorer panel will provide more analysis details using a graphical representation of the network path. This shows what AWS objects are involved in passing or managing data from the source Amazon EC2 instance to the transit gateway. Each object is identified by its ARN and a graphical icon. In this case, the ARN for our production server is labeled as the source. Next is the elastic network interface bound to the EC2 instance. Following is the security group that allows traffic to pass from the subnet to the transit gateway. Then the elastic network interface within the production VPC that is bound to the transit gateway. The last object in the list is the ARN for the transit gateway, which is the endpoint for this network path analysis.
4. Repeating these steps in the development VPC between the development database and the transit gateway will ensure successful implementation of the network portion of this project.

___

**Amazon Resource Names (ARNs) uniquely identify AWS resources. An ARN is required when you need to specify a resource unambiguously across all of AWS. This includes when selecting a source resource and destination resource for Reachability Analyzer.**
___

#### How Reachability Analyzer works

Before you begin, verify that your source and destination resources meet the requirements.

1. **Create a path**

    The first step is to specify the path of communication for the traffic from a source to a destination for any of the following endpoint types: 

    * VPN gateways
    * Instances
    * Network interfaces
    * Internet gateways
    * VPC endpoints
    * VPC peering connections
    * Transit gateways

    The source and destination resources must be the following:

    * Owned by the same AWS account
    * In the same AWS Region
    * In the same VPC or in VPCs that are connected through a VPC transit gateway or peering connection

    In the case of a shared VPC, the resources can belong to different AWS accounts in the same organization from AWS Organizations.

2. **Analyze the path**

    After you create the path, Reachability Analyzer analyzes the path once. You can analyze a path at any time to determine whether your intended connectivity is supported, even as your network configuration changes.

    For example, set instance A for source and instance B for destination. You can choose to check for connectivity through either the TCP or UDP protocols. Optionally, you can also specify a port number, source, or destination IP address. To test the connectivity between instance A and instance B within the same subnet, the Reachability Analyzer would begin at your designated entry point, instance A. It would:

    * Check if there is a network interface attached to that instance and check the outbound traffic on the security group.
    * Begin the journey to the other instance by checking its security group for inbound rules that apply at the network interface.
    * Arrive at the destination instance, instance B.

    If the instances were in different subnets, it would also check the network ACLs for appropriate rules.

    You can run a reachability analysis between two network interfaces or between a network interface and a gateway. If there is a reachable path between the source and destination, Reachability Analyzer displays the details. If not, Reachability Analyzer identifies the blocking component.

3. **View the results of the path analysis**

    After the path analysis completes, you can view the results. When the destination is:

    * **Reachable**, the Reachability Analyzer produces hop-by-hop details of the virtual network path between the source and the destination.
    * **Not reachable**, the Reachability Analyzer identifies the blocking component. Paths can be blocked by configuration issues in a security group, network ACL, route table, or load balancer. If a destination is not reachable, Reachability Analyzer provides one or more explanation codes to help you diagnose and address network misconfiguration. For example:
      * **ENI_SG_RULES_MISMATCH** means the security group has no inbound or outbound rules that apply.
      * **TGW_ROUTE_AZ_RESTRICTION** means the transit gateway is not registered in the Availability Zone where the traffic originates.

4. **Change network configuration and analyze the path**

    If the reachability status does not match your intent, you can change your network configuration. Then you can analyze the path again to confirm that the reachability status matches your intent.

    For example, you could specify:

    * Internet gateway as the source
    * Amazon EC2 instance as the destination
    * Port 22 as the destination port
    * TCP as the protocol

    This would help to verify that you can connect to the EC2 instance through the internet gateway using Secure Shell (SSH).

    If there are multiple reachable paths between a source and a destination, Reachability Analyzer identifies and displays the shortest path. You can analyze the path again, specifying an intermediate component, to find an alternative reachable path that traverses the intermediate component.

5. **Summary**

    Steps for setting up and using Reachability Analyzer:

    1. Verify that the source and destination resources meet requirements.
    2. Create the path.
    3. Analyze the path.
    4. View the results of path analysis.
    5. Change network configuration and analyze the path (if needed).

___

#### Reachability Analyzer use cases

VPCs are user-configured networks that include compute devices, resources, networking components, access controls, and so on. This gives you the ability to design and configure your network to your specific use cases. However, as your VPC grows, so does the complexity. Reachability Analyzer helps to automate, identify, and resolve misconfigurations. It also helps to maintain the security and availability of your applications through all infrastructure changes.

Reachability Analyzer uses automated reasoning to look at all the resource configurations that can affect the connectivity and determines whether the network flow is possible. In a network configuration, sometimes something can block resources from communicating with each other. This means the resources cannot communicate with each other, which means the network is not working. The root cause of the issue is usually overlapping or conflicting configurations. This highlights the importance of updating a network design as the environment changes.

Reachability Analyzer is not limited to checking if resources within or across VPCs can communicate with each other. You can also use Reachability Analyzer when launching an Amazon EC2 instance that requires internet access into a private subnet. You can use Reachability Analyzer to make sure that the EC2 instance can reach the internet.

Reachability Analyzer can help your network design by addressing some common use cases.

##### Connectivity issues

*Troubleshooting connectivity issues caused by network misconfiguration*

Imagine you have an Amazon EC2 instance in a private subnet. It is unable to connect to an Amazon Relational Database Service (Amazon RDS) database in another private subnet within the same VPC. You suspect a network misconfiguration issue, but you're unsure where the problem lies.

With Reachability Analyzer, you can create a reachability analysis to test the connectivity between the EC2 instance (the source) and the RDS database (the destination). The analysis will evaluate all the network components involved, such as security groups, network ACLs, route tables, and subnet configurations. If there's a misconfiguration preventing connectivity, the analysis will identify the specific component and the reason for the connectivity issue. This will help you to troubleshoot the problem more efficiently.

##### Network design verification

*Verifying that your network configuration matches your intended connectivity*

Imagine you have a complex VPC setup with multiple subnets, security groups, and network ACLs to support different application tiers and environments. You want to ensure that your network configuration aligns with your intended connectivity design, which specifies allowed and denied traffic flows between resources.

With Reachability Analyzer, you can create reachability analyses to test the connectivity between various source and destination resources in your VPC. By defining the expected connectivity intent (allowed or denied) for each analysis, you can verify that your network configuration matches your design. If there are any connectivity issues, the analysis will highlight them and help you to identify any departures from the intended network design.

##### Automate verification of design changes

*Automating the verification of your connectivity intent as your network configuration changes*

Imagine that your organization has a continuous integration and continuous deployment (CI/CD) pipeline for deploying infrastructure changes to your VPC environment. You want to ensure that any network configuration changes introduced during the deployment process do not inadvertently break the intended connectivity between resources.

With Reachability Analyzer, you can create reachability analyses that represent your connectivity intent and automate their implementation as part of your CI/CD pipeline. Whenever a new deployment introduces network configuration changes, the automated analyses will run and validate that the connectivity between resources remains as intended. If any issues are detected, the pipeline can be halted and notifications can be sent to the appropriate teams for investigation and resolution. This helps to minimize the impact of connectivity disruptions in your production environment.

##### VPC resource reachability

Determining whether a destination resource in your VPC is reachable from a source resource

Imagine you have a web application running on an Amazon EC2 instance in a public subnet. It requires access to an Amazon ElastiCache cluster in a private subnet for caching. Before deploying the application, you want to ensure that the EC2 instance can reach the ElastiCache cluster as intended.

With Reachability Analyzer, you can create a reachability analysis to test the connectivity between the EC2 instance (the source) and the ElastiCache cluster (the destination). The analysis will evaluate all the network components involved, such as security groups, network ACLs, route tables, and subnet configurations. If the analysis determines that the ElastiCache cluster is reachable from the EC2 instance, you can proceed with the deployment. If not, the analysis will provide insights into the connectivity issue, supporting you to address it before deploying the application.

### Activity: Troubleshooting with Reachability Analyzer

The network design for the application uses VPCs connected through transit gateway peering with a Gateway Load Balancer. The workload runs on two Amazon EC2 instances in two different Availability Zones.

The team has realized that they cannot route packets between the ywo EC2 instances in the different VPCs.

The VPCs belong to the same AWS account, and they are in the same AWS Region. The teams has already set up security group rules to allow traffic between the two servers.

#### Which tool can help troubleshoot a blocked path between two EC2 instances in different VPCs?

* VPC Reachability Analyzer

Wrong answers:

* VPC Flow Logs
* AWS Config

___

Reachability Analyzer can determine if the destination is reachable by identifying a path from the source to the destination. Paths can identify relevant VPC configuration details such as the routes, firewall rules, or other settings admitting the packet at each step. If a blocked path is identified, Reachability Analyzer produces reasons for the blocked path throughout as the packet travel from source to destination.

#### The current design for the application is configured to keep traffic in the same availability Zone where it originated until it reaches its destination. But the actual flow of the traffic to and from the two instances for the application is directed to two different firewalls in the two different Availability Zones. Using Reachability Analyzer, you identify that the communication is being blocked between the two instances. The current design for teh application has the VPC attachments in separate Availability Zones, which results in asymmetric routing of the packets. This happens by default when traffic is not specifically configured to route between the VPC attachments with a transit gateway and a Gateway Load Balancer. What is teh MOST efficient way to resolve this?

* Enable the appliance mode feature of the transit gateway to ensure symmetric routing of traffic.

Wrong answers:

* Modify the security group rules of the EC2 instances to allow traffic between them.
* Delete the current network setup and re-create the VPCs in the same availability Zone.

___

When appliance mode is enabled, a transit gateway selects a single network interface in the appliance VPC to send traffic to, for the life of the flow. The transit gateway uses the same network interface for the return traffic. This ensures that bidirectional traffic is routed symmetrically - it's routed through the same Availability Zone in the VPC attachment for the life of the flow.
___

#### Why is VPC Reachability Analyzer a suitable troubleshooting tool for this scenario?

* It can verify connectivity between the two endpoints, and also diagnose any blocked paths with the application updates or updated configurations.

Wrong answers:

* It can automatically reconfigure the transit gateway and VPC attachments to resolve and connectivity issues that it detects.
* It can monitor and analyze the performance of the AWS Site-to-Site VPN connection and the transit gateway, ensuring optimal network throughput.

___

Reachability Analyzer can verify connectivity between endpoints such as a transit gateway with an AWS Site-toSite VPN attachment and the internal application hosted in the VPC.

To resolve connectivity issues automatically, you can configure Reachability Analyzer with Amazon CloudWatch to alert on and probably automatically remediate any issues using AWS Lambda.

___

#### The original network design consisted of two transit gateways: A transit gateway in the us-east-2 Region and another transit gateway in the us-west-2 Region. Each transit gateway had one VPC and one VPN attachment. The new update to the design added a second VPN attachment to the us-west-2 Region. Can VPC Reachability Analyzer be used to troubleshoot this scenario?

* Yes, because it can verify the connectivity through the transit gateways and diagnose any blocked paths.

Wrong answers:

* No, because the source and destination resources must be in the same AWS Region.
* No, because the sources and destination resources must be in the same VPC.

___

Using two VPCs and a transit gateway, your traffic can hop through multiple elastic network interfaces before it ends up at its destination. This makes it difficult to diagnose issues with your traffic through your transit gateways. Now with the new VPN attachment, VPC Reachability Analyzer can help you verify the connectivity and troubleshoot any blocked paths for the global network.

___

#### Summary

Reachability Analyzer can be useful as a tool to verify and troubleshoot network-level connectivity. It can be used in scenarios that involve multiple VPCs, transit gateways, and AWS Site-to-Site VPN attachments. Even in global networks, Reachability Analyzer can be used to verify the connectivity of individual network path segments.

### Reachability Analyzer

#### A network engineer must troubleshoot a blocked path between two Amazon EC2 instances in a virtual private cloud (VPC). The path might be blocked because of configuration issues in a security group, network access control list (network ACL), route table, or load balancer. Which AWS service can help identify the blocking component in this network?

* VPC Reachability Analyzer

Wrong answers:

* AWS CloudTrail
* AWS X-Ray
* AWS Transit Gateway Network Manager

##### Explanation

When there is a blocked network path, Reachability Analyzer displays information about the component or combination of components that is blocking the path.

The other options are incorrect because of the following:

* CloudTrail is a service that provides auditing of AWS account activity. It is not designed to troubleshoot blocked network paths.
* X-Ray is a service that analyzes and helps with troubleshooting distributed applications. It is designed to trace application-level requests, not troubleshoot network-level requests.
* Transit Gateway Network Manager can help to monitor transit gateways and provide global network visibility. It is not designed to provide troubleshooting for network connectivity.

#### A video game company has a complex virtual private cloud (VPC) setup. It includes multiple subnets, security groups, and network access control lists (network ACLs) to support different application tiers and environments. The company plans to roll out a substantial update to its network design. Which capability of VPC Reachability Analyzer can help the company verify that the updated network configuration matches its intended connectivity design?

* Reachability analyses to test connectivity between resources

Wrong answers:

* Continuous monitoring of network traffic flows
* Integration with AWS Config for resource inventory
* Visualization of network topology diagrams

##### Explanation

Reachability Analyzer can be used to verify that any changes to network configuration match the intended connectivity.

The other options are incorrect because of the following:

* Reachability Analyzer does not provide continuous monitoring of network traffic flows.
* AWS Config can help you manage resource configuration changes, but it is not designed to integrate with Reachability Analyzer to verify network connectivity.
* Reachability Analyzer can help this company verify its network topology diagrams, but it is not designed to provide such a visualization.

#### Which resource types can be used as a source or destination resource in VPC Reachability Analyzer? (Select THREE.)

* VPN gateways
* Network interfaces
* EC2 instances

Wrong answers:

* AWS Lambda functions
* Amazon S3 buckets
* AWS CloudFormation stacks

##### Explanation

Reachability Analyzer analyzes the path of connectivity between source and destination resources. These are components that can connect to a network using protocols like TCP or UDP.

The other options are incorrect because of the following:

* Lambda functions are serverless compute resources and not a supported resource type.
* S3 buckets are object storage resources and are typically accessed over HTTP. They are not reachable sources or destinations for Reachability Analyzer.
* CloudFormation stacks are infrastructure-as-code resources and not a valid source or destination in Reachability Analyzer.

#### An engineering team plans to verify changes to its network configuration using VPC Reachability Analyzer. It must check that an Amazon EC2 instance can make requests to an Amazon RDS database in a different virtual private cloud (VPC) in the same Region. Which additional condition must be met for VPC Reachability Analyzer to be used?

* The VPCs must be connected through a VPC peering connection or a transit gateway.

Wrong answers:

* The EC2 instance and RDS database must be in the same Availability Zone.
* The EC2 instance and RDS database must be in the same AWS account.
* Reachability Analyzer cannot be used here, because the EC2 instance and RDS database must be in the same VPC.

##### Explanation

For VPC Reachability Analyzer to verify connectivity between resources, they must either be in the same VPC or in connected VPCs.

The other options are incorrect because of the following:

* The EC2 instance and RDS database are not required to be in the same Availability Zone.
* The source and destination resources can belong to different AWS accounts if they are in the same organization from AWS Organizations.
* Resources can be in different VPCs if they are connected through a VPC peering connection or transit gateway.

### Summary

Reachability Analyzer is a configuration analysis tool that can perform connectivity testing between a source resource and a destination resource in VPCs. When the destination is reachable, Reachability Analyzer produces hop-by-hop details of the virtual network path between the source and the destination. It inspects resource configurations (such as security groups, routes, and firewalls) that can affect network connectivity to determine if the network flow is possible.

To use Reachability Analyzer, the source and destination resources must be in the same AWS Region. Additionally, they must be either in the same VPC or in VPCs connected through a VPC peering connection or a transit gateway. Reachability Analyzer supports various AWS resource types as sources and destinations. These resource types include EC2 instances, internet gateways, network interfaces, transit gateways, VPC endpoints, VPC peering connections, and IP addresses.

Reachability Analyzer analyzes possible paths through your network without sending any packets, making it a useful tool for verifying and troubleshooting connectivity between network resources. If multiple paths are available, Reachability Analyzer identifies the shortest path between two resources.

When the destination is not reachable, Reachability Analyzer identifies the blocking component. For example, paths can be blocked by configuration issues in a security group, network ACL, route table, or load balancer. For unreachable paths, Reachability Analyzer provides an explanation code and detailed information about the component or combination of components that is blocking the path.

Reachability Analyzer can help address the following common networking use cases:

* Connectivity issues
* Network design verification
* Automate verification of design changes
* VPC resource reachability

## Tracing with X-Ray

### Pre-assessment

#### What are the benefits of using AWS X-Ray? (Select TWO.)

* View detailed insights into application latency and bottlenecks
* Integrate with AWS Lambda functions and other AWS services

Wrong answers:

* Detect and identify unused services
* Detect threats and automate incident response in real time
* Apply fine-grained access control and authentication mechanisms

##### Explanation

X-Ray is designed to provide detailed insights into how a distributed application handles requests. This data can help customers troubleshoot any issues and optimize application performance. X-Ray also provides seamless integration with Lambda and other AWS services.

The other options are incorrect because of the following:

* X-Ray can help identify performance issues, but is not designed to detect and identify unused services. Services like Amazon CloudWatch or AWS Trusted Advisor can be used to identify unused or underutilized services.
* X-Ray trace data can help provide audit trails and logs for security and compliance purposes. However, it is not designed to detect threats and automate responses. Services like Amazon GuardDuty and Amazon Inspector can be used for threat detection and response.
* As mentioned previously, X-Ray trace data can help with security and compliance. However, X-Ray is not designed to apply fine-grained access control and authentication mechanisms. Services like AWS Identity and Access Management (IAM) and Amazon Cognito can be used to provide fine-grained access control and authentication.

#### Which statement correctly describes the relationship between traces, trace maps, and segments in AWS X-Ray?

* A trace represents a single request, a trace map visualizes a single request, and segments represent individual components or services involved in the request.

Wrong answers:

* A trace represents a single request, a trace map visualizes the entire application, and segments represent individual components or services involved in the request.
* A segment represents multiple trace maps, a trace map visualizes a single request, and a trace represents individual components or services involved in each request.
* A trace is a collection of trace maps, a trace map visualizes the entire application, and segments represent individual requests within a trace.

##### Explanation

In X-Ray, a trace map is a visual representation of a single trace. A trace captures the end-to-end journey of a request as it travels through your application. Segments represent the individual components or services involved in each trace.

The other options are incorrect because they do not correctly describe the relationship between traces, trace maps, and segments.

#### How does AWS X-Ray improve the tracking of requests across distributed application components? (Select TWO.)

* Correlating data across services
* Using a user-centric model

Wrong answers:

* Managing log formats
* Monitoring network traffic
* Providing a SQL querying language for traces

##### Explanation

X-Ray improves tracking of requests across distributed application components by correlating the data across application components. It also uses a user-centric model instead of a service-centric or a resource-centric model. With this, you can create a user-centric picture of requests as they travel across services and resources.

The other options are incorrect because of the following:

* X-Ray does not manage log formats. Amazon CloudWatch is designed to help you organize and manage logs from different sources.
* X-Ray does not monitor network traffic. It monitors requests to your application components and downstream services.
* X-Ray does not provide a SQL querying language. It does provide a filter expression language.

#### How do the AWS X-Ray SDK and the X-Ray daemon work together in an instrumented application?

* The X-Ray SDK sends trace data to the X-Ray daemon, which then relays it to the X-Ray service.

Wrong answers:

* The X-Ray daemon sends trace data to the X-Ray SDK, and the X-Ray SDK sends it to the X-Ray service.
* The X-Ray daemon instruments your application code, and the X-Ray SDK processes the trace data.
* The X-Ray SDK and the X-Ray daemon work independently and do not interact with each other.

##### Explanation

The X-Ray SDK is used to instrument application code to generate trace data. However, instead of sending this data directly to X-Ray, the SDK sends it to the X-Ray daemon. The daemon is an agent that listens for traffic on UDP port 2000 and receives the trace data (segments) from the X-Ray SDK. The daemon then buffers these segments in a queue and uploads them to the X-Ray service in batches.

The other options are incorrect because they do not correctly describe the interaction between the X-Ray SDK and the X-Ray daemon.

### X-Ray Features and Functionality

Imagine that you are running a distributed application, with multiple components that requests pass through. A request through such an application might consist of many calls to databases, applications, and web services. These components might run in on-premises servers, Amazon EC2, containers, AWS Lambda, or other AWS services. You might have dozens, if not hundreds, or even thousands of integration points in a distributed application.

X-Ray is a service that can help you troubleshoot and optimize your distributed applications. X-Ray helps you understand how your application and its underlying services are performing. With this information, you can identify and troubleshoot the root cause of performance issues and errors.

X-Ray gives you a visual representation of your services—a service map—that illustrates each integration point, and gives you quick insight into successes and failures. Then, you can drill down into the details of each individual trace.

You can enable X-Ray with one click for Lambda, API Gateway, and Amazon SNS. You can also turn it on for SQS queues that are not Lambda event sources, and you can add custom instrumentation to your function using the X-Ray SDK to write your own code.

X-Ray integrations support both active and passive instrumentation. Active instrumentation samples and instruments incoming requests. Services that support active instrumentation write traces to X-Ray. Passive instrumentation instruments requests that have been sampled by another service. Services that support passive instrumentation can’t create traces, but can add information to them.

Integration with Lambda supports active and passive instrumentation of incoming requests on all runtimes. Lambda adds two nodes to your service map: one for the Lambda service, and one for the function itself.

When you trace your Lambda function, the X-Ray daemon automatically runs in the Lambda environment to gather trace data and send it to the X-Ray service.

API Gateway also supports both active and passive instrumentation. API Gateway uses sampling rules to determine which requests to record, and adds a node for the gateway stage for your service map.

X-Ray integration with Amazon SNS supports passive instrumentation. If an SNS publisher traces its client with the X-Ray SDK, subscribers can retrieve the tracing header and continue to propagate the original trace from the publisher with the same trace ID.

Amazon SQS also supports passive instrumentation. If a service traces requests by using the X-Ray SDK, SQS can send the tracing header and continue to propagate the original trace from the sender to the consumer with a consistent trace ID.

You can use groups to apply custom filters, based on your expected thresholds for things like latency or errors. You also get built-in analytics that bucket your individual traces into categories and give you a time-series distribution.

#### X-Ray features

With X-Ray, you can gain insights into the requests that your distributed application serves to identify issues and opportunities for optimization. X-Ray provides tools that you can use to quickly view, filter, and analyze the collected data from your application.

X-Ray makes it convenient for developers to analyze the behavior of their distributed production applications with end-to-end tracing capabilities. It creates a map of your underlying application components. You can use X-Ray to identify performance bottlenecks, edge case errors, and other hard-to-detect issues.

X-Ray supports applications of any type or size, whether in development or production. It covers basic asynchronous event calls and three-tier web applications, in addition to complex microservices-based distributed applications. Developers can quickly find and address problems in their applications and improve the experience for end users of their applications.

To use X-Ray, you must first instrument your application so that X-Ray can track how your application handles a request. Instrumenting your application means adding code or other integrations that enable your application to generate and send trace data to X-Ray.

X-Ray can provide trace information about any received responses and calls that an instrumented application makes, including the following:

* Downstream AWS resources
* Microservices
* Databases
* Web APIs

You can use trace data and visualizations to gain insights into your application's performance, identify issues, and find opportunities for optimization. You can also use analysis tools in X-Ray to view, filter, and investigate details for any traced request to your application.

##### How X-Ray works

X-Ray helps you analyze and debug modern applications built using microservices and serverless architecture. As mentioned previously, to use X-Ray, you must first instrument your application so that X-Ray can track how your application handles a request. Adding instrumentation to your application lets X-Ray send trace data and metadata for incoming and outbound requests and other events within your application.

You can instrument your application in three different ways:

* **Auto instrumentation**: Instrument your application with zero code changes, typically through configuration changes, adding an auto-instrumentation agent, or other mechanisms.
* **Library instrumentation**: Make minimal application code changes to add pre-built instrumentation targeting specific libraries or frameworks, such as the AWS SDK, Apache HTTP clients, or SQL clients.
* **Manual instrumentation**: Add an instrumentation code to your application at each location where you want to send trace information.

X-Ray tracks data in instrumented applications through different components called traces, segments, and subsegments.

Imagine you're planning a cross-country road trip. The entire journey from start to finish can be considered a trace. Within this trace, you will have different legs or stages of the trip. For example, driving from one city to another or stopping at a certain location. You can think of these stages as segments. In each segment, you might have smaller events or activities, such as stopping for gas, getting food, or taking a short detour. These smaller events within a segment are called subsegments. You will learn more about these components in the next section. By breaking down a request's journey through your distributed application into traces, segments, and subsegments, X-Ray can provide a detailed view of how your application is performing.

The following diagram depicts how X-Ray collects and processes data from a data request. To learn more, choose each numbered marker.

![Diagram of four icons of how X-Ray works.](./images/W11Img010XRayDataCollection.png)

1. **Collect traces**

    The distributed application receives a request for data. You can collect data about the request from each of the underlying service nodes, or components, that the request passes through.

    You can add an AWS collector or agent, such as the X-Ray daemon, to your components to collect trace data.

2. **Record traces**

    As the data request passes through application components, the AWS collector or agent collects the trace id and segments.

    This data is sent to a tracing framework, which combines the data gathered from each service into singular units, or traces.

    The tracing framework can interact with other AWS services and track trace data during these interactions as well.

3. **View service map**

    X-Ray collects the request data and sends it to a console graphical user interface (GUI).

    X-Ray uses trace data to generate a detailed trace map. The trace map shows the services that are called in a single request. Use the trace map to identity bottlenecks, latency spikes, and other issues.

    X-Ray also generates a service map that provides an overall view of how your application interacts with your service components.

4. **Analyze issues**

    You can drill into the service that is showing unusual behavior to identify the root issue of any errors or latency in your application.

#### X-Ray use cases

What specific problems does X-Ray solve? Without X-Ray, tracking requests across distributed application components requires per-service or per-resource processes. This is because a request travels across many different individual components in a distributed application. The problem is further complicated by the varying log formats and storage media across the frameworks, services, and resources that your application might use. This makes it difficult to correlate the various pieces of data and create an end-to-end picture of a request.

To solve this problem, X-Ray provides a user-centric model, instead of a service-centric or resource-centric model, for collecting data related to requests made to your application. With this approach, you can create a user-centric picture of requests as they travel across services and resources.
___

**X-Ray correlates and aggregates data on your behalf, so you can focus on improving the experience for end users of your application.**
___

##### Analysis and debugging

Receive trace data from your basic and complex applications, whether they are in development or production. X-Ray provides a detailed breakdown of the requests flowing through your application, including information about the different services and resources involved. This makes it convenient to identify issues, diagnose errors, and troubleshoot problems within your application.

##### Detailed service maps

Compile data from your AWS resources to determine bottlenecks in your cloud architecture and improve application performance. X-Ray generates a service map that illustrates the architecture of your application and shows how different components interact with each other. This visual representation helps you understand the dependencies between services and identify areas for optimization and potential bottlenecks.

##### Performance analytics

X-Ray can be used to profile your application's performance by identifying hotspots and bottlenecks. It can help you understand which parts of your code are consuming the most resources or taking the most time, so you can optimize your application's performance. Compare trace sets with different conditions for root cause analysis purposes.

##### Secure data audits

You can configure X-Ray to help meet your security and compliance objectives. X-Ray trace data can help provide audit trails and logs for security and compliance purposes.

#### X-Ray benefits

X-Ray provides several benefits for developers and operations teams working on distributed applications.

##### Distributed tracing

X-Ray provides end-to-end tracing capabilities, so developers can trace requests as they flow through various services and resources. This helps in understanding the complete request path and identifying performance bottlenecks or errors across different components.

##### Improved troubleshooting

With detailed tracing information and insights into request flows, developers can quickly pinpoint the root cause of issues and troubleshoot them more effectively. This reduces the time spent on debugging and resolving problems, leading to faster issue resolution and improved application reliability.

##### Performance insights

X-Ray visualizes the latency and duration of each component so developers can pinpoint performance bottlenecks in their application's request processing. This information helps in optimizing the application's architecture and resource allocation to improve overall performance.

##### Service map

X-Ray automatically generates a service map that visualizes the dependencies between different components of an application. This helps developers understand how services interact and identify potential points of failure or bottlenecks. It also aids in managing complex architectures and ensuring smooth integration between services.

##### Real-time monitoring and alerting

X-Ray continuously monitors application performance and provides real-time insights into latency, error rates, and other metrics. Developers can set up alarms and notifications based on specific thresholds. They will receive alerts when performance issues occur, so they can take proactive measures to address them.

##### Integration with AWS services

X-Ray integrates with other AWS services, such as Lambda, Amazon EC2, Amazon API Gateway, and AWS Elastic Beanstalk. With this integration, developers can gain deeper insights into the performance and behavior of these services. This facilitates comprehensive monitoring and optimization of the entire application stack.

##### Support for multiple programming languages

X-Ray supports tracing for applications that are written in Node.js, Java, and .NET. Developers can use X-Ray with their preferred programming language without any limitations.

#### Summary

X-Ray is designed to provide application-level request tracing to troubleshoot and optimize distributed applications. Applications instrumented with X-Ray can send trace data to the X-Ray API. This aggregates data from different application components and displays it in user-centric and request-centric maps.
