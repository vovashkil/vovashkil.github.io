# Creating an HTML Webpage

## Lab overview

In this lab, you create a basic HTML webpage that includes a variety of HTML elements. You also learn how to host the page on a web server so that it is accessible from the internet.

Objectives
By the end of this lab, you will be able to do the following:

Verify that a web server is already installed on an AWS Cloud9 instance and is running.
Troubleshoot networking configurations to permit access to the web server from the internet.
Use the AWS Cloud9 integrated development environment (IDE) file editor to create a basic HTML page that uses heading and paragraph elements.
Include hyperlinks and embedded images in an HTML page.
Apply non-Cascading Style Sheets (CSS) styling to text in a webpage.
Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Analysis: A detailed examination of a topic or concept to promote understanding.
 Caution: Information of special interest or importance (not important enough to cause problems with equipment or data if you miss it, but it could result in the need to repeat certain steps).
 Consider: A moment to pause to consider how you might apply a concept in your own environment or to initiate a conversation about the topic at hand.
 Hint: A hint to a question or challenge.
 Learn more: Where to find more information.
 Note: Additional information or elaboration on a point.
 Task complete: A conclusion or summary point in the lab
 Tip: A shortcut or recommended best practice.
 Warning: An action that is irreversible and could potentially impact the failure of a command or process (including warnings about configurations that cannot be changed after they are made).
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
Lab environment
The following diagram depicts the basic architecture of the lab environment. The resources depicted in the diagram already exist in your Amazon Web Services (AWS) account when you start the lab.

AWS Architecture diagram showing the initial state of the lab environment

Image description: The diagram illustrates a website developer working in an AWS Cloud environment using an AWS Cloud9 IDE hosted on an Amazon Elastic Compute Cloud (Amazon EC2) instance. The instance is set up in a security-controlled public subnet of a virtual private cloud (VPC) and is accessible over the internet. The hosted website is available to consumers through the Apache HTTP Server running on the EC2 instance. For more information, refer to the following detailed diagram overview.

To review the detailed diagram overview, expand this section.
Following is a description of the components and how they’re connected:

AWS Cloud: The overall environment is encapsulated in the AWS Cloud, which is the broader context where all the components reside.

Lab VPC: In the AWS Cloud, there is a virtual private cloud (VPC) designated as Lab VPC. This is like a virtual network in the AWS environment that is isolated from other virtual networks.

Public subnet: Inside the Lab VPC, there’s a public subnet. This subnet is accessible from the internet. A subnet is a range of IP addresses in the VPC.

Security group: In the public subnet, there’s a security group. It acts as a virtual firewall controlling the traffic to the Amazon Elastic Compute Cloud (Amazon EC2) instance.

Amazon EC2 instance: Inside the security group, there’s an EC2 instance. This is a virtual server in AWS where applications can run. The EC2 instance is depicted the EC2 instance group icon. Inside this instance, two key components are mentioned as follows:

AWS Cloud9 IDE: This is an IDE provided by AWS. In this diagram, it’s part of the EC2 instance. This indicates that the AWS Cloud9 IDE is being used for development directly in the EC2 instance.
Apache HTTP Server on Ubuntu guest operating system: This indicates that the EC2 instance is running the Ubuntu operating system and has an Apache HTTP Server installed on it. The Apache server is a software that handles HTTP requests and serves webpages.
Internet gateway: There’s an internet gateway connected to the public subnet, which makes communication possible between the EC2 instance and the internet.

You (website developer): On the left side of the diagram, there’s an icon of a person with the label You (website developer). This symbolizes the developer who interacts with the AWS Cloud and, specifically, the EC2 instance, perhaps using the AWS Cloud9 IDE for developing a website.

Website consumers: On the right side of the diagram, there’s an icon of three people with the label Website consumers. This represents end users or visitors who access the website hosted on the EC2 instance through the internet.

AWS services used in this lab
The services used in this lab are as follows:

AWS Cloud9
Amazon Elastic Compute Cloud (Amazon EC2)
AWS services not used in this lab
AWS service capabilities used in this lab are limited to what the lab requires. Expect errors when accessing other services or performing actions beyond those provided in this lab.

Task 1: Configure the development environment
In this task, you configure the AWS Cloud9 development environment for the lab.

Task 1.1: Connect to the AWS Cloud9 IDE
Connect to the development environment.

Copy the Cloud9Environment URL value that is listed to the left of these instructions, and paste it into a new web browser tab.

A new browser tab opens and displays the AWS Cloud9 IDE.

Task 1.2: Verify the web server is running
Run commands to verify that the web server is running.

 Note: Your AWS Cloud9 IDE runs on an Ubuntu Linux EC2 instance. It comes with an Apache HTTP Server already installed.

To verify the web server is running, in the AWS Cloud9 terminal, run the following command:


sudo systemctl status apache2
The response should indicate that the service is active and running.

Observe the web server document root directory and contents.

To discover the default web server DocumentRoot location, run the following command:


cat /etc/apache2/sites-available/000-default.conf
In the web server’s configuration file, webpages are served to users from the default directory /var/www/html.

To list the contents of the default directory, run the following command:


ls /var/www/html
Observe that a file called index.html already exists. Next, you try loading this page in a browser.

Task 1.3: Load the webpage
Make adjustments as needed, and then confirm that you can load the webpage.

To try loading the webpage in a new browser tab, do the following:

To retrieve the IPv4 public IP address of the instance AWS Cloud9 is running on, run this command:


curl 169.254.169.254/latest/meta-data/public-ipv4
Copy the IP address from the command line output into your clipboard to use later.

Enter http://public-ip in a new web browser tab and replace the public-ip placeholder value with the public IP address value in your clipboard.

Note: The page does not load.

Correct the issue.

 Hint: It is a networking issue. Try to figure out how to fix it.

If you need help, to review the solution, expand this section.
To test access to the index.html page, refresh the http://public-ip page.

This time it can be reached. The Ubuntu Apache2 Default Page opens.

 Tip: If you encounter an issue loading the page, verify that you entered http://public-ip and replaced the public-ip placeholder value with the public IP address value you copied to your clipboard earlier in this task.

 Note: Whether you enter http://public-ip or http://public-ip/index.html, and replace the public-ip placeholder value, the web server loads the same page. In fact, if you rename index.html to index.htm, it will still load the same webpage. In the default configuration, web servers will load an index.htm or index.html file if it exists in the document root location of the web server.

You can also enter http://public-DNS where public-DNS is the Public IPv4 DNS value assigned to the instance. You can find this value in the EC2 console, when the instances selected, in the Details tab. This URL will still display the webpage. The option works because AWS creates a DNS record for your EC2 instance at this location.

Move the existing index.html file to a backup location, then try refreshing the site. To do this:

Return to the AWS Cloud9 Bash terminal, and run the following command:


sudo mv /var/www/html/index.html /var/tmp/
Refresh the webpage in the browser.

Notice that a page similar to the following example opens. There are currently no files in the DocumentRoot location.

no page found

 Note: Leave this browser tab open to use later in the lab.

Task 1.4: Configure the AWS Cloud9 IDE environment window to show the web server document root
Create a symlink so that you can access the files you will be working with through the AWS Cloud9 environment window, which is the panel on the left that displays directories and files.

Notice that in the AWS Cloud9 file browser, there is only the contents of the /home/ubuntu/environment directory.

before symlink of www directory

In the AWS Cloud9 Bash terminal, run the following commands:


ln -s /var/www/ /home/ubuntu/environment/www
sudo chown -R ubuntu /var/www/
 Analysis: The first command created a symlink to the /var/www directory in your environment directory. The second command changed ownership of the files in the /var/www directory so the ubuntu user (which is you) can edit the files in this www directory. If you want, you can verify the user by running whoami.

In the file browser, expand the www directory.

symlinked

 Task complete: In this task, you successfully configured the AWS Cloud9 development environment for the lab.

Task 2: Create a basic webpage
In this task, you create a basic webpage that displays a single line of text.

Create a new file named index.html and save it to the html subdirectory.

In the AWS Cloud9 file editor, add HTML code to the index.html file to create a basic webpage. Include the following:

A DOCTYPE declaration indicating that your file is of type HTML
Start and end tags for the following elements: html, head, and body
A title element in the head section with AnyCompany bicycle parts as the content
A heading 1 element in the body section that displays the message AnyCompany bicycle parts
Try to accomplish these requirements without assistance or by consulting references in this course or online.

To review the solution if needed, expand this section.

<!DOCTYPE html>
<html>
    <head>
        <title>AnyCompany bicycle parts</title>
    </head>
    <body>
        <h1>AnyCompany bicycle parts</h1>
    </body>
</html>
Save the changes.

Refresh the http://public-ip page.

Notice that the new webpage opens.

basic website with h1

 Task complete: In this task, you successfully created a basic webpage that displays a single line of text.

Task 3: Add additional elements to the webpage
In this task, you add formatted text to the webpage, so the page starts to provide valuable information to users.

Task 3.1: Add a comment
Author a comment in the HTML page.

To add a comment to the page source, do the following:
Under heading 1, enter an HTML comment stating product list will go here.

Save the changes.

To test the changes, refresh the webpage.

The text in the comment should not display to the end user.

To review the solution if needed, expand this section.

<h1>AnyCompany bicycle parts</h1>
<!--product list will go here-->
Task 3.2: Add heading and paragraph elements
Add additional HTML elements to the webpage.

Under the comment, add a heading 2 element that displays the text Products.

Under the Products heading, add a paragraph element that includes the following text:


We offer a variety of bicycle parts for sale. Come into our store to browse our selection.
Under the Products section, add another heading 2 element that displays the text Services.

Add paragraph elements under the Services heading. Use multiple paragraph tags to create separation between the sections, and include the following text:


Do you need help installing your bicycle replacement parts, or does your bike need adjustment? We can help with that. Call one of our store locations to schedule an appointment and get a service quote.
  
Our experienced service technicians have passed a rigorous certification program with industry-wide recognition.
  
We offer a wide variety of services, including parts installation, bicycle tune-ups, flat tire repair, derailleur adjustments, and brake caliper adjustments.
  
We specialize in custom bike builds to meet your specific needs. Tell us which types of conditions you plan to do most of your riding in, and our service technicians can recommend the types of frames, tires, and groupsets that are most suitable for those environments.
 Tip: To display all the text, in the AWS Cloud9 IDE, choose View > Wrap Lines. The line numbers in the file editor make it clear which lines are wrapped and which lines are new.

To bold specific words in one of the paragraphs you just added, use the bold element start and end tags. Apply bold formatting to the following text which is already in the page:


We offer a wide variety of services, including
Save the changes.

Refresh the http://public-ip page.

The page should display as follows.

 Note: The text lines will wrap differently depending on the width of your browser window.

look of the page currently

To review the solution, expand this section.

<!DOCTYPE html>
<html>
    <head>
        <title>AnyCompany bicycle parts</title>
    </head>
    <body>
        <h1>AnyCompany bicycle parts</h1>
        <!--product list will go here-->
        <h2>Products</h2>
        <p>We offer a variety of bicycle parts for sale. Come into our store to browse our selection.</p>
        
        <h2>Services</h2>
        <p>Do you need help installing your bicycle replacement parts, or does your bike need adjustment? We can help with that. Call one of our store locations to schedule an appointment and get a service quote.</p>
        <p>Our experienced service technicians have passed a rigorous certification program with industry-wide recognition.</p>
        <p><b>We offer a wide variety of services, including</b> parts installation, bicycle tune-ups, flat tire repair, derailleur adjustments, and brake caliper adjustments.</p>
        <p>We specialize in custom bike builds to meet your specific needs. Tell us which types of conditions you plan to do most of your riding in, and our service technicians can recommend the types of frames, tires, and groupsets that are most suitable for those environments.</p>
    </body>
</html>
To display store location information, add another section to the bottom of the body section that uses a heading 2 element, paragraph tags, and bold tags.

Your challenge is to make the page display as follows. page with store location section

If you need to review the solution code which must be added, expand this section.

<h2>Store location</h2>
<p><b>Address:</b> 100 Anywhere Street, Anytown, USA</p>
<p><b>Phone:</b> 555-0100</p>
<p><b>Hours:</b> Mon-Fri 7 a.m.-7 p.m., Sat 8 a.m.-6 p.m., Sun Closed</p>
Add another heading 2 element at the bottom of the body section that displays the text About us.

Add text to the About us section that displays in italics and also uses paragraph tags to display the following text:


AnyCompany was founded by a group of friends who share a passion for bicycling, and they all agree that it is always a great day to bike!
To view the solution code if needed, expand this section.

<h2>About us</h2>
<p><i>AnyCompany was founded by a group of friends who share a passion for bicycling, and they all agree that it is always a great day to bike!</i></p>
Task 3.3: Add hyperlinks
Add hyperlinks to the webpage.

Below the italicized About us text description, add a hyperlink as follows:

For the link text, enter Inspirational photo.
For the link, enter https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/SPL-PW-300-DVF301-DEV/images/biking-outdoors.jpeg.
Save the changes.

To test the result, refresh the webpage, and then choose Inspirational photo.

An image should display in the browser.

To review the solution, expand this section.

<h2>About us</h2>
<p><i>AnyCompany was founded by a group of friends who share a passion for bicycling, and they all agree that it is always a great day to bike!</i></p>
<a href="https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/SPL-PW-300-DVF301-DEV/images/biking-outdoors.jpeg">Inspirational photo</a>
 Consider: Notice that the browser navigates the user away from the page. To return to the page, choose the browser back button. In the next step, you provide users the ability to load a linked page while leaving the webpage open in the original browser tab.

To adjust the hyperlink to open in a new browser tab, do the following:
Add a target attribute to the anchor element’s start tag and give it the value _blank.

Refresh the page, and then choose Inspirational photo.

The image should open the linked photo in a new browser tab.

To review the solution, expand this section.

<a href="https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/SPL-PW-300-DVF301-DEV/images/biking-outdoors.jpeg" target="_blank">Inspirational photo</a>
In the Store location section, under the Hours line, add a new hyperlink to provide users directions:

For the link text, enter Get directions.
For the link, enter https://www.openstreetmap.org/search?query=nyc.
Configure the linked page to open in a new browser tab.

Task 3.4: Add an HTML entity
Add an HTML entity to the webpage.

Add a new paragraph element before the end of the body section. It should contain the following text:


2024, Amazon Web Services, Inc. or its Affiliates. All rights reserved.
In the element you just added, before the year, enter the HTML entity that renders a copyright symbol.

 Learn more: Refer to Common HTML Entities Used for Typography for information about how to find the alphanumeric value for the HTML entity. Then, enter the value into your page source.

Save the changes.

To verify that the copyright symbol displays correctly on the page, refresh the webpage.

To review the solution code if needed, expand this section.

<p>&copy;2024, Amazon Web Services, Inc. or its Affiliates. All rights reserved.</p>
Task 3.5: Add an image and a favicon
Make the webpage more interesting by adding images to the page.

Create an images directory on the web server and download an image to the directory. To accomplish this, in the AWS Cloud9 IDE Bash terminal run the following commands:


mkdir /home/ubuntu/environment/www/html/images
cd /home/ubuntu/environment/www/html/images
wget https://us-west-2-tcprod.s3.us-west-2.amazonaws.com/courses/SPL-PW-300-DVF301/v1.0.2.prod-9ba89a9a/scripts/logo-black.png
Add a company logo to the page using a relative URL, in your index.html file. To accomplish this, do the following:

Add an image element above the heading 1 element at the beginning of the body section.

Configure the image element to display the logo-black.png image you downloaded.

Reference the image location using a relative URL.

 Tip: Notice that in the AWS Cloud9 file browser the image is stored in a subdirectory named images, and your index.html page is in the html directory.

To review the solution, expand this section.

<body>
    <img src="images/logo-black.png">
    <h1>AnyCompany bicycle parts</h1>
To display the same image as an icon in the web browser tab, add a link element after the title element in the <head> section of the page as follows:


<link rel="icon" href="images/logo-black.png">
Save the changes.

To test, refresh the webpage.

Your completed webpage should display as follows.

completed webpage

 Task complete: In this task, you successfully added formatted text to the webpage so that the page provides valuable information to users.

Optionally preserve your work
 Note: In the next lab, you continue to work on improving this webpage with more details.

 Consider: You can optionally choose to download your index.html file progress so you can continue building on it in the next lab. Otherwise, a starter file will be available in the next lab environment to use instead. To download a file from the AWS Cloud9 IDE, open (right-click) the file in the file viewer, and then choose Download.

Conclusion
You have successfully done the following:

Verified that a web server is already installed on an AWS Cloud9 instance and is running
Troubleshot the networking configuration to permit access to the web server from the internet
Used the AWS Cloud9 IDE file editor to create a basic HTML page that uses heading and paragraph elements
Included hyperlinks and embedded images in an HTML page
Applied non-CSS styling to text in a webpage
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End Lab and then confirm that you want to end your lab.

For more information about AWS Training and Certification, see https://aws.amazon.com/training/.

Your feedback is welcome and appreciated.
If you would like to share any feedback, suggestions, or corrections, please provide the details in our AWS Training and Certification Contact Form.
