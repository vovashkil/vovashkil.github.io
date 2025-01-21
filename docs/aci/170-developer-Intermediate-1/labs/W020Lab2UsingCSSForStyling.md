# Using CSS to Define Webpage Styles

``
$ curl 169.254.169.254/latest/meta-data/public-ipv4
35.91.239.226
``

## Lab overview

This lab challenges you to continue from where you left off in the previous lab, Python 3 – Lab 2: Organizing Elements in a Webpage. In that lab, you added tables, an unordered list, and other non-Cascading Style Sheets (CSS) stylings to an HTML page for the AnyCompany bicycle parts business. In this lab, you style the same webpage using CSS and HTML content division (div) elements.

Objectives
By the end of this lab, you should be able to do the following:

Add div elements to an HTML page to support styling.
Add styling to an HTML page using inline CSS, internal CSS, and external CSS approaches.
Define CSS element selectors based on id and class.
Reference div elements and individual elements in div elements to accomplish fine-grained webpage formatting.
Create pointer hover effects using CSS.
Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Analysis: A detailed examination of a topic or concept to promote understanding.
 Caution: Information of special interest or importance (not so important to cause problems with the equipment or data if you miss it, but it could result in the need to repeat certain steps).
 Consider: A moment to pause to consider how you might apply a concept in your own environment or to initiate a conversation about the topic at hand.
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

Image description: The diagram illustrates a website developer working in an AWS Cloud environment using an AWS Cloud9 integrated development environment (IDE) hosted on an Amazon Elastic Compute Cloud (Amazon EC2) instance. This instance is set up in a security-controlled public subnet of a virtual private cloud (VPC) and is accessible over the internet. The hosted website is available to consumers through the Apache HTTP Server running on the EC2 instance. For more information, expand the following detailed diagram overview.

Detailed diagram overview
AWS services used in this lab
AWS Cloud9
Amazon Elastic Compute Cloud (Amazon EC2)
AWS services not used in this lab
AWS service capabilities used in this lab are limited to what the lab requires. Expect errors when accessing other services or performing actions beyond those provided in this lab.

Task 1: Establish the development environment
In this task, you establish the AWS Cloud9 integrated development environment (IDE) for the lab.

Task 1.1: Connect to the AWS Cloud9 IDE
Connect to the development environment.

Copy the Cloud9Environment URL value that is listed to the left of these instructions, and paste it into a new browser tab. It connects you to the AWS Cloud9 IDE.
Task 1.2: Load progress from the previous lab
Load the previous lab solution.

To load the solution, choose one of the following two options:

Option 1: If you saved the index.html file you built in the previous lab, upload it to the web server document root as follows:

In the AWS Cloud9 IDE file browser, expand the www directory, and then choose the html directory.

On the menu, choose File, and then choose Upload local files.

Choose Select files.

Select the index.html from your computer, and then choose Open.

Option 2: To copy the index.html file into your web server files location, run the following command:


sudo cp /var/tmp/DVF302-solution.html /var/www/html/index.html
 Expected output: There is no expected output unless there is an error.

 Caution: Run the following command separately from the preceding command, as running them together may cause issues in some browsers.

To set the proper permissions on the file, run the following command:


sudo chown ubuntu /var/www/html/index.html
 Expected output: There is no expected output unless there is an error.

In a new browser tab, test if you can access the http://public-ip webpage. Replace the public-ip placeholder value with the IPv4 public IP address of the EC2 instance where the AWS Cloud9 IDE is running.

 Tip: To retrieve the IPv4 public IP address, run the following command in the AWS Cloud9 terminal:


curl 169.254.169.254/latest/meta-data/public-ipv4
 Expected output: Your IP address will differ from the following example, but the format should be the same.


******************************
**** This is OUTPUT ONLY. ****
******************************

65.42.12.36
Confirm that the webpage displays similar to the following example.

end-lab-1

Image description: The image depicts a webpage for AnyCompany bicycle parts. It has a list of products with images and services offered. It also provides details for the store location, phone number, and hours of operation. There is an About us section at the bottom of the page.

 Task complete: You successfully established the development environment.

Task 2: Style sections of the page using three different CSS approaches
In this task, you author inline CSS in a start tag. You also author CSS code embedded in the head section of the HTML page. Finally, you author CSS externally in a separate file.

Task 2.1: Style using inline CSS
Wrap sections of the HTML source code in div elements and apply inline styling with CSS.

In the AWS Cloud9 file browser, expand the www directory, and then expand the html directory.

Choose index.html.

Create a div element directly under the <body> tag.

Configure the div to encompass the table that contains the website logo and company name.

Define a style attribute directly in the div start tag, and set the values in the style attribute as follows:

Set the background color to black.

Set the text color to white.

Set the font size to 250%.

 Tip: For information about which CSS properties to set in the style attribute, refer to Cascading Style Sheets in the Additional resources section.

Remove the font element where the website title currently displays, but keep the website title text.

Remove the bgcolor and align attributes that are currently set directly on the table element, but keep the table element.

Save the changes.

To test the changes, refresh the http://public-ip page.

It should display as follows.

header look

Image description: The updates change the logo and AnyCompany bicycle parts title section to a black background.

If needed, expand this section to reveal the solution code.

<div style="background-color:black;color:white;font-size:250%;">
    <table>
        <tr>
        <td><img src="images/logo-black.png"></td>
        <td>AnyCompany bicycle parts</td>
        </tr>
    </table>
</div>
 Analysis: Notice that all the styling attributes that apply to the table are now defined in the div tag itself. You have just implemented styling using the inline CSS approach.

Task 2.2: Add style using internal CSS
Add styling to the webpage using the internal CSS approach.

In the div tag that you added previously, add an id attribute with the value header.

In the head section, define a style element with a type attribute of text/css as follows:


<style type="text/css">
</style>
In the new style element in the head section, create an element selector for the id you just defined in the div as follows:


<style type="text/css">
    #header {
    }
</style>
 Tip: To reference an id, start your CSS selector with a # character followed by the value of the id you want to reference.

In the div tag, copy the value contained in the style attribute of that tag, and paste it into the CSS selector.

 Tip: Format the attribute selectors so each property in the selector appears on a separate line. This makes it more readable, even if it is not necessary for the code to function.

The code in the head section should be as follows:


<head>
    <title>AnyCompany bicycle parts</title>
    <link rel="icon" href="images/logo-black.png">
    <style type="text/css">
        #header {
            background-color:black;
            color:white;
            font-size:250%;
        }
    </style>
</head>
Remove the style=“” attribute and its contents from the div tag.

Save the changes.

Refresh the webpage.

 Tip: There should not be any noticeable change to the page. The significance of the change you implemented is that instead of defining the style in the div element using inline CSS, you defined it using internal CSS.

To review the solution if needed, expand this section.

<head>
    <title>AnyCompany bicycle parts</title>
    <link rel="icon" href="images/logo-black.png">
    <style type="text/css">
        #header {
            background-color:black;
            color:white;
            font-size:250%;
        }
    </style>
</head> 
<body>
    <div id="header">
        <table>
            <tr>
                <td><img src="images/logo-black.png"></td>
                <td>AnyCompany bicycle parts</td>
            </tr>
        </table>
    </div>
    ... (truncated)
Task 2.3: Add style using external CSS
Move the header styling into a separate file. This is the most commonly used approach because it separates the content layer (the HTML) from the presentation layer (the CSS).

In the AWS Cloud9 IDE, create a new folder inside the html folder and name it css.

In the css folder, create a file and name it main.css.

Open the main.css file in the text editor.

Confirm that you have the index.html file open in one tab and the main.css file open in another tab as follows.

index.html and main.css open in tabs

Image description: The image illustrates the AWS Cloud9 interface with two tabs open: one for the index.html file and one for the main.css file.

Choose View at the top of the page, and then choose Layout > Vertical Split.

Drag the index.html tab into the empty panel.

Your screen should display as follows.

split view

Image description: The image illustrates the AWS Cloud9 interface with the main.css file open in the top part of the split screen. The index.html file is open in the bottom part of the split screen. There is a terminal session below the index.html file.

Notice that you can edit and view the code in both the index.html file and the main.css file at the same time. This is helpful for the rest of the lab.

 Tip: To resize each open editor panel, drag the vertical border between the panels up or down.

To move the CSS details into the new file and link the HTML file to the new CSS file, do the following:

Copy the contents of the style tag into the main.css file.

Remove the style element and its contents from the head section.

Add the following element to the head:


<link rel="stylesheet" type="text/css" href="css/main.css">
Save the changes to both the index.html file and the main.css file.

Refresh the webpage.

There should be no change to how the page displays. However, the style is now defined in a separate file.

The source should be as follows.

external CSS implemented

Image description: The image illustrates the main.css file in the top part of the AWS Cloud9 interface and the index.html file in the bottom part.

 Tip: For the remainder of the lab, you edit both files, so keep both files open.

Task 2.4: Style heading 2 elements with CSS properties
Style the heading 2 elements in your webpage by authoring a CSS type selector.

In the main.css file, add the following type selector after the existing id selector:


h2 {
 
}
To add CSS properties to the h2 selector, configure the following settings:

Set the background color to darkblue.

Set the text color to white.

Add padding to match the following specifications:

10 pixels on the left
10 pixels on the top
10 pixels on the bottom
Add margins to match the following specifications:

5 pixels on the left
5 pixels on the right
Set the font family to Copperplate.

 Tip: For more information, refer to CSS: Cascading Style Sheets in the Additional resources section.

To review the solution if needed, expand this section.

h2 {
    background-color: darkblue;
    color: white;
    padding-left: 10px;
    padding-top: 10px;
    padding-bottom: 10px;
    margin-left: 5px;
    margin-right: 5px;
    font-family: Copperplate;
}
Save the changes to the main.css file.

Refresh the webpage.

Notice that all four heading 2 elements are formatted as blocks with a dark-blue background and white text. The words are all capitalized, even though the headings in the HTML are not. This is how the Copperplate font is designed to render.

 Tip: For more information, refer to Copperplate Gothic in the Additional resources section.

Experiment by making the following changes to the padding and the margin settings:

To comment out the padding-left property, make the following changes:


/*padding-left: 10px;*/
Save the changes.

Refresh the page.

Notice that there is a difference in how the page displays. The left padding provides space between the background-colored edges of the element and where the first letter of the first word begins.

Remove the change.

Now modify a different property — the margin-left property.

Save the changes.

Refresh the webpage.

 Analysis: Notice that there is a difference in how the page displays. Observe where the blue around the PRODUCTS heading starts relative to the black box of the header. They align on the left side because you commented out the margin-left property. However, on the right side of the page, the blue box does not extend as far as the black header box. This is because you have a margin-right property set for the h2 element but not in the header id selector that styles the div that contains the company logo and name table.

Undo the change.

Save the file.

Refresh the webpage.

 Task complete: You successfully styled sections of the page using three different CSS approaches.

Task 3: Update the page layout using CSS
In this task, you update the existing webpage layout using CSS.

Task 3.1: Wrap content in div elements with class attributes
Add div elements to the page and assign class names to each div. The following diagram depicts the page layout to be built.

layout of the page

Image description: Overall, the layout indicates a structured webpage with dedicated areas for a header, navigation menu, main content (products and services), a sidebar with additional information, and a footer. It’s a common layout for business or ecommerce websites that need to provide a lot of information in an organized way. For more information, expand the following Additional details section.

Additional details
At the top of the layout, spanning the full width, is a rectangle labeled header. This probably represents the topmost section of the webpage, which might contain the website’s title, logo, or other introductory content.
Beneath the header is a narrower, full-width rectangle labeled nav-menu. This section is probably the navigation bar, which might contain links to different parts of the website, such as Home, About Us, Services, Contact, and so on.
Beneath the nav-menu, occupying the majority of the left side of the page, is a large rectangle labeled products. This section might be designated for showcasing various products or services.
Adjacent to the right of the products section is a vertical rectangle labeled sidebar, which spans from the top of the products section to the bottom of it. Inside this sidebar are two smaller rectangles, one on top of the other. The upper rectangle is labeled location, indicating that it is a space for location details or a map. The lower rectangle is labeled about-us, which can be used for a brief description of the company or the individual who is running the website.
Beneath the products and the sidebar, there is a large rectangle that stretches across the layout. This section is labeled services, and it is split into two parts as follows:
On the left side of the services section, there’s a smaller rectangle labeled services-image, indicating a place for images related to the services.
To the right of the services-image is a rectangle labeled services-text, which probably contains descriptions or details of the services.
On the far right, still in the services section, is a rectangle labeled cert, which might be reserved for certifications or other credentials.
The bottom part of the layout features a full-width rectangle labeled footer. This section typically contains copyright information, contact details, or additional navigation links.
Remove all five <hr> tags from the HTML source code.

Add the following div tag above <h2>Products</h2>:


<div class="products">
Notice that you set a class attribute in the div tag. This is different from the id attribute you added previously in the header div.

Set the end </div> tag below the </table> tag that defines the end of the products table.

In the file editor, cut the Services section (all HTML code lines up to and including the specialist image), and paste it beneath the About us section (above the copyright line).

Add div tags to the Store location and About us sections as follows:

Wrap the Store location section (including the address, phone, hours, map, and directions content) in a div with a class="location" attribute.

 Tip: If you would like to indent multiple lines of code in the AWS Cloud9 editor, selecting them. Choose Edit at the top of the screen, and then choose Line > Indent. Although not required, indenting everything inside a given div tag helps you track the start and end div tags in your code.

Wrap the About us section (including the inspirational photo) in a div with a class="about-us" attribute.

Wrap both the Store location and the About us div elements inside another div element with a class="sidebar" attribute.

 Tip: Refer to the previous diagram to understand the layout you want to achieve in this step.

Wrap the Services section (including the specialist image) in a new div with a class="services" attribute.

 Tip: The div should end just before the paragraph tag that contains the copyright.

Save the changes.

If you need to review the order and the nesting of the div tags in your HTML source code, expand this section.

...
<body>
    <div id="header">
        <table>
            ...
        </table>
    </div>
    <div class="products">
        ...
    </div>
    <div class="sidebar">
        <div class="location">
            <h2>Store location</h2>
            ...
        </div>
        <div class="about-us">
            <h2>About us</h2>
            ...
        </div>
    </div>
    <div class="services">
        <h2>Services</h2>
            ...
        <img src="images/specialist.png" height="150">
    </div>
    <p>&copy; ...</p>
        ...
Task 3.2: Create columns with float and width settings
Create columns by specifying both float and width settings.

Add the following empty CSS class selectors to the bottom of the main.css file.


.products {
}
.sidebar {
}
.location {
}
.about-us {
}
.services {
}
 Tip: Notice that the selectors start with a dot (.) because you want to refer to class attributes. By comparison, the id selector you used to reference the header section started with a hashtag (#).

For each class selector, set a float property with the value left.

For the products class selector, set a width property with value 75%.

For the sidebar class selector, set a width property with value 25%.

For the location, about-us, and services class selectors, set a width property with value 100%.

If you need to review the solution, expand this section.

.products {
    float: left;
    width: 75%;
}
.sidebar {
    float: left;
    width: 25%;
}
.location {
    float: left;
    width: 100%;
}
.about-us {
    float: left;
    width: 100%;
}
.services {
    float: left;
    width: 100%;
}
Save the changes.

Refresh the webpage.

The top section of the page should display as follows.

columns created

Image description: The image depicts heading columns with the specified float and width settings.

If the page does not render as displayed here, verify that you nested the div tags correctly in your HTML source code.

Task 3.3: Create nested divs in the Services section
Add additional div elements as child elements of the services div and then style them with CSS.

Create a new div element directly underneath <h2>Services</h2> with a class="services-image" attribute.

The div element should have nothing in it.

Add an image element inside the new services-image div, and configure it as follows:

For the source, use the repair image, which is in the www/html/images directory.

Set the height to 350 pixels.

 Tip: You can define the height in the image tag as a property.

Under the new services-image div, create another new div element with a class="services-text" attribute.

This div should contain all the existing services-related paragraph elements, including the unordered list and the paragraph tag that appears after the list. It should not contain the specialist image.

Wrap the specialist image in a div with a class="cert" attribute.

Under the end tag for the div with class name services, wrap the copyright line in a new div with a class="footer" attribute.

Task 3.4: Style the Services section
Update the Services section using style tags.

Add a CSS selector to the main.css file for the services-image class, and configure the following settings:

Configure the CSS selector to float left.
Set the width to 40%.
Set the overflow to hidden.
Set a margin on the left of 5 pixels.
Add a CSS selector to the main.css file for the services-text class, and configure the following settings:

Configure the CSS selector to float left.
Set the width to 45%.
Set padding on the left to 20 pixels.
Add a CSS selector to the main.css file for the cert class, and configure the following settings:

Configure the CSS selector to float left.
Set the width to 10%.
Add a CSS selector to the main.css file for the footer class, and configure the following settings:

Configure the CSS selector to float left.
Set the width to 100%.
Set the background color to black.
Set the text color to white.
Set the font size to 12 pixels.
Align the text so it is horizontally centered.
To review the solution if needed, expand this section.

.services-image {
    float: left;
    width: 40%;
    overflow: hidden;
    margin-left: 5px;
}
.services-text {
    float: left;
    width: 45%;
    padding-left: 20px;
}
.cert {
    float: left;
    width: 10%;
}
.footer {
    float: left;
    width: 100%;
    background-color: black;
    color: white;
    font-size: 12px;
    text-align: center;
}
Save the changes.

Refresh the webpage.

It should display as follows.

divs added

Image description: The Services section is styled based on the options you defined.

Notice that the webpage looks more professional. Still, there are additional improvements to make. For example, the specialist graphic will look better if it is placed lower on the screen. Also, the content in the Store location and About us sections extends wider than the blue heading boxes. You fix these issues and others in the next section of the lab.

Task 3.5: Update the products table formatting
In this task, you format the layout of the products table.

Remove the hard-coded formatting in the products table HTML code as follows:

Remove the border and width settings from the table element.
Remove the align and valign attributes from the table rows.
Remove the width attribute from the images in the products table.
Add a CSS selector to the main.css file for the image elements in the products class, and set the width to 130 pixels as follows:


.products img {
    width: 130px;
}
 Tip: Although you can add this code anywhere in the main.css file, consider adding it under the .products selector. Continue the practice of placing new, more granular selector code below the related selector code. This makes it more efficient to locate your selector code as the number of lines in your CSS file grows.

 Tip: Earlier in this lab, you configured an h2 element selector that applies globally across all h2 elements in the page. With this new CSS selector, you also define an element selector (this one is for images). However, the scope of this element selector is set so that only images in an element that is part of the products class are affected.

Add a CSS selector for the table elements in the products class, and set the width to 100% as follows:


.products table {
    width: 100%;
}
Add a CSS selector for the paragraph elements in the products class to use the Copperplate font by adding the following to the main.css file:


.products p {
    font-family: Copperplate;
}
Add a CSS selector for the td elements in the products div, and set it to display a solid border of 1 pixel as follows:


.products td {
    border: 1px solid;
}
Save the changes to both files.

Refresh the webpage.

Notice that there are a few issues with the formatting of the table. For example, the table extends beyond the width of the header above it. Also, some columns are wider than others.

To adjust the table layout, add padding and table-layout selectors to the table elements in the products class, so that the CSS selector has these lines:


.products table {
    width: 100%;
    padding: 5px;
    table-layout: fixed;
}
Save the changes.

Refresh the webpage.

Notice that there is an improvement, but there are still issues with the layout.

Adjust the table rows so that all content in them vertically aligns to the bottom and horizontally aligns to the center as follows:


.products tr {
   vertical-align: bottom;
   text-align: center;
}
Save the changes.

Refresh the webpage.

Notice the improvements to the page layout.

Remove the border that you temporarily applied to the table.

Save the changes.

Refresh the webpage.

Notice that the border has been removed.

Task 3.6: Update the Store location and About us sections
Update the Store location and About us sections using CSS.

Modify the inspirational photo part of the page. Instead of providing a link to it, embed it in the page as follows:

Remove the anchor a element and its contents.
Replace it with the following image element:

<img src="https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/SPL-PW-300-DVF301-DEV/images/biking-outdoors.jpeg">
To finish formatting the Store location and About us sections of the page, add the following to the main.css file:


.location p, .about-us p {
    padding: 20px;
    background: lightgrey;
    margin-left: 5px;
    margin-right: 5px;
}
.location img, a {
    display: block;
    margin-left: auto;
    margin-right: auto;
    text-align: center;
}
.about-us img {
    margin-left: 5px;
    margin-right: 5px;
    max-width: 96%;
}
 Consider: Notice how the first selector you added applies styling to paragraph elements that display in two different CSS classes. By combining these into a single selector statement, you avoid repeating code unnecessarily.

Save the changes.

Refresh the webpage.

Notice the improvements to the page layout.

Remove the hard-coded italics from the HTML page, and specify the italics in CSS as follows:

In the About us section, locate the paragraph element, and remove the italics element while keeping the text inside it.

Create an id attribute in the same paragraph element with the value italicize.

The line should display as follows:


<p id="italicize">AnyCompany was founded by a group of friends who share a passion for bicycling, and they all agree that it is                     always a great day to bike!</p>
In the main.css file, create a new CSS selector to format in italics the text inside any paragraph elements in the sidebar div that have the id="italicize" attribute.

 Tip: With this approach, you define a selector on the parent div because the sidebar div is the parent of the about-us div. However, the style is still applied to the child content. This demonstrates how parent properties apply to child elements unless you apply an overriding setting at a more granular level.

To review the solution, expand this section.
Add the following to the main.css file:


.sidebar p[id="italicize"] {
  font-style: italic;
}
If you also added the following selector to the main.css file, it would override the previous selector for the paragraph element. To observe the effect, add the following, but remove it afterward.


.about-us p[id="italicize"] {
  font-style: normal;
}
To format how the certified specialist image displays on the page, add the following to the main.css file:


.cert img {
    display: block;
    margin-left: auto;
    margin-right: auto;
    margin-top: 50%;
}
Save the changes.

Refresh the webpage.

Notice that the image moves down vertically in relation to the text to the left of it.

 Task complete: You successfully updated the page layout using CSS.

Task 4: Add a navigation menu with hover features
In this task, you add a navigation menu to the webpage.

To add id attributes to the parts of the page that you want to link to from the navigation menu, do the following in the index.html file:

Locate <div class=“products”>, and update it so that it contains an id attribute as follows:


<div class="products" id="products-link">
Locate <div class=“services”>, and update it so that it contains an id attribute as follows:


<div class="services" id="services-link">
Locate the <div class=“location”>, and update it so that it contains an id attribute as follows:


<div class="location" id="location-link">
Locate the <div class=“about-us”>, and update it so that it contains an id attribute as follows:


<div class="about-us" id="about-us-link">
To create the navigation menu, under the company logo and company name, add the following code after the end tag of the header div:


<div class="nav-menu">
   <a href="#products-link">Products</a>
   <a href="#services-link">Services</a>
   <a href="#location-link">Location</a>
   <a href="#about-us-link">About us</a>
</div>
 Analysis: Notice that the hyperlinks you added point to the id attributes you added to the page. These hypertext reference (href) links take the user to the specific location on the same webpage.

Save the changes.

Refresh the webpage.

Notice that the links display on the page; however, the formatting needs improvement.

The page currently displays as follows.

navigation links unformatted

Image description: There is a navigation menu below the company banner that displays as text links.

You want the navigation menu to display as follows. Notice that when the user hovers over a button, the background color changes from grey to blue.

navigation implemented

Image description: There is a navigation menu below the company banner that uses a button layout instead of text links.

One way to update the format is to create a table with one row and four columns and place one link in each table cell. However, with CSS, there is a more efficient method, which you learn about next.

Add the following CSS code to your main.css file:


.nav-menu {
    font-size: 20px;
    font-style: italic;
}

.nav-menu a {
    float: left;
    display: block;
    color: white;
    background-color: grey;
    text-align: center;
    padding-top: 10px;
    padding-bottom: 10px;
    width: 25%;
    text-decoration: none; 
}
 Analysis: The float is set to the left. Also, each anchor element is set to a width of 25%. Because there are four links to display, they should fit one after the other in a single horizontal line (25% x 4 = 100%).

Also, text-decoration is set to none, so the standard HTML styling that uses underlines on hyperlinks does not apply.

Save the changes.

Refresh the webpage, and test by hovering the pointer over the links.

You improved the layout. However, the background color does not change when you hover over the links. To implement this improvement, you need to add another CSS selector.

Add the following to your CSS file:


.nav-menu a:hover {
    background-color: darkblue;
}
Save the changes.

Refresh the webpage.

When you hover the pointer over the menu links, the background color changes.

Test one of the navigation links as follows:

Make the browser tab with the webpage smaller so the Services section heading does not display on the page.
On the navigation menu, choose Services.
The browser should scroll down the webpage so the Services heading displays at the top of the page or your browser scrolls down until it reaches the bottom of the webpage.

Your completed webpage should display as follows. In later labs, you add more products and additional functionality to the page.

webpage complete

Image description: The website is fully styled using the CSS you configured in this lab.

 Task complete: You successfully formatted a webpage using CSS. You experienced how CSS provides a full set of features that you can use to accomplish fine-grained control over the display of webpage content.

Optionally preserve your work
In the next lab, you continue to improve the webpage by using CSS to enhance the display.

 Consider: You can optionally choose to download your index.html and main.css progress so you can continue building on it in the next lab. Otherwise, starter files will be available in the next lab environment to use instead. To download a file from the AWS Cloud9 IDE, open (right-click) the file in the file viewer, and then choose Download.

Conclusion
You have successfully done the following:

Added div elements to an HTML page to support styling
Added styling to an HTML page using inline CSS, internal CSS, and external CSS approaches
Defined CSS element selectors based on id and class
Referenced div elements and individual elements in div elements to accomplish fine-grained webpage formatting
Created pointer hover effects using CSS
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End Lab and then confirm that you want to end your lab.

Additional resources
For information, see each of the following resources:

CSS: Cascading Style Sheets In the left navigation pane, under Reference, expand the Properties menu to view an extensive list of properties available. For information about any of the properties, choose the corresponding link.
Copperplate Gothic
For more information about AWS Training and Certification, see https://aws.amazon.com/training/.

Your feedback is welcome and appreciated.
If you would like to share any feedback, suggestions, or corrections, please provide the details in our AWS Training and Certification Contact Form.