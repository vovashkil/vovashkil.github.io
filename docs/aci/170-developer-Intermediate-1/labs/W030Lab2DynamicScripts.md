# Using Dynamic Scripts in a Webpage

```
curl 169.254.169.254/latest/meta-data/public-ipv4
35.92.117.167
```

## Lab overview

This lab challenges you to continue from where you left off in the previous lab, Adding a Form and Buttons to a Webpage. In that lab, you added an HTML form to the webpage for the AnyCompany bicycle parts business. You also added two buttons that did not perform any actions.

In this lab, you add JavaScript logic to the page for event handling purposes. The JavaScript logic makes it possible for the end user to use the buttons to change the look of the page. You also add form validation to the product order form that you previously created. The JavaScript ensures that the user has selected at least one product before they can submit the form.

Objectives
By the end of this lab, you will be able to do the following:

Perform form validation actions using JavaScript.
Author a JavaScript function that modifies the look of a webpage when the webpage user chooses a button.
Author JavaScript code to locate specific elements and read and modify element attributes in the Document Object Model (DOM).
Write JavaScript code that logs messages to the browser console and creates pop-up windows to display to the website user.
Code JavaScript that swaps the image displayed on a webpage.
Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Caution: Information of special interest or importance (not important enough to cause problems with equipment or data if you miss it, but it could result in the need to repeat certain steps).
 Consider: A moment to pause to consider how you might apply a concept in your own environment or to initiate a conversation about the topic at hand.
 Expected output: A sample output that you can use to verify the output of a command or edited file.
 Hint: A hint to a question or challenge.
 Learn more: Where to find more information.
 Note: Additional information or elaboration on a point.
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
The following diagram depicts the basic architecture of the lab environment. The resources depicted in the diagram already exist in your Amazon Web Services (AWS) account when you start the lab.

AWS Architecture diagram showing the initial state of the lab environment

Image description: The diagram illustrates a web developer working in the AWS Cloud infrastructure to develop and host a website. The website is served from an Amazon Elastic Compute Cloud (Amazon EC2) instance running Ubuntu and Apache. It is accessible to the public through an internet gateway. The security group acts as a firewall to control access to the EC2 instance. For more information, refer to the following detailed diagram overview.

Detailed diagram overview
The diagram illustrates an AWS infrastructure setup that includes various components arranged hierarchically to represent how a web development environment is configured in the cloud. Starting from the outermost layer moving inward, the components are as follows:

AWS Cloud: This is the outermost boundary, indicating that all subsequent components are hosted in the AWS Cloud environment.
Lab VPC: In the AWS Cloud, there is a virtual private cloud (VPC) designated as Lab VPC. The VPC is a virtual network dedicated to your AWS account. It is isolated from other virtual networks.
Public subnet: In the Lab VPC, there’s a public subnet. This is a segment of the VPC where resources can be accessed from the internet. It implies that resources in this subnet can send and receive traffic directly from the internet.
Security group: The next layer represents a security group. It acts as a virtual firewall that controls the inbound and outbound traffic for the resources it’s associated with. In this architecture, the security group is associated with the Amazon Elastic Compute Cloud (Amazon EC2) instance. The security group ensures that only specified traffic can reach the EC2 instance.
Amazon EC2 instance: At the core, inside the security group boundary, there’s an EC2 instance, which is symbolized by the EC2 instance group icon. An EC2 instance is a virtual server in Amazon EC2 used to run applications on the AWS infrastructure. Inside this EC2 instance, the following components are detailed:
AWS Cloud9 IDE: The AWS Cloud9 integrated development environment (IDE) is represented by the AWS Cloud9 IDE resource icon. This suggests that the AWS Cloud9 service is being used for development purposes on this EC2 instance.
Apache HTTP Server on Ubuntu guest operating system: The EC2 instance is running the Ubuntu operating system, and an Apache HTTP Server is installed on it. The Apache HTTP Server is software that handles HTTP requests and serves webpages. In this architecture, it’s running on an Ubuntu system in the EC2 instance.
Internet gateway: On the right side, outside the Lab VPC boundary, there is an internet gateway. It connects the AWS Cloud infrastructure to the wider internet so traffic can flow between the two.
You (website developer): On the left side, outside the AWS Cloud, there is an icon of a person labeled You (website developer). This represents the developer who interacts with the AWS Cloud and, specifically, with the EC2 instance, possibly using the AWS Cloud9 IDE for developing websites.
Website consumers: On the right side, outside the AWS Cloud, there is an icon of three people labeled Website consumers. This represents the end users or visitors who access the website hosted on the EC2 instance through the internet.
AWS services used in this lab
AWS Cloud9
Amazon Elastic Compute Cloud (Amazon EC2)
AWS services not used in this lab
AWS service capabilities used in this lab are limited to what the lab requires. Expect errors when accessing other services or performing actions beyond those provided in this lab.

Task 1: Establish the development environment
In this task, you connect to the AWS Cloud9 development environment for use in this lab and load the solution files from the previous lab.

Task 1.1: Connect to the AWS Cloud9 IDE
Connect to the AWS Cloud9 integrated development environment (IDE) so you can carry out the tasks in this lab.

Copy the Cloud9Environment URL that is listed to the left of these instructions, and paste it into a new browser tab.

It connects you to the AWS Cloud9 IDE.

Task 1.2: Load progress from the previous lab
Load the solution files from the previous lab into your AWS Cloud9 environment.

To load the solution, choose one of the following two options:

Option 1: If you saved the index.html and the main.css files you built in the previous lab, upload them to the web server document root as follows:

In the AWS Cloud9 IDE file browser, expand the www directory, and then choose the html directory.
On the menu, choose File, and then choose Upload local files.
Choose Select files.
Select the index.html from your computer, and then choose Open.
In the AWS Cloud9 IDE file browser, choose the css directory.
Choose File, and then choose Upload local files.
Choose Select files.
Select the main.css from your computer, and then choose Open.
Option 2: To copy the index.html and main.css files into your web server files location, run the following commands:


cp /var/tmp/DVF304-solution-index.html /var/www/html/index.html
cp /var/tmp/DVF304-solution-main.css /var/www/html/css/main.css
 Expected output: There is no expected output unless there is an error.

In a new browser tab, test if you can access the http://public-ip webpage. Replace the public-ip placeholder value with the IPv4 public IP address of the EC2 instance where the AWS Cloud9 IDE is running.

 Command: To retrieve the IPv4 public IP address, run the following command in the AWS Cloud9 terminal:


curl 169.254.169.254/latest/meta-data/public-ipv4
 Expected output: Your IP address will differ from the following example, but the format should be the same.


65.42.12.36
Confirm the webpage displays as follows.

end-lab-4

Image description: The image depicts the AnyCompany bicycle parts website. Customers can browse bicycle parts, select quantities of items to purchase, find store information, and learn more about the company. For a detailed description of the website, expand the following detailed image description section.

Detailed image description
 Task complete: You successfully connected to the AWS Cloud9 development environment for use in this lab and loaded the solution files from the previous lab.

Task 2: Make it possible for users to change the banner color
In this task, you implement a JavaScript function that changes how the page displays. Specifically, it makes it possible for users to use the Light banner and Dark banner buttons you created in the previous lab to change how the content displays inside the header div.

Task 2.1: Style the banner by class
Update the main.css file to style the banner using a class, not by id.

In the AWS Cloud9 IDE, in the file browser, expand the www and html directories, and then open the index.html file in the file editor.

Expand the css directory, and then also open the main.css file in the file editor.

Modify the header section of the page so the CSS styling is accomplished by class instead of by id as follows:

In the main.css file, change the #header line to .banner.

Save the change.

In the index.html file, change the <div id=“header”> line to <div class="banner">.

Save the change.

Refresh the webpage.

There should be no change to how the page displays. However, the JavaScript code you author later in this lab refers to the elements in this section of the DOM by the new banner class you defined here.

 Caution: To ensure that cached content is ignored when refreshing a webpage, press Ctrl + the refresh icon (Windows) or Shift + the refresh icon (macOS).

Task 2.2: Apply id attributes to the banner buttons
Give each button a unique id attribute so it can be invoked from JavaScript.

For the banner buttons to function, each button requires a unique id attribute.

Scroll to the About us section of the HTML source code, and locate the following two lines of code:


<button type="button">Light banner</button>
<button type="button">Dark banner</button>
Add id attributes to each button so they can be uniquely invoked as follows:

Give the Light banner button an id attribute with the value light_button.

Give the Dark banner button an id attribute with the value dark_button.

To review the solution, expand this section.

<button type="button" id="light_button">Light banner</button>
<button type="button" id="dark_button">Dark banner</button>
Task 2.3: Author a basic function to be invoked by a button
Author a function for the buttons so they perform an action when invoked.

At the bottom of the body element content, just before the closing body tag, add a new script element.

Define a JavaScript variable as follows:

In the new script element, use the querySelector method to locate the light button object that exists in the DOM in the index.html file.

 Learn more: For more information about the querySelector method, see Document: querySelector() Method and Introduction to the DOM in the Additional resources section.

Assign it to a new variable that you defined named light_button.

To review the solution, expand this section.

<script>
   var light_button = document.querySelector('#light_button');
</script>
Define a JavaScript function as follows:

Below the variable, define a function, and give it the name updateBanner.

Inside the function, create a single line of code that uses a console object to print the message In updateBanner function to the browser console when the function is invoked.

 Learn more: For more information, see Console object in the Additional resources section.

Define an event listener to invoke the function as follows:

Use the addEventListener method to invoke the function when the button is selected.
Add the new line of code below the function you just created.
Test invoking the basic function as follows:

Save the changes.

Refresh the bicycle parts webpage.

On the webpage, open the context menu (right-click anywhere on the page), and then choose Inspect (Google Chrome or Mozilla Firefox or Microsoft Edge).

In the developer tools panel, choose the Console tab.

If using Firefox, make sure Logs is selected.
To test your JavaScript logic, on the webpage, choose Light banner.

The console should display the message In updateBanner function.

To review the solution, expand this section.

var light_button = document.querySelector('#light_button');      
function updateBanner() {
    console.log("In updateBanner function");
}
light_button.addEventListener('click', updateBanner);
Task 3: Finish creating the function logic
In the previous task, you established the basic functionality. When the Light banner button is selected, your updateBanner function is invoked and the code in it is run. However, the code in the function doesn’t do anything other than print a line to the console to show it was invoked.

In this task, you define logic so that the function updates the way the banner displays on the page. You make the updateBanner function generic enough to perform the action needed by both the Light banner button and the Dark banner button.

Your objective is to accomplish the following three actions when one of the two buttons is selected:

Update the background color on the banner div.

Update the color of the text in the banner div.

Swap the logo image to the appropriate color for the banner chosen by the user.

 Note: To review the images, choose www/html/images/logo-black.png and www/html/images/logo-white.png in the AWS Cloud9 file browser.

Task 3.1: Finish coding the updateBanner function
Start coding the function details.

Create a variable named dark_button that selects the Dark banner button object.

Replace the current updateBanner function code with the following code:


function updateBanner(backgroundColor, textColor, logoUrl) {
    var banner_div = document.querySelector("<FMI-1>");
    banner_div.style.backgroundColor = backgroundColor;
    banner_div.style.color = textColor;

    var logo = document.querySelector("<FMI-1> img");
    logo.setAttribute("src", logoUrl);
}
 Hint: To indent or outdent multiple lines of code in the AWS Cloud9 editor, select the lines. On the menu, choose Edit > Line, and then choose Indent or Outdent as needed. Indentation is not essential for JavaScript the way that it is for Python. However, applying standard formatting to your code can help you understand what your code is doing.

Replace both fill me in (FMI) placeholder values named <FMI-1> so that the following takes place:

The banner_div variable selects the div object in the DOM that has the banner class attribute.
The logo variable selects all image elements inside the banner class.
 Note: Notice that the function takes in three parameters: background, text, and logoUrl. These parameters must be passed into the function. You want the values passed in to be different, depending on whether the user selects the Light banner button or the Dark banner button.

Task 3.2: Add event listeners for the buttons
Author event listener code for the updateBanner function to be invoked when a user selects the Light banner or Dark banner button.

Update the light button event listener, and create a new event listener for the dark button as follows:

Remove the existing light button event listener.

Copy the following JavaScript code, and paste it into the same location:


light_button.addEventListener('click', function () {
    updateBanner("<FMI-2>", "<FMI-3>", "images/<FMI-4>");
});

dark_button.addEventListener('click', function () {
    updateBanner("<FMI-3>", "<FMI-2>", "images/<FMI-5>");
});
Replace the FMI placeholders in the previous code so that the appropriate values are passed to the updateBanner function when each button is selected as follows:

When the Light banner button is chosen, the logo-white image should display, the background color should be white, and the text in the div should be black.
When the Dark banner button is chosen, the logo-black image should display, the background color should be black, and the text in the div should be white.
Save the changes.

Task 3.3: Test the functions
Refresh the webpage.

On the webpage, verify that the developer tools panel is open. If not, open the context menu (right-click anywhere on the page), and then choose Inspect (Chrome or Firefox or Edge).

In the developer tools panel, choose the Elements tab. Expand the body element, and then expand the banner div and all the elements in it.

It should display as follows.

elements view pre-javascript invocation

Image description: The image depicts the Chrome developer tools panel open to the Elements tab.

 Note: The banner div element does not have an inline style attribute applied.

To test your changes, choose Light banner on the webpage.

The banner section of the page should display as follows.

light background look

Image description: The image depicts the AnyCompany logo and name with a white background.

The Elements tab of the developer tools should also indicate that the attributes were updated. Notice the new style attribute applied to the banner div and how the image element was updated.

banner image

Image description: The image depicts the Chrome developer tools panel open to the Elements tab. The banner class and style are set to white for background-color and black for color.

 Note: The new CSS attribute updates have been applied inline in the HTML code rendered to the end user. These inline CSS attribute settings override the settings specified in the main.css file, which has not changed. If you refreshed the webpage, these inline attributes would go away.

Test the Dark banner button.

The banner should revert to how it displayed originally.

dark background look

Image description: The image depicts the AnyCompany logo and name in white and the background color in black.

The Elements tab should indicate that the attributes were updated.

elements view of dark banner

Image description: The image depicts the Chrome developer tools panel open to the Elements tab. The banner class and style are set to black for background-color and white for color.

If your code is not functioning as intended, try the following troubleshooting tips:

Review the Console tab in the developer tools panel of the webpage. There might be error messages that indicate what the issue is. If you find an error, it can be helpful to copy the text of the error and paste it into a search engine. Determine if others have had similar errors, and review how they fixed them.

In the index.html file in the AWS Cloud9 IDE file editor, you might notice information (i) icons next to some of the lines of code in the JavaScript section of your code. Hover over the icons for information about what might need to be corrected. For example, perhaps you forgot to end a line with a semicolon (;).

If you need additional help after attempting to troubleshoot any issues on your own, expand this section to review the solution.
Notice that there is a slight difference in the height of the banner section when you toggle from dark mode to light mode and back. This is because there is a slight difference in the size of the logo images.

To fix the issue, add the following to the main.css file:


.banner img {
    height: 150px;
}
Save the changes.

Refresh the webpage.

To test the changes, on the webpage, choose Light banner, and then choose Dark banner.

The resizing issue should be resolved.

Congratulations! You used JavaScript to author event listeners that make it possible for the end user to change the display of the webpage. The code traverses the DOM and changes specific element attributes.

 Task complete: You successfully implemented a JavaScript function that changes the display of the page.

Task 4: Confirm product selection before order submissions
In this task, you use JavaScript to enhance the webpage. However, instead of affecting the display of the webpage, you use code to perform client-side form data validation. Specifically, you ensure that the user chooses a quantity of at least 1 for at least one product before they can submit an order. If they do not, you alert the user so they can correct the issue and try again.

Task 4.1: Add a document event listener
Start by adding an event listener that logs a message to the console when the webpage finishes loading.

In the same script section if the index.html file, below the existing code, attach an event listener using the document interface, which represents the root node of the HTML DOM tree, as follows:


document.addEventListener('DOMContentLoaded', function () {
    //function logic goes here
    console.log('In document.addEventListener')
});
 Learn more: For more information about the Document interface, see Document in the Additional resources section.

Save the changes.

Verify that you have the developer tools panel open for the webpage, and choose the Console tab.

Refresh the webpage.

Notice the In document.addEventListener message in the Console tab.

 Note: The addEventListener takes the following parameters: event, function, and capture. The event and function parameters are required. DOMContentLoaded is an event that occurs after the entire HTML document has been loaded and all the scripts associated with the page have been run. This listener waits for the entire document to load, then runs the code. For more information, see Document: DOMContentLoaded Event in the Additional resources section.

Task 4.2: Add a form variable and an event listener for the form
Continue by adding a form variable to the document event listener. Then add an event listener to notice when the form is submitted. That event listener should contain logic to ensure a quantity of at least 1 was selected for at least one product in the form.

Under the //function logic goes here comment, create a variable named form that selects the form element contained in the products class.

 Hint: Use the querySelector method that you used in Task 2.

Copy the following code, and paste it under the form variable, but keep it enclosed inside the document.addEventListener() method.


form.addEventListener('submit', function (event) {
    var inputElements = <FMI-1>.querySelectorAll('input[type="number"]');
    var atLeastOneSelected = false;

    // Loop through each input element
    <FMI-2>.forEach(function(input) {
        var quantity = parseInt(input.value, 10);
        if (quantity > 0) {
            atLeastOneSelected = true;
        }
    });

    // If no quantities selected
    if (<FMI-3>) {
        event.preventDefault();
        alert('<FMI-4>');
    }
});
 Hint: Remember, you can indent or outdent multiple lines of code in the AWS Cloud9 editor. Choose Edit > Line, and then choose Indent or Outdent as needed.

Replace <FMI-1> with the correct value to store all the input elements of type number that appear in the form element into the inputElements variable.

Replace <FMI-2> with the name of the variable that contains the elements that contain the quantity values selected by the person submitting the form.

Replace <FMI-3> so that it checks for the condition where none of the products were selected (given a quantity higher than 0).

Replace <FMI-4> with a pop-up message to the user. It should explain what needs to be corrected to successfully submit the form.

Save the changes to your code.

Task 4.2: Test the form validator
Verify the code you added is working as intended by testing form submission.

Reload the webpage in your browser to ensure that the updated logic is loaded into your browser session.

Leave all the quantities selected as 0 for all products in the form, and then choose Submit.

If your code is functioning correctly, you should receive a pop-up message displaying the text you authored in place of the <FMI-4> placeholder as follows.

pop up message

Image description: The image is a screenshot of the AnyCompany bicycle parts website with a pop-up window displaying the text you authored in place of “Please choose a quantity greater than 0 for at least one product.”

To dismiss the pop-up message, choose OK.

Verify that you have the developer tools panel open, and choose the Network tab.

On the webpage, enter a quantity of at least 1 for any of the products, and then choose Submit.

The pop-up window should not appear. Instead, the Network tab should have a line with the external IP address of the webpage.

To review the form data that was submitted, choose the link for the IP address, and then choose Payload (Chrome or Edge) or Request (Firefox).

 Note: This is the same form behavior that you achieved at the end of the previous hands-on lab where you created the form and tested it.

If needed, try the following troubleshooting tips:

Review the Console tab in the developer tools panel of the webpage. There might be error messages that indicate what the issue is. If you find an error, it can be helpful to copy the text of the error and paste it into a search engine. Determine if others have had similar errors, and review how they fixed them.

In the index.html file in the AWS Cloud9 IDE file editor, you might notice information (i) icons next to some of the lines of code in the JavaScript section of your code. Hover over the icons for information about what might need to be corrected. For example, perhaps you forgot to end a line with a semicolon (;).

If you need additional help after attempting to troubleshoot any issues on your own, expand this section to review the solution.

<script>
    ...(code from Task 2 not shown)...

   document.addEventListener('DOMContentLoaded', function () {
       var form = document.querySelector('.products form');

       form.addEventListener('submit', function (event) {
           var inputElements = form.querySelectorAll('input[type="number"]');
           var atLeastOneSelected = false;

           // Loop through each input element
           inputElements.forEach(function(input) {
               var quantity = parseInt(input.value, 10);
               if (quantity > 0) {
                  atLeastOneSelected = true;
               }
           });

           // If no quantities selected
           if (!atLeastOneSelected) {
               event.preventDefault();
               alert('Please choose a quantity greater than 0 for at least one product.');
           }
       });
   });
</script>
 Task complete: You successfully used JavaScript to enhance the webpage to perform client-side form data validation. You ensured that the user chose a quantity of at least 1 for at least one product before the user could submit an order. If not, you alerted the user so they can correct the issue and try again.

Congratulations! You successfully implemented client-side form validation on your webpage.

Performing these checks before users can make submissions is a more efficient design. There is no benefit to sending data across the network if you know prior to submission that the user needs to provide more information to process the order. By implementing the check on the client-side, you alert the user to the issue more quickly, and you avoid unnecessary additional processing on the server-side.

Optionally preserve your work
 Note: In the next labs, you work with the Django web framework. Over a series of labs, you migrate the webpage you created to run on Django. Using Django provides a database storage layer for your web application. You can store product information and web form data in a database and further enhance the AnyCompany bicycle parts website. For example, you can confirm to the user in a response webpage that their order has been received. You can also display the submitted order details to them.

 Consider: You can optionally choose to download your index.html and main.css file progress so you can continue building on them in the next lab. Otherwise, starter files will be available in the next lab environment to use instead. To download a file from the AWS Cloud9 IDE, open (right-click) the file in the file viewer, and then choose Download.

Conclusion
You have successfully done the following:

Performed form validation actions using JavaScript.
Authored a JavaScript function that modifies the look of a webpage when the webpage user chooses a button.
Authored JavaScript code to locate specific elements and read and modify element attributes in the DOM.
Written JavaScript code that logs messages to the browser console and creates pop-up windows to display to the website user.
Coded JavaScript that swaps the image displayed on a webpage.
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End Lab and then confirm that you want to end your lab.

Additional resources
Document: querySelector() Method
Introduction to the DOM
Console object
EventTarget: addEventListener() Method
Document
Document: DOMContentLoaded Event
For more information about AWS Training and Certification, see https://aws.amazon.com/training/.

Your feedback is welcome and appreciated.
If you would like to share any feedback, suggestions, or corrections, please provide the details in our AWS Training and Certification Contact Form.

Python is property of the Python Software Foundation (PSF), and JavaScript is a trademark of Oracle Corporation. Reference in this lab to any specific commercial product, process, or service, or the use of any trade, firm or corporation name is provided for informational purposes, and does not constitute endorsement, recommendation, or favoring by Amazon Web Services.