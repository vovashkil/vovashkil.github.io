# Zero Trust Architecture for Service-To-Service Workloads

* back to AWS Cloud Institute repo's root [aci.md](../../aci.md)
* back to [AWS Cloud Fundamentals 2](../aws-cloud-fundamentals-2.md)
* back to repo's main [README.md](../../../../README.md)

## Resources

* AwsRegion `us-west-2`

---

## Lab Overview

As a network engineer, you are tasked with setting up an AWS Client VPN to allow customers secure access to a server located in an Amazon Virtual Private Cloud (Amazon VPC). However, due to company policies and administrative restrictions on your computer, you can only download and manage sensitive files on an Ubuntu Amazon Elastic Compute Cloud (Amazon EC2) instance on AWS. After carefully planning your approach, you decide on the following solution:

Generate the necessary certificates and keys required for mutual authentication that is needed for the AWS Client VPN endpoint.
Configure the Client VPN endpoint.
Install OpenVPN on an Amazon EC2 instance and test the connectivity.
There are three main components when using AWS Client VPN:

Client VPN endpoint: Your network administrator creates and configures an AWS Client VPN. This controls what networks and resources you can access when you are established on a VPN.

VPN client application: This is the software that you use to connect to the Client VPN endpoint and establish the secure connection. In this lab, you will install OpenVPN on an Ubuntu instance.

Client VPN endpoint configuration file: This configuration file includes information about the Client VPN endpoint and the certificates required to establish the VPN connection. You load this configuration file into your VPN client application.

Objectives
By the end of this lab, you should be able to do the following:

Generate server and client certificates and keys.
Create an AWS Client VPN endpoint.
Install OpenVPN on Ubuntu and test the connection.
Technical knowledge prerequisites
This hands-on lab assumes that you have completed the networking portion of Cloud Fundamentals 1. Due to this assumption, this lab does not walk through some of the provisioning of resources.

Duration
This lab requires approximately 1 hour to complete.

Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose of each icon:

 Command: A command that you must run.
 Expected output: A sample output that you can use to verify the output of a command or edited file.
 Note: Additional information or elaboration on a point.
 Task complete: A conclusion or summary point in the lab.
 WARNING: An action that is irreversible and could potentially impact the failure of a command or process (including warnings about configurations that cannot be changed after they are made).
Start lab
To launch the lab, at the top of the page, choose Start Lab.

 Caution: You must wait for the provisioned AWS services to be ready before you can continue.

To open the lab, choose Open Console .

You are automatically signed in to the AWS Management Console in a new web browser tab.

 Warning: Do not change the Region unless instructed.

Common sign-in errors
Error: Choosing Start Lab has no effect
In some cases, certain pop-up or script blocker web browser extensions might prevent the Start Lab button from working as intended. If you experience an issue starting the lab:

Add the lab domain name to your pop-up or script blocker’s allow list or turn it off.
Refresh the page and try again.
AWS services used in this lab
AWS Client VPN
AWS Client VPN is a managed client-based VPN service that enables you to securely access your AWS resources and the resources in your on-premises network. With Client VPN, you can access your resources from any location using an OpenVPN-based VPN client.

Task 1: Generate server and client certificates and keys
In this task, you launch an Ubuntu instance, and generate the server and client certificates needed for mutual authentication. Client VPN uses these certificates to perform authentication between clients and the Client VPN endpoint. Both certificates will be imported into AWS Certificate Manager (ACM) and specified when you create the Client VPN endpoint.

Task 1.1: Launch an Ubuntu EC2 instance
In this task, you launch an Ubuntu 24.04 LTS (HVM) instance in the VPC called Ubuntu VPC. For more information on how to launch an Amazon EC2 instance, see Connect to your instance.

In the AWS Management Console, in the search box, search for and choose EC2.

Launch an Ubuntu 24.04 LTS (HVM), SSD Volume Type instance with the following settings:

Name the instance Ubuntu.
Choose the Ubuntu Server 24.04 LTS (HVM), SSD Volume Type instance.
For Key Pair (login), choose VPNLabKey.
For the Network settings, ensure that Ubuntu VPC and Ubuntu public subnet are selected.
Ensure that the Auto-assign public IP is set to Enable.
For the Security group setting, choose UbuntuSG.
For the IAM instance profile, choose UbuntuInstanceProfile.
Choose Launch instance.

With the Ubuntu instance selected, choose Actions, choose Networking, and then choose Change source/destination check.

In the pop-up window, select the Stop checkbox, and then choose Save.

Task 1.2: Update the Ubuntu instance security group
In this task, you update the security group to allow ICMP traffic for testing, HTTPS traffic, and UDP traffic from port 1194 for the Client VPN. For more information on viewing and adding rules to security groups, see View your security groups.

In the navigation pane, choose Security Groups, choose Ubuntu SG, and then add the following inbound rules:
Ensure all ICMP - IPv4 from anywhere is allowed.
Ensure all HTTPS traffic from anywhere is allowed.
Ensure UDP traffic from port 1194 from anywhere is allowed.
Choose Save rules.
Task 1.3: Install mutual authentication on the Ubuntu instance
With mutual authentication, Client VPN uses certificates to perform authentication between the client and the server. The server uses client certificates to authenticate clients when they connect to the Client VPN endpoint. You must upload the server certificate to AWS Certificate Manager (ACM), which is done in the following task. When the server certificate is uploaded to ACM, you also specify the certificate authority (CA).

In this task, you generate a server certificate and key, and a client certificate and key.

In the EC2 management console, connect to the Ubuntu VPN instance using SSM, and then run the following commands to update the Ubuntu instance.

sudo su
cd ~
apt update
apt upgrade -y
 Shortened example of expected output


$ sudo su
root@ip-10-0-15-244:/var/snap/amazon-ssm-agent/7983# cd ~
root@ip-10-0-15-244:~# apt update

Get:1 http://us-west-2.ec2.archive.ubuntu.com/ubuntu noble InRelease [256 kB]
Get:2 http://us-west-2.ec2.archive.ubuntu.com/ubuntu noble-updates InRelease [89.7 kB]
Get:3 http://us-west-2.ec2.archive.ubuntu.com/ubuntu noble-backports InRelease [89.7 kB]
Get:4 http://security.ubuntu.com/ubuntu noble-security InRelease [89.7 kB]
...
root@ip-10-0-15-244:~# apt upgrade -y

Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
...
Install the AWS Command Line Interface (AWS CLI) service.

snap install aws-cli --classic
 Expected output


root@ip-10-0-15-244:~# snap install aws-cli --classic
aws-cli (v2/stable) 2.17.11 from Amazon Web Services (aws✓) installed
To clone the OpenVPN easy-rsa repo to the Ubuntu instance, run the following command:

git clone https://github.com/OpenVPN/easy-rsa.git
 Example expected output


root@ip-10-0-15-244:~# git clone https://github.com/OpenVPN/easy-rsa.git
Cloning into 'easy-rsa'...
remote: Enumerating objects: 6663, done.
remote: Counting objects: 100% (1439/1439), done.
remote: Compressing objects: 100% (601/601), done.
remote: Total 6663 (delta 888), reused 1141 (delta 837), pack-reused 5224
Receiving objects: 100% (6663/6663), 52.26 MiB | 24.21 MiB/s, done.
Resolving deltas: 100% (3137/3137), done.
To navigate to the easy-rsa/easyrsa3 folder, run the following command:

cd easy-rsa/easyrsa3
To initialize a new public key infrastructure (PKI) environment, run the following command:

./easyrsa init-pki
 Expected output


Notice
------
'init-pki' complete; you may now create a CA or requests.

Your newly created PKI dir is:
* /root/easy-rsa/easyrsa3/pki

Using Easy-RSA configuration:
* undefined
To build a new certificate authority, run the following command.

./easyrsa build-ca nopass
For the Common Name prompt, enter a name for your certificate.
 Expected output


root@ip-10-0-15-244:~/easy-rsa/easyrsa3# ./easyrsa build-ca nopass
...
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields, but you can leave some blank.
For some fields, there will be a default value.
If you enter '.', the field will be left blank.
-----
Common Name (e.g.: your user, host, or server name) [Easy-RSA CA]:servercert

Notice
------
CA creation complete. Your new CA certificate is at:
* /root/easy-rsa/easyrsa3/pki/ca.crt
Generate the server certificate and key by running the following command, at the prompt, enter Yes.

./easyrsa --san=DNS:server build-server-full server nopass
 Shortened example of expected output


root@ip-10-0-15-244:~/easy-rsa/easyrsa3# ./easyrsa --san=DNS:server build-server-full server nopass

...

Notice
------
Private-Key and Public-Certificate-Request files created.
Your files are:
* req: /root/easy-rsa/easyrsa3/pki/reqs/server.req
* key: /root/easy-rsa/easyrsa3/pki/private/server.key

...

Notice
------
Certificate created at:
* /root/easy-rsa/easyrsa3/pki/issued/server.crt


Notice
------
Inline file created:
* /root/easy-rsa/easyrsa3/pki/inline/server.inline
To generate the client certificate and key, at the prompt, enter Yes.
 Note: The client certificate and the client private key file will be used for future steps.


./easyrsa build-client-full client1.domain.tld nopass
 Shortened example of expected output


Notice
------
Private-Key and Public-Certificate-Request files created.
Your files are:
* req: /root/easy-rsa/easyrsa3/pki/reqs/client1.domain.tld.req
* key: /root/easy-rsa/easyrsa3/pki/private/client1.domain.tld.key

...

Type the word 'yes' to continue, or any other input to abort.
  Confirm request details: yes

...

Notice
------
Certificate created at:
* /root/easy-rsa/easyrsa3/pki/issued/client1.domain.tld.crt


Notice
------
Inline file created:
* /root/easy-rsa/easyrsa3/pki/inline/client1.domain.tld.inline
Use the following commands to copy the server and client certificates and keys to the certs_folder, and then navigate to the certs_folder.

mkdir ~/certs_folder/
cp pki/ca.crt ~/certs_folder/
cp pki/issued/server.crt ~/certs_folder/
cp pki/private/server.key ~/certs_folder/
cp pki/issued/client1.domain.tld.crt ~/certs_folder
cp pki/private/client1.domain.tld.key ~/certs_folder/
cd ~/certs_folder/
Upload the server certificate and keys to AWS Certificate Manager (ACM) using the AWS CLI by running the following command. Replace the AWS_REGION placeholder value with the AwsRegion value that is listed to the left of these instructions.

aws acm import-certificate --certificate fileb://server.crt --private-key fileb://server.key --certificate-chain fileb://ca.crt --region AWS_REGION
 Expected output


root@ip-10-0-15-244:~/certs_folder# aws acm import-certificate --certificate fileb://server.crt --private-key fileb://server.key --certificate-chain fileb://ca.crt --region us-west-2
{
    "CertificateArn": "arn:aws:acm:us-west-2:123456789000:certificate/59fd30e9-d062-4f70-a6dd-000000000000"
}
To upload the client certificates and keys to AWS Certificate Manager (ACM) using the AWS CLI by running the following command. Replace the AWS_REGION placeholder value with the AwsRegion value that is listed to the left of these instructions.

aws acm import-certificate --certificate fileb://client1.domain.tld.crt --private-key fileb://client1.domain.tld.key --certificate-chain fileb://ca.crt --region AWS_REGION
 Expected output


root@ip-10-0-15-244:~/certs_folder# aws acm import-certificate --certificate fileb://client1.domain.tld.crt --private-key fileb://client1.domain.tld.key --certificate-chain fileb://ca.crt --region us-west-2
{
    "CertificateArn": "arn:aws:acm:us-west-2:123456789000:certificate/692b20b4-0a8e-4625-bb88-000000000000"
}
 Task complete: You successfully generated server and client certificates and keys.

Task 2: Create a Client VPN endpoint
The Client VPN endpoint is a resource that you create and configure to manage Client VPN sessions. It is the termination point for all Client VPN sessions.

In this task, you create a Client VPN endpoint using the mutual authentication as an authentication option. The certificates that you generated in the previous steps are used here.

Task 2.1: Create a VPC for the Client VPN endpoint
In this task, you create a VPC with a Linux EC2 instance for the Client VPN endpoint. The Client VPN endpoint is the termination point for all Client VPN sessions (Ubuntu VPC) that are accessing resources in the VPC you create.

In the AWS Management Console, in the search box, search for and choose VPC.

Choose Create VPC.

Choose VPC and more, and then configure the VPC settings as follows:

Name the VPC Resources.
The CIDR block is 192.168.0.0/16.
The VPC needs only one Availability Zone (AZ) and one public subnet.
No endpoints or gateways are needed.
Choose Create VPC.
Task 2.2: Launch a Linux instance
Now, you will launch a Linux EC2 instance in the Resources VPC that you created. This Linux instance will be used to test the connection between the client (Ubuntu instance) and the Linux server.

In the console, navigate to the EC2 Dashboard, and launch an Amazon Linux 2023 AMI instance with the following settings:
For the name, enter Linux server.
For the instance, choose the Amazon Linux 2023 AMI instance.
For Key pair (login), choose VPNLabKey.
For Network settings, choose the VPC Resources-vpc and subnet Resources-vpc-subnet-public1-us-west-2a.
Ensure that Auto-assign public IP is set to Enable.
Choose Create security group and configure the following settings:
Name the security group Resources-vpc SG.
Add ICMP-IPv4 from all traffic.
Allow Custom UDP traffic on Port 1194 from source 192.168.0.0/16.
Remove the default SSH rule.
In the Advanced details section, locate IAM instance profile, and choose UbuntuInstanceProfile.
Choose Launch instance.
Task 2.3: Create a Client VPN endpoint in the Resources-vpc
In this task, you will create the Client VPN endpoint and configure it to enable and manage Client VPN sessions.

In the console, navigate to the VPC Dashboard, and in the navigation pane, locate the Virtual private network (VPN) section, and choose Client VPN endpoints.

Choose Create client VPN endpoint, and configure the settings as follows:

For Name tag - optional, enter CVPN.
For Client IPv4 CIDR, enter 10.0.0.0/22.
In the Authentication information section, configure the settings as follows:
For Server certificate ARN, choose the server certificate that you created with your custom name in Task 1.
For Authentication options, select the Use mutual authentication checkbox.
For Client certificate ARN, choose the client certificate that you created in Task 1. It has the client1.domain.tld parameter.
For DNS server options, leave blank.
In the Other parameters - optional section, configure the settings as follows:
Leave the DNS server options blank.
For Transport protocol, select UDP.
Select Enable split-tunnel.
For VPC ID, choose Resource VPC-vpc.
For Security Group, choose the Resources-vpc SG that you created.
For VPN port, choose 1194.
Choose Create client VPN endpoint.
After you create the Client VPN endpoint, the state displays as pending-associate. To change this state, you must associate at least one target network.

With the Client VPN endpoint selected, copy and paste the Client VPN endpoint ID link into a text editor for a future step. The endpoint ID link is located next to the endpoint’s name column.
Task 2.4: Associate a target network
To move the Client VPN from a pending-associate state to an available state, you must associate a target network with the Client VPN endpoint. A target network is a subnet in a VPC.

In the console, with the Client VPN endpoint selected, choose the Target network associations tab, and then choose Associate target network.

For VPC, choose Resources-vpc.

For Choose a subnet to associate, choose Resources-vpc-subnet-public1.

Choose Associate target network.

 WARNING: The change from pending-associate to available can take up to 10 minutes. You can move on to the next task while the target network is being associated.

Once the subnet is associated with the Client VPN endpoint, the state of the Client VPN endpoint changes to available. Clients can then establish connection, but they cannot access resources in the VPC until you add authorization rules.

Two configurations are automatically completed for you. The Client VPN adds the local route of the VPC to the Client VPN endpoint route table, and the VPC’s default security group is automatically applied for the Client VPN endpoint.

Task 2.5: Add an authorization rule for the VPC
Clients must have a route to the VPC in the Client VPN endpoint’s route table and an authorization rule to access the VPC. The route was added automatically in the previous task.

With the Client VPN selected in the console, choose the Authorization rules tab, and then choose Add authorization rule.

For Destination network to enable access, set the destination as 192.168.0.0/16. This allows access to the entire VPC.

For the Grant access to option, choose Allow access to all users.

Choose Add authorization rule.

Task 2.6: Download the Client VPN endpoint configuration file
The configuration file includes the Client VPN endpoint details and certificate information for the VPN connection. You will provide this file to any end user who must connect to the Client VPN endpoint. The end user is responsible for configuring their VPN client application. In this task, you will download and prepare the Client VPN endpoint configuration file.

With the Client VPN selected in the console, choose Download client configuration.

Open the Client VPN endpoint configuration file using a text editor, and add the following tags at the end of the file:


<cert>

</cert>

<key>

</key>
Now, you will locate the client certificate and key that were generated in Task 1, and paste the contents from the client certificate and key certificate into the corresponding tags in the configuration file.

 Note: If your session timed out, reconnect to the Ubuntu instance.

Use the following path to view your client certificate, copy the content from -----BEGIN CERTIFICATE----- through -----END CERTIFICATE-----, and then paste it between the cert tags in the downloaded configuration file.

sudo su
cd ~
cd easy-rsa/easyrsa3/pki/issued
cat client1.domain.tld.crt
 Expected output


...

-----BEGIN CERTIFICATE-----
THIS CONTENT HAS BEEN REDACTED
-----END CERTIFICATE-----
Use the following path to view your client key, copy the content from -----BEGIN PRIV KEY----- through -----END PRIV KEY-----, and paste it between the key tags in the downloaded configuration file.

cd ..
cd private
cat client1.domain.tld.key
 Expected output


...

-----BEGIN PRIV KEY-----
THIS CONTENT HAS BEEN REDACTED
-----END PRIV KEY-----
 Shortened example of expected output



client
dev tun
proto udp
remote cvpn-endpoint-000000000000000000.prod.clientvpn.us-west-2.amazonaws.com 1194
remote-random-hostname
resolv-retry infinite
nobind
remote-cert-tls server
cipher AES-256-GCM
verb 3

<ca>
-----BEGIN CERTIFICATE-----
THIS CONTENT HAS BEEN REDACTED
-----END CERTIFICATE-----

</ca>

reneg-sec 0

verify-x509-name server name

<cert>
-----BEGIN CERTIFICATE-----
THIS CONTENT HAS BEEN REDACTED
-----END CERTIFICATE-----
</cert>

<key>
-----BEGIN PRIV KEY-----
THIS CONTENT HAS BEEN REDACTED
-----END PRIV KEY-----
</key>
Save the file to your desktop.
 Task complete: You successfully created and configured a Client VPN endpoint.

Task 3: Install OpenVPN and test the connection
So far, you created and configured the Client VPN endpoint and downloaded the configuration file. In this task, you will download the software application that you use to connect to the Client VPN endpoint.

Task 3.1: Export the Client VPN configuration file
In this task, you will export the Client VPN endpoint configuration file.

In the console, navigate to the VPC Dashboard, and in the navigation pane, choose Client VPN endpoint.

Select the Client VPN endpoint that you created, and copy the Client VPN endpoint ID to a text editor.

Navigate to the Ubuntu session manager terminal window.

Navigate to the certs_folder folder, by running the following command:


sudo su
cd ~
cd certs_folder/
To export the configuration file, replace the CLIENT_VPN_ENDPOINT and AWS_REGION placeholder values with the Client VPN endpoint id value you copied to your local text editor in earlier task and AwsRegion value that is listed to the left of these instructions respectively.

aws ec2 export-client-vpn-client-configuration --client-vpn-endpoint-id CLIENT_VPN_ENDPOINT --output text --region AWS_REGION
 Shortened example of expected output


root@ip-10-0-15-244:~/certs_folder# aws ec2 export-client-vpn-client-configuration --client-vpn-endpoint-id cvpn-endpoint-063385602a3155e6d --output text --region us-west-2
client
dev tun
proto udp
remote cvpn-endpoint-063385602a3155e6d.prod.clientvpn.us-west-2.amazonaws.com 1194
remote-random-hostname
resolv-retry infinite
nobind
remote-cert-tls server
cipher AES-256-GCM
verb 3
<ca>
-----BEGIN CERTIFICATE-----
THIS CONTENT HAS BEEN REDACTED
-----END CERTIFICATE-----

</ca>


reneg-sec 0

verify-x509-name server name
Notice how your cert and key tags and contents are missing. This is because you have to create a configuration for yourself to access the Client VPN endpoint.

In the certs_folder path, use vim to create a file called myconfig.ovpn.

Copy and paste your configuration file (which you saved to your desktop previously) into myconfig.ovpn file.

To save your changes, press ESC, and then enter :wq to write to the file and quit.

To confirm that the file was created and contains its content, run cat myconfig.ovpn.

Task 3.2: Install OpenVPN and test the connection
In this task, you install the software OpenVPN on the Ubuntu instance and test the VPN connection

To install Open VPN, run the following command:

apt-get install openvpn -y
Now, you connect and authenticate to the Client VPN endpoint and test the VPN connection.

To establish a connection from the client to the Client VPN endpoint, run the following command:

cd ..
openvpn --config certs_folder/myconfig.ovpn --dev tun
 Expected output


root@ip-10-0-15-244:~# openvpn --config certs_folder/maycvpn.ovpn --dev tun
2024-05-14 18:36:38 Note: Kernel support for ovpn-dco missing, disabling data channel offload.
2024-05-14 18:36:38 OpenVPN 2.6.9 x86_64-pc-linux-gnu [SSL (OpenSSL)] [LZO] [LZ4] [EPOLL] [PKCS11] [MH/PKTINFO] [AEAD] [DCO]
2024-05-14 18:36:38 library versions: OpenSSL 3.0.13 30 Jan 2024, LZO 2.10
2024-05-14 18:36:38 DCO version: N/A
2024-05-14 18:36:38 TCP/UDP: Preserving recently used remote address: [AF_INET]54.214.247.161:1194
2024-05-14 18:36:38 Socket Buffers: R=[212992->212992] S=[212992->212992]
2024-05-14 18:36:38 UDPv4 link local: (not bound)
2024-05-14 18:36:38 UDPv4 link remote: [AF_INET]54.214.247.161:1194
2024-05-14 18:36:38 TLS: Initial packet from [AF_INET]54.214.247.161:1194, sid=00a37f6b 56b4ee62
2024-05-14 18:36:38 VERIFY OK: depth=1, CN=servercert
2024-05-14 18:36:38 VERIFY KU OK
2024-05-14 18:36:38 Validating certificate extended key usage
2024-05-14 18:36:38 ++ Certificate has EKU (str) TLS Web Server Authentication, expects TLS Web Server Authentication
2024-05-14 18:36:38 VERIFY EKU OK
2024-05-14 18:36:38 VERIFY X509NAME OK: CN=server
2024-05-14 18:36:38 VERIFY OK: depth=0, CN=server
2024-05-14 18:36:38 Control Channel: TLSv1.2, cipher TLSv1.2 ECDHE-RSA-AES256-GCM-SHA384, peer certificate: 2048 bits RSA, signature: RSA-SHA256, peer temporary key: 256 bits ECprime256v1
2024-05-14 18:36:38 [server] Peer Connection Initiated with [AF_INET]54.214.247.161:1194
2024-05-14 18:36:38 TLS: move_session: dest=TM_ACTIVE src=TM_INITIAL reinit_src=1
2024-05-14 18:36:38 TLS: tls_multi_process: initial untrusted session promoted to trusted
2024-05-14 18:36:40 SENT CONTROL [server]: 'PUSH_REQUEST' (status=1)
2024-05-14 18:36:40 PUSH: Received control message: 'PUSH_REPLY,route 192.168.0.0 255.255.0.0,route-gateway 10.0.0.161,topology subnet,ping 1,ping-restart 20,echo,echo,ifconfig 10.0.0.162 255.255.255.224,peer-id 0,cipher AES-256-GCM'
2024-05-14 18:36:40 OPTIONS IMPORT: --ifconfig/up options modified
2024-05-14 18:36:40 OPTIONS IMPORT: route options modified
2024-05-14 18:36:40 OPTIONS IMPORT: route-related options modified
2024-05-14 18:36:40 net_route_v4_best_gw query: dst 0.0.0.0
2024-05-14 18:36:40 net_route_v4_best_gw result: via 10.0.0.1 dev enX0
2024-05-14 18:36:40 ROUTE_GATEWAY 10.0.0.1/255.255.240.0 IFACE=enX0 HWADDR=06:61:89:44:1d:63
2024-05-14 18:36:40 TUN/TAP device tun0 opened
2024-05-14 18:36:40 net_iface_mtu_set: mtu 1500 for tun0
2024-05-14 18:36:40 net_iface_up: set tun0 up
2024-05-14 18:36:40 net_addr_v4_add: 10.0.0.162/27 dev tun0
2024-05-14 18:36:40 net_route_v4_add: 192.168.0.0/16 via 10.0.0.161 dev [NULL] table 0 metric -1
2024-05-14 18:36:40 Initialization Sequence Completed
2024-05-14 18:36:40 Data Channel: cipher 'AES-256-GCM', peer-id: 0
2024-05-14 18:36:40 Timers: ping 1, ping-restart 20
^C2024-05-14 18:41:53 event_wait : Interrupted system call (fd=-1,code=4)
2024-05-14 18:41:53 net_route_v4_del: 192.168.0.0/16 via 10.0.0.161 dev [NULL] table 0 metric -1
2024-05-14 18:41:53 Closing TUN/TAP interface
2024-05-14 18:41:53 net_addr_v4_del: 10.0.0.162 dev tun0
In this output, you can see something similar to the following:


2024-05-14 18:36:38 [server] Peer Connection Initiated with [AF_INET]54.214.247.161:1194
This shows that there was a successful connection between the client and the Client VPN endpoint. At this point, the client can send traffic and receive traffic according to the Client VPN endpoint’s configuration.

Duplicate the Ubuntu instance tab so that it shows a blank terminal. You are now replicating a client. Ensure that you can see the $ symbol in the duplicated terminal.

On the Ubuntu instance, ping the private IP of the Linux instance to verify that you can send traffic through this VPN connection. Stop the ping after a few replies have come back.

Navigate to the AWS Management Console and navigate to the Client VPN endpoint page.

Select the Client VPN endpoint that you created, and choose the Connections tab. Here, you can view the number of connections that were made from which Client VPN endpoint, and the time and date.

 Task complete: You successfully installed OpenVPN and tested the connection from a client to the Client VPN endpoint and its resources.

Conclusion
 Congratulations! You successfully completed the following:

Generated server and client certificates and keys.
Created a Client VPN endpoint.
Installed OpenVPN on Ubuntu and tested the connection.

--

### Additional Resources

For more information about Client VPNs, review [What Is AWS Client VPN?](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html).
For more information on how to connect using OpenVPN, review [AWS Client VPN for Linux](https://docs.aws.amazon.com/vpn/latest/clientvpn-user/client-vpn-connect-linux.html).
For more information on getting started with Client VPN, review [Getting started with AWS Client VPN](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-getting-started.html).
For more information on mutual authentication, review [Mutual authentication](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/mutual.html).
For more information on upgrading Ubuntu, review [How do I upgrade Ubuntu on my EC2 Linux instance from one LTS version to another?](https://repost.aws/knowledge-center/ec2-linux-upgrade-ubuntu-lts).

---
