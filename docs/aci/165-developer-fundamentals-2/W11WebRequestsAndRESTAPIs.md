# Web Requests and REST APIs

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to repo's main [README.md](../../../README.md)

## Web Requests

### Pre-assessment

#### Which Python library provides a high-level interface for making HTTP requests and processing HTTP responses?

* Requests

Wrong answers:

* urllib3
* pandas
* BeautifulSoup

The Python Requests library is used to make HTTP requests and process HTTP responses. It provides a user-friendly interface for sending GET, POST, and other requests and manipulating the resulting data.

The other options are incorrect for the following reasons:

* **urllib3** is a lower-level HTTP library. Although it can be used to make HTTP requests, it is more complex and less user-friendly compared to the Requests library. Requests builds on top of urllib3 and makes the process of making HTTP requests less complicated.
* **pandas** is a library used for data manipulation and analysis. It provides powerful tools for working with structured data, such as data frames, but it is not designed for making HTTP requests or interacting with web APIs.
* **BeautifulSoup** is a package used for parsing HTML and XML files. It is commonly used for web scraping to extract data from webpages but does not provide functionality for making HTTP requests. Instead, it works in conjunction with libraries like Requests to retrieve and parse the content.

#### What is an HTTP request as it relates to web communication?

* Message sent from a client to a server that specifies an action to be performed

Wrong answers:

* File containing JavaScript
* Method for rendering webpages in a browser
* Database query used to retrieve information from web servers

HTTP requests are an essential part of web communication, where a client (such as a web browser or application) requests a resource or process from a server. They include the request type (GET, POST, and so on), headers, and parameters. The server processes the request and sends an HTTP response containing the requested data.

The other options are incorrect for the following reasons:

* A file containing JavaScript is used to add interactivity to webpages and does not relate to the structure or purpose of an HTTP request.
* Browser rendering interprets HTML, cascading style sheets (CSS), and JavaScript for webpage visuals. It is unrelated to sending HTTP requests.
* A database query is used for data retrieval from databases. It is not directly related to HTTP requests.

#### A pizza restaurant chain is building an app for customers to see pizzas available for delivery orders with toppings, sizes, and crusts as options.

The following is a sample API endpoint:

```
http://api.example.com/api/pizzas?toppings=mushrooms,pepperoni&size=large&crust=thin
```

What does the toppings=mushrooms,pepperoni&size=large&crust=thin part of the URL indicate? (Select TWO.)

* It specifies the order details for a large, thin-crust pizza with mushroom and pepperoni toppings.
* It represents query string parameters specifying the toppings, size, and crust type.

Wrong answers:

* It is the URL for a pizza recipe webpage.
* It is a request for a list of available pizza sizes.
* It is a query to find pizza restaurants that offer large pizzas.

The other options are incorrect because of the following:

* The URL does not lead to a pizza recipe webpage.
* The URL does not indicate a request for a list of available pizza sizes.
* The URL does not search for pizza restaurants offering large pizzas.

## HTTP Protocol Overview

HTTP is the fundamental protocol used to transfer data across the web. It acts as the foundation for data communication on the web, facilitating the transfer of hypertext requests and information between servers and clients. Web browsers can use this protocol to fetch and display webpages from servers, making the internet navigable and functional.

Most website addresses begin with either **http://** or **https://**, such as **https://aws.amazon.com**.  

Most website addresses use HTTPS instead of HTTP because HTTPS builds on HTTP to provide more secure communication. Imagine you are on your bank's website. HTTPS ensures that your personal and financial information is encrypted and protected from potential threats. The differences between HTTP and HTTPS are as follows:

* **HTTP**: This is a protocol that structures the way data is requested and delivered over the web. It forms the backbone of web communication, ensuring that your browser can retrieve and present the content you seek from various servers around the globe.
* **HTTPS**: HTTPS stands for hypertext transfer protocol secure. It is an extension of HTTP that integrates security through cryptography, safeguarding the data exchanged between your browser and web servers. This secure version of HTTP is essential for protecting sensitive information online.

### HTTP basic role and function

#### Client

The client is a device or software that requests data from a server-provided service. It acts as the user’s interface to the internet.

#### Web browser

A web browser is software installed on the client that makes it possible for users to access websites. The browser retrieves files, such as images, text, or downloadable files, from the web server and displays them to the user. Common web browsers include Google Chrome, Internet Explorer, Microsoft Edge, Firefox, and Safari.

#### URI

A URI is a string of characters that uniquely identifies a resource on the internet and provides a means to access it. A URI can contain the following:

* **Uniform resource locator (URL)**: The URL specifies the internet protocol, directory path, file name, and, possibly, a search directive. It’s akin to giving someone the directions, including the name and address, to locate a person.
* **Uniform resource name (URN)**: This is a globally unique and persistent identifier, similar to a person’s name. It defines the identity of a resource without implying its location.

### HTTP key features

#### Connectionless

HTTP operates in a connectionless manner. After a client sends a request and the server returns the response, the connection is closed. The client must create a new connection for any subsequent requests that it sends to the server.

#### Media independent

HTTP is media independent, meaning it can handle various types of data as long as both the server and the client can process the data format. With this flexibility, HTTP can support text, images, videos, and more.

#### Stateless

Each HTTP request is independent, meaning that the server does not retain any information from previous requests. This stateless nature makes the protocol more straightforward and reduces server overhead.

Web browsers can use HTTP to retrieve and display webpages, making it possible for users to browse the internet. HTTP is also used to interact with APIs so applications can communicate with web servers to request and send data.

An API is a set of rules that makes it possible for different software entities to communicate with each other. APIs make the implementation and maintenance of software more efficient by providing clear guidelines for interaction. They make it more efficient to develop software that can communicate with other systems.

### API Applications

#### Social media APIs

Social media sites, like X and Facebook, offer APIs that developers can use to automatically create apps that can post statuses, retrieve messages, or analyze social media engagements.

#### Payment gateways

Services like PayPal and Stripe provide APIs that make it possible for online stores to process payments securely without the need to handle sensitive financial information directly.

#### Weather services

APIs from providers like OpenWeatherMap make it possible for applications to access real-time weather data. This is useful for apps that need to deliver weather updates or use weather conditions to make decisions.

#### Maps and location services

Developers can use map APIs, like the Google Maps API, to embed maps into their websites or apps, offering functionalities like location tracking, route planning, and distance calculation.

**In summary, HTTP is a vital protocol that underpins web communication, making it possible to transfer data between clients and servers. Its stateless, connectionless, and media-independent nature makes it an efficient and versatile protocol for web interactions.**

### HTTP request-response cycle

The client sends an HTTP request, and the server sends back an HTTP response.

#### Client request

The cycle begins when the client, typically a web browser, sends an HTTP request to the server. This request can be for various resources, such as webpages, images, or data from an API.

#### Server processing

The server receives the request and processes it. This involves interpreting the request, fetching the necessary resources, and preparing an appropriate response.

#### Server response

The server sends an HTTP response back to the client. This response includes the requested resource, status information, and any relevant headers.

#### Response received

The client receives the response and renders the content for the user. For example, a browser might display a webpage, or an application might process the data received from an API.

### HTTP request structure

HTTP requests are foundational for interacting with web-based services. HTTP is a client-server protocol. This means the client initiates requests and sends them to a host located on a server, which then processes the requests and waits for an appropriate response. The server validates the requests and acts accordingly, depending on the request method, to deliver an HTTP response containing a status line, headers, and a message body.

#### Request line

```
GET /index.html HTTP/1.1
```

The request line can include the following components:

* **Method**: The HTTP method specifies the action to be performed. Common methods include the following:
 * **GET**: Retrieves data from the server
 * **POST**: Sends data to the server to create a new resource
 * **PUT**: Updates an existing resource on the server
 * **DELETE**: Deletes a resource from the server
 * **HEAD**: Similar to GET, but only retrieves the response headers, not the body
 * **PATCH**: Similar to PUT, but only updates part of a resource instead of replacing it
 * **CONNECT**: Establishes a tunnel to the server
 * **OPTIONS**: Describes the communication options for the target resource
* **URI**: Indicates the resource on the server you want to interact with and is often the path to a specific page or endpoint, such as /index.html
* **HTTP version**: Specifies the HTTP version being used, such as HTTP/1.1 or HTTP/2

#### Headers

```
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
Content-Type: application/json
Authorization: Bearer <your_access_token>
Accept-Language: en-US.
```

HTTP headers provide additional information about the request. They are key-value pairs separated by a colon. Common headers include the following:

* **Host**: Specifies the domain name of the server
* **User-Agent**: Provides information about the client making the request, such as the browser type
* **Accept**: Indicates the content types the client can process, such as text, html and application, json
* **Content-Type**: Specifies the media type of the body of the request (used with POST and PUT requests)
* **Authorization**: Contains credentials for authenticating the client with the server, such as a bearer token
* **Accept-Language**: Indicates the preferred languages for the response, such as en-US or fr-CA

#### Request body

```
{ 	
    "username": "newuser",
    "password": "pass123" 
}
```

The body contains the data being sent to the server. It is usually included in POST and PUT requests.

Examples of request bodies include the following:

* **Form Data**: Data submitted from a web form
* **JSON**: Structured data often used in API requests

#### Example POST request

```
POST /api/v1/users HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Content-Type: application/json
Authorization: Bearer <your_access_token>
Accept-Language: en-US

{ 	
    "username": "newuser",
    "password": "pass123"
}
```

This POST request is designed to create a new user in the API provided by the server at **www.example.com**. The path **/api/v1/users** indicates that this action is being performed on the users resource of version 1 of the API. The request includes the necessary headers to provide information about the client, the format of the request body, authentication, and language preferences. The JSON body contains the user details to be created on the server.

### URLs

```
https://docs.aws.amazon.com/codecommit/?id=docs_gateway
```

#### Protocol

In this example, **https://** specifies that the HTTPS protocol is being used for communication. This protocol ensures that the data is encrypted and secure.

#### FQDN

The fully qualified domain name (FQDN) is the complete address, including all subdomains and the top-level domain (TLD), as follows:

* **docs.aws** is the subdomain used to organize the website's documentation section.
* **amazon** is the primary domain name registered by Amazon.
* **.com** is the TLD, indicating the domain’s highest level in the DNS hierarchy.

#### Port

This is the port number that the web server listens to for the request. The port number typically varies with the type of protocol used. For HTTP, the default port number is 80. For HTTPS, it is 443. In this example, **:443** specifies that the HTTPS port is being used. If the port is omitted from the URL, the HTTPS defaults to port 443.

#### Endpoint

The endpoint is the specific path on the server being accessed, which, in this example, is **/codecommit/**. Endpoints help the server determine which action to perform or which data to return.

#### Query string parameters

The query string parameters are key-value pairs appended to the URL to provide additional information to the server. Here, **?id=docs_gateway** might indicate a specific document or gateway to be accessed.

*query string* parameters are used to pass additional information to the server. They are appended to the URL after a question mark (?) and consist of key-value pairs separated by an equals sign (=). Multiple parameters can be included by separating them with an ampersand (&).

#### Query string parameters example

```
https://example.com/search?query=python&sort=recent
```

In the example URL, **query=python** specifies that the search query is for Python tutorials, and **sort=recent** specifies that the results should be sorted by the most recent items.

```
https://bookstore.example.com/browse?category=fiction&author=doe&price_range=10-20
```

The raw HTTP GET request would be as follows:

```
GET /browse?category=fiction&author=doe&price_range=10-20 HTTP/1.1
Host: bookstore.example.com
User-Agent: Mozilla/5.0
Accept: text/html
```

**Even though query string parameters and headers are both specified as key-value pairs, query string parameters are included in the URL to provide additional data for the request. Headers provide metadata about the request and are not part of the URL.**

In the previous bookstore request, **/browse?category=fiction&author=doe&price_range=10-20** specifies the resource path (**/browse**) and query parameters as follows:

* **category=fiction** indicates the book category.
* **author=doe** specifies the author's name.
* **price_range=10-20** specifies the price range for the search.

In addition, the GET request includes the host (**bookstore.example.com**), which indicates the domain name of the server. It includes the following request headers:

* **User-Agent: Mozilla/5.0** provides information about the client making the request.
* **Accept: text/html** indicates that the client expects an HTML response.

### HTTP response structure

An HTTP response is the server's reply to the request initiated by the client. Its purpose is to provide the requested resources, confirm the successful application of the request, or address any encountered errors. The response comprises a status line, headers, and a body containing the requested data or error messages.

#### Status line

```
HTTP/1.1 200 OK\
```

The status line contains the following information:

* **HTTP version**: This indicates the version of the HTTP protocol used, such as HTTP/1.1 or HTTP/2.
* **Status code**: This is a three-digit code indicating the result of the request. Status codes are categorized as follows:
 * **1xx - Informational**: The request was received and is continuing to process.
 * **2xx - Successful**: The request was successfully received, understood, and accepted (for example, 200 OK).
 * **3xx - Redirection**: Further action needs to be taken to complete the request (for example, 301 Moved Permanently).
 * **4xx - Client error**: The request contains bad syntax or cannot be fulfilled (for example, 404 Not Found).
 * **5xx - Server error**: The server failed to fulfill an apparently valid request (for example, 500 Internal Server Error).

#### Headers

```
Content-Type: text/html
Content-Length: 26904
Connection: keep-alive
Date: Wed, 18 Jan 2023 22:01:46 GMT
Server: Server
```

Headers provide additional information about the response, such as metadata about the data being returned, server information, and control directives. Common headers include the following:

* **Content-Type**: Indicates the media type of the response body, such as text/html or application/json.
* **Content-Length**: Specifies the size of the response body in bytes.
* **Connection**: Indicates whether the network connection stays open after the current transaction finishes. The value **keep-alive** means that the connection will be kept open for further requests. Alternatively, the value can be **close**, indicating that the connection will be closed after the response is sent.
* **Date**: Provides the date and time when the response was generated.
* **Server**: Identifies the server software that handled the request, such as Apache or NGINX. It can also be generic (**Server**) to obfuscate the server details for security reasons.

#### Response body

```
<!DOCTYPE html>
<html>
<head>
    <title>Example</title> 
</head>
<body> 
    <h1>Hello, world!</h1>
</body>
</html>
```

The response body contains the data requested by the client, such as HTML, JSON, or images. The body is included in the response if the request is successful and data needs to be returned.

#### Example HTTP response

```
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 26904
Connection: keep-alive
Date: Wed, 18 Jan 2023 22:01:46 GMT
Server: Server

<!DOCTYPE html> 
<html>
<head>
    <title>Example</title>
</head>
<body>
    <h1>Hello, world!</h1>
</body>
</html>
```

The status line is the first line in the response, and it provides three important pieces of information: the HTTP version (**HTTP/1.1**), the status code (**200** - successful), and the reason phrase (**OK** is a brief description of the status code). The response also includes five response headers that provide information about the **Content-Type**, **Content-Length**, **Connection**, **Date**, and **Server**.

Finally, the body of the response contains the actual data requested. In this case, it is an HTML document.

### HTTP status codes

For a complete list and detailed explanations, see [Mozilla Developer Network (MDN) HTTP Response Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status).

| Status Code Category | Status Code | Description |
| -------------------- | ----------- | ----------- |
| 1xx - Informational | 100 Continue | The server received the request headers, and the client should proceed to send the request body. |
| 2xx - Successful | 200 OK | The request was successful. |
| 3xx - Redirection | 301 Moved Permanently | The resource has moved to a new URL permanently. |
| 4xx - Client Error | 400 Bad Request | The server did not understand the request because the syntax was not valid. |
| | 401 Unauthorized | Authentication is required and failed or was not provided. |
| | 404 Not Found | The requested resource was not found. |
| 5xx - Server Error | 500 Internal Server Error | The server encountered an unexpected condition. |
| | 502 Bad Gateway | The server received a response that was not valid from an inbound server that it accessed while attempting to fulfill the request. |

Status codes come in the form of a three-digit number that you can use to quickly identify the outcome of an HTTP request. For example, a 4xx status code indicates a client-side error, meaning that something went wrong on the client's end. If a server responds to your request with a 4xx status code, you might want to check the following:

* Was the request sent in the appropriate syntax that the server expects, or is it missing parameters?
* Do you have the necessary authentication settings configured to authorize the request?
* Does the resource you are attempting to access exist?

A 5xx status code signifies a server-side error, indicating that the server encountered an issue while processing the request. The server or endpoint might be experiencing downtime or some other problem might hinder it from processing the request. Because there is nothing the client can do to resolve this, *exponential backoff* is a common way to address server-side errors. This involves the client reattempting the request with exponentially longer wait times between each failed attempt. At some point, the server is expected to come back online to process the request and return a 2xx status code, indicating a successful request.

Each component of an HTTP response provides critical information that aids in effective communication between the client and server. The status code informs you whether the request was successful or if an error occurred, and headers provide metadata about the response.

### Using curl to sending HTTP requests

curl, which stands for **client URL**, is a command line tool for sending and receiving data that uses a wide variety of protocols, including HTTP.

```
curl -I https://docs.aws.amazon.com/codecommit/
```

This command sent a HEAD request to the specified URL and retrieved the status line and HTTP headers only, without the response body.

```
curl https://docs.aws.amazon.com/codecommit/
```

#### Finding a raw HTTP request

```
curl -v -I https://docs.aws.amazon.com/codecommit/
```

In the verbose output, notice that some lines start with >, which represents the raw HTTP request sent by curl. Let's review only the section of the response that includes those lines, as follows:

```
> HEAD /codecommit/ HTTP/1.1
> Host: docs.aws.amazon.com
> User-Agent: curl/7.81.0
> Accept: */*
> 
```

It includes the request line with the HTTP method (**HEAD**), path (**/codecommit/**), the HTTP version (**HTTP/1.1**), and the host header and other headers included in the request.

### Python Requests Library and HTTP Requests

### Requests library features

#### Support for HTTPS

You can make HTTP requests that are protected by TLS to secure communication between the client and the server. Similar to a web browser, the Requests library verifies TLS certificates to ensure that the communication is secure.

#### Connection pooling

Opening and closing an HTTP connection can be a time-consuming operation. The library maintains and manages a pool of prebuilt HTTP connections. When a client opens an HTTP connection, the library retrieves one of the prebuilt connections. When the client closes the connection, the library returns it to the pool. This feature enhances the performance of requests by reusing HTTP connections and provides scalability when the number of requests increases.

#### Session with cookie persistence

Because the HTTP protocol is stateless, if a client wants to preserve data between requests, they have to do so programmatically. With the Requests library, you can create a Session object to persist data across requests. The data is stored in a cookie, which the library carries over from one request to another without needing programmatic management.

### Installing the Requests library

1. To verify if the Requests library is already installed or to display which version is installed, run the following command:

```
pip show requests
```

2. To install the Requests library, run the following command:

```
pip install requests
```

3. After installing the Requests library, you can start using it in a Python script by first importing it with the following statement:

```
import requests
```

### Using the Requests library

The Requests library provides a single object named requests that you use to access the library's functionality. This object exposes methods that you invoke to make different types of HTTP requests and receive responses.

#### get(url, params=None, **kwargs)

This **get()** method sends an HTTP GET request. The method's parameters are as follows:

* **url** specifies the endpoint URL and path of the request.
* **params** is optional and represents parameters to send in the query string of the request. You can assign a dictionary, a list of tuples, or bytes to the params parameter.
* **kwargs is optional and represents one or more keyword arguments that are passed with the request.

This method returns a Response object.

#### put(url, data=None, **kwargs)

The **put()** method sends an HTTP PUT request. The method's parameters are as follows:

* **url** specifies the endpoint URL and path of the request.
* **data** is a keyword parameter that represents the information to send in the body of the request. You can assign a dictionary, a list of tuples, bytes, or a file-like object to the data parameter. If you want to send the information in a JSON format, use the **json** keyword parameter instead. The information must be a JSON serializable Python object, such as a dictionary.
* **kwargs is optional and represents one or more keyword arguments that are passed with the request.

This method returns a Response object.

#### post(url, data=None, json=None, **kwargs)

The **post()** method sends an HTTP POST request. The method's parameters are as follows:

* **url** specifies the endpoint URL and path of the request.
* **data** and **json** are keyword parameters that represent the information to send in the body of the request. If you want to send the information in a JSON format, use the json keyword parameter. The information must be a JSON serializable Python object, such as a dictionary. Otherwise, use the **data** keyword parameter. You can assign a dictionary, a list of tuples, bytes, or a file-like object to the data parameter. The Requests library assigns a default value of None to each of these parameters.
* **kwargs is optional and represents one or more keyword arguments that are passed with the request.

This method returns a Response object.

#### delete(url, **kwargs)

The **delete()** method sends an HTTP DELETE request. The method's parameters are as follows:

* **url** specifies the endpoint URL and path of the request.
* **kwargs is optional and represents one or more keyword arguments that are passed with the request.

This method returns a Response object.

#### head(url, **kwargs)

The **head()** method sends an HTTP HEAD request. The method's parameters are as follows:

* **url** specifies the endpoint URL and path of the request.
* **kwargs is optional and represents one or more keyword arguments that are passed with the request.

This method returns a Response object.

#### patch(url, data=None, **kwargs)

The **patch()** method sends an HTTP PATCH request. The method's parameters are as follows:

* **url** specifies the endpoint URL and path of the request.
* **data** is a keyword parameter that represents the information to send in the body of the request. You can assign a dictionary, a list of tuples, bytes, or a file-like object to the data parameter. If you want to send the information in a JSON format, use the json keyword parameter instead. The information must be a JSON serializable Python object, such as a dictionary.
* **kwargs is optional and represents one or more keyword arguments that are passed with the request.

This method returns a Response object.

#### request(method, url, **kwargs)

The **request()** method constructs an object of type Request and sends the request. You can use this method to make a request using any of the HTTP method types. The method's parameters are as follows:

* **method** specifies the HTTP method and that it can have a value of GET, PUT, POST, DELETE, OPTIONS, HEAD, or PATCH.
* **url** specifies the endpoint URL and path of the request.
* **kwargs is optional and represents one or more keyword arguments. A commonly used keyword argument is params, which represents parameters to send in the query string of the request. Similarly, the data or json keyword arguments represent parameters to send in the body of the request.

This method returns a Response object.

A Response object represents the HTTP response the server returns after processing the HTTP request.

### [Web Requests and REST APIs Practice Environment](./W11APIPracticeEnvironment.md)

### Practice using the API exposed by the Pets service

| HTTP Method | URL Path | Description |
| ----------- | -------- | ----------- |
| GET | /pets | This returns a JSON string containing a list of all the pets in the database and their attributes. |
| GET | /pet/{id} | * This returns a JSON string containing the attributes of the pet identified by {id}. |
| PUT | /pet | * This creates a new pet or updates a pet in the database. The attributes of the new or updated pet must be provided in the body of the request as a JSON string. If the service finds an item with the provided id attribute in the database, it performs an update operation. Otherwise, the service performs a create operation.
* It returns a JSON string confirming the pet creation or update and its id attribute. |
| DELETE | /pet/{id} | * This deletes the pet identified by {id} from the database.
* It returns a JSON string confirming the pet deletion and its id attribute. |

#### Making a GET request to retrieve all pets

```
import requests

# Initialize the API's endpoint URL.
petsURL = "https://6rkxwg3aua.execute-api.us-west-2.amazonaws.com"

# Make the request.
response = requests.get(petsURL + "/pets")

# Print the response.
print(response.text)
```

Output:

```
[{"owner": "Carlos", "id": "2", "name": "Olfie", "birthDate": "2019-06-06", "gender": "F"}, {"owner": "John", "id": "1", "name": "Fluffy", "birthDate": "2021-08-10", "gender": "F"}]
```

#### Making a GET request to retrieve a specific pet

```
import requests

# Initialize the API's endpoint URL.
petsURL = "https://6rkxwg3aua.execute-api.us-west-2.amazonaws.com"

# Specify the id of the pet to retrieve.
id = "1"

# Make the request.
response = requests.get(petsURL + "/pet/" + id)

# Print the response.
print(response.text)
```

Output:

```
{"owner": "John", "id": "1", "name": "Fluffy", "birthDate": "2021-08-10", "gender": "F"}
```

#### Making a PUT request to add a pet

```
import requests

# Initialize the API's endpoint URL.
petsURL = "https://6rkxwg3aua.execute-api.us-west-2.amazonaws.com"

# Initialize the new pet's information.
newPet = {
    "id": "3",
    "name": "Rocky",
    "gender": "M",
    "birthDate": "2018-12-01",
    "owner": "Jane"
}

# Make the request.
response = requests.put(petsURL + "/pet", json=newPet)

# Print the response.
print(response.text)
```

Output:

```
"Created or updated item 3"
```

#### Making a DELETE request to delete a pet

```
import requests

# Initialize the API's endpoint URL.
petsURL = "https://6rkxwg3aua.execute-api.us-west-2.amazonaws.com"

# Specify the id of the pet to delete.
id = "2"

# Make the request.
response = requests.delete(petsURL + "/pet/" + id)

# Print the response.
print(response.text)
```

Output:

```
"Deleted pet 2"
```

#### Making a PUT request to update a pet

```
import requests

# Initialize the API's endpoint URL.
petsURL = "https://6rkxwg3aua.execute-api.us-west-2.amazonaws.com"

# Initialize the new pet's information.
petUpdate = {
    "id": "1",
    "name": "Fluffy",
    "gender": "F",
    "birthDate": "2018-12-01",
    "owner": "Kwesi"
}
                          
# Make the request.
response = requests.put(petsURL + "/pet", json=petUpdate)

# Print the response.
print(response.text)
```

Output:

```
"Created or updated item 1"
```

```
[
  {
    "owner": "Kwesi",
    "id": "1",
    "name": "Fluffy",
    "birthDate": "2018-12-01",
    "gender": "F"
  },
  {
    "owner": "Jane",
    "id": "3",
    "name": "Rocky",
    "birthDate": "2018-12-01",
    "gender": "M"
  }
]
```

#### Processing response data

#### Respond object methods

##### content

* Content of the response in byte format

##### headers

* Dictionary containing the response headers

##### raw

* File-like representation of the response
* Useful in situations where you want to start processing the response without waiting for the entire response to be downloaded
* Requires you to set the parameter stream=True on the invoking request

##### reason

* Textual description of the HTTP status code of the response

##### status_code

* HTTP status code of the response

##### text

* Content of the response in Unicode format

##### json(**kwargs)

* Returns the content of the response decoded as JSON
* Useful if the returned data has a JSON format

```
import requests

# Initialize the API's endpoint URL.
petsURL = "https://6rkxwg3aua.execute-api.us-west-2.amazonaws.com"

# Make the request.
response = requests.get(petsURL + "/pets")

# Print the different parts of the response.
print("Response status code:")
print(response.status_code)
print("\nResponse status code reason:")
print(response.reason)
print("\nResponse headers:")
print(response.headers)
print("\nResponse content as Unicode text:")
print(response.text)
print("\nResponse content decoded as JSON:")
print(response.json())
print("\nResponse content in bytes:")
print(response.content)
print("\nResponse content as raw:")
print(response.raw)
AWSLabsUser-jCbH4KxhR
```

Output:

```
Response status code:
200

Response status code reason:
OK

Response headers:
{'Date': 'Fri, 20 Dec 2024 21:26:40 GMT', 'Content-Type': 'application/json', 'Content-Length': '180', 'Connection': 'keep-alive', 'Apigw-Requestid': 'DHAangGlPHcEP6w='}

Response content as Unicode text:
[{"owner": "Kwesi", "id": "1", "name": "Fluffy", "birthDate": "2018-12-01", "gender": "F"}, {"owner": "Jane", "id": "3", "name": "Rocky", "birthDate": "2018-12-01", "gender": "M"}]

Response content decoded as JSON:
[{'owner': 'Kwesi', 'id': '1', 'name': 'Fluffy', 'birthDate': '2018-12-01', 'gender': 'F'}, {'owner': 'Jane', 'id': '3', 'name': 'Rocky', 'birthDate': '2018-12-01', 'gender': 'M'}]

Response content in bytes:
b'[{"owner": "Kwesi", "id": "1", "name": "Fluffy", "birthDate": "2018-12-01", "gender": "F"}, {"owner": "Jane", "id": "3", "name": "Rocky", "birthDate": "2018-12-01", "gender": "M"}]'

Response content as raw:
<urllib3.response.HTTPResponse object at 0x7d2232456050>
```

### Knowledge Check

#### What are standard HTTP methods for sending requests? (Select TWO.)

* PUT
* POST

Wrong answers:

* ADD
* HEADER
* CREATE

The other options are incorrect because of the following:

* **ADD** is not a standard HTTP method.
* **HEADER** is not a standard HTTP method. Headers are part of an HTTP request but not a method.
* **CREATE** is not a standard HTTP method.

#### A user sends an HTTP request and receives a 4xx status code in the response. Which options should the user consider? (Select TWO.)

* Check that the syntax of the request is valid.
* Check that the appropriate authentication settings were used to carry out the request.

Wrong answers:

* Proceed to send the request body because the status code is informational.
* Do nothing as the request was successful.
* Reattempt the request at a later time because the server is experiencing issues.

The other options are incorrect because of the following:

* The status code is not informational. Informational status codes are in the 1xx range.
* The request was not successful because a 4xx status code indicates an error. Successful requests are indicated by 2xx status codes.
* The error is on the client side, not the server side. Server-side errors are indicated by 5xx status codes, so reattempting the request later is unlikely to resolve the issue without making changes to the request.

#### A developer uses the Requests library in a Python script to make an HTTP request to a web server. The server returns a response. Which property of the Response object should the developer access to retrieve the content of the response in Unicode format?

* text

Wrong answers:

* content
* ucode
* raw

The text property of a Response object contains the content of the response in Unicode format.

The other options are incorrect because of the following:

* The **content** property contains the content of the response in byte format.
* The **ucode** property is not a property of a Response object.
* The **raw** property is a file-like representation of the response.

### Summary

* The HTTP protocol is the backbone of web communication. HTTP is stateless, connection-less, and media independent, which makes it ideal for web interactions. It has a secure counterpart, HTTPS, which encrypts data to protect sensitive information. HTTP is a request-response protocol. When you send an HTTP request to a server, the server returns an HTTP response.
* An HTTP request has multiple components, including an HTTP method, HTTP version, path, headers, and body. The HTTP method specifies the action to be performed on the server resource (for example GET, POST, PUT, or DELETE). The HTTP version identifies the version of the protocol used by the request. The headers and body contain metadata about the request and the content sent to the server, respectively. In addition, an HTTP request can have query string parameters that contain information to be passed to the resource.
* An HTTP response includes an HTTP version, status code, headers, and response body. The HTTP version indicates the protocol version used in the response. The status code is a three-digit number that categorizes the outcome of the request (for example, 200, 400, or 404). The headers provide additional metadata about the response. The response body contains the actual data requested, such as HTML, JSON, or images, and is included if the request is successful.
* An API provides a way for computer programs to communicate with each other. It makes it possible to have seamless interactions between software applications, such as social media sites, payment gateways, weather services, and mapping technologies.
* You can use the Python Requests library to programmatically make requests to websites and web APIs by using the HTTP protocol. The Requests library is not part of the Python standard library and requires a separate installation.
* To make an HTTP request using the Requests library, you can use one of the following methods: get(), put(), post(), delete(), head(), patch(), and request(). Using the first six methods, you can make a request with an HTTP method that corresponds to the method's name. The request() method is a generalized method that you can use to make a GET, PUT, POST, DELETE, HEAD, or PATCH request.
* All the Requests library methods used to make a request return a response object. You can use the methods and properties of a response to access the various parts of the returned data and facilitate its manipulation. For example, the text property contains the response data in Unicode format. The json() method returns the content of the response decoded as JSON.

## REST APIs

### Pre-assessment

#### Which design principles are associated with REST API architecture? (Select THREE.)

* Statelessness
* Uniform interface
* Layered system

Wrong answers:

* Synchronous communication
* Monolithic design
* Use of XML data format

A REST API should be designed to be stateless, which means that it does not maintain client state. The client must send all required information to the server for the server to process its request. A REST API should also provide a uniform interface, with standardized request and response formats. It should also make use of a layered system. This means that calls and responses in REST APIs can go through different layers of intermediaries, such as load balancers and proxies, to improve performance and security. The client and server are oblivious to the additional layers through which requests and responses, respectively, travel.

The other options are incorrect because of the following:

* REST APIs typically use asynchronous communication, not synchronous communication.
* REST architecture recommends a modular design, not a monolithic design.
* REST architecture does not prescribe a data format, although JSON is the more common data format.

#### What is the primary benefit of a REST API's lightweight design?

* Straightforward to use and self-descriptive

Wrong answers:

* Allows for the use of complex data structures for data transmission
* Promotes the use of caching to improve performance
* Enables the client and server to be written in different programming languages

RESTful API design should be lightweight and flexible. This makes a RESTful API developer-friendly and intuitive to use.

The other responses are incorrect because of the following:

* RESTful APIs do not use complex data structures to transmit information. They allow transmission of data in popular data formats, such as JSON, XML, and HTML.
* A RESTful API design does promote the use of caching, but this is due to its scalability and ability to optimize client-server interactions, rather than its lightweight design.
* A RESTful API does enable the client and server to be written in different programming languages, but this is due to the separation between the client and server in a RESTful API design, rather than its lightweight design.

#### A developer wants to write a POST request that creates a new resource through a REST API. Which elements will they MOST likely need to include in the client code? (Select THREE.) 

* Request body
* Request parameters
* Request headers

Wrong answers:

* Basic authentication credentials
* Response body
* HTTP status

A POST request is used to create a new resource, such as a user account or a forum post. The request body contains the data that should be used to contain the new resource. Request parameters, such as path or query parameters, can be used to pass in additional information with the POST request. This includes the type of resource being created or the id of another resource with which to associate the new resource. Request headers are often included with POST requests to contain additional information for the server, such as authentication tokens or content type.

The other options are incorrect because of the following:

* Although POST requests often require authentication, basic authentication is not a widely used strategy because it is not very secure.
* The client does not send a response body with a POST request. The client receives a response body from the server after the server has processed the request.
* The client does send an HTTP status with a POST request. An HTTP status is received by the client from the server and indicates the success or failure of the request.

### API Overview

APIs enable applications to interact by defining a set of rules for software components.

The *application* part of the name refers to any software designed for a specific purpose. The *programming* and *interface* components represent the contract that allows two or more applications to interact with each other. An API facilitates these interactions through code, in addition to any hardware or software needed for the communication.

In APIs, the application sending the request is the client, and the server is another application sending the response. The API defines how a client (the code that needs the exposed functionality) interacts with the server (the code that exposes the functionality). This definition forms the contract between the two.

APIs can be public, meaning they are accessible to anyone; private, meaning they are used only internally within a company; or partner, which are shared between companies.

Many APIs, especially public and partner APIs, require authentication to ensure secure access. Common methods include API keys and OAuth tokens, which help protect the API from unauthorized use.

Weather apps on your smartphone are examples of public APIs. These apps do not create the data themselves. Instead, they use APIs to connect to various weather services, send requests, and display the responses on your device. The API facilitates or streamlines the process of obtaining data from the weather services.

### Understanding APIs: Types and uses

#### REST

*Representational state transfer (REST)* is not technically a protocol or a standard but an architectural style for networked applications. REST APIs allow for data transfer in formats such as JSON, HTML, plaintext, or media files. This type of API architecture uses only HTTP/HTTPS for communication, which makes it less flexible than some other APIs, like Simple Object Access Protocol (SOAP), regarding communication methods. However, REST is very popular due to its scalable and stateless nature.

With REST APIs, you can perform specific data operations on a remote server. For example, a mobile app could retrieve, update, or delete user profiles on a cloud server by using REST APIs.

#### RPC

In a *Remote Procedure Call (RPC) API*, the operations exposed by the server are presented as procedures or functions that take parameters and return results. This is similar to calling a function in programming, except the caller (client) and callee (server) are on different machines. 

With RPC APIs, developers can call remote functions on external servers as if they were local to their software. For example, you could enhance a financial application by remotely calling calculation functions on a separate financial service.

#### SOAP

*Simple Object Access Protocol (SOAP)* uses XML to transfer data over HTTP, HTTPS, Simple Mail Transport Protocol (SMTP), User Datagram Protocol (UDP), and Transmission Control Protocol (TCP). It is favored for its flexible communication methods and ability to handle stateful requests. This can be crucial for applications needing to maintain connection information for security or other purposes. SOAP offers high reliability and predictable exchanges between applications. However, a major drawback is that SOAP requires the use of XML and has strict communication requirements.

SOAP APIs facilitate complex transactions and ensure secure, reliable communication between applications. For example, a corporate software system could use SOAP APIs to handle secure transactions and data exchanges with a supply chain management system.

#### WebSocket

*WebSocket* is a protocol that enables a persistent, two-way communication session between the client and the server. This allows for quicker interactions, because the client can receive event-driven responses from the server without needing to poll the server. The connection remains active until ended by either the client or the server.

For example, a gaming application can use WebSocket APIs to allow real-time communication and updates between players across different devices.

### REST API components

#### Inputs

When designing an API, you need to define which information must be provided to the API. 

These details are known as the *input parameters*, which could include data like user IDs, search terms, or configuration settings.

#### Operations

Operations in an API specify the actions the API should perform upon receiving inputs. These define what each part of the API does with the given resources or collections.

In REST APIs, operations correspond to specific functions, often mapped to HTTP methods like GET, POST, PUT, or DELETE, combined with a URL path.

#### Endpoint

An API endpoint is the specific URL where the API can be accessed. It comprises the server's address and a path that locates the API service on the server.

For example, in a REST API, an endpoint might be something like https://api.example.com/users, where actions defined by operations are performed.

#### Outputs

*Outputs* refer to the data that the API sends back to the client after processing a request. 

For example, if a client requests the current weather, the output might be a JSON object containing the temperature, humidity, and weather conditions.

### Basics of REST APIs

The term REST is an acronym for *Representational State Transfer*. REST is not a specification or standard. Instead, it is an architectural style that contains a set of rules to give developers a flexible and lightweight way to integrate applications. The REST architectural style emphasizes stateless communication and interaction with resources using standard HTTP methods.

### Benefits of a RESTful API

* **Lightweight**: RESTful APIs rely on the HTTP standard that is straightforward to use. A RESTful request is self-descriptive because you can examine its HTTP method and URI, and know the intent of the request. REST is also format-agnostic, so you can use popular data formats, such JSON, XML, and HTML. You do not need to wrap data in a complex structure for transmission.
* **Independence**: In a REST API design, the application that exposes the API is completely independent from the clients that use it. You can write the client in a different programming language or technology than the server application without affecting the API design. Changes to the implementation of the client and server applications do not affect each other. The same API can also be used by different types of clients, such as a web or mobile applications.
* **Scalability**: Systems that implement RESTful APIs can scale efficiently because REST optimizes client-server interactions. A RESTful API design promotes the use of caching to improve performance. You can use a cache to return a response directly to the client without having to pass the request the server. This reduces server processing and increases scalability.

### The REST architectural style design principles

#### Cacheable

REST requires servers to mark responses as either cacheable or not cacheable. Systems and clients can choose to allow caching or cache responses to improve performance on the client side and increase scalability on the server side. If the client and server allow caching, the client is allowed to store server data on the client.

#### Layered system

Calls and responses in REST APIs go through different layers of intermediaries that the client and server are oblivious to. This means that neither the client nor server knows whether they are speaking to an intermediary or the end application. Components in the system are unable to see beyond their own layer. This type of design makes it possible for the use of load balancers and proxies to improve performance and provide improved security for protected resources.

#### Client-server independence

In a RESTful design, the client and the server are completely independent of each other. This allows for updates and maintenance of each to occur separately without fear of affecting the other. 

#### Stateless

A RESTful API is stateless. The server does not maintain the client state, so each interaction on the server-side is isolated from other interactions. This also means that the client must ensure all required information is provided to the server for the server to process the request.

#### Code on demand

In the REST architectural style, a server can send code to the client to extend or customize the client's functionality. A response can contain executable code that the client can run on demand. For example, suppose a browser client is presenting a registration page with a phone number to the user. When the user first enters a value for the phone number, the client can invoke a REST API to download code that validates the phone number and run the code in the browser.

#### Uniform interface

A uniform interface indicates that the server receives requests and transfers information to the client in a standard format. All RESTful requests identify a resource on the server using a URI, and all requests for the same resource have the same URI. This forces clients to access all resources using the same set of standards. Likewise, when the server sends a response back to the client, the response has a standard format and contains all the information that client needs to process the response.

The resources that are accessed by a RESTful API can include text files, HTML pages, videos, table data, or images. Resources can be represented in different formats, such as text, HTML, XML, or JSON. However, JSON and XML are the most common.

### REST API Operations

A RESTful API uses HTTP methods to indicate the type of operation to perform on a resource. In particular, it uses the following four HTTP methods to invoke create, read, update, and delete (CRUD) operations:

* **POST**: Create a record
* **GET**: Read a record
* **PUT**: Update a record
* **DELETE**: Delete a record

RESTful APIs use the different parts of an HTTP request and response to pass important information, such as the resource URI, metadata, authorization tokens, caching instructions, and cookies.

### RESTful API authentication methods

RESTful APIs can perform authentication to validate the identity of the client making a request. Authentication is the process of verifying that you are who you claim to be.

REST APIs can use traditional HTTP authentication schemes such as Basic and Bearer.

#### Basic Authentication

Basic authentication prompts the user to enter a user ID and password, and encodes them using Base64. Base64 is a binary-to-text encoding scheme that transforms binary data into printable characters. The encoded user ID and password pair is sent in the *Authorization* header of the request. For example, a Basic64 encoded user ID and password would be included in the request header as follows:

```
Authorization: Basic  am9oblNtaXRoOlBhc3N3b3JkMQ==
```

Basic authentication is not considered very secure. It relies solely on the secrecy of a user ID and password, and its Base64 encoding scheme can be effortlessly decoded. For these reasons, it is not a recommended authentication method. If you use Basic authentication, use it with HTTPS for added security.

#### Bearer Authentication

Bearer authentication is commonly referred to as *token authentication*. This scheme uses security tokens to grant access to a protected resource. The token is referred to as a *bearer token* or *access token* and is created by an authentication server. The name *bearer authentication* means *Give access to the bearer of this token*. The token is sent in the Authorization header of the request and has the following format:

```
Authorization: Bearer <token>
```

Bearer authentication should only be used with HTTPS.

#### RESTful APIs authentication using an API key

ou use an API key when you want to authenticate the application that is making the API request, not the individual user. An API key is a generated unique value that is assigned to a client application. When the application makes an API request, the server identifies the calling application by the API key. The server will grant access to the protected resource as long as the API key is presented with the request and remains valid. API keys are primarily intended to identify application traffic from API clients. One common use case for API keys is to monitor API usage.

An API key is sent in the Authorization header of the HTTP request based on the following format:

```
Authorization: Apikey <key>
```

#### Open Authorization (OAuth) standard to authenticate RESTful API calls

OAuth is a scheme that allows a website or application to access resources that exist on another website or application on behalf of a user. OAuth uses access tokens, typically a bearer token, to authenticate a user.

### Using curl options for REST APIs

```
curl [OPTIONS] [URL]
```

#### curl options

* **-I (--head)**: Fetches only the headers of the response
* **-v (--verbose)**: Provides detailed information about the request and response, including the raw request sent by curl

| Option | Description | Example |
| ------------------------- | -------------------------- | ------------------------ |
| -X (--request) <command> | Specify the request method to use | curl -X POST -d "name=John" https://example.com |
| -d (--data) <data> | Send data in a request (primarily used in POST and PUT requests) | curl -X PUT -d "name=John" -d "id=123" https://example.com/users/123 |
| -i (--include) | Include response headers in the output | curl -i https://example.com |
| -o (--output) <file> | Write to file instead of standard output | curl -o fileName https://example.com |
| -O (--remote-name) | Write output to a file named as the remote file | curl -O https://example.com/filename |
| -T (--upload) <file> | Transfer local file to destination | curl -T fileName https://example.com |
| -u (--user) <user:password> | Set username and password for server authentication | curl -u userName:Password1 https://example.com |
| -G (--get) | Uses the GET HTTP method for the request | curl -G -d "tool=curl" https://example.com |
| -H (--header) <header> | Pass custom headers to the server | curl -H "Content-Type: application/json" -d '{"name":"John", "id":123}' https://example.com/users/123 |

#### [Curl Documentation Overview](https://curl.se/docs/)

When using the single dash option, you do not have to put a space between the option and its value, but it is recommended. When using double-dash options, it is a requirement that a space exists between the option and the value.

#### Using -X, -H, and -d options in a PUT request

```
curl -X PUT -H "Content-Type: application/json" \
-d '{"id":"5","name":"Dax","gender":"M","birthDate":"2020-1-1","owner":"Mia"}' \
https://6rkxwg3aua.execute-api.us-west-2.amazonaws.com/pet

```

Output:

```
"Created or updated item 5"
```

The command uses curl to send a PUT request with JSON data to the Pets API. This request creates a new item in the Pets database with the details provided in the JSON data. The following is a breakdown of the options used in the request:

* **-X**: This option specifies the HTTP request method to use. In this case, **PUT** is used to create or update a resource on the server.
* **-H**: This option adds a header to the request. The header specifies the type of content being sent. Here, **"Content-Type: application/json"** indicates that the data sent is in JSON format.
* **-d**: This option sends the JSON data in the request body, which includes the details of the pet.

#### Using the -G option to send a GET request

When using **-d** to send data, curl defaults to a POST request unless otherwise specified. By combining **-G** with **-d**, you can append the data to the URL as query parameters while still making a GET request.

```
curl -G https://6rkxwg3aua.execute-api.us-west-2.amazonaws.com/pet/5
```

Output:

```
curl -G https://6rkxwg3aua.execute-api.us-west-2.amazonaws.com/pet/5
```

#### -i curl option to return both the response headers and body in a single request

```
curl -G -i https://6rkxwg3aua.execute-api.us-west-2.amazonaws.com/pet/5
```

Output:

```
HTTP/2 200 
date: Fri, 20 Dec 2024 22:57:15 GMT
content-type: application/json
content-length: 82
apigw-requestid: DHNrzhZHPHcEPLg=

{"owner": "Mia", "id": "5", "name": "Dax", "birthDate": "2020-1-1", "gender": "M"}
```

#### Saving the response to a local file

```
curl -G -i -o response.txt https://6rkxwg3aua.execute-api.us-west-2.amazonaws.com/pet/5
```

Output:

```
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    82  100    82    0     0    172      0 --:--:-- --:--:-- --:--:--   172
```

```
AWSLabsUser-jCbH4KxhRnWb8L27fxTYx1:~/environment $ cat response.txt 
HTTP/2 200 
date: Fri, 20 Dec 2024 22:58:51 GMT
content-type: application/json
content-length: 82
apigw-requestid: DHN63jLPvHcEMqQ=

{"owner": "Mia", "id": "5", "name": "Dax", "birthDate": "2020-1-1", "gender": "M"}
```

### API Design Best Practices

* Keep API simple, use intuitive endpoints for user-accessible resources.
* Even using XML instead of JSON for your REST API, ensure your API can at least respond to JSON requests.

#### Naming standards

Make names for resources, operations, and variables clear and consistent within the service. Keep names short and descriptive. If this is not possible, it could indicate that an operation or object should be broken into smaller parts. Often, an organization has specific naming standards to follow. Keep these in mind when developing APIs to prevent future name changes to align with requirements.

If you need to include two words to best portray the endpoint's purpose, separate the words with a dash, like /senior-leadership. It is also best to avoid using special characters as much as possible and, if they can’t be avoided, use ones within the ASCII character set. Anything outside the ASCII character set cannot be used directly by a URL. Special characters reserved for other uses by operating systems or applications would need to be encoded. For more information see [RFC 3986 - Uniform Resource Identifier (URI): Generic Syntax](https://tools.ietf.org/html/rfc3986). For now, it is best to use unreserved alpha characters, digits, hyphens (-), periods (.), and underscores (_).

Use a hierarchical structure with forward slashes to separate endpoints into logical groups, like /users/photos instead of user-photos. Identify user-accessible resources, not database structure. Avoid exposing unintended resources via endpoints.

#### Nouns

Only use nouns to identify endpoints. The nouns should signify what each resource does. The reason you should not use verbs in your endpoint name is that your HTTP method is your verb. If you look at the URL as a sentence, the resource or collection would be the noun and the HTTP method is the verb, because it is the action that will occur on the resource or collection.

Use plural nouns if the endpoint contains all of something or a collection of something. For instance, products could be used for an endpoint that contains all available products. Another example would be posts for an endpoint that contains all the posts made by a company. This can help prevent a user from deleting an entire collection, because the plural noun signifies more than just one.

#### Versioning

Make your versioning clear and provide proper documentation on changes. Then, users can decide if they want to use the new version or stay with an older version of the API. Versioning also ensures that invalid requests do not reach your updated endpoints.

You can provide versioning in the header or the URL. Having the versioning in the URL increases browser discovery, making it more convenient for developers or users to navigate to the various versions. An example of URL versioning would be https://example.com/v2/.

You could also do a combination of the two, such as using URL versioning for all major version changes and header versioning to navigate down to smaller sub-version changes. For example, in v3.5, the 3 indicates the major version, while the .5 represents the fifth minor update or iteration of the v3 API.

#### Selecting and designing HTTP methods

You should ensure that GET methods do not alter the state of the endpoint. Read operations (like GET requests) should only read and return data. They should not modify the data they are requesting. Modifying data with a GET request is called a side effect and can be unexpected and problematic for an API. It should be obvious to a client when an operation will or will not make a change to the system. Use PUT, POST, and DELETE methods for operations that alter the state.

It is also important to remember that GET, PUT, and DELETE methods should be *idempotent*, which means that repeated calls with the same parameters should always have the same result. This is because identical inputs, like with a call to retrieve information, should always result in the system having the same end state.

On the other hand, POST and PATCH methods are *not idempotent* because they change the end state. If a user were to make multiple identical POST requests, such as placing an online order, each request would process separately, resulting in the same item being purchased multiple times.

#### Handling HTTP status codes and error responses

Status codes are crucial to good API design. They provide users with information about the outcome of their requests, whether successful or if an error was encountered. By including the appropriate status codes in your API responses, users can understand what happened and which action, if any, they need to take.

One example is to use a 204 response code for successful DELETE requests in APIs. Another would be to use the 403 status code for unauthorized actions.

The following table includes some of the common HTTP status codes you might want to include in your API.

| Code and message | Type | Meaning |
|----------------- | ---- | ------- |
| 200 OK | Success | The request was successful. |
| 201 CREATED | Success | The request was successful and a new resource was created. |
| 202 ACCEPTED | Success | The request was successful but has not been completed yet. Should be used for operations that might take a long time to complete. |
| 204 NO CONTENT | Success | The request response body is intentionally empty. Typically used for PUT, POST, or DELETE requests when the API declines to return a message or representation. Also used in GET requests to indicate the resource exists but does not have state representation. |
| 301 MOVED PERMANENTLY | Redirection | The resource has moved to a new URI. Used to specify the relocation of a resource. The new location should be included in the response’s location header. |
| 400 BAD REQUEST | Client Error | An error occurred on the client side. Used to throw errors that do not fit any of the other error codes found in 4xx. |
| 401 UNAUTHORIZED | Client Error | There is a problem with the client’s credentials. |
| 403 FORBIDDEN | Client Error | The client request was formed correctly, but the API forbade access. Used to enforce application-level permissions. |
| 404 NOT FOUND | Client Error | The client’s URL doesn’t map to any resource. |
| 405 METHOD NOT ALLOWED | Client Error | The HTTP method used is not allowed for the resource. |
| 408 REQUEST TIMEOUT | Client Error | The server did not receive a complete request in the time allotted by the server. |
| 500 INTERNAL SERVER ERROR | Server Error | The API malfunctioned. |

Error handling is an important part of API design. Well-designed and well-documented errors assist client developers in creating robust applications. Errors should have descriptive names that clarify what is happening, even if the developer or user does not have the API documentation in front of them.

An API might also have a set of error codes that add further details or context to an error. For example, if a user is logging in through an authentication API, there could be multiple reasons for rejecting a login attempt. A single AuthenticationRejectedError might be defined for this situation, and accompanying error codes can indicate the exact reason for the rejection. For instance, it could be that no authentication credentials were sent (status code 401) or the credentials are not permitted access (status code 403). Including detailed error codes helps developers handle different error cases without requiring the API to define many specific errors. Use the correct HTTP status codes to notify users of errors.

Beyond notifying the user of the request status, it is also a good practice to include error messages that provide more context on the issue. At a minimum, any 400 status codes or validation errors should be accompanied by a consumable JSON error message. 

For example, a 400 Bad Request response might include a JSON error message like the following:

```
{
  "error": "InvalidRequest",
  "message": "The 'email' field is required."
}
```

#### Ensuring clarity and future-proofing in API design

##### Extending with new endpoints

When adding new features to an API, avoid the temptation to reuse operations by adding flags (additional parameters) to the input or output that change the operation's behavior. To maintain clarity, create new endpoints unless those flags are purely for sorting and filtering results.

For example, if your library API started offering movies in addition to books, it would be better to create separate operations for movies rather than adding a flag like *type=movie* to make existing operations return movies instead of books. Overloading operations with such flags makes documentation harder to interpret and complicates extending operations in the future. Each operation should have one responsibility. If new functionality is needed, add new operations rather than making existing ones more complex.

##### Filtering, sorting, and pagination

For endpoints containing large amounts of data, use design patterns that include filtering, sorting, and pagination to help users find specific information conveniently.

*Filtering* limits the results returned based on specific criteria using URL query string parameters.

*Sorting* can be enabled in the URL by specifying a query string parameter that users can use to sort the data found in a resource. A common query string parameter for sorting is the word *sort*. It is straightforward and should be intuitive to the user.

*Pagination* limits the number of results returned in one response, similar to navigating through pages of data on a website.

##### Parameters

There are different types of parameters you can pass to a RESTful API, including path, query, and body parameters.

Resource identifiers should be path parameters (for example, *playlists/1234*). Use lowercase letters to reduce the potential for mistakes. If it is necessary to separate words in a path, use hyphens.

Query string parameters should be used for querying, as well as for filtering or sorting (for example, *playlists/1234?sort=random* to return playlist songs in random order).

Body parameters should be used for POST and PUT requests to send the data required for create or update operations. Keep in mind that the body parameter is not part of the URL. When you call a POST API with curl, for example, you would pass the body separately using the -d flag.

##### Documentation

Ensure that you have clear and detailed documentation for your API. This will help users understand how to use the API correctly and to its full potential. Documentation should include the following:

* All endpoints available to the user
* Examples of allowable requests to the endpoints
* Status codes and messages that can be encountered while using the API

When documenting an API, writing a lengthy text document can be prone to ambiguity, leading to developers misinterpreting the instructions and implementing the API incorrectly.

To prevent these types of errors, you can use an *interface definition language (IDL)* to capture the details of the API. IDLs provide a specific structure and syntax to an API design. In some cases, the IDL can be used by automated processes to generate various software artifacts, such as libraries, or generate the API documentation for you. The unambiguous, standardized format of an interface definition language is both human- and machine-readable, and enables tools that can do the following:

* Validate that the definition is complete and correct
* Generate starter code for both the client and server

There are many types of interface definition languages. Some are independent of implementation details, such as programming languages. Others are implementation-specific. You can describe models, inputs, outputs, and errors that define your API independently of the language used for implementation and how your clients will call it.

**An interface definition language also separates the concerns of various aspects of API development, so different teams can own different parts.**

Defining the API early allows server and client teams to work independently on their respective parts.

These client teams might be responsible for another backend service, website, data analysis job, and other aspect that calls the defined API. Both teams can be confident that the server and client components will integrate seamlessly at deployment time, as long as they adhere to the API definition.

Some common tools and frameworks for defining RESTful APIs include OpenAPI, Coral (an Amazon DL), and Smithy.

Your API should satisfy the following best practices:

* Provide clear and accessible documentation
* Be straightforward and hard to misuse
* Be complete so all exposed functionality works
* Allow for modifications

### Knowledge Check

### A developer is building a REST API for a forum application for users of a video game. They have a /users endpoint for user data, and they need to choose a name for another endpoint that will hold users' photo data. Which endpoint follows best practices for REST API resource names?

* /users/photos

Wrong answers:

* /user-photos
* /get-user-photos
* /get/users/photos

Because user data is already available at /users, best practice is to add another hierarchical group for resources that belong to users.

The other options are incorrect because of the following:

* The endpoint /user-photos creates a separate endpoint from /users and does not group resources logically and hierarchically.
* The endpoint /get-user-photos uses a verb, which is not recommended. Only nouns should be used to identify endpoints.
* The endpoint /get/users/photos also uses a verb. HTTP methods already provide the verb that indicates the action being performed by the client request.

#### A developer is building a REST API. What are common HTTP methods that they should implement with idempotency? (Select THREE.)

* GET
* DELETE
* PUT

Wrong answers:

* PATCH
* POST
* TRACE

An HTTP request is idempotent if repeated calls with the same parameters always have the same result. Identical inputs to GET, PUT, and DELETE should result in the same end state for the system. If these methods are not implemented idempotently, this can cause unintended side effects or cause users to lose trust in this service.

The other options are incorrect because of the following:

* POST is not typically implemented idempotently. Multiple POST requests with the same data can result in different outcomes or cause multiple resources with the same data to be created.
* PATCH is also not inherently idempotent because it partially updates a resource. Multiple PATCH requests might have different results, depending on the resource's state.  
* TRACE should be implemented idempotently, but it is not as common an HTTP method as GET, PUT, and DELETE.

#### How are authentication headers specified in a curl command to a REST API?

* Using the --header option followed by the authentication header key-value pairs 

Wrong answers:

* Using the -u option followed by the authentication credentials
* Using the --anyauth option followed by the authentication method and credentials
* Using the -a option followed by the authentication header key-value pairs

The --header option in curl is used to specify individual header key-value pairs, including the authentication headers.

The other options are incorrect because of the following:

* The -u option in curl is used for basic authentication through a username and password, not for specifying authentication headers.
* The --anyauth option in curl is used for testing if authentication is required in a request, not for specifying authentication headers.
* The -a option in curl is used for appending to a target file when uploading.

### Summary

* An API is a collection of rules or protocols that enables applications to exchange data or functionality with each other. In a client-server model, the API defines how the client application makes a request to the server application and what the server application returns to the client application.
* APIs can use different types of protocols, styles, and standards. Common API types include REST APIs, SOAP APIs, and WebSocket APIs. You can use the curl tool to test APIs from a command line terminal.
* A REST API, also called a RESTful API, conforms to the design principles of the Representational State Transfer architecture. The REST architectural style emphasizes stateless communication and interaction with resources using standard HTTP methods. RESTful APIs are lightweight and scalable, and they decouple the client application from the server application.
* In a RESTful API, the HTTP GET method is used to retrieve a resource, and the POST method is used to create a resource. The PUT method is used to update a resource, and the DELETE method is used to delete a resource.
* When designing a RESTful API, keep it straightforward and choose the right HTTP method. You should also return the correct status code, handle errors properly, and describe errors accurately. Finally, you should always document your API clearly and completely.

### [Lab: Forecasting the Weather with an API](./W11Lab1ForecastingWeather.md)
