# Deploying Standardized Assets Using AWS Service Catalog

## Lab overview

In this lab, you will create an AWS Service Catalog portfolio that contains four products. Each AWS Service Catalog product is backed by an AWS CloudFormation template, which is supplied as part of the lab. The first product is an Amazon Virtual Private Cloud (Amazon VPC) environment for end user development purposes. The Amazon VPC is the destination for the other products that you will build. The second product is an Amazon Elastic Compute Cloud (Amazon EC2) Linux instance. The third product is an Amazon Relational Database Service (Amazon RDS) MySQL database deployment. Lastly, you will build an Amazon Simple Storage Service (Amazon S3) product that is restricted by an AWS Identity and Access Management (IAM) user and IP address range of your Amazon VPC.

You will also create and assign template and launch constraints for the AWS Service Catalog products that you create. You will set tags for the products and portfolio that you create, and assign IAM users to the newly created portfolio.

The lab includes two pre-assigned IAM users. The first IAM user is admin user. The admin user is assigned the role of an AWS Service Catalog admin (not an AWS admin), and has permission to create portfolios and products in AWS Service Catalog, but no direct access to other services. The second IAM user is developer user. The developer user mimics an end user experience and can only launch AWS Service Catalog products.

In a typical deployment scenario, the admin user is an automation or deployments team, or a business unit AWS admin who does not have control of the entire AWS environment. The developer user is a developer, business owner, or operations team member who is not concerned with the underlying AWS infrastructure and is more of a consumer of the final AWS services.

## Objectives

By the end of this lab, you should be able to do the following:

Create an AWS Service Catalog portfolio.
Create an AWS Service Catalog Amazon VPC product.
Create an AWS Service Catalog Amazon EC2 product.
Create an AWS Service Catalog Amazon RDS product.
Create an AWS Service Catalog Amazon S3 product.
Create AWS Service Catalog launch constraints.
Create AWS Service Catalog template constraints.
Launch a newly created AWS Service Catalog Amazon VPC product.
Launch newly created Amazon EC2, Amazon RDS, and Amazon S3 products in an Amazon VPC product.
Technical knowledge prerequisites
This hands-on lab assumes that you completed the Cloud Operations 1 (CO1) course and the associated labs.

Duration
This lab requires 90 minutes to complete.

Icon key
Various icons are used throughout this lab to call attention to certain aspects of the guide. The following list explains the purpose for each one:

 Caution: Information of special interest or importance (not so important to cause problems with the equipment or data if you miss it, but it could result in the need to repeat certain steps).
 Note: A hint, tip, or important guidance.
 Task complete: A conclusion or summary point in the lab.
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
Amazon EC2
Amazon Elastic Compute Cloud (Amazon EC2) provides on-demand, scalable computing capacity in the AWS Cloud. Using Amazon EC2 reduces hardware costs, so you can develop and deploy applications faster. You can use Amazon EC2 to launch as many or as few virtual servers as you need, configure security and networking, and manage storage. You can add capacity (scale up) to handle compute-heavy tasks, such as monthly or yearly processes, or spikes in website traffic. When usage decreases, you can reduce capacity (scale down) again.

Amazon RDS
Amazon Relational Database Service (Amazon RDS) is a web service that makes it easier to set up, operate, and scale a relational database in the AWS Cloud. It provides cost-efficient, resizable capacity for an industry-standard relational database and manages common database administration tasks.

Amazon S3
Amazon Simple Storage Service (Amazon S3) is an object storage service that offers industry-leading scalability, data availability, security, and performance. Customers of all sizes and industries can use Amazon S3 to store and protect any amount of data for a range of use cases, such as data lakes, websites, mobile applications, backup and restore, archives, enterprise applications, Internet of Things (IoT) devices, and big data analytics. Amazon S3 provides management features so that you can optimize, organize, and configure access to your data to meet your specific business, organizational, and compliance requirements.

AWS Service Catalog
AWS Service Catalog enables organizations to create and manage catalogs of IT services that are approved for AWS. These IT services can include everything from virtual machine images, servers, software, databases, and more to complete multi-tier application architectures. AWS Service Catalog allows organizations to centrally manage commonly deployed IT services, and helps organizations achieve consistent governance and meet compliance requirements. End users can quickly deploy only the approved IT services they need, following the constraints set by their organization.

Task 1: Create your portfolio
In this task, you will use the admin user credentials to create a new AWS Service Catalog portfolio. AWS Service Catalog portfolios contain products created by an AWS Service Catalog administrator. The portfolios provide a way to allow specific end users access to products with certain constraints determined by the admin. The admin user will only have access to create portfolios and products in the AWS Service Catalog, and they will have read-only access to AWS.

To log in as admin, you must log out as a normal lab user, and then log in using a special URL.

To sign out of the AWS Management Console, complete the following steps:
In the top-right of the window, choose the displayed user or role.
Choose Sign out.
Close the browser tab.
To the left of these lab instructions, copy the value of LoginURL.
This is the IAM user sign-in link that points to the AWS account used in this lab.

Open a new web browser tab, paste the LoginURL, and then press Enter.
 Caution: If you receive an error that states does not support access for federated users, choose Logout here, and try again.

On the AWS sign-in page, configure the following:
For Account ID, if the input field is empty, paste the value of AWSAccountID located to the left of these instructions.
For IAM user name, enter user-admin.
For Password, paste the value of AdministratorPassword located to the left of these instructions.
Choose Sign in.

At the top of the AWS Management Console, in the unified search bar, search for and choose Service Catalog.

The AWS Service Catalog web console opens.

 Caution: Make sure that the Region listed in the console matches the LabRegion listed to the left of these instructions.

In the left navigation pane, under Administration, choose Portfolios.

 Note: If the navigation pane is collapsed, choose the menu  icon.

Choose Create portfolio.

On the Create portfolio screen, configure the following:

For Portfolio name, enter My Portfolio.
For Owner, enter Lab.
Choose Create.
The portfolio is created. The page displays a list of account portfolios and a banner message with the text  Success You successfully created portfolio My Portfolio.

Choose the My Portfolio link.
This displays the details of your portfolio.

Choose the Access (0) tab.
Here, you can grant users access to the portfolio and allow them to launch the associated resources.

Choose Grant access.

Choose the Users tab, and configure the following:

Select  user-admin.
Select  user-developer.
Choose Grant access.
A banner message displays the text  Success You added access for user(s): user-admin and user-developer.

Choose the Tags (0) tab.
Here, you can create portfolio tags, which help identify information regarding the portfolio that users can access and use programmatically.

On Add tags specific to this portfolio, configure the following:
Tag 1:

For Key, enter Portfolio.
For Value, enter My Portfolio.
Choose Add tag.
A banner message displays the text Success Portfolio was updated.

Tag 2:

For Key, enter Provider.
For Value, enter Infrastructure Team.
Choose Add tag.
A banner message displays the text Success Portfolio was updated.

Choose the TagOptions (0) tab.
Choose TagOptions library.
The TagOptions Library is an AWS Service Catalog feature that allows administrators to define and manage a centralized library of tag options that can be used to tag resources in Service Catalog. This is where you create tags that can be associated with products being launched. You will use these tags later by applying them to your products.

On the TagOptions library page, under Create new TagOption, configure the following tags:
Tag 1:

For Key, enter CostCenter.
For Value, enter Operations.
Choose Add.
A banner message displays the text Success Key value pair CostCenter: Operations has been added to your TagOptions library.

Tag 2:

For Key, enter CostCenter.
For Value, enter Development.
Choose Add.
A banner message displays the text Success Key value pair CostCenter: Development has been added to your TagOptions library.

Two tags are now in the TagOptions section of the page.

In the left navigation pane, under Administration, choose Portfolios.

Choose the My Portfolio link.

Choose the TagOptions (0) tab, and configure the following:

Select  Key: CostCenter, Value: Development.
Select  Key: CostCenter, Value: Operations.
Choose Actions , and then choose Associate TagOption.

In the Associate TagOptions window, choose Ok.

A banner message displays the text Success You have associated 2 TagOptions: CostCenter: Operations and CostCenter: Development.

 Task complete: You successfully created a portfolio, associated users with the portfolio, and added tagging for both the portfolio and products.

Task 2: Create your products
AWS Service Catalog products are a powerful way of grouping services into a full solution for your end users, so they do not need access to the AWS Management Console. AWS Service Catalog products are based on AWS CloudFormation templates. Products can be a single service or a combination of services. In this task, you will create AWS Service Catalog products to associate with your portfolio.

Task 2.1: Create an Amazon VPC product
The first product that you will create is an Amazon VPC, which will be the foundational network that you associate with your Amazon EC2 and Amazon RDS products.

Open the context (right-click) menu for VPC.template, and download it to your computer by choosing the Save Link As… option.

On the My Portfolio page, choose the Products (0) tab.

Choose Create product.

On the Create product page, under Product details, configure the following:

For Product type, select  CloudFormation.
For Product name, enter VPC.
For Product description, enter Development VPC Product.
For Owner, enter Lab.
Under Version details, configure the following:
For Version source, select  Use a template file.
For Upload a CloudFormation template file, choose  Choose file and browse to the VPC.template file that you downloaded earlier.
For Version name, enter 1.
Under Support details, configure the following:
For Email contact, enter support@example.com.
Choose Create product.
A banner message displays the text  Success Successfully added prod-xxxxxx to portfolio.

 Note: You can choose the refresh  button to confirm that the product was successfully added to your portfolio.

Task 2.2: Create a Linux EC2 product
The second product that you will create is a Linux EC2 instance that allows your end user to choose a destination subnet and security group upon provisioning. The CloudFormation template this product is based on also ensures which specific Amazon Machine Image (AMI) to use.

Open the context (right-click) menu for LINUX.template, and download it to your computer by choosing the Save Link As… option.

On the My Portfolio page, choose the Products (1) tab.

Choose Create product.

On the Create product page, under Product details, configure the following:

For Product type, select  CloudFormation.
For Product name, enter EC2.
For Product description, enter Linux Instance Product.
For Owner, enter Lab.
Under Version details, configure the following:
For Version source, select  Use a template file.
For Upload a CloudFormation template file, choose  Choose file and browse to the LINUX.template file that you downloaded earlier.
For Version name, enter 1.
Under Support details, configure the following:
For Email contact, enter support@example.com.
Choose Create product.
A banner message displays the text  Success Successfully added prod-xxxxxx to portfolio.

 Note: You can choose the refresh  button to confirm that the product was successfully added to your portfolio.

Task 2.3: Create an Amazon RDS node product
The third product that you will create is an Amazon RDS MySQL database instance. The product allows your developer users to choose a DB Security Group and MySQL password upon provisioning.

Open the context (right-click) menu for RDS.template, and download it to your computer by choosing the Save Link As… option.

On the My Portfolio page, choose the Products (2) tab.

Choose Create product.

On the Create product page, under Product details, configure the following:

For Product type, select  CloudFormation.
For Product name, enter RDS Node.
For Product description, enter RDS Node Product.
For Owner, enter Lab.
Under Version details, configure the following:
For Version source, select  Use a template file.
For Upload a CloudFormation template file, choose  Choose file and browse to the RDS.template file that you downloaded earlier.
For Version name, enter 1.
Under Support details, configure the following:
For Email contact, enter support@example.com.
Choose Create product.
A banner message displays the text  Success Successfully added prod-xxxxxx to portfolio.

 Note: You can choose the refresh  button to confirm that the product was successfully added to your portfolio.

Task 2.4: Create an Amazon S3 product
The fourth product that you will create is an S3 bucket that will allow access to a specific IAM user and IP range.

Open the context (right-click) menu for S3.template, and download it to your computer by choosing the Save Link As… option.

On the My Portfolio page, choose the Products (3) tab.

Choose Create product.

On the Create product page, under Product details, configure the following:

For Product type, select  CloudFormation.
For Product name, enter S3.
For Product description, enter Product that creates a S3 Bucket.
For Owner, enter Lab.
Under Version details, configure the following:
For Version source, select  Use a template file.
For Upload a CloudFormation template file, choose  Choose file and browse to the S3.template file that you downloaded earlier.
For Version name, enter 1.
Under Support details, configure the following:
For Email contact, enter support@example.com.
Choose Create product.
A banner message displays the text  Success Successfully added prod-xxxxxx to portfolio.

 Note: You can choose the refresh  button to confirm that the product was successfully added to your portfolio.

 Task complete: You successfully created Amazon VPC, Amazon S3, Amazon EC2, and Amazon RDS products for your end users to use.

Task 3: Create launch constraints for your products
In this task, you will create launch constraints for your products. You need to assign an IAM role to each AWS Service Catalog product that allows AWS Service Catalog to create the products and their underlying services (Amazon VPC, Amazon S3, Amazon EC2, and Amazon RDS) on behalf of the end user. These are referred to as launch constraints.

For the launch constraints, you will use four IAM roles that were built specifically for this lab: SC-VPC-ROLE, SC-EC2-ROLE, SC-RDS-ROLE, and SC-S3-ROLE. These IAM roles have their trusted entity set to the AWS Service Catalog service, which allows AWS Service Catalog to launch AWS services. This mechanism is used instead of granting direct access to AWS services to the end user (developer, in this lab), but still gives the end user the ability to launch the services in a defined, governed, and pre-approved way.

Task 3.1: Add a launch constraint for your Amazon VPC product
In the left navigation pane, under Administration, choose Portfolios.

Choose the My Portfolio link.

Choose the Constraints (0) tab.

Choose Create constraint.

On the Create constraint page, under Create constraint, configure the following:

For Product, choose VPC.
For Constraint type, select  Launch.
Under Launch constraint, configure the following:
For Method, select  Select IAM role.
For IAM role, choose SC-VPC-ROLE.
Choose Create.
A banner message displays the text  Success Successfully created constraint.

Task 3.2: Add a launch constraint for your Amazon EC2 product
Choose Create constraint.

On the Create constraint page, under Create constraint, configure the following:

For Product, choose EC2.
For Constraint type, select  Launch.
Under Launch constraint, configure the following:
For Method, select  Select IAM role.
For IAM role, choose SC-EC2-ROLE.
Choose Create.
A banner message displays the text  Success Successfully created constraint.

Task 3.3: Add a launch constraint for your Amazon RDS product
Choose Create constraint

On the Create constraint page, under Create constraint, configure the following:

For Product, choose RDS Node.
For Constraint type, select  Launch.
Under Launch constraint, configure the following:
For Method, select  Select IAM role.
For IAM role, choose SC-RDS-ROLE.
Choose Create.
A banner message displays the text  Success Successfully created constraint.

Task 3.4: Add a launch constraint for your Amazon S3 product
Choose Create constraint.

On the Create constraint page, under Create constraint, configure the following:

For Product, choose S3.
For Constraint type, select  Launch.
Under Launch constraint, configure the following:
For Method, select  Select IAM role.
For IAM role, choose SC-S3-ROLE.
Choose Create.
A banner message displays the text  Success Successfully created constraint.

 Task complete: You successfully created launch constraints so your end users can launch the products you created with IAM roles, without needing access to the services in the AWS Management Console.

Task 4: Launch your Amazon VPC product
In this task, you will launch the development Amazon VPC product. This will create an Amazon VPC that has a public and private subnet with an associated internet gateway. This is a useful example of allowing your end consumers of products in your portfolio to dynamically create an Amazon VPC without allowing them access to make changes through the console.

You will do this as the developer user, so you must sign out of the console, and then sign in as developer.

To sign out of the AWS Management Console, complete the following steps:
In the top-right of the window, choose the username user-admin @.
Choose Sign out.
Close the browser tab.
To the left of these instructions, copy the value of LoginURL.

Open a new web browser tab, paste the LoginURL, and then press Enter.

On the AWS sign-in page, complete the following steps:

For Account ID, if the input field is empty, paste the value of AWSAccountID located to the left of these instructions.
For IAM user name, enter user-developer.
For Password, paste the value of AdministratorPassword located to the left of these instructions.
Choose Sign in.

At the top of the AWS Management Console, in the unified search bar, search for and choose Service Catalog.

You are now signed in as the developer user and directed to the AWS Service Catalog web console.

 Caution: Make sure that the Region listed in the console matches the LabRegion listed to the left of these instructions.

In the left navigation pane, under Provisioning, choose Products.

In Products list, select  VPC, and choose Launch product.

For Provisioned product name, enter myVPC.

Under Parameters, configure the following according to the LabRegion listed to the left of these instructions.

If the LabRegion is us-west-2:

For RegionAZ1Name, select us-west-2a.
For RegionAZ2Name, select us-west-2b.
If the LabRegion is us-east-1:

For RegionAZ1Name, select us-east-1a.
For RegionAZ2Name, select us-east-1b.
Accept the default settings for VPC Configuration, Public Subnet Configuration, and Private Subnet Configuration.

Under Manage tags, configure the following:
Verify that Key is set to CostCenter.
Choose the Value search field, and choose Development.
Choose Launch product.

Wait until the status of your VPC product changes from Under Change to Available. You can choose the refresh  button to view the latest status.

A banner message displays the text  Success Successfully launched myVPC. You can now view the events and outputs associated with this product below.

Under Provisioned product details, scroll and choose the Outputs tab.

Copy the Key and Value of the following items into a text editor. You will use these values in later tasks.

DevLinuxSecurityGroup
DevRDSSecurityGroup
Subnet1Public
 Task complete: You successfully launched a development VPC environment as an end user.

Task 5: Launch your Amazon EC2 product
In this task, you will launch the development Amazon EC2 product. This will create a Linux EC2 instance that will have a specific security group and subnet. This is a useful example of allowing your end consumers of products in your portfolio to dynamically create an EC2 instance without allowing the users access to make changes through the AWS Management Console.

In the left navigation pane, under Provisioning, choose Products.

In the Products list, select  EC2, and choose Launch product.

For Provisioned product name, enter myEC2.

Under Parameters, configure the following:

Verify that AWSAmiId is set to its default value, /aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-x86_64.
Verify that ApplicationName is set to LinuxInstance.
Verify that InstanceType is selected as t2.small.
For SecurityGroup, select the value of DevLinuxSecurityGroup that you noted earlier. It should appear in the list as DevLinux-SG.
For Subnet, select the value of Subnet1Public that you noted earlier. It should appear in the list as Dev Pub Sub 1.
Under Manage tags, configure the following:
Verify that Key is set to CostCenter.
Choose the Value search field, and choose Development.
Choose Launch product.

Wait until the status of your Amazon EC2 product changes from Under Change to Available. You can choose the refresh  button to view the latest status.

A banner message displays the text  Success Successfully launched myEC2. You can now view the events and outputs associated with this product below.

 Task complete: You successfully launched an Amazon EC2 Linux instance into your development Amazon VPC environment.

Task 6: Launch your Amazon RDS product
In this task, you will launch the development Amazon RDS product. This will create an RDS node that will have a specific security group and subnet group. This is a useful example of allowing your end consumers of products in your portfolio to dynamically create an RDS node without allowing them access to make changes through the console.

In the left navigation pane, under Provisioning, choose Products.

In the Products list, select  RDS Node, and choose Launch product.

For Provisioned product name, enter myRDS.

Under Parameters, configure the following:

Verify ApplicationName is set to RDS.
For DBSecurityGroup, select the value of DevRDSSecurityGroup that you noted earlier. It should appear in the list as DevRDS-SG.
For DBSubnetGroupName, choose devdbsubnet.
For MySQLPassword, paste the value of AdministratorPassword located to the left of these instructions.
Under Manage tags, configure the following:
Verify that Key is set to CostCenter.
Choose the Value search field, and choose Development.
Choose Launch product.

Wait until the status of your Amazon RDS product changes from Under Change to Available. You can choose the refresh  button to view the latest status, and it may take up to 10 minutes for the RDS product to change its status to Available.

A banner message displays the text  Success Successfully launched myRDS. You can now view the events and outputs associated with this product below.

 Task complete: You successfully launched an RDS node into your development Amazon VPC environment.

Task 7: Launch your Amazon S3 product
In this task, you will launch the development Amazon S3 product. This will create an S3 bucket that will give specific access to your developer user’s Amazon Resource Name (ARN) and to a specific IP range. This is a useful example of allowing your end consumers of products in your portfolio to dynamically create an S3 bucket without allowing them access to make changes through the console.

Return to the AWS Service Catalog Management Console.

In the left navigation pane, under Provisioning, choose Products.

In the Products list, select  S3, and choose Launch product.

For Provisioned product name, enter myS3.
Under Parameters, configure the following:
For S3UserARN, paste the value of DeveloperUserARN located to the left of the instructions.
For S3AccessCIDR, enter 10.3.0.0/16.
Under Manage tags, configure the following:
Verify that Key is set to CostCenter.
Choose the Value search field, and choose Development.
Choose Launch product.

Wait until the status of your Amazon S3 product changes from Under Change to Available. You can choose the refresh  button to view the latest status.

A banner message displays the text  Success Successfully launched myS3. You can now view the events and outputs associated with this product below.

 Task complete: You successfully launched the Amazon S3 product, which creates a bucket that only has access from your end user and to a specific IP range.

Task 8: Add template constraints
In this task, you will add template constraints. Template constraints help make AWS Service Catalog flexible in applying guardrails for end users. Limiting user access allows for higher security and fewer mistakes. A template constraint can be applied to any CloudFormation template input parameter, limiting its input values to either one value or a list of values.

In this example, you will limit the security group and subnet that can be selected for the Linux EC2 instance created earlier in this lab. You might have noticed that the end user can select any security group and subnet in the VPC. Once you configure the constraint, the developer user will not be able to select any security groups or subnets in the VPC, and they will be forced to select the single security group and subnet that you assigned in the template constraints.

To perform this update, log in as the admin user.

To sign out of the AWS Management Console, complete the following steps:
In the top-right of the window, choose the username user-developer @.
Choose Sign out.
Close the browser tab.
To the left of these instructions, copy the value of LoginURL.

Open a new web browser tab, paste the LoginURL, and then press Enter.

On the AWS sign-in page, enter the following:

For IAM user name, enter user-admin.
For Password, paste the value of AdministratorPassword located to the left of the instructions.
Choose Sign in.
At the top of the AWS Management Console, in the unified search bar, search for and choose Service Catalog.
You are now signed in as the admin user and directed to the AWS Service Catalog web console.

 Caution: Make sure that the Region listed in the console matches the LabRegion listed to the left of these instructions.

In the left navigation pane, under Administration, choose Portfolios.
 Note: If the left navigation pane is not visible, choose the menu icon  in the top-left corner to reveal it.

Choose the My Portfolio link.

Choose the Constraints (4) tab.

Choose Create constraint.

On the Create constraint page, under Create constraint, configure the following:

For Product, choose EC2.
For Constraint type, select  Template.
Under the Template constraint section, configure the following:
For Method, select  Interactive editor.

For Rule name, enter Linux-Security-Group-Constraint.

For Rule description, enter Restricts by Security Group.

For Product version, select 1.

For Parameter, select  Security Group.

For Parameter value, select the checkbox  next to the security group ID that is the value of DevLinuxSecurityGroup that you copied earlier.

 Note: You can also paste the value of DevLinuxSecurityGroup into the search input field.

Choose Add rule.

Choose Add additional rule and configure the following:

For Rule name, enter Linux-Subnet-Constraint.

For Rule description, enter Restricts to Public Subnet.

For Product version, select 1.

For Parameter, select  Subnet.

For Parameter value, select the checkbox  next to the subnet ID that is the value of Subnet1Public that you copied earlier.

 Note: You can also paste the value of Subnet1Public into the search input field.

Choose Add rule.

Choose Create.

A banner message displays the text  Success Successfully created constraint.

 Task complete: You successfully created template constraints to ensure that your end users do not launch an EC2 instance in any other environment except the development Amazon VPC environment with specific subnets and security groups.

Task 9: Test your template constraints
In this task, you will verify that the template constraints you created in the previous task are working, and that the end user (developer user) is constrained to the specific security group you added in the template constraint.

For this task, you must sign out of the console, and then sign in as the developer user.

To sign out of the AWS Management Console, complete the following steps:
In the top-right of the window, choose user-admin @.
Choose Sign out.
Close the browser tab.
To the left of these instructions, copy the value of LoginURL.

Paste the LoginURL into a new browser tab.

On the AWS sign-in page, configure the following:

For Account ID, if the input field is empty, paste the value of AWSAccountID located to the left of these instructions.
For IAM user name, enter user-developer.
For Password, paste the value of AdministratorPassword located to the left of these instructions.
Choose Sign in.

At the top of the AWS Management Console, in the unified search bar, search for and choose Service Catalog.

You are now signed in as the developer user and directed to the AWS Service Catalog web console.

 Caution: Make sure that the Region listed in the console matches the LabRegion listed to the left of these instructions.

In the left navigation pane, under Provisioning, choose Products.

In the Products list, select  EC2, and choose Launch product.

For Provisioned product name, enter MyEC2-2.

Under the Parameters section, configure the following:

Verify that AWSAmiId is set to its default value, /aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-x86_64.
Verify that ApplicationName is set to LinuxInstance.
Verify that InstanceType is selected as t2.small.
For SecurityGroup, notice that the value is preselected to the one that was set in the template constraint in the preceding task.
For Subnet, notice that the value is preselected to the one that was set in the template constraint in the preceding task.
Under Manage tags, configure the following:
Verify that Key is set to CostCenter.
Choose the Value search field, and choose Development.
Choose Launch product.

Wait until the status of your Amazon EC2 product changes from Under Change to Available. You can choose the refresh  button to view the latest status.

A banner message displays the text  Success Successfully launched MyEC2-2. You can now view the events and outputs associated with this product below.

 Task complete: You successfully verified that the end user (developer user) is constrained to the specific security group and subnet added in the template constraints.

Conclusion
You successfully completed the following:

Created an AWS Service Catalog portfolio.
Created an AWS Service Catalog Amazon VPC product.
Created an AWS Service Catalog Amazon EC2 product.
Created an AWS Service Catalog Amazon RDS product.
Created an AWS Service Catalog Amazon S3 product.
Created AWS Service Catalog launch constraints.
Created AWS Service Catalog template constraints.
Launched a newly created AWS Service Catalog Amazon VPC product.
Launched newly created Amazon EC2, Amazon RDS, and Amazon S3 products in an Amazon VPC product.
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End Lab and then confirm that you want to end your lab.

Additional resources
AWS Service Catalog Documentation.
AWS Service Catalog resources.
