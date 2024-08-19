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





### Week 7: Storage 2 Part 3
### Week 8: Databases 2 Part 1
### Week 9: Databases 2 Part 2
### Week 10: Security 2 Part 1
### Week 11: Security 2 Part 2
