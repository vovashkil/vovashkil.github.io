# Creating Views in a Web Framework

## Lab overview

This is the third in a series of labs that have you working with Django, a Python web framework that helps you avoid extra coding and helps you build websites that are scalable and maintainable. In the first Django lab, you installed the Django web framework in a Python virtual environment and then created a basic Django project with a hello world web app running in it. In the second lab, you configured Django to use MySQL as the database, and defined models for the bicycle supplies web app.

In this lab, you create views in Django to handle the web app logic that eventually makes it possible for users to do the following:

Load the main webpage that displays the bicycle supplies web app product order form
Place an order and view an order confirmation
View order history
View line item details for any previous order
Objectives
By the end of this lab, you should be able to do the following:

Create a view in Django that pulls data from a database and displays it on a webpage.
Create a view that filters database results to return requested detail.
Create a view that inserts new records into multiple database tables.
Add URL patterns for Django to handle requests and route users to different URLs as appropriate.
Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Caution: Information of special interest or importance (not so important to cause problems with the equipment or data if you miss it, but it could result in the need to repeat certain steps).
 Command: A command that you must run.
 Consider: A moment to pause to consider how you might apply a concept in your own environment or to initiate a conversation about the topic at hand.
 Expected output: A sample output that you can use to verify the output of a command or edited file.
 Hint: A hint to a question or challenge.
 Learn more: Where to find more information.
 Note: A hint, tip, or important guidance.
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

Image description: The diagram illustrates a web developer using the AWS Cloud infrastructure. The web developer is accessing an AWS Cloud9 IDE which is hosted on an Amazon Elastic Compute Cloud (Amazon EC2) instance running Ubuntu as the guest operating system. A security group acts as a firewall to control access to the EC2 instance. For more information, refer to the following detailed diagram overview.

Detailed diagram overview
The diagram illustrates an AWS infrastructure setup that includes various components arranged hierarchically. Starting from the outermost layer moving inward, the components are as follows:

AWS Cloud: This is the outermost boundary, indicating that all the subsequent components are hosted within the AWS Cloud environment.
Lab VPC: In the AWS Cloud, there is a virtual private cloud (VPC) designated as Lab VPC. The VPC is a virtual network dedicated to your AWS account. It is isolated from other virtual networks.
Public subnet: In the Lab VPC, there’s a public subnet. This is a segment of the VPC where resources can be accessed from the internet. It implies that resources in this subnet can send and receive traffic directly from the internet.
Security group: The next layer represents a security group. It acts as a virtual firewall that controls the inbound and outbound traffic for resources it’s associated with. In this architecture, the security group is associated with the Amazon Elastic Compute Cloud (Amazon EC2) instance. The security group ensures that only specified traffic can reach the EC2 instance.
Amazon EC2 instance: At the core, within the security group boundary, there’s an EC2 instance, which is symbolized by the EC2 instance group icon. An EC2 instance is a virtual server in Amazon EC2 used to run applications on the AWS infrastructure. Inside the EC2 instance, the following components are detailed:
AWS Cloud9 IDE: The AWS Cloud9 integrated development environment (IDE) is represented by the AWS Cloud9 IDE resource icon. This suggests that the AWS Cloud9 service is being used for development purposes on this EC2 instance.
Ubuntu guest operating system: The EC2 instance is running the Ubuntu operating system.
You: On the left side, outside the AWS Cloud, there is an icon of a person labeled You. This represents the developer who interacts with the AWS Cloud and, specifically, with the EC2 instance, possibly using the AWS Cloud9 IDE for developing websites.
AWS services used in this lab
AWS Cloud9
Amazon Elastic Compute Cloud (Amazon EC2)
AWS services not used in this lab
AWS service capabilities used in this lab are limited to what the lab requires. Expect errors when accessing other services or performing actions beyond those provided in this lab guide.

Task 1: Run the script to configure the development environment
In this first task, you run a script that installs the Django framework on your Ubuntu Linux instance and gets your environment to match the end state of the previous lab.

Task 1.1: Connect to the IDE and run the setup script
Start by connecting to the AWS Cloud9 integrated development environment (IDE) and running scripts to configure the environment to match the environment that you had at the end of the previous lab.

Copy the Cloud9Environment URL value that is listed to the left of these instructions, and paste it into a new browser tab. It connects you to the AWS Cloud9 IDE.

 Command: In the AWS Cloud9 IDE terminal window, run the following command:


./setup.sh
The shell script completes configurations on the Amazon EC2 instance on which your AWS Cloud9 IDE is installed. The configuration replicates the steps that you completed in the previous lab: installing a Python virtual environment, installing Django, creating the bicycle_project Django project, and creating the bicycle_app Django app.

 Caution: If you receive a prompt asking which services should be restarted, use your Tab key to select Ok and press the Enter key so that the script continues running.

 Expected output: Output has been truncated.


...
Successfully installed cffi-1.16.0 cryptography-42.0.2  pillow-10.2.0 pycparser-2.21 pymysql-1.1.0
restore bicycles database
delete product table contents
reset auto_increment on product table
create the django user
 Command: To activate the Python virtual environment and start the Django web server, run the following commands:


cd ~/environment/django
source .venv/bin/activate
python manage.py runserver 0.0.0.0:8080
 Expected output:


Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
February 07, 2024 - 22:10:13
Django version 5.0.2, using settings 'bicycle_project.settings'
Starting development server at http://0.0.0.0:8080/
Quit the server with CONTROL-C.
 Caution: The web server only remains running while you keep the process active in the terminal. Leave this terminal as it is. Note that debug and log information is written to this terminal’s output as you progress through the lab.

To add product data to the product table and test data to the order and order_details tables, do the following:

Open a second terminal window in AWS Cloud9.

 Command: In the new terminal, run the following:


cd ~/environment/django
source .venv/bin/activate
python manage.py loaddata /home/ubuntu/environment/products.json
python manage.py loaddata /home/ubuntu/environment/orders.json
python manage.py loaddata /home/ubuntu/environment/order_details.json
 Expected output:


Installed 12 object(s) from 1 fixture(s)

Installed 1 object(s) from 1 fixture(s)

Installed 2 object(s) from 1 fixture(s)
The output from the last three commands should indicate that objects were installed.

 Note: If you are interested in seeing the data that you just inserted in the database, open the products.json, orders.json, and order_details.json files in the AWS Cloud9 file editor.

Later, your web app creates similar rows of data dynamically when customers place orders. However for now, this test data helps you test the views that you create next, which pull data from these tables.

Leave this terminal open. You return to it much later in this lab.

Task 1.2: Confirm that the app is running
Continue by confirming that the bicycle app is running, and then review what still needs to be built.

Choose the terminal tab where you have the runserver process running.

Choose the link in the Cloud9 Help dialog box. The dialog box should appear in the corner of the terminal.

A new browser tab opens and displays the webpage. It matches what you configured in the previous lab.

Prior lab web app progress page.

Image description: Image shows in bold text “Hello from bicycle_app” and then has an unordered list of bicycle parts with prices next to them.

 Caution: You can get to the same preview page at any time by choosing Preview > Preview Running Application, and then in the preview panel choose the pop-out into new window icon to open the preview in a new browser tab.

Keep this browser tab open for the duration of this lab. You return to it later.

Understanding the work to be done
Recall that Django uses a Model View Template architecture. In the previous lab, you defined three models for the bicycle supplies website: Product, Order, and Order_Item. You also defined a very basic view and a basic template.

In this lab, you significantly improve the view logic to accomplish the following:

Retrieve all orders from the order table.
Retrieve the details for a particular existing order.
Present a mock test order form to website users.
Record orders placed with the test order form into the Order and Order_Item tables.
You have seen this summary in the previous lab, but it is presented here again to review if it is helpful. The design that you accomplish is illustrated in the following diagram. Here is an explanation of each labeled step:

Step 1: Your browser makes a request to load the URL

Step 2: Django consults the URL patterns defined in urls.py to know where to route the request.

Step 3: A function written in Python in the views.py file is invoked. It contains the application logic.

Step 4: The view logic typically runs a SQL query by using the included model to look up data or modify or insert data. A dataset from the database is returned to the view.

Step 5: To build the response, the view logic typically loads an HTML template and then injects data from the dataset into it.

Step 6: Finally, the view logic returns the response, which might render the same page to display data from the dataset, or the view logic might redirect the user to a different webpage that makes use of a different template to display dataset results.

Model-view-template data flow.

Image description: Image depicts the logic using six steps, as explained before the image.

Functionality overview
The following table summarizes the functionality of the view functions that you create in this lab and what the templates that you create in the next lab must achieve.

The heading of each column in the table describes what an end user might want to do. For each action that a user might take, they start at a page that must first load. After the page loads, the user takes an action, such as submitting an order or choosing a link to view details.

As you work on this lab, you might find this table helpful to refer back to.

Load the main page	Place an order and view order confirmation	View order history	View line item details for a prior order
Start URL	n/a	/	/
or /order_result	/order_history
Start page - template to render	n/a	products.html	products.html or order_result.html	order_history.html
Start description	User wants to see the website,
tries to load the main page.	From the main page (already
loaded), user places an order by
selecting a quantity of at least
one for at least one product
and choosing Submit.	From any page on the website,
the user could choose the Order
history link, which appears in
the site menu.	From the order history page, a
user wants to see order line item
details for a particular order.
They choose the Order details link
for a particular order.
HTTP request method	GET	POST	GET	GET
View function invoked	index	process_order	all_orders	lookup_order
Models queried	Products	Order, Order_Item	Order	Order, Order_Item
Query type	SELECT	INSERT	SELECT	SELECT
End URL	/	/order_result	/order_history	/order_result
End page - template to render	products.html	order_result.html	order_history.html	order_result.html
End description	User sees main page,
could place an order.	After placing order from the
main page, the user sees
an order confirmation
with order summary and
order line item details.	User sees a listing of all orders
they have ever placed on the
website, one row for each order.
Each row contains a link to
view the order details.	The line item details are displayed
for the prior order for which
the user requested details.
Recall from the JavaScript lab earlier, some user actions can be handled on the client side, without the need to make a request over the network. For example, the JavaScript form validator that you added to the website checks if the user selected to order at least one product, before allowing the order to be submitted.

However, many user actions, including all those listed in this table, require invoking an HTTP request. If the request is simply to load a static web page, no view logic is required. However, inserting records in a database or retrieving records from a database requires you to author web application logic to handle the request. For the AnyCompany bicycle supplies app that you are preparing to host on Django, you author that logic in Python in the views.py file.

In this lab, you create each of the four view functions described in the table. Then in the next lab, you create the templates that the views use to render data to and collect data from the end users.

 Task complete: In this task, you successfully ran a script that installed the Django framework on your Ubuntu Linux instance and you further configured the environment to match the end state of the previous lab.

Task 2: Create views that require data lookups
In this task, you create the views (index, all_orders, and lookup_order) that require data lookups but no data inserts.

Task 2.1: Create the index view
Start this task by creating a view that can return data from the Product model.

In this task, you create the index view that can eventually be used to load the products order form that displays on the AnyCompany bicycle supplies main page.

Before using Django, you created the content that displays in the Products area of the page by hardcoding the names of the products in the HTML, like this:


<form method="POST">
<table>
  <tr>
     <td>
        <img src="images/cassette.jpeg">
        <p>Cassette $50
          <br>
          <label for="cassette_qty">Quantity: </label>
          <input type="number" id="cassette_qty" name="cassette_qty" min="0" max="4" value="0">
        </p>
     </td>
...(truncated)
For each product, you had to update the HTML file to add the product details. The resulting section webpage looked like this:

Products div from main webpage.

Image description: Image shows the bicycle parts website Products section. It is a listing of product images, descriptions, prices, and quantity wrapped in an HTML form element that contains input elements for each product.

Now that you are using Django, and these product details are in the database, you can read the details such as the product name, price, and image file name out of the database dynamically, and then use those details to present the page to the user. This is a more scalable way to maintain the webpage than continuing to hardcode the product details into the HTML document.

Here is the structure of the Product database table that you created in the previous lab:


mysql> describe bicycle_app_product;
+---------------+--------------+------+-----+---------+-------+
| Field         | Type         | Null | Key | Default | Extra |
+---------------+--------------+------+-----+---------+-------+
| id            | int          | NO   | PRI | NULL    |       |
| product_name  | varchar(255) | NO   |     | NULL    |       |
| description   | varchar(255) | NO   |     | NULL    |       |
| price         | decimal(8,2) | NO   |     | NULL    |       |
| product_group | int          | NO   |     | NULL    |       |
| image_url     | varchar(255) | NO   |     | NULL    |       |
+---------------+--------------+------+-----+---------+-------+
Now that you have reviewed these details, it’s time to create the view.

Navigate to the django > bicycle_app directory and open views.py in the AWS Cloud9 file editor.

Delete the existing contents of the file, and then paste in the following code:


from django.shortcuts import render                            
from django.http import HttpResponse                           
from .models import Product             
from django.template import loader                     

import json
import pprint                                     
from django.core import serializers

def index(request):
    print('\n***LOG: in "index" function')
    product_items = Product.objects.all()

    #The 4 lines below used during VIEW TESTING 
    jsondata = serializers.serialize('json', product_items)  
    json_to_runserver = json.loads(jsondata)
    pprint.pprint(json_to_runserver)
    return HttpResponse('/ page loaded. Check the runserver console for test result.')
 Consider: Take a moment to observe what the index function does.

The import statements import all the necessary resources, including HttpResponse and the Product model.
The index function is invoked when a user requests the webpage. This routing logic is defined in the bicycle_app > urls.py file and was configured in an earlier lab.
The line product_items = Product.objects.all() accesses the database using the Product model and returns the contents of the Product database table. The JSON-formatted data is stored in a variable named product_items.
The next three lines of code serialize the JSON, parse it into a Python dictionary, and then pretty-print the content to the terminal where the runserver process is active, so that you can see the data content.
The return HttpResponse line simply hardcodes a response to the browser to avoid an error page.
Save the changes.

Refresh the webpage.

 Note: The webpage now displays the hardcoded response.

Hardcoded browser reply.

Image description: The image shows a webpage with the following line of text, “/ page loaded. Check the runserver console for test result.”

In the AWS Cloud9 IDE, look in the terminal where the runserver command is still running.

 Expected output: The output should look similar to the following:


...
{'fields': {'description': 'stop quickly when necessary',
             'image_url': 'hydraulic-brake.jpeg',
             'price': '69.00',
             'product_group': 4,
             'product_name': 'hydraulic brake'},
  'model': 'bicycle_app.product',
  'pk': 11},
 {'fields': {'description': 'wanna look cool?',
             'image_url': 'sports-glasses.jpeg',
             'price': '129.00',
             'product_group': 2,
             'product_name': 'sports glasses'},
  'model': 'bicycle_app.product',
  'pk': 12}]
[12/Jan/2024 19:55:16] "GET / HTTP/1.1" 200 44
You can see in the runserver terminal output that all the data in the product_items object is available. This provides the data that you need to display an order form to the user later.

Task 2.2: Create the all_orders view
Continue by creating a view that can display the history of all orders for the AnyCompany bicycle supplies web app. This view must return all the data from the Order table to the user.

In views.py, start creating a function name all_orders by adding these two lines to the bottom of the file:


def all_orders(request):
    print('\n***LOG: in "all_orders" function')
Save the change.

In bicycle_app > urls.py, add the following new line to the urlpatterns list:


path("order_history", views.all_orders, name="all_orders"),
Now if someone tries to load the https://…vfs.cloud9.us-west-2.amazonaws.com/order_history URL, Django runs the logic defined in the all_orders function defined in views.py. However, loading that URL now would show an error, because you have not yet defined all of the needed all_orders function logic yet. You do that next.

In your views.py code, update the from .models import line so that it also imports the Order model.

Author the all_orders view logic.

 Hint: Refer to the index function that you created earlier in this lab when defining the all_orders function logic. The end result should include the same number of lines that accomplish a similar objective. But in this case, you are pulling data from a different model.

The function should accomplish the following:

Capture all rows of the Order table into a variable named orders.
Serialize the data and pretty-print it to the console.
Return a static message as an HttpResponse to the /order_history page, indicating that the order_history page loaded and that testers should check the runserver console for test results.
Add the following commented-out code at the bottom of the function that can later be uncommented when you have an order_history.html template in which to display the content:

```python
#The 2 lines below is uncommented in the next lab
#context = {'orders': orders}
#return render(request, "order_history.html", context)
If you need help, choose here to see the coded solution for the all_orders function.

...
from .models import Product, Order #now includes Order
...
def all_orders(request):
    print('\n***LOG: in "all_orders" function')
    orders = Order.objects.all() 

    #The 4 lines below used during VIEW TESTING 
    jsondata = serializers.serialize('json', orders)  
    json_to_runserver = json.loads(jsondata)
    pprint.pprint(json_to_runserver)
    return HttpResponse('/order_history page loaded. Check the runserver console for test result.') 

    #The 2 lines below are uncommented in the next lab
    #context = {'orders': orders}
    #return render(request, "order_history.html", context)
```

Save the change and load the webpage. To load the page, you need to add /order_history to the end of the preview URL.

 Note: If you authored the code correctly, the webpage displays the hardcoded response.

Hardcoded browser reply.

Image description: The image shows a webpage with the following line of text, “/order_history page loaded. Check the runserver console for test result.”

 Expected output: In the terminal where the runserver command is still running, the output should look similar to the following:


...
***LOG: in "all_orders" function
[{'fields': {'amount': '88.00', 'order_date_time': '2024-01-29T19:16:32.615Z'},
  'model': 'bicycle_app.order',
  'pk': 1}]
[29/Jan/2024 19:20:32] "GET /order_history HTTP/1.1" 200 72
This shows that your view is retrieving all the orders in the Order table.

Task 2.3: Create the lookup_order view
Further build out the solution by creating a third view for the AnyCompany bicycle supplies web app. This view must return the order details data from the Order_Item table whenever someone requests the order details based on a given order ID.

Start creating a function name lookup_order in views.py by adding these two lines to the bottom of the file:


def lookup_order(request):
    print('\n***LOG: in "lookup_order" function')
Save the change.

In bicycle_app > urls.py, add the following new line to the urlpatterns list:


path("lookup_order/<str:order_id>", views.lookup_order, name="lookup_order"),
This makes it so that if someone chooses a link to load details for a previous order by using the https://…vfs.cloud9.us-west-2.amazonaws.com/lookup_order/<str:order_id> URL, where <str:order_id> is an existing order ID, Django runs the logic defined in the lookup_order function defined in views.py.

In your views.py code, update the from .models import line so that it also imports the Order_Item model.

Next, update the lookup_order view logic to accomplish the following:

Receive an order_id object in addition to the request object.
Capture order objects to a variable named order. Use a filter so that only results where the ID matches the order_id are returned by the request.
 Learn more: The Django documentation discusses how to author filters.

If you need to see how to do this, choose here to see an example of that line of code:

order = Order.objects.filter(id=order_id)
Serialize the data and pretty-print it to the console.

Return a static message as an HttpResponse to the /lookup_order page, indicating that the lookup_order page loaded and that testers should check the runserver console for test results.

Add the following commented-out code at the bottom of the function that can later be uncommented when you have an order_history.html template in which to display the order details:


#The 3 lines below is uncommented in the next lab
#items = Order_Item.objects.filter(order_number=order_id).values() 
#context = {'order_details': items, 'order': order}
#return render(request, "order_result.html", context)
 Hint: Refer to the all_orders function that you coded earlier when creating this lookup_orders function. The end result should include the same number of lines that accomplish a similar objective, but in this case you are filtering the data returned by the Order model.

If you need help, choose here to see the coded solution for the lookup_order function

from .models import Product, Order, Order_Item #now includes Order_Item
....
def lookup_order(request, order_id):
    print('\n***LOG: in "lookup_order" function')
    order = Order.objects.filter(id=order_id)

    #The 4 lines below used during VIEW TESTING 
    jsondata = serializers.serialize('json', order)  
    json_to_runserver = json.loads(jsondata)
    pprint.pprint(json_to_runserver)
    return HttpResponse('/lookup_order page loaded. Check the runserver console for test result.')
    
    #The 3 lines below are uncommented in the next lab
    #items = Order_Item.objects.filter(order_number=order_id).values() 
    #context = {'order_details': items, 'order': order}
    #return render(request, "order_result.html", context)
Save the change and test loading the webpage for an order ID that exists. To load the page, you need to add /lookup_order/1 to the end of the preview URL.

 Note: If you authored the code correctly, the webpage displays the hardcoded response.

Hardcoded browser reply.

Image description: The image shows a webpage with the following line of text, “/lookup_order page loaded. Check the runserver console for test result.”

 Expected output: In the terminal where the runserver command is still running, the output should look similar to the following:


...
***LOG: in "lookup_order" function
[{'fields': {'amount': '88.00', 'order_date_time':  '2024-01-30T17:41:16.865Z'},
  'model': 'bicycle_app.order',
  'pk': 1}]
 [30/Jan/2024 17:58:17] "GET /lookup_order/1 HTTP/1.1" 200 71
Now test again for an order ID that does not yet exist (for example, load the /lookup_order/2 URL).

The hardcoded HTTP Response to the browser should remain the same, but this time the result set displayed in the runserver terminal is blank.

 Expected output:


...
***LOG: in "lookup_order" function
[]
[30/Jan/2024 17:58:47] "GET /lookup_order/2 HTTP/1.1" 200 71
This shows that the object filter that you authored is working correctly.

Congratulations! You have created three of the four views that you need to build in this lab.

 Task complete: In this task, you successfully created the views (index, all_orders, and lookup_order) that require data lookups.

Task 3: Create the process_order view
The views that you created so far were all similar in that they all required retrieving data from the database. In this task, you create the process_order view, which requires gathering information from the end user and inserting it into the Order and Order_Item database tables.

Task 3.1: Update settings.py
Start the task by updating the Django project settings.

Open bicycle_project > settings.py in the file editor.

Add the following line just below the ALLOWED_HOSTS line:


CSRF_TRUSTED_ORIGINS = ['https://*.amazonaws.com', 'http://127.0.0.1', 'http://localhost']
 Note: This sets the domains from which you want to allow HTTP POST requests. CSRF stands for Cross Site Request Forgery. If interested, you can read more about CSRF in the Django documentation.

Save the change and close the file.

Task 3.2: Create an HTML file to test submitting orders
Continue the task by creating a mock order form that can be used for testing.

In the bicycle_app > templates directory, create a new file named test_form.html.

Open it in the file editor and paste in the following HTML:

```django
{% raw %}
<h2>Test page for submitting form data</h2>
<form action="order_result" method="POST">
    {% csrf_token %} 

   <p>Product: {{ product_items.0.product_name }}</p>

   <input type="hidden" name="product_name"  value="cassette">
    <input type="hidden" name="product_id" value="1">
    <input type="hidden" name="amount" value="50.00">
    <label>Quantity:</label>
   <input type="number" name="quantity" value="0" min="0"  max="4">
    <br/><br/>

    <p>Product: crankset</p>
   <input type="hidden" name="product_name"  value="crankset">
    <input type="hidden" name="product_id" value="2">
    <input type="hidden" name="amount" value="215.00">
    <label>Quantity:</label>
   <input type="number" name="quantity" value="0" min="0"  max="4">
    <br/><br/>

    <input type="submit" value="Submit" name="placeOrder">
</form>
{% endraw %}
```

 Note: The form provides mostly hardcoded sample data so that you can soon test if the view logic can take submitted data and write it to the Order and Order_Item tables in the database. An analysis of this code appears later in this lab.

Save the changes to the file.

Task 3.3: Update the index function to render the test page
Continue the task by updating the index function, so that it renders the test_form.html page.

The following diagram shows how the index view logic retrieves product data from the database and then returns to the user a webpage that contains an HTML form in it. The form contains hidden input elements that contain essential information for order submissions that occurs if the user chooses to submit an order using the form.

Index view.

Return to the tab where you have views.py open in the file editor.

Update the index function as follows:

Comment out the return HttpResponse… line

Just below the line you commented out, add these two new lines:

context = {'product_items': product_items}
return render(request, "test_form.html", context)
The index function still retrieves the Product information from the database, but now rather than sending a hardcoded one line response to the browser, it instead renders the test_form.html template file to the user, along with a context object that contains product data that the template can reference.

Verify that the test page renders by doing the following:

Reload the base URL webpage, for example at https//…vfs.cloud9.us-west-2.amazonaws.com, where the URL matches your unique AWS Cloud9 Preview URL. Be sure to remove anything in the URL that appears after amazonaws.com.
The test page should appear as shown here.

Test form.

Image description: Image shows a webpage with “Test page for submitting form data” in bold text. Below this is a list of products followed by a quantity input box for “cassette” and “crankset”. At the bottom is a Submit button.

 Note: If you analyze the test_form.html template in the AWS Cloud9 file editor, you might notice a few details:

The  Django Template variable

```django
{% raw %}
{% csrf_token %}
{% endraw %}
```

was included in the form, because the Django settings have CSRF protection enabled.

The {{ product_items.0.product_name }} is included to prove the point that data retrieved by the index function defined in views.py can be used to populate what appears in the form. So the word “cassette” is pulled from the database. By contrast the word “crankset” was hardcoded in the template.

You replace the hardcoded values seen in the rest of this test form when you create the actual template in the next lab.

 Note: The Submit button logic is not yet implemented. You work on that next.

Task 3.4: Begin creating the process_order function
Continue creating the necessary views by adding a process_order function to the views.py file.

As illustrated in the following diagram, when a user submits the form with order data, the process_order view logic parses the data received in the HTTP POST request. And it generates the values needed to create an Order table entry as well as one or more Order_Item table entries. Finally, the view returns order results data to the runserver log output and routes the user to the order_result URL. In the next lab, when you create the order_result.html template, the view logic is readily updated to render the order results to the end user.

Two views.

In views.py, create a new function named process_order that takes a request object.

Add a line to the new function that prints a message to the runserver terminal when the function is invoked:


print('\n***LOG: in "process_order" function')
Save the changes.

Next, open the bicycle_app > urls.py file in the file editor and add the following new urlpattern to it:


path("order_result", views.process_order, name="process_order"),
 Note: The path that you added is to “order_result”. When a user submits the form, the path gets invoked by the form action <form action="order_result" method="POST"> line in the test_form.html file that you just created.

The URL patterns to handle order processing are now set as follows:

When a user loads the base page at “”, which is at the URL …vfs.cloud9.us-west-2.amazonaws.com, the index function is invoked, which renders the test form page to the user.
When a user submits the form, Django invokes the process_order function and then direct the browser to the order_result URL.
Save the change and close the urls.py file.

Return to the views.py file editor.

Task 3.5: Parse the POST data in the process order function logic
Continue building the solution by configuring how the data is processed when a user submits an order by choosing the Submit button in the test form.

Open models.py in your file editor.

Observe the structure of the Order_Item model that you created in the previous lab. Notice that it contains the following four fields:

order_number
product_id
quantity
amount
You want to parse these values out of the submitted form data or calculate these values as necessary, so that you can create new Order_Item table entries to record the order details.

Observe the structure of the Order model too. These values also need to be calculated based on the submitted data so that you can add a new row to the Order table when an order is submitted.

Back in the views.py file, in the process_order function, add the following code:

```python
if request.method == "POST":
   print('LOG: in "process_order" function - POST  received')
   #save POST data and convert from Django QueryDict to  Python Dict
    received_data = dict(request.POST)

    # parse into Python "lists"
    product_name = received_data['product_name']
    print('product_name = ' + str(product_name))
    product_id = received_data['<FMI-1>']
    print(<FMI-2>)
    item_price = received_data['amount']
    print(<FMI-3>)
    quantity = received_data['<FMI-4>']
    print(<FMI-5>)

    #more logic goes here

    #return a response
   return HttpResponse('/order_result page loaded. Check  the runserver console for test result.') 

else:
    #should never get here
   return HttpResponse('process_order must receive a POST  action.')
```

 Note: You can indent or outdent multiple lines of code in the AWS Cloud9 file editor by selecting them, and then from the Edit menu choose Line > Indent or Line > Outdent as necessary.

Replace all five FMI (fill me in) placeholders in the code so that all values related to each product in the form data that was submitted are saved to Python lists.

 Note: The product_name line of code shows an example of how this can be done. You might also find it helpful to refer to the test_form.html code and the name attribute for the input elements. You could also open the developer tools network tab in the browser where the test form is loaded, and try submitting the form once to see the payload form data that is being submitted.

The print lines that include the FMI placeholders are used to print the Python list contents to the runserver terminal output. This permits you to verify that the data is correctly parsed.

 Hint: The print('product_name = ’ line shows an example.

Save the changes.

Refresh the base URL webpage that displays the web form.

Choose a quantity of at least 1 for at least one of the products, and choose Submit.

If your code is working correctly, the browser should display the message “/order_result page loaded. Check the runserver console for test result.”

 Expected output: the runserver output should display the following:


...
***LOG: in "process_order" function
LOG: in "process_order" function - POST received
product_name = ['cassette', 'crankset']
product_id = ['1', '2']
item_price = ['50.00', '215.00']
quantity = ['3', '2']
[24/Jan/2024 01:18:34] "POST /order_result HTTP/1.1" 200 71
 Note: The quantities that you observe are different, depending on how many of each item you ordered.

Choose here if you need to see the solution code for the process_order function so far.

def process_order(request):
    print('\n***LOG: in "process_order" function')
    if request.method == "POST":
        print('LOG: in "process_order" function - POST received')
        #save POST data and convert from Djanjo QueryDict to Python Dict
        received_data = dict(request.POST)
        # parse into Python "lists"
        product_name = received_data['product_name']
        print('product_name = ' + str(product_name))
        product_id = received_data['product_id']
        print('product_id = ' + str(product_id))
        item_price = received_data['amount'] 
        print('item_price = ' + str(item_price))
        quantity = received_data['quantity']
        print('quantity = ' + str(quantity))

        #more logic goes here

        #return a response
        return HttpResponse('/order_result page loaded. Check the runserver console for test result.') 
    else:
        #should never get here
        return HttpResponse('process_order must receive a POST action.')
Excellent! Of the values that you need to submit to create an Order_Item record, you now have all of them stored in Python lists. However, you need to create the JSON-formatted order and order item objects that you need to submit to the database tables.

In the process_order function code, add the following just above the #more logic goes here comment to generate a new order number.


#ITERATE THROUGH SUBMITTED DATA
i = 0
items = []
total_order_amount = float(0)
for i in range(len(quantity)):
    if int(quantity[i]) != int(0):
       print('ITEM WANTED: ' + product_name[i] + ' -  quantity: ' + quantity[i])
       total_order_amount += float(quantity[i])*float (item_price[i])

        # calculate amount for single product
       single_prod_total_amt = float(quantity[i]) * float (item_price[i])
       print('single_prod_total_amt: ' + str (single_prod_total_amt))

        # gather order item data and append it to a list
        order_item_data = {
            "product_id": product_id[i],
            "quantity": quantity[i],
            "amount": single_prod_total_amt
        }
        print('order_item_data =' + str(order_item_data))
        items.append(order_item_data)
        #print("No " + product_name[i] + " requested.")
    i += int(1)

print('total order amount: ' + str(total_order_amount))

# gather order data
order = Order(amount=total_order_amount)
 Caution: All the code that you pasted in should be in the if request.method == “POST”: section of the function, with proper indentation.

 Note: Keep in mind that you can indent or outdent multiple lines of code in the AWS Cloud9 file editor by selecting them, and then from the Edit menu choose Line > Indent or Line > Outdent as necessary.

Save the changes.

Refresh the base URL page again.

 Hint: To clear the quantities of the products selected during the previous form submission, hold down the Ctrl key and choose the browser refresh icon (Windows) or on macOS, hold down the Shift key and choose refresh.

Select a quantity of at least 1 for each product, and then choose Submit.

The usual static message should appear in the webpage. However, in the runserver terminal output, you should see additional data.

 Expected output:


...
***LOG: in "process_order" function
LOG: in "process_order" function - POST received
product_name = ['cassette', 'crankset']
product_id = ['1', '2']
item_price = ['50.00', '215.00']
quantity = ['3', '2']
ITEM WANTED: cassette - quantity: 3
single_prod_total_amt: 150.0
order_item_data ={'product_id': '1', 'quantity': '3',  'amount': 150.0}
ITEM WANTED: crankset - quantity: 2
single_prod_total_amt: 430.0
order_item_data ={'product_id': '2', 'quantity': '2',  'amount': 430.0}
total order amount: 580.0
[30/Jan/2024 18:34:14] "POST /order_result HTTP/1.1" 200 71
 Note: The single_prod_total_amt values were calculated for each product, and the total_order_amount was also calculated.

Task 3.6: Establish a database connection
Take a moment to confirm the existence of test data in the Order and Order_Item tables.

 Command: In second terminal window (the one where runserver is not running), run the following command to connect to the MySQL database.


mysql -u django -p
 Expected output:


Enter password:
 Command: When prompted for a password, enter djangoAciDb2034.

 Expected output:


Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 40
Server version: 8.0.36-0ubuntu0.22.04.1 (Ubuntu)

Copyright (c) 2000, 2024, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input     statement.

mysql>
You should now see a mysql> prompt, indicating that you are connected to the database.

 Command: At the mysql> prompt, run the following commands:


show databases;
use bicycles;
show tables;
select * from bicycle_app_order;
select * from bicycle_app_order_item;
 Expected output:


Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables;
+----------------------------+
| Tables_in_bicycles         |
+----------------------------+
| auth_group                 |
| auth_group_permissions     |
| auth_permission            |
| auth_user                  |
| auth_user_groups           |
| auth_user_user_permissions |
| bicycle_app_order          |
| bicycle_app_order_item     |
| bicycle_app_product        |
| django_admin_log           |
| django_content_type        |
| django_migrations          |
| django_session             |
+----------------------------+
13 rows in set (0.00 sec)

mysql> select * from bicycle_app_order;
+----+--------+----------------------------+
| id | amount | order_date_time            |
+----+--------+----------------------------+
|  1 |  88.00 | 2024-02-09 18:37:47.479674 |
+----+--------+----------------------------+
1 row in set (0.01 sec)

mysql> select * from bicycle_app_order_item;
+----+------------+----------+--------+-----------------+
| id | product_id | quantity | amount | order_number_id |
+----+------------+----------+--------+-----------------+
|  1 |          3 |        2 |  35.00 |               1 |
|  2 |          4 |        1 |  18.00 |               1 |
+----+------------+----------+--------+-----------------+
2 rows in set (0.00 sec)
 Consider: Observe the number of rows returned by the last two commands. They show how many records currently exist in the Order and Order_Item tables. It is expected that at this point, your order form is not yet adding records. The only data in the order and order_item tables is the test data that you added in task 1.1.

Leave this mysql client connection open. You return to it in a moment.

Task 3.7: Update process_order view to save data to the database
Complete the last task in the lab by saving the order data to model objects of type Order and Order_Item. This has the effect of saving the order data to the Order and Order_Item database tables.

In the process_order function, add the following code just below the #more logic goes here comment and just above the #return a response comment.


# add new entries in the database for both order and order items
try:
    order.full_clean()
    print("order is valid")
    # write order to the database
    order.<FMI-1>()
    print("order",order.id, "saved")
    # iterate over order items
    for item in items:
        item["order_number"] = order.id
        order_item = Order_Item(
            order_number=order,
            product_id=item["product_id"],
            quantity=item[<FMI-2>],
            amount=item["amount"],
        )
        order_item.full_clean()
        order_item.<FMI-3>()
    # display sucessful order confirmation page
    order_data = {
        "id": order.id,
        "order_date_time": order.order_date_time,
        "amount": total_order_amount,
    }
    context = {"order_details": items, "order": order_data}
    #return render(request, "order_result.html", context)
except ValidationError as e:
    # should never get here
    print("ERROR: object not valid", e)
 Caution: All the code that you pasted in should still be in the if request.method == “POST”: section of the function, with proper indentation. Keep in mind that you can indent or outdent multiple lines of code in the AWS Cloud9 file editor as necessary by selecting them, and then from the Edit menu choose Line > Indent or Line > Outdent.

Replace the three FMI placeholders in the code so that the following occurs:

The order object that you created from the Order model, with the order = Order(amount=total_order_amount) line, is saved to the database.

The quantity is set properly in the order_item object.

The order_item object created from the Order_Item model for every type of product ordered is saved to the database.

 Learn more: See the Django Model instance reference documentation for details if needed.

Save the changes and reload the base URL webpage that displays the web form.

Choose a quantity of at least 1 for at least one of the products, and choose Submit.

If your code is working correctly, the browser should again display the standard message “/order_result page loaded. Check the runserver console for test result.”

 Expected output: The runserver output should display the order results output in the same way as it did before. Here is an example:


...
***LOG: in "process_order" function
LOG: in "process_order" function - POST received
product_name = ['cassette', 'crankset']
product_id = ['1', '2']
item_price = ['50.00', '215.00']
quantity = ['1', '4']
ITEM WANTED: cassette - quantity: 1
single_prod_total_amt: 50.0
order_item_data ={'product_id': '1', 'quantity': '1', 'amount': 50.0}
ITEM WANTED: crankset - quantity: 4
single_prod_total_amt: 860.0
order_item_data ={'product_id': '2', 'quantity': '4', 'amount': 860.0}
total order amount: 910.0
order is valid
order 6 saved
[30/Jan/2024 19:01:19] "POST /order_result HTTP/1.1" 200 71
Choose here if you need to see the solution code for process_order function.

def process_order(request):
    print('\n***LOG: in "process_order" function')
    if request.method == "POST":
        print('LOG: in "process_order" function - POST received')
        #save POST data and convert from Djanjo QueryDict to Python Dict
        received_data = dict(request.POST)

        # parse into Python "lists"
        product_name = received_data['product_name']
        print('product_name = ' + str(product_name))
        product_id = received_data['product_id']
        print('product_id = ' + str(product_id))
        item_price = received_data['amount']
        print('item_price = ' + str(item_price))
        quantity = received_data['quantity']
        print('quantity = ' + str(quantity))
        
        #ITERATE THROUGH SUBMITTED DATA
        i = 0
        items = []
        total_order_amount = float(0)
        for i in range(len(quantity)):
            if int(quantity[i]) != int(0):
                print('ITEM WANTED: ' + product_name[i] + ' - quantity: ' + quantity[i])
                total_order_amount += float(quantity[i])*float(item_price[i])   
                # calculate amount for single product
                single_prod_total_amt = float(quantity[i]) * float(item_price[i])
                print('single_prod_total_amt: ' + str(single_prod_total_amt))

                # gather order item data and append it to a list
                order_item_data = {
                    "product_id": product_id[i],
                    "quantity": quantity[i],
                    "amount": single_prod_total_amt
                }
                print('order_item_data =' + str(order_item_data))
                items.append(order_item_data)
            #print("No " + product_name[i] + " requested.")
            i += int(1)

        print('total order amount: ' + str(total_order_amount))

        # gather order data
        order = Order(amount=total_order_amount)
        
        #more logic goes here
        # add new entries in the database for both order and order items
        try:
            order.full_clean()
            print("order is valid")
            # write order to the database
            order.save()
            print("order",order.id, "saved")
            # iterate over order items
            for item in items:
                item["order_number"] = order.id
                order_item = Order_Item(
                    order_number=order,
                    product_id=item["product_id"],
                    quantity=item["quantity"],
                    amount=item["amount"],
                )
                order_item.full_clean()
                order_item.save()
                # display sucessful order confirmation page
                order_data = {
                "id": order.id,
                "order_date_time": order.order_date_time,
                "amount": total_order_amount,
            }
            context = {"order_details": items, "order": order_data}
            #return render(request, "order_result.html", context)
        except ValidationError as e:
            # should never get here
            print("ERROR: object not valid", e)    
        #return a response
        return HttpResponse('/order_result page loaded. Check the runserver console for test result.')

    else:
        #should never get here
        return HttpResponse('process_order must receive a POST action.')
So what did you accomplish by adding this additional code logic? Check the database to find out.

 Command: Return to the terminal where you have the mysql client open, and run the following two commands again:


select * from bicycle_app_order;
select * from bicycle_app_order_item;
 Expected output: What is shown below is an example. Your results will be different, depending on what items you ordered.


mysql> select * from bicycle_app_order;
+----+---------+----------------------------+
| id | amount  | order_date_time            |
+----+---------+----------------------------+
|  1 |   88.00 | 2024-03-06 22:13:51.280965 |
|  2 | 1060.00 | 2024-03-06 22:49:11.253346 |
+----+---------+----------------------------+
2 rows in set (0.00 sec)

mysql> select * from bicycle_app_order_item;
+----+------------+----------+--------+-----------------+
| id | product_id | quantity | amount | order_number_id |
+----+------------+----------+--------+-----------------+
|  1 |          3 |        2 |  35.00 |               1 |
|  2 |          4 |        1 |  18.00 |               1 |
|  3 |          1 |        4 | 200.00 |               2 |
|  4 |          2 |        4 | 860.00 |               2 |
+----+------------+----------+--------+-----------------+
4 rows in set (0.00 sec)
Did the the number of rows of data increase?

If your process_order view logic is working correctly, each time that you submit an order, the Order table should contain an additional row and the Order_Item table should contain one or two additional rows, depending on how many types of products you ordered.

Try loading the https://…vfs.cloud9.us-west-1.amazonaws.com/order_history page, and then observe the runserver terminal output.

The latest orders are listed, because this view returns all orders.

Try loading the https://…vfs.cloud9.us-west-2.amazonaws.com/lookup_order/2 page, and then observe the runserver terminal output.

Recall that when you tested this at the end of task 2.3, it returned an empty data set. However, now there is an order with an order_number value of 2, so the view finds a record.

Congratulations! You have now successfully created view logic that records order detail to database tables when a user submits a form.

In this series of Django labs so far, you have installed and configured Django, and built models and views. In the next lab, the work that you have done in these last three labs come to fruition when you implement templates and bring the look and feel of the AnyCompany bicycle supplies website that you authored earlier to this Django hosted environment. See you in the next lab!

Lab files
The lab environment is ephemeral. All the lab resources are deleted when the lab time expires. If you want to keep a copy of the lab code, you can download all the lab code using the AWS Cloud9 environment.

To save the files on your local computer, in the AWS Cloud9 menu bar, choose File, and then choose Download Project.
 Task complete: In this task, you successfully created the process_order view, which required gathering information from the end user and inserting it into the Order and Order_Item database tables.

Conclusion
You have successfully done the following:

Created a view in Django that pulls data from a database and displays it on a webpage
Created a view that filters database results to return requested detail
Created a view that inserts new records into multiple database tables
Added URL patterns for Django to handle requests and route users to different URLs as appropriate
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End Lab and then confirm that you want to end your lab.

For more information about AWS Training and Certification, see https://aws.amazon.com/training/.

Your feedback is welcome and appreciated.
If you would like to share any feedback, suggestions, or corrections, please provide the details in our AWS Training and Certification Contact Form.

Django is property of the Django Software Foundation, JavaScript is a trademark of Oracle Corporation, and Python is property of the Python Software Foundation (PSF). Reference in this lab to any specific commercial product, process, or service, or the use of any trade, firm or corporation name is provided for informational purposes, and does not constitute endorsement, recommendation, or favoring by Amazon Web Services.