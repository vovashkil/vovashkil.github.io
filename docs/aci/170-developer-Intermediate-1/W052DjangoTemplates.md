# Week 5: Django Templates

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to repo's main [README.md](../../../README.md)

## Django Templates

### Pre-assessment

#### What is the role of a template in a Django application?

* Define the web interface displayed in a browser.

Wrong answers:

* Present a graphical dashboard to operators with resource metrics.
* Structure the code in a multi-tier architecture.
* Embed the business logic in the presentation layer.

A template includes the presentation code, mainly as HTML, that defines the web interface in a client browser. It is not recommended to embed any business logic in templates. With Django, this logic belongs in a view instead.

#### Which languages are used in a Django template file? (Select TWO.)

* HTML
* Django template language (DTL)

Wrong answers:

* Python
* SQL
* JSON

The webpage structure and static content are coded in HTML. The dynamic parts come from data that is fetched using DTL.

#### How should a Django developer make use of an existing template?

* Render the template from a view.

Wrong answers:

* Render the template from a model.
* Render the template from middleware.
* Render the template from the command line interface (CLI).

A view implements the logic of manipulating data by using models. Then, the view places the data used by a template in a context variable. Finally, the view calls a function to render the template by passing the context as an argument.

## The Django Template System

### Purpose

Without a template, a view must return the content of a webpage directly to the browser client. This implies that your Python code will be cluttered with HTML code.

The main benefit of a template system is to keep your views HTML-free. The views implement the application logic by manipulating models. The templates display application data with a nice look-and-feel by focusing on the presentation. You get a separation between the logic and the presentation. It also makes both types of code easier to maintain and edit in an integrated development environment (IDE).

### Introduction to the Django template system

The **Django template system** is flexible and supports multiple implementations. These variants are called the **template backend** or **template engine** in Django documentation. Django comes with two implementations, one internal Django implementation and one external implementation called **Jinja2**. You can select one of them or a third-party implementation.

You can choose which template backend to use for your web application in the Django project **settings.py**. The **TEMPLATES** JSON variable includes a **BACKEND** property pointing to a Python package that represents the engine, as shown in the following example. By default, the value is **django.template.backends.django.DjangoTemplates**, which corresponds to the Django template backend. This default template engine provides a language called **Django template language (DTL)** to create templates.

#### TEMPLATES in settings.py

* **BACKEND** – A dotted Python path to a template engine class implementing Django’s template backend API
* **DIRS** – List of directories where the engine should look for template source files in search order—an empty list means **templates/** by default
* **APP_DIRS** – Boolean to tell if the engine should look for templates inside applications — **True** by default
* **OPTIONS** – Backend-specific settings for DTL. The **context_processors** are used to populate the context when a template is rendered with a request. Each element in the list defines a variable that a template can access in the context object

The DTL is the focus of the following instructions. To learn more about Jinja2 instead, visit [the Jinja documentation](https://jinja.palletsprojects.com/).

### DTL

DTL strikes a balance of power and simplicity for most web projects. With the template backend, you can mix in one HTML file for your presentation logic with extra tags and filters to insert dynamic data. The content of a template HTML file consists of HTML elements and DTL elements.

The following example shows the content of an HTML file as a template. It illustrates how using a variable called **name** can make the webpage more dynamic. The variable's value is inserted as text by typing the variable name inside double curly braces.

```
<html>

<body>
  <h1>Hello {{ name }}!</h1>
</body>

</html>
```

## Organizing and Referencing Templates

Templates are HTML files. They must be placed in directories that are recognized by the template backend. The template backend might be configured to look into specific directories listed in **settings.py**. If the **DIRS** list variable is left empty in the configuration, the template backend looks into the default directories. By default, templates are placed under the **<app>/templates/** folder, either directly or in sub-folders.

A best practice is to repeat the application name as a folder under **templates/** so the path of the HTML files is **<app>/templates/<app>/*.html**. Repeating the application name is recommended to avoid confusion when referencing templates in a project with more than one application. The following section explains how templates are referenced.

The following file tree structure shows where two template files, **pet.html** and **pets.html**, belonging to one application, **pets_app**, are placed.

```
.
├── manage.py
├── pets_project/
└── pets_app/
    ├── models.py
    ├── views.py
    ├── static/
    └── templates/
        └── pets_app/
            ├── pet.html
            └── pets.html
```

### Template inheritance

Usually each HTML file represents one webpage. In the preceding example, two webpages are designed, one to list all pets, **pets.html**, and one to show details about one pet, **pet.html**. After coding these templates, they might have a lot in common. The page structure and look and feel are the same. The header, top menu, side navigation, and footer are repeated. It is possible that only the middle section of the webpages might differ. To avoid code duplication, it is wise to place the common code in a **base.html** template file and refer to it from the two webpages.

This is called **template inheritance**, and it is a Django feature. You can use it to build a base skeleton template that contains all the common elements of your site. It defines blocks that child templates can override.

DTL permits extending a base template like this:

```
{% extends 'pets_app/base.html' %}
```

Note that the base template might be placed in the same application or in a different application. The consequence of using **extends** is that the block content in the parent template, defined as

```
{% block content %}
...
{% endblock content %}
```

is overridden by the corresponding block content in the child template.

1. **Base template**. The base template **base.html** defines all the common elements on the website. Here, you can find a banner div element and a footer div element. The background HTML color is lightpink.
2. **Block content**. This **skeleton** template indicates a placeholder for more specific content. This is achieved with the **block tag** and the **endblock tag**. The placeholder's name is **content**. This block part will be overridden by a child template with a block that has the same name.
3. **Child template**. The child template **pets.html** includes the **`extends`** element that points to the parent template.
4. **Child content**. The child template includes a **block** element and an **endblock** element. Inside, the code defines the content that overrides its parent. The background HTML color is lightblue.
5. **Preview**. The result of **rendering the child template pets.html** is a webpage made in pink by the parent template and in blue by the child template.

This example was simplified for clarity. In reality, the styling code-defining colors should be placed in a separate CSS file under the **static/** folder. The base template should include a **<head>** HTML element including a **<link>** element pointing to this style sheet.

### Referencing a template

You can reference a template from the following sources:

* A view using the Django Python library
* Another template using DTL

#### Referencing by inheritance

A child template invokes a parent template with the **`extends`** tag. The parent template can be referenced with an absolute path from the templates/ directory as in **`\{\% extends "pets_app/base.html" \%\}`** or with a relative path to the child template as in **`\{\% extends "./base.html" \%\}`**.

Child template -> (extends) -> Parent template

#### Embedding a template

A similar use case to inheritance is when you need to include a common HTML code in many templates. It is possible with DTL by using **`\{\% include "pets_app/contact.html" \%\}`**.

Template -> (includes) -> Common template

#### Referencing from a view

A view might return some HTML content directly like this: **`return HttpResponse('<h1>Hello from Pets application</h1>')`**. This class is imported from **django.http**. Although it might seem practical, mixing HTML in your Python code is an anti-pattern.

To separate the concerns, the view must use a template for presenting the data on a webpage by using the **render()** function from **django.shortcuts**. As an example, your view might render a template like this: **`return render(request, "pets_app/pets.html", context)`**. The template is always referenced with an absolute path from the **templates/** directory. The HTTP request and the context holding application data are passed as arguments. This context data can be accessed in the template.

View -> (Renders) -> Template

## Displaying Data from a View

Templates are mostly made of HTML code. You can also use DTL to enhance and add dynamic content to your webpage.

### Passing application data to a template

Your view is responsible for fetching and manipulating data that will be displayed in templates by using models. It also needs to find the proper template and complete its rendering. Your view function must complete the following four steps:

1. **Context** – Fetch and prepare the application data used later in the template and place the data in a Python dict.
2. **Template** – Fetch the template based on the configured engine.
3. **Content** – Render the template with the context data to obtain the plain HTML code content.
4. **Response** – Return an HTTP response with the HTML content as its body.

You can implement these four steps in multiple ways using the Django APIs, from low-level APIs to high-level APIs. Two convenient methods achieve the same result. In this example, you need to display a webpage for a particular pet.

#### Four-line implementation

The previously described steps are displayed. A **loader** from the **django.template** gets a **Template** object from the engine. This object has a **render()** function that takes the context data and the request data.

```
from .models import Pet
from django.template import loader
from django.http import HttpResponse

def pet(request, pet_id):
    # 1 - prepare application data in a context dict
    context = {'pet': Pet.objects.filter(id=pet_id).first()}
    # 2 - fetch the template for the configured engine
    template = loader.get_template("pets_app/pet.html")
    # 3 - render the template with the context data
    content = template.render(context, request)
    # 4 - return the HTTP response
    return HttpResponse(content)
```

#### Shortcut

This is a two-line implementation. The **django-shortcuts** module gives a **`render()`** function that encapsulates the template rendering for you.

```
from .models import Pet
from django.shortcuts import render

def pet(request, pet_id):
    # 1 - prepare application data in a context dict
    context = {'pet': Pet.objects.filter(id=pet_id).first()}
    # 2-3-4 - load template, render it and return the HTTP response
    return render(request, "pets_app/pet.html", context)
```

### Accessing data in a template

The data available in a template might come from the Django framework, like the **request** object, or directly from a view with the **context** object. There is no distinction within a template as to where the data is coming from. In fact, the **context** dict is internally expanded to include the request object. In the preceding code example, two variables called **pet** and **request** are made available from inside the template. The **pet** variable comes from the context because it was populated with **`{ "pet": ... }`**.

Access contextual data with **double curly braces**. Examples include **`{{ pet.name }}`** or **`{{ request.method }}`**. The following code shows how the **pets_app/pet.html** template can be implemented.

#### Pet template

In this example, only the **pet** object is used. The **request** object is not used. The pet model's fields can be addressed directly such as **pet.name**, **pet.birth**, or **pet.weight**.

A one-to-one relationship can also be reached and navigated as in **pet.card.rabies**.

The **gender** field is a **models.TextChoices** enumeration, and **pet.get_gender_display** is used to get plain English text (Female, Male) instead of a single letter (F, M) with **pet.gender**.

```
{% extends "pets_app/base.html" %}
{% block content %}
<div class="pet" style="background-color: lightblue;">

    <h2>{{ pet.name }} - WORK IN PROGRESS</h2>

    <div class="pet">
        Gender: {{ pet.get_gender_display }}<br/>
        Birth: {{ pet.birth }}<br/>
        Owner: {{ pet.owner }}<br/>
        <br/>
        Weight: {{ pet.weight }} lb<br/>
        Height: {{ pet.height }} in<br/>
        <br/>
        Vaccines: rabies {{ pet.card.rabies }} / 
            hepatitis {{ pet.card.hepatitis }}<br/>
        <br/>
    </div>
</div>
{% endblock content %}
```

## Template Language Tags and Filters

### Built-in template tags

Use template tags to induce presentation logic for how things should be displayed to webpage visitors. Tags are recognized in templates by curly braces with percentages as **`{% tag ... %}`**.

#### Template composition tags

The template inheritance **extends** tag is used to avoid repeating HTML code across multiple templates, and it signals that the current template is a child of a parent template. It works with two other tags called **block** and **endblock**. They delimit which part of the parent template will be overridden by the child template.

A similar tag called **include** has been introduced as a way of embedding a template within a template. For instance, **`\{\% include "pets_app/contact.html" \%\}`** will start a rendering process of a subtemplate with the same context data. You can pass extra parameters like this: **`\{\% include "pets_app/subheader.html" with title="Rocky" \%\}`**.

There are some key differences between **`extends`** and **`include`**. The **`extends`** tag must be the first tag in a template, while the **include** tag can be used anywhere. When using the **`extends`** tag, child templates **inherit** all block tags from the parent. The **`include`** tab simply renders the included template without inheritance.

The recommendation is to use the **`extends`** tag for the overall site templating, the **base.html**, where webpages share a common structure and styling. On the other hand, the **include** tag is useful for reusing the same pieces of code, like an internal header.

#### Linking tag

When you want to include a link on a webpage to another webpage, edit the first template, the **from-template**, to point to a second template, the **to-template**. This is achieved by using another Django template language tag called url.

The **`\{\% url 'pet' pet.id \%\}`** example is used to create a URL to the next template through its path and view. The first argument, **'pet'**, is the path name in **urls.py**. The second argument, **pet.id**, is a dynamic string element in the path. The corresponding path in **urls.py** could be **`path("pet/<str:pet_id>", views.pet, name="pet")`**. So, in this case, the url tag will resolve to a string like **`pet/42`**, for example. File paths and URL paths must never be hardcoded in a Django template. Instead, they must be resolved using tags.

##### The indirect reference from the from-template to the to-template, involving a path and a view

From template -> (Links to) -> Path -> (Calls) -> View -> (Renders) -> To template

#### Loops tags

If the view passes a list variable to a template, you need to iterate through that list to display its elements on the webpage. The **`for`** tag is used to loop over each item in an array. You can loop over a list by using **`{% for obj in list %}`** and in reverse order with **`{% for obj in list reversed %}`**. If the list is empty, you can use an optional **`{% empty %}`** clause whose following text is displayed. Finally, the loop ends with an **`{% endfor %}`** clause.

The **cycle** tag can be used inside a **`for`** loop. It takes a list of values as arguments and it returns one value in a round-robin way each time it is called. A classic use case for this tag is when you need to alternate between two background colors for table rows. Also, a cycle can be restarted from its first item with the **`resetcycle`** tag.

##### Listing all the pets from a pets variable example

```
{% extends "pets_app/base.html" %}
{% block content %}
<div class="pets" style="background-color: lightblue;">

    <h3>List of pets - WORK IN PROGRESS</h3>
    <table>
        <tr>
            <td>Name</td>
            <td>Gender</td>
            <td>Birth</td>
            <td>Weight</td>
            <td>Owner</td>
        </tr>
        {% for p in pets %}
        <tr style="background-color: {% cycle 'lightgrey' 'lightgreen' %};">
            <td>{{ p.name }}</td>
            <td>{{ p.get_gender_display }}</td>
            <td>{{ p.birth }}</td>
            <td>{{ p.weight }}</td>
            <td>{{ p.owner }}</td>
        </tr>
        {% empty %}
        <tr><td>No pet yet</td></tr>
        {% endfor %}
    </table>
</div>
{% endblock content %}
```

#### Choices tags

If you need to evaluate a variable to decide how the HTML code should be, the **`if`** tag is useful. The variable argument evaluates to **True** if it exists, it is not empty, and it is not a **False** Boolean value. You can output one branch or multiple branches with **`elif`** and **`else`**. Finally, the if tag block ends with an **`{% endif %}`** clause.

Continuing on the previous example, you can derive from the **Weight** column to a **Small**, **Medium**, or **Large** pet using an **if** tag.

```
{% extends "pets_app/base.html" %}
{% block content %}
<div class="pets" style="background-color: lightblue;">

    <h3>List of pets - WORK IN PROGRESS</h3>
    <table>
        <tr>
            <td>Name</td>
            <td>Gender</td>
            <td>Birth</td>
            <td>Size</td>
            <td>Owner</td>
        </tr>
        {% for p in pets %}
        <tr style="background-color: {% cycle 'lightgrey' 'lightgreen' %};">
            <td>{{ p.name }}</td>
            <td>{{ p.get_gender_display }}</td>
            <td>{{ p.birth }}</td>
            <td>{% if not p.weight %}
                -
                {% elif p.weight < 8 %}
                Small
                {% elif p.weight < 16 %}
                Medium
                {% else %}
                Large
                {% endif %}</td>
            <td>{{ p.owner }}</td>
        </tr>
        {% empty %}
        <tr><td>No pet yet</td></tr>
        {% endfor %}
    </table>
</div>
{% endblock content %}
```

#### Date and time tag

You do not need the view to place the current date and time in the context object. You can fetch it directly from the template using the **`now`** tag without any contextual information from the view. The tag is followed by the date formatting. For example, this tag **`{% now "F jS, Y, H:i T" %}`** might output **September 20th, 2024, 15:23 UTC**.

Continuing on with the previous example, you can modify the copyrights section in the base template to avoid hardcoding the year. This translates into: **`<p>&copy; {% now "Y" %}, Amazon Web Services, Inc. or its Affiliates. All rights reserved.</p>`**

### Built-in template filters

You have the choice to transform data in the view using Python or in the template by using filters. You should use filters to display the data on a webpage when the transformation is intended solely for the presentation layer.

A filter is recognized in templates by a pipe following a variable, as in **`{{ variable | filter }}`**. Note that all the spaces inside the curly braces are optional and are ignored when rendered. It is sometimes possible to pipe multiple filters, as in **`{{ variable | filter1 | filter2 }}`**. Also, many filters accept or necessitate an argument, as in **`{{ variable | filter:argument }}`**.

Visit [Built-in template tags and filters](https://docs.djangoproject.com/en/stable/ref/templates/builtins/) in the Django documentation.

#### Textual filters

There are many possibilities for manipulating strings in a template. The following tables attempt to classify these filters in categories.

* Generic string formatting

| Data | Filter | Purpose | Outcome |
|---------------------- | ------------------- | -------------------------------------| ----------- |
| value = "helLo wOrld" | {{ value | lower }} | Converts a string into all lowercase | hello world |
| value = "helLo wOrld" | {{ value | upper }} | Converts a string into all uppercase | HELLO WORLD |
| value = "helLo wOrld" | {{ value | capfirst }} | Capitalizes the first character | HelLo wOrld |
| value = "helLo wOrld" | {{ value | title }} | Converts a string into title-case | Hello World |
| value = None | {{ value | default_if_none:"never" }} | Returns the value if not None or a given default otherwise | never |
| value = "helLo wOrld" | {{ value | truncatechars:8 }} | Truncates a string and adds "..." | helLo w… |
| value = "helLo wOrld" | {{ value | truncatewords:1 }} | Truncates a string after a number of words | helLo … |
| num = 4 | You have {{ num }} budd{{ num | pluralize:"y,ies" }} | Returns a plural suffix eventually | You have 4 buddies |
| value = "helLo wOrld" | {{ value | wordcount }} | Returns the number of words | 2 |

* Characters formatting

| Data | Filter | Purpose | Outcome |
|---------------------- | ------------------- | -------------------------------------| ----------- |
| value = "I'm the vet"	| {{ value | addslashes }} | Adds slashes before quotes | I\'m the vet |
| value = "I am the vet" | {{ value | cut:" " }} | Removes all values of arg from the given string | Iamthevet |
| value = "<h1>I'm the vet</h1>" | {{ value | escape }} | Escapes HTML characters: < > ' " & | &lt;h1&gt;I&#x27;m the vet&lt;/h1&gt; |
| value = "I am the vet\nWelcome" | {{ value | linebreaks }} | Replaces line breaks with appropriate HTML | <p>I am the vet<br>Welcome</p>
value = "I am the vet\nWelcome" |
| {{ value | linebreaksbr }} | Converts all newlines to HTML line breaks | I am the vet<br>Welcome |
| value = "I am the vet" | {{ value | wordwrap:5 }} | Wraps words at specified line length | I am\nthe \nvet |
| value = "I'm the Vet!   " | {{ value | slugify }} | Converts to ASCII, converts spaces to hyphens, removes characters that aren’t alphanumerics, underscores, or hyphens, converts to lowercase; also strips leading and trailing whitespace | im-the-vet |
| value = "<h1>I'm the vet</h1>" | {{ value | striptags }} | Strips all HTML tags | I'm the vet |
| value = "Buddy" | {{ value | center:10 }} | Centers the value in a field of a given width | '  Buddy   ' |
| value = "Buddy" | {{ value | ljust:10 }} | Left-aligns the value in a field of a given width | 'Buddy     ' |
| value = "Buddy" | {{ value | rjust:10 }} | Right-aligns the value in a field of a given width | '     Buddy' |

* URL, email, and phone formatting

| Data | Filter | Purpose | Outcome |
|---------------------- | ------------------- | -------------------------------------| ----------- |
| value = "https://www.example.org/foo?a=b&c=d"	| {{ value | urlencode }} | Escapes a value for use in a URL | https%3A//www.example.org/foo%3Fa%3Db%26c%3Dd |
| value = "Check out www.example.org and contact ana@example.com" | {{ value | urlize }} | Converts URLs and email addresses in text into clickable links | Check out <a href="http://www.example.org" rel="nofollow">www.example.org</a> and contact <a href="mailto:ana@example.com">ana@example.com</a> |
| value = "800-COLLECT" | {{ value | phone2numeric }} | Converts a phone number with letters to numerical | 800-2655328 |

#### Numeric filters

Integers and floats have their own filters. The following table classifies filters in this category.

| Data | Filter | Purpose | Outcome |
|---------------------- | ------------------- | -------------------------------------| ----------- |
| value = 21 | {{ value | divisibleby:3 }} | Returns True if the value is divisible by the argument | True |
| value = 1.23456 | {{ value | floatformat:2 }} | Formats a float, for instance by indicating the number of decimals | 1.23 |
| value = 1234567890 | {{ value | getdigit:4 }} | Returns the requested digit where 1 is the right-most digit | 7 |
| value = 12345 | {{ value | filesizeformat }} | Formats as a human-readable file size | 12.1 KB |
| value = 12345 | {{ value | stringformat:"E" }} | Formats the variable according to the argument | 1.234500E+04 |

#### Date and time filters

These filters are applied with variables holding data from the **datetime** Python package. The following table lists the filters in this category.

| Data | Filter | Purpose | Outcome |
|---------------------- | ------------------- | -------------------------------------| ----------- |
| value = datetime( 2031, 4, 17, 14, 00) | {{ value | date:"D H:i T, M d, Y" }} | Formats a date according to the given format | Thu 14:00 UTC, Apr 17, 2031 |
| value = datetime( 2031, 4, 17, 14, 00) | {{ value | time:"H\h i\m" }} | Formats a time according to the given format | 14h 00m |
| before = datetime( 2031, 4, 17, 14, 00), after = datetime( 2032, 5, 17, 14, 00)| {{ before | timesince:after }} | Formats a date as the time since that date compared to today or an optional date | 1 year, 1 month |
| before = datetime( 2031, 4, 17, 14, 00), after = datetime( 2031, 4, 17, 15, 30) | {{ after | timesuntil:before }} | Formats a date as the time until that date compared to today or an optional date | 1 hour, 30 minutes |

In the webpage listing pets, you can replace the **Birth** column by an **Age** column and use the **timesince** tag without any argument to compare the birth date with today's date: **`{{ p.birth | timesince }}`**.

The **date** and **time** filters accept many format strings. For more information, visit the [Date filter](https://docs.djangoproject.com/en/stable/ref/templates/builtins/#date) in the Django documentation.

#### Boolean filters

The following filters evaluate a value to eventually replace it with a given string.

| Data | Filter | Purpose | Outcome |
|---------------------- | ------------------- | -------------------------------------| ----------- |
| value = "" | {{ value | default:"never" }} | If value evaluates to False (value is None or empty string), uses the given default | never |
| value = True | {{ value | yesno:"yep,no,maybe" }} | Maps values for True, False, and None to three strings | yep |

#### Dictionary and list filters

A dictionary or a list variable can be manipulated or formatted using filters. A regular text can also be transformed into lists or displayed with a number on each row.

| Data | Filter | Purpose | Outcome |
|---------------------- | ------------------- | -------------------------------------| ----------- |
| value = ['Willow', 'Luna', 'Milo'] | {{ value | length }} | Returns the length of a string or a list | 3 |
| value = [{"name": "Willow", "age": 3}, {"name": "Luna", "age": 1}, {"name": "Milo", "age": 2}] | {{ value | dictsort:"age" }} | Returns a dictionary list sorted by a key | [{'name': 'Luna', 'age': 1}, {'name': 'Milo', 'age': 2}, {'name': 'Willow', 'age': 3}] |
| value = [{"name": "Willow", "age": 3}, {"name": "Luna", "age": 1}, {"name": "Milo", "age": 2}] | {{ value | dictsortreversed:"name" }} | Returns a dictionary list reverse sorted by a key | [{'name': 'Willow', 'age': 3}, {'name': 'Milo', 'age': 2}, {'name': 'Luna', 'age': 1}] |
| value = ['Willow', 'Luna', 'Milo'] | {{ value | first }} | Returns the first item in a list | Willow |
| value = ['Willow', 'Luna', 'Milo'] | {{ value | last }} | Returns the last item in a list | Milo |
| value = ['Willow', 'Luna', 'Milo'] | {{ value | join:", " }} | Joins a list with a string | Willow, Luna, Milo |
| value = "Buddy" | {{ value | make_list }} | Returns a string turned into a list | ['B', 'u', 'd', 'd', 'y'] |
| value = ['Willow', 'Luna', 'Milo'] | {{ value | random }} | Returns a random item from the given list | Luna |
| value = ['Willow', 'Luna', 'Milo'] | {{ value | slice:":2" }} | Returns a slice of the list | ['Willow', 'Luna'] |
| value = ['Willow', 'Luna', 'Milo'] | {{ value | unordered_list }} | Returns an HTML unordered list | <li>Willow</li><li>Luna</li><li>Milo</li> |
| value = "Willow\nLuna\nMilo" | {{ value | linenumbers }} | Displays text with line numbers | 1. Willow\n2. Luna\n3. Milo |

### Extra tags and filters

By loading extra packages, you can unlock extra tags and filters. You can insert a load tag towards the top of your template as in **`{% load feature %}`** where the **feature** is a custom template tag set.

Some tags and filters might be accessible by configuring extra applications or middleware in the project settings or by setting variables. The **load** tag is not always necessary.

The following tag sets must be enabled in the project settings, or they must be loaded with the **load** tag. Sometimes both actions are necessary.

* **static** – Static files like a CSS stylesheet or a logo image are placed in a storage defined by the **STATIC_ROOT** and **STORAGES** settings in the project **settings.py**.

With this **static** tag set, you can avoid hardcoding a path to a static file in your HTML code. It will make your code future-proof in case the static artifacts change location, which is likely to be the case between a development environment and the production environment. Only the settings will differ, not the code.

As an example, after loading the static tag set with **`{% load static %}`**, you can point to your stylesheet with **`<link rel="stylesheet" type="text/css" href="{% static 'css/main.css' %}">`**. Django will resolve a path based on the settings. If the static files are local and **STATIC_ROOT** is **static/**, it can become **/static/css/main.css**.

* **csrf_token** – Cross-site request forgery (CSRF) is a malicious exploit of a website. You need to protect your application's post forms against it. By adding the **django.middleware.csrf.CsrfViewMiddleware** package in the **MIDDLEWARE** setting, you get access to the tag in all your templates. You can use the tag inside a **<form>** element to enable the protection against CSRF by typing: **`{% csrf_token %}`**.
* **humanize** – This library eases how text is presented to visitors. By adding the **django.contrib.humanize** package in the **INSTALLED_APPS** setting and using **`{% load humanize %}`** in a template, you get access to extra filters.

For instance, **`{{ date | naturalday }}`** could return **yesterday**, **today**, or **tomorrow**. For more information, visit [django.contrib.humanize](https://docs.djangoproject.com/en/stable/ref/contrib/humanize/) in the Django documentation.

* **i18n** – This library stands for *internationalization** and helps indicate translatable text in templates. It is enabled by **`{% load i18n %}`** and additionally with **`USE_I18N = True`** in the project settings. It unlocks access to a translate tag, such as **`{% translate "This is a pets service." %}`**.
* **l10z** – This library stands for **localization** and controls how values are displayed in templates. It can effect how numbers and dates are shown. It is enabled with **`{% load l10z %}`**, which gives access to a **localize** filter as in **`{{ date | localize }}`**.
* **tz** – This library helps with timezone conversions in templates. It is enabled with **`{% load tz %}`** and additionally with **`USE_TZ = True`** in the project settings. It gives access to both tags **(localtime, timezone, get_current_timezone)** and filters **(localtime, utc, timezone)**.

## Model-View-Template Example

### The requirements

* One webpage must display the complete list of pets, including the pet's name, picture, and owner. The pet's name and picture can be selected to access more information about one pet.
* A **pet webpage** must list all the information available about a single pet including vaccinations and vet visits.
* A **new-vet-visit** link must be made available on the pet webpage to create a new visit and update the rabies vaccination date. The webpage must refresh automatically with the new information.

### The software architecture

* **Templates** – the site is made of two webpages, so two templates are necessary. Because they have a common structure, they can inherit from one base-skeleton template.
 * pets.html
 * base.html
 * pet.html
* **Views** – Two views are necessary to get data and render the two webpages. Another view must implement the new-vet-visit link action and write data.
 * listPets()
 * pet()
 * visit()
* **Models** – You already have models and a database with test data from the Django Models course. You must add pet pictures.
* **URL paths** – The number of paths can be aligned with the number of views, so three paths are necessary.
 * "pets"
 * "pet/<str:pet_id>"
 * "visit/<str:pet_id>"

### Models pets_app/models.py

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
        return str(self.pet) + " - " + str(self.rabies)

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
    picture = models.ImageField(max_length=255, null=True)
    
    def __str__(self):
        return self.name + " - " + self.gender + " - " + str(self.birth.year)

class VetVisit(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    vet = models.CharField(max_length=100)
    date = models.DateField(default=datetime.today().strftime('%Y-%m-%d'))
    notes = models.TextField(null=True, blank=True)
    
    @property
    def is_today(self):
        return self.date == datetime.today().date()
    
    def __str__(self):
        return self.pet.name + " - " + self.vet + " - " + str(self.date) + " - " + self.notes
```

### The views pets_app/views.py

```
from django.shortcuts import render
from .models import Pet, VetVisit
from datetime import datetime

def listPets(request):
    context = {'pets': Pet.objects.all()}
    return render(request, "pets_app/pets.html", context)

def pet(request, pet_id):
    context = {'pet': Pet.objects.filter(id=pet_id).first()}
    return render(request, "pets_app/pet.html", context)
    
def visit(request, pet_id):
    pet = Pet.objects.filter(id=pet_id).first()
    lastvisit = pet.vetvisit_set.last()
    if lastvisit and not lastvisit.is_today:
        vet = pet.vetvisit_set.last().vet
        newvisit = VetVisit(pet=pet, vet=vet, notes="rabies vaccination")
        newvisit.save()
        pet.card.rabies = datetime.today().strftime('%Y-%m-%d')
        pet.card.save()
    context = {'pet': pet}
    return render(request, "pets_app/pet.html", context)
```

### The templates pets_app/templates/pets_app/

#### base.html

```
{% load static %}
<!DOCTYPE html>
<html>

<head>
    <title>Pets Application</title>
    <link rel="icon" href="{% static 'favicon.ico' %}">
    <link rel="stylesheet" type="text/css" href="{% static 'css/main.css' %}">
</head>

<body>
    <div class="banner">
        <table>
            <tr>
                <td><img src="{% static 'logo-white.png' %}"></td>
                <td>Pets Application</td>
            </tr>
        </table>
    </div>
    <div class="nav-menu">
        <a href="{% url 'index' %}">Home</a>
    </div>

{% block content %}
{% endblock content %}

    <div class="footer">
        <p>&copy; {% now "Y" %}, Amazon Web Services, Inc. or its Affiliates. All rights reserved.</p>
    </div>
</body>

</html>
```

#### pets.html

```
{% extends "pets_app/base.html" %}
{% block content %}
<div class="pets" id="pets-link">

    <h2>Pets</h2>
    <table>
        <tr>
            {% for p in pets %}
            {% if forloop.counter0|divisibleby:3 %}
        </tr>
        <tr>
            {% endif %}
            <td><a href="{% url 'pet' p.id %}">
                <img src="{{ p.picture.url }}" width="120" />
                <p>{{ p.name }}</a></p>
                <p>{{ p.owner }}</p>
            </td>
            {% endfor %}
        </tr>
    </table>
</div>
{% endblock content %}
```

#### pet.html

```
{% extends "pets_app/base.html" %}
{% block content %}
<div class="pet">
    <h2>{{ pet.name }}</h2>
    <div class="pet">
        <img src="{{ pet.picture.url }}" width="200" /><br/>
        Gender: {{ pet.gender }}<br/>
        Birth: {{ pet.birth|date:"Y-M-d" }}<br/>
        Breed: {% for b in pet.breed.all %}
            {% if forloop.last %}
                {{ b.name|lower }}
            {% else %}
                {{ b.name|lower }},
            {% endif %}
        {% endfor %}<br/>
        Owner: {{ pet.owner|title }}<br/>
        <br/>
        Weight: {{ pet.weight|floatformat }} lb<br/>
        Height: {{ pet.height|floatformat }} in<br/>
        <br/>
        Vaccines: rabies {{ pet.card.rabies }} / 
            hepatitis {{ pet.card.hepatitis|default_if_none:"never" }} / 
            borrelia {{ pet.card.borrelia|default_if_none:"never" }} / 
            distemper {{ pet.card.distemper|default_if_none:"never" }}<br/>
        <br/>
        Vet visits: 
        <ul>
            {% for vv in pet.vetvisit_set.all %}
                <li>{{ vv.date|date:"Y-M-d" }}: vet {{ vv.vet|title }}
                    {% if vv.notes %}
                        wrote <i>{{ vv.notes|striptags }}</i>
                    {% endif %}
                </li>
            {% endfor %}
        </ul>
        <a class="btn btn-info pull-right" 
            href="{% url 'visit' pet.id %}">
            New visit today with rabies vaccine
        </a><br/><br/>
    </div>
</div>
{% endblock content %}
```

### Final result

#### Main page

The **/pets** URL is served by the **listPets** view that renders **pets.html**. A **for** tag helps looping over all the pets by iterating over the **pets** variable in the template context.

#### Pet link

Each pet's picture and name are selectable with a **url** tag link pointing to the **pet path**.

#### Pet webpage

The pet path is **pet/<str:pet_id>** and is served by the **pet** view. That view renders the **pet.html** template. Vaccinations and visits are listed because of the **pet** data in the template context.

#### New visit link

A url tag helps create a link towards the **visit/<str:pet_id>** path.

#### New visit and vaccination

The visit path is served by the **visit** view. It modifies the database and re-renders the same template, **pet.html**. The **rabies vaccination date** has changed and a **new visit** is in the log.

### [Lab: Creating Templates in a Web Framework](./labs/W052Lab2DjangoTemplates.md)

### Knowledge Check

#### Which template engines are built into the Django framework?

* Django template language (DTL) and Jinja2

Wrong answers:

* Django template language (DTL) and Mako
* Cheetah and Django template language (DTL)
* Genshi and Jinja2

##### Explanation

Django ships built-in backends for its own template system. One is the Django template language, and the other one is Jinja2.

Cheetah, Genshi, and Mako are three Python-based template frameworks.

#### Which steps does a Django developer follow to render an existing template? (Select THREE.)

* Create a view and code the business logic.
* Set the template data in a context variable.
* Render the template by passing the context.

Wrong answers:

* Create a template model.
* Set the template data in a template model.
* Render the template by passing the template model.

A view implements the logic of manipulating data by using models. Then, the view places the data used by a template in a context variable. Finally, the view calls a function to render the template by passing the context as an argument.

#### Which of the following are built-in Django template filters? (Select THREE.)

* time
* float
* upper

Wrong answers:

* for
* integer
* double

##### Explanation

These template filters can be applied to date and time, numeric, and string variables.

**for** is not a filter but a tag. It is used to create loops.

**integer** and **double** are not tags nor filters.

### Summary

* The **Django template system** supports multiple **template engines**. Django comes with its own backend, the **Django template language**. It is configured in the project settings.
* **Application data** can be passed from a view to a template through a **context** object at rendering time. There are multiple ways to render a template. The data can be accessed with **double curly braces**.
* Templates are made of HTML elements combined with **template tags** and **template filters**. The template language proposes many tags and filters. Some might come from extra libraries that need to be configured or loaded.
