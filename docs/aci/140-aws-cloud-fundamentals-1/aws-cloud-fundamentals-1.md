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

#### Week 4 Assessment
##### What function does authoritative DNS have?
* It translates domain names into IP addresses and responds to DNS queries of a given domain name.

##### What function does recursive DNS have?
* It provides a local client DNS service by accepting DNS queries from a client and returns an answer after completing a search.

An authoritative nameserver holds the DNS records for a specific domain and responds to DNS queries. TLD nameservers maintain domain names that share a common domain extension. A domain registrar provides a way to purchase and manage a domain name.

##### When dows a client use a session key during a TLS handshake?
* The client uses a session key after it encrypts a random number with a web server's public key.

The server decrypts the random number using its private key. The server and client now have all the components to calculate the session key. The client sends an encrypted message with the session key to the server for confirmation. The web server decrypts the message with its session key and confirms with the client. Subsequent messages between the client and server are encrypted with the sessions key.

##### How does the API Gateway send REST API request to the appropriate backend endpoint?
* It matches an incoming API request to a corresponding method request, then sends an integration request to the appropriate backend endpoint.

The backend endpoint returns the result to the API Gateway as an integration response. A developer can optionally map an integration response to a method response to return to the client.

##### How does AWS PrivateLink provide private connections between a VPC and other services?
* It uses VPC endpoints that ensure network traffic from a VPC is routed over the AWS private network to the target service.

AWS PrivateLink doesn't provide any kind of built-in network traffic encryption or use a VPN. PrivateLink also doesn't use a transit gateway, but rather VPC endpoints to route traffic to a target service.

##### What request elements can be configured to change the cache behavior of an Amazon CloudFront distribution? (Select TWO.)
* **Query strings** and **HTTP headers**.

The web content distribution can serve different versions of content, depending on the query strings and headers.

##### How does Amazon CloudFront enhance delivery of web content for applications?
* Requests for content are routed to the nearest edge location.

Edge locations serve out cached web content instead of the web servers, which means less networks to traverse for providing content to users.

##### What purpose does Cross-Origin Resource Sharing (CORS) serve?
* CORS allows a client browser to check with third-party servers if a request is authorized before any data transfers.

In addition to being an extension of the same-origin policy that's enforced by modern browsers, CORS also mitigates against cross-site request forgery attempts.

##### What is the next step in troubleshooting process after diagnostic data is collected?
* Analyze the data to determine the root cause of observed instances.

The order of troubleshooting steps is the following: categorize the problem, collect diagnostic data, analyze the data, and review the documentation. Seeking online or third-party assistance is also an option after all attempts to resolve the issue haven't worked.

##### What purpose do security certificate serve for HTTPS?
* They provide a way to confirm an identity of a server and establish a way to encrypt web data.

In a typical HTTPS session, a web server presents a security certificate to a requesting client. The client validates the certificate with a Certificate Authority. After validating the web server's identity, the client uses the web server's public key to initiate an encrypted session with the web server.

##### What is required to implement **traffic dials** for AWS Global Accelerator endpoints?
* **Endpoint groups**.

An endpoint group, and all the endpoints in it, must be in one AWS Region. However, endpoint groups could be in multiple Regions. A traffic dial sends a specified percentage of traffic to an endpoint group. Additional **weights** could be assigned to each endpoint in an endpoint group for additional custom traffic routing.

##### What is a benefit of using response caching in Amazon API Gateway?
* It can reduce the number of calls made to backend services.

Response caching improves the latency of requests to an API endpoint. Response caching doesn't throttle API requests to an endpoint, but but redirects them to the cache. Response caching is specific to the Amazon API Gateway service. Additional configuration is required to use it with Amazon CloudFront.

##### How does AWS Global Accelerator improve an application's performance.
* It directs traffic to the optimal AWS endpoint of the application.

The optimal AWS endpoint is based on several factors, including the client's location, the health of the endpoint, and the configured endpoint **weights**. AWS Global Accelerator only prioritizes an application's incoming traffic over the AWS network.

### Week 5: Storage 2 Part 1
#### Uploading with the Amazon S3 console
**The maximum size of a file that you can upload by using the Amazon S3 console is 160 GB. To upload a file larger than 160 GB, you can perform a multipart upload using AWS Command Line Interface (AWS CLI), AWS SDKs, or Amazon S3 REST API. The maximum size of a single object in Amazon S3 is 5 TB.**

#### Uploading to S3 with the REST API
You can send a PUT request to upload an object of up to 5 GB in a single operation. When you use PutObject to add an object to a bucket, you must have WRITE permissions on the bucket that you are uploading the object to.

**You must have the s3: PutObject in your AWS Identity and Access Management (IAM) permissions.**

##### The authentication header: calculating signature
Python script calculates the preceding signature, using the provided parameters:

```
import base64
import hmac
from hashlib import sha1

access_key = 'AKIAIOSFODNN7EXAMPLE'.encode("UTF-8")
secret_key = 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'.encode("UTF-8")

string_to_sign = 'PUT\n\nimage/jpeg\nTue, 12 Aug 2024 21:15:45 +0000\n/DOC-EXAMPLE-BUCKET/photos/puppy.jpg'.encode("UTF-8")
signature = base64.encodestring(hmac.new(secret_key, string_to_sign, sha1).digest()).strip()

print(f"AWS {access_key.decode()}:{signature.decode()}")
```
#### Multipart uploads

#### Using AWS SDKs
* **High-level APIs.** The AWS SDK high-level API provides a high level of abstraction that minimizes the complexity of file transfers. When possible, this API uses multiple connection threads to upload multiple parts of a single upload at once.
* **Low-level APIs.** The low-level APIs correspond to Amazon S3 REST operations. Low-level APIs provide better control and granularity. If you need to pause and resume multipart uploads, vary part sizes during the upload, or do not know the data size in advance, we recommend using low-level APIs. Otherwise, use the high-level API.

##### SDK for Python to upload a file in multiple parts to an S3 bucket

```
import boto3
from boto3.s3.transfer import TransferConfig

# Set the multipart threshold value (5 GB)
GB = 1024 ** 3
config = TransferConfig(multipart_threshold=5*GB)

# Perform the transfer
s3 = boto3.client('s3')
s3.upload_file('FILE_NAME', 'BUCKET_NAME', 'OBJECT_NAME', Config=config)
```

#### Using the REST API 
1. Initiate a multipart upload with the **CreateMultipartUpload** action.
2. Upload a part in a multipart upload with the **UploadPart** action.
3. Complete a multipart upload by assembling previously uploaded parts with the **CompleteMultipartUpload** action.
4. Cancel multipart uploads with the **AbortMultipartUpload** action if needed. This action ends a multipart upload. After a multipart upload is ended, no additional parts can be uploaded using that upload ID. The storage consumed by any previously uploaded parts will be freed.

**If any part uploads are currently in progress when you stop multipart uploads with the AbortMultipartUpload action, those part uploads might or might not succeed. It might be necessary to end a given multipart upload multiple times to completely free all storage consumed by all parts.**

**You can use ListMultipartUploads action to list in-progress multipart uploads. An in-progress multipart upload is a multipart upload initiated using the Initiate Multipart Upload request that has not yet completed or ended.**

**To verify that all parts have been removed so you don't get charged for the part storage, you should call the ListParts action and ensure that the parts list is empty.**

#### Using the AWS CLI
```
$ aws s3 cp large_test_file s3://DOC-EXAMPLE-BUCKET/
```

It's a best practice to use aws s3 commands, such as the **aws s3 cp** command, for multipart uploads and downloads. This is because aws s3 commands automatically perform multipart uploading and downloading based on the file size. Use aws s3api commands, such as **aws s3api create-multipart-upload** command, only when aws s3 commands don't support a specific upload. For example, your multipart upload involves multiple servers, or you manually stop a multipart upload and resume it later. Or, the aws s3 command doesn't support a required request parameter.

#### Amazon S3 Transfer Acceleration
Transfer Acceleration uses the globally distributed edge locations in Amazon CloudFront.

Transfer Acceleration uses standard TCP and HTTP and HTTPS.

##### Transfer Acceleration use cases
Transfer Acceleration is ideal for transferring gigabytes to terabytes of data across continents. It's also useful for clients that upload to a centralized bucket from all over the world. If your objects are smaller than 1 GB or the dataset is less than 1 GB, consider using the CloudFront PUT and POST commands for optimal performance.

#### Transfer Acceleration and regular Amazon S3 transfer
Each time you use Transfer Acceleration to upload an object, AWS checks whether Transfer Acceleration is probably faster than a regular Amazon S3 transfer. **If AWS determines that Transfer Acceleration might not be faster than a regular Amazon S3 transfer, AWS does not charge for that use of Transfer Acceleration.** AWS might bypass Transfer Acceleration for that upload. It’s either faster or no charge is incurred.

#### Transfer Acceleration Speed Comparison tool
This tool allows you to compare accelerated and non-accelerated upload speeds across AWS Regions. The Speed Comparison tool uses multipart uploads to transfer a file from your browser to various Amazon S3 Regions with and without using Transfer Acceleration.

To use the Speed Comparison tool, copy the following URL into your browser window. In the URL, replace **Region** with the Region you are using (for example, **us-west-2**). Replace **DOC-EXAMPLE-BUCKET** with the name of the bucket that you want to evaluate.

(opens in a new tab)https://s3-accelerate-speedtest.s3-accelerate.amazonaws.com/en/accelerate-speed-comparsion.html?region=Region&origBucketName=DOC-EXAMPLE-BUCKET 

#### Transfer Acceleration requirements and considerations
* **Bucket ownership**. – You must be the bucket owner to set the Transfer Acceleration state. The bucket owner is the AWS account that creates the resource. The bucket owner can assign permissions to other users to allow them to set the acceleration state on a bucket.
* **Permissions**. – To enable or disable Transfer Acceleration on a bucket, you must have **s3:PutBucketAccelerateConfiguration permissions**. To return the Transfer Acceleration state of a bucket, you must have **s3:GetBucketAccelerateConfiguration** permissions.
* **Supported URI styles**. – Transfer Acceleration is supported on only **virtual-hosted style** requests. For more information about virtual-hosted and path-style URIs for Amazon S3 endpoints, see the Getting Started with Amazon S3 course.
* **Bucket name**. – The name of the bucket using Transfer Acceleration must be DNS-compliant and must not contain periods (".").
* **Connection endpoints**. – To access a bucket that is enabled for Transfer Acceleration, you must use the endpoint **.s3-accelerate.amazonaws.com**. Or you can use the dual-stack endpoint .**s3-accelerate.dualstack.amazonaws.com** to connect to the enabled bucket over IPv6. You can continue to use the regular endpoint in addition to the accelerate endpoints. For example, suppose your application issues requests to your bucket using the hostname **DOC-EXAMPLE-BUCKET.s3.us-east-1.amazonaws.com**. To accelerate that request, change the hostname in your request to **DOC-EXAMPLE-BUCKET.s3-accelerate.amazonaws.com**.

#### Using Transfer Acceleration
You can enable Transfer Acceleration on a bucket using the console, the REST API, AWS CLI, or AWS SDKs. After Transfer Acceleration is enabled, you can point your Amazon S3 PUT and GET requests to the s3-accelerate endpoint domain name.

#### Use AWS CLI to enable and use Transfer Acceleration
##### Enabling acceleration
```
$ aws s3api put-bucket-accelerate-configuration --bucket my-bucket --accelerate-configuration Status=Enabled
```

**Note**: You use **Status=Enabled** to enable Transfer Acceleration and **Status=Suspended** to suspend Transfer Acceleration.

###### Uploading an object to a bucket with Transfer Acceleration
The following example uploads a file to a bucket with Transfer Acceleration by using the --endpoint-url parameter to specify the accelerate endpoint. 

```
$ aws s3 cp file.txt  s3://DOC-EXAMPLE-BUCKET --region us-east-2 --endpoint-url http://s3-accelerate.amazonaws.com
```

#### Amazon S3 Storage Classes and Use Cases
1. Amazon S3 Standard (S3 Standard)
2. Amazon S3 Intelligent-Tiering (S3 Intelligent-Tiering)
3. Amazon S3 Standard-Infrequent Access (S3 Standard-IA)
4. Amazon S3 One Zone-Infrequent Access (S3 One Zone-IA)
5. Amazon S3 Glacier Instant Retrieval
6. Amazon S3 Glacier Flexible Retrieval
7. Amazon S3 Glacier Deep Archive
8. Amazon S3 on Outposts

#### Amazon S3 Cost Optimization Tools
For predictable workloads, you can use Amazon S3 storage class analysis. For unpredictable workloads, you can use Amazon S3 Intelligent-Tiering.

#### Amazon S3 storage class analysis
Amazon S3 storage class analysis monitors access patterns across objects to help determine when to transition data to the right storage class to optimize costs.

##### Cobfiguration
* **Entire bucket**. With this option, you can receive an analysis for every object in the bucket. When you use the Amazon S3 console to configure storage class analysis, leave the **Prefix** field empty if you want to analyze the whole bucket.
* **Prefix and tags**. You can configure filters that group objects together by prefix, object tags, or by a combination of both. You receive a separate analysis for each filter you configure, and can have up to 1,000 filter configurations per bucket.
* **Exports**. Storage class analysis for a bucket or filter can provide daily exports of analysis data. The analysis for the day is added to the file to form a historic analysis log for the configured filter. The file is updated daily in the destination of your choice. For more information about granting permissions for Amazon S3 storage class analysis, see [Grant Permissions for S3 Inventory and S3 Analytics](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies.html#example-bucket-policies-s3-inventory-1) in the Amazon Simple Storage Service User Guide.

**Amazon S3 storage class analysis only provides recommendations for S3 Standard to S3 Standard-IA classes.**

After you configure storage class analysis reports, it takes 24 hours to generate the first report. After that, Amazon S3 continues to monitor and provide exports on a daily basis. Data in the exported file is sorted by date within the object age group.

You can then use Amazon Quicksight, or another business intelligence tool, to run analytics and produce reports on the data gathered by storage class analysis. 

#### Storage class analysis FAQs
##### How do you use storage class analysis?
You can gather information to help you improve the lifecycle management of your S3 Standard-IA storage. After you configure a filter, you will start seeing data analysis in 24–48 hours, based on the filter in the Amazon S3 console. However, storage class analysis observes the access patterns of a filtered dataset for 30 days or longer to gather information for analysis before giving a result. The analysis continues running after the initial result, and updates the result as the access patterns change.

When performing analysis for infrequently accessed objects, storage class analysis reviews the filtered objects grouped together by age, starting when they were uploaded to Amazon S3. Storage class analysis determines if the age group is infrequently accessed by looking at the following factors for the filtered dataset:
* It reviews objects in the S3 Standard storage class that are larger than 128 KB.
* It calculates how much average total storage you have per age group.
* It determines the average number of bytes transferred out (not frequency) per age group.

Analytics export data only includes requests with data relevant to storage class analysis. This might cause differences in the number of requests and total upload and request bytes compared to those in storage metrics or your own internal systems.

Failed **GET** and **PUT** requests are not counted for the analysis. However, you will see failed requests in storage metrics.

##### How much of your storage did you retrieve?
The Amazon S3 console graphs how much of the storage in the filtered dataset has been retrieved for the observation period.

##### What percentage of your storage did you retrieve?
The Amazon S3 console graphs what percentage of the storage in the filtered dataset has been retrieved for the observation period. 

The storage class analysis uses the following predefined object age groups:
* Amazon S3 objects less than 15 days old
* Amazon S3 objects 15–29 days old
* Amazon S3 objects 30–44 days old
* Amazon S3 objects 45–59 days old
* Amazon S3 objects 60–74 days old
* Amazon S3 objects 75–89 days old
* Amazon S3 objects 90–119 days old
* Amazon S3 objects 120–149 days old
* Amazon S3 objects 150–179 days old
* Amazon S3 objects 180–364 days old
* Amazon S3 objects 365–729 days old
* Amazon S3 objects 730 days or more older

It usually takes about 30 days of observing access patterns to gather enough information for an analysis result. It might take longer than 30 days, depending on the unique access pattern of your data. However, after you configure a filter, you will start seeing data analysis based on the filter in the Amazon S3 console in 24–48 hours. You can see analysis on a daily basis of object access, divided by object age group in the Amazon S3 console.

##### How much of your storage is infrequently accessed?
The Amazon S3 console shows the access patterns grouped by the predefined object age groups. The Frequently accessed or Infrequently accessed indicators are meant to help you in the lifecycle creation process.

#### S3 Intelligent-Tiering
S3 Intelligent-Tiering optimizes costs by automatically moving data between three access tiers with the option to activate a fourth and fifth archive and deep archival tiers. The first tier is optimized for frequent access, and the next lower-cost tier is optimized for infrequent access. The Archive Instant Access tier is a low-cost tier optimized for rarely accessed data.

Additionally, there is an Archive Access tier that must be activated before you can use it. After activation, S3 Intelligent-Tiering moves data you have not accessed for more than 90 consecutive days to the this archival tier. It has the same performance as the S3 Glacier Flexible Retrieval storage class. The last, optional tier, is the Deep Archive Access tier. After activation, objects you have not accessed for 180 days automatically move to this lowest-cost tier. This tier has the same performance as the S3 Glacier Deep Archive storage class.

##### Highlights
S3 Intelligent-Tiering delivers automated cost savings and performance. The following are some highlights:
* Up to 40 percent cost savings using the Frequent Access and Infrequent Access tiers
* Up to 68 percent cost savings using the Archive Instant Access tier
* Up to 95 percent cost savings using the optional Archive Access and Deep Archive Access tiers
* No operational overhead, lifecycle changes, retrieval charges, or minimum storage duration
* The same low-latency and high-throughput performance of S3 Standard with the Frequent, Infrequent, and Archive Instant Access tiers
* Opt-in asynchronous archive capabilities for objects that become rarely accessed
* Durability of 99.999999999 percent of objects across multiple Availability Zones and for 99.9 percent availability over a given year

#### S3 Lifecycle policies
With lifecycle management, objects automatically move to more economical storage classes as the content ages. Lifecycle management also helps you create rules to delete objects based on the object’s age.

An S3 Lifecycle policy transitions objects between storage classes only downward and not upward. Storage classes start with S3 Standard, then S3 Standard-IA, then S3 Intelligent-Tiering, then S3 One Zone-IA, then S3 Glacier, and end with S3 Glacier Deep Archive.

#### S3 Lifecycle configuration rule use cases
* **Application logs**: If you upload periodic logs to a bucket, your application might need them for a week or a month. After that, you might want to delete them.
* **Limited-time access**: You might frequently access documents for a short period of time for specific projects or business needs and then infrequently access them later. You can archive these files and then permanently delete them after their retention periods expire.
* **Archival**: Some companies import data to Amazon S3 primarily for archival purposes. For example, they might archive digital media, financial and healthcare records, raw genomics sequence data, long-term database backups, and data that must be retained for regulatory compliance.

##### Considerations
* **Lifecycle configuration and versioning**. You can add S3 Lifecycle configurations to both un-versioned buckets and versioning-enabled buckets. You can define separate lifecycle rules for current and non-current object versions.
* **Object expiration**. When an object reaches the end of its lifetime, Amazon S3 queues it for removal and removes it asynchronously. There might be a delay between the expiration date and the date Amazon S3 removes an object. You are not charged for storage time associated with an object that has expired. The following are some expiration option types:
 * **Versioning-enabled bucket**: If the current object version is not a delete marker, the lifecycle expiration action causes Amazon S3 to add a delete marker with a unique version ID.
 * **Versioning-suspended bucket**: In a versioning-suspended bucket, the expiration action causes Amazon S3 to create a delete marker with null as the version ID. This delete marker replaces any object version with a null version ID in the version hierarchy, which effectively deletes the object.
 * **Non-version-enabled buckets**: When an object expires, the object is permanently deleted.
* **Minimums**. Amazon S3 doesn't transition objects smaller than 128 KB because it's not cost effective. This applies to the following transitions:
 * From the S3 Standard or S3 Standard-IA storage classes to S3 Intelligent-Tiering or S3 Glacier Instant Retrieval
 * From the S3 Standard storage class to S3 Standard-IA or S3 One Zone-IA

Objects must remain for a minimum of 30 days in S3 Standard before they can transition to S3 Standard-IA and S3 One Zone-IA.

Objects in S3 Intelligent-Tiering, S3 Standard-IA, and S3 One Zone-IA storage are charged for a minimum storage duration of 30 days. Objects deleted before 30 days incur a pro-rated charge equal to the storage charge for the remaining days.

* **Configurations not supported**. Lifecycle configuration on buckets with multi-factor authentication is not supported. **AWS CloudTrail object-level logging does not capture lifecycle actions. If you require logging, you can use Amazon S3 server access logs to capture S3 Lifecycle actions.**

#### AWS Storage Blog: Canva
Review [AWS BLOG](https://aws.amazon.com/blogs/storage/how-canva-saves-over-3-million-annually-in-amazon-s3-costs/) to learn how Canva saves over $3 million annually in Amazon S3 costs by using storage class analysis and S3 Lifecycle policies.

#### Additional Resources
##### Uploading an object using multipart upload
How to use AWS SDKs, REST API, and AWS CLI for multipart uploads - [MULTIPART UPLOAD](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpu-upload-object.html).

##### Enable or disable Transfer Acceleration
Setting up the permission to enable or disable Transfer Acceleration on a bucket - [PUT BUCKET](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketAccelerateConfiguration.html).

##### Return the Transfer Acceleration state
Setting up the permission to return the Transfer Acceleration state of a bucket - [GET BUCKET](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketAccelerateConfiguration.html).

##### [PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html)

##### [AWS Signature Version 4](https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html)

##### [Signing and authenticating REST requests](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RESTAuthentication.html)

#### Advanced Features of Amazon S3
#### Pre-assessment
##### What special step do users need to follow when accessing a presigned URL for an encrypted object?
* Use the URL in the same way as for unencrypted objects.

##### What is the maximum length of a SQL expression when using Amazon S3 Select?
* 256 KB

#### Accessing Your Amazon S3 Resources

#### Object URLs
The Object URL you can find in the console is called **virtual-hosted-style access**. This means that **the bucket name is part of the domain name** in the URL.

```
https://DOC-EXAMPLE-BUCKET-1111111.s3.us-west-2.amazonaws.com/kitty.jpg
```

Whether the object or file is publicly accessible directly through the link is governed by the following: 
* **For buckets with access control list (ACL) disabled**: Accessing the object or file through the link is determined by the bucket policies and the Block Public Access settings related to bucket policies. 
* **For buckets with ACL enabled**: ACL permissions are active on the file. Accessing the object or file through the link depends on both of ACL permissions assigned to the file and the Block Public Access settings related to ACL permissions. 

#### Presigned URLs
The main purpose of a presigned URL is to grant temporary access to the required object. When you create a presigned URL, you must provide your security credentials and specify the following:
* Bucket name
* Object key
* HTTP method (PUT for uploading objects)
* Expiration date and time

A presigned URL remains valid for a limited period of time, which is specified when the URL is generated. You can use presigned URLs to embed live links in web pages, which can be valid for up to seven days.

##### Permissions to the object
Anyone with valid security credentials can create a presigned URL. However, to access an object successfully, the user creating the presigned URL must have permissions to perform the operation on the object.

##### Credentials
The credentials that you can use to create a presigned URL include the following:
* AWS Identity and Access Management (IAM) instance profile – Valid up to 6 hours.
* AWS Security Token Service (AWS STS) – Valid up to 36 hours when signed with permanent credentials, such as the credentials of the AWS account root user or an IAM user.
* IAM user – Valid up to 7 days when using AWS Signature Version 4.

To create a presigned URL that's valid for up to 7 days, first designate IAM user credentials (the access key and secret access key) to the SDK that you're using. Then, generate a presigned URL using AWS Signature Version 4.

##### Token expiration
If you created a presigned URL using a temporary token, the URL expires when the token expires, even if you created the URL with a later expiration time.

##### Tools required
You can generate a presigned URL programmatically using REST API, AWS Command Line Interface (AWS CLI), an AWS SDK, or the AWS toolkit in AWS Cloud9.

#### [How to generate presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html)

#### Amazon S3 resource ARNs
```
arn:partition:service:region:namespace:relative-id
```

#### Amazon S3 ARN examples
##### The following ARN identifies the /developers/design_info.doc object in the DOC-EXAMPLE-BUCKET bucket.
```
arn:aws:s3:::DOC-EXAMPLE-BUCKET/developers/design_info.doc
```

##### The following ARN uses the wildcard * in the relative-ID part of the ARN to identify all objects in the DOC-EXAMPLE-BUCKET bucket.
```
arn:aws:s3:::DOC-EXAMPLE-BUCKET/*
```

##### The following ARN uses * to indicate all Amazon S3 resources (all S3 buckets and objects). 
```
arn:aws:s3:::*
```

##### The following ARN uses both wildcards, * and ?, in the relative-ID part. It identifies all objects in buckets, such as DOC-EXAMPLE-BUCKET1, DOC-EXAMPLE-BUCKET2, DOC-EXAMPLE-BUCKET3, and so on. 
```
arn:aws:s3:::DOC-EXAMPLE-BUCKET?/*
```

##### Policy variables in Amazon S3 ARNs
Suppose that you organize your bucket as a collection of folders, one folder for each of your users. The folder name is the same as the username. To grant users permission to their folders, you can specify a policy variable in the resource ARN: 
```
arn:aws:s3:::DOC-EXAMPLE-BUCKET/developers/${aws:username}/
```

#### Static website hosting
1. **Create an S3 bucket**: You start by creating an S3 bucket and giving it a unique name. This bucket will act as the container for your website files. 
2. **Configure the bucket for website hosting**: After the bucket is created, you configure it to activate website hosting. This involves specifying the index document (for example, index.html) and optionally an error document. 
3. **Upload your website files**: Upload your static website files (HTML, CSS, JavaScript, images, and so on) to the S3 bucket. You can do this through the console, AWS CLI, or AWS SDKs.
4. **Set permissions and make files public**: You need to ensure that your website files are publicly accessible. By default, Amazon S3 blocks public access to the bucket and objects for security reasons.
5. **Obtain the website endpoint**: After the files are uploaded and the permissions are set, Amazon S3 provides you with a website endpoint URL. This URL serves as the address for your static website.
6. **Configure DNS and domain**: If you have a custom domain for your website, you can configure DNS settings to point it to the Amazon S3 website endpoint. Users can then access your website through your custom domain name.

#### [Configuring a static website on Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/HostingWebsiteOnS3Setup.html)

#### Managing object tagging
A tag is a basic label consisting of a customer-defined key and an optional value that can be applied to a whole bucket or to individual objects in a bucket. For example, you can use a tag of **phototype:raw** to identify raw photographs and **phototype:finished** to identify processed photos.

**Tags are not additive. If you put new tags on an object that already has tags, the new tags will replace the current tags.**

When you assign tags, use the following guidelines:
* You can create tags from the console, AWS CLI, or APIs.
* Tag keys and values are case sensitive. 
* You can associate **up to 10 tags** with an object. Tags associated with an object must have unique tag keys. 
* A **tag key** can be up to **128 Unicode characters** in length, and **tag values** can be **up to 256 Unicode characters** in length. 

#### Use cases
##### Access control
You can use tagging with IAM policies for fine-grained permission control. The tag and its value create a condition in the policy to allow or deny a specified action.

Use the Amazon S3 condition key **"s3:ExistingObjectTag/<key>": "<value>"** to specify the tag's key and value. 

In the following example, this policy grants a user read-only privileges to files with a tag of **phototype: finished**. 

##### Lifecycle management
In a bucket's lifecycle rule configuration, you can specify a filter to select a subset of objects to which the rule applies. You can specify a filter based on the key name prefixes, object tags, or both.

For example, you plan to archive raw photos to Amazon S3 Glacier after orders are finalized. You configure a lifecycle rule with a filter for objects with the prefix **photos/** and with the **phototype:raw** tag.

##### Amazon CloudWatch metrics and AWS CloudTrail logs
When working with CloudWatch metric configurations, you can filter the configuration into groups of related objects within a single bucket based on tags. If you specify a filter, only requests that operate on single objects can match the filter and be included in the reported metrics. Requests like **Delete Multiple Objects** and **List** don't return any metrics for configurations with filters.

For example, you want to view metrics only on finished photos, so you filter on the **phototype:finished** tag.

##### Replication
You can use tags to determine which objects are replicated. Tags offer fine-grained control to selectively replicate your storage to back up critical data for compliance and disaster recovery.

For example, you might choose to replicate only files with a tag of **phototype:finished** to back up your customer work.

#### Adding a tag
Tags can be managed from the console or programmatically using the AWS SDKs. The following example shows a tag, **phototype:raw**, applying to objects in the bucket that match the **Specified objects** search criteria.

#### Using automation to tag objects
Automation ensures that tags are consistently applied when resources are created. The following example shows how to use the AWS SDK for Python (Boto3) to set tags for a new object. 

```
import logging
import boto3
from botocore.exceptions import ClientError
client = boto3.client('s3')


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True
s3 = boto3.client('s3')
with open("./test.txt", "rb") as f:

    s3.upload_fileobj(f, "DOC-EXAMPLE-BUCKET", "test.txt",
      ExtraArgs={
        'Metadata': {'mykey': 'myvalue'}
        })


# set tag after object uploads to Amazon S3
response = client.put_object_tagging(
    Bucket='DOC-EXAMPLE-BUCKET',
    Key='test.txt',
    Tagging={
        'TagSet': [
            {
                'Key': 'ENV',
                'Value': 'Prod'
            },
             {
                'Key': 'type',
                'Value': 'txt'
            }
        ]
    }
)
```

**Tags are not additive. If you put new tags on an object that already has tags, the new tags will replace the current tags.**

#### [Using object tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-tagging.html)

#### Amazon S3 Object Lambda

##### Using S3 Object Lambda
The following examples are potential use cases that can be streamlined with S3 Object Lambda:
* Redact personally identifiable information for analytics or non-production environments. 
* Convert across data formats, such as converting XML to JSON. 
* Augment data with information from other services or databases. 
* Compress or decompress files as they are being downloaded. 
* Resize and watermark images using caller-specific details, such as the user who requested the object.
* Implement custom authorization rules to access data.

##### Getting started
You can start using S3 Object Lambda with the following steps: 
1. Create a Lambda function to transform data for your use case. 
2. Create an S3 Object Lambda Access Point from the Amazon S3 console.
3. Select the Lambda function that you created in step 1.
4. Provide a supporting S3 Access Point to give S3 Object Lambda access to the original object.
5. Update your application configuration to use the new S3 Object Lambda Access Point to retrieve data from Amazon S3.

##### [Transforming objects with S3 Object Lambda ](https://docs.aws.amazon.com/AmazonS3/latest/userguide/transforming-objects.html)

#### Amazon S3 Batch Operations
* **Put object tagging.** Replace the Amazon S3 object tags of each object that is listed in the manifest.
* **Put object ACL.** Replace the Amazon S3 ACLs for each object that is listed in the manifest.
* **Initiate restore object.** Send a restore request to Amazon S3 Glacier for each object that is specified in the manifest.
* **Put object copy.** Copy each object specified in the manifest. You can copy objects to a different bucket in the same Region or to a bucket in a different Region.
* **Invoke Lambda function.** Invoke a Lambda function to perform custom actions on objects that are listed in a manifest.
* **Manage S3 Object Lock.** Manage the retention dates of many Amazon S3 objects. You can add legal holds to many Amazon S3 objects at once.

##### [Additional information](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-operations.html)

##### Terminology 
###### Manifest
The manifest is a list of all of the objects that you want S3 Batch Operations to run the specified action on. You can use a CSV-formatted Amazon S3 inventory report as a manifest or use your own customized CSV list of objects. 

###### Job
A job is the basic unit of work for S3 Batch Operations. A job contains all of the information necessary to run the specified operation on the objects listed in the manifest. After you provide this information and request that the job begin, the job runs the operation for each object in the manifest.

###### Operation
The operation is the type of API action, such as copying objects, that you want the S3 Batch Operations job to run. Each job performs a single type of operation across all objects that are specified in the manifest. 

###### Task
A task is the unit of execution for a job. A task represents a single call to an Amazon S3 or Lambda API to perform the job's operation on a single object. S3 Batch Operations creates one task for each object specified in the manifest.

##### Workflow
1. **Choose objects**. Specify the manifest for your job. The manifest is an Amazon S3 object that lists object keys that you want Amazon S3 to act on.
2. **Select an operation**. Specify the operation that you want S3 Batch Operations to run against the object in the manifest. Each operation type accepts parameters that are specific to that operation. You can then perform the same tasks as if you performed the operation one by one on each object.
3. **View process**. S3 Batch Operations does your requested actions across your target S3 objects. It automatically retries and displays object-level progress. It also sends notifications and delivers completion reports when requested changes are made to your target Amazon S3 objects. 

##### Assigning permissions
There are two considerations for granting permissions to create an S3 Batch Operations job: the identity who will create the job requires the appropriate permissions, and Amazon S3 must have permission to perform S3 Batch Operations on your behalf.

###### Creating a job
The identity creating the Amazon S3 Batch Operations job must have the **s3:CreateJob** permission. This identity must also have the **iam:PassRole** permission to pass the IAM role specified for the job to Amazon S3 Batch Operations.

###### Creating a role for Amazon S3
The role that S3 Batch Operations uses to perform the job requires the following two policies:
* It requires a trust policy that permits the S3 Batch Operations service principal to assume the IAM role.
* It requires a permissions policy that grants S3 Batch Operations permission to work with your S3 objects. The exact permissions required will depend on the operation. Keep the following guidelines in mind:
 * Regardless of the operation, Amazon S3 needs permission to read your manifest object from your S3 bucket. For Amazon S3 inventory report manifests, grant permission to read the **manifest.json** object and all associated CSV data files.
 * Grant permission to write a report to your bucket if your job includes a completion report.
 * Version-specific permissions such as **s3:GetObjectVersion** are required only if you are specifying the version ID of the objects.
 * If you are running S3 Batch Operations on encrypted objects, the IAM role must also have access to the AWS Key Management Service (AWS KMS) keys used to encrypt them.

##### IAM policy examples
The following examples of the policies must be attached to the IAM role that S3 Batch Operations uses to perform the job. If you create the job using the Amazon S3 console, the console will generate policies specific to your job. You can copy and paste these into the IAM editor during the job configuration. If you use AWS CLI or an SDK, you must complete all IAM tasks before creating the job.

The following is an example of the trust policy that you must attach to the role to permit the S3 Batch Operations service principal to assume the role: 

```
{
   "Version":"2012-10-17",
   "Statement":[
      {
         "Effect":"Allow",
         "Principal":{
            "Service":"batchoperations.s3.amazonaws.com"
         },
         "Action":"sts:AssumeRole"
      }
   ]
}
```

The following is an example of a permissions policy that permits S3 Batch Operations to perform a Put object tagging operation. You need to personalize the following three parameters for your environment: **DOC-EXAMPLE-SOURCE-BUCKET**, **DOC-EXAMPLE-MANIFEST-BUCKET**, and **DOC-EXAMPLE-REPORT-BUCKET**.

```
{
  "Version":"2012-10-17",
  "Statement":[
    {
      "Effect":"Allow",
      "Action":[
        "s3:PutObjectTagging",
        "s3:PutObjectVersionTagging"
      ],
      "Resource": "arn:aws:s3:::{{<DOC-EXAMPLE-SOURCE-BUCKET>}}/*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:GetObjectVersion",
        "s3:GetBucketLocation"
      ],
      "Resource": [
        "arn:aws:s3:::{{<DOC-EXAMPLE-MANIFEST-BUCKET>}}/*"
      ]
    },
    {
      "Effect":"Allow",
      "Action":[
        "s3:PutObject",
        "s3:GetBucketLocation"
      ],
      "Resource":[
        "arn:aws:s3:::{{<DOC-EXAMPLE-REPORT-BUCKET>}}/*"
      ]
    }
  ]
}
```

##### [Additional information about BATCH OPS POLICIES](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-iam-role-policies.html)

##### Amazon S3 Inventory
Amazon S3 Inventory helps you manage your storage by creating lists of the objects in an S3 bucket on a defined schedule. You can configure multiple inventory lists for a bucket. The inventory lists are published to comma-separated values (CSV), Apache Optimized Row Columnar (ORC), or Apache Parquet (Parquet) files in a destination bucket.

You can configure what object metadata to include in the inventory and whether to list all object versions or only current versions. You can also configure where to store the inventory list flat-file output and whether to generate the inventory daily or weekly. It might take up to 48 hours for Amazon S3 Inventory to deliver the first report.

The most convenient way to set up an inventory is by using the console. You can also use the REST API, AWS CLI, or AWS SDKs. The console will automatically attach an appropriate policy to the destination bucket for you.

##### Configuring Amazon S3 Inventory
1. Create a destination bucket
2. Configure an Amazon S3 inventory

##### Creating an S3 Batch Operations job
1. Create a manifest
2. Create an IAM role
3. Create the job
4. Choose a manifest file
5. Select the manifest file
6. Choose the operation
7. Configure additional options
8. Configure additional options
9. Review and create your job
10. Wait for the job to be ready
11. Prepare to run the job
12. Run the job

#### Amazon S3 Select
#### Using SQL with Amazon S3 Select 
With Amazon S3 Select, you can use basic SQL queries to filter the contents of Amazon S3 objects. You can retrieve just the subset of data that you need instead of downloading the entire object. This reduces the amount of data that Amazon S3 transfers, which can greatly reduce transfer costs and increase performance. Amazon S3 Select can query compressed CSV-formatted reports directly, saving you the time of downloading and decompressing them.

Amazon S3 Select works on objects stored in CSV, JSON, or Apache Parquet format. It also works with objects that are compressed with GZIP or BZIP2 (for CSV and JSON objects only), and server-side encrypted objects. You can specify the format of the results as either CSV or JSON, and you can determine how the records in the result are delimited.

#### Requirements and constraints
##### Requirements
* You must have **s3:GetObject** permission for the object you are querying. 
* If the object you are querying is encrypted with server-side encryption with customer-provided keys (SSE-C), you must use HTTPS. You must provide the encryption key in the request.

##### Constraints
* The maximum length of a SQL expression is 256 KB. 
* The maximum length of a record in the input or result is 1 MB. 
* Amazon S3 Select can only emit nested data by using the JSON output format. 
* You cannot query objects in the S3 Glacier Flexible Retrieval, S3 Glacier Deep Archive, or Reduced Redundancy Storage (RRS) storage classes. You also cannot query the objects in the S3 Intelligent-Tiering Archive Access tier or the S3 Intelligent-Tiering Deep Archive Access tier. 

##### Parquet object constraints
* Amazon S3 Select supports only columnar compression using GZIP or Snappy. Amazon S3 Select doesn't support whole-object compression for Parquet objects. 
* Amazon S3 Select doesn't support Parquet output. You must specify the output format as CSV or JSON. 
* The maximum uncompressed row group size is 512 MB. 
* You must use the data types that are specified in the object's schema.
* Selecting a repeated field returns only the last value.

#### Knowledge Check
##### What formats should developers store objects in if they want to use Amazon S3 Select? (Select TWO.)
* Comma-separated values (CSV)
* JSON

Wrong answers:
* Microsoft Excel (XLSX)
* Open Document Format (ODF)
* Apache Optimized Row Columnar (ORC)

Amazon S3 Select works on objects stored in **CSV, JSON**, or Apache Parquet format. It also works with objects compressed with GZIP or BZIP2 (for CSV and JSON objects only) and server-side encrypted objects.

##### A developer is configuring a job to copy the contents of a source bucket to a destination bucket (Put object copy). They want a completion report to be written to a reports bucket. They must configure a permissions policy for Amazon S3 Batch Operations that permits certain actions on certain resources. Which actions must they permit for the bucket containing the manifest? (Select TWO.)
* GetObject
* GetBucketLocation

Wrong answers:
* PutObject
* GetObjectTagging
* PutObjectTagging

The correct options are **GetObject** and **GetBucketLocation**.

When using permissions policies for S3 Batch Operations to perform a PUT object tagging operation, there are three actions permitted in the bucket containing the manifest. They are **GetObject**, **GetObjectVersion**, and **GetBucketLocation**.

##### What are appropriate use cases for presigned URLs? (Select TWO.)
* Embed it on a website to download objects.
* Use it in a command line client (such as curl) to download objects.

Wrong answers:
* Use it as a permanent link on a static website. 
* Send it in an email containing personally identifiable information. 
* Use it with permanent user credentials.

A use-case scenario for presigned URLs is granting temporary access to Amazon S3 resources. For example, users can embed a presigned URL on a website or use it in a command line client (such as curl) to download objects. A user can also programmatically generate a presigned URL for another user to upload an object to a bucket.

#### Security in Amazon S3

#### Amazon S3 Block Public Access
**Block all public access** setting activated by default.

##### What does private access mean?
Unless you share a bucket and objects with someone outside of your account, only the principals in your AWS account can access the objects in your S3 buckets. S3 Block Public Access provides controls across an entire AWS account or at the individual S3 bucket level. Implementing S3 Block Public Access ensures that objects are not publicly accessible.

##### What does public access mean?
Amazon S3 considers a bucket or object public if it grants any permissions to members of the following groups:
* **AuthenticatedUsers** – This group allows all AWS accounts to access the resource. Any authenticated AWS user, from any AWS account in the world, can access your resource if the request is signed (authenticated). 
* **AllUsers** – This group allows anyone in the world access to the resource. The requests can be signed (authenticated) or unsigned (anonymous).

##### Is S3 Block Public Access on by default?
For new buckets, access points, and objects, S3 Block Public Access is on by default. It stays active even if a user modifies an object's permissions to allow public access. The

S3 Block Public Access setting overrides the modified permissions and continues to restrict public access to the object.

##### Why don't I want my objects made public?
Few use cases would require a bucket to be made public. Buckets and objects that are public can be accessed by anyone on the internet. Most businesses do not want their intellectual property, business documentation, or customer data made available to the public. Therefore, S3 Block Public Access is built into Amazon S3 security by default.

##### Can I activate public access on only some objects or buckets?
Yes. You can grant public access to buckets and objects through access control lists (ACLs), access point policies, and bucket policies. By doing this, you can have some buckets or objects available for public consumption. Others can be secured for private access or locked down for access only to a particular service or set of users.

##### Can I activate S3 Block Public Access on a single object?
Amazon S3 doesn't support S3 Block Public Access settings for a single object. You can activate S3 Block Public Access settings only for access points, buckets, and AWS accounts.

#### Overview
1. **S3 Block Public Access**. You can block all public access to your Amazon S3 objects at the bucket or account level. S3 Block Public Access overrides other Amazon S3 access permissions to enforce a no public access policy.
2. **Set block public access permissions**. With a few selections in the Amazon S3 console, you can turn on S3 Block Public Access. Activate all four settings, unless you know you need public access.
3. **Block all public access**. When you activate the primary option, you activate all four of the following options: 
 * Block public access granted by new ACLs.
 * Block public access granted by any ACLs.
 * Block public access granted by new public bucket policies.
 * Block public and cross-account access by any public bucket policies.4. Audit your Amazon S3 ACLs and policies
4. **Audit your Amazon S3 ACLs and policies**. Use AWS Trusted Advisor and the Amazon S3 console to ensure that your buckets are private by using bucket permission checks.

#### S3 Block Public Access settings
##### Block all public access
Sometimes, you want to make sure that a bucket will never allow public access. With this one-click option, you can prevent public access to your bucket. This overrides any configured ACLs and bucket polices that would normally grant public access. Choosing this option equates to choosing all the other options listed here.

Any new bucket you create will have this option on by default. You need to deactivate this option if you want to allow public access to your buckets or objects.

##### Block public access granted through new ACLs
This option only affects how you evaluate ACL public permissions, and it ignores any existing ACLs that grant public permission on buckets and objects. This does not alter the existing ACLs themselves, but any resources configured with existing public ACLs will no longer be publicly accessible.

It can be confusing because it does not prevent you from creating new ACLs that would normally grant public access. You can still create them, but those ACLs will not become effective, resulting in the bucket or object not being publicly accessible. 

You should review your ACLs, once activated, and remove any public ACLs to prevent any possible future mistakes. Any existing public ACLs will no longer be ignored if the Block public access granted through any ACLs option is later deactivated.

With this option, if you have any bucket policies granting public access to buckets and objects, those buckets or objects will remain publicly accessible. If you want to block all public access to buckets and objects, choose the Block all public access option.

##### Block public access granted through new public bucket policies
This option only prevents the creation of new bucket policies that grant public access. Any existing bucket policies are not affected. If you currently have any bucket policies configured that grant public access, those buckets or objects will remain publicly accessible. 

To use this setting effectively, you should apply it at the AWS account level. A bucket policy can permit users to alter a bucket's S3 Block Public Access settings. Therefore, users who have permission to change a bucket policy can insert a policy to disable the S3 Block Public Access settings for the bucket. If you activate this setting for the entire account instead of a specific bucket, Amazon S3 blocks public policies. It does this even if a user alters the bucket policy to deactivate this setting.

With this option, if you have any existing bucket policies or ACLs granting public access to buckets and objects, they will remain publicly accessible. If you want to block all public access to buckets and objects, choose the Block all public access option.

##### Block access granted through any public bucket policies
This option only affects how you evaluate bucket policy permissions. This option ignores any buckets or objects that have public permissions granted through bucket policies. It restricts access to a bucket with a public policy to only AWS services and authorized users within the bucket owner's account. It blocks all cross-account access to the bucket with a public policy except by AWS services. It still permits users within the account to manage the bucket. 

This does not alter existing bucket policies, but it ignores any existing bucket policies that grant public access. It blocks public access and any cross-account access configurations. 

With this option, if you have any ACLs granting public access to buckets and objects, they will remain publicly accessible. If you want to block all public access to buckets and objects, choose the Block all public access option.

#### Preventing accidental public access
##### DO
* Use S3 Block Public Access at the account level to prevent public access to your buckets.
* Audit your existing bucket ACLs and bucket policies.
* Configure the appropriate roles and permissions to limit who can change S3 Block Public Access settings.

##### DON'T
* Don't allow public access unless you have an explicit reason that something must be public, such as static website hosting in Amazon S3.
* Don't allow public access to troubleshoot. Start with the most restrictive permissions and open them only as needed.

#### Amazon S3 Object Ownership
Object Ownership is an Amazon S3 bucket-level setting you can use to control ownership of objects uploaded to a bucket, and to activate or deactivate ACLs.

##### The following option works with ACLs deactivated:
* **Bucket owner enforced (default)**: ACLs are deactivated, and the bucket owner automatically owns and has full control over every object in the bucket. ACLs no longer affect permissions to data in the S3 bucket. The bucket uses policies to define access control.

##### The following options work with ACLs activated:
* **Bucket owner preferred**: The bucket owner will own the object if uploaded with the bucket-owner-full-control canned ACL. Without this setting and canned ACL, the object is uploaded to the bucket, but the uploading account still owns the bucket. 
* **Object writer**: The AWS account that uploads an object owns the object, has full control over it, and can grant other users access to it through ACLs.

When the ACLs enabled option is selected, you can edit Object Ownership options, which are Bucket owner preferred and Object writer.

For most modern use cases in Amazon S3, AWS recommends that you keep ACLs deactivated. You can use your bucket policy to share data with users outside of your account as needed. This approach simplifies permissions management. You can deactivate ACLs on both newly created and already existing buckets. For newly created buckets, ACLs are off by default. For an existing bucket with objects, after you deactivate ACLs, the object and bucket ACLs are no longer part of an access evaluation. Access is granted or denied based on policies. For existing buckets, you can activate ACLs at any time after you deactivate them. Your pre-existing bucket and object ACLs will be restored.

##### Enforcing S3 Object Ownership
If you activate ACLs and set the Object Ownership to Bucket owner preferred, you can add a bucket policy to require all Amazon S3 PUT operations to include the bucket-owner-full-control canned ACL. If the uploader fails to meet the ACL requirement in their upload, the request fails. This setting helps bucket owners enforce uniform object ownership across all newly uploaded objects in their buckets.

##### [Controlling ownership of objects and disabling ACLs for your bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html)

#### Controlling Access with Access Policies
Access policies dictate who has access to which resources. There are two types of access policies: resource based and identity based. Resource-based policies attach to resources, such as buckets and objects. For example, bucket policies and ACLs are resource-based policies because you attach them directly to resources, such as buckets and objects.

##### Bucket policies
To grant other AWS accounts or IAM users access to a bucket and the objects in it, attach a bucket policy. Because you are granting access to a user or account, a bucket policy must define a principal entity within the policy. A principal is an account, user, role, or service. Bucket policies supplement and sometimes replace legacy ACL-based access policies.

**Bucket policies are limited to 20 KB in size.**

Bucket policies grant access to another AWS account or IAM user. Therefore, you must specify the principal you are granting access to as a **Principal** in the bucket policy.

```
{
   "Version":"2012-10-17",
   "Statement":[
      {
         "Principal":{
            "AWS":"arn:aws:iam::111122223333:user/JohnDoe"
         },
         "Effect":"Allow",
         "Action":[
            "s3:GetObject",
            "s3:GetObjectVersion"
         ],
         "Resource":"arn:aws:s3:::DOC-EXAMPLE-BUCKET/*"
      }
   ]
}
```

##### Bucket policy use cases
* You need to grant cross-account permissions to other AWS accounts or users in another account, without using IAM roles.
* Your IAM policies reach the size limits for users, groups, or roles.
* You prefer to keep access control policies in the Amazon S3 environment.
* You need to ensure strict access control for sensitive data stored in a specific bucket. You also do not want access granted inadvertently to unauthorized users through IAM policies.

#### Access policy elements
##### Effect
The Effect element specifies whether the statement actions are allowed or denied. Valid values for Effect are Allow and Deny. This is a required element.

##### Action
The Action element defines the actions that the policy allows or denies. This is a required element.

##### NotAction
NotAction is an advanced policy element that explicitly matches everything except the specified list of actions. Either Action or NonAction is required in a policy.

##### Principal
The Principal element defines which principal is allowed or denied access to a resource. You cannot use the Principal element in an IAM identity-based policy because you are already attaching the policy directly to a principal.

For resource-based policies, such a bucket policy, a principal entity must be defined within the policy.

##### NotPrincipal
Use the NotPrincipal element to deny access to all principals except specific users. These include IAM users, federated users, IAM roles, AWS accounts, AWS services, or other principals specified in the NotPrincipal element.

##### Resource or NotResource
The Resource and NotResource elements specify the objects (or resources) that the statement applies to. Statements must include either a Resource or a NotResource element and must be specified as an Amazon Resource Name (ARN). Resource is a required element in the policy.

##### Condition (Optional)
Use the Condition element (or Condition block) to specify conditions for when a policy is in effect. This is an optional element.

#### Bucket policy examples
##### Allowing a user to read only objects that have a specific tag key and value ^^environment: production**

```
{
   "Version":"2012-10-17",
   "Statement":[
      {
         "Principal":{
            "AWS":"arn:aws:iam::111122223333:user/JohnDoe"
         },
         "Effect":"Allow",
         "Action":[
            "s3:GetObject",
            "s3:GetObjectVersion"
         ],
         "Resource":"arn:aws:s3:::DOC-EXAMPLE-BUCKET/*",
         "Condition":{
            "StringEquals":{
               "s3:ExistingObjectTag/environment":"production"
            }
         }
      }
   ]
}
```

##### Requiring SSE-KMS for all objects written to a bucket
The following example policy requires every object that is written to the bucket to be encrypted with server-side encryption using AWS Key Management Service (AWS KMS) keys (SSE-KMS). If the object isn't encrypted with SSE-KMS, the request will be denied.

```
{
"Version": "2012-10-17",
"Id": "PutObjPolicy",
"Statement": [{
  "Sid": "DenyObjectsThatAreNotSSEKMS",
  "Principal": "*",
  "Effect": "Deny",
  "Action": "s3:PutObject",
  "Resource": "arn:aws:s3:::DOC-EXAMPLE-BUCKET/*",
  "Condition": {
    "Null": {
      "s3:x-amz-server-side-encryption-aws-kms-key-id": "true"
    }
  }
}]
}
```

##### Restricting access to only HTTPS requests
Suppose you want to prevent potential attackers from manipulating network traffic. You can use HTTPS (TLS) to only allow encrypted connections while restricting HTTP requests from accessing your bucket. To determine whether the request is HTTP or HTTPS, use the **aws:SecureTransport** global condition key in your S3 bucket policy. The **aws:SecureTransport** condition key checks whether a request was sent by using HTTP.

If a request returns true, then the request was sent through HTTPS. If the request returns false, then the request was sent through HTTP. You can then allow or deny access to your bucket based on the necessary request scheme.

In the following example, the bucket policy explicitly denies HTTP requests.

```
{
    "Version": "2012-10-17",
    "Statement": [{
        "Sid": "RestrictToTLSRequestsOnly",
        "Action": "s3:*",
        "Effect": "Deny",
        "Resource": [
            "arn:aws:s3:::DOC-EXAMPLE-BUCKET",
            "arn:aws:s3:::DOC-EXAMPLE-BUCKET/*"
        ],
        "Condition": {
            "Bool": {
                "aws:SecureTransport": "false"
            }
        },
        "Principal": "*"
    }]
}
```

#### Amazon S3 Object Lock
 With S3 Object Lock, you can store objects using a write once, read many (WORM) model. Use S3 Object Lock to prevent objects from being deleted or overwritten for a fixed amount of time or indefinitely. You can use S3 Object Lock if you have regulatory requirements that specify that data must be WORM protected. You can also use S3 Object Lock to add an additional layer of protection against data changes and deletion.

S3 Object lock provides the following two primary ways to manage object retention:
* **Retention periods** specify a fixed period of time during which an object can’t be overwritten or deleted.
* **Legal holds** provide the same protection as a retention period but have no expiration date. Instead, legal holds remain in place until you explicitly remove them.

#### S3 Object Lock considerations
The following are the four S3 Object Lock considerations:
* Before you can lock any objects, you must configure a bucket to use S3 Object Lock. To do this, you specify when you create the bucket that you want to activate S3 Object Lock. After you configure a bucket for S3 Object Lock, you can lock objects in that bucket using retention periods, legal holds, or both.
* S3 Object Lock works only in versioned buckets, and retention periods and legal holds apply to individual object versions. When you create a bucket with S3 Object Lock turned on, Amazon S3 automatically activates versioning for the bucket.
* S3 Object lock doesn't prevent you from creating new versions of an object. If you create an object with same name as an existing protected object, Amazon S3 creates a new object version. The existing protected version of the object remains locked according to its retention configuration.
* S3 Object Lock protection is maintained regardless of which storage class your objects reside in and throughout S3 Lifecycle transitions between storage classes.

#### Retention modes
When setting a retention period for your objects, you can choose between two retention modes to manage object retention. These retention modes apply different levels of protection to your objects. S3 Object Lock provides two retention modes: governance mode and compliance mode.

##### Governance mode
In governance mode, you can grant specific users permission to alter the retention settings or delete the object, if necessary.

You can also use governance mode to test retention-period settings before creating a compliance-mode retention period.

##### Compliance mode
In compliance mode, an object is immutable until the retention period you defined passes. In compliance mode, no users can overwrite or delete protected objects, including the root user in your AWS account.

When an object uses compliance mode, you cannot change its retention mode or shorten its retention period. The only way to delete an object under compliance mode before its retention date expires is to delete the associated AWS account. We recommend using compliance mode if you have a legal requirement to store compliant data.

#### Bypassing governance mode
To bypass **governance-mode** retention settings, you must meet the following requirements:
* Your user account must have the **s3:BypassGovernanceRetention** permission.
* You must explicitly include the **x-amz-bypass-governance-retention:true** header as a request header with any request that requires overriding governance mode. The console automatically applies this header for requests made through the console if you have the permission required to bypass governance mode.

The following example shows you how to bypass governance-mode retention settings to delete an object using AWS Command Line Interface (AWS CLI). This command contains the following attributes: 
* **bucket**: The name of the bucket where the object resides
* **key**: The name of the object you want to delete
* **version-id**: The version ID of the object you want to remove
* **bypass-governance-retention**: Indicates that S3 Object Lock should bypass governance mode restrictions to process this operation

```
aws s3api delete-object --bucket DOC-EXAMPLE-BUCKET --key filename.csv --version-id iOrnGkO8C8ISXSwF.iFrtNjOkek11GbG --bypass-governance-retention
```

#### Specifying object retention periods
You can configure a retention period on an object version either for the entire bucket or at the object-version level.

##### Configuring a retention period for all objects in a bucket
If you want to automatically protect all object versions in a bucket, you can configure a default retention period. During the retention period you define, Amazon S3 stores a timestamp in your object version's metadata to indicate when the retention period expires.

You apply a retention period, either in number of days or number of years. The minimum is 1 day, and there is no maximum limit.

##### Configuring a retention period for a specific object version
You can apply retention settings on individual objects in addition to default retention settings for all objects within an S3 bucket. For example, suppose that for compliance reasons, you need to store a set of objects for 7 years and another set of objects for 5 years. Using S3 Object Lock, you can put 7-year and 5-year retention dates on the two sets of objects.

When you assign a retention period for a particular object version, you specify a **Retain until date** for it. Amazon S3 protects that object version until the retention period expires.

#### Legal holds
Like a retention period, a legal hold prevents an object version from being overwritten or deleted. However, a legal hold doesn't have an associated retention period and remains in effect until removed. Any user who has the **s3:PutObjectLegalHold** permission can freely place a legal hold.

Legal holds are appropriate for any situation where you are not sure how long you want your objects to stay immutable. For example, you might have an active litigation or an upcoming external audit of your data and you want to keep objects in a WORM state until the audit is complete.

Placing a legal hold on an object version doesn't affect the retention mode or retention period for that object version. If the retention period expires, the object doesn't lose its WORM protection. Rather, the legal hold continues to protect the object until an authorized user explicitly removes it. Similarly, if you remove a legal hold while an object version has a retention period in effect, the object version remains protected until the retention period expires.

#### Configuring Amazon S3 Object Lock
1. Start "Create bucket".
2. Choose Advanced Settings.
3. Object Lock settings.
4. Enable.
5. When you create a bucket with Object Lock enabled, Amazon S3 automatically enables versioning for the bucket.
6. Note that the Bucket Versioning setting has automatically been set to Enabled
7. Choose "Create bucket".
8. Bucket -> Properties tab.
9. Edit Object Lock retention.
10. Choose Enable.
11. Choose Governance mode. With this option set, users with specific IAM permissions - **s3:BypassGovernanceRetention** - can overwrite or delete protected object versions during the retention period.
12. Enter a retention period.
13. Save changes.

#### Managing S3 Object Lock at scale with Amazon S3 Batch Operations 
You can perform S3 Object Lock operations at scale using S3 Batch Operations to apply or change legal holds or retention periods. A single S3 Batch Operations job can perform a specified operation on billions of objects containing exabytes of data. With S3 Batch Operations, you can track progress, send notifications, and store a detailed completion report of all actions.

You can perform S3 Batch Operations on a custom list of objects, or you can use an Amazon S3 inventory report to generate lists of objects. After providing a list of objects, select a retention period or legal hold status. S3 Batch Operations will apply the policy to those objects. For instance, you can extend the retention period by 1 year for millions of objects for which a hold is about to expire. You can use S3 Batch Operations through the console, AWS CLI, AWS SDKs, or REST API.

#### Amazon Macie with Amazon S3
#### Macie
Macie is a fully managed data security and data privacy service. It uses machine learning and pattern matching to help you discover, monitor, and protect your sensitive data in AWS. In this section, you will learn the benefits of deploying Macie to help protect your data.

#### Use cases
Macie automates the discovery of sensitive data, such as personally identifiable information and financial data. It provides you with an inventory of S3 buckets and their access control and encryption settings. Macie gives you detailed dashboards with aggregated information so you can control and monitor Amazon S3 in a single view.

##### Discover sensitive data
You can automate discovery and reporting of sensitive data by creating and running sensitive-data discovery jobs. A sensitive-data discovery job analyzes objects in S3 buckets to determine if they contain sensitive data. If Macie detects sensitive data in an object, it creates a sensitive-data finding for you. The finding provides a detailed report of the sensitive data that Macie found.

You can configure a job to run only once for on-demand analysis and assessment or on a recurring basis for periodic analysis, assessment, and monitoring. You can also choose various options to control the breadth and depth of a job's analysis. Options include the S3 buckets you want to analyze, the sampling depth, and the custom include and exclude criteria derived from properties of S3 objects. With these scheduling and scope options, you can build and maintain a comprehensive view of the data that your organization stores in Amazon S3. You can discover any security or compliance risks for that data.

##### Machine learning
Macie automatically uses machine learning and pattern matching to analyze objects in S3 buckets. These techniques and criteria can detect a large and growing list of sensitive data types for many countries and regions, including the following:
* Multiple types of personally identifiable information
* Personal health information
* Financial data

You can also customize what Macie looks for to reflect your unique scenarios, intellectual property, or proprietary data. Examples include customer account numbers and internal data classifications.

##### Inventory and access control
If you require an inventory of your S3 buckets, Macie automatically evaluates and monitors those buckets for security and access control. Within minutes, Macie can identify and report overly permissive or unencrypted buckets within your organization.

If Macie detects sensitive data or potential issues with the security or privacy of your data, it creates detailed findings for you to review in a dashboard.

The dashboards give you a snapshot of aggregated statistics for your buckets. These include how many of your buckets are publicly accessible or shared with other AWS accounts. You can drill down on each statistic to view the supporting data.

##### AWS CloudTrail integration
Macie integrates with CloudTrail and provides a record of actions taken by a user, a role, or another AWS service. This includes actions from the Macie console and programmatic calls to Macie API operations.

By using the information collected in CloudTrail, you can determine which requests were made to Macie. For each request, you can identify when it was made, the IP address it was made from, who made it, and additional details.

#### Macie integration
Macie can integrate with both **CloudTrail** and **Amazon GuardDuty** to help monitor the permission and security of buckets. **CloudTrail** data about access and permissions is limited to **account-level** and **bucket-level** settings and doesn’t reflect object-level settings. To monitor **object-level events**, AWS recommends that you use the **Amazon S3 protection feature of GuardDuty**. This feature monitors object-level Amazon S3 data events and analyzes them for malicious and suspicious activity.

##### GuardDuty
GuardDuty is a security monitoring service that analyzes and processes certain types of AWS logs. These include CloudTrail data event logs for Amazon S3 and CloudTrail management event logs. It uses threat intelligence feeds, such as lists of malicious IP addresses and domains, and machine learning. It can identify unexpected and potentially unauthorized and malicious activity within your AWS environment.

##### [GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)

#### Streamlining Access to Amazon S3 with VPC Endpoints
##### VPC endpoints overview
A VPC endpoint is a logical entity within a VPC that permits connectivity to AWS services, such as Amazon S3. The VPC endpoint routes requests across the AWS network to Amazon S3, and then routes responses back to the VPC. Because the traffic stays on the AWS network, you can connect to supported AWS services. You don't need an internet gateway, NAT device, virtual private network (VPN) connection, or AWS Direct Connect connection. Traffic between your VPC and the AWS service does not leave the AWS network.

Endpoints are virtual devices that scale horizontally, and are highly available and redundant. They permit communication between your VPC and AWS services without creating availability risks or bandwidth constraints on your network traffic. VPC endpoints use AWS PrivateLink, a technology that you can implement to privately access services by using private IP addresses.

##### VPC endpoint types
There are two types of VPC endpoints: **Gateway endpoints** and **interface endpoints**.

#####  Gateway endpoints
Gateway endpoints support both Amazon S3 and Amazon DynamoDB. Gateway endpoints are specified in your route table. They use the route prefix to direct traffic for Amazon S3 or DynamoDB to a gateway endpoint.

Using a gateway endpoint provides a way to access S3 buckets without your data traversing the internet. Requests stay within the AWS network. This improves security because you do not need to add an internet gateway or NAT instance to access Amazon S3 data. A private subnet does not have a route to the internet.

##### Gateway endpoint benefits
The following are gateway endpoint benefits:
* Reduced data transfer charges from outbound network communication between VPC and services that require public AWS services, such as Amazon S3
* Security in depth using IAM, gateway endpoint policies, and S3 bucket policies 
* Compliance and regulatory adherence because data does not leave the AWS network

##### Interface endpoints
An interface endpoint is an elastic network interface with a private IP address from the IP address range of your subnet. It is an entry point for traffic going to supported AWS services or to a VPC endpoint service.

Interface endpoints permit on-premises networks connected to a VPC to privately access supported AWS services, such as Amazon S3. This reduces the need to operate fleets of proxy servers in your VPC for on-premises applications. With interface endpoints, those on-premises applications can communicate with Amazon S3 using the private IP of an interface endpoint. Doing this reduces the complexity and potential failure points of the proxy server fleets.

##### Interface endpoint benefits
The following are interface endpoint benefits:
* You can reduce data transfer charges from outbound network communication between VPCs and services that require public AWS services.
* Interface endpoints provide security and convenient access control using VPC endpoint policies and VPC security groups.
* Applications in Amazon VPC can securely access PrivateLink endpoints across AWS Regions using inter-Region VPC peering. 
* Interface endpoints streamline on-premises network and firewall configuration for Amazon S3 access. Public IPs or an internet gateway are no longer required.
* Interface endpoints reduce the need to build self-managed proxy servers with private IPs for Amazon S3 access from on-premises applications.

##### Feature comparison: a gateway endpoint and an interface endpoint
* **Security**:
 * **Gateway endpoints**: Uses endpoint policies for security.
 * **Interface endpoint**: Uses endpoint policies and security groups.
* **Amazon network connectivity**:
 * **Gateway endpoints**: Uses Amazon network to connect to Amazon S3.
 * **Interface endpoint**: Uses Amazon network through AWS PrivateLink to connect to AWS services.
* **Access outside of the VPC**:
 * **Gateway endpoints**: Not accessible from outside the VPC.
 * **Interface endpoint**: Can be accessed from on premises and across Regions.
* **IP connectivity**:
 * **Gateway endpoints**: Uses the public IPs of Amazon S3 and modifies the route table.
 * **Interface endpoint**: Uses private IPs and can use public or endpoint-specific DNS names.
* **Cost**:
 * **Gateway endpoints**: No additional charge for using gateway endpoints.
 * **Interface endpoint**: Charges a fee.

#### Gateway endpoints overview
Gateway endpoints work by connecting the specific VPC with the resource (for example, Amazon S3) to which it connects. You then add a route in the route table to include the Destination as the service prefix id, and the Target as the endpoint ID.

After the route is added, any request for Amazon S3 is routed to the endpoint that connects to Amazon S3. If the subnet is associated with the modified route table, the subnet is automatically granted access to the endpoint. The default policy automatically grants access to authenticated principals. Any security group in use must add a specific rule that permits outbound traffic to the endpoint.

##### Default route table
This route table doesn't contain route information for the gateway endpoint. Therefore, no users, applications, or services can route to the VPC endpoint. Requests to Amazon S3 will route over the public internet.

| Destination | Target |
| ----------- | ------ |
| 10.0.0.0/16 | local |
| 0.0.0.0/0 | igw-id |

##### Modified route table
This route table is modified to add the destination as the process-id for Amazon S3 and the target as the VPC-id. It permits principals in the subnet to route directly to Amazon S3. 

| Destination | Target |
| ----------- | ------ |
| 10.0.0.0/16 | local |
| pl-id for Amazon S3 | vpce-id | 

##### [Gateway endpoints for Amazon S3](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html#create-gateway-endpoint-s3)

#### Interface endpoints
An interface endpoint is an elastic network interface with a private IP address from the IP address range of your subnet. You can configure any API and HTTPS requests to Amazon S3 from your VPC and on-premises applications to connect to Amazon S3 securely and privately through PrivateLink.

##### Routing requests from an on-premises application to Amazon S3
###### On-premises applications
The on-premises data center has applications that need access to Amazon S3. The on-premises applications send their requests through Direct Connect to the interface endpoint.

Direct Connect gives your on-premises resources access to services on AWS through your VPC.

###### PrivateLink
PrivateLink connects to services through a private IP address assigned from within the VPC. PrivateLink uses a distributed system of virtual hyperplane nodes at the network level to decide on routing and connection distribution.

###### Interface endpoints for Amazon S3
The interface endpoints forward requests to the S3 bucket using PrivateLink.

Security groups are associated with the endpoint network interface. You can configure the security group rules to restrict access to the endpoint.

When using private DNS and endpoint-specific hostnames, all traffic to the service is directed to the interface endpoint. The traffic doesn't use a default route, such as a NAT gateway or public IP address. Using private DNS keeps the traffic for the service contained securely within the Amazon network.

When you create an interface endpoint, Amazon S3 generates the following two types of endpoint-specific Amazon S3 DNS names:
* A **Regional DNS name** includes a unique VPC endpoint ID, a service identifier, the Region, and **vpce.amazonaws.com** in its name. For example, for VPC endpoint ID **vpce-1a2b3c4d**, the DNS name generated might be similar to **vpce-1a2b3c4d-5e6f.s3.us-east-1.vpce.amazonaws.com**.
* A **Zonal DNS name** includes the Availability Zone—for example, **vpce-1a2b3c4d-5e6f-us-east-1a.s3.us-east-1.vpce.amazonaws.com**. You might use this option if your architecture isolates Availability Zones. For example, you can use it for fault containment or to reduce Regional data transfer costs.

##### Example
The following diagram illustrates routing requests to Amazon S3 using a private DNS endpoint hostname. There are two subnets (subnet 1 and subnet 2) within the VPC. Subnet 1 contains an EC2 instance and subnet 2 contains an EC2 instance and an endpoint network interface. Outside of the VPC, there is an S3 bucket within a Region. In this example, the default DNS name is **DOC-EXAMPLE-BUCKET.us-east-1.amazonaws.com**; the endpoint-specific DNS hostname is **vpce-123.DOC-EXAMPLE-BUCKET.us-east-1.vpce.amazonaws.com**.

1. **Default DNS name**. The default DNS name is a public DNS name. It permits traffic to route out of the AWS network through the internet gateway and into the public internet.
2. **Endpoint hostname**. The private DNS hostname ensures that the traffic stays on the AWS network and is routed to the interface endpoint in subnet 2.
3. **Endpoint network interface**. The endpoint network interface contains security group rules to control traffic flow. All traffic in the VPC for Amazon S3 is routed through the network interfaces and then to Amazon S3.
4. **S3 bucket**. The S3 bucket can be reached through the network interface from internal VPC traffic. Or, it can be reached from the internet using the default DNS name.

#### Securing endpoints
You can secure gateway endpoints in three locations: **on the service (such as an EC2 instance)**, **on the endpoint**, and **on the S3 bucket**. When using endpoint policies, AWS evaluates all the policies and applies the most restrictive set. It is a best practice to manage permissions using the endpoint policy, and then set the S3 bucket to only accept connections from the appropriate access point. Here, AWS applies the more restrictive endpoint policy. You must manage and maintain only the policies for the endpoint.

#### Access control and endpoint policies
An endpoint policy is an IAM resource policy attached to an endpoint. The endpoint policy controls the requests, users, or groups that are allowed access through the endpoint. The following are important details about the endpoint policy:
* The endpoint policy explicitly denies access to any actions not listed in the policy. 
* If you do not attach a policy at endpoint creation, the default policy is attached and allows full access to the AWS service.
* If a service does not support endpoint policies, the endpoint allows full access to the service.
* An endpoint policy does not override or replace IAM user policies or service-specific policies (such as S3 bucket policies). It is a separate policy for controlling access from the endpoint to the specified service.
* You cannot attach more than one policy to an endpoint. However, you can modify the policy at any time. If you do modify a policy, it can take a few minutes for the changes to apply.

Secure access to Amazon S3 through a gateway VPC endpoint. We use a modified route table so the EC2 instance request for Amazon S3 is routed to the endpoint that connects to Amazon S3.
* EC2 Instance - IAM policy
* Gateway endpoint - Resource policy: Gateway endpoint policy
* Amazon S3 - Resource policy: S3 bucket policy.

Like gateway endpoints, you can secure interface endpoints using resource policies on the endpoint itself and the resource the endpoint provides access to. With interface endpoints, you can use security groups to restrict access to the endpoint.

Secure access to Amazon S3 through an interface VPC endpoint. A security group permits the resources, such as EC2 instances, to communicate with the endpoint network interfaces for the VPC endpoint.
* EC2 Instance - IAM policy
* Interface endpoint:
 * Security group configuration
 *  Resource policy: Endpoint policy
* Amazon S3 - Resource policy: S3 bucket policy.

#### Example: Controlling access to buckets from specified VPC endpoints
You can also control access to S3 buckets using S3 bucket policies. You can use a bucket policy to control access to the bucket from only specified VPC endpoints or specific VPCs. It is a best practice to restrict access to only those VPCs or endpoints that require access.

The following is an example of an Amazon S3 bucket policy. It restricts access to a **DOC-EXAMPLE-BUCKET** to only the VPC endpoint with the **vpce-1a2b3c4d** ID. The policy denies all access to the bucket if the specified endpoint is not being used.

```
{
"Version": "2012-10-17",
"Id": "Policy147258369",
"Statement": [{
  "Sid": "Access-to-specific-VPCE-only",
  "Principal": "*",
  "Effect": "Deny",
  "Action": "s3:*",
  "Resource": ["arn:aws:s3:::DOC-EXAMPLE-BUCKET",
               "arn:aws:s3:::DOC-EXAMPLE-BUCKET/*"],
  "Condition": {
    "StringNotEquals": {
      "aws:SourceVpce": "vpce-1a2b3c4d"
    }
  }
}]
}
```

##### Policy element reminder
* **Principal** element indicates which principals are restricted in the policy. Using an asterisk (*) indicates that this policy applies to all principals.
* **Effect** element allows or denies the actions in the policy. This policy denies all actions specified by the Action element.
* **Action** element determines which actions are denied to a bucket. This policy states that all Amazon S3 actions will be denied if the Condition element is not met.
* **Resource** element specifies the resource that you want to allow actions on. Here, the specific resource is the **finance-bucket** and objects and folders within the **finance-bucket**.
* **Condition** element specifics the condition necessary to access the resource. Here, if the request doesn't come specifically from the **SourceVpce** called **vpce-1a2b3c4d**, requests to the **DOC-EXAMPLE-BUCKET** will be denied.

#### Using Encryption to Protect Sensitive Data
Amazon S3 employs server-side encryption to protect data at rest. When you upload an object, it automatically encrypts the object using a unique data-encryption key. You can choose to have Amazon S3 manage the data key on your behalf, or use your own key. 

There are three options for server-side encryption:
* Amazon S3 managed keys
* AWS Key Management Service keys
* customer-provided keys

##### Data keys
Data keys are symmetric keys that you can use to encrypt and decrypt data. This might include large amounts of data or other data encryption keys. 

AWS KMS generates, encrypts, and decrypts data keys. However, AWS KMS does not store, manage, or track your data keys or perform cryptographic operations with data keys. 

When using Amazon S3 with AWS KMS keys, the Amazon S3 service performs the encryption and decryption, and securely manages the data keys on your behalf.

1. When you upload an object to a bucket, Amazon S3 requests a data key from AWS KMS. AWS KMS returns a unique data key in plain text, and a version that is encrypted with a customer managed key.
2. Amazon S3 then uses the data key to encrypt the uploaded object, and removes the key from memory. The encrypted version of the data key is stored in Amazon S3 with the object.
3. When Amazon S3 receives a GET request for the object, it sends the encrypted data key to AWS KMS to decrypt. Then, Amazon S3 uses the plain text data key to decrypt the object before returning it to the requester. The data key is again removed from memory.

AWS KMS APIs can also be used directly by applications to obtain data keys for client-side cryptographic operations.

#### Data in transit
You can protect data in transit by using either HTTPS or client-side encryption. By providing the appropriate level of protection, you protect the confidentiality and integrity of your workload’s data from any third party who might intercept the data while in transit.

##### Ensuring encrypted connections
HTTPS requests use TLS to encrypt data over the connection. To protect data in transit, use an S3 bucket policy to enforce the use of HTTPS requests. Doing this ensures the integrity of the data and denies any request that comes in over standard HTTP. To enforce the use of HTTPS on buckets, use the **aws:SecureTransport** condition in your S3 bucket policies.

#### Server-side encryption 
Amazon S3 encrypts an object before saving it to disk and decrypts it when you download it. If you authenticate and have access permissions, there is no difference in how you access encrypted or unencrypted objects.

For example, when you share an object using a presigned URL, that presigned URL works the same for both encrypted and unencrypted objects. Additionally, when you list objects in your bucket, the list API returns a list of all objects, regardless of their encryption.

#### Server-side encryption options
##### Server-side encryption with Amazon S3 managed keys (SSE-S3)
Amazon S3 applies SSE-S3 as the base level of encryption for every bucket in Amazon S3. It encrypts each object with a unique key, which it then encrypts with a root key that it regularly rotates. SSE-S3 uses one of the strongest block ciphers available, 256-bit Advanced Encryption Standard (AES-256), to encrypt your data.

You do not incur charges when using SSE-S3.

##### Server-side encryption with AWS KMS keys (SSE-KMS)
A KMS key includes metadata, such as the key ID, creation date, description, and key state. The KMS key also contains the key material used to encrypt and decrypt data. You can choose a customer managed key that you create and manage. Or, you can choose an AWS managed key that Amazon S3 creates in your AWS account and manages for you. Like a customer managed key, your AWS managed key is unique to your AWS account and Region. Only Amazon S3 has permission to use this key on your behalf.  

The following are benefits of using SSE-KMS:
* You manage the rotation of customer managed keys.
* It is more convenient to manage a few primary keys instead of billions of data keys.
* You gain centralized access and auditing.
* SSE-KMS performs better for large datasets.

You incur a charge when you use SSE-KMS, and you are subject to request limits. To reduce the cost of SSE-KMS, use Amazon S3 Bucket Keys. This bucket-level key for SSE can reduce AWS KMS request costs by up to 99 percent. It does this by decreasing the request traffic from Amazon S3 to AWS KMS.

##### Dual-layer server-side encryption with KMS keys (DSSE-KMS)
DSSE-KMS is similar to SSE-KMS, but DSSE-KMS applies two individual layers of object-level encryption instead of one layer. Both layers of encryption are applied to an object on the server side. So you can use many AWS services and tools to analyze data in Amazon S3 along with an encryption method that can satisfy compliance requirements.

When you use DSSE-KMS with an S3 bucket, the KMS keys must be in the same Region as the bucket. Also, when DSSE-KMS is requested for the object, the Amazon S3 checksum that's part of the object's metadata is stored in encrypted form. There are additional charges for using DSSE-KMS and AWS KMS keys.

S3 Bucket Keys aren't supported for DSSE-KMS.

##### Server-side encryption with customer-provided keys (SSE-C)
With SSE-C, you manage the encryption keys. Amazon S3 manages the encryption, as it writes to disks, and decryption, when you access your objects. With this option, you are responsible for managing and rotating the keys. Amazon S3 data can be decrypted only with these keys. This means that if you lose your keys, even AWS Support cannot help you gain access to your data.

**You can apply only one type of server-side encryption to the same object simultaneously.**

##### [SSE-S3 additional information](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingServerSideEncryption.html)

##### [Customer managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk)

##### [S3 Bucket Keys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-key.html)

##### [DSSE-KMS additional information](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingDSSEncryption.html)

##### [SSE-C additional information](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerSideEncryptionCustomerKeys.html)

#### S3 Bucket Keys for SSE-KMS
Workloads that access millions or billions of objects encrypted with SSE-KMS can generate large volumes of requests to AWS KMS. When you configure your bucket to use an S3 Bucket Key for SSE-KMS, AWS KMS generates a bucket-level key. This is used to create unique data keys for new objects that you add to the bucket. The S3 Bucket Key is used for a time-limited period within Amazon S3. This reduces the need for Amazon S3 to make requests to AWS KMS for encryption operations and reduces traffic from Amazon S3 to AWS KMS. You can access AWS KMS encrypted objects in Amazon S3 at a fraction of the previous cost.

When you configure an S3 Bucket Key, objects that are already in the bucket do not use the S3 Bucket Key. To configure an S3 Bucket Key for existing objects, use a **COPY** operation. Amazon S3 shares an S3 Bucket Key only for objects encrypted by the same KMS key.

##### [Configuring an S3 Bucket Key](https://docs.aws.amazon.com/AmazonS3/latest/userguide/configuring-bucket-key-object.html)

#### Using Amazon S3 default encryption
Amazon S3 applies SSE-S3 as the base level of encryption for every bucket in Amazon S3. However, you can change this by configuring default encryption for a bucket. Implementing default encryption on your buckets is a streamlined process. After setup, no maintenance time is required. Your chosen method encrypts new objects added to your buckets automatically, helping you meet compliance requirements. You can choose SSE-S3 or SSE-KMS. If you have existing objects in your bucket and you set the default encryption, the setting does not retroactively encrypt existing objects.

If you are using a custom KMS key, you must grant users access to use the key. Otherwise, they will not be able to decrypt the objects. In addition, the default encryption on the bucket applies to all objects unless the object PUT request header contains a different encryption method. The header can specify an encryption method other than the default encryption. It then uses the encryption method specified in the header when the object is written to the bucket. 

You can track default encryption configuration requests for Amazon S3 buckets by doing one of the following:
* Using AWS CloudTrail events
* Creating Amazon CloudWatch Events with S3 bucket-level operations as the event type

#### Knowledge Check
##### Which groups does Amazon S3 grant permissions to its members to consider a bucket or an object public? (Select TWO.)
* AuthenticatedUsers 
* AllUsers

Wrong answers:
* All-Identity 
* AllPrincipals
* Everyone

Amazon S3 considers a bucket or object public if it grants any permissions to the members of the following groups: 
* **AuthenticatedUsers**: This group allows all AWS accounts to access the resource. This means that any authenticated AWS user, from any AWS account in the world, can access a resource if the request is signed (authenticated).
* **AllUsers**: This group allows anyone in the world access to the resource. The requests can be signed (authenticated) or unsigned (anonymous).

##### Which endpoint service uses only endpoint policies to secure the endpoint? 
* Gateway endpoints

Wrong answers:
* Interface endpoints
* Access endpoints
* Security group endpoints

Gateway endpoints use only endpoint policies for security. Interface endpoints use both endpoint policies and security groups for security.

##### An endpoint policy can provide access to an Amazon S3 bucket. What should the S3 bucket policy specify to enforce that requests only originate from the virtual private cloud (VPC) endpoint?
* The bucket policy should include a condition to only accept connections from the appropriate endpoint.

Wrong answers:
* The bucket policy should be identical to the endpoint policy.
* The bucket policy should specify only the administrator who manages the bucket permissions as the principal.
* No bucket policy should be on the bucket.

A best practice is to manage permissions using the endpoint policy and then set the S3 bucket to only accept connections from the appropriate access point. Here, AWS applies the more restrictive endpoint policy. Users must manage and maintain only the policies for the endpoint.

An endpoint policy does not override or replace AWS Identity and Access Management (IAM) user policies or service-specific policies, such as S3 bucket policies. It is a separate policy for controlling access from the endpoint to the specified service.

#### Assessment
##### A developer is configuring a database server on Amazon EC2 that requires a storage solution capable of providing low-latency and high-IOPS performance. Durability and data consistency are also important factors. Which AWS Cloud storage service would be most suitable for this scenario?
* **Amazon EBS** provides block-level storage volumes that can be directly attached to Amazon EC2 instances. EBS volumes offer low-latency access, high-IOPS performance, durability, and data consistency. This makes it an optimal choice for hosting a database server.

The other options are incorrect because of the following:
* Amazon S3 is an object storage service designed for storing and retrieving a large amount of unstructured data. Although it offers high durability and scalability, it does not provide the low-latency access and high-IOPS performance required for a database server.
* Amazon EFS is a fully manage file storage service that provides scalable and highly available file storage. However, it might not offer the desired low-latency access and high-IOPS performance required for a database server.
* Amazon S3 Glacier Deep Archive is designed for data archiving and backup purposes. It does not provide the low latency and high IOPS performance required.

##### A developer wants a long-term storage solution to support data backup operations. The backups contain historical data that cannot be re-created and must be retained for compliance purposes. They are infrequently accessed, but when needed they must be retrieved within 48 hours. Which Amazon $3 storage class is the most cost-effective option that meets the requirements?
* S3 Glacier Deep Archive delivers low-cost storage for archive data that is accessed less than one
time per year and is retrieved asynchronously. Its default retrieval time is 12 hours. 

The other options are incorrect because of the following:
* The S3 Glacier Flexible Retrieval storage class is ideal for workloads that require the flexibility to retrieve the data in minutes or up to 5-12 hours.
* The S3 One Zone-IA is a good choice for storing secondary backup copies of on-premises data or easily re-creatable data, and it is not suitable for the scenario. 
* S3 Standard-IA is for data that is accessed less frequently but requires rapid access when needed. Although it can be used for backups, it is not the most cost-effective solution.

##### A user is trying to upload an object that is 1 TB in size to an Amazon S3 bucket. What method could they use?
* For an object that is 1 TB in size, users can use AWS CLI, AWS SDKS, or REST API with multipart upload APl operation to upload a single large object, up to 5 TB in size.

##### What can Amazon S3 storage class analysis help a developer determine about their data?
* Amazon S3 analytics storage class analysis observes data access patterns over a period of time. After storage class analysis observes the infrequent access patterns of a filtered set of data, users can use the analysis results to help them improve their lifecycle configurations.

##### An application frequently uploads large objects to Amazon S3 using multipart upload. Which action will minimize storage costs for incomplete multipart uploads?
* Using lifecycle policies, the **AbortIncompleteMultipartUpload** element can set a maximum number of days for a multipart upload to remain in progress. If the upload does not complete within that specified number of days, it becomes eligible for a cancel operation. Amazon S3 stops the multipart upload and deletes the parts associated with the multipart upload.

##### A developer is working on a serverless application that requires dynamically transforming data stored in Amazon S3 before it is returned to the user. Which AWS offering can they use to achieve this functionality?
* S3 Object Lambda is a resource that allows adding custom code functions to Amazon S3 GET requests. Developers can use it to dynamically modify or transform data retrieved from Amazon S3 before the data is returned to the user. 

The other options are incorrect because of the following:
* DynamoDB is a fully managed NoSQL database service, and it does not provide the functionality to dynamically transform data stored in Amazon S3.
* EventBridge is an asynchronous solution for responding to events. It cannot transform and return the data to the user.
* CloudWatch is a monitoring solution.

##### A company offers a website that allows users to securely store and download private files. The web server is running very slow because of an overwhelming number of download requests. A developer must find a most effective solution to reduce the web server load and cost, and it must allow users to download only their own files. Which solution meets all these requirements?
* Presigned URLs can be used to share access to S3 buckets. When a developer creates a presigned URL, they associate it with a specific action and an expiration date. Anyone who has access to the URL can perform the action embedded in the URL, as if they were the original signing user.

The other responses are incorrect because of the following:
* Storing files on an Amazon EBS volume and using other instances to serve the content is possible. But it is a much higher-cost solution, and the company cannot limit users to only accessing their content.
* An instance store is temporary storage and it does not address any of the concerns mentioned in this question.
* The use of a CloudFront cache alone would not allow users to download only their own files.

##### A developer wants to apply tags to their Amazon S3 resources. Which Amazon S3 resources can tags be applied to?
* Tags can be applied to S3 buckets and objects.

##### A data analyst is working with a large dataset stored in Amazon S3. They need to retrieve specific data from the dataset without downloading the entire file. Which AWS offering can they use to efficiently query and retrieve only the required data?
* S3 Select makes it possible to run SQL-like queries on data stored in Amazon S3 and retrieve only the specific data, without the need to download the entire file. It improves query performance and reduces data transfer costs by filtering and retrieving only relevant portions of the data. 

The other options are incorrect because of the following:
* Athena is an interactive query service that can be used to analyze data directly in Amazon S3 with standard SQL queries. However, S3 Select is a more specific and efficient service for retrieving only the required data.
* Amazon Redshift is a fully managed data warehousing service that is optimized for online analytic process workloads. Although Amazon Redshift can efficiently handle large-scale data analytics, it is not service specifically designed for querying and retrieving specific data from objects stored in
Amazon S3.
* Amazon EMR is a managed big data processing service. Although Amazon EMR can process large datasets and perform complex data transformations, it is not the most efficient choice for retrieving specific data from objects stored in Amazon S3.

##### A digital media company uses Amazon S3 to manage a collection of images, videos, and audio files. They have content from various clients and need to keep track of usage rights, copyright information, and the content's expiration dates to ensure compliance with licensing agreements. What is the best way for them to organize and manage the content?
* Object tagging to assign custom metadata is the most effective way to organize the Content for the media company.

##### A user wants to bypass governance mode retention settings to delete an object in an Amazon S3 bucket using the AWS CLI. What are the requirements for deleting the object? (Select TWO.)
* To bypass governance mode retention settings to delete an object using the AWS CLI, a user must meet the following requirements:
 * The user account must have the **s3:BypassGovernanceRetention** lAM permission.
 * The user must explicitly include **x-amz-bypass-governance-retention:true** as a request header.

##### Which levels can an Amazon S3 Object Lock be applied at?
* S3 Object Lock must be enabled for a bucket. But the lock operation happens at the object and object version level.

##### How does the Amazon S3 Object Ownership feature control ownership of objects?
* Using Amazon S3 Object Ownership, the bucket owner has full control of the objects and can automatically own any new objects written by other accounts.

##### A developer works for a financial company that stores sensitive customer data in Amazon S3. Which AWS service will discover and classify the data to help with compliance and data protection requirements?
* Macie uses machine learning to automatically discover, classify, and protect sensitive data stored in Amazon S3. Macie can identify personally identifiable information (Pll), financial data, intellectual property, and other sensitive content.

The other options are incorrect because of the following:
* GuardDuty is a threat detection service that helps identify malicious activity and unauthorized access in AWS accounts and workloads.
* Amazon Rekognition is an artificial intelligence (Al) service that provides images and video analysis capabilities.
* Athena is an interactive query service that analyzes data directly in Amazon S3 with standard SQL queries.

##### A developer has been tasked with making sure that all new objects in an Amazon S3 bucket are encrypted at rest, regardless of the options specified when the object is uploaded. How can they achieve this?
* The correct option is to use default encryption for the bucket with at least the SSE-S3 option. Amazon S3 now applies server-side encryption with Amazon S3 managed keys (SSE-S3) as the base level of encryption for every bucket in Amazon S3. All new object uploads to Amazon S3 are automatically encrypted at no additional cost and with no impact on performance. The other options are incorrect because server-side encryption is already performed by default.

### Week 6: Storage 2 Part 2
#### Amazon S3 Storage Lens
S3 Storage Lens provides metrics pre-aggregated by up to six levels: 
* AWS Organization - optional, the highest level
* account
* Region
* storage class
* bucket
* prefix - the most granular level

#### S3 Storage Lens benefits
* It provides a single view of object storage usage and activity across hundreds of accounts in your organization. This includes drill-downs to the account, bucket, or prefix level.
* It produces actionable recommendations to help improve cost efficiency and apply data protection best practices.
* There is no performance impact from using S3 Storage Lens.

#### S3 Storage Lens overview
##### S3 Storage Lens
S3 Storage Lens provides organization-wide visibility into Amazon S3 usage, activity trends, and recommendations.

##### Configure
You can configure the scope of the dashboard and select metrics tiers. S3 Storage Lens provides metrics pre-aggregated by up to six levels, such as AWS Organization, accounts, Regions, and buckets.

##### Aggregate
S3 Storage Lens aggregates metrics daily by scanning internal Amazon S3 data.

##### Analyze
Analyze your metrics in the interactive dashboard with filters, drill-downs, trends, and contextual recommendations.

##### Optimize
Optimize your storage using insights and flagging outliers. Implement recommendations such as data protection and cost efficiency discovered in S3 Storage Lens.

#### Permissions
S3 Storage Lens requires specific permissions in AWS Identity and Access Management (IAM) to authorize access to S3 Storage Lens actions. You must attach the IAM policy to IAM users, groups, or roles. You can grant them permissions to activate or deactivate S3 Storage Lens or access a dashboard or configuration. You cannot use your account's root user credentials to view S3 Storage Lens dashboards. To access those, you must grant the requisite IAM permissions to a new or existing IAM user and then log in with those user credentials.

##### [S3 Storage Lens and AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-s3lens.html)

##### [S3 Storage Lens IAM permissions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_iam_permissions.html#storage_lens_iam_permissions_account)

#### S3 Storage Lens terms
##### Default dashboard
The S3 Storage Lens default dashboard on the console is named **default-account-dashboard**. Amazon S3 pre-configures the default account dashboard to visualize the summarized insights and trends of your entire account’s aggregated storage usage and activity metrics. It updates these metrics daily in the Amazon S3 console.

The following are some important notes:
* You can create up to 50 dashboards per Region.
* Deactivated dashboards do not update.
* If you delete a dashboard, all configurations and historical data for that one dashboard are removed.
* Organization-level dashboards are limited to a Regional scope.

##### Custom dashboards
You create and modify S3 Storage Lens dashboards to show all, or a portion of, your account’s storage.

You filter by Region, bucket, and prefix (available only with advanced metrics and recommendations). When you no longer need the dashboard, deactivate or delete it.

##### Metrics
S3 Storage Lens offers the following two types of storage metrics:
* **Usage metrics** are free and provide information about the size, quantity, and characteristics of your storage. Free metrics are retained for a **14-day** period.
* **Activity metrics** are available for a fee, and require that you activate advanced metrics and recommendations metrics. Activity metrics detail how often your storage is requested. This includes the number of requests by type, upload and download bytes, and errors. Activity metrics have a **15-month** data retention policy.

##### Recommendations
Recommendations provide automated suggestions to help optimize your storage. They are placed contextually alongside relevant metrics in the dashboard. Recommendations only appear when they are relevant. Historical data is not eligible for recommendations because recommendations are relevant to only what is happening in the most recent period.

##### Call-outs
Call-outs are recommendations that alert you to interesting anomalies within your storage usage and activity over a period that might need further attention or monitoring. Call-outs do not necessarily indicate an issue. They might represent planned or anticipated activity in your storage.

Call-outs are available when **advanced metrics** are activated (there is a fee for advanced metrics).

For example, you might see an outlier in your dashboard for upload bytes on a certain day. You can compare this to your historical trends to determine if this is a one-off occurrence. For example, if a group had to upload a significant amount of data as a planned task. It could also be a reoccurring event, such as end-of-month reporting or inventory.

##### Reminders
Reminders provide insight into how Amazon S3 works and can help you learn more ways to use Amazon S3 features to reduce storage costs.

Reminders are available when advanced metrics are activated (there is a fee for advanced metrics).

#### Metrics cost tiers
##### Free metrics
Free metrics contain metrics that are relevant to your storage usage, such as the number of buckets and the objects in your account. There are also use-case based metrics, such as cost-optimization and data-protection metrics. All free metrics are collected daily, and data is available for queries for 14 days.

##### Advanced metrics
Advanced metrics include all the metrics in free metrics, along with additional metrics. These include advanced data-protection and cost-optimization metrics. There are also additional metric categories, such as activity metrics and detailed status-code metrics. Advanced metrics data is available for queries for 15 months.

**There are additional charges when you use S3 Storage Lens with advanced metrics and recommendations.**

##### [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/)

##### [Metric selection](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_basics_metrics_recommendations.html#storage_lens_basics_metrics_selection)

#### Amazon S3 Storage Lens metrics use cases
You can use your S3 Storage Lens dashboard to visualize insights and trends, flag outliers, and receive recommendations. S3 Storage Lens metrics are organized into categories that align with key use cases. 

##### Identify cost-optimization opportunities
With cost-optimization metrics, you can identify opportunities to reduce your Amazon S3 storage costs. You can identify buckets with incomplete multipart uploads that are more than 7-days old or buckets that are accumulating non-current versions.

##### Apply data-protection best practices
You can use data-protection metrics to identify buckets that aren't following data-protection best practices within your organization. For example, you can identify buckets that don’t use AWS KMS keys for default encryption or don't have S3 Versioning enabled.

##### Apply access-management best practices 
With S3 Storage Lens access-management metrics, you can identify bucket settings for S3 Object Ownership. You can then migrate access control list (ACL) permissions to bucket policies and deactivate ACLs.

##### Improve the performance of application workloads
If you have S3 Storage Lens advanced metrics activated, you can use detailed status-code metrics to get counts for successful or failed requests. You can then use this to troubleshoot access or performance issues.

#### Metrics categories
Free metrics include summary, cost-optimization, data-protection, access-management, performance, and event metrics. When you upgrade to advanced metrics and recommendations, you can activate additional cost-optimization and data-protection metrics. You can use these to further reduce your Amazon S3 storage costs and improve your data-protection stance. You can also activate activity metrics and detailed status-code metrics to improve the performance of application workflows.

##### Summary metrics
Summary metrics provide general insights about your Amazon S3 storage, including your total storage bytes and object count.

##### Cost-optimization metrics
Cost-optimization metrics provide insights that you can use to manage and optimize your storage costs. For example, you can identify buckets that have incomplete multipart uploads that are more than 7 days old.

With advanced metrics and recommendations, you can activate advanced cost-optimization metrics. These metrics include S3 Lifecycle rule count metrics that you can use to get per-bucket expiration and transition S3 Lifecycle rule counts.

##### Data-protection metrics
Data-protection metrics provide insights for data-protection features, such as encryption and S3 Versioning. You can use these metrics to identify buckets that are not following data-protection best practices. For example, you can identify buckets that are not using default encryption with KMS keys or S3 Versioning.

With advanced metrics and recommendations, you can activate advanced data-protection metrics. These metrics include per-bucket replication rule count metrics.

##### Access-management metrics
Access-management metrics provide insights for S3 Object Ownership. You can use these metrics to see which S3 Object Ownership settings your buckets use.

##### Event metrics
Event metrics provide insights for Amazon S3 event notifications. With event metrics, you can see which buckets have event notifications configured.

##### Performance metrics
Performance metrics provide insights for S3 Transfer Acceleration. With performance metrics, you can see which buckets have Transfer Acceleration activated.

##### Activity metrics (advanced)
If you upgrade your dashboard to advanced metrics and recommendations, you can activate activity metrics. Activity metrics provide details about how your storage is requested (for example, All requests, Get requests, Put requests), bytes uploaded or downloaded, and errors.

##### Detailed status-code metrics (advanced)
If you upgrade your dashboard to advanced metrics and recommendations, you can activate detailed status-code metrics. These provide insights for HTTP status codes, such as 403 Forbidden and 503 Service Unavailable. You can use these to troubleshoot access or performance issues. For example, you can review the 403 Forbidden error count metric to identify workloads that are accessing buckets without the correct permissions applied.

#### Recommendations
S3 Storage Lens provides automated recommendations to help you optimize your storage. Recommendations are placed contextually alongside relevant metrics in the S3 Storage Lens dashboard. Historical data is not eligible for recommendations because recommendations are relevant to what is happening in the most recent period. Recommendations appear only when they are relevant.

##### Suggestions
Suggestions alert you to trends within your storage usage and activity that might indicate a storage-cost optimization opportunity or a data-protection best practice. You can use the suggested topics in the Amazon S3 User Guide and the S3 Storage Lens dashboard. Review these for more details about specific Regions, buckets, or prefixes to further assist you.

##### Call-outs
Call-outs are recommendations that alert you to interesting anomalies within your storage usage and activity over a period that might need further attention or monitoring. The following are call-out types:
* **Outlier call-outs** – S3 Storage Lens provides call-outs for metrics that are outliers, based on your recent 30-day trend. The outlier is calculated by using a standard score, called a z-score. In this score, the current day's metric is subtracted from the average of the last 30 days for that metric. It is then divided by the standard deviation for that metric over the last 30 days. The resulting score is usually between -3 and +3. This number represents the number of standard deviations that the current day's metric is from the mean. S3 Storage Lens considers metrics with a score more than 2 or less than -2 to be outliers. This is because they are higher or lower than 95 percent of normally distributed data.
* **Significant change call-outs** – The significant change call-out applies to metrics that are expected to change less frequently. Therefore, it is set to a higher sensitivity than the outlier calculation. It is typically plus or minus 20 percent compared to the prior day, week, or month.
 * **Addressing call-outs in your storage usage and activity** – If you receive a significant change call-out, it’s not necessarily a problem. It might be the result of an anticipated change in your storage. For example, you might have recently added a large number of new objects, deleted a large number of objects, or made similar planned changes. If you see a significant change call-out on your dashboard, review it and determine whether it can be explained by recent circumstances. If not, use the S3 Storage Lens dashboard to drill down for more details. This can help you understand the specific Regions, buckets, or prefixes that are driving the fluctuation.

##### Reminders
Reminders provide insights into how Amazon S3 works. They can help you learn more about ways to use Amazon S3 features to reduce storage costs or apply data-protection best practices.

#### Using Amazon S3 Storage Lens with AWS Organizations
S3 Storage Lens collects metrics and usage data for all AWS accounts that are part of your AWS Organizations hierarchy. You must activate S3 Storage Lens trusted access using your AWS Organizations management. By activating trusted access, you permit S3 Storage Lens to access your Organizations hierarchy, membership, and structure through the Organizations APIs. S3 Storage Lens will be a trusted service for your entire organization’s structure. You can then add delegated administrator access to accounts in your organization. These accounts can then create organization-wide dashboards and configurations for S3 Storage Lens.

##### Granularity of view
Data is pre-aggregated at the account, Region, storage class, and bucket levels. You can easily drill down from top-level insights to more granular details.

##### Percent change comparison
You can compare the changes by day, week, or month to help determine trends.

##### Trends and distributions
You can use S3 Storage Lens to gather quick summary insights that give you holistic visibility into your storage at an organization-wide view.

##### Top N overview
In the bottom section of the dashboard, you can perform a top N analysis of a metric over a date range, where N is 1–25.

#### Knowledge Check
##### Amazon S3 Storage Lens provides organization-wide visibility into object storage usage and activity trends. S3 Storage Lens provides metrics pre-aggregated by up to six levels. What is the highest level of these metrics? 
* AWS Organization

##### How many dashboards can a developer create in each home AWS Region by using Amazon S3 Storage Lens?
* 50

##### Amazon S3 Storage Lens metrics are organized into categories that align with key use cases. Which metrics can only be activated in the advanced metrics? (Select TWO.)
* Activity metrics
* Detailed status-code metrics 

#### Summary
##### S3 Storage Lens
S3 Storage Lens aggregates your usage and activity metrics and displays the information in an interactive dashboard on the Amazon S3 console. You can also view this information through a metrics data export in CSV or Parquet format. You use the dashboard to visualize insights and trends and flag outliers. The dashboard provides recommendations for optimizing storage costs and applying data protection best practices.

##### Metrics cost tiers
The S3 Storage Lens metrics glossary provides a complete list of free and advanced metrics for S3 Storage Lens. The following are the two tiers of metrics:
* **Free metrics** contain metrics that are relevant to your storage usage. These include the number of buckets and the objects in your account and use-case based metrics, such as cost-optimization and data-protection metrics.
* **Advanced metrics** include all the metrics in free metrics along with additional metrics, such as advanced data-protection and cost-optimization metrics. There are also additional metric categories, such as activity metrics and detailed status-code metrics. 

##### S3 Storage Lens metrics use cases 
S3 Storage Lens metrics are organized into the following categories that align with key use cases:
* **Identify cost-optimization opportunities**: With cost-optimization metrics, you can identify opportunities to reduce your Amazon S3 storage costs.
* **Apply data-protection best practices**: You can use data-protection metrics to identify buckets that aren't following data-protection best practices within your organization.
* **Apply access-management best practices**: With S3 Storage Lens access-management metrics, you can identify bucket settings for Object Ownership. You can then migrate ACL permissions to bucket policies and deactivate ACLs.
* **Improve the performance of application workloads**: If you have S3 Storage Lens advanced metrics activated, you can use detailed status-code metrics to get counts for successful or failed requests. You can then use these to troubleshoot access or performance issues.

##### Metrics categories
Free metrics include summary, cost-optimization, data-protection, access-management, performance, and event metrics. When you upgrade to advanced metrics and recommendations, you can activate additional cost-optimization and data-protection metrics. You can use these to further reduce your Amazon S3 storage costs and improve your data-protection stance. You can also activate activity metrics and detailed status-code metrics that you can use to improve the performance of application workflows. Both activity metrics and detailed status-code metrics are only available in the advanced metrics and recommendations.

##### Recommendations
Recommendations are grouped into the following three categories:
* Suggestions
* Call-outs
* Reminders

##### S3 Storage Lens and Organizations

S3 Storage Lens works with Organizations to provide a single view of object storage usage and activity across your Amazon S3 storage. This offers the following benefits:
* **Trusted access**: To use your organization's management account, you must activate trusted access for S3 Storage Lens. You can then aggregate storage metrics and usage data for all member accounts in your organization.
* **Delegated administrator**: You can create dashboards and metrics for S3 Storage Lens for your organization by using your Organizations management account. You can also give delegated administrator access to other accounts in your organization.

#### Amazon S3 Reliability, Availability, and Performance

#### Pre-assessment
##### What is the result of trying to retrieve an object whose current version is a delete marker? 
* Amazon S3 will return a 404 Not Found error.

##### For disaster recovery architecture, a company wants to use the Amazon S3 Standard storage class for their frequently accessed objects. They want to use S3 Glacier Flexible Retrieval for their replicas. What is the most efficient way to achieve this?
* Select S3 Glacier Flexible Retrieval as the destination storage class on the replication rule.

##### Which destination can Amazon S3 send event notification message to?
* Amazon Simple Notification Service (Amazon SNS) topics

#### Amazon S3 Event Notifications
You can configure event notifications to send messages in response to certain events that happen in your bucket. You can also use event notifications to invoke custom code in Lambda functions. Event-based notification offers several advantages.

##### New functionality
Notifications help you focus on applications by attaching new functionality driven by events. There is no need to manage fleets of Amazon Elastic Compute Cloud (Amazon EC2) instances to poll for changes.

##### Speed
You need to speed up the processing of new objects when they arrive in your bucket. On average, Amazon S3 sends notifications in less than 1 second.

##### Integration
Event notifications can connect storage in Amazon S3 with workflows. You can architect an application where changes in your data invoke blocks of code or workflows. 

#### Supported event types
Currently, Amazon S3 can publish notifications for the following events. 

##### New object created events
Amazon S3 API actions, such as PUT, POST, and COPY, can create an object. Using these event types, you can get notifications when an object is created using a specific action (for example, **s3:ObjectCreated:Put** action event type). Or, you can use the **s3:ObjectCreated:*-** event type to request notification regardless of the action that created an object. You do not receive event notifications from failed operations.

The following are supported event types:
* s3:ObjectCreated:*
* s3:ObjectCreated:Put
* s3:ObjectCreated:Post
* s3:ObjectCreated:Copy
* s3:ObjectCreated:CompleteMultipartUpload

##### Object removal events
Amazon S3 supports deleting versioned and unversioned objects.

By using the **ObjectRemoved** event types, you can get a notification when an object or a batch of objects is removed from a bucket.

You can request a notification when an object is deleted or a versioned object is permanently deleted by using the **s3:ObjectRemoved:Delete** event type. By using the **s3:ObjectRemoved:DeleteMarkerCreated** event type, you can also request notification when a delete marker is created for a versioned object. You can also use the wildcard **s3:ObjectRemoved:*-** event type to request notification whenever an object is deleted. You do not receive event notifications from automatic deletes from lifecycle policies or from failed operations.

The following are supported event types:
* s3:ObjectRemoved:*
* s3:ObjectRemoved:Delete
* s3:ObjectRemoved:DeleteMarkerCreated

##### Restore object events
Amazon S3 supports restoring objects archived to the S3 Glacier storage classes. Use the **s3:ObjectRestore:Post** event type to request notification of object restoration initiation. Use the **s3:ObjectRestore:Completed** event type to request notification of restoration completion.

The following are supported event types:
* s3:ObjectRestore:Post
* s3:ObjectRestore:Completed

##### Replication events
Amazon S3 sends replication event notifications in the following situation:
* When an object fails replication
* When an object exceeds the 15-minute threshold
* When an object is replicated after the 15-minute threshold
* When an object is no longer tracked by replication metrics 

It also publishes a second event when that object replicates to the destination AWS Region.

The following are supported event types:
* s3:Replication:OperationFailedReplication
* s3:Replication:OperationMissedThreshold
* s3:Replication:OperationReplicatedAfterThreshold
* s3:Replication:OperationNotTracked

#### Supported destinations
##### Events
To receive only the event notifications you want and not for the whole bucket, filter the event notification on prefixes or suffixes of your objects.

For example, you can choose to receive notifications on object names that start with **images/**.

##### Amazon Simple Notification Service (Amazon SNS)
Using Amazon SNS, you can push messages to mobile devices or distributed services. You can publish a message once and deliver it one or more times. Currently, only Standard SNS is supported as a destination; First-In-First-Out is not supported. 

##### Amazon Simple Queue Service (Amazon SQS)
In your notification configuration, you can request that Amazon S3 publish events to an SQS queue. Currently, only Standard SQS queues are supported as a destination; First-In-First-Out SQS queues are not supported, but can be configured as an Amazon EventBridge target.

##### Lambda
Lambda can run custom code in response to S3 bucket events. You upload your custom code to Lambda and create a Lambda function. When Amazon S3 detects an event of the specified type, it publishes the event to Lambda, which runs your function.

For example, you can automate the processing of raw images uploaded to your bucket by invoking a Lambda function each time a new image is uploaded.

##### EventBridge
EventBridge is a serverless event bus that receives events from AWS services. You can set up rules to match events and deliver them to targets, such as an AWS service or an HTTP endpoint.

Unlike other destinations, you can either activate or deactivate events to be delivered to EventBridge for a bucket. If you activate delivery, all events are sent to EventBridge. Additionally, you can use EventBridge rules to route events to additional targets.

#### Granting permissions
Before Amazon S3 can publish messages to a destination, you must grant the Amazon S3 principal the necessary permissions. It needs these permissions to call the relevant API to publish messages to an SNS topic, an SQS queue, or a Lambda function.

You can use the Amazon S3 console to configure event notifications on an S3 bucket for a Lambda function. The console automatically sets up the necessary permissions to invoke the function from the bucket. For permissions to publish messages to an SNS topic or SQS queue, you must attach an AWS Identity and Access Management (IAM) policy to the destination topic or queue.

The following is an example of an IAM policy that you attach to the destination SNS topic:

```
{
 "Version": "2012-10-17",
 "Id": "example-ID",
 "Statement": [
  {
   "Sid": "example-statement-ID",
   "Effect": "Allow",
   "Principal": {
     "Service": "s3.amazonaws.com"  
   },
   "Action": [
    "SNS:Publish"
   ],
   "Resource": "arn:aws:sns:us-east-2:123456789012:MyTopic",
   "Condition": {
      "ArnLike": { "aws:SourceArn": "arn:aws:s3:::DOC-EXAMPLE-BUCKET" },
      "StringEquals": { "aws:SourceAccount": "111122223333" }
   }
  }
 ]
}
```

##### [Amazon S3 event notifications](https://docs.aws.amazon.com/AmazonS3/latest/userguide/EventNotifications.html#grant-destinations-permissions-to-s3)

#### Demo: Enabling and configuring S3 event notifications
In this demonstration, you learn how to configure Amazon S3 event notifications on an inventory report in your S3 bucket. This demo includes instructions for configuring an Amazon SNS topic and an Amazon SNS subscription, configuring Amazon S3 inventory reports, and enabling event notifications for your S3 bucket.

To begin, sign in to the AWS Management Console using credentials with administrator rights. Navigate to the Services menu, and choose S3 to open the S3 console.

Locate the bucket called customer-photos-123. This pre-created bucket holds a variety of sample images, and you can use it to run the inventory report. Next, you configure an SNS event topic. In the AWS Management console, navigate to the Services menu, and choose Simple Notification Service to sign in to the Amazon SNS console.

In the left navigation pane, select the icon with three horizontal lines, and choose Topics. On the Topics page, choose Create topic. The topic defaults to First-in, First-out. But for this demo, choose Standard. In the Name field, enter the name Inventory-report-available. Copy the name, and paste it into the Display name-optional field. Scroll down, and expand the access policy section.

Under Choose method, choose Advanced. In the JSON editor, a default access policy is displayed. An access policy indicates who and what has permissions to publish to a topic. For this demonstration, you use a unique policy as shown on the screen. The policy effect is either allow or deny.

Here it is set to Allow, all AWS principals to complete the action called SNS:Publish on the specific Inventory-report resource. The Condition element is optional and specifies conditions for when a policy is in effect. In this case, the condition is that this policy runs only if the SourceAccount matches the one listed. Copy this policy, and paste it into the JSON editor. Scroll down, and choose Create topic.

The console returns you to the new topic's Details page. Scroll down, and choose Subscriptions. On the Subscriptions page, choose Create subscription. On the Create subscription page, choose the Topic ARN field.

Open your access policy and copy the Resource ARN. Paste it into the Topic ARN field. For Protocol, choose Email. For Endpoint, enter an email address that can receive notifications. Choose Create subscription.

The console opens the new subscription's Details page. Locate Status and notice that it now says Pending confirmation. Check your email inbox. It takes a few minutes for the confirmation email to appear. The sender ID is no-reply@sns.amazonaws.com. Choose Confirm subscription in the email from AWS Notifications.

Amazon SNS opens your web browser and displays a subscription confirmation with your subscription ID. Go back and refresh the SNS Subscriptions tab. Under Status notice that the Pending confirmation now says Confirmed.

Next, navigate to the Services menu and choose S3. When the S3 console opens, choose Create bucket to create a bucket that will hold the inventory reports. For name, enter s3-demo-mgmt-inventory-123. Scroll down, and choose Create Bucket. Next, configure the inventory configuration. On the customer-photos-123 bucket, choose Management and scroll down to the Inventory configurations. Choose Create inventory configuration.

In Inventory configuration name, enter the name as daily-inventory. Under Destination, choose the destination bucket where you want reports to be saved. Choose Browse S3, select the s3-demo-mgmt-inventory-123 bucket, and then select Choose path.

The destination bucket must be in the same AWS Region as the bucket for which you are setting up the inventory. Under the Destination bucket field, you see the permission that is added to the destination bucket policy to allow Amazon S3 to place data in that bucket. Leave Frequency as Daily. Leave the Output format for the report as CSV. And under Status, choose Enable.

In the Additional fields section, select Size and Last modified date. Choose Create.

Now you need to enable and configure event notifications for the s3-demo-mgmt-inventory-123 bucket. Return to the Amazon S3 bucket overview. In the S3 Buckets list, choose s3-demo-mgmt-inventory-123, and choose Properties. Scroll down to the Event Notifications section, and choose Create event notification.

Under Event name, enter new-inventory-report-added. In the Event types section, choose All object create events. In the Destination section under Destination, choose SNS topic. And under Specify SNS topic, select Choose from your SNS Topics. In the SNS topic dropdown, select the Inventory report available. Choose Save changes.

The inventory report can take up  to 48 hours to populate. This is an example of the Inventory-report notification. Finally, to view the inventory report and ensure that the notifications were successful, open the AWS Management Console and navigate to the S3 console. Select the s3-demo-mgmt-inventory-123 bucket.

Under the Name column, notice that you now have a customer-photos-123 object. This is the bucket on which you configured the inventory reports. Chose the customer-photos-123, choose daily-inventory, choose data, and select the inventory report.

When the report opens, select Object Actions, Query with S3 Select. Notice the configurations that you chose earlier in the demo, such as Format CSV and Comma delimited output. Scroll to the SQL query section. This SQL query will return the first five objects in the report.

To list more items in the report, change the size from five to 20 and choose Run SQL query. The results appear at the bottom. Under Raw, you see the output values in a CSV format. Choose Formatted to view the results in columns.

Here the columns indicate the bucket name, the object key name, IsLatest version is true, the Deletemarker is false, and the size of the file and the date. If you need a copy of the CSV file, choose Download results and save the file to your computer.

If you return to the daily-inventory prefix, two new prefixes appear.

The 2020-12-18T00 contains the manifest.json, which is the actual manifest file, and the manifest.checksum, which is the MD5 checksum of the manifest.json file. The hive folder is the sysmlink.txt file, which is the Apache Hive-compatible manifest file.

#### Amazon S3 Replication
S3 Replication provides automatic, asynchronous copying of objects across S3 buckets. S3 Replication is an elastic, fully managed, low-cost feature that automatically replicates objects between S3 buckets. S3 Replication gives you the most flexibility and functionality in cloud storage to help you meet your compliance, business continuity, and data sovereignty requirements.

##### Replicate objects while retaining metadata
You can use replication to make copies of your objects that retain all metadata, such as the original object creation times and version IDs. This capability is important if you must ensure that your replica is identical to the source object.

##### Replicate objects into different storage classes
You can use replication to directly put objects into S3 Glacier Flexible Retrieval, S3 Glacier Deep Archive, or another storage class in the destination buckets. You can also replicate your data to the same storage class and use lifecycle configurations on the destination buckets. You can then move your objects to a colder storage class as they age.

##### Maintain object copies under different ownership
Regardless of who owns the source object, you can tell Amazon S3 to change replica ownership to the AWS account that owns the destination bucket. This is called the owner override option. You can use this option to restrict access to object replicas.

##### Keep objects stored over multiple AWS Regions
To ensure geographic differences in where your data is kept, you can set multiple destination buckets across different Regions. This feature might help you meet certain compliance requirements.

##### Replicate objects within 15 minutes
To replicate your data in the same Region or across different Regions within a predictable time frame, you can use S3 Replication Time Control (S3 RTC). S3 RTC replicates 99.99 percent of new objects stored in Amazon S3 within 15 minutes. This is backed by a service-level agreement (SLA).

##### Sync buckets and replicate existing objects
To sync buckets and replicate existing objects, use Batch Replication as an on-demand replication action.

##### Replicate objects and fail over to a bucket in another Region
You can keep all metadata and objects in sync across buckets during data replication. Use two-way replication rules (also known as bi-directional replication) before configuring Amazon S3 Multi-Region Access Point failover controls. Two-way replication rules help ensure that when data is written to the S3 bucket that traffic fails over to, that data is then replicated back to the source bucket.

#### Same-Region Replication (SRR)
Customers can use it to consolidate application logs from multiple buckets or multiple accounts into one central archival bucket. They also use it to keep development, testing, and production buckets in sync for their users.

Amazon S3 supports automatic and asynchronous replication of newly uploaded S3 objects to a destination bucket in the same Region. SRR makes another copy of S3 objects within the same Region, with the same redundancy as the destination storage class. This helps you automatically aggregate logs from different S3 buckets for in-Region processing. You can also configure live replication between test and development environments. SRR helps you address data sovereignty and compliance requirements by keeping a copy of your objects in the same Region as the original.

##### Cross-Region Replication (CRR)
If you need data stored in multiple Regions, you can replicate your bucket to other Regions using CRR. You can automatically copy objects from a bucket in one Region to a different bucket in a another, separate Region. You can replicate the entire bucket or you can use tags to replicate only the objects with the tags you choose.

Customers use CRR for multiple reasons. They use it to meet compliance requirements that dictate maintaining data in different physical locations a minimum number of miles apart. They also use it to minimize latencies for geographically distributed users and centralize a global data lake in the same Region as their compute clusters.

Now, if you are looking for a predictable SLA-backed guarantee on your data replication, consider using S3 RTC. It is designed to replicate 99.99 percent of your objects within 15 minutes of upload, with replication typically completing in seconds. You get an SLA commitment that 99.9 percent of your objects will get replicated to your destination bucket in that 15-minute time interval.

#### Replication requirements
##### Regional requirements
The source bucket owner must have the source and destination Regions activated for their account. The destination bucket owner must have the destination Region activated for their account.

##### Versioning
Both source and destination buckets must have versioning activated.

##### Permissions
To use replication, Amazon S3 must have permissions to replicate objects from the source bucket to the destination bucket, or buckets, on your behalf. 

The owner of the source bucket might not own the object in the bucket. The object owner must then grant the bucket owner READ and READ_ACP permissions with the object access control list (ACL).

##### S3 Object Lock
If the source bucket has S3 Object Lock activated, the destination buckets must also have S3 Object Lock activated.

#### Configuring replication rules
To set up replication, you need to define a replication configuration on your bucket. A replication configuration is a set of rules that dictate which options Amazon S3 applies to your objects during replication. You can use the AWS Management Console, REST API, AWS CLI, or AWS SDKs to configure replication rules.

##### Select source bucket and objects
Specify whether you want to replicate all of the objects in the source bucket or a subset. You identify a subset by providing a prefix, object tag, or both.

##### Select IAM role
Specify an IAM role that Amazon S3 can assume to replicate objects on your behalf.

##### Select destination buckets
Choose the destination bucket, or buckets, where you want Amazon S3 to replicate objects in the same or a different Region.

#### Optional configurations
##### Select storage class
By default, Amazon S3 stores replica objects in the same storage class as the source object. You can specify a different storage class for the replicas. For example, you can choose to store your replicas in a lower-cost storage class than your source bucket to save costs.

##### Configure replica modification sync
By default, Amazon S3 replicates metadata, such as tags and S3 Object Lock settings, from the source objects to the replicas only.

You can choose to replicate object metadata bidirectionally between buckets by turning on the replica modification sync feature. Replica modification sync is useful for keeping all object and object metadata changes in sync when building shared datasets across Regions.

##### Activate S3 RTC
If you need a predictable replication time backed by an SLA, you can activate S3 RTC. It replicates 99.99 percent of objects within 15 minutes after upload, with the majority of those new objects replicated in seconds.

##### Use encryption
You can use replication for objects encrypted at rest using server-side encryption with customer provided keys (SSE-C). Client-side encryption (encrypting the data before uploading to Amazon S3) will not have any effect on replication.

##### Configure multiple ownership
When Amazon S3 replicates an object, it also replicates the corresponding object ACL for that object.

Your source and destination objects might be owned by different accounts. You can configure replication to change replica ownership to the AWS account that owns the destination buckets. 

##### Activate replication metrics
You can turn on replication metrics in your replication configuration to monitor the progress of your replication through Amazon CloudWatch metrics.

#### Replicable items
Amazon S3 replicates only specific items in buckets that are configured for replication. By default, Amazon S3 replicates the following:
* Objects created after you add a replication configuration
* Unencrypted objects
* Objects encrypted with SSE-C, objects encrypted at rest under an Amazon S3 managed key (SSE-S3), or a KMS key stored in AWS Key Management Service (SSE-KMS)
* Object metadata from the source objects to the replicas
* Only objects in the source bucket for which the bucket owner has permissions to read objects and ACLs
* Object ACL updates, unless you direct Amazon S3 to change the replica ownership when source and destination buckets aren't owned by the same accounts
* Object tags (if there are any)
* S3 Object Lock retention information (if there is any)

#### Non-replicable items
By default, Amazon S3 doesn't replicate the following: 
* Objects that existed before you added the replication configuration to the bucket
* Objects in the source bucket that are replicas created by another replication rule
* Objects in the source bucket that have already been replicated to a different destination
* Objects that are stored in S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive
* Objects in the source bucket that the bucket owner doesn't have permission to replicate (when the bucket owner is not the owner of the object)
* Updates to bucket-level sub-resources
* Actions performed by lifecycle configuration

**If you want to activate existing object replication for your account, you can use S3 Batch Replication. This provides you a way to replicate objects that existed before a replication configuration was in place. You can also replicate objects that have previously been replicated, and objects that have failed replication. You do this with a Batch Operations job. This differs from live replication, which continuously and automatically replicates new objects across S3 buckets.**

#### Amazon S3 Versioning
With versioning, you can keep multiple variants of an object in an S3 bucket. You can preserve, retrieve, and restore previous versions of objects in a bucket.

Use versioning to recover from both unintended user actions and application failures. For example, if you overwrite an object, Amazon S3 creates a new object version in the bucket. You can always restore the previous version. If you delete an object, instead of removing it permanently, Amazon S3 inserts a delete marker, which becomes the current object version. You can then restore the previous version.

##### Versioning bucket states
Buckets can be in one of the following three versioning states:
* Unversioned (default setting)
* Versioning-enabled
* Versioning-suspended

**To use versioning, you must activate it on your bucket. After you activate versioning on a bucket, it can never return to an unversioned state. You can suspend versioning to stop accruing new versions of the same object in a bucket. The versioning state you define applies to all of the objects in a bucket.**

##### [Additional information VERSIONING](https://docs.aws.amazon.com/AmazonS3/latest/userguide/manage-versioning-examples.html)

#### Working with version IDs
Regardless of whether you activate versioning, all objects in Amazon S3 have a version ID. Version IDs are Unicode strings associated with your objects. Only Amazon S3 generates version IDs, and you cannot edit them. If you don't activate versioning for a bucket, Amazon S3 sets the value of the version ID for its objects to null.

When you activate versioning for a bucket, Amazon S3 automatically generates a unique version ID for each new object you add to that bucket. This value distinguishes it from other versions of the same object.

When you activate versioning on a bucket, objects that are already stored in the bucket are unchanged. The version ID's value (null) remains the same.

#### Viewing and managing multiple object versions
Sign in to the console and navigate to the bucket that contains the object. To see a list of the versions in the bucket, select **Show versions**.

To download the noncurrent object version, select the check box next to the version that you want to retrieve. Next, to download the object, choose **Download**.

To delete the current version, select the check box next to it. Next, choose **Delete**.

#### Working with delete markers
When you delete an object in a bucket with versioning without specifying a version ID, Amazon S3 creates a delete marker for the object. A delete marker is a placeholder (or marker) for a versioned object that was named in a DELETE request. A delete marker has a key name and a version ID like any object in an S3 bucket.

When Amazon S3 creates a delete marker, the delete marker becomes the current version of the object.

When you try to retrieve an object whose current version is a delete marker, Amazon S3 returns a 404 Not Found error.

#### Removing delete markers
To restore a deleted object in a bucket with versioning, you must delete the delete marker associated with it. For example, if you want to delete a delete marker using the REST API, you must specify its version ID in a delete request.

The following example removes the delete marker for photo.gif version 1234567.

```
DELETE /photo.gif?versionId=1234567 HTTP/1.1
Host: DOC-EXAMPLE-BUCKET.s3.amazonaws.com
Date: Wed, 28 Oct 2009 22:32:00 GMT
Authorization: AWS AKIAIOSFODNN7EXAMPLE:0RQf4/cRonhpaBX5sCYVf1bNRuU=
```

If you don't specify a version ID in your delete request, Amazon S3 adds another delete marker instead of deleting the object. The new delete marker then becomes the current version of the object. It is possible to have multiple delete markers of the same object in one bucket. 

To undelete an object, you must delete the delete marker. Select the check box next to the delete marker of the object to recover, and then choose **Delete**.

#### Working with versioning-suspended buckets
In Amazon S3, you can suspend versioning to stop accruing new versions of the same object in a bucket. You might do this because you only want a single version of your objects in a bucket. Or, you might not want to accrue charges for multiple versions. When you suspend versioning, existing objects in your bucket do not change. What changes is how Amazon S3 handles objects in future requests. Amazon S3 will do the following:
* If a null object version exists and you add another object with the same key, the added object overwrites the original null version.
* If there are versioned objects in the bucket, the version you add becomes the current version of the object. Adding an object to a bucket that contains versioned objects does not overwrite the object already in the bucket. Here, Amazon S3 attaches a version ID of null to the new object. The noncurrent version of the object retains its original version ID and is not overwritten.

#### Multi-factor authentication (MFA) delete
You can use MFA delete to add an additional layer of security to your buckets with versioning. MFA delete can help prevent accidental bucket deletions. The user who initiates the delete action must prove physical possession of an MFA device with an MFA code. This adds an extra layer of friction and security to the delete action.

With MFA delete, the following two forms of authentication are required to change the versioning state of a bucket or delete an object version:
* Your AWS account credentials
* A  valid six-digit code and serial number from an MFA authentication device in your physical possession

An MFA authentication device can be one of the following: 
* A virtual MFA device, which is an application that is compliant with RFC 6238, a standards-based, time-based, one-time password algorithm. You can install the application on a phone or other device.
* A Universal 2nd Factor security key with an AWS supported configuration.
* A hardware-based MFA device. This device is a tamper-evident hardware key fob or display card device provided by Gemalto, a third-party provider.

##### [MFA for IAM](https://aws.amazon.com/iam/features/mfa/?audit=2019q1)

##### Activating MFA delete
You can activate MFA delete using AWS CLI or REST API. The following example activates versioning and MFA delete on a bucket using AWS CLI.

```
aws s3api put-bucket-versioning --bucket DOC-EXAMPLE-BUCKET --versioning-configuration Status=Enabled,MFADelete=Enabled --mfa "SERIAL 123456"
```

##### Deleting with MFA delete 
To permanently delete objects from a bucket using MFA delete, you must include the **x-amz-mfa** request header in your DELETE request. The MFA header consists of the concatenation of your MFA device’s serial number, a space, and the MFA code displayed on your authentication device. Requests that include **x-amz-mfa** must use HTTPS. 

The following example request shows how to delete a specific version of report.csv in a bucket called **DOC-EXAMPLE-BUCKET**, which has MFA delete.

```
DELETE /report.csv?versionId=3HL4kqCxf3vjVBH40Nrjfkd HTTPS/1.1
Host: DOC-EXAMPLE-BUCKET.s3.amazonaws.com
x-amz-mfa: serial_number 123456
Date: Fri, 28 May 2021 21:01:00 GMT
Authorization: AWS AKIAIOSFODNN7EXAMPLE:0RQf4/cRonhpaBX5sCYVf1bNRuU=
```

#### Knowledge Check
##### What happens to the version IDs of objects that were already stored in a bucket when versioning is activated?
* The version ID values of the objects (null) remain the same.

When a user activates versioning on a bucket, the version IDs of objects that were already in the bucket (null) do not change.
Wrong answers:
* Amazon S3 generates new version IDs for the objects. 
* Objects already stored in the bucket do not have any version ID associated with them.
* It is not possible to activate versioning on a bucket that contains objects. A user needs to empty the bucket before activating versioning.

##### What information does a delete request for an object in a bucket with multi-factor authentication (MFA) delete activated need to include?
* It must include the x-amz-mfa request header in the DELETE request. The MFA header consists of the concatenation of the MFA device’s serial number, a space, and the MFA code displayed on the authentication device.

To permanently delete objects from a bucket with MFA delete activated, the DELETE request must include the x-amz-mfa request header. The MFA header consists of the concatenation of the MFA device’s serial number, a space, and the MFA code displayed on the authentication device. Requests that include x-amz-mfa must use HTTPS.
Wrong answers:
* It must include the x-amz-mfa request header in the DELETE request. The MFA header consists of the AWS account number and the MFA code displayed on the authentication device.
* It must include the x-amz-content-sha256 header with a hash of the request payload.
* There is no need to include any information with the delete request for objects in a bucket with MFA delete activated.

##### For security reasons, a company's source and destination buckets are owned by different AWS accounts. How do they ensure that the AWS account that owns the destination bucket owns the replicated objects?
* They must select the Replica Ownership option when configuring the replication rule.

They can use the Replica Ownership setting to ensure that the AWS account that owns the destination bucket also owns the replicated objects.
Wrong answers:
* They must select an AWS Identity and Access Management (IAM) role that grants access to the AWS account that owns the replicated objects.
* They must contact AWS Support and create a technical support case.
* They don’t need to do anything. Amazon S3 automatically changes object ownership for them.

#### Hybrid Cloud and Edge Storage

#### AWS Snow Family
#### Snowcone
Snowcone provides storage and compute resources in a portable, ruggedized, self-contained solution. Customer use cases for Snowcone can be grouped into three general workflows. 

##### Data transfer to and from AWS
* **Usage scenario**: Bulk data transfer into or out of AWS, either offline by shipping physical devices, or online using Snowcone with AWS DataSync.
* **Customer examples**: Public sector, defense, intelligence, and law enforcement customers use Snowcone for tactical edge scenarios at land, air, and sea to migrate data to AWS. Snowcone devices are deployed and used to collect data as an Network File System (NFS)v4 mount point and transfer that data back to AWS.

##### Edge computing for data collection, processing, and transfer
* **Usage scenario**: Aggregating and processing data in edge locations and then transferring it to AWS.
* **Customer examples**: Media and entertainment, professional sports teams, and other content creators use Snowcone to do the following with content from cameras on movie sets, photo shoots, and at sporting events:
 * Aggregating and encoding the content
 * Migrating the data to Amazon Simple Storage Service (Amazon S3) 

##### Edge computing with local processing and storage
**Usage scenarios**: 
* Edge computing applications to collect data, process the data to gain immediate insight, and then transfer the data to AWS.
* Transfer data that is continuously generated by sensors or machines online to AWS from hospitals, factory floors, or other edge locations.

* **Customer examples**: Customers in healthcare use Snowcone as an Internet of Things (IoT) hub to process data, and transfer it to the AWS Cloud. Snowcone provides a secure path for customers to centrally manage the configuration and operation of Snowcone devices deployed across worldwide customers and organizations.

Customers focused on getting packages from delivery stations to a customer's doorstep are deploying Snowcone devices in trucks for data collection. Snowcone is used to process data locally for immediate insights and to transfer the data to AWS for broader, long-term analysis.

#### Snowball Edge
Snowball Edge is a data migration and edge computing device that comes in two device options: Compute Optimized and Storage Optimized. There are two main use cases: data transfer and compute and storage. 

##### Data transfer
Use Snowball Edge to transfer offline data, or data that is not actively being changed, updated, or manipulated. The data transfer process occurs over a small period of time—from a couple of days to a couple of weeks. If you use Snowball Edge to transfer any active data that might change or is incomplete, you can experience versioning issues and data transfer errors because of incomplete objects. 

##### Data center migration
Customers might find it challenging to move existing data to the cloud, whether they want to move all their data or only specific datasets. Their situation might require that they frequently develop and test their applications in the cloud with sample datasets. After customers test the applications and verify that they are ready, they need to migrate the full datasets to the cloud. This migration process must occur in a relatively short period of time.

To move large volumes of data, they can create multiple Snowball Edge jobs to increase the number of Snowball Edge devices to meet their needs. Using the storage-optimized model, customers can transfer up to 80 TB of data on the single device. 

Copying data from on-premises storage to the Snowball Edge devices takes time, which varies based on the number of files and the file sizes. Snowball Edge simplifies the process of planning for migration, secures and protects the data, and facilitates a predictable and timely migration. 

AWS encourages customers to work with their account team to plan their migration projects.


##### Backup seeding
Backup seeding provides a staged approach to transferring backups to the cloud. You can perform a seed backup to a temporary storage medium and then transfer it to the cloud. For larger backups, the size of your data might limit your use of a high-speed internet connection for the task. Transfers can take long periods of time to complete, and often cannot complete before the next backup cycle begins. 

If you need to retrieve a backup, you can use Snowball Edge as an export device, so you can restore your data from nearly any size backup in a timely manner. 

You can also use Snowball Edge as the temporary storage medium or populate it from other temporary backup storage options. The transfer to the cloud is accomplished by physically shipping the Snowball Edge instead of attempting to use a high-speed internet connection. 

Use Amazon S3 storage for all new backup operations. Backups can be retrieved from Amazon S3 storage over an internet connection for restoration or by using Snowball Edge to export the backup.

##### Assisted database migration
Larger data migrations can include many terabytes of information. This process can be challenging due to network bandwidth limits or the amount of data. 

AWS offers AWS Database Migration Service (AWS DMS), which uses Snowball Edge as a key component to copy point-in-time database components to the cloud. All relevant data is maintained, uploaded to the cloud, and then transferred to the appropriate location. Snowball Edge provides quick transfers, maintains data integrity and security, and simplifies the database migration process.

##### NAS appliance archival
On-premises network-attached storage (NAS) devices continue to grow in capacity. The volume and rate of data growth is driving a need to offload data to the cloud. It's nearly impossible for customers to back up NAS appliance data because of the large volume of data. Restoration from backup to a new NAS device cannot happen within a reasonable time period. 

You can use Snowball Edge to transfer the initial copies of the files stored in the on-premises NAS appliances. Use the Snowball Edge devices to store cold or archival copies of the file data before securely transferring the data to the AWS Cloud. The data remains accessible in the cloud when you need it. You can then perform updates to the data on the files stored as objects in the cloud. 

To transition cold data, copy the data to the Snowball Edge device, upload to the AWS Cloud, and then delete it from the on-premises NAS appliance. After the archival, NAS data is in the AWS Cloud. You can transition it through its lifecycle to Amazon S3 Glacier Instant Retrieval, Amazon S3 Glacier Flexible Retrieval, or Amazon S3 Glacier Deep Archive storage classes to optimize archival storage costs. 

##### Data lake creation or migration
To create a new data lake or migrate an existing data lake to the cloud, you must transfer large volumes of data. 

Use Snowball Edge as a standalone device or multiple devices to accomplish the task. Upload speeds for data transfer commonly range from 200–450 MBps using the Snowball Edge adapter. After importing your data into your S3 bucket, you can perform the following operations: 
* Use the data.
* Migrate the data to be stored as file or block storage within Amazon S3.
* Integrate with other AWS services, such as Amazon Athena for analysis, AWS Glue for data transformation, and Amazon OpenSearch Service for search capabilities. 

##### Archive data
Archive data presents several challenges. It typically consumes large amounts of local storage space, which is expensive to expand and maintain. The archive data might be located in offline storage, such as tape or external hard drives. Often only a single copy of the archive data is maintained, which is at risk for data loss. 

Using Snowball Edge, you can import your data into your S3 bucket and transition it through the data management lifecycle using S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, or S3 Glacier Deep Archive storage classes for long-term, money-saving storage. The archive data no longer takes up local storage space and uses storage designed for durability and high availability that mitigates the risk of potential data loss.

#### Compute and storage
You can use the Snowball Edge compute functions to collect information from your data center for processing before you import the data to the AWS Cloud. You can also use Snowball Edge for edge computing. Edge computing brings data storage and compute resources closer to where you need them.

Snowball Edge provides storage and compute resources in a portable, ruggedized self-contained solution. Local compute can meet usage needs with the Amazon Elastic Compute Cloud (Amazon EC2) Amazon Machine Images (AMIs) and AWS Lambda functions that are powered by AWS IoT Greengrass.

##### Imagery processing and analysis
Because many remote locations have imagery data associated with video sensors, you might need to assess the imagery and provide real-time actionable intelligence. One customer, GE Oil & Gas, assesses pipeline inspection gauges with imagery and ultrasonic sensor data to address pipeline health, such as bad welds and fissures.

Customers use Snowball Edge to capture sensor inputs from drones, submersibles, custom devices, and even healthcare equipment, such as CAT scans and MRI devices where internet links are inaccessible or intermittent.

##### Backup software to offline migration
Snowball Edge helps you create offline backup migrations, and is designed to work with software from many vendors. The Snowball Edge compute capabilities work well in scenarios where you don't have on-premises devices to handle the software agents. 

##### Import data obfuscation
In any dataset with personally identifiable information (PII), such as scenarios with financial services companies, you want to obfuscate, or conceal, your data. The PII is identified on ingest and Lambda begins pseudonymizing, or disguising, the data to avoid exposing unprotected PII information. The confidentially protected data is stored for upload in the AWS Cloud or for temporary local use from the Snowball Edge. 

##### Overflow compute on the edge
Customers that need additional temporary compute power use Snowball Edge to provide the additional resources. Providing additional resources when needed is similar to the tenets for utility computing in the cloud. Here, the tenets are applied to on-premises computing using a Snowball Edge device.

#### Ordering an AWS Snow Family device
Ordering an AWS Snow Family device to migrate your workload is a straightforward process. For Snowcone and Snowball Edge, you can create a new job in the Snow Family console. In the following example, you will learn about the Snowball Edge configuration and ordering process. 

The Snowball Edge process always begins with configuring resources, creating a job, and placing an order. You should plan every Snowball Edge job before you begin the ordering process. After you order the Snowball Edge device, you cannot change the configuration. If you need to change a setting, you must cancel the Snowball Edge order and place a new order. To avoid incurring charges, you must cancel a Snowball Edge order before it ships.

If you plan to use Amazon EC2 as part of your Snowball Edge job, you must identify and create each of the Amazon EC2 AMIs. You must do this before you create the Snowball Edge order and then add them to your job during the job creation process.

1. **Create a Snowball Edge order**. AWS management console with AWS Snow Family page displayed.
To configure and order your Snowball Edge device, use the AWS Management Console. Create a Snowball Edge job under the AWS Snow Family service. The console walks you through the job creation process, step by step. Choose Order an AWS Snow Family device to continue. 
2. **Select the job type**. To create the Snow Family job, you add a unique job name for the Snowball Edge job. Each job is identified and tracked separately. You select the job type: **Import into Amazon S3, Export from Amazon S3, Local compute and storage only**, or **Import virtual tapes into AWS Storage Gateway**. In this example, select **Import into Amazon S3** and choose Next to continue.
3. **Select the Snowball Edge device type**. Select the Snow Family model for the job. You can choose from Snowcone, Snowcone SSD, Snowball Edge Storage Optimized, Snowball Edge Compute Optimized, or Snowball Edge Compute Optimized with GPU devices for your job. If you select a device that is backlogged or constrained, a notification message appears at the top of the page. AWS recommends working with your account team to plan your Snow Family device. You add the additional information for the job as you continue this configuration page. In this example, you select the Snowball Edge Storage Optimized with 80TB option. With this option, you have three pricing options to choose from: on-demand pricing, a 1-year term pricing commitment, and a 3-year term pricing commitment. Term pricing is for long-running Snow Family jobs. On-demand is for short-term jobs like migration projects.
4. **Add compute services**. Add any compute services by selecting your preconfigured EC2 AMIs for your Snowball Edge order. Your selection of compute services is optional and based on how you intend to use the Snowball Edge device. 
5. **Select your Amazon S3 bucket and data**. Every Snowball Edge job is associated with one or more S3 buckets, even local compute and storage jobs that are not uploaded to Amazon S3 when the job is completed. Select the S3 bucket or buckets to associate with the job. You can also create a new bucket if necessary. For an export job type, you select the S3 bucket data that you want to export. You can also explicitly select a range of objects by using object key ranges for the export job.
6. **Configure features and options**. If you want to manage the device remotely with OpsHub or Snowball Client, you can configure it in this step.  For more information, see [Using AWS Snow Device Management to Manage Devices](https://docs.aws.amazon.com/snowball/latest/snowcone-guide/aws-sdm.html) in AWS Snowcone User Guide.
7. **Create role permissions and set the encryption key**. You first choose the AWS Key Management Service (AWS KMS) encryption key, which is used to secure data access on the Snowball Edge device. The job details that you enter create a specific AWS Identity and Access Management (IAM) service role for the Snowball Edge device. The role is used to grant access to the appropriate secure user and to configured resources on the device. These permissions are required to allow the services to interact with the Snowball Edge device. For more information, refer to [Step 4: Choose Your Security Preferences](https://docs.aws.amazon.com/snowball/latest/developer-guide/set-security.html) in the AWS Snowball Edge Developer Guide.
8. **Add shipping details**. Add your shipping details, including shipping location, and select the default **One-Day Shipping** or **Two-Day Shipping**. The Snowball Edge device will be shipped after the device has been prepared for your job. The shipping rate applies only to the transportation time to and from your location. The requested shipping information varies based on the AWS Region.
9. **Set notifications**. To complete the configuration details, add an Amazon Simple Notification Service (Amazon SNS) topic. You can track the job status using the Amazon SNS notifications. Notifications are sent through SMS or text messages. You can check the job status at any time using the console.
10. **Review and submit the order**. The final step in the process is to review your Snow Family order. You can edit any area that is incorrect before submitting your order. After you submit your order, you cannot change it. You must cancel the order and create a new order.
11. **Summary**. The configuration and ordering process is quick and simple to complete when you have prepared. If you need to make changes, you can cancel your order before it ships and create a new one. If the order ships, you must return the Snowball Edge device before the order can be terminated. You are charged for any unit that ships.

#### Snowmobile
Snowmobile moves extremely large amounts of data to AWS. Transfer up to 100 PB per Snowmobile, a 45-foot-long ruggedized shipping container pulled by a semi-trailer truck. It provides the following use cases: 
* Migrate massive amounts of data.
* Customize data transfer operations to your location.
* Meet security requirements for data migration.

#### Configuring a Snowmobile job
A Snowmobile job includes the data migration process using a Snowmobile. There are five main steps:

##### Site survey
AWS personnel will work with the customer to understand their migration objectives, data center environment, and network configurations to help them determine a migration plan.

##### Site preparation
The customer will identify and make available local resources such as parking space and power source for the Snowmobile. The customer also identifies resources such as local security, network address, ports, and available rack positions to connect the Snowmobile with the local network backbone. 

##### Dispatch and setup
AWS personnel will dispatch a Snowmobile to the customer site and configure it for them so that it can be accessed securely as a network storage target.

##### Data migration
The customer will then copy data from any number of sources within their data center to the Snowmobile.

##### Return and upload
The Snowmobile is returned to an AWS Region that the customer has designated, where their data will be uploaded into the AWS storage services that they have selected.

#### Data migration process works using Snowmobile
##### How does a customer get started with a Snowmobile?
They would need to contact their sales team(opens in a new tab) to request a Snowmobile.

##### How does a customer connect their data center to a Snowmobile?
Each Snowmobile comes with a removable high-speed connector rack on wheels with two kilometers of ruggedized networking cable. The connector rack can be rolled to a location inside a customer's data center and connected directly to their network backbone. This way, the Snowmobile will operate as a network storage target inside their network for them to perform a high-speed data transfer. 

##### How does a customer copy their data to a Snowmobile?
When the Snowmobile is connected to their data center, it will appear as a network storage target. They can copy data from local storage devices to the Snowmobile using the same tools and in the same manner as data copied to any network attached storage device with an NFS interface. 

##### How does a customer verify that their data has been successfully copied to Snowmobile?
At the time that their data is copied into the Snowmobile, a set of logs will be generated with checksums for each file transferred. These logs are available to them for verification. The logs are also used when data is imported from the Snowmobile to AWS to verify that all data has been transferred successfully.

##### Does a customer need to keep a local copy of their data while a copy is shipped back to AWS on a Snowmobile?
Yes. They should always keep their source copy until AWS has worked with them to verify that the Snowmobile copy has been successfully uploaded to AWS.

##### Can a customer export data from AWS with Snowmobile?
Snowmobile does not support data export. It helps customers quickly, easily, and more securely migrate exabytes of data to AWS. When a customer needs to export data from AWS, they can use AWS Snowball Edge to export up to 100 TB per appliance and run multiple export jobs in parallel as necessary.

#### AWS at the Edge with Amazon CloudFront

#### CloudFront use cases
##### Accelerate static website content delivery
CloudFront can speed up the delivery of your static content (for example, images, style sheets, JavaScript, and so on) to viewers across the globe. By using CloudFront, you can take advantage of the AWS backbone network and CloudFront edge servers to give your viewers a fast, safe, and reliable experience when they visit your website. 

##### Serve video-on-demand or live streaming video
CloudFront offers several options for streaming your media to global viewers—both prerecorded files and live events.

For video-on-demand (VOD) streaming, you can use CloudFront to stream in common formats, such as MPEG DASH, Apple HLS, Microsoft Smooth Streaming, and CMAF, to any device.

For broadcasting a live stream, you can cache media fragments at the edge, so that multiple requests for the manifest file that delivers the fragments in the right order can be combined, to reduce the load on your origin server.

##### Encrypt specific fields throughout system processing
When you configure HTTPS with CloudFront, you already have secure connections to origin servers. When you add field-level encryption, you can protect specific data throughout system processing in addition to HTTPS security, so that only certain applications at your origin can see the data. 

##### Customize at the edge
Running serverless code at the edge opens up many possibilities for customizing the content and experience for viewers, at reduced latency. For example, you can return a custom error message when your origin server is down for maintenance, so viewers don't get a generic HTTP error message. Or you can use a function to help authorize users and control access to your content, before CloudFront forwards a request to your origin.

##### Serve private content by using Lambda@Edge customizations
Using Lambda@Edge can help you configure your CloudFront distribution to serve private content from your own custom origin, in addition to using signed URLs or signed cookies.

#### Using CloudFront with Amazon S3 for static web site
1. Create a bucket.
 * During the process of creating a bucket, select **ACL enabled**, and then **Bucket owner preferred**.
 * During the process of creating a bucket for this example, make sure to clear the check box for **Block all public access**. You must allow public read access to the bucket and files so that CloudFront URLs can serve content from the bucket. However, you can restrict access to specific content by using the CloudFront private content feature. For more information, see [Serving Private Content with Signed URLs and Signed Cookies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html). 
2. Upload content: index.html file and the css folder (with the style.css file inside it), for example.
 * During the uploading process, expand the **Permissions** section, keep settings at their defaults, and for **Predefined ACLs**, select **Grant public-read access**.
 * You can use the Amazon S3 URL **https://<DOC-EXAMPLE-BUCKET> .s3.<AWS Region>.amazonaws.com/<object name>** to verify that your content is publicly accessible, but remember that this is not the URL you will use to access your content with CloudFront.
 * **Note that if you created the bucket in the US East (N. Virginia) Region (us-east-1), omit the <AWS Region> portion of the URL. For example: https://DOC-EXAMPLE-BUCKET.s3.amazonaws.com/index.html**
3. Create a CloudFront distribution.
 * Open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v3/home](https://console.aws.amazon.com/cloudfront/v3/home). Choose **Create a CloudFront distribution**.
 * In the **Origin** section, for **Origin domain**, choose the Amazon S3 bucket that must be accessed with CloudFront. For the other settings in the **Origin** section, accept the default values.
 * For the **Default cache behavior** settings, accept the default values. For more information about cache behavior options, see [Cache Behavior Settings](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesCacheBehavior).
 * For this example, in the **Web Application Firewall (WAF)** section, select **Do not enable security protections** so that no charge will be incurred.
 * For the remainder of the settings, accept the default values. For more information about these options, see [Distribution Settings](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesGeneral).
 * At the bottom of the page, choose **Create distribution**.
 * On the **General** tab for your CloudFront distribution, under **Details**, the value of the **Last modified** column for your distribution changes from **Deploying** to the timestamp when the distribution was last modified. This process typically takes a few minutes. Record the domain name that CloudFront assigns to your distribution, which appears in the list of distributions. (It also appears on the **General** tab for a selected distribution.) It looks similar to the following: **d111111abcdef8.cloudfront.net**.
4. To access the content through CloudFront, combine the CloudFront distribution domain name with the path to access the content. For example, the distribution domain name looks similar to the following: **d111111abcdef8.cloudfront.net**. Traditionally, the path to access the main page of a website is **/index.html**. Here, you could access the content through CloudFront at a URL that looks similar to the following: **https://d111111abcdef8.cloudfront.net/index.html**.

#### AWS for Media Storage

####  Four fundamental stages common to most video workflows whether on premises or cloud-based, live, or VOD:
* Ingest stage
* Process stage
* Store stage
* Deliver stage

##### AWS Elemental MediaPackage
AWS Elemental MediaPackage can cache segments of live streams for start-over or catch-up TV, in addition to its packaging functions. 

##### AWS Elemental MediaStore
AWS Elemental MediaStore is a storage service that is specially tuned for workflows that require extremely low latency.

#### Example of hosting on-demand streaming video with Amazon S3
You can use Amazon S3 with Amazon CloudFront to host videos for on-demand viewing in a secure and scalable way. Video on demand (VOD) streaming means that your video content is stored on a server and viewers can watch it at any time. 

In the following example, you will get some ideas about how you can use CloudFront with Amazon S3 to host VOD. 

1. **Create an S3 bucket and upload a video**. Create a bucket to store the original video that you plan to stream. Make sure that **Object Ownership** is kept at the default, which is **ACLs disabled (recommended)**. **Block Public Access** settings for this bucket is kept at defaults. Do not clear the check box for **Block all public access**. All settings are kept at the defaults because a CloudFront origin access identity (OAI) will be used later. Then, upload a video. 
2. **Create a CloudFront OAI**. To restrict direct access to the video from your S3 bucket, create a special CloudFront user called an origin access identity (OAI). By using an OAI, you make sure that viewers can't bypass CloudFront and get the video directly from the S3 bucket (such as using the object URL). Only the CloudFront OAI can access the file in the S3 bucket. 
 * **Access Amazon CloudFront**. Sign in to the AWS Management Console and open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v3/home](https://console.aws.amazon.com/cloudfront/v3/home). In the left navigation pane, under the **Security** section, choose **Origin access**.
 * **Create origin access identity**. On the **Origin access** page, choose the **Identities (legacy)** tab, and then choose **Create origin access identity**. 
 * **Enter name**. Enter a name (for example, **S3-OAI**) for the new origin access identity, and then choose **Create**.
 * **Make a note of the Origin access identities ID**. It should look similar to this: **E1FWPUN776XWQ2**. Use this ID to verify an S3 bucket policy in the upcoming steps.
3. **Create a CloudFront distribution**. To use CloudFront to serve and distribute the video in the S3 bucket, you must create a CloudFront distribution. In this example, you will use the OAI that was created earlier.
 * **CloudFront**. Return to the main CloudFront console. Choose **Create a CloudFront distribution**.
 * **Origin domain**. In the **Origin section**, for **Origin domain**, choose the domain name of the S3 origin, which starts with the name of the S3 bucket that has the video file stored. 
 * **Origin access**. For **Origin access**, select **Legacy access identities**. For **Origin access identity**, choose the origin access identity that you created in Step 3 of the previous interaction (for example, **S3-OAI**). Then select **Yes, update the bucket policy**.
 * **Default cache behavior**. In the **Default cache behavior** section, for **Viewer protocol policy**, select Redirect **HTTP to HTTPS**. When you select this feature, HTTP requests are automatically redirected to HTTPS to secure your website and protect your viewers' data.  
 * **Web Application Firewall (WAF)**. For this example, in the **Web Application Firewall (WAF)** section, select **Do not enable security protections** so that no charge will be incurred.
 * **All other settings**. For the remainder of settings, accept the default values. For more information about the different settings options, see [Values That You Specify When You Create or Update a Distribution](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html) in the Amazon CloudFront Developer Guide. 
 * **Create distribution**. At the bottom of the page, choose **Create distribution**.
 * **CloudFront distribution status**. On the **General** tab for your CloudFront distribution, under **Details**, the value of the **Last modified** column for your distribution changes from Deploying to the timestamp when the distribution was last modified. This process typically takes a few minutes.
4. **Review the bucket policy**. Now that the CloudFront distribution is created, you can review the changes to the S3 bucket permissions. Open the Amazon S3 console, and choose the bucket that was used as the origin of the CloudFront distribution. Then, choose the **Permissions** tab. In the **Bucket policy** section, you will see a statement in the bucket policy text. Verify that the Origin Access Identity ID that you noted earlier matches the one in the policy. You can locate it at the end of the line that begins with **“AWS”:**. Also notice that the policy grants read access, through the **s3:GetObject** action, to the entire **cloudfront-origin bucket** (for example, **DOC-EXAMPLE-BUCKET**) as shown in the **“Resource”**: parameter. If you instead configure CloudFront to be limited to objects within a folder in the bucket, that folder path would be included in the resource parameter.
5. **Access the video through the CloudFront distribution**. Now CloudFront can serve the video stored in the S3 bucket. To access the video through CloudFront, you must combine the CloudFront distribution domain name with the path to the video in the S3 bucket. To find the CloudFront distribution domain name, open the CloudFront console. In the left-navigation pane, choose **Distributions**. On the **General** tab, you can see your distribution domain name. For example, the distribution domain name looks similar to the following: **d111111abcdef8.cloudfront.net**.

You will then combine this domain name with the video name (for example, kitty.mp4) with a forward slash (/). Here, you can access your content through CloudFront at a URL that looks similar to the following: **https://d111111abcdef8.cloudfront.net/kitty.mp4**.

##### [Amazon Simple Storage Service user guide > Hosting video steaming](https://docs.aws.amazon.com/AmazonS3/latest/userguide/tutorial-s3-cloudfront-route53-video-streaming.html)

#### Knowledge Check
##### What does Amazon CloudFront use to deliver content with low latency? 
* Edge locations 

##### Which step must someone complete before starting to configure their AWS Snowball Edge job? 
* Configure any Amazon EC2 Amazon Machine Images (AMIs) and AWS Lambda functions required for the job.

They must prepare and configure Amazon EC2 AMIs and Lambda functions before creating their Snowball Edge job.
Wrong answers:
* Determine their networking IP addresses for the Snowball Edge device.
* Set up a shipping address in the AWS Management Console.
* Set up permissions on the Amazon S3 bucket.

##### Which AWS offering is suitable for video-on-demand (VOD) storage?
* Amazon S3

VOD usually requires longer-term storage. Amazon S3 can be used for VOD storage because of its extremely high reliability and durability.

Wrong answers:
* AWS Elemental MediaPackage
* AWS Elemental MediaStore
* An Amazon EC2 instance store

The other options are incorrect because of the following: 
* AWS Elemental MediaPackage and AWS Elemental MediaStore are usually used for live streams that requires high frequency of read and write requests with extremely low latency.
* An instance store provides temporary block-level storage the EC2 instance. It is not suitable for tasks that requires longer-term storage.

#### Assessment



### Week 7: Storage 2 Part 3

#### Amazon EBS Features and Configurations

#### Types of EBS volumes 
##### General Purpose SSDs
* **General Purpose SSD (gp2) volumes** provide a balance of price and performance. They are suitable for a wide range of workloads, including boot volumes, small to medium-sized databases, and development and test environments. gp2 volumes offer baseline performance with the ability to burst performance for short periods.
* **The next-generation General Purpose (gp3) volumes** provide better price-to-performance ratio compared to gp2. They are designed for a broad range of workloads, including system boot volumes, virtual desktops, and low-latency interactive applications. These volumes provide independent configuration of IOPS and throughput. This offers flexibility in adjusting performance based on workload requirements.
* **All General Purpose SSD volume types** support boot volumes.

##### Provisioned IOPS SSDs
* **Provisioned IOPS SSD (io1) volumes** are suitable for I/O-intensive applications, critical databases, and large-scale workloads. They provide consistent and high I/O performance. io1 volumes deliver low-latency, predictable performance and are ideal for applications with demanding I/O requirements. 
* **The next-generation Provisioned IOPS SSD (io2) volumes** offer improved durability and higher performance compared to io1. They are designed for critical business applications such as transactional databases and analytic workloads. io2 volumes provide higher durability and more IOPS per volume, and they deliver consistent performance for mission-critical applications.
* **io2 Block Express volumes** provide the highest performance and lowest latency storage for I/O-intensive workloads. They are specifically optimized for the most demanding enterprise applications, large databases, and analytics workloads. With io2 Block Express, you can achieve higher throughput and IOPS performance while maintaining data durability and availability.  
* **All Provisioned IOPS SSD volume types** support boot volumes.

##### Throughput Optimized HDDs
* **Throughput Optimized HDD (st1) volumes** are designed for large, sequential workloads such as big data processing, data warehouses, and log processing. They offer low-cost storage with high throughput, and are optimized for sustained workloads with large block sizes. st1 volumes are ideal for workloads that require high throughput and cost-effective storage.

##### Cold HDDs
* **Cold HDD (sc1) volumes** are suitable for infrequently accessed workloads, such as long-term storage, backups, and archival data. They provide the lowest cost per gigabyte and are designed for scenarios that prioritize cost optimization. sc1 volumes are a cost-effective choice for workloads with low access frequency.  

#### Choosing the correct Amazon EBS volume type 
* **Is your workload more IOPS intensive or throughput intensive?** If your workload is IOPS intensive, start with the SSD volume types and review the performance characteristics. If your workload is more throughput intensive, you can start with HDD volume types to see if their performance can meet your requirements. 
* **Do the workload requirements exceed the maximum performance characteristics for a selected EBS volume type?** If yes, eliminate the volume type from consideration for that volume. Review characteristics for the next higher performing EBS volume type. 
* **What is the application's latency sensitivity?** If it is very low, and sub-millisecond to single-digit millisecond latency is needed, io2 Provisioned IOPS might be required. If single-digit to low two-digit latency is tolerable, gp3 General Purpose SSD might be the correct choice. If your workload is not latency sensitive, HDD volume types can be the most cost-effective choice. 
* **Do you prefer to optimize for price or performance?** When comparing the EBS volume types, multiple volume types can satisfy the requirements. Compare the EBS volume configurations required. Which configuration is more cost effective? Does a configuration offer additional desirable performance characteristics? Is there a trade-off and what is the value to your workload?

#### Which EBS volume type would you choose? 
##### Scenario one
**Background:**

A fast-growing technology startup company is developing a cloud-based software-as-a-service (SaaS) product. They need a storage solution that can handle their dynamic workload and provide optimal performance. 

**Requirements:**
* They need storage for boot volumes and development and test environments. 
* They require a balance of performance and cost effectiveness.
* Workload demands may vary, and they need the ability to burst performance when necessary.

The General Purpose SSD volume type (gp2) is ideal for this scenario. It provides a balance of price and performance, so it's suitable for their diverse workload. The ability to burst performance ensures optimal performance during peak demands, such as development and testing. gp2 meets their requirements for boot volumes and development and testing environments, and offers flexibility and cost effectiveness.

##### Scenario two
**Background:**

A data analytics company processes and analyzes large volumes of data for their clients. They need a storage solution that can efficiently handle their demanding workloads. 

**Requirements:**
* They require storage for data processing and analytics workloads.
* They require high throughput for processing large datasets.
* Cost effectiveness is a priority for their workloads.

The Throughput Optimized HDD (st1) volume type is the most suitable choice for the data analytics company. They deal with big data processing and require high throughput, and st1 provides cost-effective storage optimized for sustained workloads with large block sizes. It offers the required throughput for efficiently processing large datasets while prioritizing cost optimization. 

#### Attaching a volume to an instance 
You can attach an available EBS volume to one or more of your instances that is in the same Availability Zone as the volume. 

##### Console
**To attach an EBS volume to an instance by using the console, follow these steps:**
1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).
2. In the left navigation pane, choose **Volumes**.
3. Select the volume to attach, and choose **Actions > Attach volume**.
4. For **Instance**, enter the ID of the instance or choose the instance from the list of options.
5. For **Device name**, enter a supported device name for the volume. This device name is used by Amazon EC2. The block device driver for the instance might assign a different device name when mounting the volume. 
6. Choose **Attach volume**.
7. Connect to the instance and mount the volume. 

##### AWS CLI
**To attach an EBS volume to an instance by using the command line**, you can use one of the following commands:
* [attach-volume](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/attach-volume.html) using the AWS Command Line Interface (AWS CLI)
* [Add-EC2Volume](https://docs.aws.amazon.com/powershell/latest/reference/items/Add-EC2Volume.html) using AWS Tools for Windows PowerShell

**You can only attach volumes that are in the Available state. The volume must be attached to an instance in the same Availability Zone.**

#### Amazon EC2 Instance Root Device Volume
When you launch an instance, the root device volume contains the image used to boot the instance. Amazon Web Services (AWS) provides EC2 instances with two types of root devices: AMIs backed by Amazon EC2 instance store and AMIs backed by Amazon EBS. 

**Only the following instance types support an instance store volume as the root device: C3, D2, G2, I2, M3, and R3. st1 and sc1 volumes can't be used as root volumes.**

#### Root device storage concepts
You can launch an instance from either an instance store–backed Amazon Machine Image (AMI) or an Amazon EBS–backed AMI. The description of an AMI includes which type of AMI it is. You will see the root device referred to in some places as either ebs (for Amazon EBS–backed) or instance store (for instance store–backed). This is important because there are significant differences between what you can do with each type of AMI. It is recommended that you use AMIs backed by Amazon EBS, because they launch faster and use persistent storage.

##### Instance store–backed instances 
Instance store volumes temporarily attached to the host computer that Amazon EC2 instances run on. When an EC2 instance is created, the instance store volumes are automatically attached and mapped to specific device names, such as /dev/sda1 and /dev/sdb, called block devices. 

The data in an instance store persists only during the lifetime of its associated EC2 instance. If an EC2 instance reboots, whether intentionally or unintentionally, data in the instance store persists. However, data in the instance store is lost under any of the following circumstances:
* The underlying storage drive fails.
* The EC2 instance stops.
* The EC2 instance hibernates.
* The EC2 instance terminates.

##### Amazon EBS–backed instances 
EBS volumes are not the same as instance stores. Instances that use Amazon EBS for the root device automatically have an Amazon EBS volume attached. When you launch an Amazon EBS–backed instance, AWS creates an Amazon EBS volume for each Amazon EBS snapshot referenced by the AMI that you use. 

When an EC2 instance is created, you have the flexibility to attach EBS volumes of various sizes and types to your instance. These EBS volumes are then assigned unique volume IDs, which are used to map them to specific device names within the instance.

If an Amazon EBS–backed instance fails, you can restore your session by following one of these methods:  
* Stop the failed instance and and then start it again (try this method first).
* Automatically snapshot all relevant volumes and create a new AMI. For more information, see [Create an Amazon EBS–Backed Linux AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-an-ami-ebs.html).
* Attach the volume to the new instance by following these steps:
 1. Create a snapshot of the root volume.
 2. Use the snapshot to register a new AMI.
 3. Launch a new instance from the new AMI.
 4. Detach the remaining EBS volumes from the old instance.
 5. Reattach the EBS volumes to the new instance.

#### Amazon EBS–optimized instances
An Amazon EBS–optimized instance uses an optimized configuration stack and provides additional dedicated capacity for Amazon EBS I/O. This optimization provides the best performance for your EBS volumes by minimizing contention between Amazon EBS I/O and other traffic from your instance.

EBS-optimized instances deliver dedicated bandwidth to Amazon EBS. When attached to an EBS-optimized instance, General Purpose SSD (gp2 and gp3) volumes are designed to deliver at least 90 percent of their provisioned IOPS performance 99 percent of the time in a given year. Provisioned IOPS SSD (io1 and io2) volumes are designed to deliver at least 90 percent of their provisioned IOPS performance 99.9 percent of the time in a given year.

Both Throughput Optimized HDD (st1) and Cold HDD (sc1) deliver at least 90 percent of their expected throughput performance 99 percent of the time in a given year. Noncompliant periods are approximately uniformly distributed, targeting 99 percent of expected total throughput each hour.

#### EBS-optimized supported
The following instance types support EBS optimization, but EBS optimization is not enabled by default.  
* c1.xlarge 
* c3.xlarge, c3.2xlarge, c3.4xlarge 
* g2.2xlarge
* i2.xlarge, i2.2xlarge, i2.4xlarge 
* m1.large, m1.xlarge 
* m2.2xlarge, m2.4xlarge 
* m3.xlarge, m3.2xlarge 
* r3.xlarge, r3.2xlarge, r3.4xlarge 

You can enable EBS optimization when you launch these instances or after they are running. Instances must have EBS optimization enabled to achieve the level of performance described. When you enable EBS optimization for an instance that is not EBS optimized by default, you pay an additional low, hourly fee for the dedicated capacity. 

#### EBS optimized by default
The following instance types support EBS optimization, and EBS optimization is enabled by default. There is no need to enable EBS optimization, and there is no effect if you disable EBS optimization. These instances include dedicated bandwidth to Amazon EBS. Choose an EBS-optimized instance that provides more dedicated Amazon EBS throughput than your application needs. Otherwise, the connection between Amazon EBS and Amazon EC2 can become a performance constraint.

##### General purpose
These instances offer a balance of compute, memory, and network resources. They are suitable for a wide range of applications, including web servers, code repositories, small to medium databases, development environments, and other workloads with moderate resource requirements. 

For the full list of instance types, see [General Purpose](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html#current-general-purpose).

##### Compute optimized
Compute optimized instances are ideal for compute-bound applications that benefit from high-performance processors. Instances belonging to this family are well suited for the following:
* Batch processing workloads
* Media transcoding
* High-performance web servers
* High performance computing (HPC)
* Scientific modeling
* Dedicated gaming servers and ad server engines
* Machine learning inference
* Other compute-intensive applications

For the full list of instance types, see [Compute Optimized](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html#current-compute-optimized).

##### Memory optimized
These instances are optimized for memory-intensive workloads. Memory optimized instances are designed to deliver fast performance for workloads that process large datasets in memory. They offer a larger memory capacity relative to the CPU resources. Memory optimized instances are well suited for applications that require substantial in-memory data processing, such as real-time big data analytics, in-memory databases, caching fleets, and memory-intensive scientific simulations. 

For the full list of instance types, see [Memory Optimized](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html#current-compute-optimized).

##### Storage optimized
Storage optimized instances are designed for workloads that require high sequential read and write access to very large datasets on local storage. They are optimized to deliver tens of thousands of low-latency, random IOPS to applications. 

They provide a high ratio of storage to compute resources. Storage optimized instances excel in scenarios involving large-scale data processing, distributed file systems, data warehousing, log processing, and other data-intensive applications.

For the full list of instance types, see [Storage Optimized](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html#current-storage-optimized).

##### Accelerated computing
Accelerated computing instances use hardware accelerators, or co-processors, to perform functions, such as floating-point number calculations, graphics processing, or data pattern matching, more efficiently than is possible in software running on CPUs. 

For the full list of instance types, see [Accelerated Computing](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html#current-accelerated-computing).

#### Viewing instance types that support EBS optimization
* To view the instance types that support EBS optimization, and that have it enabled by default, use the following describe-instance-types command:

```
aws ec2 describe-instance-types \
--query 'InstanceTypes[].{InstanceType:InstanceType,"MaxBandwidth(Mb/s)":EbsInfo.EbsOptimizedInfo.MaximumBandwidthInMbps,MaxIOPS:EbsInfo.EbsOptimizedInfo.MaximumIops,"MaxThroughput(MB/s)":EbsInfo.EbsOptimizedInfo.MaximumThroughputInMBps}' \
--filters Name=ebs-info.ebs-optimized-support,Values=default --output=table
```

* To view the instance types that support EBS optimization but do not have it enabled by default, use the following describe-instance-types command:

```
aws ec2 describe-instance-types \
--query 'InstanceTypes[].{InstanceType:InstanceType,"MaxBandwidth(Mb/s)":EbsInfo.EbsOptimizedInfo.MaximumBandwidthInMbps,MaxIOPS:EbsInfo.EbsOptimizedInfo.MaximumIops,"MaxThroughput(MB/s)":EbsInfo.EbsOptimizedInfo.MaximumThroughputInMBps}' \
--filters Name=ebs-info.ebs-optimized-support,Values=supported --output=table
```

#### EBS Volumes with Block Device Mapping

#### Block device mapping concept
A block device mapping defines the block devices (instance store volumes and EBS volumes) to attach to an instance. You can specify a block device mapping as part of creating an AMI, so that the mapping is used by all instances launched from the AMI. Alternatively, you can specify a block device mapping when you launch an instance, so this mapping overrides the one specified in the AMI from which you launched the instance. 

#### Block device mapping entries
When you create a block device mapping, you specify the device name used within Amazon EC2 for each block device that you need to attach to the instance. The block device driver for the instance assigns the actual volume name when mounting the volume. The name assigned can be different from the name that Amazon EC2 recommends.

##### Instance store volumes
For instance store volumes, you also specify the virtual device: ephemeral[0-23]. Note that the number and size of available instance store volumes for your instance varies by instance type.

##### NVMe instance store volumes
NVMe instance store volumes are automatically enumerated and assigned a device name on instance launch, so including them in your block device mapping has no effect.

##### EBS volumes
For EBS volumes, you also specify the following information:
* **The ID of the snapshot to use to create the block device (snap-xxxxxxxx) –** This value is optional if you specify a volume size.
* **The size of the volume, in gibibytes (GiB) –** The specified size must be greater than or equal to the size of the specified snapshot.
* **Whether to delete the volume on instance termination (true or false) –** The default value is true for the root device volume and false for attached volumes. When you create an AMI, its block device mapping inherits this setting from the instance. When you launch an instance, it inherits this setting from the AMI.
* **The volume type –** This can be gp2 and gp3 for General Purpose SSD, io1 and io2 for Provisioned IOPS SSD, st1 for Throughput Optimized HDD, sc1 for Cold HDD, or standard for Magnetic. The default value is gp2.
* **The number of IOPS that the volume supports –** This is used only with io1 and io2 volumes.

#### Amazon Data Lifecycle Manager

#### Automating the snapshot lifecycle
You can use Amazon Data Lifecycle Manager to automate the creation, retention, and deletion of EBS snapshots and EBS-backed AMIs. When you automate snapshot and AMI management, it helps you to do the following:
* Protect valuable data by enforcing a regular backup schedule.
* Create standardized AMIs that can be refreshed at regular intervals.
* Retain backups as required by auditors or internal compliance.
* Reduce storage costs by deleting outdated backups.
* Create disaster recovery backup policies that back up data to isolated accounts.

When combined with the monitoring features of **Amazon EventBridge** and **AWS CloudTrail**, **Amazon Data Lifecycle Manage**r provides a **complete backup solution** for EC2 instances and individual EBS volumes at no additional cost. 

**You can't use Amazon Data Lifecycle Manager to manage snapshots or AMIs that are not created with Amazon Data Lifecycle Manager. Amazon Data Lifecycle Manager cannot be used to automate the creation, retention, and deletion of instance store–backed AMIs.**

#### Amazon Data Lifecycle Manager features
##### Lifecycle policies
Lifecycle policy consists of these core settings:
* **Policy type –** This defines the type of resources that the policy can manage. Amazon Data Lifecycle Manager supports three types of lifecycle policies:
 * **Snapshot lifecycle policy** is used to automate the lifecycle of EBS snapshots. These policies can target EBS volumes and instances.
 * **Cross-account copy event policy** is used to automate the copying of snapshots across accounts. This policy type should be used in conjunction with an EBS snapshot policy that shares snapshots across accounts.
 * **EBS-backed AMI lifecycle policy** is used to automate the lifecycle of EBS-backed AMIs. These policies can target instances only.

* **Resource type –** This defines the type of resources that are targeted by the policy. Snapshot lifecycle policies can target instances or volumes. Use volume to create snapshots of individual volumes, or use instance to create multi-volume snapshots of all of the volumes that are attached to an instance. 
* **Target tags –** The tags that must be assigned to an EBS volume for it to be targeted by the policy.
* **Schedules –** The start times and intervals for creating snapshots or AMIs. The first snapshot or AMI creation operation starts within one hour after the specified start time. Subsequent snapshot or AMI creation operations start within one hour of their scheduled time. 
* **Retention –** This specifies how snapshots are retained. You can retain snapshots based on their total count (count-based) or their age (age-based). 
 * For snapshot policies, when the retention threshold is reached, the oldest snapshot is deleted. 

##### Policy schedules
Policy schedules define when the policy creates a snapshot. 
* Policies can have up to four schedules: one mandatory schedule and up to three optional schedules. 
* By adding multiple schedules to a single policy, you can use the same policy to create snapshots or AMIs at different frequencies. 
 * For example, you can create a single policy that creates daily, weekly, monthly, and yearly snapshots. This eliminates the need to manage multiple policies.
* For each schedule, you can define the frequency, fast snapshot restore settings (snapshot lifecycle policies only), cross-Region copy rules, and tags.
 * The tags that are assigned to a schedule are automatically assigned to the snapshots that are created when the schedule is activated. 
 * In addition, Amazon Data Lifecycle Manager automatically assigns a system-generated tag to each snapshot based on the schedule's frequency.
* Each schedule is activated individually based on its frequency.
 * If multiple schedules are activated at the same time, Amazon Data Lifecycle Manager creates only one snapshot and applies the retention settings of the schedule that has the highest retention period. The tags of all the activated schedules are applied to the snapshot.

##### Quotas
Amazon Data Lifecycle Manager quotas:
* You can create up to 100 lifecycle policies per AWS Region.
* You can add up to 45 tags per resource.

##### Snapshots
Snapshots are the primary means to back up data from your EBS volumes. To save storage costs, successive snapshots are incremental, containing only the volume data that changed since the previous snapshot. When you delete one snapshot in a series of snapshots for a volume, only the data that's unique to that snapshot is removed. The rest of the captured history of the volume is preserved.

##### EBS-backed AMIs
An AMI provides the information that's required to launch an instance. You can launch multiple instances from a single AMI when you need multiple instances with the same configuration. Amazon Data Lifecycle Manager supports EBS-backed AMIs only. EBS-backed AMIs include a snapshot for each EBS volume that's attached to the source instance.

##### Target resource tags
Amazon Data Lifecycle Manager uses resource tags to identify the resources to back up. When you create a snapshot or EBS-backed AMI policy, you can specify multiple target resource tags. All resources of the specified type (instance or volume) that have at least one of the specified target resource tags will be targeted by the policy. For example, if you create a snapshot policy that targets volumes and you specify **purpose=prod**, **costcenter=prod**, and **environment=live** as target resource tags, the policy will target all volumes that have any of those tag-key value pairs.

If you want to run multiple policies on a resource, you can assign multiple tags to the target resource, and then create separate policies that each target a specific resource tag.

You can't use the \ or = characters in a tag key. Target resource tags are case sensitive. 

##### Amazon Data Lifecycle Manager tags
Amazon Data Lifecycle Manager applies the following system tags to all snapshots and AMIs created by a policy, to distinguish them from snapshots and AMIs created by any other means: 
* **aws:dlm:lifecycle-policy-id**
* **aws:dlm:lifecycle-schedule-name**
* **aws:dlm:expirationTime –** For snapshots created by an age-based schedule; indicates when the snapshot is to be deleted from the standard tier
* **aws:dlm:managed**
* **aws:dlm:archived –** For snapshots that were archived by a schedule

You can also specify custom tags to be applied to snapshots and AMIs on creation. You can't use the \ or = characters in a tag key.

The target tags that Amazon Data Lifecycle Manager uses to associate volumes with a snapshot policy can optionally be applied to snapshots created by the policy. Similarly, the target tags that are used to associate instances with an AMI policy can optionally be applied to AMIs created by the policy.

#### Use case: Automating Amazon EBS snapshot management 
The organization’s IT policy might stipulate that EBS snapshots be taken on a specified schedule (hourly, daily, weekly, and so on) to meet business continuity and data protection requirements. In addition, the organization might have compliance guidelines to copy EBS snapshots across AWS Regions, apply prescribed retention policies, and perform regular recovery actions as part of disaster readiness.

With Amazon Data Lifecycle Manager, the need for these complicated and custom scripts to manage EBS snapshots is eliminated. You can use Amazon Data Lifecycle Manager to create, manage, and delete EBS snapshots in a simple, automated way, based on resource tags for EBS volumes or EC2 instances. This reduces the operational complexity of managing EBS snapshots, which saves time and money. 

#### Amazon EBS Fast Snapshot Restore
When you create an EBS volume from an EBS snapshot, data from the EBS snapshot is lazy loaded into an EBS volume. If the volume is accessed where the data is not loaded, the application accessing the volume encounters a higher latency than normal while the data gets loaded. Higher latency because of lazy loading can lead to a poor user experience for latency-sensitive workloads.

Amazon EBS fast snapshot restore (FSR) helps you create a volume from a snapshot that is fully initialized at creation. FSR eliminates the latency of I/O operations on a block when it is accessed for the first time. Volumes that are created using FSR instantly deliver all of their provisioned performance. FSR must be turned on for specific snapshots in specific Availability Zones, and it must be explicitly activated for each snapshot. 

##### Instance launch
When launching a new EC2 instance, you can use FSR to significantly speed up the restoration process. By enabling FSR during instance launch, you can quickly provision new EBS volumes from snapshots. This reduces the time it takes to make your instance operational.

##### Scaling applications
As your applications require additional resources, you might need to scale them by attaching more EBS volumes. With FSR, you can accelerate the restoration of EBS volumes from snapshots, making it easier and faster to scale your applications while minimizing any potential impact on their availability. 

##### Disaster recovery
In the event of a failure or data loss, FSR becomes crucial for rapid recovery. By using snapshots of your EBS volumes, you can restore the data quickly and efficiently to new volumes. This ensures a faster recovery time and minimizes the impact on your business operations. 

##### Database restores
If you are using Amazon Relational Database Service (Amazon RDS) or running a database on EC2 instances with EBS volumes, FSR can speed up the process of restoring databases from snapshots. This can be particularly useful when recovering from accidental data deletion or database corruption, or when creating database clones for testing or analysis purposes.  

#### Considerations
The following are the considerations that you should pay attention to before you use FSR: 
* Fast snapshot restore is not supported with AWS Outposts, AWS Local Zones, or Wavelength Zones. 
* Fast snapshot restore can be enabled on snapshots with a size of 16 tebibytes (TiB) or less. 
* Volumes provisioned with performance up to 64,000 IOPS and 1,000 mebibytes per second (MiBps) throughput receive the full performance benefit of fast snapshot restore. For volumes provisioned with performance greater than 64,000 IOPS or 1,000 MiBps throughput, AWS recommends that you initialize the volume to receive its full performance. 

#### Enabling or disabling FSR
FSR is disabled for a snapshot by default. You can enable or disable FSR for snapshots that you own and for snapshots that are shared with you. When you enable or disable FSR for a snapshot, the changes apply to your account only. 

When you delete a snapshot that you own, FSR is automatically disabled for that snapshot in your account. If you enabled FSR for a snapshot that is shared with you, and the snapshot owner deletes or unshares it, FSR is automatically disabled for the shared snapshot in your account.

If you enabled FSR for a snapshot that is shared with you, and it has been encrypted using a custom AWS Key Management Service (AWS KMS) key, FSR is not automatically disabled for the snapshot when the snapshot owner revokes your access to the custom key. You must manually disable FSR for that snapshot.

You can use one of the following methods to enable or disable FSR for a snapshot that you own or for a snapshot that is shared with you. 

##### Console
Follow these steps to enable or disable fast snapshot restore from the console:
1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).
2. In the left navigation pane, choose **Snapshots**.
3. Select the snapshot, and choose **Actions > Manage fast snapshot restore**.
4. The **Fast snapshot restore settings** section lists all the Availability Zones in which you can enable fast snapshot restore for the selected snapshot. The **Current status** column indicates whether fast snapshot restore is currently enabled or disabled for each zone. To enable fast snapshot restore in a zone where it is currently disabled, select the zone, choose **Enable**, and then choose **Enable** to confirm. To disable fast snapshot restore in a zone where it is currently enabled, select the zone, and then choose **Disable**.
5. After you have made the required changes, choose **Close**.

##### AWS CLI
* [enable-fast-snapshot-restores](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/enable-fast-snapshot-restores.html)
* [disable-fast-snapshot-restores](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disable-fast-snapshot-restores.html)
* [describe-fast-snapshot-restores](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-fast-snapshot-restores.html)

**After you enable fast snapshot restore for a snapshot, it enters the Optimizing state. Snapshots that are in the Optimizing state provide some performance benefits when you use them to restore volumes. They start to provide the full performance benefits of fast snapshot restore only after they enter the Enabled state.**

#### Viewing the FSR state for a snapshot
* *Enabling* – A request was made to enable fast snapshot restore. 
* *Optimizing* – Fast snapshot restore is being enabled. It takes 60 minutes per TiB to optimize a snapshot. Snapshots in this state offer some performance benefit when restoring volumes. 
* *Enabled* – Fast snapshot restore is enabled. Snapshots in this state offer the full performance benefit when restoring volumes. 
* *Disabling* – A request was made to disable fast snapshot restore, or a request to enable fast snapshot restore failed. 
* *Disabled* – Fast snapshot restore is disabled. You can enable fast snapshot restore again as needed. 

##### Console
Follow these steps to view the state of fast snapshot restore from the console:
1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).
2. In the left navigation pane, choose **Snapshots**.
3. Select the snapshot.
4. On the **Details** tab, **Fast snapshot restore** indicates the state of fast snapshot restore.

##### AWS CLI
**To view snapshots with fast snapshot restore enabled by using the AWS CLI**, use the [describe-fast-snapshot-restores](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-fast-snapshot-restores.html) command to describe the snapshots that are enabled for fast snapshot restore.

#### Viewing volumes restored by using FSR
When you create a volume from a snapshot that is enabled for fast snapshot restore in the Availability Zone for the volume, it is restored using FSR. 

Use the describe-volumes command to view volumes that were created from a snapshot that is enabled for fast snapshot restore.

```
aws ec2 describe-volumes --filters Name=fast-restored,Values=true
```

The following is the example output:

```
{
    "Volumes": [
        {
            "Attachments": [],
            "AvailabilityZone": "us-east-2a",
            "CreateTime": "2020-01-26T00:34:11.093Z",
            "Encrypted": true,
            "KmsKeyId": "arn:aws:kms:us-west-2:123456789012:key/8c5b2c63-b9bc-45a3-a87a-5513e232e843",
            "Size": 20,
            "SnapshotId": "snap-0e946653493cb0447",
            "State": "available",
            "VolumeId": "vol-0d371921d4ca797b0",
            "Iops": 100,
            "VolumeType": "gp2",
            "FastRestored": true
        }
    ]
}
```

#### Fast snapshot restore quotas
You can enable up to five snapshots per Region for fast snapshot restore. The quota applies to snapshots that you own and snapshots that are shared with you. If you enable fast snapshot restore for a snapshot that is shared with you, it counts towards your fast snapshot restore quota. It does not count toward the snapshot owner's fast snapshot restore quota. 

#### Pricing and billing
You are billed for each minute that fast snapshot restore is enabled for a snapshot in a particular Availability Zone. Charges are prorated with a minimum of one hour.

For example, if you enable fast snapshot restore for one snapshot in us-east-1a for one month (30 days), you are billed $540 (1 snapshot x 1 AZ x 720 hours x $0.75 per hour). If you enable fast snapshot restore for two snapshots in us-east-1a, us-east-1b, and us-east-1c for the same period, you are billed $3240 (2 snapshots x 3 AZs x 720 hours x $0.75 per hour).

If you enable fast snapshot restore for a public or private snapshot that is shared with you, your account is billed; the snapshot owner is not billed. When a snapshot that is shared with you is deleted or unshared by the snapshot owner, fast snapshot restore is disabled for the snapshot in your account and billing is stopped.

##### [Amazon EBS pricing](https://aws.amazon.com/ebs/pricing/)

#### Amazon EBS Direct APIs
You can use the Amazon EBS direct APIs to create Amazon EBS snapshots, write data directly to your snapshots, read data on your snapshots, and identify the differences or changes between two snapshots. 

You can create incremental snapshots directly from data on premises into volumes and the cloud to use for quick disaster recovery. With the ability to write and read snapshots, you can write your on-premises data to a snapshot during a disaster. Then, after recovery, you can restore it back to AWS or on premises from the snapshot. You no longer need to build and maintain complex mechanisms to copy data to and from Amazon EBS.

#### Key elements
##### Snapshots
Snapshots are the primary means to back up data from your EBS volumes. With the EBS direct APIs, you can also back up data from your on-premises disks to snapshots. To save storage costs, successive snapshots are incremental, containing only the volume data that changed since the previous snapshot. 

##### Blocks
A block is a fragment of data within a snapshot. Each snapshot can contain thousands of blocks. All blocks in a snapshot are a fixed size. 

##### Block indexes
A block index is a logical index in units of 512 KiB blocks. To identify the block index, divide the logical offset of the data in the logical volume by the block size (logical offset of data / block size). 

The logical offset of the data must be 512 KiB aligned. This means that the logical offset of the data starts at an address that is evenly divisible by 512KiB. 

##### Block tokens
A block token is the identifying hash of a block within a snapshot, and it is used to locate the block data. Block tokens returned by EBS direct APIs are temporary. They change on the expiry timestamp specified for them, or if you run another **ListSnapshotBlocks** or **ListChangedBlocks** request for the same snapshot.

##### Checksum
A checksum is a small-sized block of data derived from another block of data for the purpose of detecting errors that were introduced during its transmission or storage. 

The EBS direct APIs use checksums to validate data integrity. When you read data from an EBS snapshot, the service provides Base64-encoded SHA256 checksums for each block of data transmitted, which you can use for validation. When you write data to an EBS snapshot, you must provide a Base64 encoded SHA256 checksum for each block of data transmitted. The service validates the data received using the checksum provided.

##### Encryption
Encryption protects your data by converting it into unreadable code that can be deciphered only by people who have access to the AWS KMS key used to encrypt it. You can use the EBS direct APIs to read and write encrypted snapshots, but there are some limitations.

##### API actions
The EBS direct APIs consist of six actions: three read actions and three write actions. The read actions are as follows:
* **ListSnapshotBlocks**: This returns the block indexes and block tokens of blocks in the specified snapshot.
* **ListChangedBlocks**: This returns the block indexes and block tokens of blocks that are different between two specified snapshots of the same volume and snapshot lineage.
* **GetSnapshotBlock**: This returns the data in a block for the specified snapshot ID, block index, and block token.

The write actions are as follows:
* **StartSnapshot**: This starts a snapshot, either as an incremental snapshot of an existing one or as a new snapshot. The started snapshot remains in a pending state until it is completed using the **CompleteSnapshot** action.
* **PutSnapshotBlock**: This adds data to a started snapshot in the form of individual blocks. You must specify a Base64-encoded SHA256 checksum for the block of data transmitted. The service validates the checksum after the transmission is completed. The request fails if the checksum computed by the service doesn’t match what you specified.
* **CompleteSnapshot**: This completes a started snapshot that is in a pending state. The snapshot is then changed to a completed state.

#### Using interface VPC endpoints with EBS direct APIs
To reduce network data transfer costs, you can establish a private connection between your VPC and EBS direct APIs by creating an interface VPC endpoint, powered by AWS PrivateLink. You can access EBS direct APIs as if they were in your VPC, without using an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. Instances in your VPC don't need public IP addresses to communicate with EBS direct APIs.

AWS creates an endpoint network interface in each subnet that you can enable for the interface endpoint.

**VPC endpoint policies are not supported for EBS direct APIs. By default, full access to EBS direct APIs is permitted through the endpoint. However, you can control access to the interface endpoint by using security groups.**

#### Creating an interface VPC endpoint for EBS direct APIs
You can create a VPC endpoint for EBS direct APIs by using either the Amazon Virtual Private Cloud (Amazon VPC) console or the AWS CLI.
1. **Open the VPC console**. You can open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/). You can also log in to the AWS Management Console, and then search for VPC in the search box.
2. **Create the endpoint**. In the left navigation pane, choose **Endpoints**, and then choose **Create endpoint**.
3. **Select the service category**. For **Service category**, select **AWS services**.
4. **Select the service name and VPC**. For Service name, select **com.amazonaws.<region>.ebs**. For **VPC**, select the default vpc.
5. **Select the security group**. For **Security groups**, select the default VPC security group, and then choose **Create endpoint**. If you enable private DNS for the endpoint, you can make API requests to EBS direct APIs by using its default DNS name for the Region (for example, ebs.us-east-1.amazonaws.com).

#### Amazon EBS Service Quotas
Your quotas can change over time. Amazon EBS constantly monitors your provisioned storage and IOPS usage within each Region, and it might automatically increase your quotas, on a per-Region basis, based on your usage.

Even though Amazon EBS automatically increases your quotas based on your usage, you can request a quota increase if needed. For example, if you intend to use more gp3 storage in US East (N. Virginia) than your current quota permits, you can request a quota increase for that volume type in that Region.

##### Considerations
* The quota for **Concurrent snapshot copies per destination Region** is not adjustable by using the Service Quotas console. However, you can request an increase for this quota by contacting AWS Support. 
* The **IOPS modifications and Storage modifications** quotas apply to the aggregated current value (for size or IOPS, depending on the quota) of volumes that can undergo modifications concurrently. You can make concurrent modification requests for volumes that have combined current value (for size or IOPS) up to the quota. For example, if your **IOPS modifications for Provisioned IOPS SSD (io1) volumes** quota is 50,000, you can make concurrent IOPS modifications requests for any number of io1 volumes if their combined current IOPS is equal to or less than 50,000. If you have three io1 volumes provisioned with 20,000 IOPS each, you can request IOPS modifications for two volumes concurrently (20,000 * 2 < 50,000). If you submit a concurrent IOPS modification request for the third volume, you exceed your quota and that request fails (20,000 * 3 > 50,000).

To view the quotas for your Amazon EBS resources, open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/). In the left navigation pane, choose **AWS services**, and choose **Amazon Elastic Block Store (Amazon EBS)**. 

##### [Full list of Amazon EBS service quotas](https://docs.aws.amazon.com/general/latest/gr/ebs-service.html#limits_ebs)

#### Cost Optimization Tips
##### Rightsizing

#### Scaling cost-effective architectures

##### Tip #1: Delete unused EBS volumes.
Unused and overlooked Amazon EBS volumes contribute to AWS costs. The lifecycle of EBS volumes can be independent of Amazon EC2 compute instances. Therefore, even if the EC2 instance associated with the EBS volumes is terminated, the EBS volumes tend to persist unless you select the **Delete on Termination** option at launch.

Also, instances spun up and down as part of development and testing cycles might leave orphaned EBS volumes if there are no workflows in use to delete them automatically.

These orphaned EBS volumes accrue charges while unattached.

##### Tip #2: Avoid provisioning EBS volumes larger than required.
You are billed based on the provisioned capacity for your EBS volumes per gigabyte per month (GB-month). What has been discovered from AWS customer experiences is that often in test and development environments, volumes are created that are much larger than required in the production environment. For many organizations that are new to AWS, and are accustomed to on-premises solutions, their developers will size volumes based on anticipated future requirements. You pay for this extra provisioned capacity every month. 
* For example, say you have 100 gp3 volumes that are sized at 2,000 GB each, and each volume actually only requires 150 GB of capacity for your data. Your cost savings opportunity in the US East (Ohio) Region is approximately $14,800 just in provisioned capacity costs. 

*Example pricing for gp3 in the US East (Ohio) Region is $0.08/GB-month as of August 22, 2023. Pricing for services can vary by AWS Region and is subject to change without notice.*

##### Tip #3: Avoid oversizing provisioned performance options.
Similar to provisioned capacity, you are billed for provisioned performance for some EBS volume types. Other EBS volume types scale performance by increasing the volume size. In both situations, if you provision performance above what you require, you are unnecessarily increasing your costs.
* gp3, io1, and io2 and io2 Block Express EBS volume types include a performance option to increase the IOPS performance without increasing the provisioned volume capacity. IOPS performance provisioning is subject to minimum IOPS-to-capacity ratios per volume type.
* The gp3 EBS volume type also includes the capability to change the throughput performance without increasing the provisioned volume capacity. Throughput performance provisioning is subject to a minimum throughput-to-IOPS performance ratio.
* gp2, st1, and sc1 EBS volume types scale performance by increasing provisioned capacity.

Scaling up provisioned performance in all cases increases the cost of your EBS volumes. You can scale up both provisioned performance and provisioned capacity dynamically with Amazon EBS Elastic Volumes. You can also scale down provisioned performance dynamically with Elastic Volumes.

##### Tip #4: Use newer EBS volume types.
One of the biggest cost savings opportunities is to move to newer volume types within the same EBS volume type category. Newer volume types either offer lower base pricing or the capability to provision less capacity and still meet your performance goals.

AWS continues to innovate and release new EBS volume types. For the General Purpose volume types, gp3 volumes are newer than the gp2 volumes, which are still available. For Provisioned IOPS performance volume types, io2 and io2 Block Express are newer than the io1 volume type that you can still have provisioned. See the following examples:
* gp3 volume pricing is approximately 20 percent less than gp2 volume pricing, per provisioned GB of capacity. Even if you do nothing else, you can save 20 percent by dynamically changing your volume type from a gp2 to a gp3 volume type.
* gp3 volumes include a performance baseline of 3,000 IOPS and 125 megabytes per second (MBps) throughput. To achieve 3,000 baseline IOPS with gp2 volumes, you would need to provision 1,000 GB of capacity. With gp3 volumes, you can provision as little as 1 GB of capacity and reach your 3,000 IOPS performance goal.
* For io1 and io2 volume types, the difference is in the ratio of the number of IOPS that you can provision per GB of volume capacity. io1 volumes have a ratio of 50:1, or 50 IOPS per 1 GB of provisioned capacity. io2 volumes have a 500:1 ratio. You can provision 10 times the IOPS per GB of provisioned capacity with io2 volumes. In addition, io2 volumes offer a decreasing, tiered pricing structure for higher provisioned IOPS levels. io2 Block Express volumes have a 1,000:1 ratio for applicable workloads and using supported EC2 instance types.

When you dynamically migrate to a newer volume type, your previous provisioned capacity remains the same. To lower the volume size, you need to create new volumes and migrate your data to them. Lowering the provisioned capacity assumes that you can use less space for your actual data.

You will benefit from lower pricing if the new provisioned volume capacity price per GB-month or cost per IOPS per month (IOPS-month) is lower. 

##### Tip #5: Use lower-cost EBS volume types.
In some cases, new volume types in a different category can provide a better cost per month, while meeting your performance requirements. Before the gp3 volume type was available, scaling gp2 volumes to meet high IOPS performance required provisioning large volumes. The same difference applies to io1 and io2 volumes. With io2 volumes, you can provision 500 IOPS per GB. With io1 volumes, you can only provision 50 IOPS per GB.

In many use cases, gp3 volumes can be used in place of io1 or io2 volumes to meet your capacity and performance requirements. The pricing is lower for gp3 volumes than for io1 or io2 volumes for both capacity and provisioned IOPS.

If a lower-cost EBS volume type will meet your requirements, you can dynamically change volume type by using Elastic Volumes. 

##### Tip #6: Delete unused snapshots.
You can back up your data to Amazon S3 by using snapshots. But snapshots are often forgotten, resulting in a $0.05 per GB-month unwanted additional spending. As part of your financial management, an optimization routine should review all snapshots and delete those that are no longer required.

For example, a snapshot that is no longer required might be related to older-than-relevant data or unused AMIs.

You can use Amazon Data Lifecycle Manager for managing the creation, retention, and deletion of EBS snapshots. In addition to reducing storage costs by deleting outdated backups, you can protect valuable data by enforcing a regular backup schedule. Read the [Automating Amazon EBS Snapshots Management Using Data Lifecycle Manager](https://aws.amazon.com/blogs/storage/automating-amazon-ebs-snapshots-management-using-data-lifecycle-manager/) blog post for a walkthrough.

You can also use AWS Backup to manage backups over the whole suite of AWS storage and database services. 

##### Tip #7: Consider archiving Amazon EBS snapshots.
Use Amazon EBS Snapshots Archive to create archival snapshots. Amazon EBS Snapshots Archive offers you a lower price per GB compared to standard EBS snapshots. The storage tier is intended for long-term storage of your rarely accessed snapshots that do not need frequent or fast retrieval.

The following are some typical use cases: 
* Archiving the only snapshot of a volume, such as end-of-project snapshots 
* Archiving full, point-in-time incremental snapshots for compliance reasons
* Archiving monthly, quarterly, or yearly incremental snapshots

##### Tip #8: Use AWS Backup to create backup copies of your data.
Use AWS Backup to create backup copies of your data to maintain archival data copies instead of keeping additional snapshots. With AWS Backup, you can create and maintain archive policies to manage your backups that meet your archive or compliance requirements. You can tier your backups to lower-cost storage tiers to save costs.

##### Tip #9: Use AWS Compute Optimizer for EBS volume recommendations.
AWS Compute Optimizer supports IOPS and throughput recommendations for General Purpose (SSD) (gp3) volumes, and IOPS recommendations for Provisioned IOPS (io1 and io2) volumes.  

AWS Compute Optimizer uses Amazon CloudWatch metrics to analyze your EBS volumes and provide recommendations to assist you in optimizing your Amazon EBS costs.

#### Knowledge Check
##### A company is working with a developer in planning to migrate their database workload to the cloud. The database being migrated is I/O intensive and sensitive to storage performance and consistency. Which Amazon Elastic Block Store (Amazon EBS) volumes would best fit their needs? 
* Volumes backed by io2 Provisioned IOPS SSDs

io2 Provisioned IOPS SSD volumes are designed to meet the needs of I/O-intensive workloads, particularly database workloads, that are sensitive to storage performance and consistency. 

The other options are incorrect because of the following:
* gp2 and gp3 General Purpose SSDs are adequate for general use, but they are not optimal for I/O-intensive databases.
* st1 Throughput Optimized HDD-backed volumes are best suited as storage volumes for large, sequential workloads such as Amazon EMR or log processing. HDD-backed volumes are not ideal for database workloads.

##### What happens to a root volume instance store when the Amazon EC2 instance is stopped? 
* The instance store data is deleted.

Stopping and terminating instances are different operations. When you stop an instance, AWS shuts it down. When you terminate an instance, AWS permanently deletes it. However, when using an instance store, when you stop the instance, the data on the root device vanishes and cannot be recovered.

##### Which offering can you use to reduce the latency on volumes restored from snapshots? 
* Amazon Elastic Block Store (Amazon EBS) fast snapshot restore (FSR)

Enable FSR on a snapshot to ensure that the Amazon EBS volumes created from it are fully initialized at creation and instantly deliver all their provisioned performance.

#### Amazon EFS Features and Configurations

#### Pre-assessment
##### Which throughput mode is the default for Amazon Elastic File System (Amazon EFS) and is recommended for most workloads? 
* Elastic Throughput

The other options are incorrect because of the following: 
* General Purpose and Max I/O are performance modes, not throughput modes.
* Provisioned Throughput is recommended for workloads requiring higher throughput-to-storage ratios.

##### Amazon Elastic File System (Amazon EFS) offers two storage class types, each with its own subtypes. What are these storage class types? (Select TWO.) 
* EFS Standard 
* EFS One Zone 

The other options are incorrect because General Purpose, Elastic Throughput, and Max I/O are performance and throughput modes.

##### A consultant is working with a client that has spiky and unpredictable workloads that have been difficult to accurately forecast. Which Amazon Elastic File System (Amazon EFS) throughput mode would be most suitable for the customer’s needs? 
* Elastic Throughput

Elastic Throughput is the default throughput mode. Use this mode when there are spiky or unpredictable workloads and performance requirements that are difficult to forecast. It is also recommended for use when an application drives throughput at an average-to-peak ratio of 5 percent or less.

The other options are incorrect because of the following: 
* Bursting Throughput is recommended for workloads that require performance to scale with the amount of data stored on the file system. 
* Provisioned Throughput is recommended for workloads requiring higher throughput-to-storage ratios.
* Max I/O is a performance mode that is recommended for workloads that must scale to higher levels of aggregate throughput and IOPS.

#### Setting Up Amazon EFS

#### Creating a file system
The quickest way to create an Amazon EFS file system is to use the quick creation option. On the **Create file system** window, choose the **Create** button to generate the file system. This option uses the most common default settings to create your file system. 

After you create the file system, you can customize the file system's settings with the exception of availability and durability, encryption, and performance mode. 

##### Default recommended settings
Choose **Create** to create a file system that uses the following service recommended settings:
* Automatic backups enabled
* Mount targets configured with the following settings:
 * Created in each Availability Zone in the AWS Region in which the file system is created
 * Located in the default subnets of the VPC you selected
 * Using the VPC's default security group – You can manage security groups after the file system is the created
* Standard storage class 
* General Purpose performance mode 
* Elastic Throughput mode
* Encryption of data at rest enabled using your default key for Amazon EFS (aws/elasticfilesystem)
* Lifecycle Management – Amazon EFS creates the file system with the following lifecycle policies:
 * **Transition into IA** set to **30 days since last access**
 * **Transition out of IA** set to **None**

 Use the **Customize** option when you create a file system. 

#### Amazon EFS console

##### Amazon EFS console landing page
The Amazon EFS console landing page appears when you search for and choose **EFS** from the AWS Management Console. If you have created file systems previously, the File systems page appears. You can always navigate back to the landing page from other pages in the EFS console.

On the EFS console, you can do the following: 
* By opening the drop-down menu, you can choose the AWS Region to create your EFS file system in.
* You can go to the **File systems** or **Access points** pages by using the navigation menu.
You can launch the **Create file system** window directly from the landing page.
You can also launch the AWS Pricing Calculator and learn more about pricing from the landing page.

##### File systems page
On the **File systems** page, you can launch the **Create file system** window, navigate to the **Access points** page, or view file systems that you have previously created. 
* Choose **Create file system** to begin creating your EFS files system. You have two available buttons that you can choose from: **Customize** or **Create**, as shown in the first screenshot in this section.
* Choose **Access points** to create access points to existing EFS file systems.

#### Amazon EFS custom file system creation 
With custom creation, you can select options other than defaults and configure additional settings during the configuration process. From the **Create file system** window, choose the **Customize** button, and the **File system settings** page opens. 

#### Available custom configuration options
##### Name the file system (optional)
You can name your file system here. This is optional and can be added later if you want.

##### Select storage class
You can select **Standard** for a Standard Multi-AZ file system or **One Zone** for a Single-AZ storage class system. 

**After you create your file system, this setting cannot be modified.**

##### Set up automatic backups
You can change the automatic backup setting here, or you can change it later after your file system has been created.

##### Set up lifecycle management
You can remove or modify the EFS Intelligent-Tiering lifecycle management setting. You can modify these settings later if you want. 

You can choose from the **Transition into IA** and **Transition out of IA** options. 

You can select **None** for both options to turn off lifecycle management.

##### Customize encryption settings
The default is to turn on encryption of data at rest. You can turn encryption off by clearing that check box. 

When the encryption of data at rest is kept at the default, Amazon EFS uses the AWS Key Management Service (AWS KMS) managed key for encryption. You can change the encryption key to a customer managed key that you have already created, or you can create a new customer managed key.

**Encryption settings cannot be modified after file system creation.**

##### Choose throughput mode
You can choose the throughout mode that you want for your file system: Enhanced or Bursting.

If you select **Enhanced**, you will have the additional selection of **Elastic** and **Provisioned** modes to choose from. 

Throughput mode and its settings can be modified after file system creation. 

##### Choose performance mode
You can use the default General Purpose performance mode or select the Max I/O performance mode. Note that the Max I/O can only be selected if you have **Bursting** mode selected in the **Throughput mode** section. 

**After you create your file system, this setting cannot be modified.**

##### Manage optional tags
You can add optional tags for file system identification or file system management. You can add or remove tags later if you want.

#### Network access and mount target configuration 
You can modify or customize your network access and customize your mount target configuration before creating your file system. If you want to use settings other than the default settings, modifying the settings is recommended by AWS.

#### Available configuration options
##### Choose the VPC
Because your file system has not yet been created, you can change the VPC that you want to use. The chosen VPC will modify the available subnets and default security groups to associate with the network configuration.

##### Manage Availability Zones
By default, Amazon EFS will attempt to create mount targets in each Availability Zone in your chosen AWS Region. For One Zone file systems, you can choose your Availability Zone. 

You can remove an Availability Zone if you want. 

##### Choose subnets
The subnets in the Availability Zones are available for you to select. You can create any number of subnets in an Availability Zone. Amazon EFS defaults to the default subnet for the Availability Zone.

##### Configure IP addresses
The private IP address for your mount targets is generated automatically by default when you create your file share. 

You can manually add an available IP address from the subnet range. 

##### Choose security groups
Amazon EFS uses the default security group. You can choose to use different security groups. The security group must be available for the VPC that you choose.

##### Add mount target
With the **Add mount target** option, you can add additional Availability Zones for mount targets. By default, this option is unavailable because Amazon EFS creates a mount target in each Availability Zone. However, if you have removed one of the Availability Zones, you can choose to add it back into the configuration. 

Only one mount target is permitted in an Availability Zone.

#### Creating a user-configured file system policy – optional 
Amazon EFS uses the default EFS file system policy to grant full access to any client that can connect to the file system by using a file system mount target. During the custom configuration process, you are presented with a policy editor to create user-configured policies.

##### Built-in policy options
The policy editor includes some options to streamline policy creation, including some of the most common policies to restrict access to your EFS file system.

##### Policy editor
Your policy is built as you select from the available options. In addition, you can customize the policy as needed. 

If you remove all the options, the policy returns to the default policy. 

##### Additional permissions
You can also grant permissions to additional AWS Identity and Access Management (IAM) principals. You can choose the level of access that you want to grant to the principal.

#### Scaling Amazon EFS file systems 
Amazon EFS file systems can automatically scale storage capacity and throughput as you add files and directories. Amazon EFS provides elastic scaling, which means that the file system can automatically grow and shrink as you add or remove data. There is no need to provision or manage storage capacity in advance.

#### Scaling behavior options
##### Performance mode
Amazon EFS offers two performance modes: General Purpose and Max I/O. General Purpose is the default mode, and it provides a balance between price and performance. Max I/O mode is designed for applications that require higher levels of throughput. Choosing the appropriate performance mode can impact the scaling behavior because applications can scale their IOPS elastically up to the limit associated with the performance mode. 

##### Throughput modes
By default, Amazon EFS file systems are built to provide throughput that scales with the amount of storage in your file system and supports bursting to higher levels for up to 12 hours a day.

Amazon EFS offers three throughput modes: Elastic, Provisioned, and Bursting. 

Use Elastic Throughput if you’re unsure of your application’s peak throughput needs. With Elastic Throughput, performance automatically scales with your workload activity, and you only pay for the throughput that you use. 

Use Provisioned Throughput if you know your workload’s peak throughput requirements and you expect your workload to consume a higher share of your application’s peak throughput capacity. Provisioned Throughput is designed to offer the highest levels of throughput consistency while providing a predictable billing experience.

Use Bursting Throughput when you want throughput that scales with the amount of storage in your file system.

##### Amazon EFS burst credits
In the Bursting Throughput mode, your file system accumulates burst credits during periods of low activity. These credits are then used for your file system to burst to higher throughput levels during peak periods. The amount of burst credits accumulated depends on the size of your file system. Ensuring sufficient burst credits can help maintain consistent performance during peak workloads.

#### Migrating On-Premises Data to Amazon EFS

#### AWS DataSync
DataSync is an online data transfer service that you can use to copy data between the following:
* On-premises Network File System (NFS) file servers
* Server Message Block (SMB) file servers
* Hadoop Distributed File System (HDFS) storage
* Self-managed object storage
* AWS storage services in the AWS Cloud - Amazon EFS is one of the AWS services supported by DataSync

##### On-premises and AWS Storage
You can use DataSync to transfer files between your on-premises NFS servers and Amazon EFS. Your on-premises NFS servers can be used as a source location or can be a destination location to support your copy transfer workflows.

##### Between AWS Storage services
You can also use DataSync to transfer data between Amazon EFS file systems in the same AWS Region, between Regions, or even between AWS accounts. 

Using DataSync to copy data between EFS file systems, you can perform one-time data migrations, periodic data ingestion for distributed workloads, and automatic replication for data protection and recovery.

With DataSync, you create scheduled or one-time tasks to copy data from your source location to your destination location. Tasks are single-direction data copies of files. DataSync includes robust features to meet your data copy requirements.

**When you use DataSync to copy files or objects between AWS Regions, you pay for data transfer between Regions. This is billed as data transfer out from your source Region to your destination Region.**

#### DataSync configuration 
All of the configuration to access your EFS file systems is performed within the DataSync service. You select your EFS file system as a source or destination location when you configure your DataSync tasks. To configure DataSync, you have three areas of focus: agents, locations, and tasks.

##### Creating an agent
For DataSync to access your self-managed storage, whether on premises or in the cloud, you need a DataSync agent associated with your AWS account.

You have a choice of agents depending on your environment. Where you deploy your DataSync agent depends on where you're copying data to and from, and whether you're working with on-premises or in-cloud storage systems.

An agent isn't required when transferring between AWS storage services in the same AWS account.

##### Configuring source and destination locations
A task consists of a pair of locations that data will be transferred between. The source location defines the storage system or service that you want to read data from. The destination location defines the storage system or service that you want to write data to.

The source and destination location are based on the task. A task copies data in a single direction from source to destination. To copy data in both directions requires two tasks. Each location would be a source in one task and a destination in the other task.

You configure source and destination locations in the DataSync console.

##### Configuring tasks
After you create a DataSync agent and configure the source and destination locations, you can configure the settings for a new task. A task is a set of two locations—source and destination—and a set of options that you use to control the behavior of the task.

You configure task settings when creating a new task in the DataSync console.

##### [Creating an agent](https://docs.aws.amazon.com/datasync/latest/userguide/configure-agent.html)

##### [Working with agents](https://docs.aws.amazon.com/datasync/latest/userguide/working-with-agents.html)

##### [Configuring a source location](https://docs.aws.amazon.com/datasync/latest/userguide/configure-source-location.html)

##### [Configuring a destination location](https://docs.aws.amazon.com/datasync/latest/userguide/create-destination-location.html)

##### [Working with locations](https://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)

##### [Creating your DataSync task](https://docs.aws.amazon.com/datasync/latest/userguide/creating-task.html)

##### [Working with AWS DataSync tasks](https://docs.aws.amazon.com/datasync/latest/userguide/working-with-tasks.html)

#### AWS Transfer Family
Transfer Family is a fully managed AWS service that you can use to transfer files into and out of Amazon EFS file systems over the Secure File Transfer Protocol (SFTP), File Transfer Protocol (FTP), and FTP over Secure Sockets Layer (FTPS) protocol. 

Using Transfer Family, you can provide your users, customers, and business partners with access to files stored in your Amazon EFS file systems for use cases such as data distribution, supply chain, content management, and web serving applications.

#### Transfer Family configuration overview
* Transfer Family supports using Amazon EFS to store your data. If you want Amazon EFS to service your users' transfer requests, you must provide an Amazon EFS file system as part of setting up your file transfer protocol–enabled server. You can use an existing file system or you can create a new one. 
* When you use a Transfer Family server and an Amazon EFS file system, the server and the file system must be in the same AWS Region. The Transfer Family server and the file system don't need to be in the same AWS account. If the server and file system are not in the same account, the file system policy must give explicit permission to the user role. 
* When you create a user, you make several decisions about user access. These decisions include which Amazon EFS file systems the user can access, which files in the file system are accessible, and what permissions the user has.
* To set access permissions, you create an identity-based IAM policy and role that provide that access information. As part of this process, you provide access for your user to the Amazon EFS file system that is the target or source for file operations.

##### [Configuring Amazon EFS to work with AWS Transfer Family](https://docs.aws.amazon.com/efs/latest/ug/using-aws-transfer-integration.html#config-efs-aws-transfer-int)

#### Securing Access to Amazon EFS
You can control what network resources have access to your file systems by using Amazon Virtual Private Cloud (Amazon VPC) routing and security group firewall rules. You can further control user and application access to your file systems by using AWS Identity and Access Management (IAM) policies and Amazon EFS access points.

#### Security groups
Both an Amazon EC2 instance and a mount target have associated security groups. These security groups act as virtual firewalls that control the traffic between them. If you don't provide a security group when you create a mount target, Amazon EFS associates the default security group of the virtual private cloud (VPC) with it. 

To enable traffic between an EC2 instance and a mount target (and thus the file system), you must configure the following rules in these security groups:
* The security group that is associated with a mount target must allow inbound access for the TCP protocol on port 2049 for NFS. The NFS port is from all EC2 instances that users want to mount the file system on.
* Each EC2 instance that mounts the file system must have a security group that permits outbound access to the mount target on TCP port 2049. Remember that security groups are stateful, so responses to allowed inbound traffic are allowed to flow outbound regardless of outbound rules, and the opposite is also true.

#### Create a security group that is associated with a mount target
1. **Open the EC2 console**. On the AWS Management Console, in the **Search** box, search for and choose **EC2**.
2. **Choose the security groups**. In the left navigation pane, under **Network & Security**, choose **Security Groups**.
3. **Create a new security group**. In the upper-right corner of the page, choose **Create security group**.
4. **Update security group details**. On the **Create security group** page, in the **Basic details** section, update the **Security group name**, **Description**, and **VPC** fields as needed.
5. **Add inbound rules**. In the Inbound rules section, choose **Add rule** and then adjust the following settings:
 * For **Type**, choose **NFS**.
  * Notice that Protocol **TCP** and Port range **2049** are entered automatically.
 * For **Source**, choose **Custom**. The security group in the **Source** search box is the security group associated with the EC2 instance.
 * Keep the remaining default values.
8. **Confirm and create the security group**. At the bottom of the page, choose **Create security group**.
9. **Summary**. The security group created in this process allows inbound NFS connections on port 2049, but only from resources in the specified security group. To view the security groups associated with your file systems mount targets in the EFS console, choose the **Network** tab on the **File system details** page. For more information, see [Creating and Managing Mount Targets and Security Groups](https://docs.aws.amazon.com/efs/latest/ug/accessing-fs.html).

#### File system policies
You can create a file system policy by using the Amazon EFS console or by using the AWS Command Line Interface (AWS CLI). You can also create a file system policy programmatically by using AWS SDKs or the Amazon EFS API directly. EFS file system policies have a 20,000-character limit.

The default EFS file system policy does not use IAM to authenticate, and grants full access to any anonymous client that can use a mount target to connect to the file system. 

The default policy is in effect whenever a user-configured file system policy is not in effect, including at file system creation. Whenever the default file system policy is in effect, a **DescribeFileSystemPolicy** API operation returns a **PolicyNotFound** response.

#### Creating a file system policy
1. **Open the EFS console**. On the AWS Management Console, in the **Search** box, search for and choose **EFS**.
2. **Open the file systems page**. In the left navigation pane, choose **File systems**.
3. **Choose the file system**. On the **File systems** page, choose the file system that you want to edit or create a file system policy for.
4. **Edit the file system policy**. Choose the **File system policy** tab, and then choose **Edit**. The **File system policy** page appears.
5. **Review policy options**. In **Policy options**, you can select any combination of the preconfigured file system policies:
 * **Prevent root access by default** – This option removes *ClientRootAccess* from the set of allowed EFS actions.
 * **Enforce read-only access by default** – This option removes *ClientWriteAccess* from the set of allowed EFS actions.
 * **Prevent anonymous access** – This option removes *ClientMount* from the set of allowed EFS actions.
 * **Enforce in-transit encryption for all clients** – This option denies access to unencrypted clients.
  * When you choose a preconfigured policy, the policy JSON object is displayed in the **Policy editor** pane.
6. **Grant additional permissions**. 
 * Use **Grant additional permissions** to grant file system permissions to additional IAM principals, including another AWS account. 
 * Choose **Add**, and enter the principal Amazon Resource Name (ARN) of the entity that you are granting permissions to. 
 * Then expand the **Permissions** drop-down list to choose the permissions that you want to grant. The additional permissions are shown in the **Policy editor**.
7. **Customize a preconfigured policy**.
 * You can use the **Policy editor** to customize a pre-configured policy or to create your own file system policy. 
 * When you use the editor, the pre-configured policy options become unavailable. 
 * To clear the current file system policy and start creating a new policy, choose **Clear**.
8. **Clear the policy editor**. When you clear the editor, the pre-configured policies become available once again. After you complete editing the policy, choose **Save**.

#### Amazon EFS Lifecycle Management
Amazon EFS lifecycle management automatically manages cost-effective file storage for your file systems. When enabled, lifecycle management migrates files that have not been accessed for a set period of time to the EFS Standard–Infrequent Access (EFS Standard-IA) or EFS One Zone–Infrequent Access (EFS One Zone-IA) storage class, depending on your file system. You define that period of time by using the Transition into IA lifecycle policy. 

Whenever a file in Standard or One Zone storage is accessed, the lifecycle management timer is reset. After lifecycle management moves a file into one of the Infrequent Access (IA) storage classes, the file remains there indefinitely if Amazon EFS Intelligent-Tiering is not enabled.

Lifecycle management applies to all files in the file system.

#### Amazon EFS Intelligent-Tiering
Amazon EFS Intelligent‐Tiering uses lifecycle management to monitor the access patterns of your workload. It is designed to automatically transition files to and from the file system's IA storage class. 

With EFS Intelligent-Tiering, files in the EFS Standard or EFS One Zone storage classes that are not accessed for the duration of the Transition into IA lifecycle policy setting, for example 30 days, are transitioned to the corresponding IA storage classes.

Additionally, if access patterns change, EFS Intelligent‐Tiering automatically moves files back to the EFS Standard or EFS One Zone storage classes when the Transition out of IA lifecycle policy is set to On first access. This helps to reduce the risk of unbounded access charges, while providing consistent low latencies.

#### Using lifecycle policies
Amazon EFS supports two lifecycle policies: **Transition into IA** and **Transition out of IA**.

##### Transition into IA
Transition into IA instructs lifecycle management when to transition files into the file system's Infrequent Access storage class. 

The Transition into IA lifecycle policy has the following values:
* None
* 1 day since last access
* 7 days since last access
* 14 days since last access
* 30 days since last access
* 60 days since last access
* 90 days since last access

##### Transition out of IA
Transition out of IA instructs EFS Intelligent-Tiering when to transition files out of IA storage. 

The Transition out of IA lifecycle policy can have the following values:
* None
* On first access

When you use the console to create an Amazon EFS file system that uses the service recommended settings, the file system's lifecycle policies use the following default settings: 
* Transition into IA is set to 30 days since last access.
* Transition out of IA is set to None. 

#### Using the console to manage lifecycle policies on an existing file system
You can use the following steps to set the lifecycle policies for an existing file system. 
1. Sign in to the AWS Management Console and open the Amazon EFS console at [https://console.aws.amazon.com/efs/](https://console.aws.amazon.com/efs/).
2. Choose **File systems** to display the list of file systems in your account.
3. Choose the file system on which you want to modify lifecycle policies.
4. On the file system details page, in the **General** section, choose **Edit**. The **Edit** page appears.
5. In the **Lifecycle management** section, you can change the following lifecycle policies:
 * Set **Transition into IA** to one of the available settings. To stop moving files into IA storage, choose **None**.
 * Set **Transition out of IA** to **On first access** to move files that are in IA storage to standard storage when they're accessed for non-metadata operations. To stop moving files from IA to standard storage on first access, set this to **None**.
6. Choose **Save changes**.

#### Using the AWS CLI to manage lifecycle policies on an existing file system
Run the put-lifecycle-configuration AWS CLI command or the PutLifecycleConfiguration API command, specifying the file system ID of the file system for which you are managing lifecycle management.

```
aws efs put-lifecycle-configuration \
--file-system-id File-System-ID \
--lifecycle-policies "[{\"TransitionToIA\":\"AFTER_60_DAYS\"},{\"TransitionToPrimaryStorageClass\":\"AFTER_1_ACCESS\"}]" \
--region us-west-2 \
--profile adminuser
```

You get the following response:
```
{
    "LifecyclePolicies": [
        {
            "TransitionToIA": "AFTER_60_DAYS"
        },
        {
            "TransitionToPrimaryStorageClass": "AFTER_1_ACCESS"
        }
    ]
}
```

#### Using the AWS CLI to stop lifecycle management for an existing file system
Run the **put-lifecycle-configuration** command, specifying the file system ID of the file system for which you are stopping lifecycle management. Keep the **--lifecycle-policies** property empty. 

```
aws efs put-lifecycle-configuration \
--file-system-id File-System-ID \
--lifecycle-policies \
--region us-west-2 \
--profile adminuser
```

You get the following response. 
```
{
    "LifecyclePolicies": []
}
```

#### Amazon EFS Performance

#### Performance summary
File system performance is typically measured by using the dimensions of latency, throughput, and input/output operations per second (IOPS). Amazon EFS performance across these dimensions depends on your file system's configuration. The following configurations impact the performance of an Amazon EFS file system: 
* **Storage class**: EFS One Zone or EFS Standard storage class types
* **Performance mode**: General Purpose or Max I/O 
* **Throughput mode**: Elastic, Provisioned, or Bursting 

#### Storage classes and performance
Amazon EFS uses the following storage classes: 
* **EFS One Zone storage classes**: EFS One Zone and EFS One Zone–Infrequent Access (EFS One Zone-IA). The EFS One Zone storage classes replicate data within a single Availability Zone (Single-AZ deployment). 
* **EFS Standard storage classes**: EFS Standard and EFS Standard–Infrequent Access (EFS Standard-IA). The EFS Standard storage classes replicate data across multiple Availability Zones (Multi-AZ deployment). 

First-byte latency when reading from or writing to either of the IA storage classes is higher than that for the EFS Standard or EFS One Zone storage classes.

#### Performance modes
Amazon EFS offers the two following performance modes:
* **General Purpose mode (recommended)** supports up to 35,000 IOPS, has the lowest per-operation latency, and is the recommended performance mode for file systems. File systems with EFS One Zone storage classes always use General Purpose performance mode. For file systems with EFS Standard storage classes, you can use either the default General Purpose performance mode or the Max I/O performance mode.
* **Max I/O mode** is designed for highly parallelized workloads that can tolerate higher latencies than the General Purpose mode. Max I/O mode is not supported for file systems using the EFS One Zone storage classes or those using Elastic Throughput mode.

**You cannot change the performance mode for a file system after the file system is created.**

AWS recommends using General Purpose performance mode for the vast majority of applications. If you are not sure which performance mode to use, choose the General Purpose performance mode. To help ensure that your workload stays within the IOPS limit available to file systems using General Purpose mode, you can monitor the *PercentIOLimit* CloudWatch metric.

#### Throughput modes 
A file system's throughput mode determines the throughput available to your file system. Amazon EFS offers three throughput modes: Elastic, Provisioned, and Bursting. The maximum throughput available with each throughput mode depends on the AWS Region. 

Your file system can achieve a combined 100 percent of its read and write throughput. For example, if your file system is using 33 percent of its read throughput limit, the file system can simultaneously achieve up to 67 percent of its write throughput limit. You can monitor your file system’s throughput usage in the **Monitoring > Throughput utilization (%)** graph on the on the file system details page of the console.

#### Choosing the correct throughput mode for a file system
##### Elastic Throughput (recommended)
Use the default Elastic Throughput when you have spiky or unpredictable workloads and performance requirements that are difficult to forecast. It is also recommended for use when an application drives throughput at an average-to-peak ratio of 5 percent or less. 

For file systems that are using Elastic Throughput, Amazon EFS automatically scales throughput performance up or down to meet the needs of your workload activity. Because throughput performance for file systems with Elastic Throughput scales automatically, you don't need to specify or provision the throughput capacity to meet your application needs. You pay only for the amount of metadata and data read or written, and you don't accrue or consume burst credits while in Elastic Throughput mode. 

**Note**: Elastic Throughput mode is available only for file systems that are configured with the General Purpose performance mode. 

##### Provisioned Throughput
Use Provisioned Throughput if you know your workload's performance requirements, or when your application drives throughput at an average-to-peak ratio of 5 percent or more.

With Provisioned Throughput mode, you specify a level of throughput that the file system can drive independent of the file system's size or burst credit balance. 

For file systems using Provisioned Throughput, you are charged for the amount of throughput activated for the file system. The throughput amount billed in a month is based on the throughput provisioned in excess of your file system’s included baseline throughput from Standard storage, up to the prevailing Bursting baseline throughput limits in the AWS Region.

If the file system’s baseline throughput exceeds the Provisioned Throughput amount, it automatically uses the Bursting Throughput permitted for the file system (up to the prevailing Bursting baseline throughput limits in that AWS Region).

##### Bursting Throughput
Use Bursting Throughput when you want throughput that scales with the amount of storage in your file system. 

In Bursting Throughput mode, the base throughput is proportionate to the file system's size in the EFS Standard storage class, at a rate of 50 kibibytes per second (KiBps) for each gibibyte (GiB) of storage. Burst credits accrue when the file system consumes below its base throughput rate, and are deducted when throughput exceeds the base rate.

When burst credits are available, a file system can drive throughput up to 100 mebibytes per second (MiBps) per tebibyte (TiB) of storage, up to the Amazon EFS Region's limit, with a minimum of 100 MiBps. If no burst credits are available, a file system can drive up to 50 MiBps per TiB of storage, with a minimum of 1 MiBps.

#### Restrictions on switching throughput modes and changing provisioned amount
You can switch an existing file system's throughput mode and change the throughput amount. However, after switching the throughput mode to Provisioned Throughput or changing the provisioned throughput amount, the following actions are restricted for a 24-hour period: 
* Switching from Provisioned mode to Elastic or Bursting mode
* Decreasing the provisioned throughput amount

#### Performance optimization tips
##### Average I/O size
The distributed nature of Amazon EFS provides high levels of availability, durability, and scalability. This distributed architecture results in a small latency overhead for each file operation. Because of this per-operation latency, overall throughput generally increases as the average I/O size increases. The increase occurs because the overhead is spread over a larger amount of data. 

##### Request model
If you activate asynchronous writes to your file system, pending write operations are buffered on the Amazon EC2 instance before they're written to Amazon EFS asynchronously. Asynchronous writes typically have lower latencies. When you use asynchronous writes, the kernel uses additional memory for caching.

A file system that has active synchronous writes, or one that opens files using an option that bypasses the cache (for example, O_DIRECT), issues synchronous requests to Amazon EFS. Every operation goes through a round trip between the client and Amazon EFS.

**Note**: Your chosen request model has trade-offs in consistency, if you're using multiple Amazon EC2 instances and speed. 

##### NFS client mount setting
When you mount your file systems on Amazon EC2 instances, Amazon EFS supports the Network File System (NFS) version 4.0 and 4.1 (NFSv4) protocols. NFSv4.1 provides better performance for parallel small-file read operations, greater than 10,000 files per second, compared to less than 1,000 files per second for NFSv4.0. For Amazon EC2 macOS instances running macOS Big Sur, only NFSv4.0 is supported.

Don't use the following mount options:
* *noac, actimeo=0, acregmax=0, acdirmax=0* – These options turn off the attribute cache, which has a very large performance impact.
* *lookupcache=pos, lookupcache=none* – These options turn off the file name lookup cache, which has a very large impact on performance.
* *fsc* – This option turns on local file caching but does not change NFS cache coherency and does not reduce latencies.

Note: When you mount your file system, consider increasing the size of the read and write buffers for your NFS client to 1 MB. 

##### Optimizing small-file performance
You can improve small-file performance by minimizing file reopens, increasing parallelism, and bundling reference files where possible.
* Minimize the number of round trips to the server.
 * Don't unnecessarily close files if you will need them later in a workflow. Keeping file descriptors open provides direct access to the local copy in the cache. File open, close, and metadata operations generally cannot be made asynchronously or through a pipeline.
 * When reading or writing small files, the two additional round trips are significant.
 * Each round trip (file open, file close) can take as much time as reading or writing megabytes of bulk data. It's more efficient to open an input or output file once, at the beginning of your compute job, and hold it open for the entire length of the job.
* Use parallelism to reduce the impact of round-trip times.
* Bundle reference files in a .zip file. Some applications use a large set of small, mostly read-only reference files. Bundling these in a .zip file helps you to read many files with one open-close round trip.
 * The .zip format provides for random access to individual files.

##### Optimizing directory performance
When you use a listing (ls) command on very large directories (over 100,000 files) that are being modified concurrently, Linux NFS clients can stop responding. This issue is fixed in kernel 5.11, which has been ported to Amazon Linux 2 kernels 4.14, 5.4, and 5.10.

AWS recommends keeping the number of directories on your file system to less than 10,000, if possible. Use nested subdirectories as much as possible.

When listing a directory, avoid getting file attributes if they are not required, because they are not stored in the directory itself.

##### Optimizing the NFD read_ahead_kb size
The NFS **read_ahead_kb** attribute defines the number of kilobytes for the Linux kernel to read ahead or prefetch during a sequential read operation.

For Linux kernel versions before 5.4.x, the **read_ahead_kb** value is set by multiplying **NFS_MAX_READAHEAD** by the value for *rsize*. The *rsize* is the client configured read buffer size set in the mount options. When you use the recommended mount options, this formula sets **read_ahead_kb** to 15 MB.

 * **Note**: Starting with Linux kernel versions 5.4.x, the Linux NFS client uses a default **read_ahead_kb** value of 128 KB. AWS recommends increasing this value to 15 MB.

The Amazon EFS mount helper that is available in **amazon-efs-utils** version 1.30.2 and later automatically modifies the **read_ahead_kb** value to equal 15 * rsize, or 15 MB, after mounting the file system.

For Linux kernels 5.4 or later, if you do not use the mount helper to mount your file systems, consider manually setting **read_ahead_kb** to 15 MB for improved performance. After mounting the file system, you can reset the **read_ahead_kb** value.

#### Amazon EFS Pricing Calculation and Cost Optimization
Amazon EFS is designed to provide serverless, fully elastic file storage that helps you share file data without provisioning or managing storage capacity and performance. There is no minimum fee or setup charge. You pay only for the storage that you use, for read and write access to data stored in Infrequent Access storage classes, for read and write access using Elastic Throughput, and for any Provisioned Throughput.

Amazon EFS offers four storage classes. There are two standard storage classes, EFS Standard and EFS Standard–Infrequent Access (EFS Standard-IA). 

The other two are One Zone storage classes, EFS One Zone and EFS One Zone-Infrequent Access (EFS One Zone-IA).

Certain configuration considerations can help you optimize your Amazon EFS file system costs. The considerations are categorized into the following three areas:
* Choosing your Amazon EFS storage class, including lifecycle management configuration
* Choosing your throughput mode
* Choosing and managing your data retention and replication methodology

#### EFS pricing explanation
##### [EFS pricing explanation](https://aws.amazon.com/efs/pricing/)

##### [AWS pricing calculator](https://calculator.aws/#/createCalculator/EFS)

#### Amazon EFS storage classes
The following are Storage class service cost comparisons:
* EFS One Zone can reduce the cost of EFS Standard pricing by approximately 47 percent. 
* EFS Standard-IA can reduce the cost of EFS Standard pricing by approximately 92 percent. 
* EFS One Zone-IA can reduce the cost of EFS One Zone pricing by approximately 92 percent. 

#### Considerations and trade-offs

#### EFS One Zone compared to EFS Standard 
With EFS One Zone compared to EFS Standard, you can potentially save up to 46.6 percent on your storage costs. However, you have trade-offs for availability can potentially incur access costs. 

##### Availability trade-offs
* EFS One Zone has an availability service level agreement (SLA) of 99.9 percent. 99.9 percent SLA translates into approximately 8.77 hours or 526 minutes per year where your EFS One Zone file system might be unreachable. 
* EFS Standard has an availability SLA of 99.99 percent. 99.99 percent SLA translates into approximately 52.6 minutes per year where your EFS Standard file system might be unreachable.

##### Availability recommendation
You must consider availability as part of your decision process. Only consider EFS One Zone when having potentially lower availability is acceptable for your workflow.

##### Potential additional access costs
* EFS Standard has a mount target in each Availability Zone in the AWS Region. The mount targets provide you access to your EFS Standard file system from within each Availability Zone. When accessing from within the same VPC and from within the same Availability Zone, there are no additional data transfer in and data transfer out costs.
* With EFS One Zone, you have one mount target that is located in a single Availability Zone. To avoid additional data transfer costs, all your resources must be located in the same Availability Zone. 
 * If your resources are located in another Availability Zone, you are charged for data transfer in and data transfer out. 
 * Using the example pricing, you would be charged $0.01 per every gigabyte transferred between Availability Zones. These transfer changes can add up and quickly reduce any cost savings that you achieved by changing storage classes.

##### Access costs recommendation
Consider how much data will be transferred between your compute or other resources in other Availability Zones and your EFS One Zone file system. If your workflow involves more than a minimal amount, your additional access costs exceed any potential savings from using an EFS One Zone storage class. 

#### Infrequent access tiers compared to standard access tiers 
With EFS Standard-IA and EFS One Zone-IA compared to EFS Standard and EFS One Zone, you can potentially save up to 91.6 percent on your storage costs. This savings only applies to the data stored in the Infrequent Access tier. As a general industry average percentage, 80 percent of data is infrequently accessed for general purpose file systems. However, you potentially can incur charges for infrequent access requests. 

##### Potential Infrequent Access tier costs
* If you move your data from the EFS Standard to the EFS Standard-IA storage tier too soon, you are charged $0.01 per GB when a file is transferred back to the EFS Standard when your files are accessed.
* If you move your data from the EFS One Zone to the EFS One Zone-IA storage tier too soon, you are also charged $0.01 per GB transferred back to EFS One Zone when your files are accessed.

##### Recommendations
* Using EFS Standard-IA and EFS One Zone-IA can generate a significant cost savings for most workflows. The most common cost issues are created when data is moved to the Infrequent Access tier too soon. To help avoid these costs, AWS recommends that you understand your workflow. 
* To calculate actual saving from moving data infrequently accessed, you need to examine when your files were last accessed and when the files were initially created. You can use the data to help you determine what percentage of your files are available to be moved to the IA storage classes and after what period of time. This can help you estimate cost savings as a percentage of your total data.
* To understand your workflow better, you can monitor your infrequent access requests. You can then change your tiering settings to closely match your actual use. Your ideal setting can be tiered after 90 days or even 120 days. For some workflows, you might even find that EFS Intelligent-Tiering does not make sense.

#### Selecting throughput mode
Amazon EFS offers Elastic Throughput mode, Bursting Throughput mode, and Provisioned Throughput mode. With EFS Provisioned Throughput, you are charged $6.00 per MiBps per month that you provisioned to exceed the base rate throughput that you would have received by using Bursting Throughput mode. 

##### Example cost estimate
* You receive 50 MiBps for each terabyte (TB) of data in your EFS file system. If you have a file system with 10 TB of data, you have a base rate of 500 MiBps throughput.
* If you provision 1 GiBps(1,000 MiBps) throughput, your costs would be calculated as follows:
((Provisioned throughput) minus (base rate throughput)) times (rate per MiBps)
(1,000 MiBps - 500 MiBps) x $6.00 per MiBps = 500 x $6.00 = $3,000 per month

##### Recommendations
* Frequently monitor your EFS file system's actual throughput.
* When creating a new file system, start with Bursting Throughput mode whenever possible and change to Provisioned Throughput mode only when required. You can change throughput modes and mode settings only once in a 24-hour period.
* For Provisioned Throughput mode, underprovision and increase the amount incrementally as required. Make sure the increment chosen is close to the amount needed. You can change the provisioned amount only once in a 24-hour period.
* As your file system grows, consider changing throughput mode back to Bursting Throughput when possible.

#### Backup and replication costs 
AWS Backup and Amazon EFS replication each come with a cost for the amount of AWS services that you use. As part of designing your data retention and replication methodology, you need to determine your requirements and be aware of the potential costs. 

#### AWS Backup 
AWS Backup of your EFS file system, automatic backups, is configured by default when you create your file system by using the Amazon EFS console. You can turn off automatic backups when you use the custom configuration method. You can add it during configuration by using the AWS CLI and AWS SDKs. In addition, with Amazon EFS replication, an automatic backup is created for the destination file system copy.

You can also create backups for your EFS file system by using the AWS Backups console, AWS CLI, and AWS SDKs. Creating your backups with AWS Backup separately helps you to further customize your backups by using the settings that you choose.

The cost for AWS Backups is $0.05 per GB per month (GB-month) for standard storage and $0.01 per GB-month for cold storage.

Backing up your data is usually considered a requirement for most organizations. AWS recommends that you make this choice based on the organization's requirements and the value of your data.

##### Optimization questions for backups
* Is a backup copy needed?
* How to manage short-term or recovery retention requirements?
* How to manage long-term or archival retention requirements?

###### Data value
You can ask a few questions to help determine the value of your data.
* Is your data temporary or transitory, or can it be easily re-created?
* What is the impact of potential data loss or corruption?
* Do you have regulatory or other compliance requirements?
* If you were subjected to ransomware, would you need to pay to recover it or would you abandon it? 

##### Recommendations
* Determine the value of your file system's data based on the use case and the cost to re-create the data if required. In most circumstances, if you have a reason that would require your data to be created if it were lost to you, having a backup of your file system is recommended.
* For short-term recovery backups, determine your management and deletion strategy. Remove older backups when they are no longer required. Clear older incremental backups according to your planned cadence.
* If you have long-term retention requirements, create your archival strategy to move older backups to cold storage. Perform periodic full backups for point-in-time retention copies, such as annual, monthly, or weekly copies. Remove older archival backups when retention requirements expire.

##### Amazon EFS replication 
When you plan to use Amazon EFS replication, you will have several associated costs, including file system capacity, automatic backup capacity, and data transfer costs. You can optimize these costs by selecting the most appropriate AWS Region to replicate to, the EFS storage class and storage tiering to use, and whether to include automatic backups for your replicated file system. 
* If you're planning to use Amazon EFS replication, do you require backups of both the source and destination file systems? If you do not require automatic backups, you can deactivate them on the destination file system. You can add them back if required at a later time. Deactivating automatic backups can save $6 per GB per month. 
* AWS charges you for the consumed capacity of your replicated EFS file system. Pricing for data storage can vary based on the AWS Region or location chosen for that storage. For example, US West (N. California) costs $0.33 per GB and US East (Virginia) costs $0.30 per GB for EFS Standard. 
* If you're using your replicated EFS file system for read-only access, you want to plan how to optimize your data tiering strategy. You will want to plan based on infrequent access requests just like you planned for your source file system. 
* You can implement different storage classes and with different performance modes for your destination file system. You should plan which storage class, performance mode, and throughput mode that you require. If your replicated file system is just for disaster recovery, you can vary the storage class from your source file system. Each consideration should be weighed carefully before you implement your service.

#### More examples of pricing calculation

#### Attaching an Amazon EFS File System with amazon-efs-utils

#### Amazon EFS client (amazon-efs-utils)

The Amazon EFS client is an open-source collection of Amazon EFS tools available at no additional cost. The amazon-efs-utils package comes preinstalled on Amazon Linux and Amazon Linux 2 AMIs. You can also build and install the package on other Linux distributions. The process to install the Amazon EFS client varies based on Linux distributions. You can also use AWS Systems Manager to automatically install or update the package to simplify and standardize your AWS resources.

##### [Using the amazon-efs-utils](https://docs.aws.amazon.com/efs/latest/ug/using-amazon-efs-utils.html)

##### [Manually installing amazon-efs-utils ](https://docs.aws.amazon.com/efs/latest/ug/installing-amazon-efs-utils.html)

##### [Automatically installing amazon-efs-utils](https://docs.aws.amazon.com/efs/latest/ug/manage-efs-utils-with-aws-sys-manager.html)

##### [Downloading Amazon EFS client](https://github.com/aws/efs-utils)

#### Using EFS mount helper
The Amazon EFS client includes a mount helper and tooling that streamlines performing encryption of data in transit for Amazon EFS file systems. A mount helper is a program that you use when you mount a Linux file system.

AWS recommends that you use the mount helper included with the Amazon EFS client to mount your Amazon EFS file systems. Using the Amazon EFS client streamlines mounting EFS file systems and can provide improved file system performance.

##### [Using EFS mount helper](https://docs.aws.amazon.com/efs/latest/ug/efs-mount-helper.html)

#### How the mount helper works
The mount helper defines a new network file system type, called efs, which is fully compatible with the standard mount command in Linux. You can mount a file system by specifying one of the following properties: 
* **File system DNS name**: If you use the file system DNS name and the mount helper cannot resolve the DNS name, the mount helper falls back to using the mount target IP address. 
* **File system ID**: If you use the file system ID, the mount helper resolves it to the local IP address of the mount target elastic network interface without calling external resources. 
* **Mount target IP address**: You can use the IP address of one of the file systems' mount targets. 

Mount helper can be used with any Amazon EC2 instance running one of the following supported Linux or macOS distributions:
* Amazon Linux 2
* Amazon Linux 2017.09 and later
* macOS Big Sur
* Red Hat Enterprise Linux (and derivatives such as CentOS) version 7 and later
* Ubuntu 16.04 LTS and later

Mount helper supports mounting to Amazon EFS Standard and Amazon EFS One Zone storage classes. You can find the value for all these properties in the EFS console. 

#### Encrypted data in transit
When encryption of data in transit is declared as a mount option for your Amazon EFS file system, the mount helper initializes a client **stunnel** process and a supervisor process called **amazon-efs-mount-watchdog**. 

Stunnel is an open-source multipurpose network relay. The client **stunnel** process listens on a local port for inbound traffic and the mount helper redirects NFS client traffic to this local port. 

The **amazon-efs-mount-watchdog** process monitors the health of TLS mounts, and is started automatically the first time an EFS file system is mounted over TLS. This process is managed by either **upstart** or **systemd**, depending on your Linux distribution, and by **launchd** on the macOS Big Sur distribution.

The mount helper uses TLS version 1.2 to communicate with your file system. Using TLS requires certificates, and these certificates are signed by a trusted Amazon Certificate Authority.

#### Monitoring Amazon EFS
AWS recommends that you monitor your AWS resources as part of the AWS Well-Architected Framework. The AWS Well-Architected Framework describes key concepts, design principles, and architectural best practices for designing and running workloads in the AWS Cloud. AWS also recommends that you collect monitoring data from all the parts of your AWS solution. By monitoring your full solution, you can debug any point of failure, if one occurs. 

Monitoring your Amazon EFS resources is an important part to maintaining the reliability, availability, and performance of your EFS file systems. In this lesson, you will learn about Amazon CloudWatch and other tools to assist you in monitoring your Amazon EFS resources.

#### Getting started with monitoring
To get started with monitoring, create a monitoring plan, determine baseline performance, and determine which tools you will use to monitor your file system. 

#### Creating a monitoring plan
Start by developing a monitoring plan. The plan incorporates the following important aspects included to make your plan successful:
* Your monitoring goals
* What resources you monitor
* How frequently you monitor
* What tools you use
* Who performs the tasks
* Who to notify when something happens

Detailed monitoring discussions and concepts are available as part of the AWS Well-Architected Framework for each of the six pillars. You can search for monitoring in the documentation for each of the pillars.

##### [AWS Well-Architected Framework ](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)

#### Baselining your EFS file system
Baselining is a method for analyzing performance. The method is marked by comparing current performance to a historical metric. The first step is to establish a baseline for your EFS file system to determine normal performance in your environment.

The changes might be of little concern, or they can help you identify issues that you need to address. Your patterns can change because your workflow matures or usage increases across your organization. If you identify changes in usage patterns, you might need to establish new baselines for your comparison. You might also need to address the changes and devise methods to address any issues to meet application requirements and user demands.
* For example, with Amazon EFS, you can monitor network throughput; I/O for read, write, and metadata operations; client connections; and burst credit balances for your file systems. 
* If performance falls outside your established baseline, you might need to change client connection parameters, throughput, or the number of connected clients to optimize the file system for your workload. 

To establish a baseline, AWS recommends that you should, at a minimum, monitor the following items: 
* Your file system's network throughput
* The number of client connections to a file system
* The number of bytes for each file system operation, including data read, data write, and metadata operations

#### Monitoring tools overview
AWS provides various tools that you can use to monitor Amazon EFS. You can configure some of these tools to do the monitoring for you, but some of the tools require manual intervention. AWS recommends that you automate monitoring tasks as much as possible. 

#### Automated monitoring tools
You can use the available automated monitoring tools to watch Amazon EFS and report when something is wrong or out of the normal range. 

##### Amazon CloudWatch alarms
With CloudWatch alarms, you can watch a single metric over a time period that you specify and perform one or more actions based on the value of the metric, relative to a given threshold, over a number of time periods. The action is a notification sent to an Amazon Simple Notification Service (Amazon SNS) topic or Amazon EC2 Auto Scaling policy. 

CloudWatch alarms do not invoke actions only because they are in a particular state; the state must have changed and been maintained for a specified number of periods.

##### Amazon CloudWatch Logs
With Amazon CloudWatch Logs, you can monitor, store, and access your log files from AWS CloudTrail or other sources. 

##### Amazon CloudWatch Events
Amazon CloudWatch Events helps you to match events and route them to one or more target functions or streams to make changes, capture state information, and take corrective action. 

##### AWS CloudTrail log monitoring
Amazon EFS is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in Amazon EFS. CloudTrail captures all API calls for Amazon EFS as events, including calls from the Amazon EFS console and from code calls to Amazon EFS API operations. 

If you create a CloudTrail trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for Amazon EFS. If you don't configure a trail, you can still view the most recent events in the CloudTrail console in Event history. You can determine the request that was made to Amazon EFS, the IP address from which the request was made, who made the request, when it was made, and additional details.

With CloudTrail log monitoring, you can share log files between accounts, monitor CloudTrail log files in real time by sending them to CloudWatch Logs, write log processing applications in Java, and validate that your log files have not changed after delivery by CloudTrail.

#### Monitoring with Amazon CloudWatch
CloudWatch helps you to monitor your EFS file systems. CloudWatch collects and processes raw data from Amazon EFS into readable, near real-time metrics. These statistics are maintained for a period of 15 months, so that you can gain a better perspective on how your web application or service is performing. 

By default, Amazon EFS metric data is automatically sent to CloudWatch at 1-minute periods, unless noted for some individual metrics. The Amazon EFS console displays a series of graphs based on the raw data from CloudWatch. Depending on your needs, you might prefer to get data for your file systems from CloudWatch instead of the graphs in the console.

##### CloudWatch metrics for Amazon EFS 
CloudWatch metrics for Amazon EFS use the EFS file system namespace and provide information for a single dimension. The dimension is the file system ID (**FileSystemId**). A file system's ID can be found in the Amazon EFS console, and it takes the form of **fs-abcdef0123456789a**. CloudWatch does not provide metrics across multiple file systems at a time. 

CloudWatch has 11 metrics specific to Amazon EFS. The following table shows the metrics and their description.

| Metric | Description |
| --------------------- | --------------------------------------------------------------------|
| **TimeSinceLastSync** | This shows the amount of time that has passed since the last successful sync to the destination file system in a replication configuration.
Any changes to data on the source file system that occurred before the **TimeSinceLastSync** value have been successfully replicated.
Any changes on the source that occurred after the **TimeSinceLastSync** value might not be fully replicated. |
| **PercentIOLimit** | This shows how close a file system is to reaching the I/O limit of the General Purpose performance mode. If this metric is at 100 percent, consider moving your application to a file system using the Max I/O performance mode.
**Note**: This metric is only submitted for file systems using the General Purpose performance mode. | 
| **BurstCreditBalance** | This is the number of burst credits that a file system has. With burst credits, a file system can burst to throughput levels above a file system’s baseline level for periods of time. |
| **PermittedThroughput** | This is the maximum amount of throughput that a file system can drive.
For file systems in the Provisioned Throughput mode, if the amount of data stored in the EFS Standard storage class permits your file system to drive a higher throughput than you provisioned, this metric reflects the higher throughput instead of the provisioned amount.
For file systems in Bursting Throughput mode, this value is a function of the file system size and **BurstCreditBalance**. |
| **MeteredIOBytes** | This is the number of metered bytes for each file system operation, including data read, data write, and metadata operations, with read operations metered at one-third the rate of other operations. |
| **TotalIOBytes** | This is the actual number of bytes for each file system operation, including data read, data write, and metadata operations.
This is the actual amount that your application is driving, and not the throughput that the file system is being metered at. It might be higher than the numbers shown in **PermittedThroughput**. |
| **DataReadIOBytes** | This is the number of bytes for each file system read operation. |
| **DataWriteIOBytes** | This is the number of bytes for each file write operation. |
| **MetadataIOBytes** | This is the number of bytes for each metadata operation. |
| **ClientConnections** | This is the number of client connections to a file system. With a standard client, there is one connection per mounted Amazon EC2 instance. |
| **StorageBytes** | This is the size of the file system in bytes, including the amount of data stored in the EFS Standard and EFS Standard-IA storage classes.
This metric is submitted every 15 minutes to CloudWatch. |

#### Accessing CloudWatch metrics
* In the EFS console
* In the CloudWatch console
* Using the CloudWatch CLI
* Using the CloudWatch API
* You can also create and access derived or calculated metrics. 

##### [Accessing CloudWatch metrics ](https://docs.aws.amazon.com/efs/latest/ug/accessingmetrics.html)

#### CloudWatch metrics in EFS console
The **File system metrics** page displays a default set of CloudWatch metrics for the file system. Any CloudWatch alarms that you have configured also display with these metrics. For file systems that use Max I/O performance mode, the default set of metrics includes Burst Credit balance in place of Percent IO limit. 

To override the default settings, choose the settings icon and update the metrics to display in the **Metric display settings** dialog box. 

You have several options to customize your dashboard. You can choose your **Display mode** between **Time series** or **Single value**, show or hide CloudWatch alarms, add metrics to your dashboard, open CloudWatch, and change the metric time window displayed.

**Throughput Utilization (%)**, which is displayed by default on the **File system metrics page**, is an example of a derived metric using CloudWatch metric math.

#### CloudWatch metrics to monitor throughput performance 
The metrics reported by Amazon EFS provide information that you can analyze in different ways.
* The CloudWatch metrics for throughput monitoring—**TotalIOBytes**, **ReadIOBytes**, **WriteIOBytes**, and **MetadataIOBytes**—represent the actual throughput that you are driving on your file system. 
* The metric **MeteredIOBytes** represents the calculation of the overall metered throughput that you are driving. You can use the **Throughput utilization (%)** graph in the Amazon EFS console **Monitoring** section to monitor your throughput use. 
* **PermittedThroughput** measures the amount of permitted throughput for the file system. For file systems in Provisioned Throughput mode, if the amount of data stored in the EFS Standard storage class permits your file system to drive a higher throughput than you provisioned, this metric reflects the higher throughput instead of the provisioned amount. For file systems in Bursting Throughput mode, this value is a function of the file system size and **BurstCreditBalance**. 
* When the values for **MeteredIOBytes** and **PermittedThroughput** are equal, your file system is consuming all available throughput. For file systems using Provisioned Throughput mode, you can provision additional throughput.
* For file systems using Bursting Throughput mode, monitor **BurstCreditBalance** to ensure that your file system is operating at its burst rate instead of its base rate. If the balance is consistently at or near zero, you must switch to Provisioned Throughput mode to get additional throughput.

#### Amazon EFS replication
With Amazon EFS replication, you can create a replica of your Amazon EFS file system in the AWS Region of your preference. When you set up replication on an EFS file system, Amazon EFS automatically and transparently replicates the data and metadata on the source file system to a new destination EFS file system. 

To set up replication, you create an Amazon EFS replication configuration. This configuration is used to manage the process of creating the destination file system and keeping it in-sync with the source file system.

Amazon EFS automatically keeps the source and destination file systems synchronized. Amazon EFS replication is continual and designed to provide a recovery point objective (RPO) and a recovery time objective (RTO) of minutes. These features can assist you in meeting your compliance and business continuity goals.

#### Replication configuration
##### Specified replication properties
When you create a replication configuration, you specify the properties for the destination file system.
* **AWS Region**: Specify the AWS Region in which to create the destination file system. Amazon EFS replication is available in all AWS Regions where EFS is supported. 
* **Availability and durability**: Specify the storage class used by the destination file system, either Regional or One Zone. 
* **Availability Zone**: If you choose One Zone availability and durability, you must choose the Availability Zone to create the destination file system in.
* **Encryption**: All destination file systems are created with encryption at rest turned on. You can specify the AWS Key Management Service (AWS KMS) key that is used to encrypt the destination file system. 
 * If you don't specify am AWS KMS key, your service-managed KMS key for Amazon EFS is used.
 * After the destination file system is created, you cannot change the AWS KMS key.

##### Default replication properties
In addition to the properties that you specify, other EFS replication properties are set by default.
* **Automatic backups**: Automatic daily backups are activated on the destination file system. After the file system is created, you can change the automatic backup setting. 
* **Performance mode**: The destination file system's performance mode matches that of the source file system, unless the destination file system uses EFS One Zone storage. In that case, the General Purpose performance mode is used. The performance mode cannot be changed. 
* **Throughput mode**: The destination file system's throughput mode matches that of the source file system. After the file system is created, you can modify the throughput mode. If the source file system's throughput mode is Provisioned, the destination file system's provisioned throughput amount matches that of the source file system, unless the source file's provisioned amount exceeds the limit for the destination file system's Region. If the source file system's provisioned amount exceeds the Region limit for the destination file system, the destination file system's provisioned throughput amount is the Region limit. 

##### Disabled by default properties
In contrast to creating your source file system, lifecycle management is not activated by default. EFS lifecycle management and EFS Intelligent-Tiering are deactivated on the destination file system. 

#### How EFS replication works 
Amazon EFS creates the destination file system with read-only permissions. After the destination file system is created, Amazon EFS performs the initial sync that copies all data and metadata on the source to the destination file system. 

An EFS file system can be part of only one replication configuration. You can't replicate a source file system to multiple destination file systems. You also can't use a destination file system as the source file system in another replication configuration.

The amount of time that the initial sync takes to finish depends on the size of the source file system. After the initial sync is finished, the replication process continually keeps the destination file system in sync with the source.

You can monitor when the last successful sync occurred by using the console, the AWS CLI, the API, and Amazon CloudWatch.

##### Replication performance
After the initial replication is finished, the majority of source file systems have their subsequent changes replicated to their destination file systems within 15 minutes.

However, if the source file system has files that change very frequently, and has either more than 100 million files or files that are larger than 100 GB, replication will take longer than 15 minutes. 

##### Permissions
Amazon EFS uses the EFS service-linked role named **AWSServiceRoleForAmazonElasticFileSystem** to synchronize the state of the replication between the source and destination file systems.

To use EFS replication, you must use the following actions to configure the IAM entity to create a service-linked role, replication configuration, and file system: 
* **elasticfilesystem:CreateReplicationConfiguration***
* **elasticfilesystem:DeleteReplicationConfiguration***
* **elasticfilesystem:DescribeReplicationConfigurations***
* **elasticfilesystem:CreateFileSystem***
* **iam:CreateServiceLinkedRole**
* You can use the **AmazonElasticFileSystemFullAccess** managed policy instead to automatically get all EFS permissions.

##### Destination mount targets
Amazon EFS does not create any mount targets when it creates the destination file system. You can create these manually. You can add mount targets, security groups, and access points to prepare for failing over as needed.

Because a destination file system is read-only while it is a member of a replication configuration, any write operations to it will fail. However, you can use the destination file system for read-only use cases, including testing and development.

#### Failing over to a destination file system 
To fail over to the destination file system in a replication configuration, you must delete the replication configuration. After the replication configuration is deleted, the destination file system becomes writeable, and you can start using it in your application workflow. This process can take several minutes to complete. 

After failing over to a destination file system, that file system can then be used as the source file system in a new replication configuration. However, it cannot be designated as a destination file system again. A replication configuration always creates a new EFS file system for the destination.

#### Backing Up Amazon EFS

#### AWS Backup
AWS Backup is a simple and cost-effective way to back up your Amazon EFS file systems that are in AWS Regions where the AWS Backup service is available. AWS Backup is a unified backup service designed to simplify the creation, migration, restoration, and deletion of backups, while providing improved reporting and auditing.

AWS Backup simplifies development of a centralized backup strategy for legal, regulatory, and professional compliance. AWS Backup also makes protecting your AWS storage volumes, databases, and file systems simpler by providing a central place. AWS Backup is integrated with a growing list of AWS services.

Amazon EFS is integrated with AWS Backup by default. You can use the EFS console, API, and AWS CLI to activate automatic backups for your file system. Automatic backups use a default backup plan with the AWS Backup recommended settings for automatic backups.

#### Key features
With AWS Backup, you can do the following: 
* Configure and audit the AWS resources that you want to back up
* Automate backup scheduling
* Set retention policies
* Monitor all recent backup and restore activity

##### Incremental backups
AWS Backup performs incremental backups of EFS file systems. During the initial backup, a copy of the entire file system is made. During subsequent backups of that file system, only files and directories that have been changed, added, or removed are copied. 

With each incremental backup, AWS Backup retains the necessary reference data to facilitate a full restore. This approach minimizes the time required to complete the backup and saves on storage costs by not duplicating data.

##### Backup consistency
Amazon EFS is designed to be highly available. You can access and modify your Amazon EFS file systems while your backup is occurring in AWS Backup. However, inconsistencies, such as duplicated, skewed, or excluded data, can occur if you make modifications to your file system while the backup is occurring. 

These modifications include write, rename, move, or delete operations. To ensure consistent backups, AWS recommends that you pause applications or processes that are modifying the file system for the duration of the backup process. Or you can schedule your backups to occur during periods when the file system is not being modified.

##### Performance
In general, you can expect the following backup rates with AWS Backup:
* 100 megabytes per second for file systems composed of mostly large files
* 500 files per second for file systems composed of mostly small files

The maximum duration for a backup operation in AWS Backup is 7 days.

**Note**: Complete restore operations generally take longer than the corresponding backup.

Using AWS Backup doesn't consume accumulated burst credits, and it doesn't count against the General Purpose mode file operation limits.

##### Backup completion window
You can optionally specify a completion window for a backup. This window defines the period of time in which a backup must be completed. 

If you specify a completion window, make sure that you consider the expected performance and the size and makeup of your file system. Doing this helps make sure that your backup can be completed during the window.

Backups that aren't completed during the specified window are flagged with an incomplete status. During the next scheduled backup, AWS Backup resumes at the point that it left off.

##### EFS storage classes
You can use AWS Backup to back up all data in an EFS file system, whatever storage class the data is in. You don't incur data access charges when backing up an EFS file system that has lifecycle management turned on and has data in the Infrequent Access (IA) storage class.

When you restore a recovery point, all files are restored to the Standard storage class. Lifecycle management policies begin over as new data. Infrequently accessed data is moved to IA storage classes when the policy rules are met.

##### IAM permissions for creating and restoring backups
You can use the **elasticfilesystem:backup** and **elasticfilesystem:restore** actions to allow or deny an IAM entity—such as a user, group, or role—the ability to create or restore backups of an EFS file system. 

You can use these actions in a file system policy or in an identity-based IAM policy.

##### On-demand backups
Using either the AWS Backup console or the AWS CLI, you can save a single resource to a backup vault on demand. Unlike with scheduled backups, you don't need to create a backup plan to initiate an on-demand backup. 

You can still assign a lifecycle to your backup, which automatically moves the recovery point to the cold storage tier and notes when to delete it.

##### Concurrent backups
AWS Backup limits backups to one concurrent backup per resource. Therefore, scheduled or on-demand backups might fail if a backup job is already in progress.

#### Automatic backups 
When you create a new file system by using the Amazon EFS console, automatic backups are activated by default. You can turn on automatic backups for file systems created by using the AWS CLI or API. 

You can deactivate this setting during or after file system creation. You can turn off automatic backups by using the EFS console or AWS CLI.

##### Default settings and behaviors 

With automatic backups, the default backup plan settings and behaviors that are applied to your backups differ from manually creating a backup. 
* Backups are created as daily backups with a 35-day retention period. 
* Backups are stored in a default EFS backup vault, which is created by Amazon EFS on your behalf. 
* A default backup plan and backup vault cannot be deleted. 
* Default backup plan settings can be edited by using the AWS Backup console.
* Automatic backups can be turned off at any time by using the Amazon EFS console or AWS CLI.
* The **aws:elasticfilesystem:default-backup** system tag key with a value of **enabled** is applied to an EFS file system when automatic backups are created.

#### Using AWS Backup to manually configure backups
When you use AWS Backup to manually set up your file system backups, you first create a backup plan. The backup plan defines the backup schedule, backup window, retention policy, lifecycle policy, and tags. You can create a backup plan by using the AWS Backup Management Console, the AWS CLI, or the AWS Backup API. As part of a backup plan, you can define the following: 
* **Schedule**: When the backup occurs
* **Backup window**: The window of time during which the backup must start 
* **Lifecycle**: When to move a recovery point to cold storage and when to delete it
* **Backup vault**: Which vault is used to organize recovery points created by the backup rule

After your backup plan is created, you assign the specific Amazon EFS file systems to the backup plan by using either tags or the Amazon EFS file system ID. After a plan is assigned, AWS Backup begins automatically backing up the Amazon EFS file system on your behalf, according to the backup plan that you defined. You can use the AWS Backup console to manage backup configurations or monitor backup activity. 

#### Knowledge Check
##### Which AWS service helps automate the tasks to install or update the amazon-efs-utils package on Amazon EC2 instances? 
* AWS Systems Manager 

The other options are incorrect because of the following: 
* SageMaker is a machine learning suite of services.
* AWS Backup is a unified backup service designed to simplify the creation, migration, restoration, and deletion of backups, while providing improved reporting and auditing. 
* Launch Wizard helps you launch third-party applications on AWS.

##### Which performance mode is recommended for workloads that must scale to higher levels of aggregate throughput and IOPS? 
* Max I/O

The Max I/O performance mode is recommended for workloads that must scale to higher levels of aggregate throughput and IOPS.

The other options are incorrect because of the following: 
* General Purpose performance mode is the default performance mode for Amazon Elastic File System (Amazon EFS), but Max I/O scales more efficiently.
* Provisioned Throughput is a throughput mode that is recommended for workloads requiring higher throughput-to-storage ratios.
* Bursting Throughput is the default throughput mode that is recommended for most workloads.

##### What is the maximum frequency that you can modify your file system's throughput settings for an Amazon Elastic File System (Amazon EFS) file system? 
* Once in a 24-hour (1-day) period

You can change your file system's throughput setting once in a 24-hour period. You can change between Bursting Throughput and Provisioned Throughput modes. You can also modify your Provisioned Throughput rate. However, you can only make changes once in the 24-hour period.

### Week 8: Databases 2 Part 1
#### Amazon RDS uses the following six database engine options. 
* **MySQL** is an open-source database engine that is popular due to its enterprise-grade features and free or low-cost licensing. It also prioritizes simplicity and ease of use. While MySQL is currently owned and sponsored by Oracle, the founding developer forked the project to create MariaDB. 
* **MariaDB** has remained open source and offers improved performance and some additional features not available with MySQL. For example, MariaDB includes support for a variety of optimized and purpose-built storage engines. 
* **PostgreSQL** is another open-source database engine, but it can be more complex to use than MySQL, due to its advanced features, including support for advanced data types and indexing options. 
* **Amazon Aurora** is a database engine built for the cloud and is compatible with MySQL and PostgreSQL. It uses storage that is replicated across three Availability Zones for increased durability, performance, and recovery. 
* **Oracle** offers a commercially licensed database engine that is widely used by large enterprises. It supports both OLTP and OLAP workloads. 
* **Microsoft SQL Server** is another commercially licensed database engine. In addition to supporting enterprise-level functionality, Microsoft SQL Server may be interesting to companies already using Microsoft products with their workloads, due to the seamless integration.

#### Database Design Principles

#### Internet-scale architectures
Internet-scale architectures must meet a huge demand, and this starts with the data. Purpose-built databases distribute the data across multiple databases, or partitions, to meet the demand from system requests. This can also help with the localization of data and can help reduce latency for some customers. You can use multiple instances within a cluster or read replicas working together to process requests to balance connectivity and throughput within an architecture.

The architecture’s ability to scale as demand increases helps to maintain availability. Many services can scale in multiple ways. This gives you the ability to choose the scaling that is best suited to the workload that you are running.

#### Distributions
To meet the demand that internet-scale applications place on their supporting databases, you can distribute data. There are many different solutions for distributing data, including the following  four methods:
* Data distribution 
 1. Partitioning
 2. Sharding
* Database distribution 
 3. Database federation
 4. Clustering

The distribution method is not visible to anyone using the database in any of the four options.

#### Data distribution
##### Partitioning
Partitioning is the process of splitting a large table into smaller entities. 

##### Sharding
Sharding is a horizontal partition that stores a large database across multiple machines. A single machine, or database server, can store and process only a limited amount of data. Database sharding overcomes this limitation by splitting data into smaller chunks, called shards, and storing them across several database servers. Most database servers have the same underlying technologies, and they work together to store and process large volumes of data.

#### Database distribution
##### Federation
With a federated database distribution, several databases work together as a single unit.

##### Clustering
With a clustered database, several servers or instances are clustered and connected to a single database. All the servers are synchronized so that each node is going to have exactly the same data as all the other nodes.

**Not all AWS database services support all four methods.**

#### Database and application scaling
Scaling up and out are two common approaches for this.

##### Scale up
To **scale up**, you increase the available resources on the system that is hosting the databases. With AWS, this means resizing the instance.

##### Scale out
To **scale out**, you scale horizontally and increase the capacity of a system. An example of this is adding replicas of the database to distribute the data. Each instance contains a complete copy of the data.

#### Knowledge Check
##### Which application scaling approach involves adding replicas of databases to distribute data?
* Scaling out

When scaling out, you add replicas of the database to distribute the data. By distributing the data across multiple systems, you begin to run into issues of consistency, availability, efficiency, query or pattern flexibility, and infinite scale. 
* **Scaling up**: You increase the available resources on the system that is hosting the databases. With AWS, this means resizing the instance.
* **Sharding**: You store a large database across multiple machines and split data into smaller chunks that are stored across several database servers. 
* **Clustering**: With a clustered database, several servers or instances are clustered and connected to a single database.

##### Column A in Table A is used to uniquely distinguish one row, or record, from another. That column is also inserted into Table B. What is the term for that column in Table A and in Table B respectively?
* In Table A it is the primary key and in Table B it is the foreign key.

* **Primary key**: Each row has an identifier column or group of columns that uniquely distinguishes the record from other records in the table. The value in the identifier column is called the primary key. 
* **Foreign key**: A table can reference another table's primary key; in which case it is called the foreign key.

##### Which distribution solution has several databases work together as a single unit?
* Federation

* **Clustering**: With a clustered database, several servers or instances are clustered and connected to a single database.
* **Partitioning**: A partition is an allocation of storage for a table, backed by SSDs and automatically replicated across multiple Availability Zones within an AWS Region. Partition management is handled entirely by Amazon DynamoDB—you never have to manage partitions yourself.
* **Sharding**: With sharding, a large database is stored across multiple machines. Database sharding splits data into smaller chunks, called shards, and stores them across several database servers.

#### SQL
#### Practice environment schema
To illustrate how to use the SQL commands, you will work on a database example throughout this topic. The database contains the following tables:
* Rating table
* User table
* Movie table

##### Table explanations
* The **rating** table will have four columns, or fields, with set types: id (int), rating (float), user_id (int), and movie_id (int).
* The **user** table will have four columns, or fields, with set types: id (int), first_name (varchar), last_name (varchar), and email (varchar).
* The **movie** table will have three columns, or fields, with set types: id (int), description (varchar), and genre (varchar).

The **rating** table is linked to the **user** table by a field called **user_id** that links to the **id** field of the **user** table. The **rating** table is also linked to the **movie** table: the **movie_id** field of the **rating** table is linked to the **id** field of the **movie** table.

#### Data types
Every column in a relational database's table must have a name and singular type of data. The following are the three main categories of data types, along with examples of the types of data included in each:

##### Date and time:
**DATE** – The supported format for dates is YYYY-MM-DD.

**TIMESTAMP** – Timestamp is formatted as YYYY-MM-DD hh:mm:ss. These values are stored as the number of seconds since the UNIX epoch, which was January 1, 1970.

**YEAR** – Years are written in the 4-year format.

##### Numeric: 
**int** – These are whole numbers between -2,147,483,648 and 2,147,483,647.

**decimal** – This is used when it is important to be precise. When declaring a decimal, the precision and scale must be provided. The precision is number of digits that are used total, and the scale is the number of digits that can follow the decimal point. 

##### String:
**text** is a string of characters.

**char** is a string that has a fixed width. The width is declared with the string.

**varchar** is a string with a variable width. A maximum can be set when the varchar is declared.

#### Types of Data Language Used in SQL
##### Data definition language (DDL)
Statements included in this category are used for the creation and modification of database objects, such as the following: 
* Tables
* Users accessing a database
* Database indexes

Some examples of DDL statements are CREATE, ALTER, DROP, and RENAME.

##### Data manipulation language (DML)
Statements included in this category are used for changing database objects. Some examples of DML statements are SELECT, INSERT, and UPDATE.

##### Data control language (DCL)
Statements included in this category are used to manage authorization to information within databases. GRANT and REVOKE are examples of DCL statements.

#### LAB
##### Creating and using a database
```
CREATE DATABASE DatabaseName;
```

```
USE DatabaseName;
```

##### Creating a table
Next to each column name parameter is the data type parameter. If the table has a primary key, PRIMARY KEY and NOT NULL are used after the column name and data type parameters. If a foreign key is used, FOREIGN KEY is used at the start of that column definition.

```
CREATE TABLE table_name (
    columnname 1 datatype PRIMARY KEY NOT NULL,
    FOREIGN KEY columnname2 datatype,
    columnname3 datatype,
   ....
);
```

##### SQL constraints
PRIMARY KEY, FOREIGN KEY, and NOT NULL are examples of SQL constraints. The other three SQL constraints are the following:
* DEFAULT is used to set a default value for a column. This value is added to each new record, unless something else is provided.
* CHECK is used to limit a value range. When used with a column, it will allow only certain values for that column. When used with a table, it limits the values in certain columns based on values in other columns in the row. 
* UNIQUE ensures that all values provided in a column are different from each other.

```
CREATE TABLE user
(
id INT PRIMARY KEY NOT NULL,
first_name VARCHAR(100),
last_name VARCHAR(100),
email VARCHAR(225)
);
```

Now, do the same with the movie and rating tables. Notice in the rating table, the id fields from both the movie and user tables are used, so they have the following characteristics:
* FOREIGN KEY is used at the start of the column definition.
* The columns are named user_id and movie_id by convention but they can be named whatever you like.
* REFERENCES is used, and then table_name(id) to point to the other table.

```
CREATE TABLE movie
(
id INT PRIMARY KEY NOT NULL,
name VARCHAR(100),
description TEXT,
genre VARCHAR(100)
);
```

```
CREATE TABLE rating
(
id INT PRIMARY KEY NOT NULL,
rating FLOAT,
user_id INT,
movie_id INT,
FOREIGN KEY (user_id) REFERENCES user(id),
FOREIGN KEY (movie_id) REFERENCES movie(id)
);
```

##### Inserting data into the tables
```
INSERT INTO user (id, first_name, last_name, email) VALUES (1, 'John', 'Doe','john.doe@example.com');
INSERT INTO user (id, first_name, last_name, email) VALUES (2, 'Jane','Doe','jane.doe@example.com');
INSERT INTO user  (id, first_name, last_name, email) VALUES (3,'Martha','Rivera','m.rivera@example.com');
INSERT INTO user (id, first_name, last_name, email) VALUES (4,'Li','Juan','li.juan@example.com');
```

```
SELECT * FROM user;
```
OR
```
SELECT first_name, last_name FROM user;
```

```
INSERT INTO movie (id,name,genre)
VALUES (1,'Back to the Future','SciFi');
INSERT INTO movie (id,name,genre)
VALUES (2,'Star Wars','SciFi');
INSERT INTO movie (id,name,genre)
VALUES (3,'Titanic','Drama');
INSERT INTO movie (id,name,genre)
VALUES (4,'The Lord of the Rings','Fantasy');
```

###### Escaping
In this instance, the way to create an escape for the single quote is to use an additional single quote.
```
INSERT INTO movie VALUES (5,'The Shawshank Redemption',NULL,'Drama');
INSERT INTO movie VALUES (6,'Harry Potter and the Philosopher''s Stone',NULL,'Fantasy');
INSERT INTO movie VALUES (7,'The Hobbit',NULL,'Fantasy');
INSERT INTO movie VALUES (8,'The Fifth Element',NULL,'SciFi');
```

```
INSERT INTO rating (id, rating, user_id, movie_id) VALUES (1,4.5,1,1);
INSERT INTO rating (id, rating, user_id, movie_id) VALUES (2,4.7,2,2);
INSERT INTO rating (id, rating, user_id, movie_id) VALUES (3,4.6,2,3);
INSERT INTO rating (id, rating, user_id, movie_id) VALUES (4,4.8,3,4);
INSERT INTO rating (id, rating, user_id, movie_id) VALUES (5,4.2,4,5);
INSERT INTO rating (id, rating, user_id, movie_id) VALUES (6,4.5,4,6);
INSERT INTO rating (id, rating, user_id, movie_id) VALUES (7,4.4,3,7);
INSERT INTO rating (id, rating, user_id, movie_id) VALUES (8,4.1,3,8);
```

##### 2 ways to insert
1. With both the column names and the values.
```
INSERT INTO TableName (columnname1, columnname2, columnname3, ...)
VALUES (value1, value2, value3, ...);
```

2. With values for all columns in the table.
```
INSERT INTO TableName
VALUES (value1, value2, value3, ...);
```

```
INSERT INTO movie (id,name,genre)
VALUES (9,'The Little Rascals',NULL),
(10,'The Smurfs',NULL);	
```

#### Selecting Data with SQL Operators

#### WHERE clause
The WHERE clause is used to filter records and extracts only records that fulfill a specified condition.

```
SELECT columnname1, columname2, ...
FROM TableName
WHERE condition;
```

Conditions can be things like WHERE a specific country or countries is entered. Conditions are set by using the column name and an operator. The following are examples of operators used in conditions:
* = Equal
* > Greater than
* >= Greater than or equal
* > Less than
* >= Less than or equal
* <> Not equal (In some versions of SQL, != is used instead.)
* BETWEEN (between a range)
* LIKE (search for a pattern)
* IN (multiple possible values for a column)

**Depending on the database configuration, the value of a string in a column might be case sensitive. That means that 'John' is not the same as 'john'.**

```
SELECT * FROM user WHERE first_name = 'John';
```

```
SELECT * FROM user WHERE last_name = 'Doe';
```

The WHERE clause is not only used in SELECT statements; it is also used in statements such as UPDATE, DELETE, and more. **You might accidentally update or delete all the rows in your table** if you forget to use the WHERE clause.

#### Additions to WHERE
##### OR statements
In an OR statement, a record is displayed if it returns TRUE for any of the conditions separated by an OR.
```
SELECT * FROM columnname1 WHERE condition OR condition;
```

##### AND statements
The AND statement is used to select records that return TRUE for all the conditions separated by AND. 
```
SELECT * FROM columnname1 WHERE condition AND condition;
```

```
SELECT * FROM user WHERE first_name = 'John' OR first_name = 'Jane';
```

```
SELECT * FROM user WHERE first_name = 'John' AND last_name = 'Doe';
```

```
SELECT * FROM user WHERE (first_name = 'John' AND last_name = 'Doe') OR last_name = 'Rivera';
```

#### Sorting Data

##### ORDER BY
The **ORDER BY** statement sorts the records based on the values of a column in ascending (ASC) or descending (DESC) order. In most engines, ORDER BY sorts records in ascending order by default. You would then use ASC to reorder it back to ascending order after you have used DESC.

```
SELECT columnname1, columnname2, ...
FROM TableName
ORDER BY column1, column2, ... ASC|DESC;
```

```
SELECT name, genre
FROM movie
ORDER BY genre ASC;
```

**NULL values can be put either at the top or at the bottom of a table when using an ORDER BY statement, depending on the database engine type.**

#### Modifying Data
##### UPDATE the data
The UPDATE statement lets you SET a new value for a field WHERE a condition is met.

```
UPDATE movie
SET genre = 'Drama'
WHERE name = 'Back to the future';
```

##### DELETE records
DELETE operation deletes a record when a condition is met. 

```
DELETE from rating where movie_id = 1;
DELETE FROM movie WHERE name = 'Back to the future';
```

##### DROP a table
A table can be removed by using the DROP TABLE command

It is also possible to remove your entire database by using the DROP DATABASE command. The command can be used like this:
```
DROP DATABASE DatabaseName;
```

#### Joining Two Tables
##### INNER JOIN
INNER JOIN returns only the rows with matching values between table 1 and table 2 on the join condition. 

If we take our movie and rating tables for example, we can try to combine these tables to get the ratings for each movie with its name and genre.

```
SELECT columnname(s)
FROM TableName1
INNER JOIN TableName2
ON TableName1.columnname = TableName2.columnname;
```

```
SELECT m.name, m.genre, r.rating as score
FROM movie m
INNER JOIN rating r
ON m.id = r.movie_id;
```

As you can see on the command, the movie and rating tables are shortened m and r respectively. This type of writing can save a lot of time when writing complex queries.

Additionally, it is possible to rename the columns in the SELECT statement by using the word AS. This is the result of the query:

```
+------------------------------------------+---------+-------+
| name                                     | genre   | score |
+------------------------------------------+---------+-------+
| Back to the Future                       | Drama   |   4.5 |
| Star Wars                                | SciFi   |   4.7 |
| Titanic                                  | Drama   |   4.6 |
| The Lord of the Rings                    | Fantasy |   4.8 |
| The Shawshank Redemption                 | Drama   |   4.2 |
| Harry Potter and the Philosopher's Stone | Fantasy |   4.5 |
| The Hobbit                               | Fantasy |   4.4 |
| The Fifth Element                        | SciFi   |   4.1 |
+------------------------------------------+---------+-------+
8 rows in set (0.00 sec)
```

In the result, only eight distinct movies are being listed. Only these movies have been rated in the rating table. 

##### LEFT JOIN
LEFT JOIN returns all rows from table 1, and values from table 2 will be included when the join conditions match. Missing values from table 2 will be set to NULL by default.

```
SELECT columnname(s)
FROM TableName1
LEFT JOIN TableName2
ON TableName1.columnname = TableName2.columnname;
```

```
SELECT m.name, m.genre, r.rating as score
FROM movie m
LEFT JOIN rating r
ON m.id = r.movie_id;
```

This is the result of the query. In the result, all the movies present in the movie table are selected. However, only the movies that have been rated have a rating in the table; the others have a NULL value.

```
+------------------------------------------+---------+-------+
| name                                     | genre   | score |
+------------------------------------------+---------+-------+
| Back to the Future                       | Drama   |   4.5 |
| Star Wars                                | SciFi   |   4.7 |
| Titanic                                  | Drama   |   4.6 |
| The Lord of the Rings                    | Fantasy |   4.8 |
| The Shawshank Redemption                 | Drama   |   4.2 |
| Harry Potter and the Philosopher's Stone | Fantasy |   4.5 |
| The Hobbit                               | Fantasy |   4.4 |
| The Fifth Element                        | SciFi   |   4.1 |
| The Little Rascals                       | NULL    |  NULL |
| The Smurfs                               | NULL    |  NULL |
+------------------------------------------+---------+-------+
10 rows in set (0.01 sec)
```

##### RIGHT JOIN
RIGHT JOIN returns all rows from table 2, and values from table 1 will be included when the join conditions match. Missing values from table 1 will be set to NULL by default. 

```
SELECT columnname(s)
FROM TableName1
RIGHT JOIN TableName2
ON TableName1.columnname = TableName2.columnname;
```

```
SELECT m.name, m.genre, r.rating as score
FROM movie m
RIGHT JOIN rating r
ON m.id = r.movie_id;
```

A RIGHT JOIN of these tables would return the following results. Because The Little Rascals and The Smurfs do not have ratings in the rating table, they are not a part of the results.

```
+------------------------------------------+---------+-------+
| name                                     | genre   | score |
+------------------------------------------+---------+-------+
| Back to the Future                       | Drama   |   4.5 |
| Star Wars                                | SciFi   |   4.7 |
| Titanic                                  | Drama   |   4.6 |
| The Lord of the Rings                    | Fantasy |   4.8 |
| The Shawshank Redemption                 | Drama   |   4.2 |
| Harry Potter and the Philosopher's Stone | Fantasy |   4.5 |
| The Hobbit                               | Fantasy |   4.4 |
| The Fifth Element                        | SciFi   |   4.1 |
+------------------------------------------+---------+-------+
8 rows in set (0.00 sec)
```

##### FULL OUTER JOIN
FULL OUTER JOIN returns all rows from both tables. Missing values on the join condition from either side will be set to NULL by default.

```
SELECT columnname(s)
FROM TableName1
FULL OUTER JOIN TableName2
ON TableName1.columnname = TableName2.columnname
WHERE condition;
```

**Not all database engines support FULL OUTER JOIN statements.**

#### GROUP BY and Aggregate Functions
Aggregate functions return a single value after performing a calculation on a set of values. Except for **COUNT(*)** , aggregate functions ignore null values.

This section will explore the following aggregate functions: 
* **COUNT**
* **SUM**
* **AVG**

##### GROUP BY statement
The GROUP BY statement serves the following primary purposes:
* You can group rows that have the same values into summary rows.
* When used with aggregate functions, like **COUNT()**, **MAX()**, **MIN()**, **SUM()**, and **AVG()**, GROUP BY can group result sets by one or more columns.

The GROUP BY clause of the SELECT statement is often used with aggregate functions. When used, GROUP BY creates a summary row for rows that have the same values, such as finding the number of students from a specific state. 

```
SELECT columnname(s)
FROM TableName
WHERE condition
GROUP BY columnname(s)
ORDER BY columnname(s);
```

##### COUNT function
The **COUNT()** function returns the number of rows that matches a specified criterion. You can add a WHERE clause to specify conditions such as returning the number of entries for a given column (for example, State) WHERE the state entered is Rhode Island (for example, WHERE State = Rhode Island).

```
SELECT COUNT(columnname)
FROM TableName
WHERE condition;
```

```
SELECT COUNT(name), genre FROM movie WHERE genre = 'SciFi';
```

```
+-------------+-------+
| COUNT(name) | genre |
+-------------+-------+
|           2 | SciFi |
+-------------+-------+
1 row in set (0.00 sec)
```

It is also possible to use the COUNT function on aggregated data by using the GROUP BY statement.

This statement returns the following result. Here, the GROUP BY statement aggregates the data and the **COUNT** function counts the number of records in each group.

```
SELECT COUNT(name), genre
FROM movie
GROUP BY genre;
```

##### It is also possible to add a condition in aggregated data by using the HAVING statement
```
SELECT COUNT(name) AS nb_movies, genre
FROM movie
GROUP BY genre
HAVING nb_movies > 2
ORDER BY genre DESC;
```

Here the result only displays the genres that have a number of movies higher than two.

```
+-----------+---------+
| nb_movies | genre   |
+-----------+---------+
|         3 | Fantasy |
|         3 | Drama   |
+-----------+---------+
2 rows in set (0.01 sec)
```

##### COUNT and DISTINCT
Using the DISTINCT keyword with the COUNT function ignores duplicates. This will return a count of only unique values. For instance, if you want to return the number of unique states in a table called StudentInfo, you could could use DISTINCT in the following way:

```
SELECT COUNT(DISTINCT State)
FROM StudentInfo;
```

##### SUM function
The **SUM()** function returns the total sum of a numeric column. It can also use WHERE to set conditions.

```
SELECT SUM(columnname)
FROM TableName
WHERE condition;
```

```
SELECT genre, SUM(rating) AS sum_ratings
FROM movie
INNER JOIN rating
ON movie.id = rating.movie_id
GROUP BY genre ORDER BY sum_ratings DESC;
```

The genre Fantasy has the highest number because it has the most records in the movie table.

```
+---------+--------------------+
| genre   | sum_ratings        |
+---------+--------------------+
| Fantasy | 13.700000286102295 |
| Drama   | 13.299999713897705 |
| SciFi   |  8.799999713897705 |
+---------+--------------------+
3 rows in set (0.00 sec)
```

##### AVG function
The **AVG()** function returns the average value of a numeric column. It can also use WHERE to set conditions.

```
SELECT AVG(columnname)
FROM TableName
WHERE condition;
```

```
SELECT genre, AVG(rating) AS average_ratings
FROM movie
INNER JOIN rating ON movie.id = rating.movie_id
GROUP BY genre
ORDER BY average_ratings DESC;
```
In the result, you can see that Fantasy has the highest average rating, but the number is 4.566666762034099 and not 13.700000286102295 because we are taking the average of all the movie records with the genre Fantasy instead of adding the averages together.

```
+---------+--------------------+
| genre   | average_ratings    |
+---------+--------------------+
| Fantasy |  4.566666762034099 |
| Drama   |  4.433333237965901 |
| SciFi   | 4.3999998569488525 |
+---------+--------------------+
3 rows in set (0.00 sec)
```

##### Using operators with AVG
Operators can be used with the AVG function to return values that are in relation to the average. In the following example, all values greater than the AVG are returned.

```
SELECT * FROM TableName
WHERE columnname > (SELECT AVG(columnname) FROM TableName);
```

##### MIN and MAX functions
The **MIN()** function returns the smallest value of the selected column and **MAX()** returns the largest value of the selected column.

```
SELECT MIN(columnname)
FROM TableName
WHERE condition;
```

#### Common Table Expressions
Common table expressions (CTEs) allow users to create tables that exist only during the life of the query. They are not persisted on disk. These tables can be used immediately within the query. This is useful when you want to work with a subset of a table or within a joined set of tables.

Imagine that you want to create a table that selects the rating for each movie. You will then query this table to extract only the movies that have a rating higher than or equal to 4.5.

When creating a transient table, WITH NewTableName is used with the AS (SELECT selectExpression) statement to create the table. Then it becomes possible to query this table by using a SELECT expression as you would normally do with a regular table. 

```
WITH bestmovie AS
(SELECT name, genre, rating
FROM movie
INNER JOIN rating 
ON movie.id = rating.movie_id
GROUP BY name, genre
ORDER BY rating DESC
)
SELECT name, rating
FROM bestmovie
WHERE rating >= 4.5;
```

In this code, the WITH NewTableName AS (SELECT selectExpression) statement is used to create the transient table (here: bestmovie). Then it becomes possible to query the table by using a SELECT expression as you would normally do with a regular table. 

Here is the result of this query. You get the two records for which the rating is higher than or equal to 4.5.

```
+------------------------------------------+--------+
| name                                     | rating |
+------------------------------------------+--------+
| The Lord of the Rings                    |    4.8 |
| Star Wars                                |    4.7 |
| Titanic                                  |    4.6 |
| Back to the Future                       |    4.5 |
| Harry Potter and the Philosopher's Stone |    4.5 |
+------------------------------------------+--------+
5 rows in set (0.00 sec)
```

It is also possible to declare multiple tables that exist solely for the life of a query. Imagine that you want to have the movie names and their corresponding rating, as well as the first names and last names of people who rated the movies. You will declare two transient tables for this.
* **The bestmovie table**: This is very similar to the one used in the previous example. It includes the movie ID, name, genre, and rating of the movies.
* **The userandmovie table**: This includes the user IDs, the first and last names of the users, as well as the movie IDs corresponding to their rated movies.

This is the current content of the bestmovie table:

| movie_id | name | genre | rating |

And, this is the current content of the userandmovie table:

| userid1 | first_name | last_name | movie_id |

```
With bestmovie AS
(SELECT movie.id AS movieid, name, rating
FROM movie INNER JOIN rating
ON movie.id = rating.movie_id
GROUP BY movieid, name
),
userandmovie AS
(SELECT user.id AS userid, first_name, last_name, movie_id
FROM user
INNER JOIN rating ON user.id = user_id
)
SELECT name, rating, first_name, last_name
FROM bestmovie bm inner join userandmovie um on bm.movieid = um.movie_id;
```

```
+------------------------------------------+--------+------------+-----------+
| name                                     | rating | first_name | last_name |
+------------------------------------------+--------+------------+-----------+
| Back to the Future                       |    4.5 | John       | Doe       |
| Star Wars                                |    4.7 | Jane       | Doe       |
| Titanic                                  |    4.6 | Jane       | Doe       |
| The Lord of the Rings                    |    4.8 | Martha     | Rivera    |
| The Shawshank Redemption                 |    4.2 | Li         | Juan      |
| Harry Potter and the Philosopher's Stone |    4.5 | Li         | Juan      |
| The Hobbit                               |    4.4 | Martha     | Rivera    |
| The Fifth Element                        |    4.1 | Martha     | Rivera    |
+------------------------------------------+--------+------------+-----------+
```

CTEs can be very useful when it comes to complex queries. They help you work with subsets of tables and simplify the final query.

CTEs are also often used to increase the efficiency of a query. By driving efficiency in your queries, you create more **sustainable workloads**.

#### Summary
#### Types of data language used in SQL
##### DDL
Statements included in this category are used for the creation and modification of database objects, such as the following:
* Tables
* Users accessing a database
* Database indexes 

Some examples of DDL statements are CREATE, ALTER, DROP, and RENAME.

##### DML
Statements included in this category are used for changing database objects. Some examples of DML statements are SELECT, INSERT, and UPDATE.

##### DCL
Statements that fall under this category are used to manage authorization to information within databases. GRANT and REVOKE are examples of DCL statements.

#### SQL constraints
* PRIMARY KEY is the value in the identifier column of a table. 
* FOREIGN KEY is when another table's primary key is used in a different table.
* NOT NULL ensures that field contains data and is not left blank.
* DEFAULT is used to set a default value for a column. This value is added to each new record, unless something else is provided. 
* CHECK is used to limit a value range. When used with a column, it will allow only certain values for that column. When used with a table, it limits the values in certain columns based on values in other columns in the row. 
* UNIQUE ensures that all values provided in a column are different from each other. 

#### SQL statements
##### Creating and using a database
The following statement is used to create a database.
```
CREATE DATABASE DatabaseName;
```

The following statement is used to access a database.
```
USE DatabaseName;
```

##### Creating and viewing tables
The following statement is an example of how to create a table in a database.
```
CREATE TABLE table_name (
    columnname1 datatype PRIMARY KEY NOT NULL,
    FOREIGN KEY columnname2 datatype,
    columnname3 datatype,
   ....
);
```

The following statement is used to view a table.
```
SELECT * FROM TableName;
```

##### Inserting data into tables
```
INSERT INTO TableName (columnname1, columnname2,...)
VALUES (valueA, valueB, valueC, ...);
```

Using SELECT * is not recommended for efficient SQL queries because it returns every column. It is best to use more precise SELECT queries to improve the speed of the query. Therefore, you should specify only the columns that you need to retrieve in the SELECT statement.  

Additionally, you want to filter the rows to retrieve only those that you will need. Aiming for the most efficient query possible can help increase the sustainability of your workloads. 

#### WHERE clause
The WHERE clause is used to filter records, and it extracts only records that fulfill a specified condition.
```
SELECT columnname1, columname2, ...
FROM TableName
WHERE condition;
```

Conditions can be things like WHERE a specific country or countries is entered. Conditions are set by using the column name and an operator. The following are examples of operators used in conditions:
* Equal =
* Greater than >
* Less than <

The WHERE clause is not only used in SELECT statements. It is also used in statements such as UPDATE, DELETE, and more. This is important because you might accidentally update or delete all the rows in your table if you forget to use the WHERE clause. You can also use OR and AND statements with WHERE.

##### ORDER BY
The ORDER BY statement sorts the records based on the values of a column in ascending (ASC) or descending (DESC) order. In most engines, ORDER BY sorts records in ascending order by default. You would then use ASC to reorder it back to ascending order after you have used DESC.
```
SELECT columnname1, columnname2, ...
FROM TableName
ORDER BY column1, column2, ... ASC|DESC;
```

##### Modifying data
The UPDATE statement lets you SET a new value for a field WHERE a condition is met. 
```
UPDATE TableName
SET columname1 = valueA, columname2 = valueB, ...
WHERE condition;
```

##### The DELETE statement is used to delete existing records in a table.
```
DELETE FROM TableName WHERE condition;
```

If you do not need a table anymore, you can remove it by using the DROP TABLE command.
```
DROP TABL TableName
```

##### Joins
When tables are linked to each other, it becomes possible to make queries that combine rows from several tables by using the JOIN statement.

There are several ways to join tables:
* INNER JOIN
* LEFT JOIN
* RIGHT JOIN
* FULL OUTER JOIN

##### GROUP BY and aggregate functions
Aggregate functions return a single value after performing a calculation on a set of values. Except for COUNT(*) , aggregate functions ignore null values. 

The GROUP BY clause of the SELECT statement is often used with aggregate functions. When used, GROUP BY creates a summary row for rows that have the same values, such as finding the number of students from a specific state. 

```
SELECT columnname(s)
FROM TableName
WHERE condition
GROUP BY columnname(s)
ORDER BY columnname(s);
```

The following are the aggregate functions:
* COUNT (can be used with DISTINCT)
* SUM
* AVG (can be used with operators)
* MIN

##### CTEs
Common table expressions (CTEs) allow users to create tables that exist only during the life of the query. They are not persisted on disk. These tables can be used immediately within the query. This is useful when you want to work with a subset of a table or within a joined set of tables.

When creating a temporary table, WITH TemporaryTableName is used with the AS (SELECT selectExpression) statement to create the temporary table. Then it becomes possible to query the temporary table by using a SELECT expression as you would normally do with a regular table. 

#### Working with Amazon RDS
#### Pre-assessment
##### A company needs to perform complex data analysis and reporting on a set of data gathered from real-time transactions. Which kind of data processing is used for complex the data analysis and reporting, and which type is for managing real-time transactions?
* Online analytic processing (OLAP) is for complex data analysis and reporting, and online transaction processing (OLTP) is for managing real-time transactions.

##### Which statement describes how Amazon RDS provides high availability?
* Amazon RDS automatically provisions and maintains a synchronous standby replica in a different Availability Zone

##### Which Amazon RDS database engine is cloud native?
* Amazon Aurora MySQL-Compatible Edition

#### Amazon RDS Deep Dive

#### Amazon Relational Database Service (Amazon RDS)
With Amazon RDS, you can achieve the following:
* Remove inefficient and time-consuming database administrative tasks without needing to provision infrastructure or maintain software.
* Deploy and scale the relational database engines of your choice in the cloud or on premises.
* Achieve high availability with Amazon RDS Multi-AZ deployments.
* Benefit from over a decade of proven operational expertise, security best practices, and innovation in databases.

By moving to a fully managed service, you can pass on the burden of repetitive tasks, such as the following, to AWS:
* Backup and restore operations
* Software installations and patching
* Managing hardware that supports the server

#### Use cases for Amazon RDS
##### Build web and mobile applications
You can use Amazon RDS to support applications that are increasing in size or traffic with high availability, throughput, and storage scalability. 

Amazon RDS makes it so you can take advantage of flexible pay-per-use pricing to suit various application usage patterns.

##### Move to managed databases
You can innovate and build new applications with Amazon RDS instead of worrying about self-managing your databases, which can be time consuming, complex, and expensive.

##### Break free from legacy databases
Amazon RDS helps you move away from expensive commercial databases by migrating to Amazon Aurora.

When you migrate to Aurora, you get the scalability, performance, and availability of commercial databases at 1/10th the cost.

#### Available engines
Amazon RDS is available on several database instance types—optimized for memory, performance, or I/O—and provides you with seven familiar database engines to choose from. You can use **AWS Database Migration Service (AWS DMS)** to migrate or replicate your existing databases to Amazon RDS.

| Commercial | Open Source | Cloud Native |
| ---------- | ----------- | ------------ |
| Microsoft SQL Server | PostgreSQL | Amazon Aurora PostgreSQL-Compatible Edition |
| Oracle | MySQL | Amazon Aurora MySQL-Compatible Edition |
| | MariaDB | |

#### Amazon RDS Specific Design Considerations

#### DB instances
* Database environment with specific compute and storage
* Can contain multiple user-created databases
* AWS Management Console, AWS comand line tools, Amazon RDS API operations

#### DB instance classes
* **Burstable instances**. An amount of CPU is flexible. It can expand or contract based on actual usage. The amount of power that you have is chosen by the instances size and the instances type can choose the balance of that power.
* **General-purpose instances** have a balance of CPU and memory.
* **Memory-optimized instances** have more memory generally.

#### DB instance storage classes
* **General purpose block storage** has again a balance of speed and price.
* **Provisioned IOPS** - for I/O intensive workloads.
* **Magnetic** are available for backwards compatinility.

#### Modifying a DB instance class
1. Preset stirage scaling configurations.
2. If needed, change the DB instance class to change preset configurations.
3. Always test any changes on a test instance first.
4. Decide if modifications apply immediately or during scheduled maintenance window.

#### DB instance configuration examples.
##### Workload 1
Requirements:
* Balance of compute, memory, and networking for a broad rabge of general workloads.
* Single digit millisecond latencies and ability to burst to 3,000 IOPS.

DB configuration:
* Instance class: Standard.
* Storage types: General Purpose.

##### Workload 2
Requirements:
* BMemory-intensive application with high compute capacity and high memeory footprint.
* Fast and consistent I/O performance.

DB configuration:
* Instance class: Memory Optimized.
* Storage types: Provisioned IOPS.

#### Amazon RDS monitoring considerations
* **Amazon CloudWatch**. Amazon RDS service allows us to roll up database specific metrics and allow us to make decisions based on those metrics.
* **Amazon RDS Performance Insights**. The Amazon RDS Performance Insights dashboard gives us performance insights around the database usage, query usage, optimization and helps us make that database run better.
* **Enhanced Monitoring**. It can be turned on to get more detailed results all the way down to second variability or granularity with respect to those metrics and allows us to get a much clearer picture of what we need.

#### DB instance control access
* **Password authentication**. It's a default option. A database admin user and a database admin password can be set at database creation time. Now, when you have created a database, especially relational databases, the authentication and authorization is done inside that database, often as just one of the tables that's stored in that database.
* **AWS Identity and access management (IAM)** - linking IAM users and roles into a database for authentication purpose.
* **Kerberos authentication** is often used with services like Microsoft Active Directory, which uses that Kerberos model which allows you to map users inside of a Kerberos controlled identity source and your database. 

**These [above] are all authentication models. The authorization is still done in that database engine.**

#### DB Instance networking
* It exists in a VPC.
 * Allows using routing to isolate a database into a specific subnet.
 * Allows you to leverage security groups and network ACLs to control traffic to come in and out of that subnet or into that database instance itself.
 * Allows you to leverage the connections that that VPC has.

#### Amazon RDS design considerations
##### Database engines
Amazon RDS is continually working to support new versions of each database engine. You can have up to 40 Amazon RDS DB instances. Of these 40, up to 10 can be Oracle or SQL Server DB instances under the License Included model. All 40 DB instances can be used for MySQL, MariaDB, or PostgreSQL. You can also have 40 DB instances for SQL Server or Oracle under the Bring Your Own License (BYOL) licensing model. If your application requires more DB instances, you can request additional DB instances.

##### Instance type and sizing
Some database engines support additional database instance classes.

| Type | Burstable instances | General-purpose instances | Memory-optimized instances |
| ---- | ------------------- | ------------------------- | -------------------------- |
| Size | Between 1 vCPU for every 1 gibibyte (GiB) RAM and 8 vCPU for every 32 GiB RAM | Between 2 vCPU for every 8 GiB RAM and 128 vCPU for every 512 GiB RAM | Between 2 vCPU for every 16 GiB RAM and 128 vCPU for every 4096 GiB RAM |
| Networking | Moderate performance | High performance | High performance |
| Workload | Good for smaller or variable workloads | Good for running general-purpose workloads | Good for query-intensive workloads or high connection counts |
| Highlights | T3, T4 configured for unlimited mode, can burst above baseline for extra charge | Balanced compute, memory, and networking | Lower cost per GiB of memory |

##### Backup and recovery
* **Automated backups**: Amazon RDS creates and saves automated backups (system snapshots and transaction logs) of your DB instance. Amazon RDS creates a storage volume snapshot of your DB instance, backing up the entire DB instance and not just individual databases.
* **Database snapshots**: You can also back up your DB instance manually, by manually creating a DB snapshot. The first snapshot of a DB instance contains the data for the full DB instance. Subsequent snapshots of the same DB instance are incremental, which means that only the data that has changed after your most recent snapshot is saved.
* **Backup retention period**: You can set the backup retention period when you create a DB instance. If you don't set the backup retention period, the default backup retention period is 1 day, if you create the DB instance using the Amazon RDS API or the AWS Command Line Interface (AWS CLI). The default backup retention period is 7 days if you create the DB instance by using the console. After you create a DB instance, you can modify the backup retention period. You can set the backup retention period to between 0 and 35 days.
* **Backup storage**: Your Amazon RDS backup storage for each Region is composed of the automated backups and manual DB snapshots for that Region. Your backup storage is equivalent to the sum of the database storage for all instances in that Region. Moving a DB snapshot to another Region increases the backup storage in the destination Region.
* **Database native backup options**: The database engine that you have chosen contains its own native solution for backups and snapshot. Amazon RDS does not interfere with these operations should you choose to implement them.
* **AWS Backup**: You can also use AWS Backup to manage backups of Amazon RDS DB instances. The AWS Backup service provides a centralized backup console that offers backup scheduling, retention management, and backup monitoring.

#### Case study: Intuit Mint
Intuit Mint (Mint.com) is a free personal financial management service used by more than six million consumers in the United States and Canada. The service connects a customer’s financial information—such as bank accounts, credit cards, and bills—and presents the information in a single place. 

Mint.com automatically updates and categorizes information in real time, so customers can perform the following actions:
* View the status of their finances
* Track their spending
* Monitor their investments

Mint.com also provides bill reminders and payment services, so that people can not only see their finances, but also take action on them.

##### The challenge
Mint.com was originally hosted in an internal data center, but wanted to make these changes:
* Improve its ability to scale up or down to meet peak traffic demands:
* Put more of its resources into new software development:

##### AWS services used
###### Amazon EC2
Mint initially migrated more than 100 MySQL instances to Amazon Elastic Compute Cloud (Amazon EC2). Approximately 1 year later, the company shut down the data center that it had previously used to host Mint.com and shifted its focus to optimizing its applications on AWS.

###### Amazon CloudFront
Amazon CloudFront is a global content-delivery network (CDN) service designed to speed the delivery of websites and other web assets.

###### Amazon RDS
As part of this optimization effort, the company migrated its MySQL instances from Amazon EC2 to Amazon Relational Database Service (Amazon RDS) for MySQL. 

###### AWS CloudFormation
Mint also uses AWS CloudFormation templates to give the company’s administrators a way to easily provision and manage its AWS resources.

##### Benefits of the migration
###### Cost reduction
Mint.com was able to reduce operational costs by 25 percent. They no longer need to tune the server and IOPS to improve database performance or worry about hardware-acquisition costs.

###### Faster failover intervention
The change to Amazon RDS for SQL also means that the team no longer has to perform manual interventions for failover scenarios. These often took up to 30 minutes but now only takes 1 minute.

###### Ease of development
Database administrators have reduced time spent on database-support activities by about 15 percent because they no longer have to perform basic administrative tasks. This means that they can focus on building better products.

The Mint.com migration into the cloud also provided some additional benefits due to their use of Amazon EC2, CloudFront, and CloudFormation.
* The Mint.com team gained greater elasticity and flexibility than their previous internal data center gave them.
* Mint.com can now scale on demand to support website traffic increases up to 200 percent.
* Mint.com can now provide security for 50 TB of financial data that it stores.

#### Amazon RDS and High Availability
Amazon RDS provides high availability by implementing a multiple-Availability Zone (Multi-AZ) approach. Amazon RDS automatically provisions and maintains a synchronous standby replica in a different Availability Zone. 

The primary DB instance is synchronously replicated across Availability Zones to a standby replica to provide data redundancy, eliminate I/O freezes, and minimize latency spikes during system backups. Running a DB instance with high availability can enhance availability during planned system maintenance and help protect your databases against DB instance failure and Availability Zone disruption.

#### Multi-AZ deployments and read replicas

| | Multi-AZ Deployments | Read Replicas |
| ----------------------- | ----------------------- | ---------------------- |
| Replication | Synchronous block-level replication is highly durable. | Asynchronous replication is highly scalable. |
| Instance availability | Only the database engine on the primary instance is active. | All read replicas are accessible and can be used for read scaling. |
| Backups | Automated backups are taken from standby. | No backups are configured by default for replicas. |
| Regions and Availability Zones | They can always span two Availability Zones within a single Region. | They can be within an Availability Zone, across Availability Zones, or across Regions. |
| Upgrades | Database engine version upgrades happen on the secondary, which is then promoted to primary. | Database engine version upgrade is independent from the source instance. |
| Failover and promotion | They automatically fail over to standby when a problem is detected. | They can be manually promoted to a standalone database instance. |

#### High availability example
A highly available architecture using a Multi-AZ deployment and two Amazon RDS read replicas.

The primary DB instance is used for writes, but can also be used for some reads. To optimize read performance, the application instances connect to the read replicas for reads (SELECT) and the primary instance for write operations (INSERT, UPDATE, DELETE). If more read capacity is required, additional read replicas can be added. 

The secondary DB instance is automatically launched by Amazon RDS in a different Availability Zone. It is always in synch with the primary. If there is an issue with the primary instance, Amazon RDS will promote the secondary instance to the primary, replace the old primary instance, and make it the new secondary. The cutover is performed by making a change to the DNS record for the database. 

#### Monitoring Amazon RDS
Amazon RDS provides metrics in real time for the operating system that your DB instance runs on. You can view the metrics for your DB instance by using the console, or consume the Enhanced Monitoring JSON output from Amazon CloudWatch Logs in a monitoring system of your choice. By default, Enhanced Monitoring metrics are stored in CloudWatch Logs for 30 days.

#### Amazon RDS Performance Insights
Amazon RDS Performance Insights is a database performance tuning and monitoring feature that helps you quickly assess the load on your database and determine when and where to take action. With Performance Insights, non-experts can detect performance problems with a user-friendly dashboard that visualizes database load.

Performance Insights uses lightweight data collection methods that don’t impact the performance of your applications. Reports make it simple to see which SQL statements are causing load and why.

##### Engine support
Amazon RD Performance Insights is available for all engines.

##### Extended data retention
Customers can retain up to 2 years of performance data. They can also view the following analysis:
* Trend performance over time
* Month-over-month activity
* Comparison of end-of-quarter or end-of-year performance with earlier performance

##### Load metrics in Amazon CloudWatch
Amazon CloudWatch can receive the following metrics:
* DBLoad
* DBLoadCPU
* DBLoadNonCPU

##### Instance support
Support is not available for burstable (t) instance types.

##### [Multi-AZ DB cluster deployments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html)

#### OLAP and OLTP
Online analytic processing (OLAP) and online transaction processing (OLTP) are data processing systems that help you store and analyze large volumes of business data. You can collect and store data from multiple sources—such as websites, applications, smart meters, and internal systems. Both systems require efficient and reliable IT infrastructure to run smoothly. You can use them both to query existing data or store new data. Both support data-driven decision-making in an organization.

##### OLAP
The primary purpose of OLAP is to analyze aggregated data. OLAP combines and groups the data so that you can analyze it from different points of view. You use OLAP systems for actions such as generating reports, performing complex data analysis, and identifying trends. 

##### OLTP
OLTP stores and updates transactional data reliably and efficiently in high volumes. OLTP databases can be one among several data sources for an OLAP system. You use OLTP systems for actions such as processing orders, updating inventory, and managing customer accounts.

#### Example of OLAP and OLTP
A company uses an OLTP database to process transactions in real time, update inventory levels, and manage customer accounts. 

The company uses an OLAP database to analyze the data collected by the OLTP database. The company’s business analysts can use it to generate reports on sales trends, inventory levels, customer demographics, and other key metrics. 

#### When to use OLAP or OLTP
OLAP and OLTP are different methods of using a database for relevant use cases. OLAP is optimized for complex data analysis and reporting, and OLTP is optimized for transactional processing and real-time updates.

| Criteria | OLAP | OLTP |
| -------- | ---- | ---- |
| Purpose | OLAP helps you analyze large volumes of data to support decision-making. | OLTP helps you manage and process real-time transactions. |
| Data source | OLAP uses historical and aggregated data typically from multiple sources. | OLTP uses real-time and transactional data. |
| Data structure | OLAP uses multidimensional (cubes) or relational databases. | OLTP uses relational databases. |
| Data model | OLAP uses star schema, snowflake schema, or other analytical models. | OLTP uses normalized or denormalized models. |
| Volume of data | OLAP has large storage requirements, typically in terabytes (TB) and petabytes (PB). | OLTP has comparatively smaller storage requirements, typically in gigabytes (GB). |
| Response time | OLAP has longer response times, typically in seconds or minutes. | OLTP has shorter response times, typically in milliseconds. |
| Example applications | OLAP is good for analyzing trends, predicting customer behavior, and identifying profitability. | OLTP is good for processing payments and orders, and managing customer data. |

#### Transactional Compliance
##### Relational databases
A database transaction is a sequence of multiple operations performed on a database as part of a single logical unit of work. Either all operations within the transaction succeed, or they are all rolled back and the database remains in the state before the transaction was issued. A transaction is ended when a control command such as a commit or rollback is issued. Transactions include data manipulation language (DML) statements:
* **Insert**: Add a new record or table.
* **Update**: Change the values within one record in a table.
* **Delete**: Remove a record from a table.

##### Nonrelational databases
Nonrelational databases typically trade off consistency for availability. This means that different users can retrieve different results while an operation is occurring and the change is still propagating. Nonrelational operations are invoked with APIs. The following are some API operations in Amazon DynamoDB:
* **PutItem**: Add a new item to the table.
* **UpdateItem**: Update existing values or add new attributes to an item in the table.
* **DeleteItem**: Remove an item from the table.

#### ACID compliance
Atomicity, consistency, isolation, durability (ACID) is a method for maintaining consistency and integrity in a structured relational database.

##### Atomicity
When implementing a transaction, atomicity ensures that your transactions either completely succeed or completely fail. No one statement can succeed without the others. Because many requests to a database are multifaceted, this interaction is important for avoiding faults in your dataset.

##### Consistency
Consistency ensures that all transactions provide valid data to the database. This data must adhere to all defined rules and constraints. For a transaction to be completed successfully, all the statements within it must be valid against all relevant constraints. If any single statement violates these checks, the whole transaction is rolled back, and the database is returned to its previous state. Consistency also ensures that data updates are not made available until all replicas have been updated as well.

##### Isolation
Isolation ensures that one transaction cannot interfere with another concurrent transaction. Databases are busy places. Isolation ensures that when multiple transactions request the same data, there are rules in place ensuring that the operations do not cause data corruption and that all data is made available in an orderly fashion.

##### Durability
Data durability is all about making sure your changes actually persist. When a transaction has successfully completed, durability ensures that the result of the transaction is permanent even in the event of a system failure. This means that all completed transactions that result in a new record or update to an existing record are written to disk and not left in memory.

#### BASE compliance
Basically available, soft state, eventually consistent (BASE) is a method for maintaining eventual consistency and integrity in a semistructured database such as a nonrelational database.

##### Basically available
Basically available allows for one instance to receive a change request and make that change available immediately. The system always guarantees a response for every request. However, it is possible that the response can be a failure or stale data, if the change has not been replicated to all nodes. In an ACID system, the change does not become available until all instances are consistent. Consistency in a BASE model is traded for availability.

##### Soft state
In a BASE system, there are allowances for partial consistency across distributed instances. For this reason, BASE systems are considered to be in a soft state, also known as a changeable state. In an ACID system, the database is considered to be in a hard state because users cannot access data that is not fully consistent.

##### Eventually consistent
This reinforces the other letters in the acronym. The data will be eventually consistent, which means a change will eventually be made to every copy. However, the data will be available in whatever state it is during propagation of the change.

#### Database Storage
Amazon RDS storage auto scaling automatically scales storage capacity in response to growing database workloads, with no downtime. You can enable storage auto scaling from the Amazon RDS console.

With Amazon RDS storage auto scaling, you simply set your desired maximum storage limit, and storage auto scaling takes care of the rest.

Monitor the storage metrics for your database servers, IOPS, and throughput before planning a migration.

#### Amazon Elastic Block Store (Amazon EBS)
The following services use Amazon Elastic Block Store (Amazon EBS) volumes for database and log storage:
* Amazon RDS for MySQL
* MariaDB
* PostgreSQL
* Oracle
* Microsoft SQL Server

#### Amazon RDS storage types
Amazon RDS provides the following three storage types, which differ in performance characteristics and price. This means that you can tailor your storage performance and cost to the needs of your database workload.
* **General Purpose SSD**: General Purpose SSD volumes offer cost-effective storage that is ideal for a broad range of workloads running on medium-sized DB instances. General Purpose storage is best suited for development and testing environments. 
* **Provisioned IOPS SSD**: Provisioned IOPS storage is designed to meet the needs of I/O-intensive workloads, particularly database workloads that require low I/O latency and consistent I/O throughput. Provisioned IOPS storage is best suited for production environments. 
* **Magnetic**: Amazon RDS also supports magnetic storage for backward compatibility. We recommend that you use General Purpose SSD or Provisioned IOPS SSD for any new storage needs. The maximum amount of storage allowed for DB instances on magnetic storage is less than that of the other storage types.

You can create MySQL, MariaDB, Oracle, and PostgreSQL RDS DB instances with up to 64 tebibytes (TiB) of storage. 

You can create SQL Server RDS DB instances with up to 16 TiB of storage. For this amount of storage, use the Provisioned IOPS SSD and General Purpose SSD storage types.

When you select General Purpose SSD or Provisioned IOPS SSD, depending on the engine selected and the amount of storage requested, Amazon RDS automatically stripes (configures multiple volumes in a RAID array) across multiple volumes to enhance performance, as shown in the following table.

| Database | Amazon RDS Storage Size | Amounts of Volumes Provisioned |
| -------- | ----------------------- | ------------------------------ |
| MariaDB, MySQL, and PostgreSQL| Less than 400 GiB | 1 |
| MariaDB, MySQL, and PostgreSQL | Between 400 and 64,000 GiB | 4 |
| Oracle | Less than 200 GiB | 1 |
| Oracle | Between 200 and 64,000 GiB | 4 |
| SQL Server | Any | 1 |

You can view the storage performance metrics for an Amazon RDS database in the RDS console. If the metrics show that your database performance is constrained by IOPS or throughput, you can change storage types or provision higher performance. When you modify a General Purpose SSD or Provisioned IOPS SSD volume, it goes through a sequence of states. While the volume is in the *optimizing* state, your volume performance is in between the source and target configuration specifications. Transitional volume performance will be no less than the lowest of the two specifications. 

When you modify an instance’s storage so that it goes from one volume to four volumes, Amazon RDS does not use the Elastic Volumes feature. Instead, Amazon RDS provisions new volumes and transparently moves the data from the old volume to the new volumes. 

This operation consumes a significant amount of IOPS and throughput of both the old and new volumes. Depending on the size of the volume and the amount of database workload present during the modification, this operation can consume a high amount of IOPS, significantly increase IO latency, and take several hours to complete, while the RDS instance remains in the *modifying* state.

#### Lab: Working with Amazon RDS Databases
Amazon EC2 is a compute service that provides secure, resizable compute capacity for databases in the cloud. Hosting a database on Amazon EC2 allows for a high degree of customization and control over the database and its environment. It maintains the long-standing tradition of manual database management, including managing replication, failover, monitoring, notifications, and backups. AWS managed database solutions, such as Amazon RDS, provide fully automated solutions for all of these tasks.

In this lab, you perform the following tasks:
* Set up and configure an Amazon RDS instance with Multi-AZ failover and encryption.
* Create and store secrets through AWS Secrets Manager.
* Activate automatic rotation of secrets through Secrets Manager.
* Set up encryption in transit with SSL.
* Test Multi-AZ failover and data synchronization.

An Amazon EC2 instance has been provisioned for use in this lab. This instance is named as CommandHost and is within a public subnet. The EC2 instance is configured to communicate with the database instance located in a private subnet via port 3306. The instance has been added to a Secrets Manager role, which is configured for automatic secret rotation. 

##### Task 1: Configure and deploy an Amazon RDS database
1.1 At the top of the AWS Management Console, in the search bar, search for and choose RDS.
1.2. Choose **Create database**.
1.3. Configure the new database using the following settings:
 * **Choose a database creation method:** Select **Standard Create**.
 * **Engine options**
  * **Engine type:** Select **MySQL**.
Templates: Select Production

Availability & durability

Select Multi-AZ DB instance
 Note: Choosing this option ensures that Amazon RDS maintains a synchronous standby replica in a different Availability Zone than the database instance. Amazon RDS automatically fails over to the standby in the case of a planned or unplanned outage of the primary. By choosing a Multi-AZ deployment, the maintenance downtime is reduced. Amazon RDS updates the secondary instance first, fails over to it, and then updates the former primary.
Settings

DB instance identifier: Enter RDSLabDB
Credentials management: Choose Self managed option
Master username: Copy mydbAdminUser from the left
Master password: Copy mydbAdminPassword from the left
Confirm password: Copy mydbAdminPassword from the left
 Note: The master user is the Amazon RDS equivalent to a root user. You should only use it for specific tasks such as creating and managing databases or adding users.
 Additional information: You can find out more about specific privileges in the Amazon RDS Master User Account Privileges documentation.
DB instance size

DB instance class: Select Burstable classes
Dropdown: Select db.t3.micro
Storage

Storage type: Select General Purpose SSD(gp3)
 Note: For more intensive workloads, Provisioned IOPS could be used here to reduce latency with a higher cost.
Connectivity

Virtual private cloud (VPC): Select RDSVPC
DB Subnet group: Select the group name that contains mydbsubnetgroup
Public access: Select No
 Note: This ensures that your Amazon RDS instance is not assigned a public IP address, which could allow direct access to the database.
Existing VPC security groups: Select the group name that contains DBSecurityGroup
 WARNING: The list may not disappear when you select the VPC security group. Choose out of the drop-down menu to close it.
Choose the X to remove any security groups listed except the one that containsDBSecurityGroup.
Monitoring - Uncheck Enable Enhanced monitoring

Scroll down, Choose  Additional configuration, and configure:

Database options

Initial database name: Enter MyRDSLab
Backup:

Ensure that Enable automatic backups is checked.
Backup retention period: Select 10 days
 Note: With Amazon RDS, you can set the time window when backups will be created as well as the number of days to store backups before they are deleted. RDS backup snapshots are created from the standby instance (when available) to minimize load on the primary instance.
 Additional information: Visit the Working With Backups documentation for more information about this feature.
Log exports

Check all the boxes available. This ensures these logs are published to Amazon CloudWatch Logs.
Maintenance

Maintenance window: Select Choose a window
Start day: Select Sunday
Start time: Select 23:00 UTC
Duration: Select 1 hours
 Note: Once you have created your database instance, modifications to its configuration could result in service interruption because the instances need to reboot.

Choose Create database

A pop-up window appears, Choose Close

You are taken to the Amazon RDS console. Here you can monitor the progress of your database instances. The new Amazon RDS instance takes about 20 minutes to create. However, to allow you to continue with the lab activities, an identical RDS instance called mydb- has already been provisioned for you as part of the lab setup. You will use that instance for the remainder of this lab.

 Congratulations! You have successfully configured and deployed an RDS instance.

Task 2: Create and verify a secret using Secrets Manager
In this task, you will add a secret to Secrets Manager and rotate the credentials to your Amazon RDS database. Secrets Manager offers built-in integrations with Amazon RDS to automatically rotate database credentials on your behalf. Further customization using Lambda functions can enable management of API keys and AUTH tokens.

Creating a secret
At the top of the AWS Management Console, in the search bar, search for and choose Secrets Manager.

Select Secrets Manager from the drop down menu

Choose Store a new secret

Create a new secret using the following configuration:

Secret type: Select Credentials for Amazon RDS database
User name: Copy mydbAdminUser from the left
Password: Copy mydbAdminPassword from the left
Encryption key: Select aws/secretsmanager
Database: Select mydb
Choose Next

For Secret name, enter mydbsecret-xxxx (replace x with random numbers)

Choose Next

Leave Automatic rotation disabled for now. You will enable automatic rotation later in the lab.

Choose Next

Observe the sample code, then Choose Store

Choose refresh  button to view the created secret.

Retrieving a secret using the Secrets Manager Console
You can retrieve your secret from the Secrets Manager console or from your EC2 CommandHost through the AWS Command Line Interface (AWS CLI). Depending on the method you choose, different details are provided about the secret.

On the secrets page, Choose the name of mydbsecret-xxxx.
 Note: This is the secret you just created.

In the Secret value section, Choose Retrieve secret value.
Here, you can view your secret details key-value pairs. To view the details in JSON format, Choose Plaintext.

You have just created a secret that allows you to programmatically connect to your database without using a stored password. An API call to Secrets Manager is made to retrieve the current version of the secret rather than loading credentials from a local config file. To simulate this, in the next part of the task, you are going to connect to an Amazon EC2 instance and use the AWS CLI. The Amazon EC2 instance, CommandHost, has an AWS Identity and Access Management (IAM) role with SecretsManager:DescribeSecret, SecretsManager:ListSecret, SecretsManager:GetSecretValue, SecretsManager:ListSecrets attached to it that grants this access.

 Additional information: about using Secrets Manager Actions, Resources, and Condition Keys for AWS Secrets Manager.

Retrieving a secret using the Amazon EC2 CommandHost through the AWS CLI
In this part of the task, you will connect to the CommandHost through the AWS CLI.

Copy the CommandHostSessionUrl value from the left side of the lab page, and paste it in a new browser tab. The terminal for the CommandHost instance opens.
 If you encounter a problem connecting to Session Manager, select for help connecting to the EC2 instance using an SSH client.

Now that you’ve successfully connected to the CommandHost, you can retrieve your secret.

 Command: To obtain the ARN for the secret, run the following commands:
 Copy edit: Replace mydbsecret-xxxx with the value of your secret name created in the earlier task.


cd ~
aws secretsmanager list-secret-version-ids --secret-id mydbsecret-xxxx
Review the details of the output.

 Expected output:


******************************
**** This is OUTPUT ONLY. ****
******************************

{
    "Name": "mydbsecret",
    "ARN": "arn:aws:secretsmanager:us-west-2:123456789123:
            secret:mydbsecret-BkoayN",
    "Versions": [
        {
            "VersionId": "05181b74-9678-4da3-8ad9-123456789123",
            "VersionStages": [
                "AWSCURRENT"
            ],
            "LastAccessedDate": 1571788800.0,
            "CreatedDate": 1571857563.07
        }
    ]
}
 Note: Pay attention to VersionStages in the output. This contains a list of all active versions of the secret and the staging labels that are attached to each version. You should see one version ID (a UUID type value) that maps to a single staging label, AWSCURRENT.

 Command: SecretARN can simply be retrieved entering the below command:

aws secretsmanager list-secret-version-ids --secret-id mydbsecret-xxxx --output text --query ARN
 Expected output:


arn:aws:secretsmanager:us-west-2:123456789123:secret:mydbsecret-f7cv9J
 Copy: the above ARN value into a local text editor to save the information for later.

 Copy edit: the following command to a local text editor:


aws secretsmanager get-secret-value --secret-id (SecretARN) --version-stage AWSCURRENT
In the text editor, replace (SecretARN) with the ARN you copied earlier in the step 24.
RDS code replace 1

 Copy edit: the updated command from the text editor into the terminal window. Press ENTER to run the code.
 Expected output:


******************************
**** This is OUTPUT ONLY. ****
******************************
{
    "Name": "mydbsecret",
    "VersionId": "a6d64c04-f23a-400c-a787-a203c434cfa7",
    "SecretString": "{\"username\":\"student\",
    \"password\":\"Pa33w0rd!\",\"engine\":\"mysql\",
    \"host\":\"nrk0zffgjbmiru.cj3z9tovul5b.us-east-1.rds.amazonaws.com\",
    \"port\":3306,\"dbname\":\"mydb\",\"dbInstanceIdentifier\":\"nrk0zffgjbmiru\"}",
    "VersionStages": [
        "AWSCURRENT"
    ],
    "CreatedDate": 1569879693.613,
    "ARN": "arn:aws:secretsmanager:us-east-1:123456789123:
    secret:mydbsecret-IS8vhu"
}
Review the details provided about the secret.

Enable automatic rotation through Secrets Manager
In this section, you will configure automatic rotation for the secret created in the previous task. Remember that the secret is attached to the Amazon RDS database. You will use a MySQL client tool that has been preconfigured on your CommandHost, along with a Linux JSON parsing tool called jq.

 Note: For simplicity, this lab uses jq to parse the secret value into environment variables to allow for easy CLI manipulation. This is NOT a security best practice for a production environment. In a production environment, AWS recommends not storing passwords in environment variables.

Start by validating your initial secret and use it to connect to the database. You will do this through your Amazon EC2 CommandHost.

 Copy edit: the following code block to a text editor:

secret=$(aws secretsmanager get-secret-value --secret-id (SecretARN) | jq .SecretString | jq fromjson)
user=$(echo $secret | jq -r .username)
password=$(echo $secret | jq -r .password)
endpoint=$(echo $secret | jq -r .host)
port=$(echo $secret | jq -r .port)
Replace (SecretARN) with the secret ARN you copied earlier in the step 24.
RDS code replace 2

 WARNING: Keep a copy of this updated code block in the text editor. You will use this updated code block later in the lab.

 Copy edit: the updated code block from the text editor into the terminal window. Press ENTER to run the code.
 WARNING: If you closed the terminal window tab or lost the connection, select here for instructions on how to reconnect.

The command retrieves the secret and stores it temporarily within an environment variable. Next, you will run a command the uses the parsed details of your secret to access your database.

 Command: Run the following command in the terminal window:

mysql -h $endpoint -u $user -P $port -p$password mydb
The terminal prompt should now be MySQL [mydb]>.

 Command: To view the details of your current connection, run the following command:

STATUS;
 Similar Expected output:

'STATUS command output sample'

Notice where the output shows SSL: Not in use. This is not preferred from a security standpoint. This is explained later in the lab, and you will change the setting.

 Command: To close the current MySQL session, run the following command:

exit
Return to the tab with the Secrets Manager page within the AWS Management Console.

In the Rotation configuration section, Choose Edit rotation , and configure:

Enable Automatic rotation
Rotation schedule:
Time unit, enter 30 days
Rotation function:
Select Use a rotation function from your account
Lambda rotation function: Select rotation-lambda
 Note: The rotation-lambda function has been provided for you so that you can see how rotation works and understand the full benefit of using Secrets Manager. To view the sample code provided, select here.

Choose Save
A green success banner showing Rotating your secret mydbsecret-XXXX displays at the top of the screen.

Secrets Manager begins to configure rotation for your secret, including attaching the rotation-lambda function and attaching a role that enables Secrets Manager to invoke the function. Your secret will now be automatically rotated for you every 30 days.

 Congratulations! You have successfully created a simple secret and then viewed and retrieved the secret via the console and AWS CLI. Then, you successfully accessed the MySQL database, verified the connection to the database, and enabled automatic rotation for the secret.

Task 3: Secure the client to database connection in-transit
Connections to a DB instance can be encrypted using Secure Socket Layer (SSL) or Transport Layer Security (TLS) from your application. SSL/TLS connections provide one layer of security by encrypting data that moves between your client and a DB instance. Using a server certificate provides an extra layer of security by validating that the connection is being made to an Amazon RDS DB instance. It does so by checking the server certificate that is automatically installed on all DB instances that you provision.

To complete the following steps, the permissions on the CommandHost must be stored. A certificate bundle rds-combined-ca-bundle.pem file has already been downloaded to your CommandHost. For more information on how to Encrypt a connection to a DB instance.

In this task, you will access your database using a SSL certificate to encrypt the data in transit. You will then verify the SSL configuration.

Connect to the database using SSL encryption
Return to the tab with the CommandHost terminal window.
 WARNING: If you closed the terminal window tab or lost the connection, select here for instructions on how to reconnect.

 Command: To update the permissions for the certificate, run the following commands:

cd ~
chmod 600 rds-combined-ca-bundle.pem
 Copy edit: The updated version of the following code block from your text editor into the terminal window. Press ENTER to run the code. Remember that this code stores your secret into session variables.

secret=$(aws secretsmanager get-secret-value --secret-id (SecretARN) | jq .SecretString | jq fromjson)
user=$(echo $secret | jq -r .username)
password=$(echo $secret | jq -r .password)
endpoint=$(echo $secret | jq -r .host)
port=$(echo $secret | jq -r .port)
 Command: To connect to the Amazon RDS database using the verified SSL cert, run the following command:
 Note: If you are connected with an SSH Client and not using Session Manager, change the –ssl-ca path to --ssl-ca=/home/ec2-user/rds-combined-ca-bundle.pem


mysql -h $endpoint --ssl-ca=/home/ssm-user/rds-combined-ca-bundle.pem --ssl-verify-server-cert -u $user -P $port -p$password mydb
The terminal prompt should now be MySQL [mydb]>.

 Note: The previous command associates the path to the SSL cert to the rds-combined-ca-bundle.pem file, which is preloaded on the CommandHost instance. The certificate bundles are avaiable for download here.

Verify database connection is using SSL encryption
 Command: To view the details of your current connection, run the following command:

STATUS;
 Expected Similar output:

'STATUS command output sample'

Look for the SSL: line in the output. It should now say Cipher in use is xxxxxxx. This confirms that the SSL connection has been properly configured.

 Command: To close the current MySQL session, run the following command:


exit
 Congratulations! You have successfully learned how to use an encrypted connection using SSL. This was accomplished by referencing the rds-combined-ca-bundle.pem file, which had been downloaded on your CommandHost. You then logged into the database and verified that SSL was in use.

Task 4: Test Multi-AZ failover
Multi-AZ failover mode works in a synchronous primary/secondary relationship. There are two servers running simultaneously. The primary is accessible by users, and the data is replicated in real time to a secondary instance (residing in a different Availability Zone), which is not accessible to users.

In this task, you will run a preinstalled Python script (failover_test.py) from your CommandHost that inserts heartbeat records into a database until the connection fails. The script then continues to check the connection until it comes back (when the database failover finishes). The script then outputs a summary of the event, detailing the failover.

Return to the tab with the CommandHost terminal window.

 Command: To change your working directory to the home directory, run the following command:


cd ~
This is the directory from which you will run the failover_test.py script.

 Command: To install PyMySQL and download the SSL certificate to the test directory, run the following command:

pip3 install --user -r requirements.txt
Now that the testing environment is set up, you can start running the Python script to test the failover and data synchronization.

 Command: To run the Python script, run the following command:

python3 create_failover_sync_db.py
This script is run to create a temporary database and table to support failover_test.py. Each time this script is run, it creates the temporary database and then drops it when completed.

After running the script, you will be prompted to provide your mydb instance data and prompted whether to connect over SSL.

Enter the following commands in response to the prompts:
This will destroy and recreate sync database and tracking table enter y to continue, n to exit [n]: Enter y and press ENTER
Connecting over SSL (y/n) [y]: Enter y and press ENTER
path to ssl cert [./rds-combined-ca-bundle.pem]: Enter ./rds-combined-ca-bundle.pem
 Expected output: The output should contain the following messages:

'STATUS command output sample'

This has created the new database and table for the failover_test.py script you will run to send the data and test the failover.

Before initiating the failover test, you will open your database instance in the console.

Return to the tab with the AWS Management Console, type RDS in the search field and Select RDS from the drop down menu.

In the left navigation pane, Choose Databases.

Select the mydb database.

Now that everything is prepared, you will start the test and initiate the failover.

Once you finish entering the metadata, the test begins running and performs a heartbeat query to the MySQL database. When there is a connection disruption, the test continues to try connections every second. When connectivity returns, the test stops and reports the total time the database was not accessible. This can be used to measure the amount of time required for failover in database clusters with such capability.

Return to the tab with the CommandHost terminal window.

 Command: To initiate the test, run the following command:


python3 failover_test.py --test_run_id test_run_0
Enter the following commands in response to the prompts:
Connecting over SSL (y/n) [y]: Enter y and press ENTER
path to ssl cert [./rds-combined-ca-bundle.pem]: Enter ./rds-combined-ca-bundle.pem
After running the previous command, the test begins running and performing a heartbeat query to the MySQL database.

Now that the script is running queries into the database, it’s time to initiate failover.

Return to the tab with the AWS Management Console, which should be open to the RDS console with the mydb database selected.

Choose Actions and select Reboot.

Check Reboot With Failover?

Choose Confirm

Return to the tab with the CommandHost terminal window.

 Expected output:

'STATUS command output sample'

 Note: If you receive an output that looks different from the one above or gives a “traceback error”. Go back to beginning of task 4 and follow steps again once your DB instance is back online.

Observe the following metrics in the output:

failure_start_time
failure_end_time
Last inserted sync record id on initial primary db node
Pre-failure Db node hostname
Post-failure Db node hostname
This verifies the data was replicated to the secondary failover instance during the reboot.

Next, you will log back into your MySQL database to review the db_sync table and see that the data replicated over.

 Copy/Paste: The updated version of the following code block from your text editor into the terminal window. Press ENTER to run the code. Remember that this code stores your secret into session variables.

secret=$(aws secretsmanager get-secret-value --secret-id (SecretARN) | jq .SecretString | jq fromjson)
user=$(echo $secret | jq -r .username)
password=$(echo $secret | jq -r .password)
endpoint=$(echo $secret | jq -r .host)
port=$(echo $secret | jq -r .port)
 Command: Run the following command:

mysql -h $endpoint --ssl-ca=/home/ssm-user/rds-combined-ca-bundle.pem --ssl-verify-server-cert -u $user -P $port -p$password mydb
 Note: If you are connected with an SSH Client and not using Session Manager, change the –ssl-ca path to --ssl-ca=/home/ec2-user/rds-combined-ca-bundle.pem

The terminal prompt should now be MySQL [mydb]>.

 Command: Run the following command:

SHOW DATABASES;
 Command: To switch into your failover test database, run the following command:

USE db_test_meter;
 Command: To query the table, run the following command:

SELECT * FROM db_sync;
Observe the db_test_meter table and data synchronization information. This is the record of each heartbeat that was gathered during the test.

#### Knowledge Check
##### Which of the following are characteristics of an online analytic processing (OLAP) system? (Select TWO.)
* OLAP uses historical and aggregated data, typically from multiple sources.
* OLAP systems are optimized for complex data analysis and reporting.

##### What is required to complete a transaction in a relational database?
* A commit command to write the changes to storage.

##### Which database storage type is designed to meet the needs of I/O-intensive workloads?
* Provisioned IOPS SSD

#### Additional Resources
##### [Amazon RDS Multi-AZ](https://aws.amazon.com/rds/features/multi-az/)

##### [Configuring and Managing a Multi-AZ Deployment ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html)

##### [Amazon RDS Read Replicas](https://aws.amazon.com/rds/features/read-replicas/)

##### [Working with DB Instance Read Replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html)

##### [Quotas and Constraints for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Limits.html)

##### [Scaling Your Amazon RDS Instance Vertically and Horizontally](https://aws.amazon.com/blogs/database/scaling-your-amazon-rds-instance-vertically-and-horizontally/)

##### [Monitoring OS Metrics with Enhanced Monitoring ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html)

##### [Overview of Monitoring Metrics in Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MonitoringOverview.html)

##### [Working with Parameter Groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.html)

##### [What Is Amazon CloudWatch Logs?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)

##### [Performance Insights](https://aws.amazon.com/rds/performance-insights/?nc=sn&amp;loc=2&amp;dn=3)

##### [Monitoring DB Load with Performance Insights on Amazon RDS ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html)

### Week 9: Databases 2 Part 2

#### Usage of read replicas for high availability
With Amazon RDS, you can create a read replica in a different AWS Region from the source DB instance. Cross-Region read replicas can be used to do the following:
* Improve your disaster recovery capabilities.
* Scale read operations into a Region closer to users located near that Region.
* Migrate from a data center in one Region to a data center in another Region.

##### [Working with Multi-AZ DB Cluster Read Replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_MultiAZDBCluster_ReadRepl.html)

#### Availability and durability

#### Backups
##### Automated backups
The automated backup feature of Amazon RDS facilitates point-in-time recovery of your DB instance. Amazon RDS provides backup storage of up to 100 percent of your provisioned database storage at no extra charge. 

When automated backups are turned on for your DB instance, Amazon RDS automatically performs a full daily snapshot of your data during your preferred backup window. It also captures transaction logs when your data is updated. When you initiate a point-in-time recovery, the daily backup is restored for your DB instance and the transaction logs are replayed to the specific time that you requested. Amazon RDS retains backups of a DB instance for a limited, user-specified period of time, which is called the retention period. By default, the retention period is set to 1 day, but it can be set for up to 35 days.

##### Manual Database snapshots
Manual database snapshots are user initiated. You can back up your DB instance as often as you want. You can also restore the instance to a specific point in time. Manual database snapshots can be exported to Amazon Simple Storage Service (Amazon S3) buckets. Database snapshots are not deleted unless you explicitly delete them. Although database snapshots serve operationally as full backups, you are billed for only the storage of incremental changes from the previous snapshot.

##### Multi-AZ Deployment
Amazon RDS provides high availability and failover support for DB instances by using Multi-AZ deployments. Amazon RDS uses the following different technologies to provide failover support: 
* Multi-AZ deployments for MariaDB, MySQL, Oracle, and PostgreSQL DB instances use AWS failover technology. 
* SQL Server DB instances use SQL Server Database Mirroring (DBM) or Always On Availability Groups (AGs).

In a Multi-AZ deployment, Amazon RDS automatically provisions and maintains a synchronous standby replica in a different Availability Zone. The primary DB instance is synchronously replicated across Availability Zones to a standby replica. Automated snapshots are taken from the standby. In this way, a Muilti-AZ deployment provides data redundancy, eliminates I/O freezes, and minimizes latency spikes during system backups. Running a DB instance with high availability can enhance availability during planned system maintenance. It helps to protect your databases against DB instance failure and Availability Zone disruption.

However, DB instances that use Multi-AZ deployments can have increased write and commit latency compared to a Single-AZ deployment. This increase is due to the synchronous data replication that occurs. For production workloads, it is best to use Provisioned IOPS and DB instance classes that are EBS optimized for fast, consistent performance.

A Multi-AZ deployment can be configured when you create your Amazon RDS instance. However, you might already have an Amazon RDS instance that is running and configured in a Single-AZ deployment mode. Then it is possible to modify it to a Multi-AZ deployment mode. First, Amazon RDS takes a snapshot of the primary DB instance from your deployment and then restores the snapshot into another Availability Zone. Amazon RDS then sets up synchronous replication between your primary DB instance and the new instance.

#### Standby replicas and read replicas
In contrast to read replicas, standby replicas are synchronous copies of a database instance and cannot handle read accesses. Standby replicas are used for increased availability, and read replicas are used for scalability. Read replicas have a separate URL that clients can use to query read-only information. In a Multi-AZ deployment, the standby instance cannot be directly accessed. If the primary DB fails, the same endpoint that is used to connect to the primary will be used to connect to the standby. This new connection occurs after the standby is promoted as the new primary.

#### Failover: Promoting read replicas
Read replicas can also be useful for disaster recovery. You can promote a read replica to a standalone instance as a disaster recovery solution if the primary DB instance fails.

#### Multi-AZ deployment
Suppose that a planned or unplanned outage of your DB instance occurs, and you have enabled Multi-AZ deployment. Then Amazon RDS automatically switches to a standby replica in another Availability Zone. It is also possible to force a failover when you reboot an instance.

#### Read replicas
Amazon RDS will automatically replace the compute instance that powers a deployment if a hardware failure occurs.

#### Lab: Restoring an Amazon RDS DB Instance

#### Knowledge Check
##### Which of the following are characteristics of Amazon RDS read replicas? (Select THREE.)
* All instances are accessible and can be used for read scalability.
* They can be within an Availability Zone, across Availability Zones, or across Regions.
* They can be manually promoted to a standalone database instance.

Amazon RDS read replicas use asynchronous replication. All read replicas are accessible and can be used for read scaling. Read replicas can be within an Availability Zone, across Availability Zones, or across Regions. The database engine version upgrade is independent from the source instance. Read replicas can be manually promoted to a standalone database instance.

Wrong answers:
* Synchronous block-level replication
* Database engine version upgrades happen when primary is upgraded.
* Replicas cannot be directly accessed.

##### In a Multi-AZ database deployment, how do replicas receive their data updates?
* Synchronously in another Availability Zone

Wrong answers:
* Asynchronously in another Availability Zone
* Asynchronously in the same Availability Zone as the primary database instance and then asynchronously pushed to other Availability Zones
* Synchronously in the same primary Availability Zone as the primary database instance and then asynchronously pushed to other Availability Zones

The correct answer is **Synchronously in another Availability Zone**. In a Multi-AZ deployment, Amazon RDS automatically provisions and maintains a synchronous standby replica in a different Availability Zone. The primary DB instance is synchronously replicated across Availability Zones to a standby replica.

#### Additional Resources
##### [Working with DB Instance Read Replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html)

##### [Multi-AZ Deployments for Amazon RDS for Microsoft SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_SQLServerMultiAZ.html)

##### [Creating a Read Replica](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html#USER_ReadRepl.XRgn)

##### [Configuring and Managing a Multi-AZ Deployment](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html)

#### Securing Amazon RDS
#### Pre-assessment
##### When moving a hardcoded database credential to AWS Secrets Manager, what AWS Identity and Access Management (IAM) identity must the code be given?
* IAM role

Wrong answers:
* IAM group
* IAM Roles Anywhere 
* IAM user

When you create rotating credentials in AWS Secrets Manager, the code must assume the IAM role RoleToRetrieveSecretAtRuntime to be able to retrieve the secret. An IAM role is an identity within your AWS account that has specific permissions. It is similar to an IAM user, but it is not associated with a specific person. 

* **IAM group**: An IAM group is an identity that specifies a collection of IAM users. 
* **IAM Roles Anywhere**: IAM Roles Anywhere can obtain temporary security credentials in IAM for workloads such as servers, containers, and applications that run outside of AWS. The workloads can use the same IAM policies and IAM roles that you use with AWS applications to access AWS resources. 
* **IAM user**: An IAM user is an identity within your AWS account that has specific permissions for a single person or application.

##### In the shared responsibility model, what is an AWS customer responsible for when it comes to securing their managed database? (Select TWO.)
* Using the concept of least privilege to determine who has authorization to log in to the database
* Ensuring that the database engine is updated with all the required security patches and updates

Wrong answers:
* Using the concept of least privilege to determine who has access to data centers and physical servers
* Ensuring that the host servers have all the required security patches and updates
* Using third-party auditors to validate the security posture and compliance of the AWS infrastructure

AWS customers are responsible for the following:
* Using the concept of least privilege to determine who has authorization to log in to the database
* Ensuring that the database engine is updated with all the required security patches and updates

And AWS is responsible for the following:
* Using the concept of least privilege to determine who has access to data centers and physical servers
* Ensuring that the host servers have all the required security patches and updates
* Using third-party auditors to validate the security posture and compliance of the AWS infrastructure

##### If a snapshot is created of an encrypted database in another Region, what is the relationship between the snapshot and its AWS Key Management Service (AWS KMS) key?
* It must have a KMS key from its destination Region assigned to it.

Wrong answers:
* It brings the KMS key from the primary instance's Region.
* It must have a net new KMS key generated for it when the snapshot is created.
* The destination Region determines if it needs a new key or can use its key.

To copy an encrypted snapshot from one AWS Region to another, you must specify the KMS key in the destination AWS Region. This is because KMS keys are specific to the AWS Region that they are created in. The source snapshot remains encrypted throughout the copy process. Amazon RDS uses envelope encryption to protect data during the copy process.

Encrypted read replicas must be encrypted with the same KMS key as the source DB instance when both are in the same AWS Region.

#### Securing Amazon RDS

#### AWS Secrets Manager
With AWS Secrets Manager, you can configure your applications to fetch secrets, such as DB passwords, at runtime. This ensures that the correct and latest secret is provided, so you can remove hardcoded DB passwords from your applications.

* For master user credentials, you configure Amazon RDS to manage the master user password in Secrets Manager when creating or modifying your instance. Amazon RDS will automatically rotate the password every 7 days by default. For more information, see [Password Management With Amazon RDS and AWS Secrets Manager](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html).

* For all other Amazon RDS credentials, see [Create an AWS Secrets Manager Secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html).

##### [Moving Hardcoded Database Credentials to AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/hardcoded-db-creds.html)

#### Encrypting AWS databases
##### Encryption at rest
You can encrypt your Amazon RDS database instances and snapshots at rest by enabling the encryption option for your Amazon RDS database instances. Data that is encrypted at rest includes the underlying storage for DB instances, its automated backups, read replicas, and snapshots.

Amazon RDS encrypted database instances use the industry standard AES-256 encryption algorithm to encrypt your data on the server that hosts your Amazon RDS database instances. After your data is encrypted, Amazon RDS handles authentication of access and decryption of your data transparently with minimal impact on performance. You don't need to modify your database client applications to use encryption.

##### Encryption in transit
Encrypt communications between your application and your DB instance using SSL/TLS. You can use SSL from your application to encrypt a connection to a DB instance running MySQL, MariaDB, SQL Server, Oracle, or PostgreSQL. Each DB engine has its own process for implementing SSL. 

When an encrypted connection is established, data transferred between the DB instance and your application is encrypted during transfer. You can also require your DB instance to only accept encrypted connections.

#### Encryption constraints
* You can only encrypt an Amazon RDS DB instance when you create it, not after the DB instance is created. However, because you can encrypt a copy of an unencrypted snapshot, you can effectively add encryption to an unencrypted DB instance. That is, you can create a snapshot of your DB instance, and then create an encrypted copy of that snapshot. You can then restore a DB instance from the encrypted snapshot, and thus you have an encrypted copy of your original DB instance.
* You cannot turn off encryption on an encrypted DB instance. 
* You cannot create an encrypted snapshot of an unencrypted DB instance.
* A snapshot of an encrypted DB instance must be encrypted using the same KMS key as the DB instance.
* You cannot have an encrypted read replica of an unencrypted DB instance or an unencrypted read replica of an encrypted DB instance. 
* Encrypted read replicas must be encrypted with the same KMS key as the source DB instance when both are in the same AWS Region.
* To copy an encrypted snapshot from one AWS Region to another, you must specify the KMS key in the destination AWS Region. This is because KMS keys are specific to the AWS Region that they are created in. The source snapshot remains encrypted throughout the copy process. Amazon RDS uses envelope encryption to protect data during the copy process.
* You cannot unencrypt an encrypted DB instance. However, you can export data from an encrypted DB instance and import the data into an unencrypted DB instance.

##### [Encrypting Amazon RDS Resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html)

#### Knowledge Check
##### When moving hardcoded credentials into AWS Secrets Manager, when should the original credentials be revoked?
* After the new secret is created and the code is updated

Wrong answers:
* Before the new secret is created and the code is updated
* Before the new secret is created and after the code is updated
* After the new secret is created and before the code is updated

The following are the steps to move a hardcoded database credential to AWS Secrets Manager:
1. Create the secret.
2. Update your code.
3. Rotate the secret.

##### If a read replica is created based on an encrypted Amazon RDS database in the same Region, what is the relationship between the read replica and its AWS Key Management Service (AWS KMS) key?
* It must be encrypted with the same AWS KMS key as the source instance (when both are in the same AWS Region).

Wrong answers:
* It must be encrypted with a net new AWS KMS key.
* It has the original AWS KMS key automatically assigned.
* It cannot have an AWS KMS key because the original database cannot be encrypted.

##### In the shared responsibility model, what is AWS responsible for when it comes to securing databases? (Select TWO.)
* Ensuring that the host servers have all the required security patches and updates
* Using the concept of least privilege to determine who has access to data centers and physical servers

Wrong answers:
* Ensuring that the database instance has all the required security patches and updates
* Using the concept of least privilege to determine who has access to a database
* Ensuring that databases are run in private subnets to protect them from unintended network access

#### Migrating to an AWS Database

#### Pre-assessment
##### Which AWS migration solution uses native database tools to provide simple and high-performing homogeneous database migrations?
* AWS Database Migration Service (AWS DMS)

Wrong answers:
* AWS DataSync
* AWS Schema Conversion Tool (AWS SCT)
* AWS Application Migration Service

AWS DMS helps customers migrate the data inside a database and uses native tools for homogeneous migrations.
* AWS SCT can help with identifying issues with migrating over two different types of schemas.
* DataSync is used to migrate data from file and object storage.
* Application Migration Service is for migrating servers.

##### Which of these are characteristics of modern applications that create challenges for database migrations? (Select TWO.)
* Large data volumes
* Proprietary vendor features

Wrong answers:
* Simple data types
* Simple business logic
* Open-source vendor features

##### Which of these tools simplifies heterogenous database migrations by providing a fully managed experience for automating schema analysis, recommendations, and conversion at scale? (Select TWO.)
* AWS Schema Conversion Tool (AWS SCT)
* DMS Schema Conversion

Wrong answers:
* AWS Application Migration Service
* AWS DataSync
* AWS AppSync

AWS SCT and DMS Schema Conversion can convert your existing database schema to the target platform.  However, AWS DMS SC is a fully managed service.
* AWS Application Migration Service is for migrating servers.
* AWS DataSync is for migrating object and file data.
* AWS AppSynch helps customers develop applications faster with serverless GraphQL and Pub/Sub APIs.

#### Reasons for migration
##### Database modernization
Moving data from legacy database engines to modern database engines, so business agility can compete in the digital age.

##### Database migration
Moving data from one platform to another, in the context of enterprise applications

##### Database replication
Frequently copying data electronically from a database in one computer or server to a database in another to share the same level of information with all users

#### Benefits of AWS DMS
AWS Database Migration Service (AWS DMS) is a managed migration and replication service that helps move your database and analytics workloads to AWS quickly, securely, and with minimal downtime and no data loss. 
* **Simple to use**: You do not need to install drivers or applications, and it typically does not require changes to the source database.
* **Minimal downtime**: AWS DMS helps you migrate your databases to AWS with virtually no downtime.
* **Supports widely used database engines**: AWS DMS can migrate your data to and from most widely used commercial and open-source database engines. 
* **Low cost**: AWS DMS is a low-cost service. You only pay for the compute resources used during the migration process, any additional log storage, and data transfer (if not in the same AWS Region).
* **Fast and convenient setup**: You can set up a migration task within minutes in the AWS Management Console. This lets you define parameters used by AWS DMS to carry out the migration.
* **Reliable**: AWS DMS is highly resilient and self-healing. It continually monitors source and target databases, network connectivity, and the replication instance.

#### Databases migration to AWS
AWS DMS and AWS Schema Conversion Tool (AWS SCT) can help you migrate your databases to or from AWS quickly and securely. With AWS DMS, your source database remains fully operational during migration. This minimizes downtime to applications that rely on the database.

You can migrate to the same database engine, or switch database engines to modernize your database platform. You can also replicate data to sync source and target databases.

##### For example:
You can migrate from an on-premises Oracle database to an Amazon Relational Database Service (Amazon RDS) for Oracle instance.

##### Or...
You can migrate an Oracle database, either on premises or in the cloud, to a PostgreSQL database like Amazon RDS for PostgreSQL or Amazon Aurora PostgreSQL-Compatible Edition. First, you would perform schema conversion, and then you would migrate databases.

#### AWS tools used for migration
##### AWS DMS
At its most basic level, AWS DMS is a server in the AWS cloud that runs replication software. You create a source and target connection to tell AWS DMS where to extract from and load to. Then, you schedule a task that runs on this server to move your data.

Within AWS DMS is DMS Schema Conversion, which assesses the complexity of a migration for a source data provider and converts database schemas and code objects. 

##### AWS SCT
If you want to switch database engines, AWS SCT can convert your existing database schema to the target platform. This includes tables, indexes, views, and stored procedures, plus your application code. If the schema from your source database can't be converted automatically, AWS SCT provides guidance on how you can create equivalent schema in your target database engine.

#### Migration process steps.
Any step with an * is supported by AWS DMS and AWS SCT.
* **Schema migration**
 Step 1: Envisioning and assessment *
 Step 2: Database schema conversion *
 Step 3: Application conversion and remediation *
 Step 4: Scripts conversion *
 Step 5: Integration with third-party applications

* **Database migration**
 Step 6: Data migration *
 Step 7: Functional testing of the entire system
 Step 8: Performance testing
 Step 9: Integration and deployment *

* **Training and support**
 Step 10: Training and knowledge transfer
 Step 11: Documentation and version control
 Step 12: Post-production support

#### DMS Schema Conversion
DMS Schema Conversion automatically converts your source database schemas and most of the database code objects to a format compatible with the target database. This conversion includes tables, views, stored procedures, functions, data types, synonyms, and more. Any objects that DMS Schema Conversion can't convert automatically are clearly marked. To complete the migration, you can convert these objects manually.

At a high level, DMS Schema Conversion operates with the following three components:
* Instance profiles, which specify network and security settings.
* Data providers, which store database connection credentials.
* Migration projects, which contain data providers, an instance profile, and migration rules.

AWS DMS uses data providers and an instance profile to design a process that converts database schemas and code objects.

##### [Sources for DMS Schema Conversion](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.Sources.html#CHAP_Introduction.Sources.SchemaConversion)

##### [Targets for DMS Schema Conversion](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.Targets.html#CHAP_Introduction.Targets.SchemaConversion)

#### AWS SCT
You can use AWS SCT to convert your existing database schema from one database engine to another. You can convert relational online transaction processing (OLTP) schema or data warehouse schema. Depending on the source, schemas can be converted to target an Amazon RDS MySQL, MariaDB, Oracle database, SQL Server, PostgreSQL DB, Aurora DB cluster, or Amazon Redshift cluster. The converted schema can also be used with a database on an Amazon Elastic Compute Cloud (Amazon EC2) instance or stored as data in an Amazon Simple Storage Service (Amazon S3) bucket.

**AWS SCT does not support Oracle-to-Amazon DynamoDB migrations.**

#### Step 1: Envisioning and assessment
##### What happens during this step?
Planning is key to the success of any migration process. You need to understand the scope of work required, based on your database schema, data volumes, data types, resources, and stakeholders. And you need integrated tools that support the project plan and automate the migration as much as possible.

The first step is to assess your current environment, evaluate any known risks, and create a business case for the migration. You will identify subject matter experts and responsible business stakeholders, and plan capacity for the target system—including hardware and software infrastructure.

##### Migration to another database
Different relational database engines have different features, so changing your engine can permit you to take advantage of them. Open-source databases are comparable to commercial databases, but offer lower licensing costs, which can motivate you to move.

Changing database technologies (going, for example, from Oracle to Aurora PostgreSQL-Compatible) can, for some applications, optimize performance and cost. AWS SCT can assist you in the migration process by cataloging the physical and logical components of the existing system. If you are performing a heterogeneous migration, AWS SCT will evaluate how much effort is needed to migrate to one or more popular open-source engines. It will provide a detailed report on each engine, and you can choose the best target for your particular use case.

##### How AWS SCT helps
AWS SCT provides an assessment report that shows you the following: 
* What AWS SCT can convert automatically
* Which objects need manual remediation
* Which objects require significant remediation 

Levels of effort are color coded as green, gray, orange, and red in the summary report. Simple actions usually require less than an hour, medium actions can be completed in 1–4 hours, and complex actions would typically take over 4 hours. You can use this information to develop level-of-effort estimates across different lines of responsibility like database administrators (DBAs), application developers, test engineers, and business stakeholders.

* **Green objects** automatically converted.
* **Gray objects** with simple acctions.
* **Orange objects** with medium-complexity actions.
* **Red objects** with complex actions.

##### Database storage objects with conversion actions
In the following example assessment report, the task involves converting an Oracle database to an Aurora PostgreSQL-Compatible database. The assessment report gives you a quick overview of how many of your database objects have been converted automatically, and how many require manual intervention. It also includes an assessment of the difficulty of each manual intervention.

##### Database code objects with conversion actions
AWS SCT not only helps you convert tables and indexes, but it can also assist you in converting code objects such as stored procedures and functions, database packages, and views and triggers. AWS SCT will translate code written in the native language of the source database into equivalent code in the target database language.

For example, AWS SCT will convert an Oracle stored procedure written in Procedural Language for SQL (PL/SQL) into an equivalent Procedural Language/PostgreSQL (PL/pgSQL) procedure for a PostgreSQL target. As before, if AWS SCT detects any issues that require manual intervention, it will highlight the offending code that needs attention. 

##### Detailed recommendations
AWS SCT will also provide you with a detailed list of migration objects that require manual intervention. The details will include which features are not supported by your target database, and recommendations on how to translate. You can also export a version of this report as a spreadsheet, so you can track which tasks are complete.

##### AWS SCT report
AWS SCT also provides a granular view of the report to use as a remediation checklist. Responsible developers, DBAs, and others can use this view to validate that corrective action has been taken on cited objects and that remediation is complete.

#### Step 2: Database schema conversion
##### What happens during this step?
The second step is to convert your database objects from the source engine to the target engine. This includes converting your tables, indexes, constraints, foreign keys, triggers, and stored procedures. It doesn’t include migrating the actual data records in your database.

##### How AWS SCT helps
AWS SCT will convert your source-object definitions to the target engine’s formats. Then, when you’re ready to build the database schema, it will apply the definitions to the target engine.

When you’re performing a heterogeneous migration, your target database might be missing features that are available in your source database. If AWS SCT can’t convert an object, it flags it for manual intervention, along with a color-coded level of effort needed to resolve.

##### AWS SCT alerts
AWS SCT will mark any items that it cannot convert with different colors for simple (gray), medium (yellow), and complex (red) actions. It will also mark the levels above in the hierarchy, if they have any items with issues.

For example, the IDX_BM_SPORTING_EVENT index is marked with a red exclamation point. You can then open the assessment report view to see the specific issues. AWS SCT flagged this index because PostgreSQL does not support bitmapped indexes.

AWS SCT will highlight any items with issues in the hierarchy menu on the left. Notice how all the levels are highlighted if there is at least one issue.

Choosing an item will reveal detailed information about the issue, plus suggestions about how to correct it and additional references.

##### Other alerts
AWS SCT generated a warning about this procedure because an INSERT statement is using a hint that is not supported by PostgreSQL. AWS SCT shows the offending code in yellow.

Notice that this is only a warning message, and that AWS SCT ignores the hint in the converted code. However, you can remove the error by simply editing the source code directly in AWS SCT and reconverting. This edit affects only the local copy of the code that AWS SCT has extracted from the source database—the actual source database is unaffected.

Any items for stored procedures and functions will also appear highlighted on the menu. Again, notice that all levels of the hierarchy get highlighted so you can see at a glance whether you have any issues.

Navigating into the menu will provide you with detailed information about the issues. This includes original code, migrated code (if any), issue description, and available hints about how to fix it.

##### If an AWS SCT conversion does not work for a migration
Sometimes you will find that a feature in your source database does not have an exact analog in the target database that AWS SCT can translate to. In these cases, you will need to recode the objects by using design patterns based on the target engine’s capabilities.

To help with this process, AWS provides migration playbooks that contain design patterns for the most popular source and target combinations. For example, the Oracle to Aurora PostgreSQL playbook contains information on design patterns that are fully, partially, or not supported by the target.

##### Data migration playbooks
The Database Migration Playbooks are a series of guides focused on best practices for creating successful blueprints for heterogeneous database migration. The playbooks complement existing automated and semiautomated database migration solutions and tools from Amazon, including AWS SCT and AWS DMS. AWS currently offers the following four migration playbooks: 
* Oracle to Aurora PostgreSQL
* SQL Server to Aurora MySQL
* SQL Server to Aurora PostgreSQL
* Oracle to Aurora MySQL

AWS will release more over time. These and future releases can all be found on the [AWS Database Migration Service](https://docs.aws.amazon.com/dms/index.html) page.

##### When a source functions and procedures are unavailable in the target engine
An [AWS SCT Extension Pack](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_ExtensionPack.html) is an add-on module that emulates functions present in the source database that are required when converting objects to the target database. Before you can install an AWS SCT Extension Pack, you need to convert your database schema.

#### Step 3: Application conversion and remediation
##### What happens during this step?
Application conversion is the process of porting application code, written in languages such as Java or C, to your new target database.

For example, your database might support an order entry application that uses web forms. The application would use embedded SQL to query and update order information. If you switch database engines, these SQL statements must be ported to the target format.

##### Impact on migration
Application conversion is arguably the most complex aspect of a migration process. You might have applications running against your database that were written long ago by resources who are no longer available. These applications are often mission critical and might be difficult to rewrite without extensive research and testing.

Converting your applications is likely the most challenging step in the conversion process. Your applications might use nonstandard features that are not supported by your target database. You might also lack in-house expertise for legacy applications that are still in use.

##### How AWS SCT helps
AWS SCT helps you modernize your SQL code to work with your new database. You can use AWS SCT to extract SQL statements that are embedded in your application code. AWS SCT will track all the places where SQL is present, convert the SQL to work with the target database, and rebuild your application program with the converted code.

During this process, you add your application's files and folders. When that is complete, AWS SCT will help you keep track of your files. AWS SCT can detect SQL within your application code, even if it's present as strings. It will extract the code for easier reading and modification and track old and converted versions of code. In most cases, AWS SCT will automaticlaly convert your SQL code to your target database. From there, you can edit the converted code. When the SQL code has been converted, AWS SCT will put it back into the application code.

#### Step 4: Scripts conversion
##### What happens during this step?
The script conversion step looks at batch scripts used for extract, transform, and load (ETL) processes; database maintenance, disaster recovery, and other processes. These scripts might not directly relate to the applications using the database, but they require analysis to ensure that they work on the new database engine.

##### How AWS SCT helps
AWS SCT can help you convert your database scripts. Use AWS SCT to convert Oracle, Microsoft, and Teradata scripts to run on PostgreSQL-derived databases, including Aurora PostgreSQL-Compatible and Amazon Redshift. As with other conversion features in AWS SCT, if the code cannot be converted for any reason, the tool will highlight the problem for manual intervention.

AWS SCT will try to automatically convert the scripts. If it cannot convert all the statements, it will highlight it on the menu. AWS SCT will add comments to the converted code that identify what the issues are. Then you can review and edit your original script in AWS SCT. When conversion is complete, you can save your scripts.

#### Step 5: Integration with third-party applications
You identify third-party applications, and validate that they continue to work after migration. This process could involve upgrading the third-party tools or changing adapters or APIs to connect to your new databases.

Other third-party applications might be tightly coupled to a third-party database. In that case, consider whether you will maintain a legacy database for these applications, or whether you want to migrate from them.

#### Data Migration

#### AWS Database Migration Service (AWS DMS)
AWS DMS is a cloud service for migrating relational databases, data warehouses, NoSQL databases, and other types of data stores. You can use AWS DMS to migrate your data into the AWS Cloud or between combinations of cloud and on-premises setups. 

During migration, the source database remains fully operational during the migration, minimizing application downtime. AWS DMS can migrate your data to and from most widely used commercial and open-source databases.

By supporting both homogenous and heterogeneous migrations, AWS DMS can continuously replicate your data with high availability between your data stores. Tasks defined in AWS DMS can perform a full load migration, migrate cached changes, or perform ongoing replication between the data stores.

#### Step 6: Data migration
##### What happens during this step?
Data migration is the process of moving data records from the source to the target. It is the activity that most people think of when they hear the term database migration.

Data migration can be challenging if you are dealing with large data volumes, and have to keep the source and target systems in sync until you can cut over your applications to the target system.

If your database also contains complex data types like large objects (LOBs) or spatial data, you will need to consider how best to migrate those data values to the target. Lastly, if you’re changing the type of your target database, you will have to translate most (if not all) data values to conform to the target system requirements.

##### How AWS DMS helps
You can use AWS DMS to migrate all your data as a full load and to replicate ongoing changes, known as **change data capture (CDC)**.

#### How AWS DMS works
AWS DMS will migrate your data records to the same database engine, or you can modernize your database to use a cloud-native or open-source engine. You can use AWS DMS to perform a one-time copy of the source data to the target. You can also use AWS DMS to keep your source and target synced by migrating ongoing transactions as they occur on the source.

If you are migrating to a new target database, you can continue replicating until you are ready to switch over your applications. If your use case requires ongoing data replication, you can use AWS DMS to keep a source and target in sync indefinitely.

#### How AWS DMS moves data
AWS DMS moves your data in one of three ways: full-load migration, ongoing replication, or a combination of both. During a full-load migration, where existing data from the source is moved to the target, AWS DMS loads data from tables on the source data store to tables on the target data store.

AWS DMS also supports ongoing replication (known as change data capture, or CDC), which keeps your target in sync with a transactionally active source. AWS DMS can combine these two types of data transfer by using an initial full load, followed by ongoing replication.

##### Filtering and transforming data
You can select which schemas or tables to include in the migration, filter out unwanted data records, and transform names to conform to your particular naming conventions. As your migration progresses, you can monitor the migration process and check the health of your migration resources through the AWS DMS console.

##### Monitoring progress
A migration task runs on a replication instance, which is an Amazon EC2 instance that has been configured with the AWS DMS software. Or, you can choose a serverless option, AWS DMS Serverless. The task migrates the data between your source and target endpoints. You can see the progress of the task in the console, and review detailed task logs, if necessary. 

#### Migration validation
AWS DMS can validate the migrated data, so you can be confident that the source and target databases match. Data validation is an option that you can choose to add to your replication task. Data validation tracks the progress of the migration, and incrementally validates new data as it is written to the target. 

#### Step 7: Functional testing of the entire system
This phase typically involves business stakeholders and analysts who understand user-facing applications and can drive test cases that exercise system boundaries.

#### Step 8: Performance testing
Performance testing sometimes occurs in parallel with functional testing. This activity involves both business stakeholders and technical personnel. When a performance issue is discovered, each system level is checked for bottlenecks. This includes the user-facing application, the SQL statements prepared by the application, the database engine, and associated storage layers. Business and technical teams work in tandem to verify that the issue is resolved, or to identify appropriate remediation to satisfy business needs.

#### Step 9: Integration and deployment
##### WHAT HAPPENS DURING THIS STEP?
Integration and deployment is the process of cutting over to your new database system. This typically involves a series of steps detailing how applications will be cut over to the new database system. Depending on business needs, the deployment might require minimized downtime. It might also have to fit into a specified time window or be performed in phases, where individual applications are cut over, one by one.

**Integration**: Initially, your system will talk to your original database. Use AWS DMS to perform a full-load migration, and then set up ongoing replication.

**Deployment**: After you verify that data is flowing correctly, and assuming that you have tested your application with the new database, you will change the application to read and write to the new database. This will stop the need for ongoing replication.

##### Rolling back data
When you are ready to switch over to production, it is important to plan for what to do in case you need to roll back changes. You may have to do this to meet business continuity requirements. You will want to test this plan in your preproduction environment as well, so the team is ready for any issues that occur during the rollout.

#### Training and Support
#### Step 10: Training and knowledge transfer
Until all of the team understands the new technologies that you are moving to, consider adding training time on the database engine, AWS, and Amazon RDS.

Even when everyone is familiar with the technologies, chances are that, while migrating, you discovered useful information about your application and how it will behave from now on. You might have slightly changed tables, stored procedures, and application code while migrating. You now want to ensure that those changes are documented, and share that knowledge with team members who support and maintain the application.

It is also important to be aware of cultural aspects with migration, because migrating to the cloud involves learning new technologies and changing some ways of thinking and acting. Some people love learning new technologies and consider this a perk of their job. Others prefer to stick with the familiar and resist any changes. You need to be prepared to manage this resistance to change, should it arise.

You also need to develop features to manage the new environment, such as monitoring and paging. Many of the features that you used previously might be implemented differently for your new database. Be prepared for technical hurdles and any required training for the new tools.

#### Step 11: Documentation and version control 
Although often overlooked, documentation is one of the most important tasks before putting a system into production. You need to document all changes that have been made to the system, and how the new system operates.

AWS supports infrastructure as code and provides services and tools to manage all your cloud infrastructure with code. Because you are creating a whole new installation, this is a good opportunity to script all steps. You might also consider treating all of these artifacts as code. This means using a version-control system and requiring code reviews for any changes to database or server infrastructure.

AWS provides tools like [AWS CloudFormation](https://aws.amazon.com/cloudformation/) and the [AWS Cloud Development Kit](https://aws.amazon.com/cdk/), which help you to manage all your AWS resources programmatically. You can script and manage the creation of Amazon RDS database instances and clusters and their backups. If you prefer to manage your database servers yourself, you can, in addition, use other services. 

#### Step 12: Post-production support
When the migrated application is running, you will need at least some support. AWS allows you to automate backups and other support tasks, but it is a good idea to plan for the support that your application might need. Ensure that automated tasks are occasionally checked, and that you have personnel for tasks that are not automated.

#### Lab: AWS Database Migration Service

#### Common Migration Processes

#### Migration playbooks
##### [Oracle Database 19c to Amazon Aurora PostgreSQL](https://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/chap-oracle-aurora-pg.html)

##### [Microsoft SQL Server 2019 to Amazon Aurora PostgreSQL](https://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-postgresql-migration-playbook/chap-sql-server-aurora-pg.html)

##### [SQL Server to Aurora MySQL ](https://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-mysql-migration-playbook/chap-sql-server-aurora-mysql.html)

##### [Oracle to Aurora MySQL](https://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/chap-oracle-aurora-mysql.html)

#### Knowledge Check
##### Which step can happen in parallel with performance testing?
* Step 7: Functional testing of the entire system

Performance testing sometimes occurs in parallel with functional testing. 

Wrong answers:
* Step 4: Scripts conversion
* Step 5: Integration with third-party applications
* Step 6: Data migration

##### Which step in a database migration process involves cutting over to the new database?
* Step 9: Integration and deployment

Wrong answers:
* Step 6: Data migration
* Step 7: Functional testing of the entire system
* Step 8: Performance testing

Integration and deployment is the process of cutting over to your new database system. This typically involves a series of steps detailing how applications will be cut over to the new database system. Depending on business needs, the deployment might require minimized downtime. 
* **Step 6**: Data migration – Data migration is the process of moving data records from the source to the target. It is the activity that most people think of when they hear the term database migration.
* **Step 7**: Functional testing of the entire system – During this step, you ensure that all applications interacting with the database perform as before, from a functional perspective. 
* **Step 8**: Performance testing – This activity involves both business stakeholders and technical personnel. When a performance issue is discovered, each system level is checked for bottlenecks. This includes the user-facing application, the SQL statements prepared by the application, the database engine, and associated storage layers.

##### Which step during the migration process highlights areas where application code might need to be altered?
* Step 3: Application conversion and remediation

Wrong answers:
* Step 2: Database schema conversion
* Step 4: Scripts conversion
* Step 5: Integration with third-party applications

The application conversion step is the process of porting application code, written in languages such as Java or C, to your new target database.
* **Step 2**: Database schema conversion – During this step, database objects are converted from the source engine to the target engine. This includes converting your tables, indexes, constraints, foreign keys, triggers, and stored procedures. But it doesn’t include migrating the actual data records in your database. 
* **Step 4**: Scripts conversion – The script conversion step looks at batch scripts used for extract, transform, and load (ETL) processes; database maintenance; disaster recovery; and other processes.
* **Step 5**: Integration with third-party applications – During this step, all third-party integrations are vetted, including connections to other databases. Where there are incompatibilities, this process could involve upgrading the third-party tools or moving to another system.

### Week 10: Security 2 Part 1
#### Application Access Controls

#### Pre-assessment
##### Which is an example of single sign-on?
* Accessing AWS resources after authenticating with an identity provider

Wrong answers:
* Setting a password that never expires
* Registering the same username and password for every website you access
* Using an account that only requires you to authenticate once a day

Single sign-on helps users log in to different applications and websites using one account.

##### Which are components of Amazon Cognito? (Select TWO.)
* User pools
* Identity pools

Wrong answers:
* Data pools
* Account pools
* API pools

**User pools** and **identity pools** are the two core components of Amazon Cognito.

##### Which security element encompasses determining which resources a user can use after they have gained access to a system?
* Authorization

Wrong answers:
* Authentication
* Admission
* Federation

**Authorization** is the process of determining which resources a user has access to after they have been authenticated.

#### Securing Access

##### Authentication
* You want to know who is requesting access to the Amazon Web Services (AWS) account and the resources in it.
* It's important to establish the identity of the requester through credentials.
* The requester can be a person or an application; AWS Identity and Access Management (IAM) calls them principals.

##### Authorization
* After the requester has been authenticated, it's important to determine what they should be permitted to do.
* IAM checks for policies that are relevant to the request to determine whether to allow or deny the request.

#### Identity providers
In AWS, identity and access management are not always handled internally. Third-party IdPs can also be used to authenticate the identities of principals for account access purposes. 

With an identity provider, commonly known as an IdP, you can manage your user identities outside of AWS, and give these external user identities permissions to use AWS resources in your account. 

When you use an IAM identity provider, you don't have to create a custom sign-in code, or manage your own user identities. The IdP provides that for you. Your external users sign in through a well-known IdP, such as logging in with an Amazon, Facebook, or Google account. 

#### Federation
AWS supports identity federation with SAML 2.0, an open standard that many IdPs use. This feature provides federated single sign-on (SSO). Users can then log into the AWS Management Console or call the AWS API operations without you having to create an IAM user for everyone in your organization. With SAML, you can streamline the process of configuring federation with AWS because you can use the IdP's service instead of writing custom identity proxy code.

##### Federation for API access to AWS
Use a SAML assertion (as part of the authentication response) that is generated in your organization to get temporary security credentials. This scenario is similar to other federation scenarios that IAM supports; however, SAML 2.0–based IdPs in your organization handle many of the details at runtime for performing authentication and authorization checking. 

##### Web-based SSO to the AWS Management Console
Users can sign in to a portal in your organization hosted by a SAML 2.0–compatible IdP. They then select an option to go to AWS, and they can use the console without having to provide additional sign-in information. You can use a third-party SAML IdP to establish SSO access to the console. Or you can create a custom IdP to provide console access for your external users.

#### Using SAML-based federation for API access to AWS
Assume that you want to provide a way for employees to copy data from their computers to a backup folder. You build an application that users can run on their computers. On the back end, the application reads and writes objects in an Amazon Simple Storage Service (Amazon S3) bucket. Users don't have direct access to AWS.

In this scenario, the Client App allows users to access the Amazon S3 bucket resource withous giving them direct access to your AWS resources.

1. **Client app makes request to IdP**. A user in your organization uses a client app to request authentication from your organization's IdP.
2. **IdP authenticates user**. The IdP authenticates the user against your organization's Lightweight Directory Access Protocol (LDAP) identity store.
3. **IdP sends client SAML assertion**. The IdP constructs a SAML assertion with information about the user and sends the assertion to the client app.
4. **App calls AssumeRoleWithSAML**. The client app calls the **AWS Security Token Service (AWS STS) AssumeRoleWithSAML API**. It passes the Amazon Resource Name (ARN) of the SAML provider, the ARN of the role to assume, and the SAML assertion from IdP.
5. **AWS returns temporary security credentials**. The API response to the client app includes temporary security credentials.
6. **App uses credentials to access AWS resources**. The client app uses the temporary security credentials to call Amazon S3 API operations.

#### Amazon Cognito
Amazon Cognito provides a user directory and authentication service. It also acts as an authorization service for OAuth 2.0 access tokens and AWS credentials. Using Amazon Cognito, you can provide authentication and authorization for users from the built-in user directory, from your enterprise directory, or from consumer identity providers. Examples include Google and Facebook.

#### Amazon Cognito features
##### Identity management
###### Self-registration
Amazon Cognito provides you with features for user self-registration. Because this is often a customer's first experience with your site, you will want to ensure that the process is both user friendly and intuitive. 

###### Identity store
Amazon Cognito can provide user pools, which are highly scalable and secure identity stores. User pools securely store user profile data for users who sign up directly and for federated users who sign in with external identity providers.

###### Migration options
Users can migrate into Amazon Cognito using either a batch import or just-in-time (JIT) migration. The batch user migration uses a comma-separated values (CSV) file import process. Using the JIT migration process, AWS Lambda integrates the migration process into the sign-in workflow and can retain users' passwords.

##### User authentication
###### Customizable UI
Amazon Cognito provides a built-in and customizable UI for user sign-up and sign-in. You can use Android, iOS, and JavaScript SDKs for Amazon Cognito to add user sign-up and sign-in pages to your apps.

###### Multi-factor authentication (MFA)
You can add an additional layer of security for your customers by enabling MFA in an Amazon Cognito user pool. Users can verify their identities using text messages or a time-based one-time password generator, such as Google Authenticator. Amazon Cognito also supports the configuration of different password rules on different pools of users. 

###### Federation
As a federation hub, Amazon Cognito helps users log in through social identity providers, such as Apple, Facebook, Google, and Amazon. They can also use enterprise identity providers through SAML and OpenID Connect (OIDC). Amazon Cognito is a standards-based identity provider. After your users are logged in to Amazon Cognito (through local authentication or external federation), they can use OAuth or OIDC to access federated resources.

###### Custom authentication
Amazon Cognito user pools help you build a custom authentication flow that uses Lambda functions to authenticate users based on one or more challenge-response cycles. You can use this flow to implement passwordless authentication based on custom challenges, or use custom challenges as additional factors.

##### Access control
###### Last mile integration with applications
Amazon Cognito secures the last mile of integration with an application. Amazon Application Load Balancers and Amazon API gateways have built-in policy enforcement points that provide access based on Amazon Cognito tokens and scopes.

###### Access AWS resources
The credential broker for Amazon Cognito, also known as Amazon Cognito identity pools, provides SSO access to AWS resources. These include Amazon DynamoDB, S3 buckets, Lambda serverless components, and other Amazon services. Users can be dynamically mapped to different roles to support least privilege access to a service.

###### Machine-to-machine authentication
Using the OAuth Client Credential Flow, Amazon Cognito provides machine-to-machine authentication, ensuring a secure experience between application components.

##### Customer experience
###### Customer outreach
Amazon Cognito helps you use a data-driven approach to drive customer acquisition and retention. You can launch customer outreach campaigns and track the engagement with Amazon Pinpoint. Amazon Pinpoint provides analytics for Amazon Cognito user activities, and Amazon Cognito enriches user data for Pinpoint campaigns.

###### Extensibility
Customer identity and access management solutions are custom solutions. Amazon Cognito provides a robust set of hooks and extensions to fully customize the authentication, registration, and user migration flows. For example, the self-registration flow can be augmented with custom identity proofing and account verification checks. The login process can be extended to create custom authentication flows or modify a token before it is generated.

You can use the Amazon Cognito SDK with Java, C++, PHP, Python, Golang, Ruby, .NET, and JavaScript.

##### Security
###### Protection from web vulnerabilities using AWS WAF
In a collaboration with AWS WAF, Amazon Cognito offers advanced bot-detection features that can help save your organization from paying for automated accounts.

###### Compromised credential protection
Amazon Cognito can detect and prevent, in real time, the reuse of compromised credentials as users sign up, sign in, or change their password. When Amazon Cognito detects users have entered credentials that have been compromised elsewhere, it prompts them to change their password.

###### Compliance
Amazon Cognito aligns with multiple security and compliance requirements, including those for highly regulated organizations, such as healthcare companies and merchants.

###### Risk-based adaptive authentication
You can protect your users' accounts and enhance their sign-in experience with adaptive authentication. When Amazon Cognito detects unusual sign-in activity, such as attempts from new locations and devices, it assigns a risk score to the activity. You can choose to either prompt users for additional verification or block the sign-in request.

Amazon Cognito consists of two core components: **user pools** and **identity pools**.

#### User Pools
Amazon Cognito provides a secure identity store (user pools) that scales to millions of users. User pools securely store user profile data for users who sign up directly and for federated users who sign in with external identity providers.

Amazon Cognito user pools are an API-based user repository. The repository and APIs support storage of up to 50 custom attributes per user, provide support for different data types, and enforce length and mutability constraints. Select the required attributes that must be provided by the user before completion of the sign-up process.

1. **Connect to application**. Users initiate a connection to the application.
2. **Request sign-in**. A sign-in request is initiated.
3. **Redirect to third-party IdP (optional)**. The sign-in request is redirected to a third-party IdP (when applicable).
4. **Additional challenges**. Amazon Cognito issues additional challenges.
5. **Challenge responses**. Users respond to the additional challenges.
6. **Provide tokens and sign in**. Amazon Cognito provides the applicable tokens for app sign-in.
7. **Provide access token and retrieve data**. The application uses the access tokens to retrieve data.

#### Amazon Cognito user pools features
With a user pool, your users can authenticate to your web or mobile app through Amazon Cognito or federate through a third-party IdP. Federated and local users have a user profile in your user pool. Local users are those who signed up or you created directly in your user pool. You can manage and customize these user profiles in the console, an AWS SDK, or AWS Command Line Interface (AWS CLI).

Amazon Cognito user pools accept tokens and assertions from third-party IdPs and collect the user attributes into a JSON Web Token (JWT) that it issues to your app. You can standardize your app on one set of JWTs while Amazon Cognito handles the interactions with IdPs, mapping their claims to a central token format. An Amazon Cognito user pool can be a standalone IdP. Amazon Cognito uses the OIDC standard to generate JWTs for authentication and authorization. When you sign in local users, your user pool is authoritative for those users. You have access to the following features when you authenticate local users.

##### Web frontend
Implement your own web frontend that calls the Amazon Cognito user pools API to authenticate, authorize, and manage your users.

##### MFA
Set up MFA for your users. Amazon Cognito supports time-based one-time password and text message MFA.

##### Secure access
Secure against access from user accounts that are under malicious control.

##### Multi-step authentication flows
Create your own custom multi-step authentication flows.

##### User migration
Look up users in another directory and migrate them to Amazon Cognito.

An Amazon Cognito user pool can also fulfill a dual role as a service provider to your IdPs and an IdP to your app. Amazon Cognito user pools can connect to consumer IdPs, like Facebook and Google, or workforce IdPs, like Okta and Active Directory Federation Services.

#### Identity Pools
When you want to authorize authenticated or anonymous users to access your AWS resources, you can set up an Amazon Cognito identity pool. An identity pool issues AWS credentials for your app to serve resources to users. You can authenticate users with a trusted IdP, like a user pool or a SAML 2.0 service. It can also optionally issue credentials for guest users. Identity pools use both role-based and attribute-based access control to manage your users’ authorization to access your AWS resources.

Identity pools don’t require integration with a user pool. An identity pool can accept authenticated claims directly from both workforce and consumer IdPs.

#### Using Amazon Cognito to authenticate a user and then grant them access to an AWS service.
1. **Authenticate and request token or assertion (optional)**. A user initiates a connection to the application.
2. **Developer authorization, token, or assertion**. Your app user signs in through a user pool and receives an OAuth 2.0 token.
3. **Request role**. Your app exchanges a user pool token with an identity pool for temporary AWS credentials. You can use these with AWS APIs and AWS CLI.
4. **Role credentials**. Your app assigns the credentials session to your user and delivers authorized access to AWS services like Amazon S3 and DynamoDB.

#### Amazon Cognito identity pools features
Amazon Cognito identity pools are a collection of unique identifiers or identities that you assign to your users or guests and authorize to receive temporary AWS credentials. You can present proof of authentication to an identity pool in the form of the trusted claims. These claims can come from a SAML 2.0, OIDC, or OAuth 2.0 social IdP. You can use this to associate your user with an identity in the identity pool. The token that your identity pool creates for the identity can retrieve temporary session credentials from AWS STS.

**The AWS Security Token Service (AWS STS) is a web service that enables you to requst temprorary, limited-privilege credentials for users.**

To complement authenticated identities, you can also configure an identity pool to authorize AWS access without IdP authentication. You can offer your own custom proof of authentication or no authentication. You can grant temporary AWS credentials to any app user who requests them with unauthenticated identities. Identity pools also accept claims and issue credentials based on your own custom schema with developer-authenticated identities.

With Amazon Cognito identity pools, you have two ways to integrate with IAM policies in your AWS account. You can use these two features together or individually. 

##### Role-based access control
When your user passes claims to your identity pool, Amazon Cognito chooses the IAM role that it requests. To customize the role’s permissions to your needs, you apply IAM policies to each role. For example, if your user demonstrates that they are in the marketing department, they receive credentials for a role with policies tailored to marketing department access needs. Amazon Cognito can request a default role, a role based on rules that query your user’s claims, or a role based on your user’s group membership in a user pool. You can also configure the role trust policy so IAM trusts only your identity pool to generate temporary sessions.

##### Attributes for access control
Your identity pool reads attributes from your user’s claims and maps them to principal tags in your user’s temporary session. You can then configure your IAM resource-based policies to allow or deny access to resources based on IAM principals that carry the session tags from your identity pool. For example, if your user demonstrates that they are in the marketing department, AWS STS tags their session as *Department: marketing*. Your S3 bucket permits read operations based on an **aws:PrincipalTag** condition that requires a value of marketing for the Department tag.

#### Activity: Securing Amazon API Gateway
Amazon Cognito has user pools and those use pool authorizers can be used with REST APIs.

We can use Amazon Cognito with a third-party IdP, and possibly deploy an identity pool if anonymous user support is required.

##### After users are autheticated against the user pools, how will the user information within the application be transmitted in subsequent APUI calls?
* By using an OpenID Connect (OIDC) token.

Wrong answers:
* By using an OAuth2 token.
* By using a SAML 2.0 identity provider (IdP).

The OpenID Connect (OIDC) token gets formatted into a JSON Web Token and issued to the users in the user pool.

This token is then used by the aplication to inject information into a header for sunsequent API calls.

#### Lab: Securing Amazon API Gateway Using an Amazon Cognito Authorizer
In this lab you will set up an Amazon Cognito user pool with Hosted UI. You will then restrict API access to a pre-created mock API with an Amazon Cognito authorizer. You will have a pre-provisioned mock API provided through Amazon API Gateway. You will create an Amazon Cognito user pool and an Amazon Cognito authorizer within API gateway. These will hook together to provide authorization and authentication when attempting to log in to the mock app.

In this lab, you will perform the following tasks:
* Set up an Amazon Cognito user pool with HostedUI.
* Parse and understand Amazon Cognito sign-in URL components.
* Create an Amazon Cognito authorizer to restrict API access.
* Test the Amazon Cognito authorizer.

#### Knowledge Check
##### What authentication protocol does AWS use to support web identity federation?
* OpenID Connect

Wrong answers:
* SAML 2.0
* OAuth 2.0
* JSON Web Token

With web identity federation, users of an app can sign in using a well-known external identity provider. These include Amazon, Facebook, and Google.

##### Which component of Amazon Cognito provides temporary AWS credentials to apps to access AWS services?
* Identity pools

Wrong answers:
* User pools
* Data pools
* Account pools

**Identity pools**, also known as the **credential broker** for Amazon Cognito, provide single sign-on access to AWS resources.

##### Which component of Amazon Cognito is used to authenticate users and return JSON Web Tokens to an app?
* User pools

Wrong answers:
* Identity pools
* Data pools
* Account pools

Amazon Cognito **user pools** can authenticate users directly or through a third-party identity provider. After successful authentication, Amazon Cognito returns user pool tokens to an app.

#### Summary

##### Identity providers
With an IdP, you can manage your user identities outside of AWS and give these external user identities permissions to use AWS resources in your account. An IdP provides custom sign-in codes and managed identities for you. Using an IdP helps you avoid distributing or embedding long-term security credentials in your applications.

##### Amazon Cognito
Amazon Cognito is an AWS identity service that provides a user directory and authentication server. Amazon Cognito also acts as an authorization service for OAuth 2.0 access tokens and AWS credentials. Amazon Cognito consists of two core components: user pools and identity pools.

##### User pools
Amazon Cognito provides a secure identity store (user pools) that scales to millions of users. User pools securely store user profile data for users who sign up directly and for federated users who sign in with external IdPs.

Amazon Cognito user pools are API-based user repositories. The repositories and APIs support the storage of up to 50 custom attributes per user, provide support for different data types, and enforce length and mutability constraints.

##### Identity pools
Amazon Cognito helps you authorize authenticated or anonymous users to access your AWS resources through the use of identity pools. An identity pool issues AWS credentials for your app to serve resources to users. Identity pools use both role-based and attribute-based access control to manage your users’ authorization to access your AWS resources.

Identity pools don’t require integration with a user pool. An identity pool can accept authenticated claims directly from both workforce and consumer identity providers.

#### Additional Resources

##### [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html)

##### [Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html)

##### [Amazon Cognito identity pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity.html)

#### Authorizing Access to APIs

#### Pre-assessment
##### Which of the following are types of API? (Select TWO.)
* REST
* WebSocket

Wrong answers:
* TCP
* Cross-origin resource sharing
* Trivial FTP

REST and WebSocket, along with HTTP, are the common API types used with Amazon API Gateway.

##### What of the following are types of AWS Lambda authorizers? (Select TWO.)
* Token-based
* Request parameter-based

Wrong answers:
* User-based
* Web-based
* Java-based

**Token-based authorizers** receive the caller’s identity as a bearer token. **Request parameter-based authorizers** receive the caller’s identity as a combination of headers, parameters, and variables.

##### Which API type includes real-time dashboards in its list of targeted use cases?
* WebSocket

Wrong answers:
* HTTP
* REST
* HTTPS

**WebSocket** APIs are used in real-time applications like chat applications, real-time dashboards, and real-time alerts and notifications.

#### Controlling and managing access to APIs in API Gateway
The method you use to control and manage access to APIs in API Gateway will depend on the type of API you are working with.

Three common API types:
* REST, 
* HTTP, 
* and WebSocket.

#### API Gateway
API Gateway is an AWS service for creating, publishing, maintaining, monitoring, and securing REST, HTTP, and WebSocket APIs at any scale. API developers can create APIs that access AWS or other web services and data stored in the AWS Cloud. You can create APIs for use in your own client applications. You can also make your APIs available to third-party app developers.

An API defines the rules that you must follow to communicate with other software systems. Developers expose or create APIs so other applications can communicate with their applications programmatically. For example, a timesheet application exposes an API that asks for an employee's full name and a range of dates. When it receives this information, it internally processes the employee's timesheet and returns the number of hours worked in that date range.

You can think of a web API as a gateway between clients and resources on the web.

##### Clients
Clients are users who want to access information from the web. The client can be a person or a software system that uses the API. For example, developers can write programs that access weather data from a weather system. Or, you can access the same data from your browser when you visit the weather website directly.

##### Resources
Resources are the information that different applications provide to their clients. Resources can be images, videos, text, numbers, or any type of data. The machine that gives the resource to the client is also called the server. Organizations use APIs to share resources and provide web services while maintaining security, control, and authentication. In addition, APIs help them to determine which clients get access to specific internal resources.

#### REST APIs
REST is a software architecture that imposes conditions on how an API should work.

You can use REST-based architecture to support high-performing and reliable communication at scale. You can conveniently implement and modify it, bringing visibility and cross-platform portability to any API system.

API developers can design APIs using several different architectures. APIs that follow the REST architectural style are called REST APIs. Web services that implement REST architecture are called RESTful web services. The term RESTful API generally refers to RESTful web APIs. However, you can use the terms REST API and RESTful API interchangeably.

#### The REST architectural style principles

##### Uniform interface
The uniform interface is fundamental to the design of any RESTful web service. It indicates that the server transfers information in a standard format. The formatted resource is called a representation in REST. This format can be different from the internal representation of the resource on the server application. For example, the server can store data as text, but send it in an HTML representation format.

Uniform interface imposes the following four architectural constraints:
* Requests should identify resources. They do so by using a uniform resource identifier.
* Clients have enough information in the resource representation to modify or delete the resource if they want to. The server meets this condition by sending metadata that describes the resource further.
* Clients receive information about how to process the representation further. The server achieves this by sending self-descriptive messages that contain metadata about how the client can best use them.
* Clients receive information about all other related resources they need to complete a task. The server achieves this by sending hyperlinks in the representation so that clients can dynamically discover more resources.

##### Statelessness
In REST architecture, statelessness refers to a communication method in which the server completes every client request independently of all previous requests. Clients can request resources in any order, and every request is stateless or isolated from other requests. This REST API design constraint implies that the server can completely understand and fulfill the request every time.

##### Layered system
In a layered system architecture, the client can connect to other authorized intermediaries between the client and server, and it will still receive responses from the server. Servers can also pass on requests to other servers. You can design your RESTful web service to run on several servers with multiple layers, such as security, application, and business logic, working together to fulfill client requests. These layers remain invisible to the client.

##### Cacheability
RESTful web services support caching, which is the process of storing some responses on the client or on an intermediary to improve server response time. For example, suppose that you visit a website that has common header and footer images on every page. Every time you visit a new website page, the server must resend the same images. To avoid this, the client caches or stores these images after the first response, and then uses the images directly from the cache. RESTful web services control caching by using API responses that define themselves as cacheable or noncacheable.

##### Code on demand
In REST architectural style, servers can temporarily extend or customize client functionality by transferring software programming code to the client. For example, when you fill a registration form on any website, your browser immediately highlights any mistakes you make, such as incorrect phone numbers. It can do this because of the code sent by the server.

#### HTTP APIs
HTTP protocol APIs use HTTP to communicate. For HTTP requests to have access to a server, HTTP APIs will expose endpoints as API gateways.

HTTP APIs are similar to REST APIs, but support fewer features. HTTP APIs are specifically designed with minimal features so they can be offered at lower prices. HTTP APIs help you create RESTful APIs with lower latency and lower cost than REST APIs. Despite having fewer features than REST APIs, both HTTP and REST APIs are RESTful API products.

Within AWS, you can use HTTP APIs to send requests to Lambda functions or to any routable HTTP endpoint. For example, you can create an HTTP API that integrates with a Lambda function on the backend. When a client calls your API, API Gateway sends the request to the Lambda function and returns the function's response to the client.

#### WebSocket APIs
A WebSocket API in API Gateway is a collection of WebSocket routes that are integrated with backend HTTP endpoints, Lambda functions, or other AWS services. You can use API Gateway features to help you with all aspects of the API lifecycle, from creation through monitoring your production APIs.

API Gateway WebSocket APIs are bidirectional. A client can send messages to a service, and services can independently send messages to clients. This bidirectional behavior offers richer client and service interactions because services can push data to clients without requiring clients to make an explicit request. WebSocket APIs are often used in real-time applications, such as chat applications, collaboration platforms, multiplayer games, and financial trading platforms.

In API Gateway, you can create a WebSocket API as a stateful frontend for an AWS service, such as Lambda or Amazon DynamoDB, or for an HTTP endpoint. The WebSocket API invokes your backend based on the content of the messages it receives from client apps.

Unlike a REST API, which receives and responds to requests, a WebSocket API supports two-way communication between client apps and your backend. The backend can send callback messages to connected clients. You can use API Gateway WebSocket APIs to build secure, real-time communication applications without having to provision or manage any servers to manage connections or large-scale data exchanges.

##### Targeted use cases
Targeted use cases include real-time applications, such as the following:
* Chat applications
* Real-time dashboards, such as stock tickers
* Real-time alerts and notifications

##### API Gateway and WebSocket APIs
API Gateway provides WebSocket API management functionality, such as the following:
* Monitoring and throttling of connections and messages
* Using AWS X-Ray to trace messages as they travel through the APIs to backend services
* Integrating with HTTP and HTTPS endpoints

#### Authorization for API Gateway
The following are examples of how to authorize API calls to your API Gateway endpoints, depending on the API type:
* Use Lambda authorizers. They support bearer token authentication strategies, such as Open Authentication (OAuth) or SAML.
* Use JWT authorizers as a part of OpenID Connect (OIDC) and OAuth frameworks.
* Use IAM to authenticate and authorize entities to access you APIs.
* Use Amazon Cognito with user pools.

Each of the authorizing options has advantages you should match to your application needs and organizational standards. For example, you need to consider who consumes the API. If it’s external developers, you probably want to consider using Lambda authorizers or Amazon Cognito.

#### Lambda authorizers
A Lambda authorizer is an API Gateway feature that uses a Lambda function to control access to your API. A Lambda authorizer is useful if you want to implement a custom authorization scheme that uses a bearer token authentication strategy, such as OAuth or SAML. They are also useful for schemes that use request parameters to determine the caller's identity.

When a client makes a request to one of your API's methods, API Gateway calls your Lambda authorizer, which takes the caller's identity as input and returns an IAM policy as output.

The two types of Lambda authorizers are the following:
* A token-based Lambda authorizer (also called a TOKEN authorizer) receives the caller's identity in a bearer token, such as a JWT or an OAuth token.
* A request parameter-based Lambda authorizer (also called a REQUEST authorizer) receives the caller's identity in a combination of headers, query string parameters, stageVariables, and $context variables.

**For WebSocket APIs, only request parameter-based authorizers are supported.**

If you are using an OAuth strategy as an organization, you might want to consider Lambda authorizers.
Mobile apps, websites, and service connect to API Gateway through the internet. When you use a Lambda function as a Lambda Authorizer, the function will communicate with an OAuth provider and determine if the caller's request is to be allowed or denied. 

1. Lambda functions
A Lambda authorizer is a Lambda function that you can write to perform any custom authorization you need.

2. Calling the Lambda function
When a client calls your API, API Gateway verifies whether a Lambda authorizer is configured for the API method.

If so, API Gateway calls the Lambda function.

3. Supplying authorization
In this call, API Gateway supplies the authorization token or the parameters based on the type of authorizer. The Lambda function returns a policy that allows or denies the caller's request.

4. Caching policy
API Gateway also supports an optional policy cache that you can configure for your Lambda authorizer.

This feature increases performance by reducing the number of invocations of your Lambda authorizer for previously authorized tokens. With this cache, you can configure a custom Time To Live (TTL).


To make it convenient to get started with this method, you can choose the API Gateway Lambda authorizer blueprint when creating your authorizer function from the Lambda console.

#### Lambda authorizer token types
For token-type Lambda authorizers, API Gateway passes the source token to the Lambda function as a JSON input. Based on the value of this token, your Lambda function will determine whether to allow the request.

1. Passing the source token
API Gateway passes the source token to the Lambda function as a JSON input.

Based on the value of this token, your Lambda function will determine whether to allow the request.

2. Validating the request
If the authorizer function allows the request, it will return an IAM policy that allows **execute-API:Invoke** on the particular API resources that you specified. The caller can invoke the specified methods that are defined in the API in the JSON output.

If your Lambda function denies the request, you will need to return a JSON  policy document that denies access to the API methods and resources specified.

#### Lambda authorizer request types
Request-type Lambda authorizers are useful if you need more information about the request itself before authorizing it.

1. When to use the REQUEST type
With request-type authorizers, you can include additional payload in the JSON input to your Lambda function.

If you want to make authorizations that are based on information found in the request header, query string parameters, or body of the request, use the REQUEST type.

2. Validating the request
The Lambda function of the REQUEST authorizer type verifies the input request parameters and returns an ALLOW IAM policy on a specified method.

The ALLOW will only be returned if all of the required parameter values match the preconfigured ones. If they match, the caller can invoke the specified method.

Otherwise, the authorizer function returns an UNAUTHORIZED error without generating any IAM policy.

#### JWT Authorizers
A JWT is a compact and self-contained way to securely transmit information between parties as a JSON object. JWTs can be signed using a secret or a public-private key pair. Thanks to these digital signatures, you can feel safe in knowing that the information has been verified and can be trusted.

JWTs consist of a header, payload, and signature. The following is some additional information about JWT authorizers:
* Typically, the header consists of the token type (JWT) and the signing algorithm.
* The payload contains the claims, which are statements about the entity. Claims are either registered, public, or private.
* The signature consists of a signed version of the encoded header, the encoded payload, a secret, and the signing algorithm specified in the header.

1. Client requests authorization
The application (or client) requests authorization to access your API.

2. OAuth or OIDC Authorizer grants access
The authorizer grants access to the API and grants an access token.

3. Client accesses API
Using the provided token, the client access the protected API.

#### Controling access to HTTP APIs with JWT authorizers
JWT authorizers are only used with HTTP APIs. For HTTP APIs, you can use JWTs as a part of OIDC and OAuth 2.0 frameworks to restrict client access to your APIs.

If you configure a JWT authorizer for a route of your API, API Gateway validates the JWTs that clients submit with API requests. API Gateway allows or denies requests based on token validation, and optionally, scopes in the token. If you configure scopes for a route, the token must include at least one of the route's scopes.

Distinct authorizers can be configured for each route of an API, or the same authorizer can be use for multiple routes. When determining the use of JWT tokens, it's important remember that there is no standard mechanism to differentiate JWT access tokens from other types of JWTs, such as OIDC tokens. Unless you require ID tokens for API authorization, we recommend you configure your routes to require authorization scopes. You can also configure your JWT authorizers to require issuers or audiences that your identity provider uses only when issuing JWT access tokens.

#### Authorizing API requests
API Gateway uses the following general workflow to authorize requests to routes that are configured to use a JWT authorizer.

1. Check identity source for a token
The **identitySource** can include only the token or the token prefixed with Bearer.

2. Decode the token
The token is decoded for verification.

3. Check the token's algorithm and signature
The token's algorithm and signature are checked by using the public key that is fetched from the issuer's **jwks_uri**. Currently, only Rivest–Shamir–Adleman algorithms are supported. API Gateway can cache the public key for 2 hours. 

As a best practice, when you rotate keys, add a grace period during which both the old and new keys are valid.

4. Validate claims
API Gateway evaluates a number of token claims.

If any of these steps fail, API Gateway denies the API request. After the JWT is validated, API Gateway passes the claims in the token to the API route's integration.

#### IAM authorization
You can control access to your Amazon API Gateway API with IAM permissions by controlling access to the following two API Gateway component processes:
* To create, deploy, and manage an API in API Gateway, you will need to grant the API developer permissions. These are needed to perform the required actions supported by the API management component of API Gateway.
* To call a deployed API or to refresh the API caching, you will need to grant the API caller permissions. These are needed to perform required IAM actions supported by the API launch component of API Gateway.

#### API Gateway permissions model for creating and managing an API
You can allow an API developer to create and manage an API in API Gateway. You need to create IAM permissions policies that allow a specified API developer to create, update, deploy, view, or delete required API entities. You attach the permissions policy to a user, role, or group.

#### API Gateway permissions model for invoking an API
You can allow an API caller to invoke the API or refresh its caching. You must create IAM policies that permit a specified API caller to invoke the API method for which user authentication is enabled. The API developer sets the method's **authorizationType** property to **AWS_IAM** to require that the caller submit the user's credentials to be authenticated. Then, you attach the policy to a user, role, or group.

#### The IAM authorization process
IAM is a great choice for authorization if you have an internal service or a restricted number of customers. This is particularly true if you have applications that use IAM to interact with other AWS services using IAM roles.

1. Sig v4
When you turn on IAM authorization, all requests must be signed using the AWS version 4 signing process (also known as Sig v4).

2. Hash-based authentication
The process uses your AWS access key and secret key to compute a hash-based message authentication code (HMAC) signature using SHA 256. You can obtain these keys as an IAM user or by assuming an IAM role.

3. Accessing an API
The key information is added to the authorization header. API Gateway will take that signed request, parse it, and determine whether the user who signed the request has the IAM permissions to invoke your API.

If not, API Gateway will deny and reject that request. So for this type of authentication, your requestor must have AWS credentials.

#### Using Amazon Cognito
There is an alternative to using IAM roles and policies or Lambda authorizers (formerly known as custom authorizers). You can use an Amazon Cognito user pool to control who can access your API in API Gateway.

1. User Pools
Amazon Cognito user pools provide a set of APIs that you can integrate into your application to provide authentication.

User pools are intended for mobile or web applications where you handle user registration and sign-in directly in the application. 

In addition, with Amazon Cognito, you can create your own OAuth 2.0 resource servers and define custom scopes within them.

2. Creating an authorizer
To use an Amazon Cognito user pool with your API, you must first create an authorizer of the COGNITO_USER_POOLS authorizer type. Then, you will need to configure an API method to use that authorizer.

3. OIDC tokens
After a user is authenticated against the user pool, they obtain an OIDC token formatted in a JWT.

Users who have signed in to your application will have tokens provided to them by the user pool. 

Then, that token can be used by your application to inject information into a header in subsequent API calls that you must make against your API Gateway endpoint.

4. Validating the token
The API call succeeds only if the required token is supplied and the supplied token is valid.

Otherwise, the client isn't authorized to make the call because the client did not have credentials that could be authorized.

#### Activity: Controlling Access to your API Gateway
The clients are having trouble delegating different levels of permissions.

##### Which policies do we delegate if we want to limit access broadly?
* Identity-based policies

Wrong answers:
* Resource-based policies
* IAM permissions boundaries

Identiry-based policies are JSON permissions policiy documents that control what actions an identity (users, groups of users, and roles) can perform, on which resources, and under what conditions.

Identity-based policies grant permissions to an identity.

#### Knowledge Check
##### Which principle of the REST architectural style refers to a communication method in which the server completes every client request independently of all previous requests?
* Statelessness

Wrong answers:
* Layered system
* Cacheability
* Uniform interface

REST and WebSocket, along with HTTP, are the common API types used with Amazon API Gateway. Clients can request resources in any order, and every request is stateless or isolated from other requests.

##### Which statement best describes the difference between HTTP APIs and REST APIs?
* HTTP APIs are similar to REST APIs but support fewer features.

Wrong answers:
* HTTP APIs help create basic RESTful APIs, but with higher latency and cost.
* HTTP APIs are specifically designed to maximize features at a higher price point.
* HTTP APIs are not considered a RESTful API product.

HTTP APIs are RESTful APIs designed to support fewer features and provide lower latency and cost.

##### Which API type supports two-way communication between clients and servers without making an explicit request?
* WebSocket

Wromg answers:
* HTTP
* REST
* HTTPS

WebSocket APIs are bidirectional. A client can send messages to a service, and services can independently send messages to clients.

#### Summary
##### API Gateway
API Gateway is an AWS service for creating, publishing, maintaining, monitoring, and securing REST, HTTP, and WebSocket APIs. API developers can create APIs that do the following:
* Can access AWS or other web services
* Can be used in their own client applications
* Can be made available to third-party app developers

##### API
APIs define the rules that you must follow to communicate with other software systems. Developers expose or create APIs so other applications can communicate with their applications programmatically. A web API acts as a gateway between clients and resources on the web.

##### REST APIs
REST is a software architecture that imposes conditions on how an API should work. The REST-based architecture can be used to support high-performing and reliable communication at scale.

The REST architectural style includes a number of principles, including the following:
* Uniform interfaces
* Statelessness
* Layered systems
* Cacheability
* Code on demand

##### HTTP APIs
HTTP APIs use HTTP to communicate. HTTP APIs are similar to REST APIs but are specifically designed with minimal features so they can be offered at lower prices.

##### WebSocket APIs
A WebSocket API in API Gateway is a collection of WebSocket routes integrated with backend HTTP endpoints, Lambda functions, or other AWS services. API Gateway WebSocket APIs are bidirectional, meaning a client can send messages to a service, and services can independently send messages to clients. WebSocket APIs are often used in real-time applications, such as chat applications, collaboration platforms, multiplayer games, and financial trading platforms.

##### API Gateway authorizers
There are many ways to authorize API calls to your API Gateway endpoints, depending on the API type. The following are a few examples:
* Lambda authorizers for REST, HTTP, and WebSocket APIs
* JWT authorizers for HTTP APIs
* IAM authorization for REST, HTTP, and WebSocket APIs
* Amazon Cognito user pools for REST APIs

##### Lambda authorizers
A Lambda authorizer uses a Lambda function to control access to your API. A Lambda authorizer is useful if you want to implement a custom authorization scheme that uses a bearer token authentication strategy, such as OAuth or SAML. They are also useful for schemes that use request parameters to determine a caller's identity.

The following are the two types of Lambda authorizers:
* A token-based Lambda authorizer receives the caller's identity in a bearer token, such as a JWT or an OAuth token.
* A request parameter-based Lambda authorizer receives the caller's identity in a combination of headers, query string parameters, stageVariables, and $context variables.

##### JWT authorizers
A JWT is a compact and self-contained way for securely transmitting information between parties as a JSON object. JWTs consist of a header, payload, and a signature. The following is information about each element:
* The header typically consists of the token type (JWT) and the signing algorithm.
* The payload contains the claims, which are either registered, public, or private.
* The signature consists of a signed version of the encoded header, encoded payload, a secret, and the signing algorithm specified in the header.

##### IAM authorization
There is a requirement to create, deploy, and manage an API in API Gateway. You will need to grant the API developer permissions to perform the required actions supported by the API management component of API Gateway.

There is a requirement to call a deployed API or to refresh the API caching. You will need to grant the API caller permissions to perform required IAM actions supported by the API launch component of API Gateway.

##### Amazon Cognito user pool authorization
There is an alternative to using IAM roles and policies or Lambda authorizers (formerly known as custom authorizers). You can use an Amazon Cognito user pool to control who can access your API in API Gateway.

#### Additional Resources

##### [Protecting REST APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-protect.html)

##### [Protecting HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-protect.html)

##### [Protecting WebSocket APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-protect.html)

#### Protecting APIs

#### Pre-assessment
##### What type of endpoint is exposed when an API is created with Amazon API Gateway?
* HTTPS

Wrong answers:
* FTP
* HTTP
* Trivial FTP

APIs created with API Gateway only expose encrypted HTTPS endpoints.

##### Which type of IAM policy specifies what actions a principal can perform on an Amazon API Gateway resource?
* Resource-based

Wrong answers:
* User-based
* Role-based
* Identity-based

Resource-based policies can also specify what actions a principal can perform on the API Gateway resource and under what conditions.

##### Which method of API protection uses X.509 certificates to verify identities before accessing an API?
* Mutual TLS

Wrong asnwers:
* Throttling
* Cross-origin resource sharing
* Mutual SSH

With mutual TLS, clients must present X.509 certificates to verify their identity to access an API.

#### Protecting data with Amazon API Gateway
##### Amazon API Gateway service
An AWS service used for API:
* Creation
* Publishing
* Maintenance
* Monitoring
* Security

Supported APU types:
* REST
* HTTP
* WebSocket

##### Accessing API Gateway
Access Amazon API Gateway through:
* AWS Management Console
* AWS SDKs
* API Gateway Version 1 APIs
* API Gateway Version 2 APIs
* AWS Command Line Interface
* AWS Tools for Windows PowerShell

##### API Gateway and AWS Lambda
API Gateway works together with AWS Lambda to form the app-facing part of the AWS serverless infrastructure. 
* Use AWS Lambda to interact with required services to allow an app to call publicly available services, which exposes Lambda functions through API methods in API Gateway.
* AWS Lambda runs code, and performs the necessary provisioning and administration of computing resources. 

##### Security aspects of using Amazon API Gateway
* Data protection
* Identity and access management
* Logging
* Monitoring

##### Data protection
* Data in transit
* Data at rest

##### Data protection in transit
* Amazon API Gateway only expose HTTPS endpoints
* API Gateway does not support unencrypted HTTP endpoints
* Certificates for default exacute-api endpoints are managed by API Gateway

Security can be increased by:
* Choosing a minimum Transport Layer Security (TLS) protocol version for enforcement. You can choose either a TLS version 1.0, or a TLS version 1.2 security policy. It’s important to note that WebSocket APIs and HTTP APIs only support TLS 1.2.
* Using an Amazon CloudFront distribution with a custom SSL certificate in your account, and use it with Regional APIs. You can then configure the security policy for the CloudFront distribution of TLS 1.1 or higher, based on your security and compliance requirements.

##### Securing data at rest
* Security for data at rest can be increased by enabling cache encryption for RESR APIs
* Policy for securing data at rest is often deternibed by local, regional, and national regulation

##### Identity and access management for Amazon API Gateway
The audience for AWS IAM for API Gateway falls within one of three categories: 
* service user - uses the API Gateway services to do his job.
* service administrator - provides you with the credentials and permissions that the service user needs.
* IAM administrator is responsible for granting or denying the permissions requested by the service administrator. An IAM administrator can also write policies to manage access to API Gateway.

##### Service users and administrators

##### Service users
* Uses service to accomplish job tasks
* Credentials provided by an administrator

##### Service admins
* In charge of API Gateway resources
* Full access to API Gateway
* Determine features and resources users should access
* Cannot change user permissions

##### IAM Administrators
* Responsible for granting or denying the permissions
* Responds to persmission requests received from service administrator
* Write policies to manage access to API Gateway

##### Authenticating to API Gateway
* As AWS root user
* As an IAM user
* Assuming an IAM role
* Federated account through an identity source, like AWS IAM Identity Center, Google, or Facebook

##### Using IAM policies to manage access to API Gateway
* Specify actions that are allowed or denied
* Set conditions under which actions are allowed and denied

##### IAM resource-based policies
* Specify actions that a proncipal can perform on an API Gateway resource
* Set conditions for acctions
* Resource-based policies are supported for REST APIs

##### Using tags to control access to a REST API
* Tags can be used to provide attribute-based access to API Gateway resources
* Tag information is provided in the condition element of a policy using condition keys

#### Protecting REST, HTTP, and WebSocket APIs
* Generating SSL certificates
* Configuring web application firewalls
* Setting throttling targets
* Only allowing access to an API from a virtual private cloud (VPC)

#### Using mutual TLS authentication for REST and HTTP APIs
Mutual TLS authentication requires two-way authentication between the client and the server. With mutual TLS, clients must present X.509 certificates to verify their identity to access your API. Mutual TLS is a common requirement for Internet of Things (IoT) and business-to-business applications.

You can use mutual TLS along with other authorization and authentication operations that API Gateway supports. API Gateway forwards the certificates that clients provide to AWS Lambda authorizers and to backend integrations.

The following are prerequisites for using mutual TLS:
* A custom domain name
* At least one certificate configured in AWS Certificate Manager (ACM) for your custom domain name
* A truststore configured and uploaded to Amazon Simple Storage Service (Amazon S3)

#### Custom domain names
To activate mutual TLS for a REST or HTTP API, you must configure a custom domain name for your API. You can activate mutual TLS for a custom domain name and then provide the custom domain name to clients. To access an API by using a custom domain name that has mutual TLS turned on, clients must present certificates that you trust in API requests.

##### [Custom domain names](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html)

#### Using ACM issued certificates
You can request a publicly trusted certificate directly from ACM, or import public or self-signed certificates. To use a certificate imported into ACM or a certificate from AWS Private Certificate Authority with mutual TLS, API Gateway needs an **ownershipVerificationCertificate** issued by ACM. This ownership certificate is only used to verify that you have permissions to use the domain name, not for the TLS handshake.

**You will need to keep your ownershipVerificationCertificate valid for the lifetime of your domain name; if it expires and auto-renew fails, all updates to the domain name will be locked!**

#### Configuring a truststore
Truststores are text files with a .pem file extension. They are a trusted list of certificates from certificate authorities (CAs). To use mutual TLS, create a truststore of X.509 certificates that you trust to access your API.

You must include the complete chain of trust, starting from the issuing CA certificate up to the root CA certificate, in your truststore. API Gateway accepts client certificates issued by any CA present in the chain of trust. The certificates can be from public or private CAs. Certificates can have a maximum chain length of four. Finally, you can also provide self-signed certificates.

#### Using throttling to protect REST, HTTP, and WebSocket APIs
You can configure throttling and quotas for your APIs to help protect them from being overwhelmed by too many requests. Both throttles and quotas are applied on a best-effort basis. You should think of them as targets instead of guaranteed request ceilings.

API Gateway throttles requests to your API using the token bucket algorithm, where a token counts for a request. Specifically, API Gateway examines the rate and a burst of request submissions against all APIs in your account, per AWS Region. In the token bucket algorithm, a burst can permit pre-defined overrun of those limits, but other factors can also cause limits to be overrun.

When request submissions exceed the steady-state request rate and burst limits, API Gateway begins to throttle requests. Clients might receive ***429 Too Many Requests*** error responses at this point. On catching such exceptions, the client can resubmit the failed requests in a way that is rate limiting.

An API developer can set the target limits for individual API stages or routes to improve overall performance across all APIs in your account.

#### Applying throttling limit settings
Amazon API Gateway provides four basic types of throttling-related settings.

##### AWS throttling limits
AWS throttling limits are applied across all accounts and clients in a Region. These limit settings exist to prevent your API—and your account—from being overwhelmed by too many requests. These limits are set by AWS, and can't be changed by a customer.

##### Per-account limits
Per-account limits are applied to all APIs in an account in a specified Region. The account-level rate limit can be increased on request. Higher limits are possible with APIs that have shorter timeouts and smaller payloads. If you need an increase in account-level throttling limits per Region, contact the AWS Support Center.

##### Per-API, per-stage
Per-API, per-stage throttling limits are applied at the API method level for a stage. You can configure the same settings for all methods, or configure different throttle settings for each method. These limits can't be higher than the AWS throttling limits.

##### Per-client throttling
Per-client throttling limits are applied to clients that use API keys associated with your usage plan as client identifier. These limits can't be higher than the per-account limits.

The API Gateway throttling-related settings are applied in the following order:
1. Per-client or per-method throttling limits that you set for an API stage in a usage plan
2. Per-method throttling limits that you set for an API stage
3. Account-level throttling per Region
4. AWS Regional throttling

#### Account-level throttling per Region
API Gateway limits the steady-state requests per second across all APIs within an AWS account, per Region by default. It also limits the burst (the maximum bucket size) across all APIs within an AWS account, per Region. In API Gateway, the burst limit represents the target maximum number of concurrent request submissions that API Gateway will fulfill before returning 429 Too Many Requests error responses.

Per-account limits are applied to all APIs in an account in a specified Region. You can increase the account-level rate limit on request. Higher limits are possible with APIs that have shorter timeouts and smaller payloads. To request an increase of account-level throttling limits per Region, contact the AWS Support Center.

#### Route-level throttling for HTTP and WebSocket APIs
For HTTP and WebSocket APIs, you can set route-level throttling to override the account-level request throttling limits for a specific stage, or for individual routes in your API. The default route throttling limits can't exceed account-level rate limits. You can configure route-level throttling using AWS Command Line Interface (AWS CLI).

#### Using AWS WAF to protect an REST APIs
AWS WAF is a web application firewall that helps protect web applications and APIs from attacks. It helps you configure a set of rules called a web access control list (ACL) that allow, block, or count web requests based on customizable web security rules and conditions that you define.

You can use AWS WAF to protect your API Gateway REST API from common web exploits, such as SQL injection and cross-site scripting attacks. These can affect API availability and performance, compromise security, or consume excessive resources. For example, you can create rules to allow or block requests from specified IP address ranges or requests from Classless Inter-Domain Routing blocks. You can also do this for requests from a specific country or region, requests that contain malicious SQL code, or requests that contain malicious scripts.

You can also create rules that match a specified string or a regular expression pattern in HTTP headers, methods, query strings, URIs, and request bodies (limited to the first 8 KB). Additionally, you can create rules to block attacks from specific user agents, bad bots, and content scrapers. For example, you can use rate-based rules to specify the number of web requests that you permit by each client IP in a trailing, continuously updated, 5-minute period.

To use AWS WAF for your API, you will need to perform the following tasks:
1. Using the AWS WAF console, AWS SDK, or AWS CLI, create a Regional web ACL that contains the necessary combination of AWS WAF managed rules and your own custom rules.
2. Associate the AWS WAF Regional web ACL with an API stage. You can do this by using the AWS WAF console, AWS SDK, or AWS CLI or by using the API Gateway console, AWS SDK, or AWS CLI.

#### Using CORS for REST and HTTP APIs
CORS is a browser security feature that restricts HTTP requests initiated from scripts running in the browser. 

CORS is typically required to build web applications that access APIs hosted on a different domain or origin. You can enable CORS to allow requests to your API from a web application hosted on a different domain. For example, if your API is hosted on **https://{api_id}.execute-api.{region}.amazonaws.com/** and you want to call your API from a web application hosted on **example.com**, your API must support CORS.

A cross-origin HTTP request is one that is made to the following:
* A different domain (for example, from **example.com** to **amazondomains.com**)
* A different subdomain (for example, from **example.com** to **petstore.example.com**)
* A different port (for example, from **example.com** to **example.com:10777**)
* A different protocol (for example, from **https://example.com** to **http://example.com**)

Cross-origin HTTP requests have two types: basic requests and non-basic requests. For REST APIs, CORS can be turned on using the API Gateway console or by using an OpenAPI definition file. For HTTP APIs, CORS can be turned on by the following methods:
* Configuring CORS for an HTTP API with a ***$default*** route and JWT authorizer
* Configuring CORS for an HTTP API by using AWS CLI

#### Protecting APIs with Perimeter Protection Services
CloudFront, AWS WAF, and AWS Shield provide a layered security perimeter that co-resides at the AWS edge. Globally distributed API clients can get accelerated API performance by using CloudFront as the entrance to APIs that are hosted on API Gateway. API Gateway endpoints that are hosted in a Region gain access to scaled distributed denial-of-service (DDoS) mitigation capacity across the AWS global edge network.

#### API Gateway endpoints
API endpoint hostname example:

```
{api-id}.execute-api.{region}.amazonaws.com
```

The API endpoint type can be **edge-optimized**, **regional**, or **private**, depending on where the majority of your API traffic originates from.

An **edge-optimized API endpoint** is the default hostname of an API Gateway API. It is deployed to the specified Region, while using a CloudFront distribution to facilitate client access, typically from across AWS Regions. Edge-optimized API endpoints automatically configure the CloudFront distribution. This means that you only need to manually configure the CloudFront distribution if you need more control. 

API requests are routed to the nearest CloudFront Point of Presence (POP), which typically improves connection time for geographically diverse clients. This is the default endpoint type for API Gateway REST APIs.

A **regional API endpoint** is intended for clients in the same Region. When a client running on an EC2 instance calls an API in the same Region, or when an API is intended to serve a small number of clients with high demands, a regional API reduces connection overhead.

For a regional API, any custom domain name that you use is specific to the Region where the API is deployed. If you deploy a regional API in multiple Regions, it can have the same custom domain name in all Regions. You can use custom domains together with Amazon Route 53 to perform tasks such as latency-based routing. 

A **private API endpoint** is an API endpoint that can only be accessed from your Amazon Virtual Private Cloud (VPC) using an interface VPC endpoint, which is an endpoint network interface (ENI) that you create in your VPC.

Now that you have a better understanding of the types of API Gateway endpoints, let's look at ways to secure them.

#### AWS Web Access Firewall (AWS WAF)
When you protect CloudFront distributions with AWS WAF, you can protect your API Gateway API endpoints against common web exploits and bots. These can affect availability, compromise security, or consume excessive resources. AWS Managed Rules for AWS WAF help provide protection against common application vulnerabilities or other unwanted traffic, without needing to write your own rules. AWS WAF rate-based rules automatically block traffic from source IPs when they exceed the thresholds that you define. This helps protect your application against web request floods and alerts you to sudden spikes in traffic that might indicate a potential DDoS attack.

#### AWS Shield
Shield mitigates infrastructure layer DDoS attacks against CloudFront distributions in real time, without observable latency. When you protect a CloudFront distribution with Shield Advanced, you gain additional detection and mitigation against large and sophisticated DDoS attacks. You also gain near real-time visibility into attacks and integration with AWS WAF. When you configure Shield Advanced automatic application layer DDoS mitigation, Shield Advanced responds to application layer attacks by creating, evaluating, and deploying custom AWS WAF rules.

You can take advantage of the perimeter protection layer built with CloudFront, AWS WAF, and Shield and help avoid exposing API Gateway endpoints directly. Use the following approaches to restrict API access through CloudFront only:
1. CloudFront can insert the X-API-Key header before it forwards the request to API Gateway, and API Gateway validates the API key when receiving the requests.
2. CloudFront can insert a custom header (not X-API-Key) with a known secret that is shared with API Gateway. A Lambda custom request authorizer that is configured in API Gateway validates the secret.
3. CloudFront can sign the request with AWS Signature Version 4 by using Lambda@Edge before it sends the request to API Gateway. Configured IAM authorization in API Gateway validates the signature and verifies the identity of the requester.

Although the X-API-Key header approach is straightforward to implement at a lower cost, it’s only applicable to REST API endpoints. If the X-API-Key header already exists, CloudFront will overwrite it. The custom header approach addresses this limitation, but it has an additional cost because it uses a Lambda authorizer. With both approaches, there is an operational overhead for managing keys and rotating the keys periodically. Also, it isn’t a security best practice to use long-term secrets for authorization.

By using the AWS Signature Version 4 approach, you can minimize this type of operational overhead with requests signed with Signature Version 4 in Lambda@Edge.

**Lambda@Edge is a feature of Amazon CloudFront that helps you run code closer to your application. improving performance and latency.**

The signing uses temporary credentials that AWS Security Token Service (AWS STS) provides, and built-in API Gateway IAM authorization performs the request signature validation. There is an additional Lambda@Edge cost in this approach. This approach supports the three API endpoint types available in API Gateway—REST, HTTP, and WebSocket. It also helps secure requests by verifying the identity of the requester, protecting data in transit, and protecting against potential replay attacks. 

##### A proposed solution architecture
1. **Client sends a request**. A client sends a request to an API endpoint that is fronted by CloudFront.
2. **AWS WAF and AWS Shield**. AWS WAF inspects the request at the edge location according to the web ACL rules that you configured. With Shield Advanced automatic application-layer mitigation activated, it can detect a DDoS attack and identify the attack signatures. Shield Advanced then creates AWS WAF rules inside an associated web ACL to mitigate the attack.
3. **Lambda@Edge is invoked**. CloudFront handles the request and invokes the Lambda@Edge function before sending the request to API Gateway.
4. **Request is signed**. The Lambda@Edge function signs the request with Signature Version 4 by adding the necessary headers.
5. **Request is verified**. API Gateway verifies the signed request and sends the request to the backend.
6. **Unauthorized requests**. An unauthorized client sends a request to an API Gateway endpoint, and it receives the HTTP 403 Forbidden message.

You can manage public-facing APIs through API Gateway and protect API Gateway endpoints by using CloudFront and AWS perimeter protection services (AWS WAF and Shield Advanced). These are best-practice approaches to building a DDoS-resilient architecture. These actions can help protect your application’s availability by preventing many common infrastructure and application layer DDoS attacks.

##### [Protecting APIs with Amazon API Gateway and perimeter protection services](https://aws.amazon.com/blogs/security/protect-apis-with-amazon-api-gateway-and-perimeter-protection-services/)

#### Activity: Securing REST APIs
##### The client wants to have the capability to register and sign in directly to their web application. Which authorization method would best support this capability?
* Amazon Cognito user pools

Wromg answers:
* JWT authorizer
* IAM authorization

Amazon Cognito user pools are intended for mobile or web applications where you handle user registration and sign-in directly in the application.

##### What do we first need to implement Amazon Cognito user pools with an API?
* A COGNITO_USER_POOLS authorizer type

Wrong asnwers:
* An HMAC signature using SHA 256 encryption
* An OIDC token formatted in a JWT

To use Amazon Cognito user pool with an API, first create a COGNITO_USER_POOLS authorizer type. Then you need to configure an API method to use that authorizer.

#### [Lab: Using AWS WAF to Mitigate Malicious Traffic](./w10-lab1-securing-web-application-using-aws-waf.md)

#### Knowledge Check
##### Which of the following are requirements for activating mutual TLS for a REST or HTTP API? (Select TWO.)
* A custom domain name
* A truststore configured and uploaded to Amazon S3

Wrong asnwers:
* Cross-Origin Resource Sharing (CORS) activated
* A private certificate authority
* An AWS WAF rule to allow TLS handshakes

To activate mutual TLS for a REST or HTTP API, a user must configure a custom domain name for their API. They must include the complete chain of trust, starting from the issuing certificate authority certificate, up to the root certificate authority certificate, in their truststore.

##### How can a user accelerate API performance for globally distributed API clients using Amazon API Gateway?
* Use an edge-optimized endpoint

Wrong answers:
* Use a REST API
* Set the API throttling limit to zero
* Activate Cross-Origin Resource Sharing (CORS)

API requests are routed to the nearest Amazon CloudFront Point of Presence, which typically improves connection time for geographically diverse clients.

##### What error message might a client receive when Amazon API Gateway begins to throttle requests?
* 429 Too Many Requests

Wrong answers:
* 401 Unauthorized
* 403 Forbidden
* 404 Not Found

Clients might receive 429 Too Many Requests error responses when API Gateway begins to throttle requests.

#### Additional Resources

##### [Mutual TLS](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-mutual-tls.html)

##### [Throttling for REST APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html)

##### [Throttling for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-throttling.html)

##### [Throttling for WebSocket APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-protect.html)

##### [Configuring CORS for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-cors.html)

### Week 11: Security 2 Part 2
