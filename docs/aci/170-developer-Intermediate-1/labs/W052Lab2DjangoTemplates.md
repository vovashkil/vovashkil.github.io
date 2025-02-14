# Creating Templates in a Web Framework

## Lab overview

This is the fourth in a series of labs that have you working with Django, a Python web framework that helps you avoid extra coding and helps you build websites that are scalable and maintainable. In the first Django lab, you installed and configured the Django web framework in a Python virtual environment.

In the second lab, you configured Django to use MySQL as the database and defined Django models for the bicycle supplies web app. In the third lab, you created Django views to process HTTP requests and read application data from a database and write application data to a database.

In this lab, you create Django templates to provide the end user interface for users. With templates, users can take essential actions. For example, they can load the main AnyCompany bicycle parts product order form. They can also place an order, view an order confirmation, view order history, and view line item details for any previous order.

In this lab, you complete the migration of the bicycle parts website to Django. In the process, you add the order-handling features that your non-Django website did not provide.

Objectives
By the end of this lab, you should be able to do the following:

Create a template in Django.
Use the Django template language to display Django model date to a user.
Configure static assets, such as images and Cascading Style Sheets (CSS), to display in a Django template.
Create a Django template that extends another template.
Use a url Django template tag to invoke a Django view to display order details.
Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Analysis: A detailed examination of a topic or concept to promote understanding.
 Caution: Information of special interest or importance (not important enough to cause problems with equipment or data if you miss it, but it could result in the need to repeat certain steps).
 Consider: A moment to pause to consider how you might apply a concept in your own environment or to initiate a conversation about the topic at hand.
 Expected output: A sample output that you can use to verify the output of a command or edited file.
 Note: Additional information or elaboration on a point.
 Task complete: A conclusion or summary point in the lab.
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

AWS Architecture diagram showing the initial state of the lab environment.

Image description: The diagram illustrates that a website developer is working in an AWS Cloud environment using an AWS Cloud9 integrated development environment (IDE) hosted on an Amazon Elastic Compute Cloud (Amazon EC2) instance. This instance is set up in a security-controlled public subnet of a virtual private cloud (VPC). To review the detailed diagram description, expand the following section.

Detailed diagram description
AWS services used in this lab
AWS Cloud9
Amazon Elastic Compute Cloud (Amazon EC2)
AWS services not used in this lab
AWS service capabilities used in this lab are limited to what the lab requires. Expect errors when accessing other services or performing actions beyond those provided in this lab.

Task 1: Run the script to configure the development environment
In this task, you run a script that installs the Django framework on your Ubuntu Linux instance. You also set up your environment to match the end state of the previous lab.

Task 1.1: Connect to the IDE and run the setup script
Start by running a script, starting the web server, and adding product data to the database.

To open the AWS Cloud9 environment, copy the Cloud9Environment URL value that is listed to the left of these instructions, and paste it into a new browser tab.

It connects you to the AWS Cloud9 integrated development environment (IDE).

 Command: In the AWS Cloud9 IDE terminal window, run the following command:


./setup.sh
 Analysis: The shell script completes configurations on the EC2 instance where your AWS Cloud9 IDE is installed. The configuration replicates the steps that you completed in the previous lab. It installs a Python virtual environment and Django, and creates the bicycle_project Django project and the bicycle_app Django app.

 Important: If you receive a prompt asking which services to restart, press Tab to navigate to Ok, and then press Enter so that the script continues to run.

 Expected output:


************************
**** EXAMPLE OUTPUT ****
************************
...
restore bicycles database
delete product table contents
reset auto_increment on product table
create the django user
tar: Ignoring unknown extended header keyword 'SCHILY.fflags'
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.FinderInfo'
 Command: To activate the python virtual environment and start the Django web server, run the following commands:


cd ~/environment/django
source .venv/bin/activate
python manage.py runserver 0.0.0.0:8080
 Expected output:


******************************
**** This is OUTPUT ONLY. ****
******************************

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
February 07, 2024 - 22:10:13
Django version 5.0.2, using settings 'bicycle_project.settings'
Starting development server at http://0.0.0.0:8080/
Quit the server with CONTROL-C.
 Important: The web server remains running while you keep the process active in the terminal. Leave this terminal as it is. Debug and log information is written to this terminal’s output as you progress through the lab. If at any point during this lab you find an error in the bicycle app webpage, you can read through any information written to the webpage. You can also read the log and output written to this runserver process terminal.

To add product data to the product table, open a second terminal window in the AWS Cloud9 IDE.

 Command: In the new terminal, run the following:


cd ~/environment/django
source .venv/bin/activate
python manage.py loaddata /home/ubuntu/environment/products.json
 Expected output:


******************************
**** This is OUTPUT ONLY. ****
******************************

Installed 12 object(s) from 1 fixture(s)
 Command: To confirm that the product data is now in the database, run the following command:


mysql --defaults-extra-file=/etc/mysql/config.cnf -e "use bicycles; select * from bicycle_app_product;"
 Expected output:


******************************
**** This is OUTPUT ONLY. ****
******************************

+----+-----------------+-----------------------------+--------+---------------+----------------------+
| id | product_name    | description                 | price  | product_group | image_url            |
+----+-----------------+-----------------------------+--------+---------------+----------------------+
|  1 | cassette        | sprockets, gear wheels      |  50.00 |             1 | cassette.jpeg        |
|  2 | crankset        | Made of Forged Alloy 6061   | 215.00 |             1 | crank-arm.jpeg       |
|  3 | chain           | 1/2 x 11/128 Inch 116 Links |  35.00 |             1 | chain.jpeg           |
|  4 | bell            | pretty loud                 |  18.00 |             2 | bell.jpeg            |
|  5 | gear shifter    | very precise                |  32.00 |             1 | gear-shifter.jpeg    |
|  6 | inner tube      | fix any flat tire           |  14.00 |             3 | inner-tube.jpeg      |
|  7 | saddle          | better with than without    |  55.00 |             2 | seat.jpeg            |
|  8 | wheel           | an extra does not hurt      | 179.00 |             2 | wheel.jpeg           |
|  9 | pedals          | you really need them        |  79.00 |             1 | pedals.jpeg          |
| 10 | brake disk      | no more noise on a wet day  |  45.00 |             4 | brake-disk.jpeg      |
| 11 | hydraulic brake | stop quickly when necessary |  69.00 |             4 | hydraulic-brake.jpeg |
| 12 | sports glasses  | wanna look cool?            | 129.00 |             2 | sports-glasses.jpeg  |
+----+-----------------+-----------------------------+--------+---------------+----------------------+
You should see that the products are listed in the output.

Task 1.2: Confirm that the app is running
Confirm that the Django environment that you now have matches the environment that you created by the end of the previous lab.

Return to the terminal where the runserver process is running, and choose the link in the Cloud9 Help dialog box, which should appear in the corner.

A new browser tab opens and displays the webpage. It matches what you configured in the previous lab.

Test form.

Image description: Image shows a webpage with Test page for submitting form data in bold text. Below this is a list of products followed by quantity input boxes for cassette and crankset. At the bottom is a Submit button.

 Tip: You can get to the same preview page at any time by choosing Preview > Preview Running Application, and then in the preview panel choose the pop out into new window icon pop-out icon to open the preview in a new browser tab.

Choose a quantity of at least 1 for at least one of the products, and choose Submit.

The browser should display the message “/order_result page loaded. Check the runserver console for test result.” And the runserver terminal output should display log information indicating that an order was saved.

Replace /order_result at the end of the URL in the browser with /order_history, and then observe the runserver terminal output.

A few orders are listed, because this view returns all orders and this lab environment is designed to match the environment that you achieved by the end of the previous lab.

Now replace /order_history at the end of the URL in the browser with /lookup_order/3, and observe the runserver terminal output.

The details for the order with the order id value of 3 are returned in the terminal.

In summary, the lab environment that you now have matches what you had at the end of the last lab.

Keep this browser tab open for the duration of this lab. You return to it later.

Understanding the work to be done
 Consider: Recall that Django uses a Model View Template architecture. In the previous labs, you defined the models and views for the bicycle supplies website.

In this lab, you finally create the templates to accomplish the following:

Present the static website content that is unrelated to order processing but that gives the site the look and feel that it had before.
Present a product order form on the main page, populated with data from the Products model.
Allow the user to place an order for any product from the website, record the order details, and return an order results page.
Provide a view to users that shows all prior orders, with a link for each order to retrieve the details for that particular prior order.
You have seen this summary in the previous lab, but it is presented here again to review if it is helpful. The design that you accomplish is illustrated in the following diagram. Here is an explanation of each labeled step:

Step 1: Your browser makes a request to load the URL.

Step 2: Django consults the URL patterns defined in urls.py to determine where to route the request.

Step 3: A function written in Python in the views.py file is invoked. It contains the application logic.

Step 4: The view logic typically runs a SQL query using the included model to look up data or modify or insert data. A dataset from the database is returned to the view.

Step 5: To build the response, the view logic typically loads an HTML template and then injects data from the dataset into it.

Step 6: Finally, the view logic returns the response, which might render the same page to display data from the dataset. Or the view logic might redirect the user to a different webpage that makes use of a different template to display dataset results.

Model-view-template data flow.

Image description: Image depicts the logic using six steps, as explained before the image.

 Task complete: In this task, you successfully ran a script to install the Django framework on your Ubuntu Linux instance, and you configured the environment to match the end state of the previous lab.

Task 2: Begin migrating the bicycle website HTML to Django
In this task, you load the website that you built in earlier labs in this course to review what it looked like. You then migrate the HTML, CSS, and image files into the Django app.

Task 2.1: Observe the pre-Django website
Begin by starting the Apache web server and loading the older website that does not use Django.

 Command: To start the Apache web server, run the following command in the second terminal window:


sudo service apache2 start
 Expected output:

None, unless there is an error.

 Command: To retrieve the public IP address, run the following command:


TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600" &> /dev/null` && curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/public-ipv4
 Expected output:


******************************
**** This is OUTPUT ONLY. ****
******************************

32.220.64.76
 Note: You can also retrieve this public IP address from the EC2 console details page.

 Tip: Your Django web server is still running in the other terminal window and uses port 8080. This Apache web server runs on port 80.

In a new browser tab, load the non-Django hosted AnyCompany website at http://public-ip/ where public-ip is the public IP address returned by the curl command that you just ran.

The website loads. The website code exactly matches what you completed building by the end of the Using JavaScript in a Webpage lab.

In the AWS Cloud9 file browser, expand the www and html directories and open the index.html file in the text editor.

This is the source code of the Apache web server-hosted page that you just loaded. If you worked through the earlier labs in this course, this code should look very familiar.

Close the browser tab where you loaded the non-Django website, but leave the index.html file open in the file editor.

Task 2.2: Migrate the HTML
Continue by starting to migrate the older website code into the Django web app code.

Copy all the code in the www > html > index.html file file to the clipboard.

Close the index.html file.

Now open the django > bicycle_app > templates > index.html file.

Delete everything in it and paste in the code that you just copied. From the File menu, choose Save to save the change.

Open the bicycle_app > views.py file and modify the index function:

Update the return render… line of code so that it renders index.html instead of the test form.
Save the change, and then load the main https://…vfs.cloud9.us-west-2.amazonaws.com/ page (with the path segment at the end of the URL after the slash removed).

At this point, the page has formatting issues and missing graphics issues. This is expected.

First try.

Image description: Image shows a generic version of the AnyCompany bicycle parts website with a table layout but the no CSS elements to help modify the look and feel of the page. Additionally, there are image placeholders but no images can be seen.

Task 2.3: Configure static content to display images
Recall that your bicycle supplies website references many image files that reside in an images directory, which is a subdirectory of the html directory where the index.html file resides. Django has a different way of referencing such static content. In this task, you configure the images to display.


django.contrib.staticfiles
Open the django > bicycle_project > settings.py file. Confirm that the INSTALLED_APPS list includes this line: django.contrib.staticfiles. Toward the bottom of the file, there should also be this line: STATIC_URL = ‘static/’.

Both of these settings are relevant to the hosting of static files. However, you do not need to modify them.

Close the settings.py file.

Copy the images directory content from the Apache web server location to the location where your Django app expects them to exist. As you just observed in the settings.py file, that is in a folder named static. You can accomplish this manually by using the file browser, or by running the following commands:


mkdir -p ~/environment/django/bicycle_app/static/
cp -R /var/www/html/css ~/environment/django/bicycle_app/static/
 Expected output:

None, unless there is an error.

 Command: You also need to copy the css folder and its contents to the static directory. To accomplish that, run the following command:


cp -R /var/www/html/images/* ~/environment/django/bicycle_app/static/
 Expected output:

None, unless there is an error.

To confirm that the files were copied over, expand the new static directory in the file browser panel. Note that there is no image subdirectory.

The following screen capture shows the expected file structure, but does not show all the files.

Screen capture shows some static directory contents.

Image description: Image shows the file tree view of the AWS Cloud9 file menu. It is highlighted on the static folder.

In the bicycle_app > templates > index.html file, add the following Django template language static template tag to the top of the file. It should appear above the <!DOCTYPE html> line.

```django
{% raw %}
{% load static %}
{% endraw %}
```

Still in index.html, edit the path to the CSS, the browser tab icon, and the company logo to use the {% raw %}{% static %}{% endraw %} template tag.

In the head section, update the path to the logo-black.png so that it matches this:

```django
{% raw %}
<link rel="icon" href="{% static 'logo-black.png' %}">
{% endraw %}
```

Still in the head section, also update the path to the CSS file so that it matches this:

```django
{% raw %}
<link rel="stylesheet" type="text/css" href="{% static 'css/main.css' %}">
{% endraw %}
```

Towards the top of the body section, in the banner div, modify the image source path for the logo-black.png so that the line looks like this:

```django
{% raw %}
<td><img src="{% static 'logo-black.png' %}"></td>
{% endraw %}
```

Save the changes.

If you return to the terminal where the runserver process is active, notice how it shows the following errors:


Not Found: /css/main.css
Not Found: /images/logo-black.png
Not Found: /images/cassette.jpeg
[28/Mar/2024 18:24:34] "GET /css/main.css HTTP/1.1" 404 2897
[28/Mar/2024 18:24:34] "GET /images/logo-black.png HTTP/1.1" 404 2924
[28/Mar/2024 18:24:34] "GET /images/cassette.jpeg HTTP/1.1" 404 2921
Not Found: /images/crank-arm.jpeg
[28/Mar/2024 18:24:34] "GET /images/crank-arm.jpeg HTTP/1.1" 404 2924
Not Found: /images/bell.jpeg
Not Found: /images/chain.jpeg
[28/Mar/2024 18:24:34] "GET /images/bell.jpeg HTTP/1.1" 404 2909
Not Found: /images/inner-tube.jpeg
[28/Mar/2024 18:24:34] "GET /images/chain.jpeg HTTP/1.1" 404 2912
Not Found: /images/gear-shifter.jpeg
[28/Mar/2024 18:24:34] "GET /images/inner-tube.jpeg HTTP/1.1" 404 2927
Not Found: /images/map.jpeg
[28/Mar/2024 18:24:34] "GET /images/gear-shifter.jpeg HTTP/1.1" 404 2933
[28/Mar/2024 18:24:34] "GET /images/map.jpeg HTTP/1.1" 404 2906
Not Found: /images/repair.jpeg
Not Found: /images/specialist.png
[28/Mar/2024 18:24:34] "GET /images/repair.jpeg HTTP/1.1" 404 2915
[28/Mar/2024 18:24:34] "GET /images/specialist.png HTTP/1.1" 404 2924
Not Found: /images/logo-black.png
[28/Mar/2024 18:24:47] "GET /images/logo-black.png HTTP/1.1" 404 2924
To address this, you restart the Django web server so that it is aware of the new static directory. To do this, perform the following:

Choose the terminal where the runserver process is active.

Press Ctrl+C to stop the server.

The terminal returns to the (.venv) prompt.

Press the up arrow key on your keyboard to reload the python manage.py runserver 0.0.0.0:8080 command (or manually type it in again). And then press Enter to start the runserver process again.

The terminal displays the usual message, indicating that the server is again running.


************************
**** EXAMPLE OUTPUT ****
************************
...
^C(.venv) AWSLabsUser-...:~/environment/django $ python manage.py runserver 0.0.0.0:8080
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
January 25, 2024 - 01:34:37
Django version 5.0.1, using settings 'bicycle_project.settings'
Starting development server at http://0.0.0.0:8080/
Quit the server with CONTROL-C.
Refresh the webpage.

Now it is starting to look better!

Update the index.html template further to adjust the source for only the following image files so that they also reference the static files:

map.jpeg
biking-outdoors.jpeg
repair.jpeg
specialist.png
The logo-white.png image referenced in the JavaScript
The logo-black.png image referenced in the JavaScript
 Caution: Do not update the references to images in the products table. You address that issue separately later.

If you need to see the corrected code for the six image references, choose here.
Line 108: {% raw %}<img src="{% static 'map.jpeg' %}" width="130px">{% endraw %}

Line 117: {% raw %}<img src="{% static 'biking-outdoors.jpeg' %}">{% endraw %}

Line 128: {% raw %}<img src="{% static 'repair.jpeg' %}" height="350">{% endraw %}

Line 148: {% raw %}<img src="{% static 'specialist.png' %}" height="130">{% endraw %}

Line 163: {% raw %}updateBanner("white", "black", "{% static 'logo-white.png' %}");{% endraw %}

Line 167: {% raw %}updateBanner("black", "white", "{% static 'logo-black.png' %}");{% endraw %}

Refresh the webpage again.

All the graphics except for those in the products table should now render correctly.

Current state of the website.

Image description: Image depicts the AnyCompany bicycle parts website where customers can browse bicycle parts, select quantities of items that they want to purchase, find store information, and learn more about the company. To review the detailed image description, expand the following section.

Detailed image description
Webpage header: At the top of the webpage, there are navigation tabs or links labeled Products, Services, Location, and About us. These are meant to navigate to different sections of the company’s website.
Main content – Products section: The main area of the page is dedicated to products. It has a bold title PRODUCTS and features a list of bicycle parts, each with an image place holder, a name, a price, and a field to enter a quantity for purchase. The following products are listed:

CASSETTE $50 with a quantity field set to 0
CRANKSET $215.00 with a quantity field set to 0
CHAIN $35.00 with a quantity field set to 0
BELL $18.00 with a quantity field set to 0
GEAR SHIFTER $32.00 with a quantity field set to 0
INNER TUBE $14.00 with a quantity field set to 0
Store Location section: To the right of the products is a section titled STORE LOCATION with a blue heading and grey background. It provides the store’s address, phone number, and operating hours:

Address: 100 Anywhere Street, Anytown, USA
Phone: 555-0100
Hours: Mon-Fri 7am-7pm, Sat 8am-6pm, Sun closed
Below this information is an image of a map and a button labeled Get directions, intended to help visitors find the store’s location with a map service.

Footer: Below the products, there is a Submit button, which is used to submit an order or inquiry form related to the selected products.

About Us section: Towards the bottom of the image, there’s a section ABOUT US, contains information about the company. It also includes an image of a bicyclist enjoying a mountain view with her arms raised high. Below this image are two buttons. One reads Light banner and the other reads "Dark banner*. The banner image changes to have a white or black background depending on which button is chosen.

Services: At the bottom of the image is the SERVICES section. It included an image of a bicycle, lists the services offered, and displays the Specialist Certified award. Below this is the copyright information.

Test the website functionality:

Hover over the top menu links. They still change color.
If your web browser is not already displaying the bottom of the page and you choose the Services link, the browser takes you down the page.
Choose the Light banner button. It still changes the top of the webpage to use black text and graphics on a white background.
Choose the Dark banner to swap the look of the banner back to white text on black background.
 Analysis: You now have all the static content of the AnyCompany bicycle parts website working and running on Django. (The parts of the website that do not have to make use of the data in the database all render correctly.)

 Task complete: In this task, you successfully loaded the website that you built in earlier labs in this course to review what it looked like. You then migrated the HTML, CSS, and image files into the Django app and confirmed that the static content renders.

Task 3: Create new templates
In this task, you continue improving the website by authoring new templates that can collect user data and render data from the database tables to the user.

Task 3.1: Create a products template
Next, you create a template to display the products order form.

In the templates directory, create a new file named products.html.

Open the products.html file in the file editor.

Return to the tab where you have the index.html file open, and select the entire products div (lines 28 to 89).

Choose Edit > Cut.

Return to the tab where the new empty products.html file is, and choose Edit > Paste.

Add the following additional lines to the top of the products.html file:

```django
{% raw %}
{% extends "index.html" %}
{% block content %}
{% endraw %}
```

Add the following additional line to the bottom of the products.html file:

```django
{% raw %}
{% endblock content %}
{% endraw %}
```

Delete everything inside the table element, and replace it with the following HTML code:

```html
<tr>
  product listings displays here
</tr>
```

Update the form start tag so that it matches what is shown here:

```html
<form action="order_result" method="POST" id="order_form"></a>
```

Add the csrf_token template tag just below the form start tag and above the table start tag.

```django
{% raw %}
{% csrf_token %}
{% endraw %}
```

Save the changes.

The products.html template file should now look like this:

```django
{% raw %}
{% extends "index.html" %}
{% block content %}
<div class="products" id="products-link">
    <h2>Products</h2>
    <form action="order_result" method="POST" id="order_form"></a>
        {% csrf_token %}
       
        <table>
            <tr>
                product listings displays here
            </tr>
        </table>
        
        <div class="submitform">
            <input type="submit" value="Submit">
        </div>
    </form>
</div>
{% endblock content %}
{% endraw %}
```

Return to the index.html file and add these lines where the products table used to be, just below the <!–product list goes here–> HTML comment:

```django
{% raw %}
{% block content %}
{% endblock content %}
{% endraw %}
```

Save the change.

The relevant section of the index.html Django template now looks like this:

Html code in index.html.

Image description: Image shows the html code for the index.html file that you have been editing.

Open views.py and in the index function, modify the return line so that it renders the products.html template instead of the index.html template.

Save the change to views.py

Refresh the webpage.

The webpage now renders with the product listings display here message displaying where the product table used to be.

Take a moment to understand what you just did!

 Analysis: You moved the products div into a separate HTML template. However, the index function defined in the views.py file still renders the page as if all the HTML code was contained in a single HTML file. Your index view is constructing a webpage from two templates, as illustrated in the following diagram. The extends template tag in the line {% extends “index.html” %} is what makes it work. You can read more about the extends tag in the Django Documentation.

Both templates also make use of the block tag, which is also an essential element of how Django implements template inheritance. The block tag is described in detail in the Django Documentation.

In the bicycle app implementation, the index.html page is acting as the main HTML document into which other templates that you define can insert additional HTML content.

Notice that the products.html template does not contain the usual <html><head>...</head><body>..</body></html> that you would find in a standard webpage. This is because, as shown in the following illustration, the contents of the products.html template get fed into another template that already contains those tags (index.html).

The part of your bicycle webpage that contained the order form will soon also be capable of rendering different content, such as order results, order history, or order details from a previous order.

At the moment, the index view is not inserting data retrieved from the model into the products template, but you adjust it to do that next.

Workflow.

Image description: See details before this image for a thorough description.

Task 3.2: Create a loop to render product data in the HTML form
Update the products template to read data from the context object into the HTML form.

Return to the products.html in the file editor.

Replace the product listings displays here text with the following code:

```django
{% raw %}
{% for i in <FMI-1> %}
    {% if forloop.counter0|divisibleby:3 %}
        </tr>
        <tr>
    {% endif %}
    <td>
        <img src="static/{{ i.image_url.url }}" width="100" />
        <p><FMI-2> $<FMI-3><br>
            <input type="hidden" name="product_name" value="{{ i.product_name }}">
            <input type="hidden" name="product_id" value="{{ i.id }}">
            <input type="hidden" name="amount" value="{{ i.price }}">
            <label>Quantity: </label>
            <input type="number" name="quantity" value="0" min="0" max="4">
        </p>
    </td>
{% endfor %}
{% endraw %}
```

Replace the three fill me in (FMI) placeholders so that the for loop iterates through the object passed to the products template by the index view.

 Tip: Analyze the context object contents in the view.py code. The paragraph element displays the name of the product and the price of the product to the web app user.

Save the changes.

If you need to see the solution code for the products.html file, choose here.

```django
{% raw %}
{% extends "index.html" %}
{% block content %}
<div class="products" id="products-link">
    <h2>Products</h2>
    <form action="order_result" method="POST" id="order_form"></a>
        {% csrf_token %}
       
        <table>
            <tr>
                {% for i in product_items %}
                    {% if forloop.counter0|divisibleby:3 %}
                        </tr>
                        <tr>
                    {% endif %}
                    <td>
                        <img src="static/{{ i.image_url.url }}" width="100" />
                        <p>{{ i.product_name }} ${{ i.price }}<br>
                            <input type="hidden" name="product_name" value="{{ i.product_name }}">
                            <input type="hidden" name="product_id" value="{{ i.id }}">
                            <input type="hidden" name="amount" value="{{ i.price }}">
                            <label>Quantity: </label>
                            <input type="number" name="quantity" value="0" min="0" max="4">
                        </p>
                    </td>
                {% endfor %}
            </tr>
        </table>
        
        <div class="submitform">
            <input type="submit" value="Submit">
        </div>
    </form>
</div>
{% endblock content %}
{% endraw %}
```

Reload the webpage.

With just a few lines of code in your template, the webpage is now displaying the entire product catalog. Take a moment to revel in the moment!

AnyCompany bicycle parts website rendering products correctly.

Image description: Image shows that the Products section of the website now shows all products in the catalog.

View the page source of the webpage and compare it to the products.html template. To do this, follow these steps:

In the webpage where the AnyCompany website is loaded, right-click anywhere in the page and choose View page source from the context menu.

Arrange your browser tabs so that you can see both the page source and the products.html file that you have open in the AWS Cloud9 file editor.

The screen capture here shows the template on left and the page source on right. This might be difficult to view in the instructions, so the better approach is to re-create this view on your screen using your live environment.

Screen capture with template on left and page source on right.

Image description: Image shows the template on the left side and the page source on the right, which has additional code base on the CSS.

 Analysis: Notice how the Django template language template tags were used to render the Product model (table) data into the webpage. The template iterates through the items (i) contained in the product_items object, which was passed to the template by the view.

After every three iterations through the for loop, a table row end tag </tr> and new table row start tag <tr> are written out. This makes it so that each row in the table will have no more than three columns in it. Those table columns, defined in the <td> elements, contain the values from the Order model.

Not all the values inserted into the form are actually presented to the end user. In fact, many of these values are injected into input elements that are hidden from the user. However, their presence in the form (as you can see in the browser page source) is important, because when the web app user submits the form, those values, such as the product id, will be submitted along with the form.

To ensure that the user can easily return to the products page at any time, open the index.html template and update the Products menu hyperlink in the nav-menu div so that it matches this:

```django
{% raw %}
<a href="{% url 'index' %}">Products</a>
{% endraw %}
```

 Tip: You can learn more about the url template variable in the Django Documentation.

Save the change, refresh the webpage, and test the link Products menu link.

The webpage should again load.

Task 3.3: Create an order results template
Although the main webpage now properly displays the order form, the template to present order results back to the user has not yet been created. You create that now.

In the templates directory, create a new file named order_result.html.

Open the new file in the file editor and paste in the following code:

```django
{% raw %}
{% extends "index.html" %}
{% block content %}

<div class="products">
    <h2>Order confirmation</h2>
    <div class="order-details">
        <p>Your order details</p>
        <div class="order_summary">
        <table>
            <tr>
               <td colspan="2"><p>Order summary</p></td> 
            </tr>
            <tr>
                <td>Order number:</td>
                <td>{{ order.id }}</td>
            </tr>
            <tr>
                <td>Order time:</td>
                <td>{{ order.order_date_time }}</td>
            </tr>
            <tr>
                <td>Total amount:</td>
                <td>${{ order.amount }}</td>
            </tr>
        </table>
        &nbsp;
        &nbsp;
        <table>

            <tr>
               <td colspan="3"><p>Order line items</p></td> 
            </tr>  
            <tr>
                <td>Product ID</td>
                <td>Quantity</td>
                <td>Cost</td>
            </tr>
            {% for i in order_details %}
            <tr>
                <td>{{ i.product_id}}</td>
                <td>{{ i.quantity }}</td>
                <td>${{ i.amount }}</td>
            </tr>
            {% endfor %}
        </table>
        </div>
    </div>
</div>

{% endblock content %}
{% endraw %}
```

Update two lines of code in views.py.

Open views.py in the file editor.

Scroll to the bottom of the process_order function and comment out this line:


#return HttpResponse('/order_result page loaded. Check the runserver console for test result.') 
Look for the return line of code a few lines earlier in the file, and uncomment it:


return render(request, "order_result.html", context)
Also, towards the top of the file, under from django.template import loader, add this new import line:


from django.core.exceptions import ValidationError
Save the changes.

Add additional HTML styling to main.css.

Open django > bicycle_app > static > css > main.css in the file editor.

After the .products tr selector code (around line 67), add the following two class selectors code:

```css
.order-details {
    padding-left: 15px;
    padding-right:15px;
}
.order_summary {
    table {
        width: 100%;
    }
    td { 
        text-align: left; 
        padding-right: 4px;
    }
    td:nth-child(2) { 
        text-align: left; 
        padding-left: 4px;
    }
    td colspan {
        text-align: left;
    }
    tr:nth-child(even) {
        background-color: #f2f2f2;
    }
    color: black;
}
```

 Note: The order_results.html template includes div elements that reference these css classes, so the styles defined here are used in the test that you conduct in the next step.

Save the changes.

Return to the https://…vfs.cloud9.us-west-2.amazonaws.com/ webpage and choose the Submit button to submit a new order.

This time you should see an order confirmation page.

Order confirmation page.

Image description: Image shows an order confirmation for two products that were ordered.

If you see the page as shown in this example image, congratulations!

Now you are really starting to see how Django lets you extend the functionality of your website well beyond what you were able to accomplish when using only HTML, CSS, and JavaScript.

Task 3.4: Create an order history template
The last remaining template to create is the order history template. You do that now.

In the templates directory, create a new file named order_history.html.

Open the new file in the file editor, and paste in the following code:

```django
{% raw %}
<FMI-1>
<FMI-2>
<div class="products">
    <div class="order-details">
        <div class="order_summary">
        <h2>Order history</h2>
        <table>
            <tr>
               <td><p>Order number</p></td>
               <td><p>Order time</p></td>
               <td><p>Total amount</p></td>
               <td><p>Details</p></td>
            </tr>
            {% for order in orders %}
            <tr>
                <td>{{ order.id }}</td>
                <td>{{ order.order_date_time }}</td>
                <td>${{ order.amount }}</td>
                <td><a href="">Order details</a></td>
            </tr>
            <FMI-3>
        </table>
        </div>
    </div>
</div>
{% endblock content %}
{% endraw %}
```

Replace the FMI placeholders in the code that you pasted in, to achieve the following:

The extends template tag is used to implement template inheritance so that the order_history template renders as a block inside of the index.html template.

A block tag to surround the other template tags so that Django replaces the tags with content retrieved from the Order model.

You indicate to Django where the for loop logic should end in the template.

If you need to see the order_results.html file solution code, choose here.

```django
{% raw %}
{% extends "index.html" %}
{% block content %}

<div class="products">
    <h2>Order confirmation</h2>
    <div class="order-details">
        <p>Your order details</p>
        <div class="order_summary">
        <table>
            <tr>
               <td colspan="2"><p>Order summary</p></td> 
            </tr>
            <tr>
                <td>Order number:</td>
                <td>{{ order.id }}</td>
            </tr>
            <tr>
                <td>Order time:</td>
                <td>{{ order.order_date_time }}</td>
            </tr>
            <tr>
                <td>Total amount:</td>
                <td>${{ order.amount }}</td>
            </tr>
        </table>
        &nbsp;
        &nbsp;
        <table>
            
            <tr>
               <td colspan="3"><p>Order line items</p></td> 
            </tr>  
            <tr>
                <td>Product ID</td>
                <td>Quantity</td>
                <td>Cost</td>
            </tr>
            {% for i in order_details %}
            <tr>
                <td>{{ i.product_id}}</td>
                <td>{{ i.quantity }}</td>
                <td>${{ i.amount }}</td>
            </tr>
            {% endfor %}
        </table>
        </div>
    </div>
</div>

{% endblock content %}
{% endraw %}
```

Update three lines of code in views.py.

Open views.py in the file editor.

Locate the all_orders function and comment out the hardcoded HttpResponse line:


#return HttpResponse('/order_history page loaded. Check the runserver console for test result.')  
Look for the two lines of code just below that and uncomment them:


context = {'orders': orders}
return render(request, "order_history.html", context)
Save the changes.

Add an Order History link to the webpage menu.

Open the index.html template and in the nav-menu div, add the following new hyperlink just below the 
line:

```django
{% raw %}
<a href=“{% url ‘index’ %}”>Products</a>
<a href="{% url 'all_orders' %}">Order history</a>
{% endraw %}
```

Save the change.

Adjust the CSS to account for the new link by following these steps:

Open the static > css > main.css file in the file editor.
In the .nav-menu a selector details, modify the width attribute so that it is set to 20%.
 Note: Does this make sense? You previously had four menu items, now you have five.

Save the change.

Refresh the main webpage at your unique https://…vfs.cloud9.us-west-2.amazonaws.com/ URL.

Choose the new Order history link.

A list of all orders should now display.

Order history webpage.

Image description: Image shows the AnyCompany bicycle parts website opened to an Order History page with order details including order number, order time, total amount, and details.

Congratulations! You now have three different views working!

If you need to see the order_history.html file solution code, choose here.

```django
{% raw %}
{% extends "index.html" %}
{% block content %}
<div class="products">
    <div class="order-details">
        <div class="order_summary">
        <h2>Order history</h2>
        <table>
            <tr>
               <td><p>Order number</p></td>
               <td><p>Order time</p></td>
               <td><p>Total amount</p></td>
               <td><p>Details</p></td>
            </tr>
            {% for order in orders %}
            <tr>
                <td>{{ order.id }}</td>
                <td>{{ order.order_date_time }}</td>
                <td>${{ order.amount }}</td>
                <td><a href="">Order details</a></td>
            </tr>
            {% endfor %}
        </table>
        </div>
    </div>
</div>
{% endblock content %}
{% endraw %}
```

Task 3.5: Implement lookup order
You might have noticed that the order_history.html file does not yet provide a functioning hyperlink to the order details for each order that it lists. You implement that last bit of logic next.

Open views.py in the text editor and locate the lookup_order function.

Delete the current function and instead paste in the following code:

```python
def lookup_order(request, order_id):
    print('LOG: in "lookup_order" function')
    order_id=int(order_id)
    order = list(Order.objects.filter(id=order_id).values())
    order_data = {
        "id": order[0]['id'],
        "order_date_time": order[0]['order_date_time'],
        "amount": order[0]['amount']
    }
    print('LOG: this is the order' + str(order_data))

    items = Order_Item.objects.filter(order_number=order_id).values() 
    context = {'order_details': items, 'order': order_data}
    return render(request, "order_result.html", context)
```

Save the changes.

Open the order_history.html file in the text editor and update the <td><a href="">Order details</a></td> line so that it now includes a destination value.

```django
{% raw %}
<td><a href="{% url 'lookup_order' order.id %}">Order details</a></td>
{% endraw %}
```

Save the change.

 Task complete: In this task, you improved the website by authoring new templates that can collect user data and render data from the database tables to the user.

Task 4: Test the completed web app
In this task, you conduct a final test of the completed Model-View-Template Django logic that you have implemented in your web app.

Load the base webpage at your unique https://…vfs.cloud9.us-west-2.amazonaws.com/ URL.

Test placing an order with no quantities selected.

A pop up warning displays, indicating that you need to order at least one product.

Test placing an order where you choose a quantity of one or more for at least two products.

After you submit the order, an order confirmation page displays with the order and order item details presented back to the user.

Choose the Order history link.

An Order history page displays all previous orders. Each order has an Order details link available.

Choose one of the Order details links.

The same order_result template that is used to display order results when placing a new order is also used to display order details for prior orders. The order line item details that were not presented on the Order history page can be seen in this detailed view.

Lab files
The lab environment is ephemeral. All the lab resources are deleted when the lab time expires. If you want to keep a copy of the lab code, you can download all the lab code using the AWS Cloud9 environment.

To save the files on your local computer, in the AWS Cloud9 menu bar, choose File, and then choose Download Project.
 Task complete: In this task, you conducted a final test of the completed Model-View-Template Django logic that you implemented in your web app.

Conclusion
You have successfully done the following:

Created a template in Django
Used the Django template language to display Django model date to a user
Configured static assets, such as images and CSS, to display in a Django template
Created a Django template that extends another template
Used a url Django template tag to invoke a Django view to display order details
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End Lab and then confirm that you want to end your lab.

For more information about AWS Training and Certification, see https://aws.amazon.com/training/.

Your feedback is welcome and appreciated.
If you would like to share any feedback, suggestions, or corrections, please provide the details in our AWS Training and Certification Contact Form.

Django is property of the Django Software Foundation, JavaScript is a trademark of Oracle Corporation, and Python is property of the Python Software Foundation (PSF). Reference in this lab to any specific commercial product, process, or service, or the use of any trade, firm or corporation name is provided for informational purposes, and does not constitute endorsement, recommendation, or favoring by Amazon Web Services.