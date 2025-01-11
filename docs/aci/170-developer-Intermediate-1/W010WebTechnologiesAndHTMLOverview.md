# Week 1: Web Technologies and HTML Overview

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to repo's main [README.md](../../../README.md)

## Technologies Used in Web Applications

### Web applications examples

* **Ecommerce applications:** Amazon.com is an example of a web application that offers users the ability to browse, search, and purchase products online.
* **Email web applications:** These applications make it possible for individual and enterprise users to access their email. Email web applications often include other communication tools, such as instant messaging and video meetings.
* **Online banking web applications:** Customers use online banking web applications to access their accounts, loans, and investments.

### Common benefits of web applications

* **Convenient Access**. To access a web application, the only tool you need is a web browser. Web browser software is available on almost every type of computing device, including personal computers, tablets, and mobile devices. You can access a web application without the need to download, install, or set up software.

* **Efficient Development**. You only need to develop a single version of a web application, and people can access it from any platform (hardware or operating system). In addition, you can use proven application design and development techniques to reduce the development cycle of a web application. For example, if you use a three-tier architecture, separate development teams can develop each tier simultaneously. This makes a web application an efficient method to implement computer applications. You will learn more about modern application architecture in another course.

* **Scalability**. You can quickly and conveniently handle an increase in the number of users who are accessing a web application. When deployed to the cloud, web applications can scale out automatically, as the number of users increase, without requiring you to purchase additional costly hardware.

### How web applications work

Web applications have a client-server architecture. Their code is divided into two parts: one part runs on the client side and the other part runs on the server side. On the client side, a web application's code runs in the web browser. On the server side, the code runs in a web server, an application server, or both.

A common implementation for web applications is a three-tier architecture that consists of a presentation tier, an application tier, and a data tier.

1. **Client request**. When a user enters a web address in the web browser, or initiates an action to be performed on the server side, the web browser creates an HTTP request. The browser then sends the HTTP request to the web server.
2. **Static webpage response**. If the HTTP request is for a webpage stored on the web server (static webpage), the web server returns the webpage to the web browser in an HTTP response.
3. **Dynamic request processing**. If the HTTP request is for a service or for a webpage that has variable content (a dynamic webpage), the web server forwards the request to the application server. The application server performs the necessary processing for building the dynamic webpage.
4. **Database access**. To build the dynamic webpage, the application server typically accesses data stored in a database server.
5. **Dynamic webpage return**. After the application server finishes building the dynamic webpage, the server returns the webpage to the web server.
6. **Dynamic webpage response**. The web server returns the dynamic webpage to the web browser in an HTTP response.
7. **Browser page display**. When the web browser receives the webpage returned from the web server, it interprets the HTML code in the webpage and displays the page.

### Web application tiers

The three-tier architecture organizes a web application into three logical and physical computing tiers. Each tier uses different components and is implemented using different technologies.

1. **Presentation tier**. The presentation tier presents the application's UI to the user. It captures the interaction between the user and the application by displaying and collecting information to and from the user. This tier runs on a web browser and a web server. The web server provides the UI in the form of a webpage, and the web browser displays the webpage to the user. The basic technologies used in developing the presentation tier of a web application are HTML, CSS, and JavaScript.
2. **Application tier**. The application tier is also called the logic tier. It processes the information collected by the presentation tier. It performs the necessary business logic to implement the application's functions. For example, an ecommerce application has logic in the application tier that checks if inventory is available. The logic tier uses an application server, which typically communicates with the data tier to add, modify, or delete data processed by the application. The technologies used in developing the logic tier of a web application include Python, Java, Hypertext Preprocessor (PHP), and Ruby.
3. **Data tier**. The data tier is also called the database tier. It stores and manages the data processed by the application. It uses a database server, which runs a relational database management system, such as MySQL or PostgreSQL, or a NoSQL database, such as Amazon DynamoDB. All communication between the presentation tier and the data tier goes through the application tier.

### HTTP protocol

Web applications use HTTP to exchange data between the client and the server. HTTP is a request-response protocol. The client sends a request to the server (HTTP request), and the server sends a response back to the client (HTTP response).

#### HTTP Request

The HTTP request captures the information that a client, such as a web browser, sends to the server to access a resource on the server. It comprises three main parts: a request line, headers, and a body.

The request line is the first line of an HTTP request. At a minimum, it has the following three elements:

* **Method**: The method indicates which type of action the client wants to perform on the server. Commonly used HTTP methods include the following:
* **GET**: Retrieve a resource from the server.
* **PUT**: Create or update a resource on the server.
* **POST**: Send data to the server for processing.
* **DELETE**: Delete a resource from the server.
* **Path**: The path identifies which resource to access on the server.
* **HTTP version number**: This number indicates the version of the HTTP specification the request complies with.

One or more headers come after the request line in an HTTP request. A request header provides the server with information about the client, how the client wants to communicate with the server, and information about the message in the body. Each request header is a name-value pair.

The body is the last part of an HTTP request. It contains any message or data the client wants to send to the server. The message body is optional and depends on the HTTP method of the request. For example, a request with a GET method does not have a message body because it asks the server to retrieve a resource. In contrast, a request with a POST method has a message body that contains the data that is sent to the server.

The following illustration provides an example of an HTTP request that retrieves the home page of the Amazon.com website.

```
GET / HTTP/1.1
Host: www.amazon.com
User-Agent: curl/8.7.1
Accept: */*
```

* In the request line, the method is **GET** and the path is **/**. This indicates that the request is to retrieve the root document of the website. In addition, the HTTP version number is **HTTP/1.1** to indicate HTTP version 1.1.
* Three request headers come after the request line as follows:
* The first header identifies the server where the request is sent. It has a name of **Host** and a value of **<www.amazon.com>**.
* The second header identifies the client as a curl. It has a name of **User-Agent** and a value of **curl/8.7.1**.
* The third header specifies different key-value pairs like **Accept-Language: en-US** the client accepts for the webpage or message that the server returns.
* Notice that this example does not have a body. This is because the method is a GET request to retrieve a webpage. It does not require any additional information to be sent to the server.

#### HTTP Response

The HTTP response captures the information the server sends back to the client in response to an HTTP request. It comprises three main parts: a status line, headers, and a body.

The **status line** is the first line of an HTTP response. It consists of the following three elements:

* **HTTP version number**: This number indicates the version of the HTTP specification the response complies with.
* **Status code**: The status code is a three-digit number that indicates the outcome of processing the request. Status codes are classified by the range of their values and have the following meanings:
* **Informational (100–199)**: The request was received and is being processed.
* **Successful (200–299)**: The request was successfully received, understood, and accepted.
* **Redirection (300–399)**: The request requires further action to complete the request.
* **Client error (400–499)**: The request contains incorrect syntax or can't be fulfilled.
* **Server error (500–599)**: The server failed to fulfill an apparently valid request.
* **Reason phrase**: Text that describes the status code.

One or more headers come after the status line in an HTTP response. A response header provides information about the server that sent the response or additional information about the response for the client to process. For example, a server can include a response header to indicate to the client that the response should not be cached anywhere. Similar to a request header, a response header is a name-value pair.

The body is the last part of an HTTP response. For a successful response, the body contains the resource or data requested by the client or additional status information about the action requested by the client. For a unsuccessful response, the body might contain further information about the error that was encountered in processing the request. For certain status codes, the message body might be empty.

The body comes after the headers and is preceded by a blank line. It contains the HTML document for the webpage requested by the client.

The HTTP protocol also has a security extension that is commonly used in web applications. If you want to secure the communication between the client and the server, you can use HTTPS. HTTPS is a version of HTTP that encrypts the data exchanged between the client and the server using the SSL or TLS protocol. By using HTTPS, you can ensure the confidentiality, integrity, and authenticity of the data that is exchanged. For example, when transferring a credit card number between a browser and a web server, you can use HTTPS for confidentiality.

### Relationship between HTML, CSS, and JavaScript

* You use HTML to define the content and structure of a webpage.
* You use CSS to define the layout of a webpage.
* You use JavaScript to control the behavior of a webpage.

### Summary

* A web application is software that you access over the internet using a web browser. It has a client-server architecture with some components running in the web browser and other components running in a web server or application server. A web application typically stores its data on a database server.
* The client-side components and server-side components of a web application use the HTTP protocol to communicate with each other. The protocol uses a request-response model and provides methods to GET, PUT, POST, and DELETE resources. You can secure the communication by using HTTPS.
* You use HTML, CSS, and JavaScript to create a webpage. You use HTML to create the webpage content, CSS to define the webpage layout, and JavaScript to control the webpage behavior.
* You can use Python and other programming languages, such as Java and PHP, to implement the server-side components of a web application.

## HTML Overview

### History of HTML

Sir Tim Berners-Lee created HTML in the early 1990s. It was originally used to create and share scientific documents on the internet. It was later adapted to describe any type of document that a web browser can display.

HTML is an open standard, and its specification has evolved over the years.

* **1991**. Berners-Lee invents HTML while working for the European Organization for Nuclear Research (CERN).
* **1995**. A working group organized by the Internet Engineering Task Force (IETF) publishes HTML 2.0.
* **1997**. The World Wide Web Consortium (W3C) makes a recommendation to publish HTML 3.2.
* **1999**. W3C makes a recommendation to publish HTML 4.01. This was the most widely used version of HTML throughout the 2000s and into the early 2010s.
* **2000**. W3C makes a recommendation to publish a combination of HTML and XML called XHTML 1.0. It is similar to HTML, but has stricter rules to increase extensibility and interoperability with multiple data formats.
* **2008**. W3C and WHATWG work together to release the first public draft of HTML5. Developers begin to adopt HTML5 in 2008, and it is used steadily after 2012.
* **2014**. W3C makes a recommendation to publish the first official release of HTML5.
* **2017**. W3C makes a recommendation to publish HTML5.2.

Today, the World Wide Web Consortium (W3C) and the Web Hypertext Application Technology Working Group (WHATWG) govern the evolution of the HTML specification.

### Summary

* HTML is a text-based markup language that is used to define the content and structure of a webpage. It is an open standard that is governed collaboratively by the World Wide Web Consortium (W3C) and the Web Hypertext Application Technology Working Group (WHATWG).
* An HTML document consists of a document type declaration line, a head part, and a body part. Most of the content of a webpage displayed by a web browser is defined in the body part.
* The content and structure of an HTML document is described by HTML elements. The structure of an HTML element consists of an opening tag, the element content, and a closing tag. HTML elements can be nested to represent a document hierarchy.
* Because HTML ignores white spaces, you should use HTML elements to structure text.
* Some common elements that you can define in the **head** element are **meta**, **title**, and **style**.
* Some common elements that you can define in the **body** element are **paragraph**, **heading** and **comment**.
* You can use the **image** element to add a picture to an HTML document and the **anchor** element to add a link.
