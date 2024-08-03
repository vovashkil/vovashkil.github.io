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

**Best practice** is to create an empty subnet, that its sole purpose is for basically that interface for the transit gateway.

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
  *  `Create record` button.

#### CloudFront solutions
CloudFront is a web service that speeds up distribution of your web content to your users.
* CloudFront delivers content through a worldwide network of data centers called edge locations.
* Users are routed to the edge location that provides the lowest latency (time delay). The content is delivered in the least possible amount of time.
* If the content is already in the edge location, CloudFront delivers it immediately.
* If the content is not in that edge location, CloudFront retrieves it from an origin that you have identified as the source for the definitive version of your content. Examples of origins are an Amazon S3 bucket, a MediaPackage channel, or an HTTP server.
* You also get increased reliability and availability because copies of your files (also called objects) are now held (or cached) in multiple edge locations around the world.

#### CloudFront components
* CloudFront origins
* Behaviors
* Distributions

##### CloudFront components: Origins
Origins can be: 
* Amazon S3 bucket, 
* Amazon EC2 instance, 
* Application or Classic Load Balancer(s),
* Custom origin - for resources, for example, on premises.

* An Amazon S3 bucket or internet-accessible HTTP-server.
* Access restrictions via `Origin Access Identity (OAI)` - specialized user for CloudFront, signed URL, or origin custom header.
* Persistent connections.
* Optimized AWS resource connections.
* Create an origin group for high availability.

An origin is the location where you store the original version of your content. When CloudFront gets a request for your files, it goes to the origin to get the files that it distributes at edge locations. You can use any combination of Amazon S3 buckets and HTTP servers as your origin servers. If your origin is one or more HTTP servers hosted on one or more Amazon EC2 instances, you can use an Application Load Balancer to distribute traffic to the instances. 

* To restrict access and securely serve this private content, you can restrict access through **Origin Access Identity (OAI), signed URL, or origin custom header**.
* You can set up CloudFront with origin failover for scenarios that require high availability. Create an origin group with two origins: a primary and a secondary. If the primary origin is unavailable, or it returns specific HTTP response status codes that indicate a failure, CloudFront automatically switches to the secondary origin.

CloudFront provides two ways to send authenticated requests to an Amazon S3 origin: origin access control (OAC) and origin access identity (OAI). For this lab, you use OAI. CloudFront OAI provides similar functionality as OAC, but it doesn’t work for all scenarios. This is why AWS recommends using OAC. Scenarios that OAI does not support include the following:
* Amazon S3 buckets in all AWS Regions, including opt-in Regions
* Amazon S3 server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS)
* Dynamic requests (PUT, POST, or DELETE) to Amazon S3
* New AWS Regions launched after December 2022

##### CloudFront components: Behaviors
Distribution options
* Path-pattern matching
* Origin detection
* HTTP methods
* Forward query strings
* Signed URL
* SSL certificate
* Protocol enforcement
* Time to Live (TTL) - how long something is in cache
* Compression with gzip

##### Distributions
When you want to use CloudFront to distribute your content, you create a distribution and choose the configuration settings that you want.

Using custom SSL certificates, you can deliver secure content using your own domain name. When a certificate is issued or imported into the AWS Certificate Manager (ACM) service, it is immediately available for use through the CloudFront console and automatically propagated to the global network of CloudFront edge locations.

You can use distributions to serve the following content over HTTP or HTTPS:
* Static and dynamic download content, for example, .html, .css, .js, and image files, using HTTP or HTTPS.
* Video on demand in different formats, such as Apple HTTP Live Streaming (HLS) and Microsoft Smooth Streaming.
* A live event, such as a meeting, conference, or concert, in real time. For live streaming, you can create the distribution automatically by using an AWS CloudFormation stack.

#### CloudFront
There's a forwarding query string through a CloudFront distribution so that database queries can be cached at the edge.

#### Edge solutions

Access application

Each hop impacts **performance** and introduces **risk**.

CloudFront and Route 53 get you to the AWS network faster.

* Shield and AWS WAF mitigate risk.
* Lambda@Edge adds intelligence and control, resulting in improved performance.

#### CloudFront solutions
* Decrease latency with edge caching
* Increase security. No direct access to origin. User HAVE to go to CloudFront, it will block malformed packets, DDoS protection.
* Create a distribution
* Define origins
* Define behaviors - how the operation is going to take place: how long the cache should stay inside.

#### CloudFront components: Distributions
* CNAME the CloudFront.net domain with Route 53 to personalize distribution.
* Unique CloudFront.net domain references objects. Example: `d.....cloudfront.net`.
* Specifies origin(s) of original content versions. Example: ``origin.example.com`. This CNAME will push you to the closest edge location where CloudFront is running.
* Types provide for HTTP/HTTPS. Example: https://cdn.mysite.com
* Contains specific configurations and tags. Example: `origins`, `behaviors`, `error pages`, `restrictions`.

#### Behaviors: Path pattern matching
* Route traffic to specific origins based on pattern match.

Path pattern matching examples: /*.jpg; /*.php, etc.

* GET http://example.com/images/1.jpg to ORIGIN A
* GET http://example.com/index.php to ORIGIN B
* GET http://example.com/web/home.css to ORIGIN C
* GET http://example.com/* (DEFAULT) to ORIGIN D

www.example.com:
* /images/*.jpg -> S3 Bucket A: origin.example.com
* /*.php -> Origin B: origin2.example.com
* /web/*.css -> Origin C: origin3.example.com
* /*.* (DEFAULT) -> origin4.example.com

#### Behaviors: Origin selection
* Set up one-to-many origins
* AWS or custom resource as origin

##### Origin Settings:
* Origin Domain Name
* Origin Path
* Origin ID
* Restrict Bucket Access: yes/no
* Origin Access Identity
* Grant Read Permissions on Bucket
* Origin Custom Headers

#### Behaviors: HTTP methods
* Define what actions are allowed through a distribution.
* Only GET requests are cached at the edge.

* GET
* POST
* HEAD
* PATCH
* DELETE
* PUT - upload files through CloudFront distribution more efficiently.
* OPTIONS

#### Behaviors: Query strings and cookies
* Forward query strings and cookies to the origin
* Vary the response based on query string/cookie
* Cache multiple copies of your object
* Query string/cookie as cache key
* Forward all
* Forward allowed list

##### Forward query strings
CloudFront can also cache query results (from database).

#### Behaviors: Signed URL
The idea behind signed URL is you are giving permission to use a specific URK for some amount of time. It's another way to control who can access an application.

* Restrict access to content.
* Subscription content, digital rights, etc.
* Canned and custom policies.
* Application creates signed URL.
* CloudFront caches the underlying object, authenticating each URL when requested.

Communication flow:
* Customer location
* www.mysite.com/asset.mp4 -> EC2 auth server
* signed URL to customer www.mysite.com/asset.mp4&Expires=5555555555&Signature=blablabla
* customer sends Authenticate URL, policy statement, and expiration -> VloudFront logic
* CloudFront edge cache sends content to requester via cache edge

#### Behaviors: SSL certificates
https://example.com
* CloudFront shared cert
* Custom cert
* AWS Certificate Manager - certs included into CloudFront distribution are free of charge.

#### Behaviors: Protocol enforcement
* HTTP and HTTPS: Viewers can use both protocols.
* Redirect HTTP to HTTPS: Viewers can use both protocols, but HTTP requests are automatically redirected to HTTPS requests.
* HTTPS only: Viewers can only access your content if they are using HTTPS.

HTTPS only - is a common setup

#### Behaviors: Time to live (TTL)
* Short TTL = dynamic content
* Long TTL = static content
* Reduce load on the origin
* If modified since
* Mix, max, default TTLs

#### Behaviors: Compression
* Compresses and serves files.
* GZIP or Brotli.
* Brotli is a widely supported lossless algorithm.
* Optimizes bandwidth consumption and download speed.
* Compresses files with header: "content-type" set.

#### CloudFront: Geographic restrictions
* No additional charges.
* Allowed list or denied list.
* Country-level granularity

Setup:
* Enable Geo-Restriction: yes/no.
* Restriction type: Whitelist/Blacklist
* Countries.

#### CloudFront: Restrictions and errors
* Caching error pages
* 4XX, 5XX codes
* Cache default page
* cache custom page

Codes:
* 400: Bad request
* 403: Forbidden
* 404: Not found
* 405: Method not allowed
* 414: Request URI too long
* 416: Request range not satisfiable
* 500: Internal server error
* 501: Not implemented
* 502: Bad gateway
* 503: Service unavailable
* 504: Gateway timeout

#### AWS Origin Shield and regional edge caches
* Regional edge caches automatically serve as a mid-tier caching layer.
* Origin Shield adds an additional caching layer between region cache and origin - additional cache, a paid service.
* Optional feature.
* Improve cache hits and reduce origin load for certain workloads.

Viewers -> Edge locations -> Regional edge caches -> Origin Shield -> AWS Elemental MediaPackage

Amazon CloudFront:
* Edge locations
* Regional edge caches
* Origin Shield (optional)

#### CloudFront Demo
##### CloudFront Distributions - > Create Distribution

##### Origin Settings
* Origin Domain Name: by default the dropdown is mapped to existing S3 buckets.
* Origin Path - empty=root, a path could be specified to limit access to some particular object path.
* Enable Origin Shield: `No`. - It's a paid service, extra cache layer before AWS resources.
* Origin ID.
* Restrict Bucket Access: `Yes`.
* Origin Access Identity -> Create New Identity - Automatically creates an Origin Access Identity (OAI).
* Grant Read Permission on Bucket -> Yes, Update Bucket Policy.

##### Default Cache Behavior Settings
###### Cache and origin request setting:
1. Use a cache policy and origin request policy
2. Use legacy cache settings -> presets for min. max, default TTL.

If `use a cache policy and origin request policy` is checked, then `Cache Policy` options are available that simplifying cache management:
* Managed-CachingOptimized - we picked up this.
* Managed-CachingDisabled
* Managed-CachingOptimizedForUncompressedObjects
* Managed-Elemental-MediaPackage

###### Lambda Function Associations.
We can push our lambda to edge.

* CloudFront Event -> Viewer Request
 * Viewer Request
 * Viewer Response
 * Origin Request
 * Origin Response
* Lambda function ARN

We can attach lambdas to a particular event type.

##### Distribution Settings
* Price Class -> Use All Edge Locations (we can limit in the drobdown).
* AWS WAF Web ACL:
 * None
 * EdgeProtect (wafv2)

##### We can edit existing CloudFront distribution
###### Origin and Origin Group
Creating an Origin Group we add extra reliability/fault tolerance

###### We create multiple behaviors for different URL path patterns

#### CloudFront LAB
1. Create an S3 bucket with ACL disabled and Block all public access
2. Create a CloudFront web distribution with origin access.
 * CloudFront -> Distributions -> Create distribution
  * Origin domain: Choose the S3 bucket created before.
  * Origin access: `the Legacy access identities`.
  * Origin access identity: `Create new OAI`.
   * A pop-up message appears. Keep the name at the default and choose `Create`.
  * Bucket policy: `Yes, update the bucket policy`.
  * Web Application Firewall (WAF): `Do not enable security protections`.
  * Keep everything else as default.
  * `Create distribution` button.

Testing with HTML code:
```
<html>
<head>My CloudFront Test</head>
<body>
<p>My text content goes here.</p>
<img src="https://DOMAIN/OBJECT" alt="my test image">
</body>
</html>
```

Replace DOMAIN with your Amazon CloudFront Distribution domain name for your distribution. For example: a1bc2d3ef45g.cloudfront.net
Replace OBJECT with the name (also known as key) of the file that you uploaded to your S3 bucket. For example: cf-image.jpg

#### Networking 2: Understanding Web Application Traffic Components
##### HTTP methods overview

| HTTP method | Description |
| ----------- | ------------------------------------------------ |
| **GET** | Use **GET** to retrieve data from a server. |
| **HEAD** | The **HEAD** method is similar to **GET**, but you use it to only request the headers of the response, not the actual content. You often use it to check availability or metadata of a resource without transferring all the data. |
| **POST** | Use **POST** to submit data to be processed by a server. It is often used for form submissions and file uploads. |
| **PUT** | Use **PUT** to add a new resource or update an existing resource on a server. It replaces the entire resource or creates it if it doesn't exist. |
| **DELETE** | Use **DELETE** to remove a resource from a server. |
| **OPTIONS** | Use **OPTIONS** to retrieve the communication options available for a resource or the server. You often use it to check what methods are allowed for a particular resource. |

##### GET method example
In the following example, a client sends an **HTTP GET** request to the server at the example.com host. 
* The User-Agent header provides details about the client, indicating it is running Mozilla 5.0 on Windows 10.
* The **Accept-Language** header indicates the preferred language of the client.
* The **Accept-Encoding** header specifies the compression algorithms the client can use.
* The **Connection header** controls whether the connection should be kept alive or closed after a response is received. It can have two common values: **Keep-Alive** or **Close.**.

#### Key aspects of HTTPS
##### Encryption
The primary feature of HTTPS is encryption. It uses SSL (Secure Sockets Layer) or TLS (Transport Layer Security) protocols to encrypt data before transmission and decrypt it on the receiving end. This ensures that any data sent between the client and the server is securely encoded and cannot be intercepted easily. 

##### SSL/TLS certificates
HTTPS relies on SSL or its successor TLS protocols for encryption. To enable HTTPS on a website, you need an SSL/TLS certificate issued by a trusted certificate authority (CA). The certificate contains a public key used for encryption and authentication.

##### Data integrity
HTTPS ensures data integrity, meaning the data transmitted between a client and server remains unchanged and unaltered during transmission.

##### Compliance and data protection
Many data protection regulations and  standards, such as the Health Insurance Portability and Accountability Act (HIPAA), require the use of encryption for transmitting sensitive data. By implementing HTTPS, your web applications can comply with these regulations.

##### Browser compatibility
Modern web browsers strongly encourage the use of HTTPS and may display security warnings for websites that don't use it. Adopting HTTPS ensures a better user experience and prevents potential visitors from being deterred by security warnings.

#### Understanding the SSL/TLS handshake
SSL/TLS uses two different keys to encrypt and decrypt a message. This is also known as public key cryptography, or **PKI**. PKI provides a way for one party to establish the identity of another party using certificates, if they both trust that third party. This is known as a certificate authority. The certificate authority verifies the certificate and authenticates both parties before communication begins. 

1. The browser opens an SSL/TLS-secure website, and connects to the web server. Next, the browser attempts to verify the authenticity of the web server by requesting identifiable information.
2. The web server sends the SSL/TLS certificate that contains a public key as a reply. 
3. The browser verifies the SSL/TLS certificate, ensuring that it is valid and it matches the website domain. Once the browser is satisfied with the SSL/TLS certificate, it uses the public key to encrypt the message.
4. It sends the message that contains a secret session key. A session key is a cryptographic key that is used for encrypting the transmitted data. 
5. The web server uses its private key to decrypt the message and retrieve the session key. 
6. It then uses the session key to encrypt and then it sends a message to the browser.
7. Both the browser and the web server switch to using the same session key to exchange messages safely.

#### Integrating Applications with cross-origin resource sharing (CORS)
In standard internet communications, when your browser interacts with a server, it sends an HTTP request and receives an HTTP response. The browser's current URL is called the current origin, while any third-party URL is considered cross-origin. The following is a summary of the request-response process when you make a cross-origin request.

1. The browser adds an origin header to the request, containing information about the current origin's protocol, host, and port. 
2. The server checks this header and responds with the requested data, along with an Access-Control-Allow-Origin header, allowing the cross-origin access. If the server doesn't allow the cross-origin access, it responds with an error message.
3. The browser acknowledges the access control request headers and shares the returned data with the client application. 

In HTTP, request methods indicate the data operations the client wants the server to perform, such as GET, POST, PUT, and DELETE. In a regular CORS interaction, the browser sends the request and access control headers together, typically for low-risk GET data requests. 

However, complex cross-origin requests involve methods other than GET, POST, or HEAD, additional headers, or specific Content-Type headers. Examples of complex requests include those to delete or modify existing data. These requests require server confirmation before the actual request is sent, and are preapproved through a preflight request. 

#### CORS communication example
1. **Preflight request**. The preflight request is an HTTP OPTIONS request your web browser sends to the server before the actual cross-origin request. The preflight request seeks permission from the server to make the actual request. The preflight request includes several headers that include the details of the actual request.
2. **Preflight response**. If the cross-origin server's CORS configuration grants access to the requesting domain, the server sends back a preflight response that lists all the HTTP request types that the requesting domain can make on the requested resource.
3. **Request**. After receiving the preflight response, the web browser knows whether the cross-origin request is permitted. Next, the browser proceeds to make the actual cross-origin request to the server.
4. **Response**. The server responds to the cross-origin request just like it would respond to a same-origin request.

#### Using AWS to support your CORS requirements
AWS provides built-in support for CORS in many of its services, allowing you to control cross-origin access to your APIs and resources hosted on AWS. AWS services with CORS support include the following:
* **Amazon Simple Storage Service (Amazon S3)** lets you create a CORS configuration document with rules that identify the origins you will allow to access your S3 data, the operations you will support for each origin, and other operation-specific information. 
* **Amazon API Gateway** is a fully managed service for creating, publishing, maintaining, and securing APIs at scale. It offers on-click CORS enabling for your REST APIs directly in the console. This feature simplifies the process of handling cross-origin requests to your API endpoints.

#### Diagnosing Network Issues
#### General troubleshooting guidance
Many problems are common and well documented, so identifying the issue based on symptoms can be straightforward. Here are the first steps to follow when troubleshooting a problem. To learn more, expand each of the following five categories.

##### Step 1: Categorize the problem
Try to categorize the problem based on characteristic symptoms:
* What error messages is the administrator seeing on the console or in log files?
* Are customers getting error messages in their browsers? 
* Are there messages or error codes?

##### Step 2: Collect data
Gather diagnostic data or reproduce the problem to gather logs, trace data, and so on. If you have various logging, tracing, and monitoring features turned on for your service, then you will have diagnostic data available when a problem occurs.

You might have to set up these diagnostic features and try to reproduce the problem.

##### Step 3: Analyze the data
Analyze data to pinpoint one or more possible root causes. Sometimes, you can manually search the relevant log files and tracing data. 

For large amounts of diagnostic data, it might be helpful to use tools for analyzing data such as the following:
* **Amazon Athena**
* **Amazon CloudWatch Logs Insights**
* **Splunk**
* **Sumo Logic**

##### Step 4: Review documentation
Search the product and service documentation for known issues and solutions. Apply the documented solutions and test. If there is a series of proposed fixes, apply them one at a time and test until the problem is fixed.

##### What else can I try?
If you exhaust all the known issues and solutions, try the following:
* Post your issue to [AWS re:Post](https://repost.aws/topics/TAgOdRefu6ShempO3dWPEofg/containers?sc_ichannel=ha%E2%89%BBilang=en%E2%89%BBisite=repost%E2%89%BBiplace=hp%E2%89%BBicontent=TAgOdRefu6ShempO3dWPEofg%E2%89%BBipos=2). AWS re:Post is a community-driven, question-and-answer service to help AWS customers remove technical roadblocks and troubleshoot problems.
* Engage with [AWS IQ](https://repost.aws/topics/TAgOdRefu6ShempO3dWPEofg/containers?sc_ichannel=ha%E2%89%BBilang=en%E2%89%BBisite=repost%E2%89%BBiplace=hp%E2%89%BBicontent=TAgOdRefu6ShempO3dWPEofg%E2%89%BBipos=2) to post a request for help by an AWS Certified expert. Pay through AWS.
* Subscribe to an AWS Support plan and open a case. 
Select a support plan that meets your needs. [Compare AWS Support Plans](https://aws.amazon.com/premiumsupport/plans/).

#### Troubleshooting resource communication issues with VPC
##### Note the symptom
While connected to the console of an EC2 instance, you are unable to use the web browser to open public websites.

##### Gather diagnostic data
You use the command line from the EC2 instance to ping a domain name and IP address to see if the EC2 instance can communicate with the public internet. The domain name is used to test if DNS resolution is working and resolves to the intended IP address.

The following screenshot is a typical response to the ping command used to ping a specific IP address. The typical response includes whether the connection to the IP address is successful. If successful, the expected attributes previously mentioned are returned. In this example, a ping to 192.168.1.1 returned that 64 bytes of data returned from the IP address in 1.5 ms.

##### Check the EC2 instance configuration
You use the EC2 console to verify that the EC2 instance is configured with an elastic network interface that has access to the internet gateway, or that it's assigned a public IP address directly.

The following screenshot highlights how to navigate to the Instances dashboard of the EC2 console. It also shows how to use the filtered search to filter by instance ID. Finally, it shows the details tab highlighting the Public IPv4 address and Elastic IP addresses.

##### Verify that the VPC has an internet gateway attached
You navigate to the VPC console. Using the left-navigation menu, you choose **Internet Gateways** under the **Virtual Private Cloud** section. Then, using the search box, you filter the list by VPC ID to display only relevant information for the task.

The following screenshot highlights how to navigate to the Internet Gateways dashboard, filter the gateway list by a VPC ID, and find the internet gateway ID for the filtered VPC ID.

##### Verify the security group
You open the security group's rules from the EC2 console. 

The Outbound rules should, at minimum, allow traffic to the remote host public IP address, and list the Type of traffic and Port range. You can also configure the outbound rule to allow all traffic to a Classless Inter-Domain Routing (CIDR) or IP address.

The following screenshot highlights the Outbound rules tab of a security group and an allowed IPv4 rule allowing traffic to 1.1.1.1/32.

##### Verify the network ACL
You verify that the network access control list (network ACL) egress and ingress rules allow traffic for both request and response against the remote public IP addresses. 

Make sure that the “allow” traffic for the remote public host IP is at the lowest order number, and is taking precedence to any deny traffic you might have. You can also configure the inbound and outbound rule to allow all traffic to CIDR or IP addresses.

##### Verify the route table
You verify that the route table has a route for the destination CIDR or IP address pointing to the internet gateway.

The following screenshot highlights the route for 1.1.1.1/32, with the target of an internet gateway igw-062e169bd5b3ca57a.

##### Verify EC2 instance routing
If you are still having issues after verifying that the VPC infrastructure is configured properly, use the command line on your EC2 instance to inspect its routing table. Verify the EC2 instance is routing the traffic to the appropriate network interface if you have more than one configured.

Depending on the operating system of your EC2 instance, you can run the terminal command 'route print' for Windows or 'netstat -rn' for Linux to show the local operating system route table.

#### Enhancing Network Communications

#### API Gateway
API Gateway is an AWS service for creating, publishing, maintaining, monitoring, and securing REST, HTTP, and WebSocket APIs. 

#### API Gateway types
* REST. Similar to HTTP, but has more features.
* HTTP. Similar to REST, but is simpler.
* WebSocket APIs.

##### HTTP API
Use HTTP APIs to create RESTful APIs with lower latency and lower cost than REST APIs. 

In this example, you use an HTTP API that integrates with a Lambda function on the backend. When a client calls your API, API Gateway sends the request to the Lambda function and returns the function's response to the client.

##### Rest API
REST APIs are a collection of resources and methods that are integrated with backend HTTP endpoints, Lambda functions, or other AWS services. You can use API Gateway features to help you with all aspects of the API lifecycle, from creation through monitoring your production APIs. Your application will use a REST API.

##### WebSocket API
With API Gateway, you can create a WebSocket API as a stateful frontend for an AWS service (such as Lambda or Amazon DynamoDB) or for an HTTP endpoint. The WebSocket API invokes your backend based on the content of the messages it receives from client applications. In your WebSocket API, incoming JSON messages are directed to backend integrations based on routes that you configure.

#### API Gateway in your application
A REST API in API Gateway is a collection of HTTP resources and methods that are integrated with backend HTTP endpoints, Lambda functions, or other AWS services. You can deploy this collection in one or more stages. Typically, API resources are organized into one or more API methods that have unique HTTP verbs that API Gateway supports. With these methods, GET, POST, and DELETE, you will validate the requests and transform the responses returned from the Lambda functions.

#### API Gateway developer features
##### Stages
After creating an API, developers can set up a stage. A stage is a named reference to a deployment, which is a snapshot of the API. By using stages, you can do the following:
* Configure stage settings to enable caching
* Customize request throttling
* Configure logging
* Define stage variables
* Attach a canary release for testing

For more information, see [Setting Up a Stage for a REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-stages.html) in the Amazon API Gateway Developer Guide.

##### Usage plans and API keys
After you create, test, and deploy your APIs, you can use API Gateway usage plans to make them available as product offerings for your customers. You can configure usage plans and API keys to allow customers to access selected APIs. Customers can access these APIs at agreed-upon request rates and quotas that meet their business requirements and budget constraints.

For more information, see [Creating and Using Usage Plans with API Keys](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html) in the Amazon API Gateway Developer Guide.

##### Throttling
To prevent your API from being overwhelmed by too many requests, API Gateway provides tools to adjust throttle limits to your API. API Gateway provides two basic types of throttling-related settings:
* Server-side throttling limits are applied across all clients. These limit settings exist to prevent your API—and your account—from being overwhelmed by too many requests. 
* Per-client throttling limits are applied to clients that use API keys associated with your usage policy as client identifier.

For more information, see [Throttle API Requests for Better Throughput](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html) in the Amazon API Gateway Developer Guide.

##### Access control
API Gateway supports multiple mechanisms for controlling and managing access to your API. Solutions include standard AWS Identity and Access Management (IAM) roles and policies, resource policies, cross-origin resource sharing (CORS), and Lambda authorizers.

For more information, see [Controlling and Managing Access to a REST API in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-to-api.html) in the Amazon API Gateway Developer Guide.

##### Data transformations
In API Gateway, an API's method request can take a payload in a different format from the corresponding integration request payload, as required in the backend. Similarly, the backend can return an integration response payload different from the method response payload, as expected by the frontend.

For more information, see [Setting Up Data Transformations for REST APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-data-transformations.html) in the Amazon API Gateway Developer Guide.

##### SDK generation
API Gateway supports generating an SDK for your language-specific application. Supported languages are Java, JavaScript, Java for Android, Objective-C or Swift for iOS, and Ruby. 

For more information, see [Generating an SDK for a REST API in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-generate-sdk.html) in the Amazon API Gateway Developer Guide. 

##### Mock integrations
API developers can generate API responses from API Gateway directly, without the need for an integration backend. You decide how API Gateway responds to a mock integration request.

For more information, see [Set Up Mock Integrations in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-mock-integration.html) in the Amazon API Gateway Developer Guide.

##### Response caching
Enabling API caching in API Gateway can reduce the number of calls made to your endpoint. Caching can also improve the latency of requests to your API.

For more information, see [Enabling API Caching to Enhance Responsiveness](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html) in the Amazon API Gateway Developer Guide. 

##### Latency
Each service integrated with an application introduces latency. Using API Gateway, developers with enhanced observability tools can reduce their application’s latency.

For more information, see [Troubleshooting Amazon API Gateway with Enhanced Observability Variables](https://aws.amazon.com/blogs/compute/troubleshooting-amazon-api-gateway-with-enhanced-observability-variables/) in the AWS Compute blog.

##### Security
Security is a shared responsibility between AWS and you. IAM includes features that are available to use with API Gateway. For example, with identity-based and resource-based policies, you can specify which API operations are allowed or denied on specified resources. You can also specify conditions under which the operations are allowed or denied.

Using API Gateway, you can create private REST APIs. These REST APIs can be accessed only from your virtual private cloud (VPC) in Amazon Virtual Private Cloud (Amazon VPC) by using an interface VPC endpoint. You can use VPC endpoint policies for private APIs in API Gateway. VPC endpoint policies are IAM resource policies that you can attach to an interface VPC endpoint to control access to the endpoint.

For more information, review [Security in Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/security.html) in the Amazon API Gateway Developer Guide.

##### Controls
Use API Gateway to control your application at the API level. Tools include throttling to help limit applications from being overwhelmed by too many requests. With AWS WAF integration as the web application firewall, you can protect the applications from attacks.

For more information, review [Throttle API Requests for Better Throughput](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html) in the Amazon API Gateway Developer Guide.

#### Working with API Gateway
When creating an API method, you must integrate it with an endpoint (or integration endpoint) in the backend. An integration endpoint can be a Lambda function, an HTTP webpage, or an AWS service action.

##### Configuring API Gateway
1. End users are making requests.
2. API Gateway first will take a look at that request and **authorize** it if you've set up authorization. So, you can have public APIs, but it's more likely that you will want some sort of authorization around those APIs, and we have different types of authorizers that are supported for API Gateway.
3. Any sort of **configuration** on that request, meaning that you can supply things called models, which will validate the structure of your request.
4.  It can **meter** that request, meaning it might need to do some throttling if it's coming from a specific API key that's used up its capacity. Or, maybe you have some throttling thresholds for certain API keys, it would do that, as well.
5.  It can **transform** and **map** your request, meaning again, it can change that data shape.
6. It gets through the request step, it will then send that request to your backend service.
7. **Configuring** on response.
8. **Transforming**.
9. **Mapping**.
10. Send response to the customer.

API Gateway is bound to a certain Region. However, you can have multiple different types of API Gateway endpoints. They can be Regional endpoints, which means they just live inside of that one Region, so if anybody wants to interact with your API, they would have to traverse the internet to that Region to make that request. 

You can also have edge-optimized endpoints, which would allow you to push your API Gateway endpoints to CloudFront using the edge location network. 

You can have private APIs, where those APIs would be inside of a VPC, so you can control the network traffic to those a little bit easier. 

#### API Endpoint Integrations
* **Proxy**. The payload passes through to back-end without changes.
* **Non-Proxy**. You are gonna set up your data mappings. You would be responsible for configuring the integration request and the integration response.
* **Mock**. Useful for testing APIs, developing APIs (you can essentially inject what would be like a mocked-out payload).

#### Improving Application Network Performance

#### Global Accelerator (other edge services - Amazon CloudFront, Lambda@Edge)
It has a similarity with CloudFront - works in Edge locations.
The difference - it's not about caching, it's about network closeness.

* The Customer Consensus application will run in three Regions for resilience. How can we **optimize traffic requests** to the best Region for customers? Data Analyst.

##### Without Global Accelerator
* It can take many networks to reach the application.
* Paths to and from the application may differ.
* Each hop impacts performance and can introduce risk.

##### With AWS Global Accelerator
* Network layer that you employ in front of your internet-facing applications.
* Traffic enters the AWS global network at edge locations.
* Improve speed and availability of global applications to the customers.

AWS Global Accelerator gets the user closer to the application and routes the user to the optimal Region based on rules we specify.
 
#### Global Accelerator use cases
* Single globally advertised IP address.
* Intelligent traffic distribution.
* Target Amazon EC2 instances and load balancers.
* Easy to set up and manage with fine-grained control.

#### Global accelerator example
* Global accelerator endpoint with anycast IP eg., 54.86.52.59
* All clients point to the same static IPs and are directed to the closest PoP.
* Instant failover to next closest available AWS Region.

#### Global Accelerator: Endpoint selection
* **Geo-proximity**. Closest Regional endpoint to client location.
* **Client affinity settings**. Continuously select the same endpoint for a given client.
* **Customer-configured policies**. Customer-defined rules to control traffic to endpoint.
* **Application health**. Continuous health checks to endpoint.

#### Traffic control
* Regional traffic dials
* Endpoint weights
* Health checks

#### Traffic controls: Regional traffic **dials**.
How much traffic do we want to flow to a particular Region.

* Dials values:
 * Min 0%
 * Max 100%
 * Default 100%

We can set 0% for one Region and 100% for another to do the following:
* Redirect traffic
* Exceeded capacity
* Out of service
* New Region

Global Accelerator requests are by default routed to the AWS Region closest to your end users to provide the optimal performance. To adjust how the traffic is routed, Global Accelerator provides traffic dials to shift traffic between the Regions that are configured behind your accelerator.

By default, the traffic dial is set to 100 (meaning, 100 percent) for all Regional endpoint groups in an accelerator. Traffic dials are useful when you need to redirect traffic from a Region that has exceeded its capacity, take a Region out of service for maintenance, or gradually ramp up traffic for a newly added Region.

Example: AWS Global Accelerator routing 100% of user traffic across two different regions, then re-directing 100% to one region and 0% to the other. In both examples, there are two elastic load balancers in each region. 

#### Traffic controls: **Endpoint weights**.
We have control over traffic to Region (with Dials) and in the Region with the Weights.

* Weights values:
 * Min 0%
 * Max 255
 * Default 128

A weight is a value that determines the proportion of traffic that Global Accelerator directs to an endpoint. Global Accelerator calculates the sum of the weights for the endpoints in an endpoint group and then directs traffic to the endpoints based on the ratio of each endpoint's weight to the total. 
* Weighted endpoints can help you roll out new application changes when performing A/B testing or blue/green deployments.
* With weighted routing, you can choose how much traffic is routed to a resource in an endpoint group.
* If there are no healthy endpoints in an endpoint group that has a weight greater than zero, Global Accelerator tries to fail over to a healthy endpoint in another endpoint group.

Example: Global Accelerator directing traffic across two Regions. Every load balancer within each Region receives different amounts of traffic based on their weight values.


#### Traffic controls: **Health check**.
If there is a resource that actually is out of commission, Global Accelerator will find out about that really quickly and stop sending traffic to that particular location.
* Traffic is not sent to targets with failed checks.

Global Accelerator continuously monitors the health of all endpoints and instantly directs traffic to another available endpoint when it determines that an active endpoint is unhealthy. These regular health checks run automatically.

**Global Accelerator requires your router and firewall rules to allow inbound traffic from the IP addresses associated with Amazon Route 53 health checkers to complete health checks for EC2 instances or elastic IP address endpoints.**

Example: Global Accelerator directing traffic to several endpoints across two Regions, except for one marked as unhealthy.

### Week 5: Storage 2 Part 1
### Week 6: Storage 2 Part 2
### Week 7: Storage 2 Part 3
### Week 8: Databases 2 Part 1
### Week 9: Databases 2 Part 2
### Week 10: Security 2 Part 1
### Week 11: Security 2 Part 2
