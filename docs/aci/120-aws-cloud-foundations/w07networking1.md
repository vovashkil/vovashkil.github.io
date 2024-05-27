###### back to AWS Cloud Institute repo's root [aci.md](../aci.md)
###### back to repo's main [README.md](../../../README.md)
# Networking 1
## Networking Fundamentals
### Server
A **server** is a physical or virtual computer that runs software services that other computer devices or software can access. Servers are distinguished by the service that they provide. Common servers include:
* **Web server**: Stores and distributes web pages and other web content by using HTTP.
* **File server**: Stores and distributes files.
* **Database server**: Stores databases and manages access to the databases.
* **Print server**: Controls and manages one or more remote printers on the network.
* **Mail server**: Stores and delivers email, like a digital post office.
* **Proxy server**: Improves security by acting as an intermediary for requests from clients seeking resources.

### Client
A **client** is a computer hardware device that accesses a service under the management of a server. The server is typically located on a separate physical computer, and the client must connect to the server over the network to access the service.

For example, suppose you need to access a collection of files that are shared among the workers in your organization. A computer hardware device (the file server) is set up to store and distribute these files. When a user must access a file, they use their client hardware device, which is typically another computer. The client device connects to the file server over the network to retrieve the file.

The client can also refer to a piece of software on the accessing device. For example, a web browser is a client for accessing content from a web server.

### Computer network
A **computer network** is a collection of computing devices that are physically and logically connected to communicate and share resources. 

A **node** refers to any device on a network, whereas a host typically refers to servers on the network. A host is a device to which other computers (nodes) can connect to access data or other services.

#### Computer network connectivity
##### Switch
A switch is a small hardware device that connects multiple devices in the same network. It directs data traffic from a source to a destination device by switching the data from the source to the destination device. 

Computing devices connect to a switch by using a network interface (NIC) and a cable. 

##### Router
A router acts as a dispatcher as it decides which way to send each packet of data. A router is located at any gateway (where one network meets another). A router connects multiple switches, and their respective networks, to enable communication between the different networks.

### Network management models
A network management model is a representation of how data is managed, and how applications are hosted in a network. It is important to understand network management models because it defines the roles and relationships of the devices in your network. The two most common network management models for a local area network (LAN) are client-server and peer-to-peer. 

#### Client-server model
In a **client-server** network model, the data management and application hosting are centralized at the server and distributed to the clients. All clients on the network must use the designated server to access shared files and information that are stored on the serving computer. 

If the server goes down, no client is able to access the network until the server is restored. Examples of client-server models are:
* File server and desktop clients
* Print server and desktop clients
* Several peers in a network connected to each other.

#### Peer-to-peer model
In a **peer-to-peer** network model, each node has its own data and applications, and is responsible for its own management and security.

The peer-to-peer model is a distributed architecture that shares tasks or workloads among peers. Peers are equally privileged participants in the architecture. For example, files can be shared directly between systems on the network without the need for a central server.

This model might be considered under the following conditions:
* Users are responsible for backing up each node.
* Security requirements are not restrictive.
* A limited number of peers are used.

### Network topologies
After you understand the different management models, you can make a better decision about how the nodes in your network might be connected. Computer networks use different topologies to share information. A **topology** is a pattern (or diagram) that shows how nodes connect to each other. Computer networks have both physical topologies and logical topologies.
* **Physical topology**: Refers to the physical layout of wires in the network.
* **Logical topology**: Refers to how data moves through the network.

**Although physical topologies are not applicable to cloud computing with Amazon Web Services (AWS), they provide a model to represent certain aspects of communication in the cloud. An example of this is communications between VPCs.**

This lesson presents some historical topologies such as bus and star, and modern topologies such as mesh and hybrid.

#### BUS
##### Physical topology
A bus topology positions all the devices on a network along a single cable. They run in a single direction from one end of the network to the other. A bus topology is also called a line topology or backbone topology. 

##### Logical topology
The data flow on the network also follows the route of the cable, and moves in one direction.  A bus topology is simple to configure. However, it allows only one computer to send a signal at a time, which can cause network collisions that bring down the network.

#### STAR
##### Physical topology
A star topology is set up so that every node in the network is directly connected to one central switch by using coaxial, twisted-pair, or fiber-optic cable.

##### Logical topology
This central switch manages data transmission. Data that is sent from any node on the network must pass through the central switch to reach its destination. The central switch can also function as a repeater to prevent data loss.

#### MESH
##### Physical topology
A mesh topology is a complex structure of connections similar to peer-to-peer, where the nodes are interconnected. Mesh networks can be full or partial mesh. In a partial mesh topology, all devices are connected to at least two other devices.

In a full-mesh topology, all nodes are interconnected. A full mesh topology provides full redundancy for the network. It is an expensive topology because it requires each node to have multiple network adapters and cables. You will most likely find a full mesh topology in a wide area network (WAN).

#### HYBRID
A **hybrid** topology combines two or more different topology structures. They are usually found in large organizations where separate departments have personalized network topologies to accommodate their network usage and other requirements. The star-bus topology is the most common hybrid topology today.

### Routing overview
**Routing** is the process of path selection in any network. Communication between two nodes in an interconnected network can take place through many different paths. Routing is the process of selecting the best path using predetermined rules. At a high level, routers typically serve the following three main functions:
* Determine the path data takes when it moves from a source to a destination. 
* Forward data to the next device on the selected path to eventually reach its destination.
* Sometimes the router may send copies of the same data packet by using multiple different paths (load balancing).

Data moves along networks in the form of data packets. Each data packet has a header that includes the packet’s intended destination. As a packet travels to its destination, several routers might route it multiple times. When a data packet arrives, the router first looks up its address in a routing table. A routing table lists the routes to particular network destinations. Next, the router forwards or moves the packet onward to the next point in the network.

#### Types of routing
There are two different types of routing, based on how a router creates its routing tables.

##### STATIC ROUTING
In **static routing**, a network administrator uses static tables to manually configure and select network routes. Static routing is helpful in situations where the network design or parameters are expected to remain constant. 

##### DYNAMIC ROUTING
In **dynamic routing**, routers create and update routing tables at runtime based on actual network conditions. They attempt to find the fastest path from the source to the destination by using a dynamic routing protocol, which is a set of rules that create, maintain, and update the dynamic routing table. The biggest advantage of dynamic routing is that it adapts to changing network conditions, including traffic volume, bandwidth, and network failure. 

### Network Communications

### Network protocol
A network protocol is a collection of rules, conventions, and procedures that govern communication between computer systems. Think of it as a language between a subsystem on one computer and its peer on another computer. 

iA web browser on Computer A communicates with a web server on Computer B by using an application protocol, such as HTTP. The network interface (NIC) on Computer A communicates with the NIC on Computer B by using a link layer protocol, such as Ethernet.

#### Types of network protocols
In networking, the following are three main types of network protocols:
* Network management protocols
* Network communication protocols
* Network security protocols

Having a foundational understanding of the different types of protocols helps you choose the best protocols for your network design and business goals.

##### Network communication protocols
How do we ensure your communication across the network? Communication protocols determine the formats and rules used to transfer data over the network. This applies to both hardware and software. Communication protocols also handle authentication and error detection as well as the syntax, synchronization, and semantics that both analog and digital communications must abide by to function.

* **Hypertext transfer protocol (HTTP)** is an application layer protocol that allows the browser and server to communicate.
* **Transmission Control Protocol (TCP)** separates data into packets that can be shared over a network. These packets can then be sent by devices like switches and routers to the designated targets.
* **User Datagram Protocol (UDP)** works in a similar way to TCP, sending packets of data over the network. The key difference between the two is that TCP ensures that a connection is made between the application and server, but UDP does not.
* **Dynamic Host Configuration Protocol (DHCP)** automatically assigns IP addresses to devices connected to a network. 

##### Network management protocols
Network management protocols define the policies and procedures used to monitor, manage, and maintain your network. This ensures stable communication and optimal performance for your network, and these protocols can be applied to all devices on your network (computers, switches, routers, and servers).

Management protocols help to do the following: 
* Troubleshoot connections between host and client devices. 
* Provide connection status, availability, packet or data loss, and so on, related to the health of your network connection.

Common network management protocols:
* **Simple Network Management Protocol (SNMP)** is used to monitor and manage network devices. This TCP-based protocol adds visibility and the ability to modify endpoints, which alter behavior of devices across the network. SNMP relies on the use of agents to collect and send data to an overarching SNMP manager, which in turn queries agents and gets their responses.
* **Internet Control Message Protocol (ICMP)** is primarily used for diagnostic purposes. Managed devices on the network can use this protocol to send error messages, providing information regarding network connectivity issues between devices.

##### Network security protocols
Network security protocols ensure that data traffic on your network is secure. These protocols define how the network secures data from malicious attempts. This protects the data from unauthorized users, services, or devices that access your network data.

Network security protocols rely on encryption and cryptography to secure data.

Common security protocols: 
* **Transport Layer Security (TLS)** is an encryption protocol designed to provide communications security. Client-server applications use the TLS protocol to communicate over a network while preventing eavesdropping and tampering. 
* **Secure File Transfer Protocol (SFTP)**, as its name might suggest, is used to securely transfer files across a network. Data is encrypted and the client and server are authenticated.
* **Secure Hypertext Transfer Protocol (HTTPS)** is the secure version of HTTP, encrypted with TLS. Data sent between the browser and server are encrypted to ensure protection.

### The Internet Protocol (IP)
To properly route your messages to a location, you need an address. Just like each home has a mailing address, each computer has an IP address. However, instead of using the combination of street, city, state, zip code, and country, the IP address uses a combination of bits, 0s and 1s.

An IP address is a numerical label that is assigned to each device on a computer network and uses the Internet Protocol for communication. Here is an example of a 32-bit address in binary format. It’s called 32 bit because you have 32 digits. 

An IP address serves two main functions:
* An IP address identifies a host and a network. 
* IP addresses are also used for location addressing.

**A public IP address is an IP address that can be accessed over the internet. A public IP address is similar to a postal address that is used to deliver mail to your home. A public IP address is a globally unique IP address that is assigned to a computing device that must access the internet.

A private IP address is assigned to computers within a private network and cannot be accessed from the internet. For example, the application and database servers in your data center are assigned private IP addresses.**

### IP address types
Typically, you don’t see an IP address in its binary format. Instead, IP addresses are typically written and displayed as decimal-based or hexadecimal-based notation. The two types of IP addresses are IPv4 and IPv6.

#### IPv4 addresses
IPv4 addresses are represented in 32-bit notation. In the following IPv4 IP address example, the 32 bits are grouped into groups of 8 bits, also called octets. Each of these groups is converted into decimal format separated by a period.

An IPv4 address has two components, the network part and the host part. The number of bits that are allocated to each part depends on the network class and the CIDR block. Classes and CIDR blocks are discussed later in this module.

#### Classful and Classless IP addressing
Shortly after IPv4 was introduced, the Internet Architecture Board (IAB) and supporting community realized there were not enough addresses as more and more devices were connected to the internet. Every laptop, mobile phone, tablet, server, Internet of Things (IoT) device, and so on, needs at least one IP address to connect to the global network, the internet. 

The IPv4 range is split using classful addressing into smaller ranges. This architecture divides IPv4 addresses into 5 address classes by using the leading four address bits. 

1. The Class A range starts at 0.0.0.0 and ends at 127.255.255.255, providing over 2.1 billion IP addresses.
2. The Class B range starts at 128.0.0.0 and ends at 191.255.255.255, providing a little over 1 billion IP addresses.
3. The Class C range starts at 192.0.0.0 and ends at 223.255.255.255, providing a little over 2 million IP address.
4. There are also Class D and Class E IP ranges.

The classful process was eventually replaced with CIDR. CIDR removes the limitations of being limited to class A, B, and C size networks and adds address space use and routing scalability.

#### IPv6 addresses
IPv6 uses a 128-bit addressing scheme, and therefore has more than 79 octillion (7.9 x 1029) times as many available addresses as IPv4. Instead of using binary and decimal digits, IPv6 uses eight sets of four hexadecimal digits (blocks) that are separated with colons. The letters A-F can be uppercase or lowercase, and computers understand either format. One hexadecimal character (0–9, A–F) is represented as 4 bits. So, four hexadecimal characters form a 16-bit group. 

Typically, an IPv6 address consists of two 64-bit parts.
##### Network prefix
The network prefix is the leftmost 64 bits. It is used for routing to different networks.

The network prefix has two sub-components: 
* the global routing prefix 
* and the subnet ID.

##### Interface ID
The interface ID is the rightmost 64 bits and is similar to the host ID for IPv4 addresses.

### Subnetting

### Subnets
As the internet grew, the limited size of the IPv4 address space resulted in a lack of available IP addresses. To create a large number of new network addresses, another way of dividing the 32-bit address was developed. This method is called subnetting.

An IP subnet modifies the IP address by using some host address bits as additional network address bits. That is, the dividing point between the network address and the host address is moved to the right. This division creates more possible networks, but it reduces the number of hosts that are members of each network.

Increase the number of bits that are allocated for the network to create more network addresses.

#### Example 1
Example 1: Suppose you represent a range of network IP addresses as 10.10.x.y, where 10.10 is the network ID. This ID remains fixed (or frozen), and x.y is the host ID where x and y can have any value (wild cards) from 0–255. How many hosts can have a unique IP address in this network?

**Answer**: 256 x 256 = 65,536 IP addresses.

#### Example 2
Example 2: 10.10.101.x, where 10.10.101 is the network ID (or subnet), and x is the host ID and can have any value from 0–255. How many hosts can have a unique IP address in this subnet? 

**Answer**: 256.

### CIDR notation overview
CIDR notation defines an IP address range for a network or a subnet. You specify this set of addresses in the form of a CIDR block—for example, 10.0.0.0/16. When building your network in AWS using VPC components, you specify CIDR blocks for your VPC and subnets. You must allocate enough IP addresses to support the resources on your network. 

You can assign block sizes between /28 (16 IP addresses) and /16 (65,536 IP addresses). CIDR networks are referred to as slash x (/x) networks. CIDR notation is shown here.

**192.168.1.0/24**

It begins with a starting IP address and is separated by a forward slash (the / character) followed by a number. The number at the end specifies how many of the bits of the IP address are fixed. In this example, the first 24 bits of the IP address are fixed. The rest (the last 8 bits) are flexible.

The x represents the number of bits in the IP address range that remain fixed. With CIDR, you can define networks that fall between the old classifications, which enables you to get a range of addresses that are better suited to your needs. 

32 total bits subtracted by 24 fixed bits leaves 8 flexible bits. Each of these flexible bits can be either 0 or 1, because they are binary. That means that you have two choices for each of the 8 bits, providing 256 IP addresses in that IP range.

The higher the number after the /, the smaller the number of IP addresses in your network. For example, a range of 192.168.1.0/24 is smaller than 192.168.1.0/16.

**When working with networks in the AWS Cloud, you choose your network size by using CIDR notation. In AWS, the smallest IP range you can have is /28, which provides 16 IP addresses. The largest IP range you can have is a /16, which provides 65,536 IP addresses.**

### Subnet masks
In a 32-bit IPv4 address, the subnet mask defines which bits of the address represent the network and subnet identifiers. An IPv4 address separates these 32 bits into 4 octets, or 8-bit sections, separated by periods. With a subnet mask, you set host bits to all zeroes and set network bits to all ones. For example, a subnet mask of 255.255.0.0 would have the bits of the first two octets set to 1. The first two octets identify the network, and the last two octets identify the host.

This can also be written in slash notation. In slash notation, the number after the slash matches the number of leading bits set to 1. This example subnet mask would be written as “/16.”

A subnet mask of 255.255.255.0 would have the bits of the first three octets set to 1. The first three octets identify the network, and the last octet identifies the host. This could also be expressed in slash notation as “/24.”

### Loopback address
The IP address range **127.0.0.1–127.255.255.254** is reserved for *loopback*. The loopback IP address is mostly used for testing purposes, like client-server architecture on a single machine. These addresses are managed entirely within the operating system. It enables the client and server processes on a single system to communicate with each other. When a process creates a packet with a destination address that is equal to the loopback address, the operating system loops it back to itself. It does not interact with the NIC. The operating system forwards data that is sent on the loopback to a virtual network interface within the operating system. 

#### Pinging the loopback address on a Linux terminal.
**ping 127.0.0.1**

For example, if a host machine can successfully ping 127.0.0.1 or any IP address from the loopback range, its TCP/IP software stack on the machine is successfully loaded and working.

### OSI Model
Networking follows a logical framework that configures how network traffic travels in both a local and global network. Networking concepts to understand for your design implementations start with how data moves between devices on your local network.  

Networking follows a logical framework that configures how network traffic travels in both a local and global network. Networking concepts to understand for your design implementations start with how data moves between devices on your local network.  

### The OSI model
The OSI model contains seven layers: physical layer, data link layer, network layer, transport layer, session layer, presentations layer, and application layer. These seven layers are the networking stack, which is the software that completes each function. 

The OSI model can further be grouped as Host layers and Media layers. The Media layer consists of layer 1 to layer 3. These layers define how our data moves between point A and point B. Point A could be in your local network, and point B too, or maybe point B is across the internet.

The Host layer consists of the layer 4 to layer 7. These host layers are where your data is broken up for transport and then reassembled when it reaches the destination. It is important to understand how the data is formatted, but also how both point A and point B understand the data connection.

### OSI model
The OSI model was developed by the International Organization for Standardization (ISO) as a model for a computer communications architecture and as a framework for developing protocol standards to recognize the relationship between each /option/group of AWS networking services by understanding the functions and business goals of each.

1. Physical
 Layer 1, the physical layer, helps the devices on your network communicate, and provides transmission and reception of raw bit streams over a physical medium. 
2. Data link
 Layer 2, the data link layer, provides reliable transmission of data frames between two nodes connected by a physical layer. Ethernet is an example of a layer 2 protocol.
3. Network
 Layer 3, the network layer, is responsible for moving the data from the source to the destination. As your network grows, you need a commonality along with structure and management for a network to communicate and move data between multiple different local networks known as inter-networks. Protocols you use in the network protocol include the Internet Protocol (IP).
4. Transport
 Layer 4, the transport layer, adds the functionality to support the networking used on the internet. It provides structuring and managing of your network, including addressing, routing, and traffic control. Two examples of transport protocols are TCP (Transmission Control Protocol) and UDP (User Datagram Protocol).
5. Session
 Layer 5, the session layer, manages communication sessions between two nodes. Network Basic Input/Output System (NetBIOS) is an example of a session protocol.
6. Presentation
 Layer 6, the presentation layer, adds features for the delivery and formatting of the information and further processing or display to the application layer, layer 7. Secure Sockets Layer (SSL) is an example of a presentation layer protocol.
7. Application
 Layer 7, the application layer, is the highest layer of the OSI model, and the closest to the end user. It supports communications for end-user processes and applications, and the presentation of data for user-facing software applications. HTTP (Hypertext Transfer Protocol), FTP (File Transfer Protocol ), and SMTP (Simple Mail Transfer Protocol) are examples of application layer protocols.

**The following are some mnemonics for remembering the OSI model layers:

Top down: APSTNDP – All People Seem To Need Data Processing

Bottom up: PDNTSPA – Please Do Not Throw Sausage Pizza Away**

### Protocol data unit (PDU)
During encapsulation, each layer builds a protocol data unit (PDU). A PDU is the unit of communication for a network protocol. It is a block of information that is composed of protocol-specific control information and a message. Generally, you can identify two major parts of a PDU: the header and the payload. The header contains some data at the front that provides information necessary in communication (such as the sender and receiver). The payload is the actual content of the PDU.

You can compare a PDU to a letter you write to someone. Just like a PDU header, the envelope where you put a letter includes the sender and recipient information. The letter inside of it includes a message, similar to a PDU payload.

When one computer sends data to another computer, data travels down the sender's protocol stack, across the network, and then up the receiver's stack. Different protocols act at each level of the stack, so that each layer has its own PDU.

#### Encapsulation
This process is like placing a letter in an envelope, inside a box, inside a mail truck. Similar to the mail carrier who should not read your mail, each lower layer generally has no knowledge of the upper layers' communication. The lower layer treats the upper layer PDU as raw data. This process is called encapsulation.

#### De-capsulation
When data is received,  it moves up the receiving computer's protocol stack. Each layer removes the payload of its PDU and sends the contents to the next higher layer (as appropriate). This process is called de-encapsulation. It is like when the mail carrier takes the box out of the mail truck and hands it to you. You open the box to find an envelope, and then you open the envelope and read the letter.


In the layered architectures of the OSI model layers, each layer implements protocols tailored to the specific type of data exchange. Protocol data units of the OSI model include the following: 
* The Application layer is where the user interacts with the application they are using. This data is passed to the Presentation layer and then to the Session layer. These three layers add some additional information to the original data that came from the user, and then passes it to the Transport layer.
* At the Transport layer, a header is added, with information such as which port this communication will use. At this point, the PDU at this layer is called a segment or datagram. 
* Segments are then handed to the Network layer for network addressing and routing through the network. At the Network layer, the PDU is called a packet. Packet headers include source and destination IP addresses, and protocol type, among other details. After adding the network header, the packet is sent to the Data Link layer. 
* The Data Link layer encapsulates PDUs in a frame. Frame headers include information such as source and destination media access control (MAC) addresses. Frames also include Frame Check Sequence, which is used for error checking.
* The Layer 1, the physical layer PDU, is the bit. Bits represent raw data, which is transmitted through a physical medium in the network. 

In this example, a computer is sending a file to another computer across a network. The data flows down the OSI stack from the file transfer application to the physical layer network adapter. Then the data flows across the network adapter of the other computer. Finally, the data flows up the OSI stack to the other computer’s application.

### OSI Model in AWS
Understanding the OSI model helps to to manage your on-premises servers, storage, firewalls, switches, and the entire data center. This also helps you to understand how the network and environment work at each layer. The following are some examples:
* Layer 3 adds cross-networking addressing.
* Layer 4 adds the functionality to support the networking used on the internet.
* Layer 7 adds protocols and functions at the software level for applications.

With virtualization, layers of the OSI model are abstracted into software-defined networks. When you are working in AWS, AWS manages the physical layer, and more of the layers become more abstracted and virtualized. And a new OSI model for cloud is beginning to develop.

1. AWS WAF
 AWS WAF manages layer 4 and 7, but works at layer 7. Network security controls such as security groups and network access control lists (ACLs) provide you with options to control network traffic. 

 However, these controls operate at network layer 3 and transport layer 4 of the OSI model. WAF filters traffic based on IP addresses, transport protocols, and ports. 

 You may have additional requirements to have network security controls at the application layer. An example is application protocol detection and filtering based on application protocol properties such as HTTP headers and TLS version. 

 When you build your web application at layer 7, the AWS WAF helps to protect the application by filtering and monitoring HTTP and HTTPs traffic. 
2. Amazon API Gateway
 API Gateways sit at layer 7.
3. CloudFront
 Layer 7 protects applications at layer 7 and uses HTTP, but CloudFront also runs on layers three and four.
4. AWS Cloud Map
 AWS Cloud Map sits at layer 7.
5. Route 53
 Route 53 runs from the application layer, layer 7. It is invoked by the web browser to convert the host name to an IP address. It is an application using the TCP/IP stack. 

 Route 53 transports to query DNS servers for name resolution using TCP/UDP. It sends back the correct IP address, and then the application takes over and uses the TCP/IP stack to pass the destination IP address found by DNS to the transport layer to the network layer, and so on.
6. Elastic load balancers
 Load balancers manage layer four and layer seven, but work at layer seven. From the OSI model, load balancers generally run at layer 4, the transport, or layer 7, the application layer.
* A layer 4 load balancer works at the network protocol level and does not understand or read the network packets, remaining unaware of the specifics of HTTP and HTTPS.
* A layer 7 load balancer inspects packets, has access to HTTP and HTTPS headers, and can do a more intelligent job of spreading the load out to the target.
7. Global Accelerator
 The Global Accelerator sits at layers 4 and 7.
8. Direct Connect
 Direct Connect sits at layers 1 through 4.
9. AWS App Mesh
 App Mesh does not currently allow multiple backend destinations modeled as TCP to share the same port due to restrictions in the information provided to the Envoy proxy at OSI layer 4.
10. Security groups and firewalls
 Network security controls such as security groups and network access control lists (ACLs) provide you with options to control network traffic. However, these controls operate at network layer 3 and the transport 4 layer of OSI model. Traffic is filtered based on IP addresses, transport protocols, and ports.

### The layers of the OSI model in AWS
#### Layer 1 in AWS
Layer 1 in AWS is the physical infrastructure of AWS and it is managed by AWS. Direct Connect allows touch of physical, data link, network, and transport.

#### Layer 2 in AWS
Layer 2 in AWS is the hypervisor. This is the software that allows the hardware to be used. In AWS, you do not have access to this physical hardware, but can use the AWS Command Line Interface (AWS CLI) that is layered on top for some access at layer 2.

#### Layer 3 in AWS
Layer 3 in AWS is the management layer or software-defined data center. You can create an AWS account and start building using the AWS Management Console, AWS CLI, and APIs.

#### Layer 4 in AWS
Layer 4 in AWS is the service layer. This layer is where the following AWS services sit:  Amazon Simple Storage Service (Amazon S3), AWS Lambda, Amazon Relational Database Service (Amazon RDS), or Amazon Elastic Compute Cloud (Amazon EC2). You can create an Amazon VPC, set up network access control lists (network ACLs), security groups, and add access with AWS Identity and Access Management (IAM).

11. PrivateLink
 You can use AWS PrivateLink to make services in your Amazon VPC available to other AWS accounts and Amazon VPCs. 

 AWS PrivateLink is a highly available, scalable technology that establishes private access to services across VPC boundaries. Other accounts and VPCs can create VPC endpoints to access your endpoint service.

 Endpoint services can be created on Network Load Balancers and Gateway Load Balancers.
* A Network Load Balancer functions at the network transport layer 4.
* A Gateway Load Balancer operates at layer 3 of the OSI model.
12. Cloud WAN
 Cloud WAN creates a network topology at layer 3, the network layer.
13. Routes and route tables
 Routes and route tables sit at layer 3.
14. Transit gateway
 A transit gateway acts as a Regional virtual router for traffic flowing between your Amazon VPCs and on-premises networks. 

 Routing through a transit gateway operates at layer 3, where the packets are sent to a specific next-hop attachment, based on their destination IP addresses.

## Networking in AWS
Networking designs, practical approaches, and best practices start at the foundational level. In today's market, you must build a strong network foundation, connect your hybrid infrastructures, and deliver fast and secure applications. AWS offers networking and content delivery services to run your applications with the highest levels of reliability, performance, and security in the cloud.

## AWS Networking Services
AWS offers five categories of networking solutions: 
* network foundations,
* hybrid connectivity,
* edge networking,
* application networking, 
* and network security.

### AWS network foundations
* Amazon VPC
* AWS Transit Gateway
* AWS PrivateLink

The AWS network foundation options support the foundational building blocks of your design, environment, network, and workloads to ensure that you meet your business goals. However, designing and configuring your foundation for networking is different in AWS than it is for on premises. 

#### Amazon VPC
Amazon VPC provides a private location to launch AWS resources in an isolated virtual network. 

Amazon VPC supports services to monitor your network traffic, like 
* Amazon VPC Flow Logs,
* Amazon CloudWatch, 
* and VPC Traffic Mirroring. 

#### AWS Transit Gateway
AWS Transit Gateway is a service to manage and simplify the connections and peering for your Amazon VPCs.

#### AWS PrivateLink
AWS PrivateLink helps to establish secure and private connectivity between Amazon VPCs, AWS services within your Region or inside another Amazon VPC, and your on-premises network.

### Hybrid connectivity
AWS provides services and hybrid connectivity solutions to link your on-premises and AWS networks.
* AWS Direct Connect
* AWS Cloud WAN
* AWS Client VPN
* AWS Site-to-Site VPN

This supports a wide range of hybrid architectures and use cases. 

#### Direct Connect
If you need to connect your data center to AWS, you can use AWS Direct Connect to establish a private and dedicated connection. 

#### AWS Cloud WAN
You can also use AWS Cloud WAN to provide a central dashboard for making connections between your offices, data centers, and Amazon VPCs. 

#### AWS Transit Gateway
You can also use AWS Transit Gateway to connect your Amazon VPCs and on-premises networks. 

#### AWS Client VPN
If you need to connect remote team access, you can use AWS Client VPN to securely connect your remote team to AWS and your on premises resources. 

#### AWS Site-to-Site VPN
If you need to connect remote offices to AWS, you can use AWS Site-to-Site VPN to create secure and encrypted connections quickly.

### AWS edge networking
* Amazon CloudFront
* Amazon Route 53
* AWS Global Accelerator

On AWS, edge networking services securely transmit your user-facing data with improved latency globally. When you use the AWS edge networking services, your traffic moves off the internet and behind the AWS global network. Network edge computing removes the need of reaching back to your data centers or the cloud, to the edge of the network. This interconnects your network and provides a path for the exchange of information quicker. AWS edge networking services sit at the AWS global edge locations and are configured to connect and deliver data with single-digit millisecond AWS network latency. 

#### Amazon CloudFront
Amazon CloudFront delivers data, videos, applications, and APIs with lower latency and higher transfer speeds. 

#### Amazon Route 53
Amazon Route 53 is the Domain Name System (DNS) for AWS. It sends your customers to your applications by translating names like Amazon.com that users use into numeric IP addresses like 192.0.2.1 that computers use. 

#### AWS Global Accelerator
AWS Global Accelerator optimizes your user traffic, from the user to your application.

### Application networking
* Amazon API Gateway
* AWS App Mesh
* AWS Cloudmap

On AWS, you can improve your application's network architecture with services that provide your traditional and modern applications improved 
* security, 
* availability, 
* performance, 
* and efficient monitoring capabilities.

Along with the edge networking services, AWS also offers application networking services to ensure 
* scalability, 
* high availability, 
* improved performance, 
* and security globally.

### Network security
* AWS Firewall Manager
* AWS Shield
* AWS Network Firewall
* AWS WAF

Network security helps to prevent attacks that could degrade your network's responsiveness or expose valuable data to unintended individuals. The AWS services grouped as network security, when properly configured, can help maintain your network's high availability and responsiveness. 

#### AWS Firewall Manager
AWS Firewall Manager helps to centrally configure and manage your firewall rules. 

#### AWS Shield
AWS Shield adds a safeguard to your applications against DDoS attacks. 

#### AWS Network Firewall
AWS Network Firewall deploys network security access for your Amazon VPC. 

#### AWS WAF
AWS WAF protects your web application from common web exploits.

## Networking security 
The shared responsibility model balances the agility of your network with the need to improve the security of the data as it traverses your network using network controls, configurations, and so on.

### AWS Global Infrastructure
The AWS Global Infrastructure is the core of AWS. It sits on the bottom of the shared responsibility model. Different services sit on top of the global infrastructure. 

The global infrastructure consists of Regions, Availability Zones, and edge locations that are located around the world.

AWS manages all of this—the hardware, the security, and so on—for the global infrastructure.

### Services
The next level of the global infrastructure holds the AWS services, tools, and resource. 

Compute, storage, networking, databases, and so on sit at this level on top of the global infrastructure. AWS is again responsibe for managing these services, including the security of these services and systems. 

AWS also manages another level for the AWS services, the software that assists any of the levels of services below it. 

AWS manages the Regions, the AWS Global Infrastructure, the hardware, the network, and the level services such as compute, databases, network, and storage. AWS also manages any software that is used to provide these services.

### Customer responsibility
You are responsible for the operating system and upwards on the share responsibility model. 

Client side data encryption integrity

Authentication, server side encryption, and protecting the network traffic. Including encrypting your data, using Secure Shell Layer (SSL) certificates, and so on. You are responsible for all of this as well as the operating system and the network and firewall configurations. 

You are responsible for your application, and definitely your identity and access management. You configure people to have certain access to our account and the services in that account. You are also responsible for your customer data, securing that data,  and backups of that data.  

## Knowledge check
### Which of the following statements describes a function of the Application layer of the Open Systems Interconnection (OSI) model?
**The application layer supports communications for end-user processes and applications, and the presentation of data for user-facing software applications.**

The physical layer provides transmission and reception of raw bit streams over a physical medium. The transport layer provides structuring and managing of your network, including addressing, routing, and traffic control. The data link layer provides reliable transmission of data frames between two nodes connected by a physical layer.

### Which network device is used to connect multiple networks?
A **router** connects multiple switches, and their respective networks, to enable communication between networks.

A switch is a small hardware device that connects multiple devices in the same network. A host is a device to which other nodes can connect to access data or other services. A node refers to any device on a network.

### Which statement best describes the functions of an IP address?
**An IP address identifies a host and a network, and is used for location addressing.** 

#### A company has a private subnet that needs 100 IP addresses. Which Classless Inter-Domain Routing (CIDR) block would provide enough addresses?
**A CIDR block of /25 provides 128 IP addresses, which is enough to meet the requirement of 100 IP addresses.**

/26 provides 64 IP addresses, /27 provides 32 IP addresses, and /28 provides 16 IP addresses. None of these options would be sufficient to meet the 100 IP addresses requirement.

#### Which statement is true when comparing IP classes with Classless Inter-Domain Routing (CIDR) notation?
**CIDR is a system where IP address ranges are assigned with a smaller rate of unused IP addresses than IP classes.**

### Summary
#### Networking
**Networking** is how you connect computers around the world and allow them to communicate with one another. 

##### COMPUTER NETWORK
A **computer network** is a collection of computing devices that are physically and logically connected to communicate and share resources. A network management model is a representation of how data is managed, and how applications are hosted in a network. Network management models include client-server and peer-to-peer.

##### TOPOLOGY
A **topology** is a pattern that shows how nodes connect to each other. In this module, you learned about some historical topologies such as bus and star, and modern topologies such as mesh and hybrid.

##### ROUTING
**Routing** is the process of path selection in any network. In static routing, a network administrator uses static tables to manually configure and select network routes. In dynamic routing, routers create and update routing tables at runtime based on actual network conditions.

#### Network protocols
A network protocol is a collection of rules, conventions, and procedures that govern communication between computer systems. In networking, the following are three main types of network protocols:
* Network management protocols
* Network communication protocols
* Network security protocols

An IP address is a numerical label that is assigned to each device on a computer network and uses the Internet Protocol for communication. IP addresses can be public or private.
* IPv4 addresses are represented in 32-bit notation.
* IPv6 uses a 128-bit addressing scheme. 

#### Subnetting
* A subnet modifies the IP address by using some host address bits as additional network address bits.
* CIDR notation defines an IP address range for a network or a subnet. You specify this set of addresses in the form of a CIDR block—for example, 10.0.0.0/16.
* Subnet masks define which bits of the address represent the network and subnet identifiers.

#### The OSI model
* The OSI Model is a conceptual framework used to describe the functions of a networking system.
* The OSI model contains seven layers: physical layer, data link layer, network layer, transport layer, session layer, presentations layer, and application layer.
* Mnemonics for remembering the OSI model layers: PDNTSPA – Please Do Not Throw Sausage Pizza Away.

#### Networking services on AWS
##### Network foundation services
AWS network foundation services support the foundational building blocks of your design, environment, network, and workloads to ensure that you meet your business goals. Network foundation services include Amazon VPC, AWS Transit Gateway, and AWS PrivateLink.

##### Hybrid connectivity services
Hybrid connectivity services link your on-premises and AWS networks. Hybrid connectivity services include AWS Direct Connect, AWS Cloud WAN, AWS Transit Gateway, AWS Client VPN, AWS Site-to-Site VPN.

##### Edge networking services
Edge networking services securely transmit your user-facing data with improved latency globally. Edge networking services include Amazon CloudFront, Amazon Route 53, and AWS Global Accelerator.

##### Application networking services
Application networking services ensure scalability, high availability, improved performance, and security globally.

##### Network security services
Network security services can help maintain your network's high availability and responsiveness. Network security services include AWS Firewall Manager, AWS Shield, Network Firewall, and AWS WAF.

### Additional Resources
#### [AWS Networking and Content Delivery](https://aws.amazon.com/products/networking/)

#### [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/)

## Networking in AWS
### Pre-assessment
#### Which of the following statements are applicable to virtual private cloud (VPC) peering connections? (Select TWO.)
**connections are one to one**, and **connections can span accounts**.

A VPC peering connection is a one-to-one relationship between two VPCs. Only one peering resource can exist between any two VPCs.

You can create multiple VPC peering connections for each VPC that you own, but transitive peering relationships are not supported.

### AWS Global Infrastructure
AWS networking helps you connect your workloads to your on-premises environment, customers, and partners. AWS networking services are built on top of the AWS Global Infrastructure. The AWS Global Infrastructure is a collection of smaller groupings of infrastructure that is connected by a global high-speed network.

AWS Global Infrastructure is designed for resiliency and high availability, with redundant hardware and connectivity at geographically dispersed locations across the globe. AWS has multiple Regions, Availability Zones, local zones, and edge locations to help design systems that are resilient and highly available.

### Amazon VPC
#### AMAZON VPC
Amazon VPC is your network environment in the cloud. With Amazon VPC, you can launch AWS resources into a virtual network that you have defined. Virtual private clouds (VPCs) deploy into one of the AWS Regions and can host resources from any Availability Zone within its Region. You can use both IPv4 and IPv6 in your VPC for secure and easy access to resources and applications. A VPC is a virtual network dedicated to your AWS account.

In this example, the VPC uses CIDR 172.31.0.0/16, providing 65,536 addresses.

#### SUBNETS
A subnet is a range of IP addresses in your VPC. You can launch AWS resources into a specified subnet. Use a public subnet for resources that must be connected to the internet and a private subnet for resources that won't be connected to the internet. A subnet resides within one Availability Zone. AWS reserves the first four IP addresses and the last IP address in each subnet CIDR block. Consider larger subnets over smaller ones (/24 and larger). You are less likely to waste or run out of IPs if you distribute your workload into larger subnets.

In this example, VPC 172.31.0.0/16 provides 65,536 addresses. Each public subnet and private subnet has a separate /20 CIDR subnet range, each providing 4,096 addresses. Each subnet's CIDR is a subset of the VPC CIDR.

### Using subnets to divide your VPC
Each subnet must reside within one Availability Zone; it cannot span zones. You can optionally assign an IPv6 CIDR block to your VPC and assign IPv6 CIDR blocks to your subnets. The first four IP addresses and the last IP address in each subnet CIDR block are not available and cannot be assigned to an instance. For example, in a subnet with CIDR block 10.0.0.0/24, the following five IP addresses are reserved:
* 10.0.0.0: Network address.
* 10.0.0.1: Reserved by AWS for the VPC router.
* 10.0.0.2: Reserved by AWS. The IP address of the DNS server is always the base of the VPC network range plus 2.
* 10.0.0.3: Reserved by AWS for future use.
* 10.0.0.255: Network broadcast address. We do not support broadcast in a VPC; therefore, we reserve this address.

This VPC has four subnets. With CIDR /22, it includes a total of 1,024 IP addresses between the four subnets. As AWS reserves five IP addresses from each subnet, each subnet includes 251 available IP addresses.

A subnet resides within one Availability Zone. 

* In addition to the IPv4 addresses, you can also assign an IPv6 CIDR block to your VPC, and assign IPv6 CIDR blocks to your subnets. VPCs permit custom security controls to control inbound and outbound traffic. They require IPv4 and support IPv6.
* The first four IP addresses and the last IP address in each subnet CIDR block are not available and cannot be assigned to an instance. 

## VPC Networking Fundamentals
### VPC core components
#### INTERNET GATEWAYS
An internet gateway permits communication between instances in your VPC and the internet. It imposes no availability risks or bandwidth constraints on your network traffic.

An internet gateway serves the following purposes:

1. Provides a target in your route table for internet-routable traffic

A subnet does not allow outbound traffic by default. Your VPC uses route tables to determine where to route traffic. To allow your VPC to route internet traffic, you create an outbound route in your route table with an internet gateway as a target, or destination. 

2. Protects IP addresses on your network by performing network address translation (NAT)

Resources on your network that connect to the internet should use two kinds of IP addresses:
* Private IP: Use private IPs for communication within your private network. These addresses are not reachable over the internet.
* Public IP: Use public IP addresses for communication between resources in your VPC and the internet. A public IP address is reachable.

An internet gateway performs NAT by mapping a public and private IP address. In this example, the internet gateway translates the source IP of a request from the private IP used on the network (172.31.2.15) to the public IP address (203.0.133.15). The recipient directs its response to the public IP address. The internet gateway receives the response and translates the public IP to the matching private IP address. The VPC routes the response to the requester.

#### ROUTE TABLES
A route table contains a set of rules (routes) that the VPC uses to determine where to direct network traffic. When you create a VPC, it automatically has a main route table. Initially, the main route table (and every route table in a VPC) contains only a single route. This is a local route that permits communication for all the resources within the VPC. You can't modify the local route in a route table. Whenever you launch an instance in the VPC, the local route automatically covers that instance. You can create additional custom route tables for your VPC. 

Each subnet in your VPC must be associated with a route table. If you don't explicitly associate a subnet with a particular route table, the subnet is implicitly associated with and uses the main route table. A subnet can be associated with only one route table at a time, but you can associate multiple subnets with the same route table. Use custom route tables for each subnet to permit granular routing for destinations.

In this example, both route tables direct network traffic locally, but the public route table includes routes to the internet gateway.  

#### PUBLIC SUBNETS
Your public subnet configuration acts as a two-way door—allowing traffic to flow in either direction, invited or not invited. Because there is no automatic outbound routing, you must configure a subnet to be public.

A public subnet requires the following:
* **Internet gateway** – The internet gateway allows communication between resources in your VPC and the internet.
* **Route table** – A route table contains a set of rules (routes) that are used to determine where network traffic is directed. It can direct traffic to the internet gateway.
* **Public IP addresses** – These are addresses that are accessible from the internet. Public IP addresses obscure the private IP addresses, which are only reachable within the network. 

#### PRIVATE SUBNETS
Private subnets allow indirect access to the internet. Traffic stays within your private network. A private IP address assigned to an Amazon EC2 instance will never change unless you manually assign a new IP address on the network interface of the EC2 instance.

Although you can put web-tier instances into a public subnet, we recommend that you put web-tier instances inside private subnets behind a load balancer placed in a public subnet. 

### Elastic IP addresses and NAT gateways
The following VPC components are designed for dynamic cloud computing, allowing you to connect private subnets to the internet. 

#### ELASTIC IP ADDRESSES
An Elastic IP address is a static, public IPv4 address designed for dynamic cloud computing. Elastic IP addresses permit association with an instance or a network interface. They can be re-associated and direct new traffic immediately. Elastic IP addresses are restricted to five per Region and support Bring Your Own IP (BYOIP).

In this example, a customer has access to a public subnet through the internet gateway. Two EC2 instances are shown in the public subnet. An arrow shows that the Elastic IP address 203.0.133.15 in the account is originally associated with one EC2 instance, but it is removed and associated with a new EC2 instance.

#### NETWORK ADDRESS TRANSLATION
NAT is designed for IP address conservation. With NAT, private IP networks that use unregistered IP addresses can connect to the internet. A single device, such as a router, can act as an agent between the internet (public network) and a local network (private network).

#### NAT GATEWAYS
NAT gateways communicate between instances in your VPC and the internet. NAT gateways provide a target in your subnet route tables for internet-routable traffic.

Instances in the private subnet can initiate outbound traffic to the internet or other AWS services.
NAT gateways managed by AWS prevent private instances from receiving inbound traffic from the internet.
You can put NAT gateways in both public and private subnets. If you need more control over your NAT gateway, you can install one on an EC2 instance to create a NAT instance.

**For Accessibility**: A VPC in a single Availability Zone with an internet gateway, a public subnet, and a private subnet. The VPC uses a CIDR of 172.31.0.0/16. The public subnet contains a NAT gateway with an Elastic IP address of 203.0.133.15. The private subnet contains an EC2 instance with a private IP address of 172.31.128.75. Outbound traffic to the internet from the private subnet flows to the NAT gateway. The NAT gateway translates the source address to 203.0.133.15 to obscure the private instance’s private IP address and then sends the traffic to the internet gateway.

### Elastic network interfaces and egress-only internet gateways
#### ELASTIC NETWORK INTERFACES
An elastic network interface is a logical networking component in a VPC that represents a virtual network card. An elastic network interface is a virtual network interface that can be moved across EC2 instances in the same Availability Zone. It maintains its private IP address, Elastic IP address, and message authentication code (MAC) address.

In this graphic, a customer has a route to an elastic network interface through the internet gateway. The interface has an Elastic IP address 203.0.133.15 assigned, in addition to a private IPv4 address of 172.31.2.11. A dotted line shows that the elastic network interface was once attached to an EC2 instance with primary IP address 172.31.2.15. The interface is now attached to an EC2 instance with primary IP address 172.31.2.18. The new attachment is shown with a solid arrow.

#### OUTBOUND-ONLY INTERNET GATEWAYS
An egress-only internet gateway is a VPC component that supports outbound traffic over IPv6 from instances in your VPC to the internet. It prevents the internet from initiating an IPv6 connection with your instances. No NAT instance or NAT gateway is required for IPv6 traffic.

In this graphic, an egress-only internet gateway sits outside of the VPC. A router within the VPC directs IPv6 traffic from a public EC2 instance to the public internet. A custom route table is shown with default local routes for IPv4 and IPv6. IPv6 traffic to ::/0 public destinations have a target of an egress-only internet gateway ID.

### VPC Design Considerations

### Default VPC
Each AWS account comes with a default VPC that is preconfigured for you to use immediately. The default VPC is suitable for getting started quickly and for launching public instances, such as a blog or simple website. The following diagram represents a default VPC. The CIDR block for the default VPC is always a /16 subnet mask. In this example, the CIDR block of 172.31.0.0/16 means that this VPC can provide up to 65,536 IP addresses. It includes one public subnet in each Availability Zone in the Region. These subnets use a /20 subnet mask, providing 4,096 addresses per subnet. It also includes an internet gateway. The VPC uses a main route table to connect the subnets to the internet gateway.

### Benefits of using multiple VPCs
Multiple VPCs create logical isolation for your workloads. You can deploy VPCs into one account, or into multiple accounts for enhanced security. Multiple VPC patterns are best suited for a single team or organization that maintains full control over the provisioning and management of all resources in each application environment.

AWS with multiple VPCs in one Region, or VPCs in multiple accounts or Regions for enhanced security.

### Deploying a VPC across multiple Availability Zones
Deploying a VPC across multiple Availability Zones creates an architecture that achieves high availability by distributing traffic while provide data security. If you have an outage in one Availability Zone, you can fail over to the other.

In this diagram of a VPC spanning two Availability Zones, the backend servers are in two private subnets (app subnets) in the two separate Availability Zones. They send outbound traffic to NAT gateways in public subnets located in their Availability Zone. Backend traffic from both NAT gateways route to an internet gateway.

Elastic Load Balancing (ELB) receives inbound traffic and routes it to the application servers in the private subnets of both Availability Zones. ELB is an AWS service that automatically distributes incoming application traffic across multiple resources, such as Amazon EC2 instances.

### Designing a networking solution using AWS
There's a lot to understand as we look at a standard three-tier architecture. Let's start by just looking at the network components as we look to build an application that begins with a front-end web server, that moves to an application server, and then communicates to a database running in a master standby configuration. We begin by looking at the physical infrastructure and the idea that, even though we've got a three-tier application, we always think from the beginning about high availability. This means running in an AWS Region with multiple Availability Zones. Now, every AWS Region has at least two Availability Zones. You certainly can use more than two, but for the simplicity of today's discussion, we're going to live in Availability Zone 1 and Availability Zone 2.

You, of course, can spread across more if you need. Everything lives inside the VPC. For today, we've chosen the CIDR block of 10.10/16 as our networking component for the VPC.

And then, we've divided our assets into subnets. Everything that lives inside your VPC lives inside a subnet, and the subnets all have their own CIDR block, they cannot collide, they must be unique, and they all are a subset of the core VPC CIDR block itself.

What we want to do is arrange communications in the subnets, always with the goal of protecting the assets. Because how do we want our architecture to be consumed? Do we ever want consumers out here in the internet, communicating directly to the database? No, we never do. We always want them to go through the front-application web servers. And from there, the application servers communicate with the app servers, the app server communicates to the database. But by protecting the database from any outside communication, we protect it against hacks, intrusions, or misuse. There are many lines of defense we're going to put around the sweet gooey center of your application.

We start with the networking components. Instead of putting everything inside a single subnet, we divide our Availability Zones into public subnets and private subnets. If you've done on-premise networking, when you think about subnets, you start thinking about the switches and the routers, and making sure that all the assets that communicate with each other are on the same switch, the same router, and then other assets live on separate routers. In AWS, that's not the purpose of subnets. Now, there's a whole discussion about how AWS networks work under the hood. That's not the subject for today's conversation. If you want to know that, called "A Day in the Life of a Billion Packets."

For today, we want to talk about the fact that any asset in the public subnet are assets that will have direct communication with the outside internet, and anything that is not supposed to be touched directly will live inside a private subnet. Could I have multiple private subnets?

Of course you can; we are simplifying the diagram for instructional purposes.

What makes something public? What makes something private? Again, its access to the outside.

Now, a VPC by definition is a virtual private cloud that allows no traffic in or out except authorized communication.

Traffic in or out happens through the gateways. Now, the first gateway we talk about is the IGW, the internet gateway, and this is what allows communication from the outside internet to pass into your VPC and into whichever subnets are authorized. Well, that's our first step as we talk about routing. The VPC is designed to isolate traffic across any other VPC inside AWS. Well, any asset inside your VPC already knows how to send packets between itself and anyone else, any other component of the VPC. That's done through route tables. When you created the VPC, whether you created it in the console, whether you created it through an API, the default route table object was automatically created for you. Only has one line. In this case, it is the CIDR block of the VPC itself, 10.10/16. And where is the target? It's local. There's nothing else you have to do. But that means any asset inside the VPC, independent of its private IP address, independent of subnet, has a path to send the packet. It does not mean the packet's authorized. That's a later conversation we'll have about security groups and access control lists. But it means that the pack at least knows how to get to the other instance. But that's as far as it does.

If you want a packet from an instance in the public subnet to be able to exit out the IGW and get out into the interwebs, or vice versa, you want the interwebs to connect to your public instance, we have to add the route line that gives the path out through the IGW. We could put that access right into the default route table. The problem is that would apply to every instance, and the whole point of what we're doing is to protect that sweet gooey center right here.

So, instead, we make a new object: the public route table. When you create a new route table it automatically copies everything from the default route table, so it begins with 10.10.0.0/16. That stays local. Now, what we want to do is we want to authorize the public route table, anyone associated with it, to have access to go out the IGW. Well, which IPs are we targeting? We're targeting the entire IPv4 spectrum.

So, how do we do that in CIDR notation? 0.0.0.0/, every address, 0, 136 goes out the IGW. Now, the IGW is not a physical server. It's a network construct. It is a highly available network construct that says that any content that is targeted, that does not fall under the 10.10/16, will automatically then allow to pass outside the region into wherever the DNS lookup sends it. Final thing we need to do is associate the public route table with the public subnets. Now, any packet originating from the web instance or targeted to the web instance, if it's going outside the 10.10/16, will now have a path to go out the IGW, find what it needs, and make the return.

Because we have not added the 0.0.0.0/0 to our private subnets, if someone even knows the IP address of this instance, any attempt for a packet to pass into it will be summarily dropped. It will not touch this instance because there is no route line that allows the IGW to connect to this subnet.

And you cannot hack what you cannot touch. Pretty cool. Except we have another problem, and that is, at some point, I might want this asset to be able to go out to the internet and pick up a patch. Let's say, for example, I need to, this is an Oracle database, I need to go out to oracle.com and download the latest version of Oracle, update my system. Right now, here's exactly how that would happen. The instance would make a request to try to get out to the IGW. What it would do, DNS lookup, go to oracle.com, DNS would say, "Well that's at 54 dot something something."

I'm making the address up, at which point the instance would say, "All right, send the packet off to 54 dot whatever." What's my route table? It's still associated with default route table, 54 dot whatever. Is it part of 10.10/16? No, it's not. No other choice. Packet gets dropped. It cannot communicate out. So, we need to add a few other elements to this architecture to make that happen. We could just associate the public route table.

Problem with that is, then we've exposed our assets, and I've violated all the security protocols I just spent time developing by making this subnet public. The name would still be called private, but because it has 000 IGW access, the subnet is, in fact, a public subnet. The name is irrelevant. You can call this manbearpig. I don't care what you call it. If it has 00 IGW access, it is a public subnet. How do we protect it? Well, we start by looking at the two paths of communication that we're trying to solve in this scenario.

And the first path we're trying to solve is communication from the outside, because what you have is a DBA who wants to be able to get access to the database in the first place to see if it needs patching.

I have a DBA out at Starbucks, or wherever. She wants to log in and connect to the database. Right now, as it sits, there is no way for her packet to be accepted by the database, so we have to add another object into our architecture to make this happen.

Again, we could assign the public route table. That violates every security mechanism put in place so far. It's a new instance called a bastion host. And the whole idea of a bastion host, or a jump box, is to provide a landing place for your DBA, or your system administrator, to log into a public-facing instance. Once they're in there, they can then log in to any other instance that they have the privileges to log into because they're already inside the VPC. Now, the bastion host is going to have all sorts of security groups and access control list protections around it to prevent any unauthorized access into it.

But assuming those are open, your DBA can now log into the bastion, and she will gain root access to that bastion host, at which point she can now connect from the bastion host directly to the database or wherever else she needs because the public subnet has the local line, which means from there the packet to anywhere inside knows its path. Is it authorized or not? That's a different conversation.

We'll assume it is. She now is at root on the database, and now she can log in and do whatever checks she needs, and discovers she needs to go to oracle.com, for example, and download the latest patch from wherever the repository is. Connecting over the bastion servers still does not give her the access to initiate a packet from an instance and get back out the IGW. It doesn't just retrace its steps, so we need another object to then allow initiated traffic from a private subnet to again go out the IGW.

Once again, we have to add something. So, we use an old school trick, it's a NAT server, a Network Address Translation server. This is not something new AWS has invented, and it works fairly simple. The NAT server simply pretends to be the entire internet. The database, on trying to log out, targets the NAT server, thinking it's the whole internet, the NAT server basically says, "Yes I accept, I am whatever address you're looking for," and then it redirects the packet.

Well, to make that happen, we need a new route table. The private route table, we first make a copy as always, the default route table, which means we copy everything from the default table.

So, 10.10. 10.10.0.0/16, my local line. That's normal. The new line is, what do we do with the 000s? We don't go out the IGW. Instead, in this case, my 0.0.0.0/0 goes out the NAT-ID, and we simply target all traffic destined to go outside to this particular instance, and then we associate the private route table with both private subnets. And now, here's how the packet traffic goes. DBA is logged in at root from the database. She wants to now initiate a packet transfer out, so DNS lookup says, "You're going to 54 dot who cares." Packet now wraps itself up, checks the route table, 54 dot whatever, not part of 10.10.

Do I have another option? Yep. 000s, we definitely match that, so you must be the entire internet, and the NAT says, "Yes I am 54 dot whatever." By the way, to make this work you have to turn off source destination checking. That's on by default, and that's very important because that's what protects your asset from getting a man-in-the-middle style attack.

In this case because it's off, the NAT can masquerade and say, "Yes, I am whatever you want me to be. I'm 54 who cares." It's not but it pretends to be. It then takes the packet, reloads it. It has access to the IGW because it has access to the public route table. It sends it out, collects the packet it needs, pulls it back in, repackages it, sends it back, and you've now completed the process.

So, by having the private route table target the NAT, we can get out, or my public route tables can go out direct without needing the NAT access. In either case, when I need to initiate, it's there. Now, am I going to allow it or not? That's a permissions issue. That's another conversation. But at least now we have packets going out. There's one more piece of the puzzle I want to mention, and that's dealing with hybrid options. Because what if I don't even want my DBA to be able to connect from Starbucks? What if I want to require that she can only connect if she's logged into the private data center, or over a VPN tunnel? So, in that case, I have my private data center.

So, my private data center, in this case, I'm going to require that my DBA login from the private data center. And now, I'm going to build a VPN connection into the VPC. I'm not going to go over the IGW. Instead, I'm going to use a new gateway that's called the VGW, or the virtual private gateway.

I can now set up access by adding route table lines into whichever subnet I want direct communication from. So, perhaps I want to allow my DBA to connect direct to the database if they're coming in from the private data center. So, if my private data center uses an IP scheme of 172.68.0.0/16, I simply add that line. And, where am I going? VGW access. So, in this case, she would be able to communicate direct to the instance without needing to go over the bastion server if and only if she initiated her communication directly from the private data center.

Now, is that the best practice element? Every implementation is going to be unique, and you're going to make your own choices, but these become a default set of tools you'll want to consider as you start building out your networking options in AWS Virtual Private Cloud.

### VPC Traffic Security

### Designing your infrastructure with multiple layers of defense
As a best practice, you should secure your infrastructure with multiple layers of defense. Having multiple independent layers of security on your VPC acts as a deterrent, decreasing momentum and effectiveness of potential attacks. This approach requires an attacker to break through multiple layers of specialized defense. As a result, the effort required to mount an attack becomes difficult and costly. There are two main security constraints that you will explore in this module: network access control lists (ACLs) and security groups. 

### Network ACLs
A network ACL is an optional layer of security for your VPC that acts as a firewall for controlling traffic into and out of one or more subnets. A network ACL acts as a firewall at the subnet boundary. A network ACL contains a list of rules to determine whether traffic is allowed into or out of any subnet associated with the network ACL. Every VPC automatically comes with a modifiable default network ACL.
* By default, the default network ACL allows all inbound and outbound IPv4 traffic. You can create a custom network ACL and associate it with a subnet.
* By default, **custom network ACLs deny all inbound and outbound traffic until you add rules**.

**Network ACLs are *stateless*, which means that responses to allowed inbound traffic are subject to the rules for outbound traffic (and the other way around). When using network ACLs, you need explicit rules for both inbound and outbound connections that you want to allow.**

#### Network ACL rules
A network ACL contains a list of numbered rules, which are evaluated in order, starting with the lowest numbered rule. Each network ACL includes a rule whose rule number is an asterisk and is evaluated last. This rule ensures that if a packet doesn't match any of the other numbered rules, it is denied. You can't modify or remove this rule. Network ACLs are stateless, which means that responses to allowed inbound traffic are subject to the rules for outbound traffic, and the other way around.

##### Rule number
Rules are evaluated starting with the lowest numbered rule. As soon as a rule matches traffic, it is applied, regardless of any higher-numbered rule that might contradict it.

##### Type
This is the type of traffic; for example, Secure Shell (SSH). You can also specify all traffic or a custom range.

##### Protocol
You can specify any protocol that has a standard protocol number.

##### Port range
This the listening port or port range for the traffic; for example, 80 for HTTP traffic.

##### Source
For inbound rules only, this is the source of the traffic (CIDR range).

For outbound rules, you instead provide a destination value.

##### Allow or Deny
This is whether to allow or deny the specified traffic.

### Security groups
A security group acts as a virtual firewall for your instance to control inbound and outbound traffic. Security groups act at the network interface level, not the subnet level, and they support Allow rules only. The default group allows inbound communication from other members of the same group and outbound communication to any destination. Traffic can be restricted by any IP protocol, by service port, and by source or destination IP address (individual IP address or CIDR block).

**Security groups are stateful. For example, if you send a request from an instance, the response traffic for that request is allowed to reach the instance, regardless of the inbound security group rules. Responses to allowed inbound traffic are allowed to leave the instance, regardless of the outbound rules.**

#### Security groups
A security group allows traffic based on IP protocol, port, or IP address and uses stateful rules. Traffic can be restricted by any IP protocol, by service port, and by source or destination IP address (individual IP address or CIDR block).

#### Default and new security groups
By default, a security group includes an outbound rule that allows all outbound traffic. You can remove the rule and add outbound rules that allow specific outbound traffic only. If your security group has no outbound rules, no outbound traffic originating from your instance is allowed. Traffic can be restricted by protocol, by service port, and by source IP address (individual IP address or CIDR block) or security group.

#### Custom security group rules
With security group rules, you can filter traffic based on protocols and port numbers. 

The following tables display both inbound and outbound security group rules for a web server. The inbound rules allow for traffic on port 80 and port 443. Any user requesting the web server would be allowed in, and the web server would return the response back to their request. The outbound rules limit outbound traffic to port 1433 and 3306, if responding to traffic on 80 or 443.

#### Security group chaining
Here's an example of a chain of security groups. The inbound and outbound rules are set up in a way that traffic can only flow from the top tier to the bottom tier and back up again. The security groups act as firewalls to prevent a security breach in one tier to automatically provide subnet-wide access of all resources to the compromised client. 
* An encrypted web request comes in from a user on the internet (matching the source of 0.0.0.0/0 for HTTPS), for a web application. 
* The resulting request from the internet user is processed by the website and sent to the application server over HTTP. The application now sends data to the database to be saved. 
* The information summited by the user on the internet is inputted into a MySQL database on the AWS Cloud.

### Comparing security groups and network ACLs
A security group acts as a firewall for associated EC2 instances, controlling both inbound and outbound traffic at the instance level. Network ACLs act as a firewall for associated subnets, controlling both inbound and outbound traffic at the subnet level. A network ACL denies communication by default. The order of network ACL rules matters.

| Security Group | Network ACL |
| -------------- | ----------- |
| Associated to an elastic network interface and implemented in the hypervisor | Associated to a subnet and implemented in the network |
| Supports Allow rules only | Supports Allow and Deny rules |
| A stateful firewall | A stateless firewall |
| All rules evaluated before deciding whether to allow traffic | All rules processed in order when deciding whether to allow traffic |
| Needs to be manually assigned to instances | Automatically applied when instances are added to a subnet |

### DNS
Suppose that a company has a website hosted in the AWS Cloud. Customers enter the web address into their browser, and they are able to access the website. This happens because of **Domain Name System (DNS)** resolution. DNS resolution involves a customer DNS resolver communicating with a company DNS server.

You can think of DNS as being the phone book of the internet. DNS resolution is the process of translating a domain name to an IP address. 

For example, suppose that you want to visit AnyCompany’s website. 
1. When you enter the domain name into your browser, a DNS query is sent to a customer DNS resolver. 
2. The customer DNS resolver asks the company DNS server for the IP address that corresponds to AnyCompany’s website.
3. The company DNS server sends a DNS response with the IP address for AnyCompany’s website, 192.0.2.0.

### DNS options in a VPC
The default VPC, or any VPC created using the Amazon VPC wizard in the Amazon VPC console, includes two DNS settings: 
* **DNS hostnames**: This setting means that AWS will assign DNS names to every EC2 instance in your VPC.
* **DNS resolution**: This setting means that AWS does the DNS for you. Most customers choose to have AWS provide their DNS resolution.

Additionally, default Dynamic Host Configuration Protocol (DHCP) options set in a VPC include the following:
* domain-name-servers=AmazonProvidedDNS
* domain-name=domain-name-for-your-region

The Amazon provided DNS server is at the 169.254.169.253 IPv4 address (or the reserved IP address at the base of the VPC IPv4 network range plus two).

### Amazon Route 53
**Amazon Route 53** is a DNS web service. It gives developers and businesses a reliable way to route end users to internet applications hosted in AWS. Route 53 effectively connects user requests to infrastructure running in AWS—such as EC2 instances, ELB load balancers, or Amazon Simple Storage Service (Amazon S3) buckets. It can also be used to route users to infrastructure outside of AWS.

Another feature of Route 53 is the ability to manage the DNS records for domain names. You can register new domain names directly in Route 53. You can also transfer DNS records for existing domain names managed by other domain registrars. This makes it possible for you to manage all of your domain names within a single location.

#### Route 53 public and private DNS
A hosted zone is a container for records. Records contain information about how you want to route traffic for a specific domain, such as example.com, and its subdomains such as dev.example.com or mail.example.com. A hosted zone and the corresponding domain have the same name. 

##### PUBLIC HOSTED ZONES
**Public hosted zones** contain records that specify how you want to route traffic on the internet.

##### PRIVATE HOSTED ZONES
**Private hosted zones** contain records that specify how you want to route traffic in your VPC.

### Connecting VPCs with VPC Peering

### VPC peering overview
A VPC peering connection is a one-to-one relationship between two VPCs. Only one peering resource can exist between any two VPCs. You can create multiple VPC peering connections for each VPC that you own, but transitive peering relationships are not supported. You can create a VPC peering connection between your own VPCs, or with a VPC in another AWS account **within a single Region**.

### Establishing a VPC peering connection
To establish a VPC peering connection, the owner of the requester VPC (or local VPC) sends a request to the peer VPC. You or another AWS account can own the peer VPC. Your VPC CIDR block cannot overlap with your requester VPC’s CIDR block.

In the following diagram, VPCs A and B are peered. The route table for each VPC has a route with the Classless Inter-Domain Routing (CIDR) range of the opposite VPC targeting the peering connection ID. In the diagram, the peering ID is PCX-1. Local traffic stays within each VPC.

### Example: Three VPCs with two peering connections
This example illustrates the nontransitive nature of VPC peering. In this diagram, VPCs A and B are peered, and VPCs B and C are peered. This does not mean that A can communicate with C. By default, VPC peering does not permit VPC A to connect to VPC C unless they are explicitly established as peers. You control which VPCs can communicate with each other.

### Example: VPC peering for shared services
In this example, your security team provides you with a shared services VPC that each department can peer with. This VPC allows your resources to connect to a shared directory service, security scanning tools, monitoring or logging tools, and other services.

A VPC peering connection with a VPC in a different Region is present. Inter-Region VPC peering allows VPC resources that run in different AWS Regions to communicate with each other using private IP addresses. You won’t be required to use gateways, virtual private network (VPN) connections, or separate physical hardware to send traffic between your Regions.

### Example: Full mesh VPC peering
You can create a full mesh network design using VPC peering to connect each VPC to every other VPC in the organization.

In this architecture, each VPC must have a one-to-one connection with each VPC with which it is approved to communicate. This is because each VPC peering connection is nontransitive in nature and does not permit network traffic to pass from one peering connection to another.

For example, VPC A is peered with VPC C, and VPC C is peered with VPC E. You cannot route packets from VPC A to VPC E through VPC C. To route packets directly between VPC A and VPC E, you must create a separate VPC peering connection between them.

The number of connections required has a direct impact on the number of potential points of failure and the requirement for monitoring. The fewer connections you need, the fewer you need to monitor and the fewer potential points of failure.

As your networking needs scale up, we recommend considering other solutions, such as implementing AWS Transit Gateway. Transit Gateway helps you design and implement networks at scale by acting as a cloud router. Transit Gateway simplifies your network and puts an end to complex peering relationships.

### Facilitating Cross-Service Communications with VPC Endpoints

### VPC endpoints introduction
A VPC endpoint provides a reliable path between your VPC and supported services. You do not need an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. Instances in your VPC do not require public IP addresses to communicate with resources in the service. Endpoints are virtual devices. They are horizontally scaled, redundant, and highly available VPC components. They permit communication between instances in your VPC and services without imposing availability risks or bandwidth constraints on your network traffic.

With a VPC endpoint, you can reach your serverless services without going through the internet.

### Types of VPC endpoints
#### GATEWAY ENDPOINT
A gateway endpoint is appropriate for traffic destined to Amazon S3 or Amazon DynamoDB. Gateway endpoints keep your traffic inside the AWS network.

In the diagram, instance A in the public subnet communicates with Amazon S3 through an internet gateway. Instance A has a route to local destinations in the VPC. Instance B communicates with an S3 bucket and a DynamoDB table using unique gateway endpoints. The diagram shows an example of a private route table. The private route table directs your Amazon S3 and DynamoDB requests through each gateway endpoint using routes. The route table uses a prefix list to target the specific Region for each service.

#### INTERFACE ENDPOINT
With an interface VPC endpoint (interface endpoint), you can privately connect your VPC to services as if they were in your VPC. When the interface endpoint is created, traffic is directed to the new endpoint without changes to any route tables in your VPC. Interface endpoints are powered by AWS PrivateLink.

In this example, a Region is shown with AWS Systems Manager outside of the example VPC. The example VPC has a public and private subnet with an Amazon EC2 instance in each. Systems Manager traffic sent to ssm.region.amazonaws.com is sent to an elastic network interface in the private subnet.

### AWS PrivateLink
AWS PrivateLink provides a private connection between your VPCs and supported AWS services. This AWS service provides secure usage within the AWS network and avoids exposing traffic to the public internet. 

Before PrivateLink, services within a single VPC were connected to multiple VPCs in two ways:
* Public IP addresses using the internet gateway of the VPC
* Private IP addresses using VPC peering

With PrivateLink, services establish a **Transmission Control Protocol (TCP)** connection between the service provider's VPC and the service consumer's VPC. This provides a secure and scalable solution.

In the following diagram, traffic from Amazon EC2 instances in private subnets is routed to a Network Load Balancer. The Network Load Balancer is connected to instances in public subnets that communicate with the internet. This architecture permits backend EC2 instances to communicate with the frontend instances through the PrivateLink endpoint. And it avoids the security and cost implications of data traveling through the public internet.

### Benefits of AWS PrivateLink
#### Security
PrivateLink provides VPCs with a secure and scalable way to privately connect to AWS hosted services. PrivateLink traffic does not use public IP addresses and does not traverse the internet. PrivateLink uses private IP addresses and security groups within a VPC so that regionally hosted services function as though they were hosted directly within a VPC.

#### Simplification
PrivateLink helps avoid security policies that limit benefits of internet gateways and complex networking across a large number of VPCs. PrivateLink removes the need to permit public IPs and manage internet connectivity with internet gateways, NAT gateways, or firewall proxies.

PrivateLink facilitates connectivity to services across different accounts and VPCs, with no need for route table modifications. It is no longer necessary to configure an internet gateway, VPC peering connection, or transit VPC to establish connectivity.

#### Capabilities
PrivateLink gives on-premises networks private access to AWS services through Direct Connect. You can also make services available to other accounts and VPCs that are accessed securely as private endpoints. If you use PrivateLink with a Network Load Balancer to route traffic to your service or application, clients can connect to any service that you host. Services configured to support PrivateLink can be offered as a subscription service through the AWS Marketplace.

### Troubleshooting Your VPC
Troubleshooting your network refers to the process of identifying problems using a precise and repeatable process. You can then solve problems using the verified methods. Troubleshooting helps to target individual network components, test, and document your process. There are many services and tools that you can use to add visibility to troubleshoot, diagnose, and fix network problems.

#### VPC Flow Logs
VPC Flow Logs provides visibility in your VPC by capturing information about the IP traffic going to and from network interfaces. You can use VPC Flow Logs as a centralized source to monitor different network aspects and to provide a history of network traffic flows within entire VPCs, subnets, or specific elastic network interfaces. 

VPC Flow Logs collect metadata for all Amazon VPC networks that are used by your workload. Flow log data can be published to Amazon CloudWatch Logs or to Amazon S3. After you've created a flow log, you can retrieve and view its data in the chosen destination.

Flow logs can help you with several tasks, such as the following:
* Diagnosing overly restrictive security group rules
* Monitoring the traffic that is reaching your instance
* Determining the direction of the traffic to and from the network interfaces

**Flow log data is collected outside of the path of your network traffic, and therefore does not affect network throughput or latency. You can create or delete flow logs without any risk of impact to network performance.**

#### VPC Flow Logs use cases
VPC Flow Logs can be used to analyze and troubleshoot performance, security, and compliance in your VPC.

##### PERFORMANCE
VPC Flow Logs provides 
* flow duration, 
* latency, 
* and bytes sent.

It can be used to identify latencies, establish performance baselines, and improve applications. Being able to identify performance issues quickly delivers a better user experience.

For network performance, VPC Flow Logs can help to do the following:
* Diagnose and troubleshoot connectivity issues across your VPCs and network traffic-related problems.
* Monitor the traffic that is reaching your instance. Flow logs can help you analyze all the requests that come in and either accept or reject them. This improves access control list rules. You can create alarms for unauthorized IP addresses and the unauthorized destination port that is malicious software trying to gain access.
* Determine the direction of the traffic to and from the network interfaces.

##### SECURITY
VPC Flow Logs can be used to log all traffic from a VPC, an interface, or a subnet for root cause analysis to identify gaps in your security. Identifying suspicious traffic tightens security and points to malicious traffic traversing your network.

For network security, VPC Flow Logs can help to do the following:
* Detect network intrusions by tracking the movement of a compromised host, monitoring for port scanning, tracking network enumeration attempts, and data exfiltration.
* Monitor anomaly detection by using flow logs as a security tool to monitor the traffic that is reaching your instance, to profile your network traffic, and to look for abnormal traffic behaviors.
* Monitor remote logins by flagging ports (SSH and RDP) used for administrative activity that should only be accessible from trusted sources. You might also want to monitor the traffic on administrative web app ports.

##### COMPLIANCE
VPC Flow Logs can be used to show that your organization is compliant with specific industry, federal, state, and local regulations that your organization must follow. By directing logs into Amazon S3 to build a data lake, you can ensure that data is available for audits.

Logs stored in Amazon S3 that are accessed intermittently are ideal for quarterly and annual reports. For cost optimization, take advantage of Amazon S3 storage classes, such as S3 Standard-Infrequent Access or Amazon Simple Service Storage Service Glacier, to minimize the cost of maintaining large amounts of log information. Log collection can be automated to centralize flow logs for a multi-account environment to ensure governance and compliance.

For network compliance, VPC Flow Logs can help to do the following:
* Demonstrate that monitored network traffic complies with inbound and outbound regulations.
* Show that access controls have been maintained and no unauthorized events have occurred.

#### VPC Flow Logs basics
Flow log data for a monitored network interface is recorded as a flow log record. Flow log records are log events consisting of fields that describe the traffic flow. They can monitor all activity at three different levels:
* **VPC level** monitors all the activity of your operations within your cloud environment.
* **Subnet level** monitors all activity for a specific subnet.
* **Network interface level** monitors specific interfaces on EC2 instances and captures flow logs from those interfaces.

Flow logs are logs to be ingested and analyzed by network engineers to stay proactive against performance issues that might be caused by latency, anomalous behavior, or other concerns on your network. Providing information on changes in flow duration, latency, and changes in traffic type gives actionable insights with enriched location metadata to optimize your network configuration based on metrics. 

#### Anatomy of a flow log
You can view information about your flow logs in the Amazon EC2 and Amazon VPC consoles by viewing the **Flow Logs** tab for a specific resource. When you select the resource, all the flow logs for that resource are listed. Flow log information includes the following:
* ID of the flow log
* Flow log configuration
* Information about the status of the flow log

##### Account number
This is the AWS account ID of the owner of the source network interface for which traffic is recorded. If the network interface is created by an AWS service (for example when creating a VPC endpoint or Network Load Balancer), the record might display unknown for this field.

##### Network interface
This is the ID of the network interface for which the traffic is recorded.

eni-1235b8ca123456789 is the network interface ID of the system where these packets were sent or received.

##### Source IP
This is the source address for incoming traffic, or the IPv4 or IPv6 address of the network interface for outgoing traffic on the network interface. The IPv4 address of the network interface is always its private IPv4 address.

172.31.9.69 is the source IP address that is sending the traffic. In this case, an IPv4 address is being displayed but the flow logs do not clearly identify inbound and outbound traffic direction.

##### Destination IP
This is the destination address for outgoing traffic, or the IPv4 or IPv6 address of the network interface for incoming traffic on the network interface. The IPv4 address of the network interface is always its private IPv4 address.

172.31.9.12 is the IP address of the receiving system.

##### Source port
This is the source port of the traffic.

49761 identifies the source port being used by the transmitting system.

##### Destination port
This is the destination port of the traffic.

3389 identifies the port expected to receive this traffic. TCP/3389 is Remote Desktop Protocol (RDP) traffic. It provides a user with a graphical interface to connect to another computer over a network connection.

##### Protocol
This is the IANA protocol(opens in a new tab) of the traffic. 

6 confirms that this is a Transmission Control Protocol (TCP) packet.

##### Packets
This is the number of packets transferred during the flow.

The next two fields are where things get interesting. From this flow log, there are 20 packets, for a total of 4249 bytes of information.

##### Action
This is the action that is associated with the traffic:
* ACCEPT – The recorded traffic was permitted by the security groups and network ACLs.
* REJECT – The recorded traffic was not permitted by the security groups or network ACLs. The REJECT field tells that the packet was processed. Security groups and network ACLs help to define which traffic patterns you want to permit through. Which packets are permitted will be based on an intersection of these two security features.  The traffic pattern must be permitted by both to reach your instance.

It is worth noting that AWS does not use REJECT in the classic firewall sense.  With firewalls, you can typically apply one of three actions on a packet stream:
* Permit = Let the traffic through.
* Drop = Quietly remove the packet from the network.
* Reject = Remove the packet from the network and return an administratively prohibited error.

When AWS describes a flow as being rejected, that means the packets have been dropped.

This is important under these circumstances: 
* When you are troubleshooting inbound connection failures, blocked packets will not return an error code.
* If you are controlling outbound sessions, blocked traffic patterns will take longer to timeout, and thus use more CPU and memory.

### Knowledge Check
#### Which action is necessary to make a virtual private cloud (VPC) subnet public?
**Route outbound traffic to an internet gateway.**

Subnets are not public by default. The remaining options will not result in the subnet becoming public.

#### True or false: A single VPC can span multiple Regions.
A single VPC cannot span multiple Regions.

#### What should you use to create traffic filtering rules for a subnet?
A **network ACL** is associated to a subnet. Network ACLs contain a numbered list of rules. You evaluate the rules in order, starting with the lowest numbered rule, to determine whether traffic is allowed into or out of any subnet associated with the network ACL.

The remaining options do not allow for filtering rules for a subnet.

### Summary
#### Amazon VPC
Amazon VPC is your network environment in the cloud. With Amazon VPC, you can launch AWS resources into a virtual network that you have defined. You can launch AWS resources into a specified subnet. Use a public subnet for resources that must be connected to the internet and a private subnet for resources that won't be connected to the internet.

#### VPC core components

##### Internet gateway
An internet gateway permits communication between instances in your VPC and the internet. It imposes no availability risks or bandwidth constraints on your network traffic.

##### Route table
A route table contains a set of rules (routes) that the VPC uses to determine where to direct network traffic.

##### Public subnet
Your public subnet configuration acts as a two-way door—allowing traffic to flow in either direction, invited or not invited. Because there is no automatic outbound routing, you must configure a subnet to be public.

##### Private subnet
Private subnets allow indirect access to the internet. Traffic stays within your private network. A private IP address assigned to an Amazon EC2 instance will never change unless you manually assign a new IP address on the network interface of the EC2 instance.

##### Elastic IP address
An Elastic IP address is a static, public IPv4 address designed for dynamic cloud computing. Elastic IP addresses permit association with an instance or a network interface. They can be re-associated and direct new traffic immediately.

##### NAT
NAT is designed for IP address conservation. With NAT, private IP networks that use unregistered IP addresses can connect to the internet.  NAT gateways communicate between instances in your VPC and the internet. NAT gateways provide a target in your subnet route tables for internet-routable traffic.

##### Elastic network interface
An elastic network interface is a logical networking component in a VPC that represents a virtual network card. An elastic network interface is a virtual network interface that can be moved across EC2 instances in the same Availability Zone.

#### Design considerations
Each AWS account comes with a default VPC that is preconfigured for you to use immediately. The default VPC is suitable for getting started quickly and for launching public instances, such as a blog or simple website. Multiple VPCs create logical isolation for your workloads. You can deploy VPCs into one account, or into multiple accounts for enhanced security.

#### VPC traffic security
There are two main security constraints that you explored in this module: network access control lists (ACLs) and security groups. To review each category, choose the appropriate tab.

##### NETWORK ACL
A network ACL is an optional layer of security for your VPC that acts as a firewall for controlling traffic into and out of one or more subnets. A network ACL acts as a firewall at the subnet boundary.

##### SECURITY GROUP
A security group acts as a virtual firewall for your instance to control inbound and outbound traffic. Security groups act at the network interface level, not the subnet level, and they support Allow rules only.

#### Additional VPC functionality

##### DNS Operations in a VPC
Amazon Route 53 is a DNS web service. It gives developers and businesses a reliable way to route end users to internet applications hosted in AWS. Route 53 effectively connects user requests to infrastructure running in AWS—such as EC2 instances, ELB load balancers, or Amazon Simple Storage Service (Amazon S3) buckets. It can also be used to route users to infrastructure outside of AWS.

##### Connecting VPCs with VPC Peering
A VPC peering connection is a one-to-one relationship between two VPCs. Only one peering resource can exist between any two VPCs. You can create multiple VPC peering connections for each VPC that you own, but transitive peering relationships are not supported.

##### Facilitating Cross-Service Communications with VPC Endpoints
A VPC endpoint provides a reliable path between your VPC and supported services. You do not need an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. Instances in your VPC do not require public IP addresses to communicate with resources in the service. Endpoints are virtual devices. They are horizontally scaled, redundant, and highly available VPC components.

##### VPC Flow Logs
VPC Flow Logs provides visibility in your VPC by capturing information about the IP traffic going to and from network interfaces. You can use VPC Flow Logs as a centralized source to monitor different network aspects and to provide a history of network traffic flows within entire VPCs, subnets, or specific elastic network interfaces.

### Additional Resources
#### [VPCs and Subnets](https://docs.aws.amazon.com/vpc/latest/userguide/how-it-works.html#how-it-works-subnet)

#### [Modifying IPv4 CIDR Block](https://aws.amazon.com/premiumsupport/knowledge-center/vpc-ip-address-range/)
#### [Evolving VPC Design](https://aws.amazon.com/blogs/architecture/one-to-many-evolving-vpc-design/)
#### [Key Considerations and Best Practices](https://aws.amazon.com/blogs/networking-and-content-delivery/vpc-sharing-key-considerations-and-best-practices/)

## AWS Networking Services
### Pre-assessment
#### Which of the following statements are applicable to AWS Direct Connect?
**Direct Connect provides a private, reliable connection to AWS from physical facilities, such as data centers or offices.**

AWS WAF is a web application firewall that helps protect web applications or APIs against common web exploits and bots. Amazon CloudFront routes each user request to the edge location that can best serve content. AWS Shield is a managed DDoS protection service that safeguards applications running on AWS.

#### What is a connection to a transit gateway called?
**Attachment**. A transit gateway attachment is both a source and a destination of packets. The following resources can be attached to a transit gateway:
* One or more VPCs
* One or more VPN connections
* One or more AWS Direct Connect gateways
* One or more Transit Gateway Connect attachments
* One or more transit gateway peering connections

If a transit gateway peering connection is attached, the transit gateway must be in a different Region.

#### What are some of the networking services available in AWS? (Select TWO.)
**Amazon VPC** and **AWS Direct Connect** are services that support networking in AWS. 

Amazon Redshift is a data analytics AWS service.

Amazon S3 and Amazon EBS are storage AWS services.

### AWS networking services overview
AWS offers networking and content delivery services to run your applications with the highest levels of reliability, performance, and security in the cloud. In this lesson, you will dive deeper into AWS networking services.
* Network Foundations
 * Amazon VPC
 * AWS Transit Gateway
 * AWS Private Link
* Hybrid Connectivity
 * AWS Direct Connect
 * AWS Cloud WAN
 * AWS Client VPN
 * AWS Site-to-Site VPN
* Edge Networking
 * Amazon CloudFront
 * Amazon Route 53
 * AWS Global Accelerator
* Network Security
 * AWS Firewall Manager
 * AWS Sgield
 * AWS Network Firewall
 * AWS WAF
* Application Networking
 * Amazon API Gateway
 * AWS App Mesh
 * AWS Cloud Map

### Network foundations
#### VPC connectivity with Transit Gateway
Transit Gateway acts as a hub that controls how traffic is routed among all the connected networks, which act like spokes. This hub-and-spoke model significantly simplifies management and reduces operational costs because each network only has to connect to Transit Gateway and not to every other network. Any new VPC is connected to Transit Gateway and is then automatically available to every other connected network. Transit Gateway connects up to 5,000 VPCs and on-premises environments together.

##### Routing with Transit Gateway
A transit gateway is a network transit hub that you can use to interconnect your VPCs and on-premises networks, and it scales elastically based on traffic. Routing through a transit gateway operates at layer 3, where the packets are sent to a specific next-hop attachment based on their destination IP addresses. Your transit gateway routes IPv4 and IPv6 packets between attachments using transit gateway route tables. Configure route tables to propagate routes from the tables for the attached VPCs and virtual private network (VPN) connections. You can add static routes to the transit gateway route tables.

##### Scaling your network
A transit gateway acts as a cloud router to simplify your network architecture. As your network grows, the complexity of managing incremental connections doesn’t slow you down. When building global applications, you can connect transit gateways using inter-Region peering.

With Transit Gateway Network Manager, you can monitor your VPCs and edge connections from a central console. Integrated with popular software-defined wide area network (SD-WAN) devices, Transit Gateway Network Manager helps you identify issues in your global network.

Traffic between a VPC and transit gateway remains on the AWS global private network and is not exposed to the public internet. Transit Gateway inter-Region peering encrypts all traffic. With no single point of failure or bandwidth bottleneck, it protects you against distributed denial of service (DDoS) attacks and other common exploits.

**Image description**: Six developer VPCs, six production VPCs, VPN, and AWS Direct Connect gateway are attached to Transit Gateway. VPN and Direct Connect link on premises.

#### Transit Gateway components
Transit Gateway is made up of two components: 
* attachments 
* and route tables.

A transit gateway attachment is a source and a destination of packets. You can attach one or more of the following resources if they are in the same Region as the transit gateway:
* VPC
* VPN connection
* Direct Connect gateway
* Transit Gateway Connect
* Transit Gateway peering connection

You can use VPN connections and Direct Connect gateways to connect your on-premises data centers to transit gateways. With a transit gateway, you can connect with VPCs in the AWS Cloud creating a hybrid network.

A transit gateway has a default route table and can optionally have additional route tables. A route table includes dynamic and static routes that decide the next hop based on the destination IP address of the packet. The target of these routes could be any transit gateway attachment. By default, transit gateway attachments are associated with the default transit gateway route table.

Each attachment is associated with exactly one route table. Each route table can be associated with zero to many attachments. 

#### Transit Gateway setup
A transit gateway works across AWS accounts. After you share a transit gateway with another AWS account, the account owner can attach their VPCs to your transit gateway. A user from either account can delete the attachment at any time.

Transit gateways support dynamic and static routing between attached VPCs and VPN connections. You can turn on or turn off route propagation for each attachment.

##### Full connectivity
This diagram shows four VPCs (VPCs A, B, C, and D) with attachments to the transit gateway. A Direct Connect gateway and a VPN connection are also attached to the same transit gateway. A customer gateway device is on the other side of the VPN connection.

In this diagram, all the VPCs can communicate with each other.

##### Partial connectivity
In this diagram, VPC A and VPC C can communicate with each other but not with VPC B or VPC D.

VPC B and VPC D can communicate with each other but not with VPC A or VPC C.

##### Isolation with full access from a VPN
In this diagram, none of the VPCs can communicate with each other, but they can all be accessed through the VPN connection.

### Hybrid Connectivity Services
AWS provides services and hybrid connectivity solutions to link your on-premises and AWS networks. In this lesson, you will dive deeper into data center connectivity with Direct Connect. You will also explore how AWS Client VPN and AWS Site-to-Site VPN can meet your remote access requirements. 

#### Direct Connect
Direct Connect provides a private, reliable connection to AWS from your physical facility, such as a data center or office. It is a fully integrated and redundant AWS service that provides complete control over the data exchanged between your AWS environment and the physical location of your choice.

Direct Connect offers consistent performance with reduced bandwidth cost, backed by a service-level agreement that guarantees 99.99 percent availability. When choosing to implement a Direct Connect connection, you should first consider bandwidth, connection type, protocol configurations, and other network configuration specifications.

##### Network requirements
To use Direct Connect in a Direct Connect location, your network must meet one of the following conditions:
* Your network is co-located with an existing Direct Connect location.
* You are working with a Direct Connect Partner.
* You are working with an independent service provider to connect to Direct Connect.
The two most common solutions are co-locating at a Direct Connect location or contracting with a Direct Connect Partner.

##### CO-LOCATING
You deploy a router and supporting network equipment to a location with a physical uplink to AWS. Direct Connect links your internal network to a Direct Connect location over a standard Ethernet fiber-optic cable. One end of the cable is connected to your router, the other to a Direct Connect router. This is called a cross-connect. With this connection, you can create virtual interfaces directly to public AWS services, such as Amazon Simple Storage Service (Amazon S3) or Amazon VPC, bypassing internet service providers (ISPs) in your network path.

##### CONTRACTING WITH A PARTNER
The Direct Connect Partner provides you with the physical equipment necessary to connect to an AWS router at the Partner's physical location. You use this physical link to configure the Direct Connect service to link your physical location with AWS.

#### AWS VPN
AWS VPN has two services: 
* Site-to-Site VPN enables you to securely connect your on-premises network, such as your branch office site, to Amazon VPC.
* Client VPN enables you to securely connect users, such as remote employees, to AWS or on-premises networks.

##### Site-to-Site VPN
Based on IPsec technology, Site-to-Site VPN uses a VPN tunnel to pass data from the customer network to or from AWS.

One Site-to-Site VPN connection consists of two encrypted tunnels. Each tunnel terminates in a different Availability Zone on the AWS side, but it must terminate on the same customer gateway on the customer side.

###### Customer gateway
A resource you create and configure in AWS that represents your on-premises gateway device. The resource contains information about the type of routing used by the Site-to-Site VPN, Border Gateway Protocol, Autonomous System Number, and other optional configuration information.

###### Customer gateway device
A customer gateway device is a physical device or software application on your side of the Site-to-Site VPN connection.

###### Virtual private gateway
A virtual private gateway is the VPN connection on the Amazon side of the Site-to-Site VPN connection. You use a virtual private gateway or a transit gateway as the gateway for the Amazon side of the Site-to-Site VPN connection.

###### Transit gateway
A transit gateway is a transit hub that can be used to interconnect your VPCs and on-premises networks. You use a transit gateway or virtual private gateway as the gateway for the Amazon side of the Site-to-Site VPN connection.

##### Client VPN
Based on OpenVPN technology, Client VPN is a managed, client-based VPN service that lets you securely access your AWS resources and resources in your on-premises network. With Client VPN, you can access your resources from any location using an OpenVPN-based VPN client.

Client VPN components:

###### Client VPN endpoint
Your Client VPN administrator creates and configures a Client VPN endpoint in AWS. Your administrator controls which networks and resources you can access when you establish a VPN connection.

###### VPN client application
This is the software application that you use to connect to the Client VPN endpoint and establish a secure VPN connection.

###### Client VPN endpoint configuration file
This is a configuration file that is provided to you by your Client VPN administrator. The file includes information about the Client VPN endpoint and the certificates required to establish a VPN connection. You load this file into your chosen VPN client application.

### Edge Fundamentals

### AWS Cloud at the edge
AWS edge computing services provide infrastructure and software that move data processing and analysis as close to the endpoint as necessary. This includes deploying AWS managed hardware and software to locations outside AWS data centers and even onto customer-owned devices.

You can extend the cloud for a consistent hybrid experience using these AWS edge services related to locations.

#### AWS Edge locations
Edge locations are connected to the AWS Regions through the AWS network backbone. Amazon CloudFront, AWS WAF, and AWS Shield are services you use here.

#### AWS Local Zones
Local Zones are an extension of the AWS Cloud located close to large population and industry centers. You learned about Local Zones in Module 1: Architecting Fundamentals.

#### AWS Outposts
With Outposts, you can run some AWS services on premises or at your own data center.

#### AWS Snow Family
The Snow Family of products provides offline storage at the edge, which is used to deliver data back to AWS Regions.

### Edge locations review
#### EDGE LOCATIONS
Remember that an edge location is the nearest point to a requester of an AWS service. Edge locations are connected to Regions using the AWS backbone. They receive requests and can cache copies of your content for faster delivery.

To deliver content to your customers with lower latency, use a global network of edge locations that support AWS services.

Regional edge caches are used as part of the CloudFront service.

#### EDGE LOCATION USE CASE
In the following diagram, a video file is served by an Amazon Elastic Compute Cloud (Amazon EC2) instance acting as a web server in South America. The content can be served faster to a customer in Asia by using an edge location to cache the static video content.

### Edge Services
AWS edge networking services sit at the AWS global edge locations and are configured to connect and deliver data with single-digit millisecond AWS network latency.

#### Content delivery networks 
It’s not always possible to replicate your entire infrastructure across the globe when your web traffic is geo-dispersed. It is also not cost effective. You can use a content delivery network (CDN) for its global network of edge locations to deliver a cached copy of your web content to customers.

#### Edge caching 
Edge caching helps applications perform dramatically faster and cost significantly less at scale. 

##### WITHOUT EDGE CACHING
As an example, suppose that you are serving an image from a traditional web server, not from Amazon CloudFront. You might serve an image named **sunsetphoto.png** using the URL:

**http://example.com/sunsetphoto.png**

Your users can easily navigate to this URL and see the image. They don't realize that their request was routed from one network to another (through the complex collection of interconnected networks that comprise the internet) until the image was found.

Without edge caching architecture, multiple get requests each return results directly from an origin. Custom, ELB or Amazon S3.

##### WITH EDGE CACHING
Amazon CloudFront speeds up the distribution of your content by routing each user request through the AWS backbone network to the edge location that can best serve your content. Typically, this is a CloudFront edge server that provides the fastest delivery to the viewer. 

Using the AWS network can dramatically reduce the number of networks your users' requests must pass through, which improves performance. Users get lower latency (the time it takes to load the first byte of the file) and higher data transfer rates.

You also get increased reliability and availability because copies of your files (also called objects) are now held (or cached) in multiple edge locations around the world.

Two user requests are served by CloudFront with caching. If content is not cached, CloudFront sends get request to origin.

#### Amazon CloudFront
Amazon CloudFront is a global CDN service that accelerates delivery of your websites, APIs, video content, or other web assets. 

It integrates with other AWS products to give developers and businesses a straightforward way to accelerate content to users. There are no minimum usage commitments. 

Integrates with AWS WAF, AWS Shield, and other AWS services.

CloudFront provides extensive flexibility for optimizing cache behavior, coupled with network-layer optimizations for latency, security, and throughput. 

The CDN offers a multi-tier cache by default. CloudFront provides Regional edge caches that improve latency and lower the load on your origin servers when the object is not already cached at the edge.

CloudFront supports real-time, bidirectional communication over the WebSocket protocol. This persistent connection permits clients and servers to send real-time data to one another without the overhead of repeatedly opening connections. 

This feature is especially useful for communications applications such as chat, collaboration, gaming, and financial trading.

With support for WebSockets in Amazon CloudFront, you can manage WebSocket traffic through the same avenues as any other dynamic and static content. 

You can take advantage of distributed denial of service (DDoS) protection using the built-in CloudFront integrations with AWS Shield and AWS WAF.

#### Amazon CloudFront caching
When a user requests content that you are serving with Amazon CloudFront, the user is routed to the edge location that provides the lowest latency. Content is delivered with the best possible performance. 

##### Requested object
The request is routed to the more effective edge location. If the content is already in the edge location with the lowest latency, Amazon CloudFront delivers it immediately.

##### Non-cached content retrieved
Noncached content is retrieved from the origin. If the content is not currently in that edge location, Amazon CloudFront retrieves it from an Amazon S3 bucket or HTTP server that you have identified as the source for the definitive version of your content.

##### Retrieved content is stored in Amazon CloudFront
Origin content is transferred to an Amazon CloudFront edge location for caching. This means that the next user who requests that item will get it from the cache instead of from the origin.

##### Requested object is delivered
Data is transferred to the user. If Amazon CloudFront is serving it directly, this results in a shorter response time than if the user requested the data from the origin directly.

End user content request, CloudFront edge locations with cached copies of objects, and an S3 bucket or custom origin with content.

#### AWS Global Accelerator 
If you deliver applications to your global users over the public internet, your users face inconsistent availability and performance as they traverse through multiple public networks to reach your application. These public networks are often congested, and each hop can introduce availability and performance risk.

As you continue to migrate critical workloads (such as dynamic API delivery, gaming, video, and voice over IP) to AWS, they require higher levels of availability and performance. You can gain these capabilities through the use of multi-Region architectures.

This demand brings several challenges that you must consider, including planning for data consistency and determining how to manage deployments. Of these challenges, one of the critical decisions is determining how to distribute and manage traffic across multiple Regions.

AWS Global Accelerator is a networking service that improves the availability and performance of the applications you offer to your global users. AWS Global Accelerator uses the highly available and congestion-free AWS global network to direct internet traffic from your users to your applications on AWS, making your users’ experience more consistent.

##### Without Global Accelerator
Without AWS Global Accelerator, your access request goes through multiple internet networks. This can cause latency and poses a higher risk of failure.

##### With Global Accelerator
With AWS Global Accelerator, your users' requests reach the Amazon Global Network at the closest AWS edge location, providing expedient and safe access to the AWS network.

Global Accelerator improves your application’s availability by continuously monitoring the health of your application’s endpoints and by routing traffic to the closest healthy endpoints. AWS Global Accelerator also makes it easier to manage your global applications by providing static IP addresses that act as a fixed entry point to your AWS hosted application. The static IP addresses eliminates the complexity of managing specific IP addresses for different AWS Regions and Availability Zones.

### Network Security Services
The AWS services grouped as network security, when properly configured, can help maintain your network's high availability and responsiveness. These network security services can be configured for always-on detection and automatic inline threat mitigations to maximize availability and application responsiveness.

#### DDoS attacks
A DDoS attack is an attack in which multiple compromised systems attempt to flood a target, such as a network or web application, with traffic. A DDoS attack can prevent legitimate users from accessing a service and can cause the system to crash as a result of overwhelming traffic volume.

Imagine you have been waiting for a new red sneaker to be released by your favorite shoe store, AnyCompany. You attempt to visit their online store the day that the sneakers should be available, only to find that the website is unreachable. Meanwhile, AnyCompany is dealing with threat actors demanding money to end the attack, which is preventing customers from making purchases with AnyCompany.

With a DDoS attack, an attacker uses bot primaries to attack a target. The primaries use additional hosts to amplify the requests made to the target, rendering them at full capacity. The target is overwhelmed with requests and fails.

##### Host Layer
7. Application. HTTP floods, DNS query floods. - Application layer attacks.
6. Presentation. SSL abuse. - Presentation layer attacks.
5. Session. N/A.
4. Transport. SYN floods. - Infrastructure layer attacks.

##### Media Layer
3. Network. UDP reflection attacks. - Infrastructure layer attacks.
2. Data link. N/A.
1. Physical. N/A.

##### Open Systems Interconnection (OSI) layers are the following:
* Media layers are 1–3: physical, data link, and network layers.
* Host layers are 4–7: transport, session, presentation, and application layers.

##### Attack types are the following:
* Levels 3 and 4 (network and transport) are infrastructure layers attacks.
* Level 6 are presentation layer attacks.
* Level 7 are application layer attacks.

#### OSI layer attacks
DDoS attacks are most common at the following layers:
* Network (layer 3)
* Transport (layer 4)
* Presentation (layer 6)
* Application (layer 7)

##### Infrastructure layer attacks 
Attacks at layers 3 and 4 are typically categorized as infrastructure layer attacks. These are also the most common type of DDoS attack and include vectors like SYN floods and other reflection attacks like UDP floods. These attacks are usually large in volume and aim to overload the capacity of the network or the application servers. But fortunately, these are also the type of attacks that have clear signatures and are easier to detect.

##### Application layer attacks
An attacker might target the application itself by using a layer 7, or application layer, attack. In these attacks, similar to SYN flood infrastructure attacks, the attacker attempts to overload specific functions of an application to make the application unavailable or extremely unresponsive to legitimate users.

#### AWS Shield
Shield is a managed DDoS protection service that safeguards your applications running on AWS. It provides you with dynamic detection and automatic inline mitigations that minimize application downtime and latency. There are two tiers of Shield: AWS Shield Standard and AWS Shield Advanced.

##### Shield Standard
Shield Standard provides you protection against some of the most common and frequently occurring infrastructure (layer 3 and 4) attacks. This includes SYN and UDP floods and reflection attacks. Shield Standard improves availability of your applications on AWS. The service applies a combination of traffic signatures, anomaly algorithms, and other analysis techniques. Shield Standard detects malicious traffic, and it provides real-time issue mitigation. You are protected by Shield Standard at no additional charge.

##### AWS Shield Advanced
If you need even more protection from DDoS attacks on your applications, consider using Shield Advanced. You get additional detection and mitigation against large and sophisticated DDoS attacks, near real-time visibility, and integration with AWS WAF, a web application firewall.

#### AWS WAF
AWS WAF is a web application firewall that helps protect your web applications or APIs against common web exploits and bots. These exploits and bots might affect availability, compromise security, or consume excessive resources. AWS WAF is a highly configurable and scalable cloud-native web application firewall. It gives you the first line of defense to your applications' incoming threats.

You can monitor web requests, web access control lists (ACLs), and rules using Amazon CloudWatch. CloudWatch collects and processes raw data from AWS WAF and Shield Advanced into readable, near real-time metrics. These statistics are recorded for a period of 2 weeks. You can access historical information and gain a better perspective on how your web application or service is performing.

#### AWS Firewall Manager
AWS Firewall Manager simplifies your AWS WAF and Amazon VPC security groups administration and maintenance tasks. Set up your AWS WAF firewall rules, Shield protections, and Amazon VPC security groups once. The service automatically applies the rules and protections across your accounts and resources, even as you add new resources.

##### Manage rule compliance at scale:
* Simplify management of rules across accounts and application.
* Automatically discover new accounts and remediate noncompliant events.
* Deploy AWS WAF rules from AWS Marketplace.
* Enable rapid response to attacks across all accounts.

AWS Firewall Manager controls
* AWS WAF, 
* Amazon VPC security groups, 
* Shield Advanced, 
* and AWS Network Firewall services.

#### Firewall Manager use cases
Is the number of applications that you run growing? It's important to understand how to manage compliance at scale.

##### Large number of accounts and resources
It is hard to manage security policies centrally across all accounts and resources.

##### New applications created all the time
It is difficult to ensure that all applications are consistently protected on day one.

##### Organization-wide visibility into threats
There is no single place to monitor and respond to any threats across the organization.

### DDoS-resilient reference architecture
You keep bad traffic at the edge by using services like Amazon Route 53, Amazon API Gateway, and CloudFront with AWS WAF and Shield. In this architecture, auto scaling is a last line of defense. Each of these AWS services, depending on the attacks, catch attacks and block them before they reach your VPC.

Services that are available in AWS edge locations, like CloudFront, AWS WAF, Route 53, and API Gateway, take advantage of a global network of edge locations. Multiple edge locations provide applications with greater fault tolerance and increased scale for managing larger volumes of traffic.

In a traditional data center environment, you can mitigate infrastructure-layer DDoS attacks by using techniques like overprovisioning capacity, deploying DDoS mitigation systems, or scrubbing traffic with the help of DDoS mitigation services. On AWS, DDoS mitigation capabilities are automatically provided. You can optimize your application’s DDoS resilience by making architecture choices that best use those capabilities and help you to scale for excess traffic.

In the diagram, AWS WAF and Shield sit on the edge of the architecture and act as gatekeepers, allowing or denying traffic. Recall that Shield protects common layer 3 and layer 4 infrastructure attacks. AWS WAF protects layer 7, the application layer.

#### Architecture diagram
* AWS Cloud has Shield protection. Inside the AWS Cloud are Route 53, API Gateway, AWS WAF, Firewall Manager, CloudFront, and an AWS Region.
* Inside the Region is a VPC.
* The VPC has a public and a private subnet.
* The public subnet has an Elastic Load Balancing (ELB) load balancer.
* The private subnet has an EC2 Auto Scaling group with multiple EC2 instances.
* Users access the AWS Cloud infrastructure through Route 53, and users are filtered through CloudFront or API Gateway.
* Either route is further inspected by ELB.
* DDoS attacks are repelled by Shield and AWS WAF.

### Knowledge check
#### Which AWS service connects up to 5,000 virtual private clouds and on-premises environments together?
**AWS Transit Gateway** connects up to 5,000 VPCs and on-premises environments together. 

You use Amazon VPC to launch resources in an isolated virtual network. 

A NAT gateway is a Network Address Translation (NAT) service. 

AWS PrivateLink provides private connectivity between Amazon VPCs, AWS services, and on-premises networks without exposing traffic to the public internet.

#### Which service is a hybrid connectivity service in AWS?
**Direct Connect** is a hybrid connectivity service and is the shortest path to AWS resources. While in transit, network traffic remains on the AWS global network and never touches the public internet.

Amazon VPC is a network foundations networking service.

API Gateway is an application networking service.

Global Accelerator is an edge networking service.

#### Which are the two tiers available in AWS Shield? (Select TWO.)
**Shield Standard** and **Shield Advanced**.

AWS WAF, Firewall Manager, and Route 53 are other AWS services. AWS WAF is a web application firewall that helps protect web applications or APIs against common web exploits and bots. Firewall Manager simplifies AWS WAF and Amazon VPC security groups administration and maintenance tasks. Route 53 is a Domain Name System web service.

### Summary
#### Network foundations services
**Transit Gateway** acts as a hub that controls how traffic is routed among all the connected networks, which act like spokes. This hub-and-spoke model significantly simplifies management and reduces operational costs because each network only has to connect to Transit Gateway and not to every other network. Any new VPC is connected to Transit Gateway and is then automatically available to every other connected network.

#### Network connectivity services
* **Direct Connect** provides a private, reliable connection to AWS from your physical facility, such as a data center or office. It is a fully integrated and redundant AWS service that provides complete control over the data exchanged between your AWS environment and the physical location of your choice.
* **AWS VPN** has two services. Site-to-Site VPN enables you to securely connect your on-premises network, such as your branch office site, to Amazon VPC. Client VPN enables you to securely connect users, such as remote employees, to AWS or on-premises networks.

#### Network edge services
##### AMAZON CLOUDFRONT
**Amazon CloudFront** is a global CDN service that accelerates delivery of your websites, APIs, video content, or other web assets. When a user requests content that you are serving with Amazon CloudFront, the user is routed to the edge location that provides the lowest latency. Content is delivered with the best possible performance.

##### AWS GLOBAL ACCELERATOR
**AWS Global Accelerator** is a networking service that improves the availability and performance of the applications you offer to your global users. AWS Global Accelerator uses the highly available and congestion-free AWS global network to direct internet traffic from your users to your applications on AWS, making your users’ experience more consistent.

#### Network security services
##### AWS Shield
Shield is a managed DDoS protection service that safeguards your applications running on AWS. It provides you with dynamic detection and automatic inline mitigations that minimize application downtime and latency. There are two tiers of Shield: AWS Shield Standard and AWS Shield Advanced. 

Shield Standard provides you protection against some of the most common and frequently occurring infrastructure (layer 3 and 4) attacks. With Shield Advanced, you get additional detection and mitigation against large and sophisticated DDoS attacks, near real-time visibility, and integration with AWS WAF, a web application firewall.

##### AWS WAF
AWS WAF is a web application firewall that helps protect your web applications or APIs against common web exploits and bots. These exploits and bots might affect availability, compromise security, or consume excessive resources. AWS WAF is a highly configurable and scalable cloud-native web application firewall. It gives you the first line of defense to your applications' incoming threats.

##### AWS Firewall Manager
AWS Firewall Manager simplifies your AWS WAF and Amazon VPC security groups administration and maintenance tasks. Set up your AWS WAF firewall rules, Shield protections, and Amazon VPC security groups once. The service automatically applies the rules and protections across your accounts and resources, even as you add new resources.

### Additional Resources
#### [Common Use Cases](https://docs.aws.amazon.com/vpc/latest/tgw/TGW_Scenarios.html)

### [AWS Shield](https://aws.amazon.com/blogs/aws/aws-shield-protect-your-applications-from-ddos-attacks/)

## Networking 1: Assessment
### Which option is a layer of the Open Systems Interconnection (OSI) model?
The **transport** layer of the OSI model adds the functionality to support the networking used on the internet. It provides structuring and managing of your network, including addressing, routing, and traffic control.

Switch, route, and node are networking communication devices.

### Which action is necessary to make a virtual private cloud (VPC) subnet public?
**To make a VPC subnet public, you need to route outbound traffic to an internet gateway.

Virtual private gateways and NAT gateways use private IP addresses. Public IP addresses come from AWS. Adding your own public IP address block to a subnet doesn't make iy public.

### Which of these entities can a route table be attached to?
Route tables can be attached to **virtual private clouds (VPCs) and subnets**.

Route tables cannot be attached to AWS accounts, Availability Zones, or Regions.

### What are the maint types of network protocols? (Select THREE.)
**Commmunication protocols** determine the formats and rules that are used to transfer data over the network. This applies to both hardware and software. Communication protocols also handle authentication and error detection as well as the syntax, synchronization, and semantics that both analog and digital communications must abide by to function.

**Network management protocols** define the policies and procedures that are used to monitor, manage, and maintain your network. This ensures stable communication and optimal performance for your network. These protocols can be applied to all devices on your network (computers, switches, routers, and servers). Management protocols help to do the following:
* Troubleshoot connections between host and client devices.
* Provide status, availability, packet or data loss, and so on related to the health of your network connection.

**Network security protocols** ensure that data traffic on your network is secure. These protocols define how the network secures data from malicious attempts. This protects the data from unauthorized users, services, or devices that access your network data. Network security protocols rely on encryption and cryptography to secure data.

Network design protocols, network configuration protocols, and network file handling protocols are a combination of **network management, communication, and security protocols**.

### Which statement about protocol data units (PDUs) is accurate?
**During de-encapsulation, each layer removes the payload of its PDU and sends the contents to the next higher layer.** At the transport layer, the PDU is called a segment or datagram.

### Which layers of the OSI model are most commonly targeted during a distributed denial of service (DDoS) attack? (Select THREE.)
The **Application Layer**, **Presentation Layer**, and **Transport Layer** are the most common targets of a DDoS attack. A DDoS atack will attempt to flood these layers with requests in an attempt to overwhelm the system unit it fails.

The Session Layer, Data Link Layer, and Physical Layer are not usually targeted by a DDoS attack. 

### A company has a private subnet that needs 1,010 IPv4 addresses. Which Classless Inter-Domain Routing (CIDR) block would provide enough addresses?
A CIDR network /22 would provide 1,024 IP addresses (32 - 22 = 10 bits).

The other options would not provide sufficient IP addresses to meet this requirement.

### Which protocol below is used at the application layer of the Open Systems Interconnect (OSI) Model? (Select THREE.)
**HTTP**, **FTP**, **SMTP** are application protocols or protocols used at the application layer of the OSI Model.

The Internet Protocol (IP) belongs to layer 3, the Network Layer. The User Datagram Protocol (UDP) and Transmission Control Protocol (TCP) are used by layer 4, the Transport Layer.

### What is true for a security group's default setting?
The default configuration of a security group **blocks all inbound traffic and allows all outbound traffic**.

The rest of the answers are incorrect.

### What function does a NAT gateway serve?
A NAT gateway **allows internet traffic initiated by private subnet instances**.

Elastic Load Balancing load balances incoming traffic to multiple instances. VPC Flow Logs capture information about the IP traffic going to and from network interfaces in your VPC. Security groups can allow or deny traffic at the instance level.

### Which statement best describes the behavior of the network access control list (NACL) attached to a subnet in the AWS Cloud?
The default configuration of an NACL **allows all inbound traffic and allows all outbound traffic**.

The rest of the answers are incorrect.

### Which description is a characteristic of a protocol data unit (PDU)?
**A PDU is the unit of communication for a network protocol.**

PDUs do not receive messages from peer devices. Packets are the data unit inside the IP protocol. A node refers to any device on a network.

### Which AWS service can transalte a website domain name into the unique IP address of the server that is hosting the website content?
**Route 53** can transalte a website domain name into the unique IP address of the server that is hosting the website content.

CloudFront, ELB, and Amazon VPC do not offer this capability.

### What service makes it possible for VPCs, AWS Direct Connect, a VPN connection and the customer gateway all communicate with each other?
**Transit Gateway** permits all these services to communicate with each other through a central hub.

The other options do not offer this capability.

### Which of these AWS services or features connect a virtual private cloud (VPC) to the internet?
An **internet gateway** allows you to connect a VPC to the internet.

A public subnet is a subnet that is assoiated with a route table that has a route to an internet gateway.

A virtual private gateway is the virtual private network (VPN) endpoint on the Amazon side of your AWS Site-toSite VPN connection. AWS Direct Connect can be used to establish a dedicated connection from an on-premises network to one or more VPCs in the same Region.

### Which statement is true for virtual private cloud (VPC) endpoints?
**VPC endpoints permit private communication between instances in your VPC and services without imposing availability risks or bandwidth constraints on your network traffic.**

AWS Shield is a managed DDoS protection service that safeguards your applications running on AWS. Amazon Route 53 manages DNS records for domain names. AWS Direct Connect provides a private, reliable connection to AWS from your physical facility, such as a data center or office.

### You have multiple virtual private clouds (VPCs) connected using VPC peering. Which of the following might lead you to consider converting your architecture using AWS Transit Gateway to replace your current VPC peering connections?
**Transit Gateway solves the complexity involved with creating and managing multiple VPC peering connections at scale.** It does add costs because VPC peering within an Availability Zone is free. VPC peering does not limit the bandwidth.
 
### VPC Flow Logs provides visibility in your VPC by capturing information about the IP traffic going to and from elastic network interfaces. Where can you publish and retrieve VPC Flow Logs from? (Select TWO.)
VPC Flow Logs can be published to **Amazon CloudWatch Logs** or **Amazon S3**. After you've created a flow log, you can retrieve and view data in the chosen destination.

The other options do not offer this capability.

### AWS edge networking services help you deliver content and connect to the AWS Cloud, have low-latency, and are secure. Which of the following is NOT an AWS edge networking service?
**AWS Transit Gateway** is part of the **network foundations services**. Transit Gateway acts as a hub that controls how traffic is routed among all the connected networks.

AWS Cloudfront, Amazon Route 53, and AWS Global Accelerator are AWS edge networking services. Each of these services sit at AWS global edge locations and are configured to connect and deliver data with single-digit milisecond AWS network latency.

### When setting up an AWS Site-to-Site VPN, what is the virtual private gateway?
**A virtual private gateway is the VPN endpoint on the Amazon side of the Site-to-Site VPN connection.** A physical device or software application is a customer gateway device on the customer side of the Site-to-Site VPN connection. A resource that you create and configure in AWS that represents your on-premises gateway device is a customer gateway. A transit hub that can be used to interconnect your VPCs and on-premises networks is a transit gateway.

### Which services permit an on-premises (remote) network to communicate with instances in a virtual private cloud (VPC)? (Select TWO.)
**AWS Site-to-Site VPN** and **Direct Connect** are both services that let you connect an on-premises network to instances in a VPC.

Global Accelerator, PrivateLink, and Transit Gateway do not, by themselves, provide a method for directly connecting an on-premises environment to the AWS Cloud. They can be used in concert with AWS Site-to-Site VPN and Direct Connect in certain configurations. But as a standalone service, they do not serve the purpose that the two applicable services do.

### Which of the following are components of an AWS Site-to-Site VPN connection? (Select TWO.)
**Customer gateway device** and **vitual private gateway**.

A customer gateway device is the physical or software application on your side of the Site-to-Site VPN connection. Vitual private gateway is the VPN concentrator on the Amazon side of the Site-to-Site VPN connection. Use a virtual private gateway or a transit gateway as the gateway for the Amazon side of the Site-to-Site VPN connection.

The rest of the options are not components of a Site-to-Site VPN connection.

### A company wants to reliably route end users to their internet applications hosted on AWS using a unique domain address. Which of the following servuces are available to register and manage Domain Name System (DNS) records as well as transfer DNS records for rxisting domain names?
**Amazon Route 53** is a DNS web service. It gives developers and businesses a reliable way to route end users to internet applications hosted in AWS using unique domain names or web addresses.

AWS Transit Gateway and AWS PrivateLink provide methods of connecting networks and users but neither can setup or manage DNS records.

AWS Global Accelerator is a networking service that improves the availability and performance of the applications you offer to your global users.

### Which AWS service collects and processes raw data from AWS WAF and Shield into readable, near real-time metrics?
**Amazon CloudWatch** collects and processes raw data from AWS WAF and Shield into readable, near real-time metrics. These statistics are recorded for a period of 2 weeks. You can access historical information and gain a better perspective on how your web application or service is performing.

AWS Firewall Manager simplifies your AWS WAF and Amazon VPC security groups administration and maintenance tasks by allowing an administrator to set up AWS WAF firewall rules, Shield protections, and Amazon VPC security groups at once.

Amazon CloudFront is a global CDN service that accelerates delivery of your websites, APIs, video content, or other web assets.

AWS PrivateLink provides a private connection between your VPCs and supported AWS services. The AWS service providess secure usage within the AWS network and avoids exposing traffic to the public internet.

### Which statement describes Amazon CloudFront?
**CloudFront is a global CDN service that accelerates delivery of your websites, APIs, video content, or other web assets.**

VPC Flow Logs captures information about the IP traffic going to and from network interfaces. A user can launch AWS resources into a virtual network that you have defined with a virtual private cloud (VPC). Amazon Route 53 is a DNS web service.
