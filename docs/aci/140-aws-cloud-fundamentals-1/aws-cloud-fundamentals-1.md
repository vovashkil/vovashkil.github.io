###### back to AWS Cloud Institute repo's root [aci.md](../aci.md)
###### back to repo's main [README.md](../../../README.md)
# AWS Cloud Institute
## AWS Cloud Fundamentals 1
### Week 1: Compute 2 Part 1
### Week 2: Compute 2 Part 2
### Week 3: Networking 2 Part 1
### Week 4: Networking 2 Part 2

#### AWS transit solutions
* Without a transit gateway: VPN and AWS Direct Connect are 1:1 relationship with VPC.
* With a transit VPC. Runs on Amazon EC2. Requires vendor OS knowledge (software routing solution to route traffic to VPCs). Segmentation requires complex access lists. Cost of licensing. Scaling is limited by hardware.
* With a Transit Gateway: acts as a cloud router to simplify your network architecture. The complexity of managing incremental connections doesn’t slow you down. You can connect transit gateways using inter-Region peering.

#### Transit Gateway use cases
* Centralized route - connects all your VPCs, AWS Direct Connect, and Site-to-Site VPN connections. In this scenario, all attachments are associated with the transit gateway default route table and propagate to the transit gateway default route table. Therefore, all attachments can route packets to each other with the transit gateway serving as a layer 3 IP router.
* Isolated VPCs. You can configure your transit gateway as multiple isolated routers. This is similar to using multiple transit gateways, but it provides more flexibility in cases where the routes and attachments might change. In this scenario, each isolated router has a single route table. All attachments associated with an isolated router propagate and associate with its route table. Attachments associated with one isolated router can route packets to each other, but they cannot route packets to, or receive packets from, the attachments for another isolated router.
* Isolated VPCs with shared services. 
* Peering. You can create a transit gateway peering connection between transit gateways in the same AWS Region or in different Regions.

**All AWS resources have an account owner. Transit gateways are specific to an account. Users do not have the permissions to attach VPCs to a transit gateway that is owned by another account.**

#### AWS Transit Gateway
It's a way to simplify design to reduce the number of peering and VPN connections.

* Attachment based
* Flexible routing and segmentation
* Connectivity simplified
* Highly available/scalable
* Increased monitoring capabilities
* Multicast support

#### Transit Gateway components:
* VPC route tables
* VPC
* VPN connection
* Direct Connect gateway
* Transit gateway route table
* Transit gateway

#### Transit Gateway setup
* A transit gateway is a Reginal resource
* AWS Transit Gateway is a managed service

Networks: VPC, VPN connection, Direct Connect gateway - are attachments.

Setup:
* Attach VPCs, VPN, and Direct Connect **gateway** (not just a Direct Connect) connections.
* Network attachments must be in the same Region as the transit gateway.
* An attachment is both a source and a destination.

Connect to a transit gateway (for example, VPC) mean to **attach** the VPC to the transit gateway.

#### Direct Connect routing to a transit gateway
* Note that Direct Connect links must use Direct Connect gateway to attach to a transit gateway
* Easier network management

if we have Direct Connect, we can use a Direct Connect gateway, and the Direct Connect gateway can connect to transit gateways. 

For the Direct Connect, the transit gateway that you're connecting to doesn't have to be in the same Region. Because remember, the DX (Direct Connect) gateway allows you to connect to the VPCs that are in different Regions. It also allows you to connect to transit gateways that are in different Regions over here too. The Direct Connect gateway is required to get connected back into the transit gateway.

#### Transit gateway setup
* Enable one or more Availability Zone in an attachment VPC for the transit gateway to use.
* In each Availability Zone, you specify exactly one subnet.
* The transit gateway places a network interface in the subnet.

**Best practice*** is to create an empty subnet, that its sole purpose is for basically that interface for the transit gateway.

* In the VPC route table, add a route to the transit gateway.

Every single VPC has route tables. It says when you're gonna send the traffic to the transit gateway. When you attach the VPC to the transit gateway, we're gonna have a route table on the transit gateway that is associated with that particular network that you attached. That route table on the transit gateway gets associated with that VPC. The purpose for that association is as soon as the traffic comes into the transit gateway, the route table that's associated is gonna define as to what the possible routes are as to where that could actually go. 

* Transit gateway acts as a Regional virtual router.
* Routing operates at layer 3 with packets sent to specific next-hop.
* Targets for routes defined in the transit gateway route table are to other attachments.

* Each attachment is associated with a single transit gateway route table.
* Attachments can share the sane route table.
* The default transit gateway route table allows all attachments to communicate with each other.
* It is similar to a peering connection without as many connections to manage.

* You can create additional route tables for different attachments.
* Routes defined in the transit gateway route tables can create traffic isolation between attachments.

* Peer transit gateways across Regional boundaries.
* Add static routes to the peered gateway.
* Does not support resolving public IPv4 DNS host names to private IPv4 addresses across VPCs.

#### Transit gateway use cases 2
* Centralized route:
 * All attachments can route traffic to each other.
* Isolated VPCs:
 * Configure your transit gateway as multiple isolated routers.
 * Each isolated router has a single route table.
* Isolated VPCs with shared services: 
 * VPCs A, B, and C are isolated from each other.
 * All VPCs can communicate with VPC D.
 * Run shared services on VPC D.
* Peering
 * Create a peering connection between gateways across Regions.
 * Static routing. 

Examples of shared services: 
* NAT gateways
* intrusion detection
* network firewall
* route the traffic through for things like packet inspection

With a Transit Gateway you can still create a Peering connection.

#### NAT gateway as a shared service
* VPC A (10.1.0.0/16), VPC B (10.2.0.0/16), Outbound PVC (with NAT Gateway), Transit gateway.
 1. VPC A, VPC: 0.0.0.0/0 -> TSW (Transit Route)
 2. Transit gateway route table 1:
  * 0.0.0.0/0 -> Outbound VPC
 3. Transit gateway route table 1:
  * 10.0.0.0/8 -> Blackhole (VPC A and VPC B can't talk directly!!!)
 4. Outbound VPC Route table Egx 1:
  * 0.0.0.0/0 -> NAT GW-1
 5. Internet gateway route:
  * 0.0.0.0/0 -> IGW
  * 10.0.0.0/8 -> TGW
 6. Transit gateway route table 2:
  * 10.1.0.0/16 -> VPC A
  * 10.2.0.0/16 -> VPC B

#### Transit gateway best practices
* Use separate subnet for each VPC attachments.
* Associate one network ACL to all subnets associated with the transit gateway.
* Transit gateways are highly available by design.
* Use BGP Site-to-Site VPN connections.
* Limit the number of transit gateway route tables used.

#### Transit gateway notes
##### Key metrics
* BytesIn
* BytesOut
* PacketsIn
* PacketsOut

##### Key quotas
* 5 per Region, per account
* 20 route table per gateway
* 5000 attachments per gateway

##### Cost components
* Per attachment
* Per GB of data processed

**Peering connections** don't cost money and don't charge per GB of traffic.

#### Transit Gateway Network Manager
* Visual global monitoring tool
* Create a global network of AWS and on-premises resources to monitor.
* Register transit gateways that are in the same account.
* Transit gateway attachments are automatically included in the global network.
 
 #### Transit Gateway Network Manager setup
1. Create your network
2. Register your transit gateway
3. (Optional) Define and associate your on-premises network resources:
 * Sites
 * Links
 * Devices
4. Monitor your network

##### Transit gateway demo
* "default association route table"
* "disassociate the subnets from the route table"

1. You leave that default association route table propagation setting on, that as soon as you do your attachments, your attachments will automatically be added to the default route table.
2. We disassociate the route tables from the default and we reassociate them with those separate route tables.

#### VPC Reachability Analyzer
* Analyze reachability between two endpoints without sending any packets
* Troubleshoot misconfigurations
* Verify intended connectivity
* Automate verification

You put Source and Destination.

#### VPC endpoint solutions
There are two types of VPC endpoints: interface endpoints and gateway endpoints. Create the type of VPC endpoint required by the supported service as follows:
* **Interface endpoint**: An interface endpoint is an elastic network interface with a private IP address (from the IP address range of your subnet). It serves as an entry point for traffic destined to a supported service. PrivateLink powers interface endpoints.
* **Gateway endpoint**: A gateway endpoint is a gateway that you specify as a target for a route in your route table for traffic destined to a supported AWS service. Amazon Simple storage Service (Amazon S3) and Amazon DynamoDB are supported.

#### AWS PrivateLink AKA VPC endpoint
AWS PrivateLink is an option other than than VPC peering. For example, if we have an internal SaaS application, software as a service application, that we need to share with multiple applications across multiple VPCs, maybe even with third-party customers over here.

It's **one-way designation**. A shared service can't initiate connection back over PrivateLink.

#### VPC endpoint solutions
* VPC-based resources can access AWS service endpoints while staying on the AWS network.
* No need for internet access.

For example, we can have an EC2, and needs to connect to service like S3, rather than having to go out through the internet, the internet gateway back and forth over here, rather than doing that, we said that we can go ahead and set up a VPC endpoint.

The endpoint will allow us to direct that communication directly to the service. And the key benefit there is we're avoiding the internet. We're staying directly on the AWS network so we can have some security benefits. We can also have some performance benefits. And, plus, just overall by not touching, any time we can do stuff without touching the internet. We've got a whole bunch of different services that support endpoints.

#### VPC endpoint component
* Interface endpoint. PrivateLink is a type of interface endpoint.
* AWS PrivateLink is also known as VPC endpoint service.

#### PrivateLink components
* The endpoint is assigned a DNS name.
* The endpoint sends a request to a Network Load Balancer, which then routes to your service.
* Control access to the endpoint using endpoint policies.
* Not every AWS service supports this feature.
* Diagram: EC2 instance -> Route 53 DNS -> PrivateLink -> Shared service.

When you create a PrivateLink interface, it's gonna be tied into a Network Load Balancer.
Route 53 knows about that load balancer and that's gonna be tied into essentially, which means that you essentially now have a shared service.

This is a one-way connection, essentially, to that particular shared service, meaning it can only be initiated from the outside. 

#### PrivateLink and endpoint services features
1. Share to thousands of VPCs.
2. Security group for the connection.
3. Support for overlapping addresses.
4. One-way access.
5. Share a single service.

Notice we've got two VPCs: the SaaS VPC on the left-hand side and then we've got the other VPC that's gonna be calling that particular SaaS-based application. So the application is running on a cluster of servers running behind the scenes over here.

When you create that PrivateLink setup, it's gonna be tied into a Network Load Balancer. The Network Load Balancer, extreme scalability over here. And when you think about it, and what's gonna happen over here, so you can share that out to thousands of VPCs. So, huge amounts of traffic the Network Load Balancer can handle all in relation to that particular backend, SaaS-based application. Again, a one-way flow over here. Now, what the VPCs are actually doing is they're creating the endpoint, basically, to get connected back to your PrivateLink here. So, we've got that PrivateLink endpoint that's actually available.

That's gonna tie an ENI inside the subnet of the VPC that's actually doing the requesting over here. That's the connection. That becomes a route for actually getting connected to that particular SaaS-based application by way of the Network Load Balancer over here, too. You can define a security group for the connections inside.

#### PrivateLink setup
1. Navigate to the AWS Management Console
2. Choose a subnet in your VPC to use the interface endpoint.
3. AWS creates the endpoint network interface in the subnet.
4. Create the endpoint in the console.
5. Specify the Network Load Balancer that you created.
6. Grant permissions to consumers, such as AWS accounts or IAM roles.
7. A service consumer creates an interface endpoint to your service.
8. Accept the interface endpoint connection request.

#### PrivateLink setup
* Endpoint policies are IAM resource policies.
* You can attach an endpoint policy to a PrivateLink endpoint.
* Written in JSON format.
* Define how the endpoint can be used.

Diagram:
* Consumer account
 * VPC
  * Instance
  * PrivateLink endpoint with VPC endpoint policy attached
   * How the endpoint can actually be used?
   * What type of commands can be sent across that particular endpoint over?
* Service provider account
 * VPC
  * Network Load Balancer
  * Service nodes (target)

#### PrivateLink notes
* Ensure that the security group selected for the endpoint will allow traffic through to the service.
* By default, each interface endpoint can support a bandwidth of up to 10 Gbps, bursting to 50 Gbps per Availability Zone.
* Only IPv4 is supported.
* Endpoints do not support UDP traffic.

#### Route 53
It can perform three main functions in any combination:
* domain registration, 
* DNS routing, 
* and health checking.

#### How does DNS route traffic to your web application?
1.  Client: A user opens a web browser, enters www.example.com in the address bar, and chooses Enter.
2. DNS resolver request: The request for www.example.com is routed to a DNS resolver, which is typically managed by the user's internet service provider (ISP).
3. DNS root name server: The DNS resolver for the ISP forwards the request for www.example.com to a DNS root name server.
4. Name server for .com TLD: The DNS resolver forwards the request for www.example.com again, this time to one of the TLD name servers for .com domains. The name server for .com domains responds to the request with the names of the four Route 53 name servers that are associated with the example.com domain. The DNS resolver caches the four Route 53 name servers.
5. Route 53 name server: The DNS resolver chooses a Route 53 name server and forwards the request for www.example.com to that name server. The Route 53 name server looks in the example.com hosted zone for the www.example.com record, gets the associated value, such as the IP address for a web server, 192.0.2.44, and returns the IP address to the DNS resolver.
6. DNS resolver response: The DNS resolver finally has the IP address that the user needs. The resolver returns that value to the web browser.
7. Web browser request: The web browser sends a request for www.example.com to the IP address that it got from the DNS resolver. This is where your content is, for example, a web server running on an Amazon EC2 instance or an Amazon S3 bucket that's configured as a website endpoint.
8. Web server response: The web server at 192.0.2.44 returns the web page for www.example.com to the web browser, and the web browser displays the page.

#### LAB: Configuring DNS on Amazon EC2
1. Start an EC2 Instance with `Auto-assign public IP: Disable`.
2. Create a private hosted zone for your domain `anycompany.corp`.
 * Route 53
 * Hosted zones -> Create hosted zone.
 * Configure the hosted zone:
  * Domain name: `anycompany.corp`.
  * Description.
  * Type: `Private hosted zone`.
  * VPCs to associate with the hosted zone:
   * Region.
   * VPC ID: `Any Company VPC`.
 * `Create hosted zone` button.
3. Create a record set.
 * Create an A record:
  * Route 53 -> Hosted zones -> `anycompany.corp`
  * `Create record` button.
  * Configure the record:
   * Record name: `www`.
   * Record type: `A`.
   * Value: `the EIP of the EC2 Instance`.
   * TTL: `300`.
   * Routing policy: `Simple routing`.
  * `Create record` button.






### Week 5: Storage 2 Part 1
### Week 6: Storage 2 Part 2
### Week 7: Storage 2 Part 3
### Week 8: Databases 2 Part 1
### Week 9: Databases 2 Part 2
### Week 10: Security 2 Part 1
### Week 11: Security 2 Part 2
