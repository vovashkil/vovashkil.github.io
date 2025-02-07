# Week 4: Django Overview

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to repo's main [README.md](../../../README.md)

## Django overview

### Pre-assessment

#### Which software design pattern is used by Django?

* Model-View-Template (MVT)

Wrong answers:

* Model-View-Controller (MVC)
* Presentation–Abstraction–Control (PAC)
* Model–View–Adapter (MVA)

All four responses are architectural patterns used in the presentation layer. However, Django specifically uses Model-View-Template (MVT), so developers can structure their applications based on it.

#### Which administrative tools are made available by Django? (Select TWO.)

* Command line interface (CLI)
* Admin web interface

Wrong answers:

* Amazon Alexa integration
* Admin kit in multiple programming languages
* Chatbot

While Alexa might be able to answer a few questions, the Django project does not provide any specific integration. Also, there is no embedded artificial intelligence (AI) chatbot in Django where an admin could ask questions, and Django does not provide multi-language SDKs.

On the other hand, a command line interface (CLI) is available to get started and run administrative commands. Also, after a Django project is deployed and running, an admin web interface helps admins manage user and data information.

#### Which programming languages are used in Django? (Select THREE.)

* HTML/CSS
* Django template language
* Python

Wrong answers:

* Go
* Java
* PHP

##### Explanation

* The programming languages listed are widely used to code web applications. For instance, Go, PHP, and Java are used for business logic in the backend.
* However, Django source code is in Python. Developers using Django code their data models and business logic in Python, as well.
* Note that Django web pages are mainly designed using HTML/CSS through templates. Django also provides an extension to HTML for displaying dynamic content with the Django template language.

### Django introduction

Django is an open source **web framework** intended to speed up the development of Python-based web applications. It is used for the frontend, which is the user interface, and the backend, which is the business logic and data handling. It is made of a **set of tools and Python libraries**. Instead of coding everything from scratch, Django provides the boiler plate elements to get started immediately with a running mockup web application. You, as a developer, can then customize the webpages and enhance the functionality by using more Django components.

The Django framework includes the following important components, detailed later in this section:

* **Command line interface (CLI)** for administrative tasks
* Recognizable **project file structure** to organize the source code
* **Model-View-Template (MVT) design pattern** to organize components of a web application
* Local file-based **object database** to store data
* **Data API** to create and manipulate data objects
* **Django template language** to inject dynamic data into webpages
* Many Django **built-in applications and middleware** for extra functionalities
* Dynamic **admin interface** for managing users and data

The Django framework, tools, and community are developed and maintained under the Django project. This project is led by the Django Software Foundation, an open source, independent foundation. The latest stable version includes documentation online. The largest community of developers is on Discord. The source code, written in Python, is on GitHub. For more information, see the [Django documentation](https://docs.djangoproject.com/) on the Django website.

Django is also compatible with many Amazon Web Services (AWS) products and services. Developer tools are used to edit, deploy, and test the Django code. Compute services can run a Django project in test, staging, and production phases. Storage and database services can store static and dynamic data that is generated from user behavior or displayed to them. Finally, monitoring services help admins observe and operate running applications.

#### Django App resources

* [Developer Tools on AWS](https://aws.amazon.com/products/developer-tools/)
* [AWS Compute](https://aws.amazon.com/products/compute/)
* [Cloud Storage on AWS](https://aws.amazon.com/products/storage/)
* [AWS Cloud Databases](https://aws.amazon.com/products/databases/)
* [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
* [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/)
* [Amazon S3](https://aws.amazon.com/s3/)
* [Amazon RDS](https://aws.amazon.com/rds/)

#### Why is it called "Django"?

One of the initiators of the Django web framework was a programmer for a newspaper company and a musician. He was inspired by guitarist Django Reinhardt. So from the start, in 2003, the framework was named after the guitarist, with no special IT-related meaning.

### Django concepts

Every Django-based web application has to be created from a **Django project**. With the help of a CLI, a project file structure unfolds as a runnable project with a default single webpage.

When designing a website, you might consider different services or functionalities. These services within the same website can be mapped to **Django applications**. For a daily banking website, the overall financial view, account details, and loan management could be designed as three different Django applications. Each of them would come with their own data and user interface.

After adding business-specific applications to a project, the running website is customized to serve its purpose.

* A **Django project** represents a website and gathers all the corresponding Django applications. It controls which application is invoked based on *URL mappings*. *Settings* are used to define global variables to influence how the framework will behave. Optionally, it includes a local database.
* A **Django application** represents a logical part of a website, with a specific *configuration*. It manages its data using *models* and *forms*. It holds some business logic in *views*. The application's webpages are designed using *statics* and *templates*, which define visual elements, such as pictures and styling rules.

A Django project is made of one or more applications. This is also visible in the project file structure.

### Django CLI utility

After installing the Django Python package, a utility CLI called *django-admin* is available. This helps to create a default Django project. As soon as a project is created, a local script called *manage.py* is available in the current directory. These two utilities can be considered the same in terms of functionality. It is recommend to use manage.py because it sets an environment variable pointing to the current project settings, so it is project specific.

The following example commands create a Django project called **pets_project** with a single **pets_app** application.

#### Start a project

```
django-admin startproject pets_project.
```

**startproject** creates a project directory structure in the current directory, including a manage.py script file and a **pets_project** folder.

#### Start an application

```
./manage.py startapp pets_app
```

**startapp** creates an app directory structure under the **pets_app** folder in the current directory.

#### Running a server on the localhost

```
./manage.py runserver
```

**runserver** starts a web server on the local machine.

For more information, see [django-admin and manage.py](https://docs.djangoproject.com/en/stable/ref/django-admin/) on the Django website.

### Project file structure

At the top level, the **manage.py** admin script helps manage the project. The **db.sqlite3** file is the default database synchronized with the application models. The **static** folder gets a copy of the application's static artifacts.

```
.
├── db.sqlite3
├── manage.py
├── pets_app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
└── pets_project
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-311.pyc
    │   ├── settings.cpython-311.pyc
    │   ├── urls.cpython-311.pyc
    │   └── wsgi.cpython-311.pyc
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

Under **pets_project**, you will find overall project-related files. The **settings.py** code lists important project variables. For example, one of the variables indicates which database is being used. Another variable sets where the static artifacts are located. The **urls.py** file maps URLs with Django applications.

Under **pets_app**, you will find the code for one specific application. The **urls.py** file maps application URLs with views, building on the project URL mappings. The **views.py** code holds the business logic. Webpages are designed with templates and static content under the **static** and **templates** folders.

### MVT design pattern

When a user request is initiated, Django controls which page is displayed through a specific Django application and its URL mappings. It uses the MVT design pattern to render a specific webpage. The webpage is built from a template and populated by data coming from one or more models.

#### Model-View-Template

* The **view** is called by Django to handle user requests with the help of models and templates. It includes the web application business logic.
* The **model** acts as a data interface for anything that needs persistency. The data is stored in a database that might be external to Django.
* The **template** is the returned webpage made of static elements and dynamic elements populated from models.

### File-based object database

Django supports SQLite and uses it as a default persistence layer in the form of a local file. As noted previously, a db.sqlite3 file is present in a project's top directory. This is a lightweight database with some limitations compared to enterprise databases. For instance, it does not support a high level of concurrency. However, it is a good choice during development because it is preconfigured and convenient to use.

In pre-production, a dedicated database server, separated from the Django web server, should persist the data. Such migration is supported by Django out of the box through its settings and command line utility. It is meant to be straightforward. In addition to SQLite, Django also supports MySQL, PostgreSQL, MariaDB, and Oracle.

For more information, see [Databases](https://docs.djangoproject.com/en/stable/ref/databases/) on the Django website.

### Data API

After you define your data models through your own Python classes, Django offers a Python API to create, retrieve, update, and delete (CRUD) objects. This API is used in the views of your Django applications.

The Django shell is an interactive Python interpreter with the Django settings loaded. You can also use it to load the API, interactively create objects, and save them directly to the database. As a preview, the following is a quick sample after defining the class **Breed** in a **pets_app** application.

```
./manage.py shell
>>> from pets_app.models import Breed
>>> b = Breed(name="Chihuahua", color="any", height="7", weight= "5")
>>> b.save()
>>> exit()
```

The **Breed** class is imported, a **Chihuahua** breed object is created, and the data is stored in the configured database.

For more information, see [Making queries](https://docs.djangoproject.com/en/stable/topics/db/queries/) on the Django website.

### Django template language

Django templates are used to design webpages. They are mainly made of static HTML code. To add data from models into the webpage, Django offers the Django template language. Written inside an HTML template, Django template language is recognizable because it is marked with double curly braces, as shown in the following example.

```
Dogs of the breed {{ breed.name }} are on average 
{{ breed.height }} inch tall, with a weight of {{ breed.weight }} pounds.
```

The Django template language can also be used to write dynamic links when the value is not known in advance. This is useful to refer to artifacts, such as pictures, that are not public. Django can help construct a working URL on the fly, including security tokens, while a website is deployed and running.

For more information, see [Django template language](https://docs.djangoproject.com/en/stable/ref/templates/api/) on the Django website.

### Built-in applications and middleware

The term *application* describes a Python package that provides a set of features. A project can be enhanced by writing your own applications, including some combinations of models, views, and templates. Django contributes with built-in packages that can be used right out of the box.

The term *middleware* refers to software components that you can use to intercept and modify the Django’s request and response processing. Even if you can write your own middleware, Django includes many ready-to-use middleware components that can be added to a project.

#### Applications

Built-in Django applications for more functionalities:

* **django.contrib.admin** provides an admin web interface to manage users and data objects.
* **storage** helps with serving artifacts, like images, from an external object storage service, such as an S3 bucket.
* **django.contrib.staticfiles** collects static files from each  application into a single directory that is conveniently deployable to production.

#### Middleware

Build-in Django middleware for more request processing:

* **CsrfViewMiddleware** gives protection against Cross-site Request Forgery (CSCF) by adding hidden form fields to post forms and checking requests for the correct value.
* **SecurityMiddleware** provides several web application security enhancements against common vulnerabilities.
* **SessionMiddleware** and **AuthenticationMiddleware** associate users with requests using sessions so you can have both public and protected areas on your website.
* **CommonMiddleware** includes different features like URL rewriting, and blocking specific browsers by listing user agents.
* **LocaleMiddleware** helps with the localization and translation of your website.

For more information, see [Applications](https://docs.djangoproject.com/en/stable/ref/applications/) and [Middleware](https://docs.djangoproject.com/en/stable/topics/http/middleware/) on the Django website.

### Admin interface

By default, Django installs in newly created projects a pre-built application called *django.contrib.admin*. It adds an administration web interface to your website. It can be removed from the project settings. The default URL path is /admin, but this is editable.

The interface lists the users and shared models. Newly created models are not visible, by default. The administrator can display a list of users and data from the database. Admins can modify an entry, delete it, or create new ones, as in the Django shell.

For more information, see the [Django admin site](https://docs.djangoproject.com/en/stable/ref/contrib/admin/) on the Django website.

### Introduction to the MVT Design Pattern

Design patterns are blueprints and not code to be copied. They are different from algorithms. Design patterns are documented with a high-level description of a problem and a solution. They include a structure of classes and how they relate to each other. They also commonly show some example code as a way to explain. However, the code of the same pattern applied to two different use cases might differ.

### UI design patterns

#### Model-View-Controller (MVC)

When using UI design patterns, the business logic in your application can be separated from the presentation logic. This creates an application that is more convenient to maintain. Changes to the presentation can be made independent of the business logic, and vice versa. The business logic can also be unit tested separately from the presentation.

The Model-View-Controller (MVC) is the best-known pattern in this category. It was first developed in the late 1970s and is used for a variety of purposes.

* The **controller** receives requests from end users. It gets the data and uses it to construct a response made of a UI filled with data.
* The **model** holds the data. It is connected to data sources and handles the data logic to read and write to the persistence layer. It eventually includes the logic to refresh itself and notify the controller.
* The **view** represents the UI initiated or refreshed by the controller with data from the model.

#### Django Model-View-Template

Django uses MVT instead of MVC.

* The **view** gets called by the Django framework as a match to a specific URL to handle user requests. It includes the web application business logic. It does not require a model or a template to return a response, but this is convenient and makes the code more readable. A view is implemented as a regular Python function.
* The **model** acts as a data interface for anything that needs persistence. It does not include any data logic to integrate with the persistence layer or refresh itself. However, the data is stored in a database that might be external to Django. The framework implements the data logic to integrate with the database. A model is implemented as a regular Python class with variables as data attributes.
* The **template** represents the returned webpage made of static and dynamic elements populated from models. A template is implemented as an HTML file with HTML code for the static elements and Django template language code for the data elements.

If to compare MVT and MVC, MVC's controller responsibilities are in both the Django framework and MVT's view. The Django framework handles user interactions by applying changes to browser requests and responses, and by handling the routing to the corresponding views. Then, the MVT's view constructs the UI by gluing data and templates.

### Django flow

The Django flow starts when a user selects a link, issuing a request. After passing some middleware, the request gets routed to an application. There, the request is handled by a view, and a response is rendered. The response is returned to the user after passing some middleware again on the way back.

1. **HTTP request**. The user chooses a link that has a specific URL. This starts a call to the web server.
2. **Middleware for inbound traffic**. The request can be inspected or transformed on the way in. Middleware components are often used for security, to authenticate the end user, check the user session, and validate access. It might add extra HTTP headers to the request, like the locale, to influence how the view will handle the request.
3. **From URL to view**. The Django framework acts as a controller to decide which Django application will handle the request and which view function will be called inside the app.
4. **View**. A specific view is called by the framework. It gets the HTTP request's parameters and the request's body for POST requests. The view's business logic fetches or modifies data using the models and the data API. It finally prepares the HTTP response by selecting a template and setting the values of the template's dynamic data in a context object.
5. **Model**. One or more models are used by the view. The model's data attributes are read from the database or populated by the view and persisted by the framework.
6. **Template**. One template is used by the view to create a webpage. The template receives dynamic data in the form of a context object. The framework renders the complete page, mixing static HTML and contextual data. The webpage is returned in an HTTP response body.
7. **Middleware for outbound traffic**. The response can be inspected or transformed on the way out. For instance, error codes can be detected, so notifications can be sent.
8. **HTTP response**. The browser receives an HTTP response with a body containing an HTML webpage that is displayed.

### Django deployment

#### Backend

* Web server
* Interface server
* Python application

The term *server* is used to define a process serving files, APIs, or applications. It does not necessarily map to a separate virtual machine (VM) or physical server. All the backend processes could run on one or multiple machines.

There are currently two main standards: **Web Server Gateway Interface (WSGI)** and **Asynchronous Server Gateway Interface (ASGI)**. Both standards are supported by the latest stable version of Django.

#### WSGI standard

WSGI is a long-time standard for Python web servers, used by many web frameworks, such as Django. WSGI does the undifferentiated heavy lifting, like parsing the HTTP request. The framework or application must implement a specified function, as illustrated in the following example, to make it work with the WSGI interface. This is suitable for **regular synchronous web applications** where requests are handled one at a time. Example WSGI servers include Gunicorn and gWSGI.

```
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    yield b'Hello, World!\n'
```

#### ASGI standard

ASGI is supported by Django 3.0 and higher. ASGI is used for asynchronous real-time web applications, where long polling is crucial. If your website under the same Django project offers both regular and real-time webpages, ASGI is capable of serving specific parts as WSGI. Example ASGI servers include Daphne, Hypercorn, and Uvicorn.

```
async def application(scope, receive, send):
    event = await receive()
    ...
    await send({"type": "websocket.send", ...})
```

### Web Application Types examples

1. **Latency-sensitive trading screen**. - **ASGI**. Stock market price changes and business news should flow into the UI as they happen. Orders must be sent without delay. Multiple long-time polling connections are kept between the browser and the backend.
2. **Real-time assembly line monitoring dashboard**. - **ASGI**. Machines and robots send live telemetry data that must be displayed without delay. Maintenance alarms are pushed to the dashboard.
3. **Retail ecommerce application**. - **WSGI**. Users browse a products catalog and place orders. This is in a regular synchronous request-response scenario.
4. **Preliminary results of the presidential elections**. - **ASGI**. As the election unfolds, new results are sent to the UI waiting for more data.
5. **Daily banking application**. - **WSGI**. Users browse their bank accounts and pay invoices. Requests are handled one at a time.
6. **Entertainment streaming catalog**. - **WSGI**. Users browse the music or movies by genre, category, or popularity. They also search by name. This is in a regular synchronous request-response scenario.
7. **Live sports scoreboard**. - **ASGI**. Scores are updated while games are played. The UI can use long polling to get goals and scores without delays.
8. **Weather forecast**. - **WSGI**. Visitors search for a location to see the forecast. The forecast is not updated in real time, but a few times a day. So, it is likely that this is not in a long polling scenario, but regular request-response.

#### Development environment

By using the **runserver** command utility, Django spawns a lightweight development web server on the local machine. It acts as both a **web server** and **WSGI server**. It listens to the specified port, which is port 8000, by default. 

#### Production environment

A typical deployment of a non-real-time web application example includes:

* In front, **Apache HTTP Server** can serve static files as well as handle client connections.
* Apache Server proxies request to a **WSGI server** that can be implemented by **Gunicorn**, as an example.
* Django application.

##### [How to deploy Django](https://docs.djangoproject.com/en/stable/howto/deployment/) on the Django website

### Developing a Django Web Application on AWS

#### Architecture Example

A Django project can be integrated with AWS services. The AWS supported IDE is used for coding and testing. The data could be locally stored on the IDE or on external storage and a database. Later, in production, the Django web application will run on a compute platform, like AWS Elastic Beanstalk.

1. **Development**. The developer accesses a supported IDE to program a Django project and applications.
2. **Running and testing**. The developer can start a Django server locally on their IDE. The Django project can be configured to get and set its model's test data from Amazon Relational Database Service (Amazon RDS)  and images from Amazon Simple Storage Service (Amazon S3).
3. **Deployment to production**. After the Django project is fully tested on the IDE, it is deployed to the AWS compute platform of choice. For instance, an Elastic Beanstalk environment can host a Django project.
4. **User access**. Users and administrators can then access the web application from a secure public URL.
5. **Production data persistence**. The deployed Django-based web application can access data from Amazon RDS and Amazon S3 in the same way as the IDE. Based on configuration, different databases and buckets will be used in production.

### Environment setup

#### Install the Django Python package in your Python virtual environment from your IDEs terminal

```
mkdir /home/ubuntu/environment/django
cd /home/ubuntu/environment/django
python -m venv .venv
source .venv/bin/activate
pip install django
pip list --local
```

#### Create a Django project

**startproject** creates a project directory structure in the current directory, including a **pets_project** folder.

```
django-admin startproject pets_project .
```

A new file, *manage.py*,  appears in the current directory. This script has the same functionalities as django-admin. However, manage.py should now be used because it sets an environment variable pointing to the current project settings. It is project aware.

#### Adding your own application

```
./manage.py startapp pets_app
```

**startapp** creates an app directory structure under the folder **pets_app** in the current directory, including **models.p**y** inside.

* To register the newly created application, append **pets_app** in **INSTALLED_APPS** in your project **settings.py** file.

#### Applying the changes made in models to synchronize them with the database

```
./manage.py makemigrations
./manage.py migrate
```

#### Populating the database with date

After models are defined and data tables are prepared, they can be populated. It can be done manually using the Django shell and the data API, or by using in the admin interface. However, the database can be batch populated automatically by ingesting a JSON file with all the data using the Django command line.

```
./manage.py loaddata breed.json
```

#### Collecting the application's static files

```
./manage.py collectstatic
```

**collectstatic** collects the application's static files (CSS, JavaScript, and images) into the static root, which is the *static* folder, by default.

#### Creating superuser

To make use of the admin interface, create an admin user and select its username, email, and password.

```
./manage.py createsuperuser
```

**createsuperuser** creates a superuser account with a username and password that can be used to visit the admin interface.

### Preview your application

Here are some tips to run and preview a Django application in AWS Cloud9:

* Avoid using sudo and use the ports supported by AWS Cloud9. If you run your server on port 8080, 8081, or 8082, AWS Cloud9 will automatically proxy it to a URL with port 443 (HTTPS). A visual suggestion will pop up. The link opens the web application in a new tab, which is the recommended way to test it.
* Instead of using a browser tab, AWS Cloud9 has an embedded preview functionality. But, AWS Cloud9 uses an iframe in the preview panel. For the preview button to work, you need to comment out **XFrameOptionsMiddleware** under the list variable, **MIDDLEWARE**, in your project **settings.py** file.
* Add **'.amazonaws.com'** in the **ALLOWED_HOSTS** in your project **settings.py** file.

```
./manage.py runserver 0.0.0.0:8080
```

**runserver** opens an AWS Cloud9 supported port for previewing a web application.

### [Lab: Installing and Configuring Django](./labs/W040Lab1ConfiguringDjangoFramework.md)

### Knowledge Check

#### What are the first steps in Django after the Django Python package is installed?

* Create a project and then create an application

Wrong answers:

* Create a model and then create a view and template
* Create an application and then define the URLs
* Create a middleware and then create an interface

##### Explanation

* A Django project, including a custom Django application, should be created. First, the django-admin command line utility is used to create a Django project. Then, a Django application can be created with manage.py. For more information, see [django-admin and manage.py](https://docs.djangoproject.com/en/stable/ref/django-admin/) on the Django website.
* Models, views, and templates are created after a project and a custom application are created.
* Before creating an application, a project needs to be defined.
* Middleware can be created or used after a project has been created. Interfaces are not created. A WSGI server is used to run a Django project.

#### What is the role of a view in the Model-View-Template (MVT) design pattern?

* Handling a request and providing a webpage as a response

Wrong answers:

* Adding clarity through a multilayer architecture
* Managing data through an admin interface
* Monitoring user activities and system performance

A **view** is a basic Python function that implements the web application's business logic. It gets the request's parameters and content. It handles the data using models and prepares a response using templates.

#### Which template language is used by default in Django?

* Django Template Language (DTL)

Wrong answers:

* Python
* Structured Query Language (SQL)
* HTML

The **Django Template Language (DTL)** is the default template language used in Django. It's built into Django and is usable without any additional configuration.

### Summary

* Django is a Python-based web application framework that includes a number of tools and libraries. It comes with a command line utility to create Django projects and applications. 
* An MVT design pattern is used to structure the code of a Django application. The UI is built in HTML and the Django template language.
* A Data API can be called to create, read, update, and delete data objects. These objects are automatically stored in a local file-based object database or externally.
* Django handles user requests by controlling how they flow through middleware and applications, depending on which URL is requested. Django runs with the help of WSGI or ASGI interfaces.

## Django Models

### Pre-assessment

#### What is the role of a model in the Model-View-Template (MVT) design pattern?

* Holds the data

Wrong answers:

* Represents the user interface
* Guarantees the project's architecture
* Handles all the user requests

A *model* is the source of information about your data. It is used by the view to populate a template.

#### How is a model defined in Django?

* As a Python class

Wrong answers:

* As a Python dictionary
* As a Python map
* As a Python function

Each model is a Python class that subclasses django.db.models.Model.

#### After creating objects from a Django model, where can these objects be persisted?

* In a database

Wrong answers:

* In memory
* On an ephemeral storage
* In a version control repository

The **save()** function in every Django model saves its data in the configured database.

### Model Definition

A Django model is the source of information about the data stored in a database table.

#### Class

A model is created by defining a new Python class that subclasses django.db.models.Model. The standard convention is to use from django.db import models and to refer to the Django model class as models.Model.

A class corresponds to a single database table. More precisely, class attributes map to the database columns.

#### Fields

The term *field* in Django is used interchangeably for both the class attributes and the table columns. Class attributes are of different Python types or class. Similarly, database columns are of different data types. The conversion between class and table data types is Django's responsibility for the officially supported databases. In addition, third-party database backends are also available.

After a class for a model is created, its fields are defined. Django brings its own built-in field types, named **<Foo>Field**. The standard convention is to use **from django.db import models** and refer to the Django field types as **models.<Foo>Field**.

### Django’s standard field classes

#### Numeric

* **IntegerField** — Represents an integer.
* **FloatField**, **DecimalField** — Represents a real number using the float or decimal type in Python. Decimal can represent monetary amounts more precisely without rounding issues because it tracks the decimal places.
* **AutoField**, **SmallAutoField**, **BigAutoField** — Represents an integer that is automatically incremented. It can be used for setting an identifier or primary key in a table. But, this is not necessary as it will automatically be added to your model if not specified. Use these fields to override the default behavior.
* **SmallIntegerField**, **BigIntegerField**, **PositiveIntegerField**, **PositiveSmallIntegerField**, **PositiveBigIntegerField** — Represents an integer with specific boundaries.

#### Text

* **CharField**, **TextField** — Represents a string or a large amount of text. You can specify the max_length parameter to ensure compatibility with the chosen database.
* **BooleanField** — Maps to true or false.
* **EmailField**, **URLField**,**UUIDField**, **GenericIPAddressField**, **SlugField** — Represents a string following a specific format. The term *slug* is a human readable unique identifier.
* **JSONField** — Represents JSON data supported by specific databases.
* **BinaryField* — Represents raw binary data using the bytes or bytearray type in Python.

#### Time

* **DateField** — Represents a date as a Python **datetime.date** instance.
* **TimeField** — Represents a time as a Python **datetime.time** instance.
* **DateTimeField** — Represents a date with a time as a Python **datetime.datetime** instance.
* **DurationField** — Represents a period of time as a **timedelta** type in Python.

#### File

* **ImageField** — Represents an image file. It can validate the nature of the file being an image. It also provides a full image URL, including a new authorization token if the image is on Amazon Simple Storage Service (Amazon S3).
* **FileField** — Represents a file of any type.
* **FilePathField** — Represents a string for a filename in a certain directory on the file system.

#### Misc

* **GeneratedField** — Represents a value computed by the database based on other fields in the model.

### Content of the Django application models.py file defining the Breed class

```
from django.db import models

class Breed(models.Model):
    name = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    height = models.DecimalField(max_digits=8, decimal_places=2, null=True)
```

### Arguments and validators

In the code there's the use of extra parameters with CharField and DecimalField. These are named *arguments*, *options*, or *argument options* in Django. They are used to validate the input values after creating instances of the class. Using arguments is not limited to these two field types.

There are specific arguments for specific types. Each type has its own documented arguments. The **max_length** of a **CharField**, for instance, defines the maximum number of characters a string can have. Django can validate this fact and eventually throw an error.

General options are available in all built-in Django field types. For example, the **choices** option limits the possible values of a field to a defined list. If you add a **CharField** color attribute to the **Breed** class, you could attach a list of 12 recognized colors for a dog breed. Only these 12 values will be accepted under the color attribute.

A Django *validator* can be used both to validate user inputs in a form and to validate a model's object. Note that validators are not enforced at the database level. They are Python code that is intended to catch errors prior to saving. In relation to the model's fields and their options, you can programmatically call the function **clean_fields()** on your model, inherited from the Model class. This will force internal Django validators to run based on fields arguments. It might validate that a numeric value is within specified maximum or minimum limits. It might ensure that a field is not empty or null. It can even validate that a field matches a specified regular expression pattern. From the previous code example, the **FloatField** fields have **max_digits** and **decimal_places** arguments. These act as validators by restricting the float values to a maximum number of digits before and after the decimal place.

### Custom fields

You are not limited to the built-in Django field classes, like EmailField. You can create your own by subclassing the generic Field class or one of its subclasses. 

You might need to create your own because built-in field types do not cover every possible database data type. This is certainly a rare use case. But, you will have to tell Django, in code, how to handle saving and loading the data.

A more common use case for creating your own field is when you want to be more precise in the string values that can be accepted by your model. For instance, the values must have a specific format, like a social security number or a bank account identifier. Django has specific string formats like email, URL, or IP, but that might not be enough in a particular context.

For a list of available fields for particular countries and cultures that you should check before creating your own field type, see [django-localflavor documentation](https://django-localflavor.readthedocs.io/). For example, in the US, **USSocialSecurityNumberField**, **USStateField**, and **USZipCodeField** might come handy. For another recommended package that has excellent support for validating phone numbers in many countries with **PhoneNumberField**, see [django-phonenumber-field](https://django-phonenumber-field.readthedocs.io/). If this is not fulfilling your needs and you need more information, see [How to create custom model fields](https://docs.djangoproject.com/en/stable/howto/custom-model-fields/) on the Django documentation website.

### Methods

Your models inherit methods from the Model class. The following methods can be overridden:

* **clean()** — This method can be implemented to provide custom model validation, especially combining multiple fields. It can also correct and reformat the attributes if desired. The Model's method full_clean() calls both clean() and clean_fields().
* **__str__()** — It can provide a human-readable representation of an object by returning a string built from a combination of the fields' values. This method is invoked when the str() method is called on an object. This will have a visible effect on the admin web interface where objects are listed.

### Relationships among models

An application might use multiple models that have dependencies among them. For example, in a retail store, orders are made of product references. Are users allowed to remove a product without removing all the orders related to the product? Some business rules will have to be embedded in your data modeling. As a consequence, some model attributes must refer to other models. And this is why relational databases are used.

Django has the following three field types to model various real-world relationships between entities in a database:

* **ForeignKey** — Defines a many-to-one relationship between two models. For example, a VetVisit model might have a **ForeignKey** to a Pet model. Visiting a vet is for a specific pet, and the pet will possibly make several visits in their lifetime.
* **OneToOneField** — Is similar to a **ForeignKey**, but it ensures only one related object can exist. For example, a Pet model with a **OneToOneField** to a VaccinationCard model means each pet can have only one vaccination card and each card belongs to one pet.
* **ManyToManyField** — Defines a many-to-many relationship between two models. For example, a Pet model with a **ManyToManyField** to the Breed model means a pet is of one or mixed (multiple) breeds. Going the other way, many pets in your database might belong to the same breed.

## Model Creation and Migration

### Model creation

You can approach model creation in two steps—first by designing a data model and then by implementing it in Django.

#### Design Example

* A **pet** has a name, gender, birth date, and owner. The latest measured weight and height might also be available. A pet might visit a vet regularly, so the history of visits should be retained. A pet is of one or multiple breeds and has one vaccination card.
* A **vet visit** concerns a single pet. It shows the name of the vet, the visit date, and notes taken by the vet about the visit.
* A **vaccination card** must show the latest date of each vaccination. The rabies vaccination is compulsory and must be present on each existing card. The model should also support major vaccinations.
* A **breed** is recognized by its name, like *beagle*. The average weight and height for each breed might also be available.

#### Implementation Example

All classes are placed in the same models.py file in the pets_app application folder.

##### Breed class

The **Bree**d** class inherits **models.Model** and includes three fields. Argument options are used for future validations.

The breed name must be of 100 characters maximum, specified by **max_length**. The weight and height are eight digits with two decimals specified by **max_digits** and **decimal_places**.

Each field in a model class has a **null** option with a default value of False, which means that the field must not be null. For weight and height, because they can be null, **null=True** is added.

Overriding the **__str__()** function displays an object as a string in a human readable form of your choice. The function takes the **self** argument, which refers to the object itself when **str(a_breed)** is called.

```
from django.db import models

class Breed(models.Model):
    name = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    height = models.DecimalField(max_digits=8, decimal_places=2, null=True)

    def __str__(self):
        return self.name + " - " + str(self.weight) + " - " + str(self.height)
```

##### VaccinationCard class

```
from django.db import models
from datetime import datetime

class VaccinationCard(models.Model):
    rabies = models.DateField(default=datetime.today().strftime('%Y-%m-%d'), null=False, blank=False)
    hepatitis = models.DateField(null=True, blank=True)
    borrelia = models.DateField(null=True, blank=True)
    distemper = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.id) + " - " + str(self.rabies)
```

The **VaccinationCard** class includes four fields of type **DateField**. Each field represents the date that the associated vaccination was last given.

For the rabies field, the **default** argument option initializes the field to today's date using the **datetime** utility. That way, if a user creates a card and does not specify a value for the field, Django will default to today's date.

Only the first field is compulsory, which is visible through the **null** option. The **null=False** argument is not necessary, because *False* is the default, but it's informative to the reader when comparing with other fields.

While overriding the **__str__()** function, the **self.id** is used. This id field is not defined in the class but is automatically generated by Django as a default primary key.

##### Gender class

```
from django.db import models
from django.utils.translation import gettext_lazy as _

class Gender(models.TextChoices):
        FEMALE = "F", _("Female")
        MALE = "M", _("Male")
```

The **Gender** class is not a model because it subclasses **models.TextChoices** instead of **models.Model**. These text choices work similarly to **enum** from Python’s standard library.

A **.label** property from **TextChoices** is added onto values to return the human-readable name. The code **_("Female")** is a label property. The underscore indicates that this is a translatable string with help from a Django utility.

##### Pet class

```
from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=6, choices=Gender.choices, default=Gender.FEMALE)
    birth = models.DateField(default=None, null=True, blank=True)
    owner = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    height = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    card = models.OneToOneField(VaccinationCard, on_delete=models.CASCADE)
    breed = models.ManyToManyField(Breed, blank=True)
    
    def __str__(self):
        return self.name + " - " + self.gender + " - " + str(self.birth) + " - " + self.owner
```

The **Pet** model class includes a variety of fields.

The gender **CharField** argument **choices** points to the possible values from the Gender text choices. It has a **default** value of **Gender.FEMALE** in case no value is specified for the field when a pet instance is created.

The card **OneToOneField** has an **on_delete** option. The value is **models.CASCADE**, which means that if a **pet** is deleted, the attached card will also be deleted.

##### VetVisit class

```
from django.db import models
from datetime import datetime

class VetVisit(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    vet = models.CharField(max_length=100)
    date = models.DateField(default=datetime.today().strftime('%Y-%m-%d'))
    notes = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.pet.name + " - " + self.vet + " - " + str(self.date) + " - " + self.notes
```

* The **pet ForeignKey** has an **on_delete** argument, indicating that this visit will be deleted if the corresponding animal gets deleted.
* The vet field has a **max_length** argument to limit the vet's name to 100 characters.
* The **date** field sets today's date as a **default** value.
* The **notes** field accepts **null** or **blank** values.

##### Complete model.py example

```
from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _

class Breed(models.Model):
    name = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    height = models.DecimalField(max_digits=8, decimal_places=2, null=True)

    def __str__(self):
        return self.name + " - " + str(self.weight) + " - " + str(self.height)

class VaccinationCard(models.Model):
    rabies = models.DateField(default=datetime.today().strftime('%Y-%m-%d'), null=False, blank=False)
    hepatitis = models.DateField(null=True, blank=True)
    borrelia = models.DateField(null=True, blank=True)
    distemper = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.id) + " - " + str(self.rabies)

class Gender(models.TextChoices):
        FEMALE = "F", _("Female")
        MALE = "M", _("Male")

class Pet(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=6, choices=Gender.choices, default=Gender.FEMALE)
    birth = models.DateField(default=None, null=True, blank=True)
    owner = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    height = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    card = models.OneToOneField(VaccinationCard, on_delete=models.CASCADE)
    breed = models.ManyToManyField(Breed, blank=True)
    
    def __str__(self):
        return self.name + " - " + self.gender + " - " + str(self.birth) + " - " + self.owner

class VetVisit(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    vet = models.CharField(max_length=100)
    date = models.DateField(default=datetime.today().strftime('%Y-%m-%d'))
    notes = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.pet.name + " - " + self.vet + " - " + str(self.date) + " - " + self.notes
```

### Model migration

In Django, *migration* is used to propagate the changes you make to your models into your database schema. After your models.py is fully coded, you push it to the database to create the tables defined in the models. The Django manage.py utility is used for that purpose. The same procedure must be run each time you edit the file, at the class level or the field level, even for options that don’t affect the database.

After modifying at least one of your models, the following two commands must be used:

* **makemigrations** analyzes the coded models and prepares new migrations. The model changes are packaged into individual migration Python files under the migrations folder in each application, like pets_app/migrations.
* **migrate** applies the prepared migrations. The database schema is often impacted.

```
./manage.py makemigrations
./manage.py migrate
```

**makemigrations** and **migrate** apply all changes made in the models to synchronize them with the database. Tables are created or updated.

The migration generates the tables. Each table has an identifier, called **id**, because, in our examples, our models did not explicitly define a primary key. This extra identifier field becomes the default primary key.

In the example above, five tables are generated from four models. The extra table is created by Django to implement the many-to-many relationship between pet and breed, because a pet can be multiple breeds. The table is called pets_app_pet_breed, and it points to pets_app_pet and pets_app_breed to contain the cross reference between pets and breeds.

* To learn more, see [Migrations](https://docs.djangoproject.com/en/stable/topics/migrations/) on the Django website.

## Data Operations Through a Model

### Interfaces and programming languages

1. **Data storage**. After a model is defined and migrated, the corresponding table exists in the database. All save() calls on the model will commit changes to the database.
2. **SQL client**. Because a table is an artifact in a relational database, SQL can be used from a SQL client to make changes. This path does not use the model or its field validations.
3. **Django data API**. The Python data API can be used from the Django shell or in a Python script to input and modify data by instantiating the model class.
4. **Django utility**. The command line interface Python script manage.py comes with a utility called loaddata that can input a data file with all the data listed. YAML, JSON, and XML are supported.
5. **Built-in web interface**. An admin user can use the admin interface if the corresponding built-in application is kept in the Django project. The admin user navigates the exposed models and edits the data.
6. **Custom application**. The only way end users can modify data is if the application implements a way for users to input data. This can be achieved through a Django form in Python that is connected to a specific model. After a view makes use of the form, users can interact with it.

### Database SQL client

The natural and non-Django approach to manipulate data in a relational database is to install and use a compatible SQL client.

#### sqlite example

```
sqlite3 -line db.sqlite3 '.tables'
sqlite3 -line db.sqlite3 'SELECT count(*) FROM pets_app_breed'
sqlite3 -line db.sqlite3 'SELECT * FROM pets_app_breed LIMIT 5'
```

Three commands that will list the tables in the database, count the number of rows in a table, and return the first five rows from the table.

#### mysql example

```
mysql -h localhost -P 3306 -uadmin -e "USE pets_db; SHOW TABLES;"
mysql -h localhost -P 3306 -uadmin -e "USE pets_db; SELECT count(*) FROM pets_app_breed;"
mysql -h localhost -P 3306 -uadmin -e "USE pets_db; SELECT top 5 * FROM pets_app_breed;"
```

Three SQL commands that will list the tables in the database, count the number of rows in a table, and return the first five rows from the table.

This method is convenient for reading and verifying data, but it might not be convenient for modifying data. The drawback is that some of the formatting constraints specified in the model might not be enforced. Here, the developer passes by the model to work directly on the database.

### Django model data API

After you define your data models through your own Python classes, Django offers a Python API to CRUD objects. This API can be used in the views of your Django application, in the Django shell, or in a Python script.

the Django shell is an interactive Python interpreter with the Django settings loaded. You can use it to import your models and use the data API. the following commands access and exit the shell.

```
./manage.py shell
>>> # enter your Python code here
>>> exit()
```

The shell is opened with the **shell** command and closed with the **exit()** method.

#### Object creation

A model in Django is a class. You can instantiate the class by creating objects. Because the class is a subclass of **models.Model**, several inherited methods are available. The **full_clean()** method is used to validate the values, although calling it is optional. The **save()** method is used to commit the changes to the database.

In the following example, a new breed is created by instantiating the **Breed** class. The instance fields are validated. The data is saved in the database. Note that after the data is persisted, Django sets the Python instance's default primary key, **husky.id**, to an integer value.

```
from pets_app.models import Breed
husky = Breed(name='Husky', weight=10, height=10)
husky.full_clean()
husky.save()
```

#### Object lookup

The **models.Model** class has an objects attribute that represents the rows in the database table. **all()** and **filter()** functions are exposed through objects. The **all()** function returns the full list, and the **filter()** function applies some filtering by passing a lookup name from the model attributes and some value. More complex lookups can be done with operators.

The following example uses the **objects** attribute to perform two lookup queries. The first lookup uses the **all()** method to return all the pets in the database. The second lookup uses the **filter()** method to return the female pets only.

```
from pets_app.models import Pet, Gender
all_pets = Pet.objects.all()
females = Pet.objects.filter(gender=Gender.FEMALE)
```

#### Object update

To modify a row from a database, you need to retrieve the row first though a lookup. After the object is obtained, attributes can be modified, and the object can be saved, propagating the changes into the table. Conveniently, the **save()** method determines whether it needs to perform a SQL **INSERT** or **UPDATE** query based on whether the model instance has a primary key value.

The following example shows how to update the date for the latest rabies vaccine for a dog named Rocky. First, Rocky's vaccination card is retrieved through a lookup. Then, the rabies attribute is modified with today's date using a utility. Finally, the data is validated, and the card is saved.

```
from pets_app.models import Pet
from django.utils import datetime
rockys_card = Pet.objects.filter(name="Rocky")[0].card
rockys_card.rabies = datetime.today().strftime('%Y-%m-%d')
rockys_card.full_clean()
rockys_card.save()
```

When you need to update one or multiple rows at the same time, the **update()** method can be used. This can be applied after a lookup retrieving a number of rows.

In the following example, you can see the vet name being updated on all **VetVisit.objects **corresponding to that person. This happens in a single call using the update() method, and the field to be updated is **vet**.

```
from pets_app.models import VetVisit
VetVisit.objects.filter(vet="Jane Roe").update(vet="Jane Doe")
```

#### Object deletion

The **models.Model** class has a **delete()** function. But first, similar to an object update, you need to get the data from the database through a lookup. The **delete()** function will then issue a SQL **DELETE** for the object.

The following example fetches the husky breed in the database and deletes it.

```
from pets_app.models import Breed
husky = Breed.objects.filter(name="Husky")[0]
husky.delete()
```

Note that after the **delete()** function is called, the Python instance still exists. It still has data in its fields, except the primary key, which is id, is set to **None**.

For more information, see [Making queries](https://docs.djangoproject.com/en/stable/topics/db/queries/) on the Django website.

### Django utility

Object creation can be automated through data files. The manage.py CLI has a **loaddata** command which is convenient for initializing and populating multiple databases for different developers in a team or different environments, like dev, test, staging, and production.

In Django, the collection of data stored in files is a called *fixture*. With fixtures, you can decouple data from code. Fixtures can live in version control and be shared across environments. They contain serialized data that matches the structure of your models and database schema. They can be implemented in JSON, YAML, and XML formats.

The following is an example of fixtures described in YAML for the Pet application models. YAML has a more concise syntax than JSON or XML, and it is more convenient to display and read in this example. But JSON or XML could also be used.

#### Fixture for Buddy the dog

The data is listed in a single file to define one pet named Buddy. This is a good strategy when you need to add dependencies between models because the order in the same file has no effect. So, the new pet and breed will be created without error, even if the breed is declared after.

```
- model: pets_app.Pet
  pk: 1
  fields:
    name: Buddy
    gender: M
    birth: 2022-03-24
    owner: Mateo Jackson
    weight: 15
    height: 12
    card: 1
    breed: [1, 2]

- model: pets_app.Breed
  pk: 1
  fields: 
    name: Golden Retriever

- model: pets_app.Breed  
  pk: 2
  fields:
    name: Labrador

- model: pets_app.VaccinationCard
  pk: 1
  fields:
    rabies: 2022-06-01 
    
- model: pets_app.VetVisit
  pk: 1
  fields:
    pet: 1
    vet: Jane Doe
    date: 2022-04-30
    notes: healthy puppy
```

The fixture displayed in this example will create the following:

* **One Pet** — Start here by describing a male pet named Buddy that was born in 2022. His owner is Mateo, and you can see the latest known weight and height. Buddy has vaccination card number 1. Buddy is a mixed breed from breed 1 and 2, which is golden retriever and Labrador retriever.
* **Two Breeds** — Two new breeds are listed for retriever and Labrador. The average weight and height are not included. The model allows null values for these two fields.
* **One VaccinationCard** — The card number 1 is added. It belongs to Buddy. It shows the latest vaccine against rabies, which is compulsory. No other vaccine has been given.
* **One VetVisit** — A visit to the vet, Jane, for Mateo's dog Buddy shows he was a healthy puppy a month after his birth.

The **pk** field stands for *primary key*. It acts as an alias and points to the defined primary key field or to the default **id** field, if not defined.

After the fixtures are edited, it is a straightforward process to load the data. It's a good practice to place your fixtures files in the fixtures directory of every installed application, by placing data.yaml, for instance, under **pets_app/fixtures/**. That way, **loaddata** will be able to find the file without specifying a path.

The **./manage.py loaddata** command can take one file or multiple files as an argument. This comes in handy if there are dependencies between fixtures in separate files and objects must be loaded in a defined order. All files can be loaded at once, as if all the fixtures were placed in one single file. In that case, the loading order does not matter because Django will take care of the dependencies. Note that the file extension, such as *.yaml*, is optional.

Using YAML as a data format is supported by Django but requires the PyYAML dependency to be preliminarily installed through pip. The following command installs the PyYAML dependency.

```
pip install pyyaml
./manage.py loaddata data.yaml
```

The **loaddata** command populates the database with fixtures defined in a YAML file.

For fixtures in JSON format, there is no dependency to preinstall.

```
./manage.py loaddata data.json
```

The **loaddata** command populates the database with fixtures defined in a JSON file.

The utility will use the validations from the models. If no error is detected, new entries are committed to the database in one or more tables. You can use a SQL client to verify that the data persisted.

You can edit the data file and rerun the command to override the data in the database. That way, it's used to update the data. The **pk** elements in the data file define which rows are created or updated in the database tables.

Fixtures can also be generated from the data already in the database using the **./manage.py dumpdata** command. This provides a convenient way to transfer data from one database to another through files.

### Django admin web interface

The Django administration application comes with a backend interface to manage content in the database through all the models you choose to expose. With this tool, you can add, edit, and delete data without having to write custom views and forms. In addition, it has built-in functions, like search, filters, date drill down, and an inline interface for related models.

Follow these instructions to view and edit data in the Django administration interface.

1. Add the following line of code to your **settings.py** file to exempt any requests from https://\*.amazonaws.com from Cross-Site Request Forgery (CSRF) protection: **CSRF_TRUSTED_ORIGINS = ['https://\*.amazonaws.com']**
2. Add the models you want to expose for administration in your application **admin.py** with a new line per model, such as **admin.site.register(Breed)**.
3. Create a Django admin user by using the **./manage.py createsuperuser** CLI command.
4. Open the **/admin** URL of your running Django project and provide the created username and password.
5. Browse models and edit their corresponding data.

#### Possibilities in the graphical interface

1. **Django administration**. The admin web interface is accessible with admin credentials at the /admin URL.
2. **Models**. The models from models.py that are also listed in admin.py are visible on the left side.
3. **Choices**. Model fields with a choices option pointing to a list of acceptable values are automatically formatted. The menu includes a list of possible values.
4. **Date picker**. Date fields are formatted with a date picker.
5. **One-to-one menu**. The model Pet has a one-to-one relationship with another model, VaccinationCard. The list of already existing cards is in a dropdown menu. There is an option to search or create cards with additional buttons.
6. **Many-to-many selector**. The model Pet has a many-to-many relationship with another model, Breed. The existing breeds are listed for selection. You have the option to create a new breed if one is missing.
7. **CRUD operations**. The save buttons will commit the changes to the database. Deletion of an existing pet record is possible by using the Delete button.

### Django forms

Through HTML forms, users can get new data in a database. The application must include a form for users to complete. They might need to create or edit a user profile, do a money transfer, or enter passport information for a flight ticket.

With Django, you can map a form to a **Django form** that is using one or more Django models. Django forms provide a standardized way to design, validate, and process data submitted from an HTML form to the server in a Django application. They streamline working with user-submitted data.

A Django form is a Python class that is used to manage and validate user-entered data. The form you define inherits from **django.forms.Form** or **django.forms.ModelForm**. The latter is used when you want the form to interact with and save data to a model. Django automatically generates form fields based on the model fields, so the fields are not programmatically defined by the developer. The validation is tied to the model's field attributes and definitions.

For example, your application could use the following ModelForm for the simple Breed model.

```
from django import forms
from .models import Breed

class BreedForm(forms.ModelForm):
    
    class Meta:
        model = Breed
        fields = ('name', 'weight', 'height')
```

### [Lab: Creating Data Models in a Web Framework](./labs/W040Lab2DjangoModels.md)

### Knowledge Check

#### What is the meaning of migration in Django?

* To propagate model changes into a database schema

Wrong answers:

* To move a model from one Django application to another
* To transfer a model to the AWS Cloud
* To deploy a Django project to production

##### Explanation

When you create a new model, modify it with a new or edited field, or delete a model, this has a consequence on the table schema in your database. Migrating is a way to propagate the model changes into the database schema.  A migration can be done automatically with a command line utility.

#### What is the default data type and field name of a primary key in a Django model if the primary key is not explicitly specified?

* models.IntegerField id

Wrong answers:

* models.IntegerField pk
* models.CharField pkey
* models.CharField unique

##### Explanation

The default field name for the primary key in a Django model is **id**. When you create a model in Django without explicitly specifying a primary key, Django will automatically add an **IntegerField** named **id** to use as the primary key for that model. The **pk** field exists and, as an alias, always points to the primary key, whether it is declared or the default.

#### Which field argument name is used to limit the value to only a defined set of values?

* choices

Wrong answers:

* list
* options
* alternatives

##### Explanation

The **choices** argument constrains the value to a set. When choices are given, they are enforced by model validation. They also impact forms because the default form widget will be a select box with these choices instead of the standard text field.

### Summary

* A model in Django is a class that inherits from **django.db.Model** with data fields.
* A model field might be of one of the many built-in data field types, like **CharField**, or a custom type. Two models can be linked to each other by using one of the three relational field types, which are **ManyToManyField**, **OneToOneField**, and **ForeignKey**.
* Model instance data can be validated before being saved by using field arguments, also called **options**. As an example, an empty value can or cannot be accepted by setting **blank** equals true or false.
* The process of migration translates new or updated models to a refreshed database schema.
* There are different interfaces to create, read, update, and delete data through Django models. The **data API** can be used through the Django shell. It includes a way to look up data with filtering on. The Django administration interface is available to administrative users. The **loaddata** utility is used to batch data in from files. Finally, custom webpages can be created for end users to enter new data through Django forms.
