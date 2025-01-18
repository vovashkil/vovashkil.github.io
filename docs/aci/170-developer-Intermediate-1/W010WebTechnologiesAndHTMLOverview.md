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

### Pre-assessment

#### What is a valid file name extension for an HTML document? (Select TWO.)

* .html
* .htm

Wrong answers:

* .js
* .txt
* .css

The .htm extension is an older convention, and .html is recommended as the file name extension for an HTML document today.

#### What is a feature of HTML?

* HTML supports mixed-character case in tag and element names.

Wrong answers:

* HTML is sensitive to indentation levels.
* HTML is a compiled language.
* HTML is governed by a single privately owned company.

##### Explanation

* HTML is not sensitive to indentation levels.
* HTML is an interpreted language, not a compiled language.
* Today, the HTML specification is governed by the World Wide Web Consortium (W3C). It is a public-interest, non-profit organization where member organizations and the public work together to develop web standards.

#### Which HTML tag can be used to add an image to a webpage?

* <img>

Wrong answers:

* <a>
* <iframe>
* <link>

With the <img> tag, it's possible to specify the file name path of an image to include on the webpage.

* Use the <a> tag to add a hyperlink to a page.
* Use the <iframe> tag to include an inline frame to a page (a page within a page).
* Use the <link> tag to link external documents to a page, such as a Cascading Style Sheet.

### History of HTML

Sir Tim Berners-Lee created HTML in the early 1990s. It was originally used to create and share scientific documents on the internet. It was later adapted to describe any type of document that a web browser can display.

HTML is an open standard, and its specification has evolved over the years.

* **1991**. Berners-Lee invents **HTML** while working for the European Organization for Nuclear Research (CERN).
* **1995**. A working group organized by the Internet Engineering Task Force (IETF) publishes **HTML 2.0**.
* **1997**. The World Wide Web Consortium (W3C) makes a recommendation to publish **HTML 3.2**.
* **1999**. W3C makes a recommendation to publish **HTML 4.01**. This was the most widely used version of HTML throughout the 2000s and into the early 2010s.
* **2000**. W3C makes a recommendation to publish a combination of HTML and XML called **XHTML 1.0**. It is similar to HTML, but has stricter rules to increase extensibility and interoperability with multiple data formats.
* **2008**. W3C and WHATWG work together to release the first public **draft of HTML5**. Developers begin to adopt HTML5 in 2008, and it is used steadily after 2012.
* **2014**. W3C makes a recommendation to publish the first official release of **HTML5**.
* **2017**. W3C makes a recommendation to publish **HTML5.2**.

Today, the World Wide Web Consortium (W3C) and the Web Hypertext Application Technology Working Group (WHATWG) govern the evolution of the HTML specification.

### Structure of an HTML document

An HTML document consists of three parts as follows:

* Document type definition
* Head
* Body

#### HTML example

```
<!doctype html>
<html>
  <head>
    <title>This is the page title.</title>
  </head>
  <body>
    <h1>This is a level 1 heading.</h1>
    <p>The second nested element is a paragraph element that contains the text This is a paragraph.</p>
  </body>
</html>
```

#### Document type definition

The <!doctype html> declaration specifies the version of HTML that the document uses. In this example, it specifies the version HTML5.

```
<!doctype html>
```

The **<!doctype>** declaration must be the first line in an HTML document. It informs the web browser which version of HTML the document is written in. In HTML 4.01 or XHTML 1.0, the declaration requires a reference to a Document Type Definition (DTD) document that specifies the rules for the markup language used, so browsers can parse and render the content correctly. In HTML5, the declaration no longer requires a reference to a DTD, and it consists of the following line: **<!doctype html>**.

The **<!doctype>** declaration is not an HTML tag, but an instruction to the web browser. It is case-insensitive and can be written as **<!DOCTYPE html>**.

#### HTML root element

The HTML root element contains the head element and body element.

#### Head

The head element has a nested title element that defines the title of the document as **This is the page title**.

The head of an HTML document contains metadata about the page and is defined using the head element. Metadata is information about data. For HTML documents, metadata is information about the data in the document. The web browser uses this information to control the content and the display of the page. Search engines also use metadata about a page.

The HTML elements you can use in a head element include the following:

* **<meta>**: Use this element to specify metadata about the document, such as the author and the character set used. For example, for browsers to correctly display your document content, regardless of the language used, specify the following meta element: **<meta charset="UTF-8">**. The UTF-8 character set includes characters from virtually all human languages.
* **<title>...</title>**: Use this element to provide a title for your HTML document. As a best practice, you should always specify a title for a webpage. This title is displayed in the browser's tab for the page.
* **<link>**: Use this element to reference an external document used by the current page. One of the most common uses for this element is to refer to an external CSS file.
* **<style>...</style>**: Use this element to define the internal CSS rules that are used in the document. You will learn more about this element in a later course.

The web browser does not display any content you define in the head element except for the content in the title element.

#### Body

The body element has two nested elements. The first one is a heading element that contains the text **This is a level 1 heading**.

The second nested element is a paragraph element that contains the text **This is a paragraph**.

The body is defined using the body element, and contains the elements of an HTML document that are displayed by the web browser. You will typically write most of the code for your webpage in the body element. HTML provides a vast number of elements you can include in the body element to structure, define, and mark up your content.

Some common HTML elements found in the body element include the following:

* <h1>, <h2>, <h3>, <h4>, <h5>, <h6>: Use these elements to define headings and subheadings at different nested levels.
* <p>..</p>: Use this element to define a text paragraph. The browser displays the text on a new line and adds some white space before and after the paragraph.
* <img>: Use this element to include a graphics file in a document.
* <a>...</a>: Use the anchor element to define a hyperlink.

### Text Elements and Comments

#### Adding paragraphs

```
      <p>German shepherds are a breed of dogs that originated in Germany. They are large and muscular and typically have a black and tan coat. Some have a solid black coat. German shepherds are intelligent and loyal dogs.</p>

      <p>Siamese cats originated in Thailand and are a breed of short-haired cats. They are medium-sized and have a distinct color pattern. The color of their face, ears, legs, and tails are darker than the rest of their body. Siamese cats can live up to 20 years.</p>
```

#### Defining headings

You can use heading elements to format text that represent titles or subtitles in an HTML document. Use headings to define the content structure of a document, not to emphasize text. There are six levels of headings you can define with the elements that use the <h1>, <h2>, <h3>, <h4>, <h5>, and <h6> tags. Each level renders text in a progressively smaller font.

```
<!doctype html>
<html lang="en">
   <head>
      <meta charset="UTF-8">
      <title>Pet Types</title>
   </head>
   <body>
      <h1>Breeds of Pets</h1>

      <h2>Dogs</h2>

      <p>German shepherds are a breed of dogs that originated in Germany. They are large and muscular and typically have a black and tan coat. Some have a solid black coat. German shepherds are intelligent and loyal dogs.</p>

      <h2>Cats</h2>

      <p>Siamese cats originated in Thailand and are a breed of short-haired cats. They are medium-sized and have a distinct color pattern. The color of their face, ears, legs, and tails are darker than the rest of their body. Siamese cats can live up to 20 years.</p>
   </body>
</html>
```

#### Adding comments

* Single line comment:

```
<!-- This is a single comment line -->
```

* Multiple line comment

```
<!-- 
   This is the first comment line.
   This is the second comment line.
   This is the third comment line.
 -->
```

### Images

1. Place the **image** element in the position on the page where you want the image to be inserted. The image will appear in line with the other elements that surround it, without any line breaks.
2. Add a source (**src**) attribute to specify the path to the image file. The value of the path is a URL.
3. Add an alternative text (**alt**) attribute for accessibility that provides a description of the image. The browser also displays the alternative text if it cannot find the image.
4. Optionally, add a **width** and **height** attribute to scale the image so it is displayed at the correct size on the page. The values for both attributes are expressed in pixels.

### Links

You can create a link in an HTML document using the **anchor** element, which is defined using the <a> tag. You specify the destination of the link in an href attribute. The value of this attribute depends on the type of destination, as follows:

* For a link to a document in the same website, the href value is the **relative URL** of the document. This URL omits the protocol and domain name part of the full URL. For example, the attribute **href="pages/home.html"** refers to the document named **home.html** located in the **pages** directory on the same server as the referring page.
* For a link to a document on a different website, the href value is the **absolute URL** of the document. For example, the attribute **href="https://aws.amazon.com"** refers to the home page of the **Amazon Web Services** website.
* For a link to an element in the same document (a local link), the href value is the **id** of that element. This means that you have to add an id attribute to the destination element. For example, if you have an element with an **id** attribute of **"aboutUs"** in your document, you can create a link to it by specifying **href="#aboutUs"**.

### HTML Development Best Practices

* **Use lowercase characters consistently for HTML tag names**. This makes your code easily readable.
* **Write valid HTML code**. Even though browsers tolerate HTML syntax errors, try to avoid writing incomplete or broken code.
* **Use an HTML validator tool**. To check whether the HTML code in your webpage is correct, use an online validator tool. A validator tool is particularly useful if your editor or IDE does not provide a function to fully validate HTML code.
* **Test on multiple browsers**. Because each browser can have a different way of interpreting HTML, you might notice a slight difference in how a given webpage is displayed. Test the rendering of your webpage on common browsers, such as Mozilla Firefox, Google Chrome, Apple Safari, and Microsoft Edge.

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

### [Lab: Creating an HTML Webpage](./labs/W010Lab1HTMLPage.md)

### Summary

* HTML is a text-based markup language that is used to define the content and structure of a webpage. It is an open standard that is governed collaboratively by the World Wide Web Consortium (W3C) and the Web Hypertext Application Technology Working Group (WHATWG).
* An HTML document consists of a document type declaration line, a head part, and a body part. Most of the content of a webpage displayed by a web browser is defined in the body part.
* The content and structure of an HTML document is described by HTML elements. The structure of an HTML element consists of an opening tag, the element content, and a closing tag. HTML elements can be nested to represent a document hierarchy.
* Because HTML ignores white spaces, you should use HTML elements to structure text.
* Some common elements that you can define in the **head** element are **meta**, **title**, and **style**.
* Some common elements that you can define in the **body** element are **paragraph**, **heading** and **comment**.
* You can use the **image** element to add a picture to an HTML document and the **anchor** element to add a link.
