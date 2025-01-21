# Organizing Elements in a Webpage

## Lab overview

This lab challenges you to continue from where you left off in the previous lab, Creating an HTML Webpage. In that lab you created a basic HTML page for the AnyCompany bicycle parts business. In this lab, you make use of additional HTML elements such as lists and tables to organize the content on your webpage.

Objectives
By the end of this lab you should be able to do the following:

Create an HTML table that contains embedded images in it.
Create unordered lists.
Author hyperlinks that link to another element in the same webpage.
Add horizontal lines and line breaks to modify the formatting of a webpage.
Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Caution: Information of special interest or importance (not important enough to cause problems with equipment or data if you miss it, but it could result in the need to repeat certain steps).
 Command: A command that you must run.
 Consider: A moment to pause to consider how you might apply a concept in your own environment or to initiate a conversation about the topic at hand
 Expected output: A sample output that you can use to verify the output of a command or edited file.
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
The following diagram shows the basic architecture of the lab environment. The resources depicted in the diagram already exist in your Amazon Web Services (AWS) account when you start the lab.

AWS Architecture diagram showing the initial state of the lab environment.

Image description: The diagram illustrates a setup where a web developer uses the AWS Cloud infrastructure to develop and host a website. The website is served from an Amazon Elastic Compute Cloud (Amazon EC2) instance running Ubuntu and an Apache web server, which is accessible to the public through an internet gateway. The security group acts as a firewall to control access to the Amazon EC2 instance. For more information, refer to the following detailed diagram overview.

To review the detailed diagram description, expand the following section.
The diagram illustrates an AWS infrastructure setup, which includes various components arranged hierarchically to represent how a web development environment is configured in the cloud. Starting from the outermost layer and moving inward, the components are as follows:

AWS Cloud: The overall environment is encapsulated in the AWS Cloud, which is the broader context where all the components reside.

Lab VPC: In the AWS Cloud, there is a virtual private cloud (VPC) designated as Lab VPC. This is like a virtual network in the AWS environment that is isolated from other virtual networks.

Public subnet: Inside the Lab VPC, there’s a public subnet. This subnet is accessible from the internet. A subnet is a range of IP addresses in the VPC.

Security group: In the public subnet, there’s a security group. It acts as a virtual firewall controlling the traffic to the Amazon Elastic Compute Cloud (Amazon EC2) instance.

Amazon EC2 instance: Inside the security group, there’s an EC2 instance. This is a virtual server in AWS where applications can run. The EC2 instance is depicted with the EC2 instance group icon. Inside this instance, two key components are mentioned:

AWS Cloud9 IDE: This is an integrated development environment (IDE) provided by AWS. In this diagram, it’s part of the EC2 instance. This indicates that the AWS Cloud9 IDE is being used for development directly in the EC2 instance.
Apache HTTP Server on Ubuntu operating system: This indicates that the EC2 instance is running the Ubuntu operating system and has an Apache HTTP Server installed on it. The Apache server is software that handles HTTP requests and serves webpages.
Internet gateway: There’s an internet gateway connected to the public subnet, which makes communication possible between the EC2 instance and the internet.

You (website developer): On the left side of the diagram, there’s an icon of a person with the label You (website developer). This represents the developer who interacts with the AWS Cloud and, specifically, the EC2 instance, perhaps using the AWS Cloud9 IDE for developing a website.

Website consumers: On the right side of the diagram, there’s an icon of three people with the label Website consumers. This represents end users or visitors who access the website hosted on the EC2 instance through the internet.

AWS services used in this lab
AWS Cloud9
Amazon Elastic Compute Cloud (Amazon EC2)
AWS services not used in this lab
AWS service capabilities used in this lab are limited to what the lab requires. Expect errors when accessing other services or performing actions beyond those provided in this lab guide.

Task 1: Establish the development environment
In this task, you connect to the AWS Cloud9 integrated development environment (IDE) to use as the development environment. Then you add the solution file from the previous lab into this environment to use in this lab.

Task 1.1: Connect to the AWS Cloud9 IDE
Copy the Cloud9Environment URL value that is listed to the left of these instructions, and paste it into a new browser tab. It connects you to the AWS Cloud9 IDE.
Task 1.2: Load progress from the previous lab
Load the previous lab’s solution. To accomplish this, you have two options:

Option 1: If you saved the index.html file that you built in the previous lab, you can upload it:

In the AWS Cloud9 IDE file browser, expand the www directory and choose the html directory.
From the File menu, choose Upload local files. Browse to and select the index.html file from your computer.
Option 2: Move the provided index.html file into your web server files location by running the following command:


sudo mv /var/tmp/DVF301-solution.html /var/www/html/index.html
 Expected output:

None, unless there is an error.

In a separate browser tab, open the http://public-ip webpage, where public-ip is the public IP address of the EC2 instance on which the AWS Cloud9 IDE is running.

If you need help finding the public IP address, choose here.
 Command: One way to retrieve the IPv4 public IP address of the instance is to run this command in the AWS Cloud9 terminal:


curl 169.254.169.254/latest/meta-data/public-ipv4
 Expected output: Your IP address is going to differ from the example but is formatted the same.


******************************
**** This is OUTPUT ONLY. ****
******************************
52.27.126.212
Copy the IP address from the command line output to your clipboard.
Another option is to browse to the Amazon EC2 console, locate and choose the running EC2 instance that has cloud9 in the name, and from the Details tab copy the public IPv4 address value.
 Note: In this lab environment, the inbound HTTP port was already opened in the security group.

Confirm that the webpage looks like this:

Previous lab solution.

Image description: The image is a screenshot of a webpage for a bicycle parts company named “AnyCompany bicycle parts.” Overall, the image presents a straightforward, left-aligned text-centric layout with a clear division of sections. It could be styled further with Cascading Style Sheets (CSS) to improve visual appeal, such as by adding columns, background colors, or images, or by adjusting text alignment and typography. For more information, refer to the following webpage detailed overview.

Webpage detailed overview
Here is a detailed description of its layout and content:

Top of the page: The browser tab indicates the name of the company and suggests that the content relates to bicycle parts. The browser window also shows the usual buttons for navigation, refresh, and home, as well as a URL bar, though the URL itself is not visible.
Header: At the top of the webpage, there is a simple black-and-white logo representing a cyclist. Below the logo is the company name AnyCompany bicycle parts in large, bold letters.
Main content area: The main content is divided into three key sections, with headings in bold black text: Products, Services, and Store location.
Products section:
The paragraph under the heading says that the company offers a variety of bicycle parts for sale and invites customers to visit the store to browse their selection.
Services section:
The wording under this heading details the services offered, such as help with installing bicycle replacement parts, bicycle tune-ups, flat tire repair, derailleur adjustments, and brake caliper adjustments. It also mentions the ability to specialize in custom bike builds tailored to specific needs.
Store location section: Under the Store location heading is the store’s address, phone number, and hours of operation listed as follows:
Address: 100 Anywhere Street, Anytown, USA
Phone: 555-0100
Hours: Mon-Fri 7 a.m.-7 p.m., Sat 8 a.m.-6 p.m., Sun Closed
Below the hours is a Get directions link, for navigation assistance.
Footer: The bottom of the webpage includes an About us section with a short paragraph about the founding of AnyCompany by a group of friends who are passionate about bicycling. It concludes with a statement that it is always a great day to bike. Below this, there is a link labeled Inspirational photo, which suggests a motivational image might be associated.
Layout and alignment: The content is aligned to the left side of the page, creating a clean and organized look. There are no visible elements that suggest complex styling or layout formatting like columns, sidebars, or boxes. It gives the impression of a plain design that could be enhanced with Cascading Style Sheets (CSS) for a more polished and visually appealing layout.
 Task complete: You have successfully connected to the AWS Cloud9 IDE to use as the development environment. Then you added the solution file from the previous lab into this environment to use in this lab.

Task 2: Add tables and sized images to the webpage
Previously you added a logo to the webpage. Wouldn’t it be nice if you could have the company name display to the side of the logo instead of below it? In this task, you use a table to accomplish that.

 Tip: As you make changes to the HTML source, you are encouraged to save them and refresh the http://public-ip page, which you should have open in a separate browser tab. In this way, you can quickly see how the changes that you make to the source code affect the look of the webpage. You might also find it helpful to consult the Mozilla Developer Network Web Docs Table Reference, in the Additional resources section, on occasion as you complete this task.

Task 2.1: Set the logo and company name in a table
In the AWS Cloud9 file browser, expand the www directory, and then expand the html directory.

Open the index.html file in the AWS Cloud9 file editor.

Just under the opening <body> tag, create a table element.

Inside the table element, create one row that contains two columns.

Add attributes to the table element:

Set a background color of lightgrey.

Make the contents of the table horizontally align in the center.

 Tip: Consult the w3.org Table Reference found in the Additional resources section if needed.

Move the logo so that is appears in the first column.

Move the AnyCompany bicycle parts text inside the second column and configure it:

Remove the heading 1 element in which it was previously wrapped.
Wrap the text instead in a font element.
Add a color attribute to the font element so that the text displays in blue.
Add a size attribute to the font element so that the text appears in 16 point font.
Save the changes.

Refresh the website and verify the look of the page. The top of it should look like this:

Header table added.

Image description: The image shows the AnyCompany bicycle parts logo and name formatted in a table with CSS attributes. The logo and name now appear centered on the page. The text color shows as blue, the font size has increased, and the background of the text is now set to grey.

Expand this link to see the source code for the table if needed.

<table bgcolor="lightgrey" align="center">
   <tr>
      <td><img src="images/logo-black.png"></td>
      <td><font color="blue" size="16">AnyCompany bicycle parts</font></td>
   </tr>
</table>
Task 2.2: Create a table to list products
In the AWS Cloud9 IDE file browser, notice that the html directory contains an images directory. Expand it to see that there are many images available to you.

Most of them are product images. You make use of some of these in this task.

In the index.html window, directly under the <h2>Products</h2> heading, create another table.

Give it two rows, with each row containing three columns.
In the table element, set a border attribute with a value of 1.
In the top-left cell of the table, add an image element that loads the cassette.jpeg image file that is in the images directory that you looked at a moment ago.

Save the changes.

Refresh the webpage.

You should notice that the image is unnecessarily large. This requires some adjustment to your code.

Back in the file editor, add a width attribute to the image element and set it to 100 pixels.

Save the changes.

Refresh the webpage.

The Products table should look more appropriate now, as shown here:

Cassette resized.

Image description: The image shows the Products section with an image in a table that is sized appropriately.

In the same table cell where you placed the cassette image, under the image element, add a paragraph element that contains the text Cassette $50.00.

Add five more products to the table so that every cell in the table contains a product image and a description beneath it:

In row 1 column 2, display the crank-arm image with the text Crankset $215.00.
In row 1 column 3, display the chain image with the text Chain $35.00.
In row 2 column 1, display the bell image with the text Bell $18.00.
In row 2 column 2, display the gear-shifter image with the text Gear shifter $32.00.
In row 2 column 3, display the inner-tube image with the text Inner tube $14.00.
Be sure to resize all the images to match the size of the cassette image.

Add the following attributes to each of the table row elements:

align="center"
valign="bottom"
Save the changes.

Refresh the webpage.

The top of the webpage should now look as shown here.

Narrow product table.

Image description: The image shows the AnyCompany logo and company name as before, and now shows the Products sections in a table that is left aligned. The images in each table cell are formatted to a specific size with descriptions and prices centered with the image.

It is nice that the products display, but the look can be improved with a few more adjustments.

Set a width attribute on the table element so that the table uses 100% of the width of the page.

Also set the table’s border attribute to a value of 0 (or remove the attribute entirely).

Save the changes.

Refresh the webpage.

 Note: The top of the webpage should now look as shown here. The Products heading aligns differently depending on the width of your browser window. Making your browser window wider or narrower also affects how close to each other the product images display.

100% width table.

Image description: The image shows the company logo and name styled as before. And now the Products section shows images of the products centered in each table cell at a set size where the table padding dynamically increases or decreases depending on how large or small the webpage is.

Expand this link to see the source code for the Products table if needed.

<table border="0" width="100%">
    <tr align="center" valign="bottom">
        <td>
            <img src="images/cassette.jpeg" width="100px">
            <p>Cassette $50.00</p>
        </td>
        <td>
            <img src="images/crank-arm.jpeg" width="100px">
            <p>Crankset $215.00</p>
        </td>
        <td>
            <img src="images/chain.jpeg" width="100px">
            <p>Chain $35.00</p>
        </td>
    </tr>
    <tr align="center" valign="bottom">
        <td>
            <img src="images/bell.jpeg" width="100px">
            <p>Bell $18.00</p>
        </td>
        <td>
            <img src="images/gear-shifter.jpeg" width="100px">
            <p>Gear shifter $32.00</p>
        </td>
        <td>
            <img src="images/inner-tube.jpeg" width="100px">
            <p>Inner tube $14.00</p>
        </td>
    </tr>
</table>
Remove the line of text below the table that states We offer a variety of bicycle parts for sale. Come into our store to browse our selection.
Task 2.3: Add more sized images
At the bottom of the Services section of the page, add an image element.
It should display the specialist image, which is in the images directory where you found all the product images.
Set the height to 150 pixels.
Towards the bottom of the Store location section of the page, just above the Get directions hyperlink, add an image element.
It should display the map image, which is in the images directory where you found all the product images.
Set the height to 130 pixels.
Expand this link to see partial source code for the added images if needed.

...
<p>We specialize in....</p>
<img src="images/specialist.png" height="150">
...
<p><b>Hours:</b> Mon-Fri 7 a.m.-7 p.m., Sat 8 a.m.-6 p.m., Sun Closed</p>
<img src="images/map.jpeg" height="130">
...
 Task complete: You have successfully used tables to format various sections of the webpage.

Task 3: Add additional formatting elements
In this task, you add horizontal lines, an unordered list, and line breaks.

Task 3.1: Add horizontal lines
Add horizontal line elements just above the following:
The Products heading

The Services heading

The Store location heading

The About us heading

The copyright line at the bottom of the page

Save the changes.

Refresh the page.

It should now contain lines between each section of content. An example section of the page is shown here.

Horizontal rules added.

Image description: The image shows horizontal lines separating each of the main sections of the webpage.

Expand this link to see partial source code for the added horizontal lines if needed.

<hr>
<h2>Products</h2>
...
<hr>
<h2>Services</h2>
...
<hr>
<h2>Store location</h2>
...
<hr>
<h2>About us</h2>
...
<hr>
<p>
...
</p>
Task 3.2: Add an unordered list
Add an unordered list.
In the Services section of the page, locate the following line:


<p><b>We offer a wide variety of services including</b> parts installation, bicycle tune-ups, flat tire repair, derailleur adjustments, and brake caliper adjustments.</p>
Modify the source code so that the information is formatted as a bulleted list, as shown here:

Unordered list.

Image description: The image shows an example of services offered in an unordered bulleted list.

Expand this link to see the source code for the unordered list if needed.

<p><b>We offer a wide variety of services including:</b></p>
<ul>
    <li>Parts installation</li>
    <li>Bicycle tune-ups</li>
    <li>Flat tire repair</li>
    <li>Derailleur adjustment</li>
    <li>Brake caliper adjustment</li>
</ul>
Task 3.3: Add line breaks
 Note: The store location details, including the address, phone, and hours, have significant white space between each line. This is because the paragraph element adds space above and below it. Remove that space.

Locate the lines in the Store location section that currently have the following HTML source code:


<p><b>Address:</b> 100 Anywhere Street, Anytown, USA</p>
<p><b>Phone:</b> 555-0100</p>
<p><b>Hours:</b> Mon-Fri 7 a.m.-7 p.m., Sat 8 a.m.-6 p.m., Sun Closed</p>
They render the text in the following way:

Address phone hours.

Image description: The image shows the store location details formatted in individual paragraphs where the Address, Phone, and Hours headings are bolded and the subsequent details are in plain text.

Place the address, phone, and hours text inside a single paragraph element and make use of multiple line break elements as needed to reformat this section so that it displays as shown here:

Address heading on one line and address directly below with no space; same for phone and hours.

Image description: The image shows the Address, Phone, and Hours headings in bold, with details on subsequent lines below each heading and line breaks in between the main sections.

Expand this link to see the source code for the formatted store location section if needed.

<p>
    <b>Address:</b>
    <br>100 Anywhere Street, Anytown, USA
    <br><br>

    <b>Phone:</b>
    <br>555-1212
    <br><br>

    <b>Hours:</b>
    <br>Mon-Fri 7 a.m.-7 p.m.
    <br>Sat 8 a.m.-6 p.m.
    <br>Sun Closed
</p>
At the bottom of the Store location section, add another line break between the map image and the Get directions link, so that the link appears below the graphic.

Save the changes. Your webpage should now look as shown here.

End lab page look.

Image description: The image shows that the various headings have been separated by line breaks.

 Task complete: You have successfully added horizontal lines, an unordered list, and line breaks to the webpage.

In this lab, you learned some approaches to formatting webpages. You did so without yet making use of Cascading Style Sheets (CSS), which is a technique that is the focus of the next lab.

The <font> element, as well as some of the attributes that you made use of in combination with the table element—such as the align, width, and border attributes—are now deprecated. However, it is still worth knowing that these formatting approaches are commonly found in legacy HTML code that is still in use, and most modern browsers still support them.

In the next lab, you learn how using CSS provides better fine-grained presentation controls and a more scalable and modern approach to affecting the look of your webpages.

Optionally preserve your work
 Note: In the next lab in the course, you continue to improve this webpage by making use of CSS to further enhance the display of the page.

 Consider: You mighty optionally choose to download your index.html file progress so that you can continue building on it in the next lab. Otherwise, a starter file is also available in the next lab environment if you choose to use that as the starting point for the next lab instead. To download a file from the AWS Cloud9 IDE, open the context menu for each file in the file viewer and choose Download.

Conclusion
You have successfully done the following:

Created an HTML table that contains embedded images in it.
Created unordered lists.
Authored hyperlinks that link to another element in the same webpage.
Added horizontal lines and line breaks to modify the formatting of a webpage.
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End Lab and then confirm that you want to end your lab.

Additional resources
w3.org Table Reference
Mozilla Developer Network Web Docs Table Reference
For more information about AWS Training and Certification, see https://aws.amazon.com/training/.

Your feedback is welcome and appreciated.
If you would like to share any feedback, suggestions, or corrections, please provide the details in our AWS Training and Certification Contact Form.