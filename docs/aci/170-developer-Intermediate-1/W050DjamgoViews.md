# Week 5: Django Views

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to repo's main [README.md](../../../README.md)

## Django Views

### Pre-assessment

#### Which responsibilities does a view have in a Django application? (Select TWO.)

* Perform the application’s business logic
* Return a response to the client

Wrong answers:

* Access the application’s database
* Route an incoming request to a model
* Secure an incoming request using TLS

##### Explanation

* Access the application's database
 * While views often interact with the database indirectly through models, direct database access is not a primary responsibility of views. Models handle database interactions in Django's MTV (Model-Template-View) architecture.
* Route an incoming request to a model
 * Routing is handled by Django's URL configuration, not by views. Views receive requests after they've been routed.
* Secure an incoming request using TLS
 * TLS (Transport Layer Security) is typically handled at the server level or by a web server like Nginx or Apache, not at the application or view level in Django.

#### Which server-side component maps the URL path of an incoming request to a view in a Django application?

* Django framework

Wrong answers:

* Application view
* Application model
* Application template

##### Explanation

* Application view
 * While views are the destination of the URL mapping, they are not responsible for the mapping itself. Views handle the logic of processing requests and returning responses, but they don't determine which URL leads to them.
* Application model
 * Models in Django represent the data structure and database schema. They are not involved in URL routing or mapping URLs to views. Models deal with data manipulation and storage, not request handling or routing.
* Application template
 * Templates in Django are responsible for presenting data and defining how it should be displayed to the user. They are typically the last step in request processing, after the URL has been mapped to a view and the view has processed the request. Templates do not play a role in URL mapping.

#### Which function can a developer use to define the URL mapping for a Django view?

* path()

Wrong answers:

* map()
* write()
* geturl()

##### Explanation

You use the write() function to write HTML content to a Django HttpResponse object. The map() and getURL() functions are JavaScript functions.

### View Definition

The Django framework uses the Model-View-Template (MVT) design pattern to structure a web application into layers. The *model* manages the application data and persists it to a database. The *template* presents the data as HTML. The view processes the web request from the user and returns a web response. Typically, the view accesses the model and decides what data to send back to the user. It contains the application's business logic, which determines how to access the model. The view also typically uses a template to build the response containing the data that is sent back to the user.

### How a view works

In a Django application, the view is the server-side component that receives an HTTP request and returns an HTTP response. When the browser sends an HTTP request to the application, a view defined in the application receives the request, runs the business logic to process the request, and returns an HTTP response.

1. **Client request**. The web browser sends an HTTP request to the Pets application to retrieve a list of all of the pets in the database. The HTTP request has a method attribute with a value of **GET** and a path attribute with a value of **/pets**. The request also has a host header with the value of the Pets application's host name, **www.example.com**.
2. **URL mapping**. On the server, the Django framework maps the URL path of the request to a view defined in the application. Django uses the project's URL configuration file named **urls.py** to determine the name of the view that is associated with the URL path.
3. **URL configuration file**. The configuration file contains a variable named **urlpatterns** that defines the mappings between URL paths and views. Django selects the first mapping that matches the URL path of the request. In this example, the **/pets** URL path is mapped to the **listPets** view defined the **views.py** file.
4. **View invocation**. As a result of the URL mapping, Django invokes the **listPets** view function and passes the request to it as a parameter. The function runs the business logic to retrieve and return the list of pets. The logic steps consist of accessing the Pets model, rendering the template, and returning the response.
5. **Model access**. To retrieve the list of pets from the database, the view uses the **Pets** model class in the **models.py** file. Specifically, the view invokes one of the data access methods defined in the class.
6. **Template rendering**. Then, the view renders the associated template's HTML code by passing it the pets data retrieved from the model. Rendering replaces the variable placeholders in the template with the actual values returned by the model.
7. **Response return**. Finally, the view puts the rendered template in the body of an HTTP response and sends the response to the client.

### Types of views

A view can be implemented in one of two ways in Django: using a function or using a class.

#### Function-based view

A function-based view is a simple Python function that takes an object of type HttpRequest as its first parameter. This object contains the data from the incoming HTTP request. The function defines all the code that implements the business logic for the view. When the logic finishes running, the function returns an object of type HttpResponse.

The pseudocode for the function is as follows:

```
# Function-based views.py - Listing pets example

def listPets(request):
   # Access the Pets model.
   ...
   # Render the petsList.html template.
   ...
   # Return the response.
```

#### Class-based view

A class-based view is a Python class. As such, it supports object-oriented principles such as inheritance and polymorphism, which promote code reuse and extensibility. You can build a class inheritance hierarchy for the views in your application that abstracts the implementation of common repetitive code, such as the rendering of common template elements. Django provides a base class named View that you can subclass to create a view. This class defines properties and methods that give you the ability to respond to different HTTP request methods.

In addition, Django provides a list of prebuilt view classes called generic views that you can readily subclass. Generic views contain built-in code that performs the common tasks of listing, creating, reading, updating, or deleting objects using models and templates. Many times, a developer can use these views to reduce the amount of code that they need to write and speed up development. The generic view classes include ListView, CreateView, DetailView, UpdateView, and DeleteView. The following table provides a summarized description of each of these classes:

| Generic View Class | Description |
| ------------------ | ----------- |
| ListView | Displays a list of objects from a model |
| CreateView | Displays a form to create an instance of a model object |
| DetailView | Displays the attribute values of a model object |
| UpdateView | Displays a form to update the attribute values of a model object |
| DeleteView | Displays a confirmation page and deletes an existing object from a model |

```
# Class-based views.py - Listing pets example

class PetsListView(ListView):
    model = Pets
    template_name = "petsList.html"
```

Class-based view implementation uses the methods defined in the ListView superclass to run all of its logic. The listView class implements the behavior to list all the objects from the Pets model using the petsList.html template.

## URL Mapping

The purpose of URL mapping is to route the HTTP request sent by the browser to an appropriate view function based on the URL path contained in the request. The Django framework uses the file named **urls.py** in a project to perform the mapping. Specifically, Django uses the mapping defined in the Python list urlpatterns variable to find a match for the URL path and determine the view function to invoke.

### URL pattern format

The ***urlpatterns** list defined in a **urls.py** file has the following format:

```
urlpatterns = [pathMapping1, pathMapping2, ..., pathMappingn]
```

Each element of the list is a path mapping. It maps a URL path to a view function using either the path() or re_path() function. Both functions accept the same parameters but differ in the way that you specify the URL path pattern corresponding to a view function. The function signatures of the path() and re_path() functions are as follows.

```
path(route, view, kwargs=None, name=None)
```

```
re_path(route, view, kwargs=None, name=None)
```

### urlpattern parameters description

#### route

The route parameter is a string that represents the URL pattern that Django uses to match the requested URL. For the path() function, the value of the parameter is a *URL path literal*, such as "pets/". For the re_path() function, the value is a *regular expression literal*. It is typically expressed using the raw string syntax of r"", for example, r"^pets/$".

You can also mark part of the URL pattern as variable using angled brackets. When Django matches the pattern with the URL path of an incoming request, it captures the value in the incoming URL at the position where the variable is defined, and passes it to the corresponding view as a keyword argument. For example, suppose you have defined the following URL mapping:

```
path("pet/<str:pet_id>", views.pet)
```

The **<str:pet_id>** variable tells Django that only incoming URL paths that have a string after **"pet/"** will match this pattern. In addition, when a match occurs, Django will retrieve the value of the string in the incoming URL and assign it to a variable named pet_id.  Django will then pass this value as a keyword argument to the corresponding view. For example, if the incoming URL path is "/pets/12", Django will match it to the defined mapping and pass the pet_id=12 keyword argument to the pet view.

#### view

The view parameter specifies the view function or class that Django invokes when the URL path of the request matches the route pattern.

To invoke a view function, you specify the name of the function. For example, to invoke a function named listPets() in the views.py module, you can define the following URL mapping:

```
path("pets/", views.listPets)
```

To invoke a view class, you specify the result of sending the as_view() method to the class. This method returns an instance of the class. For example, to invoke a view class named PetsListView in the views.py module, you can define the following URL mapping:

```
path("pets/", views.PestsListView.as_view())
```

#### kwargs

With this optional parameter, you can pass additional information to the view when Django invokes it. This information should be a dictionary of keyword arguments. For example, consider the following URL mapping definition:

```
path("pets/dogs/", views.listPets, {"filter": "dogs"})
```

When Django receives a request with a URL path of **/pets/dogs/**, it will call **views.listPets(request, filter="dogs"')**. The view can then use the additional filter argument in its business logic to return only the list of pets that are dogs.

#### name

The name parameter is an optional keyword argument that identifies the view. The argument's key must be "name". This parameter is useful in situations where you need to retrieve the URL of the view that is defined in the mapping.

For example, suppose that you have defined the following URL mapping:

```
path("pets/", views.listPets, name="petsList")
```

If, in some other view, you want to access the URL of the listPets view, you can use the **reverse()** function as follows:

```
url = reverse("petsList")
```

Django assigns the URL value of **"/pets/"** to the url variable. You can then use the variable to invoke the listPets view.

The following is an example of two URL mapping definitions that are equivalent to each other. The first one uses the path() function, and the second one uses the re_path() function.

```
# URL mappings defined with path() function

urlpatterns = [
    path("pets/", views.listPets, name="petsList"),
    path("pet/<str:pet_id>", views.getPet, name="pet")
]
```

```
# URL mappings defined with re_path() function

urlpatterns = [
    re_path(r"^pets/$", views.listPets, name="petsList"),
    re_path(r"^pet/(?P<pet_id>\w+)/$", views.getPet, name="pet")
]
```

To match patterns that are more complex, for example a pattern that accepts a variable number or list of characters in a specific position, the re_path() function gives that capability.

### Using multiple URL configuration files

By default, Django uses the URL mappings defined in a project's urls.py file to map the URL path of an incoming HTTP request to a view function. This file is the root file for URL configurations and is defined in the project's settings.py file through the ROOT_URLCONF variable. For example, the settings.py file of the project named pets_project contains the following variable definition by default:

```
ROOT_URLCONF = 'pets_project.urls'
```

When you create an application for a project, one approach is to define all of the application's URL mappings inside of the project's urls.py configuration file. This approach is direct and suitable for a project that contains only one application. However, if the project contains or will contain multiple applications, a better approach is to define each application's URL mappings in separate configuration files. Each application defines its own urls.py file. You can then reference each application's configuration file in the project's urls.py file by using the include() function. By having a separate configuration file for each application, you do not need to modify the project level configuration when the URL mappings for an application change. This reduces the risk of changes in one application's configuration adversely affecting the other applications in the project.

#### multiple URL configuration files for a project example

In the example, a project named airlineWebsite_project contains three applications: Flights, Reservations, and Rewards. Each application defines URL mappings in its own urls.py file, and each file is referenced in the project's urls.py file using the include() function.

##### URL mappings at the project level

The URL mappings in the urls.py file for the airlineWebsite_project contain three definitions. Each definition corresponds to an application contained in the project and uses the path() function. The function for the Flights application has a route of **"flights/"** and an include() function that references the urls.py file in the Flights application. Similarly, the functions for the Reservations and Rewards applications have a route of **"reservations/"** and **"rewards/"**, respectively. They also have an include() function that references the application-level urls.py file.

##### URL mappings for the Flights application

The urls.py file for the Flights application defines two URL mappings. The first one maps an empty URL path to the **lookupFlights** view. The second one maps a URL path that contains an integer flight number to the **flightDetails** view. Note that both URLs are relative to the path that is defined at the project level, which is **"flights/"**.

##### URL mappings for the Reservations application

The urls.py file for the Reservations application defines two URL mappings. The first one maps an empty URL path to the **lookupReservations** view. The second one maps a URL path that contains an integer reservation number to the **resDetails** view.

##### URL mappings for the Rewards application

The urls.py file for the Rewards application defines two URL mappings. The first one maps an empty URL path to the **lookupRewards** view. The second one maps a URL path that contains an integer reward number to the **rewardDetails** view.

### Processing a Request and Producing a Response

After Django maps the URL path of an HTTP request to a view, it invokes the view and passes the request to the view. The view is responsible for accessing the request, performing the view's business logic, and producing a response to send back to the client. In this section, you explore how the view accesses the data in the HTTP request and review how the view interacts with the application's models.

#### Accessing data in the HTTP request

Django passes the information in an HTTP request to a view in an HttpRequest object. Django passes the object as the first parameter of the view function. This object contains all the data related to the request, including metadata. You can use the attributes and methods of an HttpRequest object to access the data that it contains. The following table lists and describes some commonly used attributes and methods of the HttpRequest object.

| Attribute or Method Name | Description |
| ------------------------ | ----------- |
| method | A string that specifies the HTTP method used in the request. |
| path | A string that contains the URL path of the request. |
| headers | A dictionary that contains the HTTP headers from the request. |
| GET | A *QueryDict* that contains the parameters that are passed in the URL query string. This attribute is populated when such parameters are present, even if the HTTP method is not GET. |
| POST | A *QueryDict* that contains the parameters of an HTTP POST request. This attribute is particularly useful for retrieving the values in a Django form. |
| get_host() | Returns the name of the host that originated the request. For example if the request is to https://www.example.com/pets, get_host returns www.example.com. |
| get_port() | Returns the port number used by the request. |

The GET and POST attributes contain an object of type *QueryDict*. This a special dictionary-type class that can accept multiple values for the same key. It is useful, for example, to capture the multiple values of a select element in an HTML form.

Also, the get_host() and get_port() methods are useful to determine the origin of the incoming request. A view might perform different logic based on the origin of a request. For example, a view might return additional diagnostic data in the response if the incoming request comes from a test or staging host.

#### Test Django application "Hello, <name>!"

Hello application that receives a person's name in a URL query string. The application then returns the message "Hello, <name>!" where <name> is the person's name.

##### Create a new application named hello_app in the django folder of the existing virtual environment

```
./manage.py startapp hello_app
```

##### Add application to settings.py in the INSTALLED_APPS list variable

```
    'hello_app'
```

##### Create a view

```
from django.http import HttpResponse

def sayHello(request):
    
    # Get the name parameter from the URL query string.
    
    name = request.GET.get("name")
    
    # Return an HTTPResponse with a "Hello" message that includes the name.
    
    return HttpResponse("Hello, {}!".format(name))
```

##### Define the URL mapping for the view

Define the URL mapping for the view in an application-level urls.py file and reference the file in the project-level URL configuration file. Create a file named urls.py in the hello_app folder:

```
from django.urls import path
from hello_app import views

urlpatterns = [
    path("", views.sayHello)
]
```

##### Edit project level urls.py

Open the urls.py file in the pets_project folder and add the following path definition to the urlpatterns list:

```
    path("hello/", include("hello_app.urls"))
```

##### Start the server

```
./manage.py runserver 0.0.0.0:8080
```

##### Test the application

```
https://somePrefix.amazonaws.com/hello/?name=John
```

### Interacting with models

 Django provides methods to create, retrieve, update, and delete (CRUD) a model. You can invoke those methods from a view to perform model operations based on the view's business logic. If you have defined additional methods in a model that are not private, you can also invoke those methods from the view. The following table lists the invocation sequence of common CRUD methods for a model and describes the objects that they return.

| Method Name | Description |
| ----------- | ----------- |
| aModelClass.objects.**create(kwargs)** | Creates an instance of **aModelClass** in the database with the fields and values defined in the **kwargs** keyword arguments. Returns the created object instance. |
| aModelClass.objects.**get(fieldName=value)** | Returns the object whose **fieldName**  is equal to **value**. The method expects to find only one match and returns an exception if otherwise. |
| aModelClass.objects.**all()** | Returns all the objects in the database for **aModelClas**s** in a QuerySet. |
| aModelInstance.**update(kwargs)**, aQuerySet.**update(kwargs)** | Updates the fields specified in the **kwargs** keyword arguments for **aModelInstance** or the instances in **aQuerySet**. A QuerySet is a collection of objects from the database. Returns the number of instances affected. |
| aModelInstance.**delete()**, aQuerySet.**delete()** | Deletes **aModelInstance** or the instances in **aQuerySet** from the database. Returns the number of objects deleted. |

### Producing a response

A view must return an HTTP response back to the client and can do it in two ways:

1. Directly return an HttpResponse object.
2. To render a template.

#### Rendering a template

A template is an HTML file that can contain placeholder variables for dynamic data. The view passes the values of the variables to the template, typically after retrieving them from models. To do so, the view invokes the render() function. This function is a shortcut function that accepts a request object, a template, and a context dictionary as arguments. The function sets the variables in the template with the values in the context dictionary, and returns an HttpResponse object with the rendered HTML.

#### Returning an HttpResponse object

When working with an HttpResponse object, you typically use the HttpResponse() constructor to set the content of the HTML page that you want to return. This constructor accepts a string or a byte string as an argument. You can also use the attributes and methods of an HttpResponse object to set the values of the data that it contains. The following table lists and describes some commonly used attributes and methods of the HttpResponse object.

| Attribute or Method Name | Description |
| ------------------------ | ----------- |
| status_code | The HTTP status code for the response. |
| headers | A dictionary that contains the HTTP headers for the response. |
| write(HTMLcontent) | Writes **HTMLcontent** to the body of the response. You can use this method to build the HTML response incrementally in the same way that you write to a file. |

##### HttpResponse object example

Creating a view function named listPets() in the views.py file in the pets_app folder. 

```
from django.http import HttpResponse
from .models import Pet

def listPets(request):
    
    # Retrieve all the pets from the database.
    all_pets = Pet.objects.all()
    
    # Build a page that displays the name, gender, owner, and birthdate of each pet.
    response = HttpResponse()
    response.write("<!doctype html>")
    response.write("<html lang='en'>")
    response.write("<head><title>Pets List</title></head>")
    response.write("<body>")
    response.write("<h1>List of Pets</h1>")
    
    for aPet in all_pets:
        response.write("<p>")
        response.write(f"Pet name: {aPet.name} <br>")
        response.write(f"Gender: {aPet.gender} <br>")
        response.write(f"Owner: {aPet.owner} <br>")
        response.write(f"Birthdate: {aPet.birth:%Y-%m-%d} <br>")
        response.write("</p>")
    
    response.write("</body>")
    response.write("</html>")
    
    # Return the response.
    return response
```

* The **listPets()** view function accesses the **Pet** model class to retrieve all the pets in the database. Specifically it sends the **object.all()** message to the class to retrieve a QuerySet named **all_pets** that contains all the pet objects.
* The function builds an HTTP response incrementally using the **HttpResponse()** constructor and multiple **write()** methods. Each invocation of the write() method adds an HTML fragment to the response body.
* To display the fields of each Pet object, the function uses a **for** loop to iterate over the **all_pets** QuerySet. For each pet, the loop writes each field label and value to the response body. The code uses a Python F-String to insert a field value into the HTML string.
* When all pets have been processed, the function returns the HttpResponse object.

Defining the appropriate URL mapping for the listPets view in the urls.py file in the pets_app folder in the **urlpatterns** list:

```
    path("pets/", views.listPets, name="petsList")
```

```
https://somePrefix.amazonaws.com/pets/
```

### [Lab: Creating Views in a Web Framework](./labs/W050Lab1DjangoViews.md)

### Knowledge Check

#### What is an advantage of using a class-based view instead of a function-based view?

* A class-based view can reuse code from a prebuilt generic view.

Wrong answers:

* A class-based view captures all the code that implements the view in a single component.
* A class-based view eliminates the need to use a template in a view.
* A class-based view performs faster than a function-based view at runtime.

##### Explanation

* A class-based view inherits code from its superclass. Therefore, its code is implemented in multiple components.
* A class-based view is a component the Model-View-Template (MVT) design pattern. It can and should use a template as part of its design.
* A class-based view's runtime performance depends on what its code does and might or might not be better than the performance of a function-based view.

#### Which variable contains the list of URL mappings in the urls.py file of a Django project?

* urlpatterns

Wrong answers:

* route
* ROOT_URLCONF
* INSTALLED_APPS

##### Explanation

* ROOT_URLCONF and INSTALLED_APPS are variables that are defined in a project’s settings.py file.
* Django does not define a configuration variable named route.

#### Which attribute of the HttpRequest object contains the parameters that are passed in the request’s URL query string?

* GET

Wrong answers:

* POST
* path
* headers

##### Explanation

* The POST attribute contains the parameters of an HTTP POST request.
* The path attribute contains the URL path of the request.
* The headers attribute contains the HTTP headers from the request.

### Summary

* A view is an application component that receives a request, processes the request, and returns a response. A view typically uses a model to access the application's database and renders a template to generate the HTML page that it returns in the response.
* Django supports two types of views, function-based and class-based. A function-based view is a Python function that contains all the code that implements the view's logic. A class-based view promotes code reuse and can inherit code from a Django prebuilt generic view.
* The Django framework routes an incoming request to the view that will process the request. By default, it uses the URL mappings defined in the urls.py file of the application's project to determine the route. You can define a URL mapping by using the path() or re_path() function.
* If a Django project contains multiple applications, a recommended practice is to define each application's URL mappings in its own urls.py file. You can then reference each application's urls.py file in the project-level urls.py file by using the include() function.
* A view must return an HttpResponse object to the sender of a request. It can do so by directly returning an HttpResponse object. Alternatively, the view can render a template and return the HttpResponse object that it receives from the rendering.
