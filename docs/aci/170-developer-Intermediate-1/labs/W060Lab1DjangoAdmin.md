# Administering a Web Application

## Lab overview

In the previous few labs in this course, you built a web app hosted on the Django web framework for AnyCompany bicycle parts. You installed and configured Django, then defined Django models, views, and templates.

In this lab, you activate the Django administrator UI and discover the benefits that it provides.

Objectives
By the end of this lab, you should be able to do the following:

Enable the Django administrator UI.
Create a Django super user and access the administrator UI.
Activate access to models and model data through the administrator UI.
Improve the display of model details in the administrator UI.
Modify model data using the administration UI.
Create Django users and groups.
Update product listings in the web application with the Django administrator UI.
Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Analysis: A detailed examination of a topic or concept to promote understanding.
 Caution: Information of special interest or importance (not important enough to cause problems with equipment or data if you miss it, but that could result in the need to repeat certain steps).
 Command: A command that you must run.
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
The following diagram shows the basic architecture of the lab environment. The resources depicted in the diagram already exist in your Amazon Web Services (AWS) account when you start the lab.

AWS Architecture diagram showing the initial state of the lab environment.

Image description: The diagram illustrates a website developer working in an AWS Cloud environment using an AWS Cloud9 integrated development environment (IDE) hosted on an Amazon Elastic Compute Cloud (Amazon EC2) instance. The instance is set up in a security-controlled public subnet of a virtual private cloud (VPC) and is accessible over the internet. The hosted website is available to consumers through the Apache HTTP Server running on the EC2 instance. To review the detailed diagram description, expand the following section.*

Detailed diagram description
Here’s a description of the components and how they’re connected:

AWS Cloud: The overall environment is encapsulated in the AWS Cloud, which is the broader context where all the components reside.

Lab VPC: In the AWS Cloud, there is a virtual private cloud (VPC) designated as Lab VPC. This is like a virtual network in the AWS environment that is isolated from other virtual networks.

Public subnet: Inside the Lab VPC, there’s a public subnet. This subnet is accessible from the internet. A subnet is a range of IP addresses in the VPC.

Security group: In the public subnet, there’s a security group. It acts as a virtual firewall controlling the traffic to the Amazon Elastic Compute Cloud (Amazon EC2) instance.

Amazon EC2 instance: Inside the security group, there’s an EC2 instance. This is a virtual server in AWS where applications can run. The EC2 instance is depicted with the EC2 instance group icon. Inside this instance, two key components are mentioned:

AWS Cloud9 IDE: This is an integrated development environment (IDE) provided by AWS. In this diagram, it’s part of the EC2 instance. This indicates that the AWS Cloud9 IDE is being used for development directly in the EC2 instance.

Ubuntu guest operating system: This indicates that the EC2 instance is running the Ubuntu guest operating system.

You (website developer): On the left side of the diagram, there’s an icon of a person with the label You (website developer). This symbolizes the developer who interacts with the AWS Cloud and, specifically, the EC2 instance, perhaps using the AWS Cloud9 IDE for developing a website.

AWS services used in this lab
AWS Cloud9
Amazon Elastic Compute Cloud (Amazon EC2)
AWS services not used in this lab
AWS service capabilities used in this lab are limited to what the lab requires. Expect errors when accessing other services or performing actions beyond those provided in this lab guide.

Task 1: Run the script to configure the development environment
In this task, you run a script that installs the Django framework on your Ubuntu Linux instance. You also set up your environment to match the end state of the previous lab.

Task 1.1: Connect to the IDE and run the setup script
Start by running a script, starting the web server, and adding product data to the database.

To open the AWS Cloud9 environment, copy the Cloud9Environment URL value that is listed to the left of these instructions, and paste it into a new browser tab.

 Command: In the AWS Cloud9 integrated development environment (IDE) terminal window, run the following command:


./setup.sh
 Analysis: The shell script completes configurations on the Amazon EC2 instance on which your AWS Cloud9 IDE is installed. The configuration replicates the steps that you completed in the previous lab and installs a Python virtual environment. It also installs Django and creates the bicycle_project Django project and the bicycle_app Django app.

 Caution: If you receive a prompt asking which services to restart, press Tab to navigate to Ok, and then press Enter so that the script continues to run.

 Expected output: If the script ran successfully, the final output should look as follows:


************************
**** EXAMPLE OUTPUT ****
************************
...
restore bicycles database
delete product table contents
reset auto_increment on product table
create the django user
 Command: To activate the Python virtual environment and start the Django web server, run the following commands:


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
February 21, 2024 - 20:17:16
Django version 5.0.1, using settings 'bicycle_project.settings'
Starting development server at http://0.0.0.0:8080/
Quit the server with CONTROL-C.
 Caution: The web server only remains running while you keep the process active in the terminal. Leave this terminal as it is. Note that debug and log information is written to this terminal’s output as you progress through the lab.

To add product data to the product table, open a second terminal window in AWS Cloud9.

 Command: In the new terminal, run the following:


cd ~/environment/django
source .venv/bin/activate
python manage.py loaddata /home/ubuntu/environment/products.json
 Expected output:


******************************
**** This is OUTPUT ONLY. ****
******************************

Installed 12 object(s) from 1 fixture(s)
(.venv)
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
Task 1.2: Confirm that the app is running
Confirm that the Django environment you now have matches the environment that you achieved by the end of the previous lab.

Return to the terminal where the runserver process is running and choose the link in the Cloud9 Help dialog box, which should appear in the corner.

 Caution: You can get to the same preview page at any time by choosing Preview > Preview Running Application. And then in the preview panel, choose the pop out into new window icon pop-out icon to open the preview in a new browser tab.

Completed website screen capture.

Image description: The image shows the AnyCompany bicycle parts website opened to the Products ordering page. It contains a form with a list of 12 bicycle products including descriptions, prices, and quantities to be ordered, along with a Submit button.

The lab environment that you now have matches what you had at the end of the last lab. Feel free to test submit an order and view order history and order details if you want to confirm the functionality of the site. However, doing so is not necessary for this lab.

Keep this browser tab open for the duration of this lab. You return to it later.

 Task complete: In this task, you successfully ran a script to install the Django framework on your Ubuntu Linux instance, and you updated database entries to get your environment to match the end state of the previous lab.

Task 2: Activate the Django administration UI
In this task, you enable the Django administration user interface and create a user that can access it.

Task 2.1: Access the Django administration login page
Start by starting running some commands and then accessing the admin console.

Observe the Django project settings.

In the AWS Cloud9 file browser, locate the django > bicycle_project > settings.py file and open it in the file editor.

Scroll down to the INSTALLED_APPS section and notice the ‘django.contrib.admin’ entry. This is what enables the Django administrator app. It is enabled by default when you install Django.

Modify the settings.

Comment out that line by using a # character, and save the change.

Leave this file open in the IDE. You return to it in a moment.

Test access to the Django administration console:

Copy the https://<unique-id>.vfs.cloud9.us-west-2.amazonaws.com URL from the address bar of the browser tab where you have the AnyCompany website open.

Open a new browser tab, paste the copied URL into the address bar, and then add /admin to the end.

The webpage displays an “Oops” message.

Now fix the issue that you caused by reverting the change.

Return to the AWS Cloud9 editor and uncomment the django.contrib.admin line.

Save the update.

Return to the browser tab where you tried loading the page, and choose the browser refresh icon to reload the page.

The page displays the following:

Django admin login screen.

Image description: Image shows a Django administration login console with form fields for Username and Password with a Log in button at the bottom.

 Note: You have now seen how to disable and then re-enable the Django administration UI. You might for security reasons decide that you don’t need it to be exposed, in which case disabling it could improve your security posture.

The administration login page is now available. However, you have not yet defined user credentials that you could use to log in. You do that next.

Task 2.2: Create a Django super user
Create a Django super administrator user that has permissions to log in to the Django administration UI.

In the AWS Cloud9 IDE, return to the second open terminal window, where you previously ran a mysql command.

 Command: To create a super user, run the following command:


python manage.py createsuperuser
 Command: When prompted for a username, enter admin and press Enter.

Leave the email field blank and press Enter.

 Command: When prompted for a password, enter djangoSecret764 or some other password that you won’t forget. Enter it again when prompted.

 Note: The password is not shown when typing for security.

 Expected output:


******************************
**** This is OUTPUT ONLY. ****
******************************

Username (leave blank to use 'ubuntu'): admin
Email address: 
Password: 
Password (again): 
Superuser created successfully.
(.venv)
Task 2.3: Log in to the Django administration console
Next, you log in as the new user.

Return to browser tab where you have the Django administration login page open.

Type in the credentials that you just created and choose Log in.

Logged in.

Image description: Image depicts the Django administration console with access to the Authentication and Authorization section. You have options to add both Groups and Users.

 Task complete: In this task, you successfully enabled the Django administration user interface and created a user that can access it.

Task 3: Enable model database tables access
In this task, you configure the Django administration UI to display models and model data.

Task 3.1: Register the models
Start by registering your existing Django models.

Open django > bicycle_app > admin.py in the file editor.

Add the following new lines to the file, just beneath # Register your models here.


from .models import Product, Order, <FMI-1>
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(<FMI-2>)
Replace the two <FMI> values with the proper values to import and register all three of the models.

 Tip: Look in the bicycle_app > models.py file. It might help you figure out what to fill in.

If you need to see the solution, expand this section.

from .models import Product, Order, Order_Item
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Order_Item)
Save the change and then refresh the Django administration web console.

The page now displays the three models that are part of your bicycle app.

Django administration form.

Image description: Image depicts the Django administration console with access to the Authentication and Authorization section. You have options to add both Groups and Users. It has a new section labeled Bicycle_App and shows a listing for Order_Items, Orders, and Products with the ability to add or change those entries.

Pretend that you are the website administrator and you have been asked to modify the price of one of the products for sale. You can now do that through this administration interface.

Modify the price of the hydraulic brake:

Choose Products.
Choose Product object (11).
Change the price to 59.00.
Choose Save.
Return to the browser tab where you have the AnyCompany bicycle parts webpage open, and refresh the page.

The price is now $59.00.

That’s nice. But it would be tedious to always have to know the product object number to be able to make an update to product data using the Django administration UI. Fortunately, there is a way to improve the way that the product table details appear.

Task 3.2: Improve Product model listings in the Django administration console
Configure the Django administration UI to display product table details.

Return to the admin.py file in the IDE and comment out the line that registers the Product model in the admin site.

Next, add the following lines of code to the bottom of the file:


class ProductAdmin(admin.ModelAdmin):
    pass
    list_display = ('id', 'product_name', 'price')
 Analysis: The code snippet is a configuration for a Django web application’s administrative interface. Here’s a summary of what the code is intended to do:

You have a digital catalog of products, each with details like an ID number, product name, and price. The code is part of setting up a special, password-protected webpage where the administrators of the website (like a store manager) can view and manage this catalog.

Specifically, the code sets up the rules for how the list of products will be displayed on this admin webpage. It specifies that when looking at the list of products, the admin will see three pieces of information for each product: its ID number, its name, and its price. This helps the admin quickly find and identify products when they need to make updates or check details.

The technical term for this setup in Django is a ModelAdmin class, and in this case, it’s named ProductAdmin. It’s a bit like a template that tells Django, “When showing the list of products in the admin area, display these particular details.”

This class would be part of a larger code base where it is connected to the product catalog data, allowing the admin interface to interact with that data based on the setup described in the code.

 Tip: You can learn more about Django ModelAdmin objects from the link in the Additional resources section.

Now, below the new ProductAdmin class, add a line to register both the Product model and the ProductAdmin class.


admin.site.register(Product, ProductAdmin)
 Tip: As you can see, this link is very similar to the line that you commented out a moment ago, but now it takes two parameters. It is also important that it appears after the ProductAdmin class definition.

Save the change and then refresh the Django administration console. Choose the Products table link.

That is a more useful display! Now you can see the product details.

Product name displaying in admin ui.

Image description: Image shows the Select a product to change form. It provides a list of all 12 products and prices that can be updated.

Implement the same improvement for the Order model so that the ID, amount, and date time of the order appear when you choose the Orders model.

Implement the same improvement for the Order_Item model as well, to display the ID, product ID, quantity, and amount.

If you need to see what the admin.py file should now contain, expand this section.

from django.contrib import admin

# Register your models here.
from .models import Product, Order, Order_Item
#admin.site.register(Product)
#admin.site.register(Order)
#admin.site.register(Order_Item)

class ProductAdmin(admin.ModelAdmin):
    pass
    list_display = ('id', 'product_name', 'price')

admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    pass
    list_display = ('id', 'amount', 'order_date_time')

admin.site.register(Order, OrderAdmin)

class Order_ItemAdmin(admin.ModelAdmin):
    pass
    list_display = ('id','product_id', 'quantity', 'amount')

admin.site.register(Order_Item, Order_ItemAdmin)
 Task complete: In this task, you successfully configured the Django administration UI to display models and model data.

Task 4: Create a user and a group
Consider this scenario: AnyCompany management doesn’t want to have to always come to you to change product prices or to add, modify, or delete products for sale. Your web development and cloud skills are too valuable for you to need to spend your time on business operations tasks such as that. Instead, they want you to grant permission to perform those types of tasks to other employees at the store.

In this task, you implement a solution to solve this business challenge. Specifically, you create a group and assign permissions to the group. You then create a user as a member of that group and test the solution by logging in as the new user.

Task 4.1: Create a group
Start by creating a Django group.

On the Django administration UI, next to Groups, choose Add.

For Name:, enter Product Managers.

Permissions: From the list of available permissions, select the following:

Bicycle_App | product | Can add product
Bicycle_App | product | Can change product
Bicycle_App | product | Can delete product
Bicycle_App | product | Can view product
Choose the right arrow icon to move these permissions into the Chosen permissions column.

Permissions selected.

Image description: Image illustrates a list of available permissions in one column and the chosen permissions in a second column. The permissions in the Chosen permissions column match the list of permissions previous selected.

Choose Save.

Task 4.2: Create a user and add the user to the group
Next, you create a user and add that user to the Django group that you already created. The user inherits the permissions granted to the group.

Create a user and add it to the Product Managers group.

Next to Users, choose Add.

For Username:, enter ProductManager1.

For Password:, enter Manager2024!.

For Password confirmation:, re-enter Manager2024!.

Choose Save.

In the Change user window that appears, under Permissions, configure the following:

Active: Leave this selected.
Staff status: Select this.
Groups: To add Product Managers to the Chosen groups column, choose the -> arrow icon next to that column pane.
Do not add any User permissions as only the permissions inherited from the group are needed for this user.
Leave all other default settings and choose Save.
Permissions selected for user.

Image description: Image illustrates the permissions selected and group configured for this user.

Test logging in as the new user:

Log out as the admin user by using the LOG OUT link in the top-right corner.

On the Logged out page, choose Log in again.

Enter ProductManager1 as the username and Manager2024! as the password.

Choose Log in.

You are successfully logged in. Notice how only the Products model is listed.

 Task complete: In this task, you successfully created a group and assigned permissions to the group. You also created a user as a member of that group and logged in as the new user.

Task 5: Add a new product to the web app without modifying the web app code
In this task, you use the Django administration UI to add a new product for sale that appears in the AnyCompany bicycle parts web app. In the process, you also verify that the user you just created has sufficient permission to modify the Products model data using the administration UI.

Still logged in as ProductManager1, add a product to the product table.

In the AWS Cloud9 file browser, go to django > bicycle_app > static and select rear-light.jpeg. Right-click and choose Download.

Back on the Django administration UI, choose the Add link next to Products and then fill in the following values:

Product name: rear light
Description: Be noticed at night
Price: 25.00
Product group: 1
Image url: Select Choose File and browse to and select the rear-light.jpeg file that you just downloaded.
Choose Save.

Return to the browser tab where you have the AnyCompany bicycle parts webpage open, and refresh the page.

The rear light now displays as a new item.

Appreciate for a moment the beauty of what you have achieved! Without the use of a web framework such as Django, you would have had to hardcode this new product information into your HTML file. Or, if the production information was being read out of a database, to add the product details to the database, you would have needed to compose a SQL insert statement or run some Python code that you authored. Both of those architectures would be time consuming and require technical skill (database skills, HTML coding skills). But now you have configured a web app where other people with limited technical skills can add and modify products by simply using a browser interface. You might even use it yourself sometimes, to save time when making a minor adjustment. Pretty cool!

 Analysis: You created a Product Managers group with access only to the Products model. You could similarly create another group named Order Managers with permissions to manage the Order and Order_Item data, so that users in that group would have the ability to modify existing orders.

By delegating the administration of the app data, you help keep the site secure, and you also offload the tedious work of dealing with changes to products and orders. This way, you can stay focused on web development and cloud architecting!

Your manager is now so impressed with this proof of concept that you have developed that she wants you to make the website more scalable and capable of serving a large number of users. Rather than run the app on a single AWS Cloud9 instance, with the database co-located on the same instance, she wants you to find a way to move the app to a more resilient and scalable hosting architecture. You work on that in the next lab. See you there!

Lab files
The lab environment is ephemeral. All the lab resources are deleted when the lab time expires. If you want to keep a copy of the lab code, you can download all the lab code using the AWS Cloud9 environment.

To save the files on your local computer, in the AWS Cloud9 menu bar, choose File, and then choose Download Project.
 Task complete: In this task, you successfully used the Django administration UI to add a new product for sale that now appears in the AnyCompany bicycle parts web app.

Conclusion
You have successfully done the following:

Enabled the Django administrator UI
Created a Django super user and accessed the administrator UI
Activated access to models and model data through the administrator UI
Improved the display of model details in the administrator UI
Modified model data using the administration UI
Created Django users and groups
Updated product listings in web application with the Django administrator UI
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End Lab and then confirm that you want to end your lab.

Additional resources
ModelAdmin objects

For more information about AWS Training and Certification, see https://aws.amazon.com/training/.

Your feedback is welcome and appreciated.
If you would like to share any feedback, suggestions, or corrections, please provide the details in our AWS Training and Certification Contact Form.

Django is property of the Django Software Foundation, and Python is property of the Python Software Foundation (PSF). Reference in this lab to any specific commercial product, process, or service, or the use of any trade, firm or corporation name is provided for informational purposes, and does not constitute endorsement, recommendation, or favoring by Amazon Web Services.