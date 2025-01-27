# Adding a Form and Buttons to a Webpage

```
curl 169.254.169.254/latest/meta-data/public-ipv4
35.93.142.205
```

## Lab overview

This lab challenges you to continue from where you left off in the previous lab, Python 3 – Lab 3: Styling a Webpage with CSS. In that lab you added Cascading Style Sheets (CSS) to an HTML page for the AnyCompany bicycle parts business. In this lab, you add a form to the page to collect product order details and submit them. You also add buttons that can be used by the website user to change the look of the webpage.

Objectives
By the end of this lab, you should be able to do the following:

Add an HTML form to a webpage.
Add input and label elements to an HTML form.
Observe HTTP GET and HTTP POST method network traffic results by using browser developer tools.
Add buttons to a webpage.
Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Analysis: A detailed examination of a topic or concept to promote understanding.
 Caution: Information of special interest or importance (not important enough to cause problems with equipment or data if you miss it, but it could result in the need to repeat certain steps).
 Command: A command that you must run.
 Consider: A moment to pause to consider how you might apply a concept in your own environment or to initiate a conversation about the topic at hand.
 Expected output: A sample output that you can use to verify the output of a command or edited file.
 Note: Additional information or elaboration on a point.
 Tip: A shortcut or recommended best practice.
 Task complete: A conclusion or summary point in the lab.
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

Image description: The diagram illustrates a setup where a web developer uses the AWS Cloud infrastructure to develop and host a website. The website is served from an Amazon Elastic Compute Cloud (Amazon EC2) instance running Ubuntu and an Apache HTTP server, which is accessible to the public through an internet gateway. The security group acts as a firewall to control access to the Amazon EC2 instance. To review the detailed diagram description, expand the following section.

Detailed diagram description
AWS services used in this lab
AWS Cloud9
Amazon Elastic Compute Cloud (Amazon EC2)
AWS services not used in this lab
AWS service capabilities used in this lab are limited to what the lab requires. Expect errors when accessing other services or performing actions beyond those provided in this lab guide.

Task 1: Establish the development environment
In this task, you connect to the AWS Cloud9 integrated development environment (IDE) for use in this lab, and load the solution files from the previous lab.

Task 1.1: Connect to the AWS Cloud9 IDE
Copy the Cloud9Environment URL value that is listed to the left of these instructions, and paste it into a new browser tab. It connects you to the AWS Cloud9 IDE.
Task 1.2: Load progress from the previous lab
To continue with the progress made in the previous lab, you need to load the solution files into your AWS Cloud9 environment.

Load the previous lab solution files. To accomplish this, complete one of the following two options:

Option 1: If you saved the index.html and the main.css files that you built in the previous lab, you can upload them to the web server document root:

In the AWS Cloud9 IDE file browser, expand the www directory and choose the html directory.
From the File menu, choose Upload local files. Browse to and select the index.html file from your computer.
In the AWS Cloud9 IDE file browser, choose the css directory.
From the File menu, choose Upload local files. Browse to and select the main.css file from your computer.
Option 2: Run the following two commands:

 Command: Copy the provided index.html and main.css files into your web server files location by running the following commands:


cp /var/tmp/DVF303-solution-index.html /var/www/html/index.html
cp /var/tmp/DVF303-solution-main.css /var/www/html/css/main.css
 Expected output:

None, unless there is an error.

In a separate browser tab, open the http://public-ip webpage (where public-ip is the IPv4 public IP address of the EC2 instance on which the AWS Cloud9 IDE is running).

 Note: You can retrieve the IPv4 public IP address by running this command in the AWS Cloud9 terminal:


curl 169.254.169.254/latest/meta-data/public-ipv4
 Expected output: Your IP address differs but should be formatted similarly.


18.236.252.155
Confirm that the webpage looks like this:

End-lab-3.

Image description: Image depicts the AnyCompany bicycle parts website where customers can browse bicycle parts, find store information, and learn more about the company. For a more detailed description, expand the following section.

Detailed image description
Webpage header: At the top of the webpage are navigation tabs or links labeled Products, Services, Location, and About us. These are meant to navigate to different sections of the company’s website.
Products section: The main area of the page is dedicated to products. It has a bold title PRODUCTS and features a list of bicycle parts, each with an image, a name, and a price. The following products are listed:
CASSETTE $50.00
CRANKSET $215.00
CHAIN $35.00
BELL $18.00
GEAR SHIFTER $32.00
INNER TUBE $14.00
Store location section: On the right side of the products, there’s a section titled STORE LOCATION. It provides the store’s address, phone number, and operating hours:
Address: 100 Anywhere Street, Anytown, USA
Phone: 555-1212
Hours: Mon-Fri 7 a.m.-7 p.m., Sat 8 a.m.-6 p.m., Sun closed
Below the hours is a button labeled Get directions, to help visitors find the store’s location by using a map service.
About us section: Below the map image, there’s a section titled ABOUT US.
Services section: There is an image of bicycle in a bike shop. There are a few paragraphs about the services offered. There is also an image indicating that the bicycle shop is “specialist certified.”
 Task complete: You have successfully connected to the AWS Cloud9 development environment for use in this lab, and loaded the solution files from the previous lab. You also verified that the website is operational by visiting the website from the IP address retrieved from the AWS Cloud9 instance.

Task 2: Create a products form
In this task, you wrap the Products table in an HTML form element with input elements that collect data from the user. You also create a Submit button by using an input element that submits the form data.

Task 2.1: Add a form element
Edit the index.html file to add form element tags.

In the AWS Cloud9 IDE file browser, expand the www and html directories and open the index.html file in the file editor.

Under <h2>Products</h2> add a new line with a form element start tag.

Place the form’s end tag just under the Product table’s end tag, but still inside the product’s div end tag.

Task 2.2: Add input and label elements
Continue editing the index.html file to add input and label elements.

At the bottom of the form, just before the form end tag, add a new div tag with class name submitform.

Inside the div, create an input element with a type attribute with value submit and a value attribute with value Submit.

 Note: A submit type submits the data from any other input elements in the form it is in. You have not yet created those other input elements, but you do that next.

Inside the Products table, locate the first product listing that has the <p>Cassette $50.00</p> line.

Inside this paragraph element, define three new elements:

A line break element
A label element
An input element
The end result should look as shown in the following code snippet, including the attributes set on the label and input elements.


<p>Cassette $50.00
  <br>
  <label for="cassette_qty">Quantity: </label>
  <input type="number" id="cassette_qty" name="cassette_qty" min="0" max="4" value="0">
</p>
Update the other product listings in the page so that each product also has these three elements. The settings are the same for all six products except the following details:

For the label elements, set the for attribute value:
Crankset – The value should be crankset_qty.
Chain – The value should be chain_qty.
Bell – The value should be bell_qty.
Gear shifter – The value should be shifter_qty.
Inner tube – The value should be innertube_qty.
For the input elements, set the id attribute value and the name attribute value to both match the label element’s for attribute value.
Expand this link to see the updated HTML code if needed.

<form>
    <table>
        <tr>
            <td>
                <img src="images/cassette.jpeg">
                <p>Cassette $50.00
                <br>
                <label for="cassette_qty">Quantity: </label>
                <input type="number" id="cassette_qty" name="cassette_qty" min="0" max="4" value="0">
                </p>
            </td>
            <td>
                <img src="images/crank-arm.jpeg">
                <p>Crankset $215.00
                <br>
                <label for="crankset_qty">Quantity: </label>
                <input type="number" id="crankset_qty" name="crankset_qty" min="0" max="4" value="0">
                </p>
            </td>
            <td>
                <img src="images/chain.jpeg">
                <p>Chain $35.00
                <br>
                <label for="chain_qty">Quantity: </label>
                <input type="number" id="chain_qty" name="chain_qty" min="0" max="4" value="0">
                </p>
            </td>
        </tr>
        <tr>
            <td>
                <img src="images/bell.jpeg">
                <p>Bell $18.00
                <br>
                <label for="bell_qty">Quantity: </label>
                <input type="number" id="bell_qty" name="bell_qty" min="0" max="4" value="0">
                </p>
            </td>
            <td>
                <img src="images/gear-shifter.jpeg">
                <p>Gear shifter $32.00
                <br>
                <label for="shifter_qty">Quantity: </label>
                <input type="number" id="shifter_qty" name="shifter_qty" min="0" max="4" value="0">
                </p>
            </td>
            <td>
                <img src="images/inner-tube.jpeg">
                <p>Inner tube $14.00
                <br>
                <label for="innertube_qty">Quantity: </label>
                <input type="number" id="innertube_qty" name="innertube_qty" min="0" max="4" value="0">
                </p>
            </td>
        </tr>
    </table>
    <div class="submitform">
        <input type="submit" value="Submit">
    </div>
</form>
Save the changes.

Refresh the webpage.

The Products area of the page should look as shown here.

Products form added.

Image description: The image shows that the Products section now has a form that allows users to set a quantity for each item and a Submit button.

 Note: Observe that each product now has a Quantity selector with a default value of 0. You set the default in each input element using the value attribute.

There is also a Submit button at the bottom of the product listings.

Test increasing the quantity amount for at least one of the products. How high of a quantity can you select? Why is that?

Expand this for the answer
You should not be able to choose more than four of any product. If you look at the input elements in the HTML source, you see that they contain a max attribute with a value of 4.

Task 2.3: Style the Submit button
With the Products section updated, you can now format the input element of type submit that acts as the form submit button.

Open the main.css file in the file editor.

In main.css, author a new CSS selector to format the contents of the submitform class div element to have the following attributes:

A width of 120 pixels
A height of 30 pixels
A grey background color
White italic text in 16 point font
Alignment to the right side with a 20 pixel right margin
Choose here if you need to see the solution CSS code

.submitform input {
    width: 120px;
    height: 30px;
    background-color: grey;
    color: white;
    font-style: italic;
    font-size: 16px;
    margin-right: 20px;
    float: right;
}
Save the changes.

Refresh the webpage.

The button should now appear just under the inner tube product and should have nice formatting.

Button formatted.

Image description: The Submit button now renders as grey with white text and is located in the bottom-right corner of the Products section just below the inner tube product listing.

Task 2.4: Observe the network during form submission with GET method
In this task, you open your browser’s development tools view and then submit the form to observe the network traffic that occurs.

Open the browser development tools view.

On the bicycle parts webpage, open the context menu (right-click anywhere on the page) and choose Inspect (if using Chrome or Firefox or Edge).

In the developer tools panel that appears, choose the Network tab.

The view should look something like the following image.

 Note: Different browsers have different developer tools UIs. This example shows a Chrome development tools view.

Developer tools UI.

Image description: The image shows a split browser pane. The left side is open to the bicycle website and the right pane shows the Chrome developer tools panel opened to the Network tab.

Keep the developer tools panel open.
On the webpage, choose 1 cassette and then choose Submit.
Observe the results.

Look at the URL in the webpage’s address bar. It should now list the items that you are attempting to purchase, along with the requested quantity of each item, in the format shown here:


http://<public-ip>/?cassette_qty=1&crankset_qty=0&chain_qty=0&bell_qty=0&shifter_qty=0&innertube_qty=0
In the developer tools, in the name column, choose the ?cassette_qty=1&... row.

On the Headers tab, observe the following:

The Request URL value matches the URL that displays in the browser’s address bar.

The Request Method is GET.

 Note: You have not defined a method attribute on the form element, and the default method for forms is GET.

On the Payload tab (Chrome or Edge) or the Request tab (Firefox), observe the following:

Chrome or Edge show Query String Parameters, but there is no Form Data.

Firefox shows No payload for this request.

Task 2.5: Observe the network during form submission with POST method
In this task, you observe how the webpage sends the data as a form instead of appending the data to the end of the URL as query string parameters.

Return to the index.html tab in the AWS Cloud9 IDE, and update the Products form element’s start tag so that it includes a method attribute with value POST.


<form method="POST">
 Note: The value of the method is not case sensitive; you could also type post.

Save the changes.

Refresh the http://public-ip webpage.

 Note: Make sure the address bar does not include any other characters after the public IP address. If it does, delete them and reload the page.

Choose at least 1 for the quantity of at least one of the products and then choose Submit.

Observe the results.

First, notice that the URL remained as http://public-ip, unlike previously where the form parameters were added to the requested URL.
In the developer tools view, on the Network tab, choose the item in the Name column that shows the IP address.
On the Headers tab, observe the following:
The Request URL value is simply the http://public-ip page.
The Request Method is POST.
On the Payload tab (Chrome or Edge) or the Request tab (Firefox), observe the following:
There is now a Form Data section that shows which items you requested and in what quantity.
 Analysis: In this case, your browser sent the data to the web server as form data, instead of appending the data to the end of the URL as query string parameters.

It is possible to invoke server-side processing of form data by using either the GET method or the POST method. However, the POST method does have some advantages. For example, you are not be limited by the number of characters that a browser can support in the URL. Also, the default GET method sends all submitted values as part of the URL. If you were having a user submit a password or other sensitive data, this would not be a secure approach. You can read more about GET, POST, and other HTTP request methods in Mozilla Developer Documentation in the Additional resources section.

Of course, the whole reason to submit data is to process it. For that, you need to implement logic on the server side. Typically, that is accomplished by using languages such as Python. There are popular Python frameworks, such as Django and Flask that can be used to connect your web frontend to a database where data can be either retrieved or stored. In fact, in later labs in this course, you use the Django framework to do just that for the AnyCompany bicycle parts website. However, storing the submitted data is beyond the scope of this particular lab.

 Task complete: You have successfully wrapped the Products table in an HTML form with input elements that collect data from the user. You also created a Submit button by using an input element that submits the form data.

Task 3: Add two buttons to the page
In this task, you create two new button elements that display on the webpage. These buttons permit the user to change the look of the banner on the webpage.

In the AWS Cloud9 IDE, in the tab where you have the index.html file open, locate the about-us div.

Inside and at the bottom of that div, just below the biking-outdoors image, create a new div and give it a class name of theme.

Inside of the theme div, create a button element and configure it as follows:

Create a type attribute with value button.
Set this text to display on the button: Light banner.
Create another button element and configure it as follows:

Create a type attribute with value button.
Set this text to display on the button: Dark banner.
Choose here if you need to see the changes to the code.

<div class="about-us" id="about-us-link">
    <h2>About us</h2>
    ...
    <img src="https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/SPL-PW-300-DVF301-DEV/images/biking-outdoors.jpeg">
    <div class="theme">
        <button type="button">Light banner</button>
        <button type="button">Dark banner</button>
    </div>
</div>
Save the changes.

Refresh the webpage.

You should see two new buttons that display under the photo of the bicyclist.

light banner and dark banner buttons

Image description: Two new buttons now appear under the photo of the bicyclist: Light banner and Dark banner.

Choose one of the new buttons.

Nothing happens. Even on the Network tab of the developer tools, you do not see any network traffic.

Even though you have defined buttons that appear to the end user, you have not yet defined the logic that should be invoked when one of the buttons is selected.

 Analysis: Recall that the button you created to collect products form data is actually defined as an input element with an attribute type=“submit”. By contrast, the Light banner and Dark banner buttons are button elements. Therefore, they behave differently. Also, these button elements are not associated with a form.

To make them do anything useful, you need to add JavaScript to your webpage, which is what you work on in the next lab.

 Task complete: You have now added buttons to your webpage that permit the website user to change the look of the banner on the image.

Optionally preserve your work
 Note: In the next lab in the course, you continue to improve the functionality of this webpage by adding JavaScript logic to it.

 Consider: You might optionally choose to download your index.html and main.css file progress so that you can continue building on them in the next lab. Otherwise, starter files are also available in the next lab environment if you choose to use that as the starting point for the next lab instead. To download a file from the AWS Cloud9 IDE, open the context menu for each file in the file viewer and choose Download.

Conclusion
You have successfully done the following:

Added an HTML form to a webpage.
Added input and label elements to an HTML form.
Observed HTTP GET and HTTP POST method network traffic results by using browser developer tools.
Added buttons to a webpage.
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End Lab and then confirm that you want to end your lab.

Additional resources
Mozilla Developer Documentation
For more information about AWS Training and Certification, see https://aws.amazon.com/training/.

Your feedback is welcome and appreciated.
If you would like to share any feedback, suggestions, or corrections, please provide the details in our AWS Training and Certification Contact Form.

JavaScript is a trademark of Oracle Corporation. Reference in this lab to any specific commercial product, process, or service, or the use of any trade, firm or corporation name is provided for informational purposes, and does not constitute endorsement, recommendation, or favoring by Amazon Web Services.
