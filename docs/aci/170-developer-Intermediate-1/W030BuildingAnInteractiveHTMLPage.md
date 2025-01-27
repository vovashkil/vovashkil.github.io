# Week 3: Building an Interactive HTML Page

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to repo's main [README.md](../../../README.md)

## HTML Forms

### Pre-assessment

#### What is the purpose of an HTML form?

* To capture user information entered in a webpage and send it to the server for processing

Wrong answers:

* To define the content of a static webpage
* To provide a default format for the elements in a webpage
* To collect usage statistics for a webpage and send it to the server for processing

##### Explanation

* A static webpage can contain a form, but this is optional. Not all static webpages capture user information.
* You can't provide a default format for the elements of a webpage or collect usage statistics for a webpage by using a form element.

#### Which HTML element defines a form for user input?

* form

Wrong answers:

* input
* dialog
* output

##### Explanation

* The input element defines an input field.
* The dialog element displays a dialog box.
* The output element defines a field for outputting values.

#### Which format does the data in a form sent to the server in an HTTP request have?

* Name-value pair

Wrong answers:

* JSON
* YAML
* XML

##### Explanation

* You typically use JSON, YAML, and XML to exchange data programmatically.

### HTML Form Elements

#### How an HTML form works

With an HTML form, a user can enter data in a webpage and send the data to a backend server for processing. For example, you can use a form to collect a keyword for a search function, a username and password on a login page, or identification information on a registration page.

##### HTML input form elements

Input form elements in the HTML document capture the data entered by the user. For example, the data consists of a first name, last name, and an email address with values of **John**, **Doe**, and **jdoe@example.com**, respectively.

##### HTML button form element

A **Submit** button form element initiates the HTTP action and method defined in the form. For example, the form action specifies **/register** as the path to the server-side resource that will process the form data. The form method specifies an HTTP **POST** method.

##### HTTP request

When the user chooses the **Submit** button, the web browser creates an HTTP request that contains the form data in its body. The data is captured as name-value pairs. In the example, the name-value pairs are **firstName=John**, **lastName=Doe**, and **email=jdoe@example.com**. The browser then sends the request to the web server.

##### Server-side processing

When the web server receives the HTTP request, it recognizes and maps the **/register** path in the header to the registration application component running on the application server. The web server then forwards the request to the application server. The registration component reads the data in the HTTP request and processes it as necessary. In this case, the component updates the application database to add John Doe's user registration.

##### HTTP response

When all the server-side processing is finished, the web server returns an HTTP response to the web browser. In this example, the web server returns an HTML page that confirms that John has been successfully registered.

### Basic HTML form elements

HTML provides various types of elements that facilitate collecting and submitting information on a webpage. These user interface elements include input fields, dropdown lists, and buttons.

#### form element

The **form** element defines an area on a webpage where the user can enter data to send to a server for processing. The **form** element is the container of all form-related elements, such as **input**, **textarea**, **select**, and **button** elements.

#### input element

The **input** element creates a field to collect data from the user. There are many types of input elements that cover the different types of data that a user can enter, including text, numbers, email addresses, dates, and checkbox items.

#### textarea element

The **textarea** element defines a field for entering multiple lines of text. It is useful for capturing free-form text, such as messages, reviews, and comments.

#### select element

The **select** element creates a container for a dropdown list of options. You define each option by using the **option** element.

#### button element

The **button** element creates a button that can be chosen to initiate actions for the form.

### Adding a Form to an HTML Document

```
<form action="/register" method="post">
    <!-- Define the form's user interface elements here. -->
</form>
```

* The **action** attribute defines the URL of the server-side resource that the form will be submitted to. In the example, the value of the attribute is **/register**. If the domain name of the server is **www.example.com**, the form data will be submitted for processing to the resource identified by the URL **http://www.example.com/register**.
* The **method** attribute specifies the **HTTP method** of the request that is sent to the server. In the example, the method is **post**. This means that the form data will be sent to the server for processing and included in the request's body as name-value pairs.

### HTML form considerations

The following are some considerations to remember when developing HTML forms:

* You **can't nest** a **form** element inside of another form element.
* The HTTP **POST** method is a common choice used to submit form data because it does not impose any limit on the size of the data. It can transfer large amounts of data in the body of the HTTP request.
* You can use HTML structuring elements inside a form. For example, you can use the **division**, **paragraph**, **table**, and **list** elements to organize the information inside a form.

### Input Form Element

```
<form>
   Enter your first name:
   <input type="text" name="firstName">
</form>
```

You must specify the **name** attribute for every input field on a form that will be sent to the server, and make sure that the name is unique for each field. This is because when the form is submitted, the server-side resource that processes the form will use the field attribute's name to access the corresponding data.

#### Some commonly used input types

| Input type | Description |
| ---------- | ---------------------------------------------------- |
| checkbox | An element for creating a checkbox. A checkbox represents a value that you can select or clear. If you create multiple checkboxes with the same name to represent multiple choices, you can select multiple values for the element. |
| email | A field for entering an email address. The browser validates that the entry has a valid email address format. |
| number | A field for entering numbers. The browser validates that the entry is numeric. You can specify the allowed minimum and maximum values using the **min** and **max** attributes, respectively. |
| radio | An element for creating a radio button. A radio button represents a value that you can select. If you create multiple radio buttons with the same name to represent multiple choices, you can a select a single value for the element. |
| reset | A button that resets the contents of a form to its default values. Specifically, it resets the form's contents to the initial values when the webpage was loaded. |
| submit | A button that submits the form for processing. It sends the form data to the URL specified in the **action** attribute of the containing form element. |
| tel | A field for entering a telephone number. No validation is performed on the entry unless you specify a **pattern** attribute. If the client device can display a phone number keyboard (like a smartphone), the device will display the keyboard when the field gains focus. |
| text | A field for entering a single line of text. This is the default type of an input element if the type is not specified. |

#### Form example

Collecting the following registration data from a user and implement the stated requirements:

* **First name**: This field is required and should have the **focus** when the page is loaded.
* **Last name**: This field is **required**.
* **Email address**: This field is **required** and **must be a valid email address**.
* **Telephone number**: This field is **optional**.
* **Yes** or **No prompt**: This field asks users if they want to subscribe to a monthly newsletter by email. It should have a **default value of No**.

```
<!doctype html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <title>Registration</title>
</head>
<body>
   <h1>Example Pet Club Registration</h1>
   <nav>
      <a href="home.html">Home</a> |
      <a href="petTypes.html">Breeds of Pets</a>
   </nav>
   <p>Enter your registration information below:</p>
   <form onsubmit="alert('Form submitted');">
      <table>
         <tbody>
            <tr>
               <td>First Name:</td>
               <td><input type="text" name="firstName" autofocus required></td>
            </tr>
            <tr>
               <td>Last Name:</td>
               <td><input type="text" name="lastName" required></td>
            </tr>
            <tr>
               <td>Email:</td>
               <td><input type="email" name="email" required></td>
            </tr>
            <tr>
               <td>Telephone Number:</td>
               <td><input type="tel" name="phoneNumber"></td>
            </tr>
         </tbody>
      </table>
      <p>Would you like to receive our monthly newsletter by email?</p>
      <p>
         <input type="radio" name="emailSubscription" value="Yes">Yes
         <br>
         <input type="radio" name="emailSubscription" value="No" checked>No
      </p>
      <input type="submit" value="Submit">
      <input type="reset">
   </form>
</body>
</html>
```

After the page loads, the **No** radio button is preselected for the monthly newsletter subscription prompt. This is because the **No** radio button element is defined with the **checked** attribute. When you choose the **Submit** button without entering any values in the form, the browser displays the following message next to the **First Name** field: **Please fill out this field**. This is because the first name element is defined with the **required** attribute.

You must enter a value for the **First Name**, **Last Name**, and **Email** fields because you defined their element with the **required** attribute. If you enter an improperly formatted email value for the **Email** field, the browser displays the following message: **Please enter an email address**. This is because the email element is defined with an input type of **email**.

After you enter and select valid values for the input fields and choose the **Submit** button, the browser displays an alert dialog box with the message: **Form submitted**. This indicates that all the fields have passed the built-in validation performed by each **input** element **type**.

### Commonly used input attributes

* **autofocus**: This attribute indicates that the element should get focus when the page is loaded.
* **checked**: This attribute indicates that the element should be preselected when the page is loaded. It is used with the **checkbox** and **radio** input form element types.
* **required**: This attribute indicates that the field must have a value before users can submit the form.
* **value**: You use this attribute to provide a default or specific value for the element. For example, if you specify the attribute **value="John"** in the first name element and the user does not enter a value for it, when the form is submitted, the value of the element sent to the server is **John**. Similarly, if you use a **checkbox** or **radio** input type and specify a **value** attribute, the value of the element sent to the server when the element is selected is the attribute value. Otherwise, if you do not provide a **value** attribute, the value sent is "**on**".

### Select Form Element

The select element creates a dropdown list of options from which the user can select one or more values. You specify each option by using the option element. For example, the following code uses a select element to capture a user's favorite type of pet.

```
<form>
    What is your favorite type of pet?
    <select name="favoritePetType">
        <option value="Cat">Cats</option>    
        <option value="Dog" selected>Dogs</option>  
        <option value="Bird">Birds</option>
    </select>
</form>
```

#### Attributes used with the select and option elements

* **name**: Similar to the **input** element, you must specify a **name** attribute for a select element so that its **value** will be sent to the server when the form is submitted.
* **selected**: This attribute indicates that the **option** element should be preselected when the page is loaded. The option's **value** becomes the default for the **select** element. In the example, the default **value** for the **select** element is **Dogs**.
* **value**: You use this attribute to provide a specific **value** for the **option** element when the element is selected. If you do not provide a **value** attribute, the value of the element when the element is selected is the element's content. In the example, if you choose the **Birds** option element, the value sent to the server is **Birds** when the form is submitted.

#### Example capturing a user's location information

* **City**: This is a text field and is required.
* **State**: This field appears after the **City** field and is required. The user should select the field value from a dropdown list of the 50 US states and Washington, DC. The field's default value is **AL** for the state of Alabama.
* **Country**: This field appears after the **State** field. Because all the state values are for the United States, give this field a default value of **United States** and make it **read-only**.

```
<tr>
    <td>City:</td>
    <td><input type="text" name="city" required></td>
 </tr>
 <tr>
    <td>State:</td>
    <td><select name="state">
          <option value="AL" selected>Alabama</option>
          <option value="AK">Alaska</option>
          <option value="AZ">Arizona</option>
          <option value="AR">Arkansas</option>
          <option value="CA">California</option>
          <option value="CO">Colorado</option>
          <option value="CT">Connecticut</option>
          <option value="DE">Delaware</option>
          <option value="DC">District of Columbia</option>
          <option value="FL">Florida</option>
          <option value="GA">Georgia</option>
          <option value="HI">Hawaii</option>
          <option value="ID">Idaho</option>
          <option value="IL">Illinois</option>
          <option value="IN">Indiana</option>
          <option value="IA">Iowa</option>
          <option value="KS">Kansas</option>
          <option value="KY">Kentucky</option>
          <option value="LA">Louisiana</option>
          <option value="ME">Maine</option>
          <option value="MD">Maryland</option>
          <option value="MA">Massachusetts</option>
          <option value="MI">Michigan</option>
          <option value="MN">Minnesota</option>
          <option value="MS">Mississippi</option>
          <option value="MO">Missouri</option>
          <option value="MT">Montana</option>
          <option value="NE">Nebraska</option>
          <option value="NV">Nevada</option>
          <option value="NH">New Hampshire</option>
          <option value="NJ">New Jersey</option>
          <option value="NM">New Mexico</option>
          <option value="NY">New York</option>
          <option value="NC">North Carolina</option>
          <option value="ND">North Dakota</option>
          <option value="OH">Ohio</option>
          <option value="OK">Oklahoma</option>
          <option value="OR">Oregon</option>
          <option value="PA">Pennsylvania</option>
          <option value="RI">Rhode Island</option>
          <option value="SC">South Carolina</option>
          <option value="SD">South Dakota</option>
          <option value="TN">Tennessee</option>
          <option value="TX">Texas</option>
          <option value="UT">Utah</option>
          <option value="VT">Vermont</option>
          <option value="VA">Virginia</option>
          <option value="WA">Washington</option>
          <option value="WV">West Virginia</option>
          <option value="WI">Wisconsin</option>
          <option value="WY">Wyoming</option>
       </select></td>
 </tr>
 <tr>
    <td>Country:</td>
    <td><input type="text" name="country" value="United States" readonly></td>
 </tr>
```

### Button Element

A **Submit** button and a **Reset** button of a form element can be created by using an **input** element with a **type** attribute of **submit** and **reset**, respectively. You can also create a button in an HTML form by using the **button** element. This element defines a button that you can use to initiate an action, such as submitting a form or running a script.

One big difference between the **button** element and the **submit** and **reset** elements is that you can nest other HTML elements inside of the **button** element. For example, you can insert an **image** element between the <button> opening tag and the </button> closing tag to use an image instead of text to describe the button. Another difference is that you can use a **button** element **inside or outside** of a **form** element.

The following describes some of the common attributes used with the **button** element:

* **disabled**: This attribute disables the button so that the user can't interact with it. The attribute is commonly used when a button should be enabled only under a certain condition, for example, based on the value of a field in the form. When that condition is satisfied, a script in the HTML document programmatically enables the button.
* **form**: You can define this attribute if the button element is defined outside of a form element and you want to associate the button with a form in the HTML document. Specify the value of the form's **id** attribute as the value of the **form** attribute.
* **formaction** and **formmethod**: If the type of the button is **submit**, these attributes specify the URL of the server resource where the form data is sent and the HTTP method used in the HTTP request, respectively. If these attributes are specified, their values override the values set for the **action** and **method** attributes of the associated form element, respectively.
* **type**: This attribute defines the type of the button and can have one of the following values: **submit**, **reset**, or **button**. A **submit** button sends the form data to the server. A **reset** button clears the form data by resetting all the form fields to their initial values. For all other types of buttons, for example a button to invoke a script, set the **type** attribute value to **button**. Note that the **submit** and **reset** values in a **button** element have the same meaning as the corresponding values in an **input** form element.

```
<button type="submit">
    <img src="../images/submitButton.jpeg" width="120" height="51" alt="Blue submit button">
</button>
<button type="reset">
    <img src="../images/resetButton.jpeg" width="51" height="51" alt="Green reset button">
</button>
```

### [Lab: Adding a Form and Buttons to a Webpage](./labs/W030Lab1FormAndButtons.md)

### Knowledge Check

#### Which attribute of an input field is required if the input field's value must be sent to the server?

* name

Wrong answers:

* id
* required
* checked

##### Explanation

* The form will only pass the **value** of **input** elements that have a **name** attribute when it is submitted.
* The **id** attribute is optional and uniquely identifies the element within the form.
* The **required** attribute indicates that the field requires a value.
* You use the **checked** attribute specifically with the **checkbox** and **radio** elements. It indicates that the element should be preselected when the page is loaded.

#### Which HTML element defines the choices in a select element?

* option

Wrong answers:

* list item
* label
* details

##### Explanation

* You create an **option** element for each choice presented by a **select** element.
* The **list item** element defines an item in a **list** element.
* The **label** element defines a text label for a form element.
* The **details** element creates an interactive widget that a user can expand or collapse to reveal summarized or detailed content.

#### What is the difference between a button created with an input element and a button created with a button element? (Select TWO.)

* You can define a button created with a **button** element inside or outside of a **form** element.
* You can't nest HTML elements inside a button created with an **input** element.

Wrong answers:

* You can add an image to a button created with an **input** element.
* You can't create a reset button with a **button** element.
* You can't submit a form with a button created with an **input** element.

##### Explanation

* You can create **submit** and **reset** buttons with both types of buttons. However, you can't add an image to a button created with an **input** element because the element does not support element nesting.

### Summary

* You use an HTML form to collect the data that a user enters on a webpage and send the data to a backend server for processing.
* You define an HTML form by using the **form** element. A **form** element's **action** attribute defines the URL of the server-side resource that will receive the form data when it is submitted. A **form** element's **method** attribute specifies the HTTP method of the request that is sent to the server.
* **Input**, **select**, and **button** elements are basic HTML elements used with a **form** element.
* An **input** element defines an input field. HTML provides many types of input fields to capture different types of input, including text, numbers, email addresses, and checkbox selections. An input element's **type** attribute specifies the type of input that the element captures. An input element also has a **name** attribute, which uniquely identifies the field. Other common attributes that you can define for an input element include **autofocus**, **required**, **readonly**, and **value**.
* A **select** element defines a dropdown list of options from which a user can select one or more values. You define each option by using an **option** element and can specify a default option by using the **selected** attribute.
* A **button** element defines a button that you can use to initiate an action. It can be used inside or outside of a **form** element and can contain nested HTML elements.

## Client-Side Scripting

### Pre-assessment

#### What is a benefit of client-side scripting in a webpage?

* Client-side scripting facilitates the building of an interactive UI in a webpage.

Wrong answers:

* Client-side scripting eliminates the need to request a webpage from a server.
* Client-side scripting decreases the load time of a webpage.
* Client-side scripting decreases the size of the code in a webpage.

To implement client-side scripting, a developer adds JavaScript code to a webpage. This increases the page's load time and overall number of lines in the code. In addition, the browser still must fetch a webpage from the server even if the page uses a client-side script.

#### What are characteristics of the JavaScript language? (Select TWO.)

* JavaScript is an interpreted programming language.
* JavaScript supports event-driven programming.

Wrong answers:

* JavaScript is an extension of the Java programming language.
* JavaScript is a statically typed programming language.
* JavaScript uses indentation to group code blocks.

JavaScript is a dynamically typed language and has no relation to Java. Unlike Python, JavaScript does not use indentation to group blocks of code. Instead, it uses braces to enclose code blocks.

#### Which keyword can a developer use to declare a variable in JavaScript?

* let

Wrong answers:

* public
* export
* new

You use the **export** keyword in conjunction with JavaScript modules.

You use the **public** and **new** keywords with a JavaScript class.

### JavaScript in Frontend Web Development

### Benefits of JavaScript

With scripting, specifically JavaScript scripting, you can control the behavior of a webpage to implement client-side logic, make the page more interactive, or present a more dynamic user interface. In fact, you can use scripting to give the user interface of a web application the features and interactivity of a mobile or desktop application.

### the purpose and benefits of using JavaScript in a webpage

#### Validating data entered in an HTML form

HTML has some builtin validation features, for example, for an **input** field:

* The **required** attribute specifies that the input field must be filled.
* For a **number** field, the **min** and **max** attributes define the minimum value and maximum value.

With JavaScript, you can access the individual values of a form element and perform different types of validation in the browser:

* Ensuring that the value entered for **start date** is before the value for **end date** in a form that has a start date input field and an end date input field.
* Making sure that the user provides a value for at least one of a number of fields in a form.

Note that as a recommended practice, you should also perform field validation on the server side. One reason is to ensure that the data hasn't been tampered with during transmission. Server-side validation is also particularly important if JavaScript is turned off in the browser.

#### Dynamically changing the content in an HTML document

There might be times when you want to change the content of a webpage based on user input, without having to fetch a new page from the server. For example, suppose that on the Example Pet Club Registration page, you want to display the **State** dropdown field only if the value of the **Country** field is **United States**. For a country other than the Unites States, the state field is not applicable, and you want to hide it on the form. You can implement this type of dynamic change in an HTML document by using JavaScript. Specifically, you can dynamically create, modify, or delete elements in an HTML document by using JavaScript.

#### Using a UI framework

A JavaScript UI framework provides a collection of prebuilt UI components, such as menus, forms, and buttons, which you can quickly combine to build a web user interface. These reusable components use HTML, CSS, and JavaScript in their implementation. By using a JavaScript UI framework, you can accelerate the development of your web application's user interface. A JavaScript UI framework also provides cross-browser compatibility. This means that a webpage will appear in the same way across different types of browsers. Some popular JavaScript UI frameworks include React, Angular, and Vue.

### JavaScript language

**JavaScript** is a programming language that was created in 1995 as a scripting language designed to run on the Netscape Navigator browser. In 1997, the **European Computer Manufacturers Association (ECMA)** standardized the language and created the **ECMAScript** standard. Although the Netscape Navigator browser is no longer in existence, virtually all browsers support JavaScript.

JavaScript is an interpreted language. Its original purpose was to provide the capability to dynamically modify the content of a webpage inside of a web browser. JavaScript scripting uses the JavaScript interpreter running in the browser along with the **Document Object Model (DOM)** that the browser generates for a webpage to change a webpage's content.

JavaScript plays a key role in the design of a webpage. Earlier in the course, you learned that HTML, CSS, and JavaScript are foundational technologies used in the development of the client side of a web application. You use HTML to define the content and structure of a webpage, CSS to define its layout and presentation, and JavaScript to add dynamic behavior or interactivity to a webpage.

JavaScript is most commonly used for client-side scripting, but it can also be used on the server side. JavaScript runtime environments, such as Node.js, provide the capability to run a JavaScript application outside of the browser on the server side.

### How to use JavaScript in an HTML document

A client-side JavaScript script is a program that controls the behavior of a webpage by dynamically manipulating the HTML elements in the page. By default, a script runs when the browser encounters the script's definition in the HTML document. A script can also run in response to events that affect the HTML document, such as when a user enters a value in a field or chooses a button or a link.

### Integrating JavaScript code

You can embed the code for a script directly in an HTML document or write it in a separate file and reference the file in the HTML document. In both approaches, you use the HTML**script** element to define the script in the HTML document. The attributes for a script element are all optional. In particular, the **type**** attribute specifies the scripting language used and has a default value of **text/javascript**, which indicates JavaScript.

#### Embedding JavaScript in HTML

You can write JavaScript code directly inside an HTML document. To do so, you use the HTML script element and enclose the code between the opening <script> tag and the closing </script> tag.

```
<script>
    // JavaScript code goes here 
</script>
```

Note that embedding JavaScript in HTML is not recommended. Mixing HTML and JavaScript in the same file makes the webpage harder to read and more difficult to maintain. It also reduces the opportunity for reuse because you can't use the embedded JavaScript code in another HTML document. For these reasons, using a JavaScript file is the recommended approach.

#### Using a JavaScript file

A good web development practice is to keep the code that defines the different layers of a webpage separate from each other. This makes the webpage easier to maintain and promotes the reuse of its different layers. JavaScript code should be separated from HTML code and define it in a file with a **.js** extension. This approach ensures a clean separation between the code that defines the structure of a webpage (HTML) and the code that defines the page's behavior (JavaScript). With this separation, you can reuse the JavaScript code in different HTML documents.

To use an external JavaScript file in an HTML document, perform the following steps:

1. Create a JavaScript file and write the code that defines the webpage behavior that you want to implement in the file.
2. Reference the JavaScript in the HTML document by using a **script** element. Specifically, add an empty script element to the document with an **src** attribute that specifies the URL of the JavaScript file.
3. Optionally, specify additional attributes for the script element. In particular, you can use the **async** and **defer** attributes to control the timing and sequence of when the script is run when the browser loads the webpage. The **async** attribute indicates that the browser should download the JavaScript file asynchronously. This ensures that the browser does not pause the processing of the HTML code in the document when it encounters the script element. In addition, the **defer** attribute specifies that the browser should wait until it has processed all the HTML code in the document before it runs the code in the JavaScript file.

An HTML document can contain multiple script elements. Furthermore, you can place a **script** element in the head or body of a document. However, as a best practice, you should add it to the body element before the </body> closing tag. As mentioned earlier, by default the browser interprets JavaScript code at the point in the document where you place the script element. Therefore, by placing the script element at the bottom of the body, you don't block the parsing and rendering of the other HTML elements, and thus facilitate the smooth display of the webpage.

### Running JavaScript code

The browser runs a script when it loads the webpage containing or referencing the script. It can also run the code in the script in response to events that occur during the lifecycle of the page or as the user interacts with the page. For example, an event can be triggered when the page is fully loaded, when an input field gains focus, or when a user selects a menu option.

Client-side JavaScript programming commonly entails writing code that is activated by events that happen on a webpage. The event occurs on an element in the page and causes the invocation of JavaScript code that you define as the *event handler*. The event handler is typically a function in a JavaScript script.

You define HTML event handlers in the code by using element attributes called *event attributes*. Event attributes have a name that starts with **on**, followed by the name of the event, such as **onclick** or **onsubmit**. The value of an event attribute is typically a JavaScript statement that invokes the function that handles the event. For example, in the Example Pet Club Registration page that you developed, you defined the following event attribute for the form element:

```
<form onsubmit="alert('Form submitted');">
```

When the user chooses the **submit** button associated with the form, the **onsubmit** event attribute causes the browser to invoke the JavaScript **alert()** function. The function displays an alert box with the message **Form submitted**.

#### Some of the commonly used event attributes

| Event Type | Event Attribute | Description |
| ---------- | --------------- | ----------- |
| Form | onblur | Triggered when an element loses focus |
| Form | onchange | Triggered when you change the value of an element |
| Form | onfocus | Triggered when an element gets focus |
| Form | onreset | Triggered when you reset the form by using a reset button |
| Form | onsubmit | Triggered when you submit the form |
| Keyboard | onkeypress | Triggered when you press a key |
| Mouse | onclick | Triggered when you choose an element |
| Mouse | ondblclick | Triggered when you open (double-click) an element |
| UI | onerror | Triggered when an error occurs loading the webpage |
| UI | onload | Triggered when the webpage is fully loaded |

You can also define an event handler on an element at runtime by using the JavaScript **addEventListener()** method. This gives you the ability to add multiple event handlers to an element. This is also the recommended way to define event handlers because it separates HTML code from JavaScript code.

#### Event handler example

```
<!doctype html>
<html lang="en">
   <head>
      <meta charset="UTF-8">
      <title>Hello World Dynamic Page</title>
   </head>
   <body>
      <button type="button" onclick="sayHello();">Say hello</button>
      <p id="messageArea"></p>
      <script>
         function sayHello() {
            document.getElementById("messageArea").innerHTML = "Hello, World!";
         }
      </script>
   </body>
</html>
```

* The **button** element has a content of **Say hello**. The element also has an event attribute with a name of **onclick** and a value of **sayHello()**.
* The paragraph element has an **id** of **messageArea**. The element is empty.
* The **script** element contains the definition of a function called **sayHello()**. The function accesses the content of the element with an **id** of **messageArea** and sets its value to **Hello, World!**.

### Using the DOM API

When a browser renders a webpage, it parses the code in the HTML document into a Document Object Model (DOM) tree. The DOM tree is an in-memory representation of the document that you can use to programmatically access and modify the elements in the document. Specifically, you write JavaScript code that uses the DOM API to access the elements in an HTML document.

A DOM tree is composed of nodes that are arranged to reflect the hierarchical structure of an HTML document. There are four main types of nodes:

* **Document node**: This is the root node of the tree and represents the entire HTML document. You access this node by referencing the  global object named **document**. This object is the entry point to any DOM manipulation.
* **Element node**: An element node represents an HTML element in the document, such as a title, paragraph, or form element.
* **Attribute node**: An attribute node represents an attribute of an HTML element, such as **id**, **name**, or **onsubmit**.
* **Text node**: A text node represents the text in an HTML element. Text nodes are the leaves of the tree and can't have any child nodes.

```
<!doctype html>
<html lang="en">
   <head>
      <meta charset="UTF-8">
      <title>Registration</title>
   </head>
   <body>
      <h1>Example Registration</h1>
      <p>Enter your registration information below:</p>
      <form id="registrationForm" onsubmit="alert('Form submitted');">
         First name:
         <input type="text" name="firstName">
         <br>
         <br>
         <input type="submit">
      </form>
   </body>
</html>
```

When the browser loads this document, it creates a DOM tree.

1. **Document node**. The document node is the root of the tree and gives you access to all the other nodes in the tree.
2. **HTML element node**. The **html** element node corresponds to the **html** element in the document. Its immediate children are the **head** and **body** element nodes.
3. **HTML attribute node**. **lang="en"** is an attribute node of the **html** element node. You can access an attribute node in JavaScript to retrieve the attribute's value.
4. **Form element node**. The form element node is a child of the **body** element node. In this example, it has an **id** attribute node and an **onsubmit** attribute node associated with it.
5. **Heading text node**. This node is the text node associated with the h1 element node. It contains the value of element, **Example Registration**.

Use the **document** object access the different elements in an HTML document. This object has properties that you can access and methods that you can invoke using the dot notation. For example, **document.head** returns the head element in the document. Likewise, **document.getElementById("registrationForm")** returns the element that has an **id** attribute value of **"registrationForm"**.

### Some commonly used properties and methods of the document object

| Property or Method | Description |
| ------------------ | ----------- |
| createElement(aTagName) | Creates an element that has a type that is specified by **aTagName**. Note that this method does not add the new element to the DOM. To do so, after you create the element, invoke an element method, such as **appendChild()**. |
| createTextNode(aString) | Creates a text node with the string **aString**. Note that this method does not add the new node to the DOM. To do so, after you create the node, invoke an element method, such as **appendChild()**. |
| getElementById(anId) | Returns the element that has an **id** attribute value of **anId** |
| getElementsByClassName(aClassName) | Returns a collection of elements that have the class attribute value of **aClassName** |
| getElementsByName(aName) | Returns a collection of elements that have the name attribute value of **aName** |
| head | Returns the document's **head** element |
| images | Returns a collection of all of the **image** elements in the document |
| querySelector(aSelector) | Returns the first element that matches the specified CSS selector, **aSelector** |
| querySelectorAll(aSelector) | Returns all the elements that match the specified CSS selector, **aSelector** |
| title | Returns the document **title** |

### Some commonly used element properties and methods provided by the DOM API

| Property or Method | Description |
| ------------------ | ----------- |
| addEventListener(anEventType, aFunction) | Adds an event listener for **anEventType** to an element. The listener causes the invocation of **aFunction** when the event occurs. |
| appendChild(aChildElement) | Adds **aChildElement** as the last child of an element |
| getAttribute(anAttributeName) | Returns the value of the specified attribute, **anAttributeName**, in an element |
| innerHTML | Returns the content of an element |
| remove() | Removes an element from the document |
| setAttribute(anAttributeName, aValue) | Sets the value of the attribute **anAttributeName** to **aValue** in an element |
| style.aPropertyName | Retrieves the inline CSS style named **aPropertyName** for an element |

### JavaScript Basic Syntax

### Data types

JavaScript supports primitive data types, objects, and arrays.

#### Primitive data types

JavaScript's primitive data types include the following:

* **Boolean**: A Boolean value is either **true** or **false**.
* **Numbers**: These represent an integer, such as **12**, or a floating-point number, such as **3.1415**. JavaScript has a special value **NaN** (not a number), which it typically returns when a calculation does not result in a valid numerical value. For example, if you attempt to divide a number by a string, the result is **NaN**. A number can also have the value of **Infinity** or **-Infinity** if it exceeds the maximum or minimum storage range of the data type, respectively.
* **Strings**: This data type represents text. You enclose a string literal in single or double quotes. **"Hello, World!"** is an example of a string literal.
* **Undefined** and **null**: If you don't assign a value to a variable, its value is **undefined**. If an object is empty, it has a value of **null**.

#### Objects

JavaScript supports the object-oriented programming concepts of *objects* and *classes*. Unlike a primitive data type, an object has properties and methods. A class is a template for creating objects.

Note that you can convert some primitive data types into classes and the other way around. For example, the following code creates a string object from a string literal with a value of **"John"** using the **new** constructor. The code then converts the string object back to a string value using the **valueOf()** method.

```
let firstNameObject = new String("John");
let firstNameString = firstNameObject.valueOf();
```

#### Arrays

An *array* is a collection of values or objects. Arrays are instances of the Array class and have properties and methods. For example, the length property returns the number of elements in an array. In JavaScript, an array has a starting index of 0 and can contain elements of different data types.

You define an array literal by enclosing its elements in square brackets and separating them with a comma. For example, the following code creates an array with three string elements, **"Dogs"**, **"Cats"**, and **"Birds"**, and assigns it to a variable named **petTypes**.

```
let petTypes = ["Dogs", "Cats", "Birds"];
```

### Variables, statements, and comments

In JavaScript, you declare a variable by using the **var** or **let** keyword. The recommended way is to use the **let** keyword, which was introduced in 2015. Use the **var** keyword only if you're running JavaScript in an older browser. To declare a constant, use the **const** keyword.

JavaScript is a dynamically typed language. This means that you don't have to specify a data type when you declare a variable. You can also assign values of different data types to a variable at runtime.

The following code provides examples of variable and constant declarations.

```
let firstName = "John"; 
let telephoneNumber;   // The telephoneNumber variable has a value of undefined.
const EYE_COLOR_BROWN = "Brown"; 
```

Notice the following in the example code:

* After running these statements, the variables **firstName** and **telephoneNumber** have a value of **"John"** and **undefined**, respectively. The constant **EYE_COLOR_BROWN** has a value of **"Brown"**.
* The code initializes the values of **firstName** and **EYE_COLOR_BROWN** using the assignment operator **=**.
* Each statement ends with a semicolon. *All statements in JavaScript must end with a semicolon.* There are situations where JavaScript will automatically insert a semicolon at the end of a statement if you omit it. However, these are exceptions, and you should always end a statement with a semicolon.
* There is a single-line comment after the declaration of the telephoneNumber variable. It is identified by the characters **//** followed by the text **The telephoneNumber variable has a value of undefined.**. A single-line comment starts with the characters **//**. The JavaScript interpreter ignores everything that follows those characters up to the end of the line. To add a multiple-line comment, start the comment text with the characters /* and end it with the characters */.

#### Additional rules and recommendations

* JavaScript is case sensitive.
* A variable name can only contain **letters**, **numbers**, **dollar signs**, and **underscores**. However, **the first character of a variable name can't be a number**.
* As a recommended practice, use camel case or the underscore character to join multiple words in a variable name. This improves the code's readability. For a constant with a primitive data value, use all capital letters.

### Operators

#### Arithmetic operators

| Operator | Description |
| -------- | ----------- |
| + | Addition |
| - | Subtraction |
| * | Multiplication |
| / | Division |
| % | Modulo (Remainder of a division) |

#### Comparison operators

| Operator | Description |
| -------- | ----------- |
| == | Equal to. JavaScript performs type coercion if both operands are not of the same type. |
| != | Not equal to. JavaScript performs type coercion if both operands are not of the same type. |
| === | Equal value and type |
| !== | Not equal value or type |
| > | Greater than |
| < | Less than |
| >= | Greater than or equal to |
| <= | Less than or equal to |

#### Logical operators

| Operator | Description |
| -------- | ----------- |
| && | AND |
| \|\| | OR |
| ! | NOT |

#### Miscellaneous operators

| Operator | Description |
| -------- | ----------- |
| = | Assignment |
| + | String concatenation |
| ++ | Increments the operand (a variable) by 1 |
| -- | Decrements the operand (a variable) by 1 |
| typeof | Returns the type of the operand |

### Conditional statements

You build conditional statements by using variations of the **if-else** statement. In its most basic form, the statement is a simple **if** statement that tests a condition and runs a block of statements if the condition is **true**. The following code shows the syntax of an **if** statement.

```
if (condition) {
    // Statements to run if the condition is true.
}
```

If you also want to run a block of statements if the condition is **false**, you add an **else** clause to the if statement. The following code shows the syntax of an **if-else** statement.

```
if (condition) {
    // Statements to run if the condition is true.
} else {
    // Statements to run if the condition is false.
}
```

If you want to test multiple conditions and run different blocks of statements depending on which condition is true, you can add one or more **else if** clauses to the **if-else** statement. The following code shows the syntax of an **if-else** statement with one **else if** clause.

```
if (condition1) {
    // Statements to run if condition1 is true.
} else if (condition2) {
    // Statements to run if condition2 is true.
} else {
    // Statements to run if none of the previous conditions are true.
}
```

Note that you can also omit the **else** clause.

### Functions

When you declare a function, you specify a name for the function and optional parameters. If the function returns a value, you use the **return** statement to specify the value to be returned.

The following code shows the syntax of a function declaration.

```
function name(parameters) {
    // Statements to run.
}
```

Functions are objects and can be assigned to variables or used as arguments to other functions. When you do so, you do not specify a name for the function. This type of function is called an *anonymous* function. To invoke a function that is assigned to a variable, specify the variable name followed by the function arguments.

The following code shows the syntax of assigning a function to a variable and invoking the function.

```
let functionVariable = function (parameters) {
    // Statements to run.
}
functionVariable(arguments) // Invokes the anonymous function.
```

### Example with validating a phone number entered in a form field

#### Changes to html file containing the form

* Add an **id** attribute to the **telephone number** field to uniquely identify it. You will use this attribute to programmatically retrieve the value of the field by using JavaScript.
* Invoke a JavaScript function named **processForm()** when the user chooses the **Submit** button. The browser should submit the form data only if the function returns a value of **true**. Implement this function in a separate file named **register.js** to follow the best practice of separating JavaScript code from HTML code.
* Declare a script reference to the external **register.js** JavaScript file.

```
<td><input type="tel" name="phoneNumber" id="phoneNumber"></td>
```

```
<form onsubmit="return processForm();">
```

```
<script src="../js/register.js"></script>
```

#### Example of JavaScript file implementation

* The code declares a constant named **US_PHONE_NUMBER** and initializes it with the regular expression pattern for a United States phone number. This constant has the built-in type of **RegExp**.
* The code retrieves the value entered for the telephone field using the **document.getElementById("phoneNumber").value** statement.
* Because the telephone number is optional, the code uses two nested **if** statements to validate it. The first one tests if the field's value is not empty. If this is true, the code then tests if the value matches the regular expression pattern using the **test()** method of the **RegExp** type.

```
// JavaScript functions for the registerWithValidation.html webpage

function formIsValid() {

    // Declare a validation flag and inititialize it to true.
    let valid = true;

    // Validate the telephone number using a regular expression.

    const US_PHONE_NUMBER = /^\d{3}-\d{3}-\d{4}$/;
    let phoneNumber = document.getElementById("phoneNumber").value;

    if (phoneNumber !== "") {
        if (!US_PHONE_NUMBER.test(phoneNumber)) {
            alert("Please enter a telephone number in the format xxx-xxx-xxxx");
            valid = false;
        }
    }

    // Return the value of the validation flag.
    return valid;
}

function processForm() {
    if (formIsValid()) {
        alert("Form submitted");
        return true;
    } else {
        return false;
    }
}
```

### Loops

With a loop statement, you can run a block of code multiple times. JavaScript supports different types of loops, including a **for** loop and **while** loop.

#### For statement

The **for** statement runs a block of statements a number of times based on a counter variable. It has the following syntax:

```
for (initialization expression; condition; increment expression) {
    // Statements to run.  
}
```

The for statement has three parameters—an *initialization expression*, a *condition* to be tested, and an *increment* expression. It operates in the following manner.

1. The statement runs the initialization expression at the beginning of the loop. This expression initializes a counter variable, for example, **let i = 0**.
2. The statement evaluates the condition. The condition compares the value of the counter variable to a maximum value, for example, **i < 12**.
3. If the condition is true, the following occurs:
 3.1. The statement runs the body of the loop.
 3.2. The statement runs the increment expression. This expression increments the counter variable, for example, **i++**.
 3.3. The statement goes back to Step 2.
4. If the condition is false, the loop ends.

#### While statement

The **while** statement runs a block of statements repeatedly while a condition remains true. It has the following syntax:

```
while (condition) {
    // Statements to run.
}
```

Make sure that the condition will eventually evaluate to false. Otherwise, the loop will never end.

### [Lab: Using Dynamic Scripts in a Webpage](./labs/W030Lab2DynamicScripts.md)

### Knowledge Check

#### A developer wants to invoke a JavaScript function when the user chooses an element on a webpage. Which HTML event attribute can the developer define on the element to listen for the occurrence of such an event?

* onclick

Wrong answers:

* oncopy
* onchange
* onload

##### Explanation

* The **onclick** event attribute listens to when the user chooses an element on a webpage.
* The **oncopy** event listens to when the browser starts a copy action.
* The **onchange** event listens to when the value of an element changes.
* The **onload** event listens to when the webpage is fully loaded.

#### Which types of nodes are found in a Document Object Model (DOM) tree? (Select TWO.)

* Element node
* Text node

Wrong answers:

* Browser node
* Event node
* HTTP node

#### A webpage contains a form element with the following input element definition:

```
<input type="text" name="firstName" id="fName">
```

Which statement can a developer use to retrieve the value of the input element?

* document.getElementById("fName").value

Wrong answers:

* document.getElementById("firstName").value
* document.getElementById("firstName").innerHTML
* document.getElementById("fName").innerHTML

Because the method is **getElementById()** and the value of the **input** element's **id** attribute is **"fName"**, the options using **"firstName"** are incorrect. Furthermore, an **input** element does not have any content, because it has no closing tag. Therefore, it does not have an **innerHTML** property.

### Summary

* You can use JavaScript to implement client-side logic in a webpage, make the page more interactive, or present a more dynamic user interface. JavaScript is an interpreted language that can also be used on the server side.
* You can embed JavaScript code directly in an HTML document or write it in an external script file and reference the file in the document. The latter approach is the recommended practice.
* JavaScript code runs when the browser loads the document. It can also run in response to events that occur during the lifecycle of the page or as the user interacts with the page. HTML provides different types of event attributes that you can attach to an element to listen and react to the occurrence of a specific event on the element.
* Client-side JavaScript programming entails accessing and manipulating the elements in an HTML document in response to events. You access a document's elements by using the document's DOM tree, which is represented by the document object. This object exposes the document's content as element, attribute, and text nodes.
* You use properties and methods on the document object to navigate the DOM tree. For example, to find an element in an HTML document, you can use the **getElementByID()** or **querySelector()** methods of the document object.
* JavaScript is a dynamically typed language that offers all the features of a high-level programming language. Its support for functions and ability to define event handlers is particularly useful in client-side scripting.
