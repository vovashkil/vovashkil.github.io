# Week 2: Organizing and Styling HTML Pages

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to repo's main [README.md](../../../README.md)

## Organizing and Styling HTML Pages

### Pre-assessment

#### What type of element is the <span> tag?

* Inline

Wrong answers:

* Internal
* External
* Outline

tThe <span> tag is only referenced as an inline element based on its use and behavior within HTML code.

#### What are the main benefits of organizing your HTML elements? (Select TWO.)

* Proper structure makes webpages more convenient to consume for readers
* Organizing makes underlying HTML code more convenient to read and update

Wrong answers:

* Helps build an outline for HTML
* Helps to add formatting and style to the webpage elements
* Provides better graphics integration with organized elements

The other options are incorrect because of the following reasons:

* Helps build an outline for HTML is not a main benefit or ordering HTML elements.
* Using CSS is suggested to add formatting and style to the webpage elements.
* Ordering the HTML elements is not a strategy that provides better graphics integration with organized elements.

#### What is the benefit of using a division <br> tag?

* Creates space in your text using a carriage return

Wrong answers:

* Changes the inline style of an element
* Creates a division around image elements
* Creates a container to group content

When using HTML, the <br> tag creates space in your text using a carriage return, this tag can be used independently and as a nested element.

### Benefits of Organizing HTML Elements

An organized set of HTML tags makes a webpage more convenient to update, navigate, and maintain. Knowing how to structure and organize HTML elements properly is an essential skill. Adding elements in the wrong order can make a webpage difficult to read and navigate. Not having the proper HTML tags can render a webpage into a chunk of unformatted text. Internet users are busy. They want to gather their information as quickly and effortlessly as possible.

#### Webpage structure

Before building a webpage, you need to consider the consumer. The consumer is the internet user who comes to your webpage for a specific reason.

Before building, take some time to determine how best to organize, or structure, your webpage to achieve your goals.

#### Organizational HTML elements

In addition to the basic HTML elements used to build a webpage, dozens of tags exist specifically for organizing and structuring content. Organizing your webpage involves placing these HTML tags in a specific order to achieve a user friendly, intuitive reading experience. Ordering your HTML elements serves three main purposes:

* Proper structure makes your webpage easier to consume for your readers.
* It makes your underlying HTML code easier to read and update.
* It provides better accessibility and streamlines the experience for screen-reader users.

Structuring your HTML elements in a consistent, logical order helps your readers consume your content. Properly structured HTML documents make your code effortless to read, helping your developers quickly update, modify, and troubleshoot your HTML pages.

### Using Line Breaks and Horizontal Rule

#### Formatting your page

The primary objective when building any webpage is to efficiently communicate your message. A brief glance at your webpage should give the consumer enough information to determine the content of the page.

One of the most strategic ways to do this is through the use of white space. White space is the area of the page that has no written words or images. Effective use of the unformatted space makes the page quicker to visually navigate.

#### Using line breaks <br>

The line break <br> element creates space in your text using a carriage return. You can add additional lines or format the space in your HTML document.

The <br> is an inline element and can be added directly to your text whenever you need a line break. Because the <br> tag isn't specifying a value, there is no end tag </> required. However, <br> and <br/> are equivalent. Any text that comes after a <br> tag appears on the next line in your output.

```
  <h3>Enter your home address below:</h3>
  <p>John Doe <br> 100 Main Street <br> Anytown <br> USA</p>
```

#### Horizontal rule <hr>

The horizontal rule element <hr> tag is used when there is a shift in the topic or theme on your webpage. This element adds visual separation, usually in the form of a horizontal line across the page.

The difference between the <hr /> and the <br /> tags is that <hr> provides breaks in the text with the horizontal rule line. The <br> can also provide breaks in the text by theme or topic, but without the horizontal rule line.

When you use the horizontal rule, you have the option to change the line size, color and formatting.

### Creating Lists

#### Ordered Lists

An ordered list is a series of steps that should be followed sequentially. Each item in the list is preceded by either a number or a letter.

##### This is an ordered list

1. First
2. Second
3. Third
4. Fourth

##### This is also an ordered list

A. Lift the cage door handle.
B. Slide the handle to the right to unlock.
C. Lower the cage door to open.
D. Lift door to close and slide handle left to lock.

#### Unordered lists

An unordered list is a group of related items written in no particular order. The following is a list of animals that you might see on the Pet Club webpage.

##### Pets in our Pet Club include the following

* Dogs
* Lizards
* Hamsters
* Cats
* Horses

#### HTML list elements

Both the ordered and unordered list elements start and end with a tag that identifies whether you are working with an ordered list <ol> </ol> or an unordered list <ul> </ul>.

Then, each item within the list is identified by a list item <li> </li> tag. The <li> tag is used for both the ordered and unordered list items.

```
<p> Complete these tasks before launching your first Amazon EC2 instance.</p>
<ol>
  <li>Sign up for an account</li>
  <li>Create an administrative user</li>
  <li>Create a key pair</li>
  <li>Create a security group</li>
</ol>

<p> Additional Amazon EC2 topics:</p>
<ul>
    <li>Using Systems Manager</li>
    <li>Patches and updates</li>
    <li>Parameter Store</li>
    <li>Building Amazon Machine Images</li>
  </ul>
```

### Spacing and Formatting Text

#### Block elements

Block elements take up the full width of your page from left to right, and can extend from top to bottom. This gives them both a height and width value by default. A block element starts on a new line and has space automatically added after it.

```
<h1>This is the h1 header and page title.</h1>
<p>This is text in a paragraph. Space is added before and after both of these block elements.</p>
```

In the following code example. a <style> element is added to draw a border around the default space allocated to both the <h1> and the <p> values.

```
<style>
h1 {
  border: 5px solid purple;
}
p {
  border: 3px solid orangered;
}
</style>
<body>
    <h1>This is the h1 header and page title.</h1>
    <p>This is text in a paragraph. Space is added before and after both of these block elements.</p>
```

#### Inline elements

With an inline element, the tag is added within the context of the code. It does not start on a new line. It is not given a default height or width value. An inline element only uses as much width as it needs.

An inline element is used to add context, emphasis, or other formatting values. For example, you might be writing a paragraph of text, but want to emphasize or bring attention to a word. In a text editor, your might use the bold or italics options. In HTML, you would use an inline element surrounding the word you want to emphasize or italicize. 

In HTML 5, the <strong> element is used to make a word or phrase bold. It uses both a beginning and end tag: <strong> text content goes here </strong>.

When you need to to draw attention to a word, as in the use of italics, use the emphasis <em> element. The emphasis element also uses both a beginning and end tag: <em> content goes here </em>.

```
<p><strong>Hamlet</strong> is my favorite play.</p>

<p>I am so <em>excited</em> for re:Invent!</p>

<p>I just <strong><em>LOVE</em></strong> puppies! </p>
```

### Building With Tables

#### Table definition

Tables are a set of data comprised of columns and rows. They are built using a horizontally and vertically aligned grid of cells. By using tables, you can conveniently organize related pieces of information.

* **Header rows**. The table header is the row at the top of the table that identifies the title of the table or the data contained within the table. Here, the header row identifies that this is an employee list.
* **Columns**. Columns run from top to bottom, like the columns of a building.  The columns contain vertically defined lists of data within the table. The columns in this example identify an employee's first name, last name, and building number.
* **Table rows**. The rows are the data cells that run horizontally from left to right.

#### HTML table tags

Tables are built using a series of tags. These tags identify the table, the header row, individual rows, and individual cells. Review each of the following tags and their descriptions.

##### HTML Table Elements

| HTML tag | Definition |
| -------- | ---------- |
| <table> | Begins a table in the HTML document |
| <th> | Identifies the table header row, which appears at the top of a table |
| <tr> | Establishes a row in a table |
| <td> | Identifies an individual cell or piece of data |

#### Table example

```
<!DOCTYPE html>
<html>
<head>
<style>
table, td {
  border: 2px solid blue
}
</style>
</head>
<body>
    <table>
        <tr>
          <th>List of Most Popular Pets</th>
        </tr>
        <tr>
          <th>Country</th>
          <th>Animal</th>
        </tr>
        <tr>
          <td>USA </td>
          <td>dog</td>
        </tr>
        <tr>
          <td>China</td>
          <td>cat</td>
        </tr>
        <tr>
          <td>Brazil</td>
          <td>dog</td>
        </tr>
          <td>Australia</td>
          <td>dog</td>
        </tr>
        </tr>
          <td>Canada</td>
          <td>cat</td>
        </tr>
    </table>
</body>
</html>
```

### Organizing With Divisions

#### Content division

The content division, or <div> element, is a generic container element to group content in the HTML document. The <div> tag doesn't modify the HTML content in any way; it just groups content within the HMTL document. By grouping content, you can add formatting and styling after the HTML content is built. Later in the course, you learn how to build separate documents for content and formatting using Cascading Style Sheets (CSS).

The <div> tag is a block element. If you add the <div> tag within your code, the output starts on its own line. It also has a default height and uses the whole width of your page. You can format this to be larger, smaller, or aligned on the page.

### [Lab: Organizing Elements in a Webpage](./labs/W020Lab1OrganizingWebpage.md)

### Knowledge Check

#### Which of the following is TRUE about inline elements? (Select TWO.)

* They do not start a new line.
* They take up only the width required.

Wrong answers:

* They are defined in a new table.
* They take the entire width of the page.
* They are preceded by a line break.

##### Explanation

With an inline element, the tag is added within the context of the code. It does not start on a new line. It is not given a default height or width value. An inline element only uses as much width as it needs.

The other options are incorrect because of the following reasons:

* Inline elements can interact with tables but are not always defined in a new table when used.
* Inline elements will not take the entire width of the page because they only use as much width as needed with no default height and width.
* Inline elements are not elements that are preceded by a line break.

### Summary

* Identify HTML elements used for web content organization.
* Apply best practice for ordering and organizing HTML elements.

The organizing and styling section covered topics related to the best practices for organizing your webpages so that they are convenient to read and navigate. With the concept of whitespace collapse, HTML automatically ignores space in your HTML document and collapses it when displaying the page. To add additional space on a page, you can add breaks or horizontal rules. You learned how to use these line breaks to add white space or carriage returns. Horizontal rules were discussed as a way to visually separate thematically different topics or sections on a page.

You learned that block elements and inline elements have different spacing and formatting sizes. Block elements start their content on a new line and inline elements sit within the flow of content and do not require additional whitespace. You learned how to create ordered and unordered lists, tables and divisions on a webpage.

## Cascading Style Sheets (CSS)

### Pre-assessment

#### How are Cascading Style Sheets (CSS) organized?

* Into a series of rulesets

Wrong answers:

* Alphabetically by element
* Ordered by priority value
* Enumerated by first in first out (FIFO)

##### Explanation

CSS is a language, it has specific rulesets for proper functionality.

* CSS does not have a structure that is listed alphabetically by element.
* Due to the nature of CSS elements, there is no need to have your elements ordered by priority value unless based off preference.
* CSS is not a language that is enumerated by first in first out (FIFO).

#### What is the purpose of CSS?

* Adds formatting and style to the webpage elements

Wrong answers:

* Helps build an outline for HTML
* Creates links to other webpages within the markup language
* Creates tables and elements to organize the webpage

##### Explanation

When creating webpages, it is suggested to create a separate Cascading Style Sheets (CSS) file to manage the web elements formatting and style.

The other options are incorrect because of the following reasons:

* The purpose of CSS is not to help build an outline for HTML.
* The purpose of CSS is not to create links to other webpages within the markup language.
* The purpose of CSS is not to create tables and elements to organize the webpage.

#### What is the benefit of using a division <div> tag?

* Creates a container to group content

Wrong answers:

* Changes the inline style of an element
* Divides the webpage into columns
* Creates a division around image elements

##### Explanation

The <div> tag creates a container to group similar or related content. The container can have style elements assigned to it, allowing for changes to background color, border, or font.

The other options are incorrect because of the following reasons:

* The <span> element can help make changes to the inline style of an element when used in conjunction with CSS.
* The <div> element can used in conjunction with other HTML elements and CSS elements in order to divide the webpage into columns.
* To create a division around image elements the <div> tag would need additional CSS formatting and styling.

### Cascading Style Sheets

You have learned that, by using HTML, you can build the text content of a webpage. Because it is a markup language used to work with text, it isn't designed to add specialized fonts or background colors. To make HTML visually appealing, you need to use a style sheet. A style sheet defines how the webpage looks. The style sheet identifies font type and colors, borders, backgrounds, and more. The style sheet for HTML is called Cascading Style Sheets (CSS). This section explains what CCS is and how to use it to build a beautiful webpage.

#### Define cascading

Cascading style sheets use the term cascading because the styles in the document are listed in priority rule order. This helps determine which style rule to apply if a rule happens to match more than one style listed.

```
font-family: 'Lucida Grande', 'Lucida Sans Unicode', 'sans-serif';
```

With the example above, if the browser doesn't have the first font installed and can't match that rule, it will cascade to the next font in the list, and continue down the list. To visualize this, imagine a cascading waterfall where the water starts at the top and flows downward. With CSS, the priority moves from the top, down the list, and down through the document. The font choice cascades down to the child elements that sit within the body of the document.

#### Before CSS

Before the release of CSS, any formatting for HTML elements was done using inline tags within the HTML code. For example, the font, color, width, and other formatting tags would be on the same line with HTML code. This made it challenging to decipher the HTML or to make small updates to the content. Updating the content often required you to fix the formatting after you fixed the content. Having the formatting tags and HTML tags in one document made even a small webpage difficult to build and maintain.

#### Styling using internal stylesheet

The following images show the Pet Club webpage with a minimal set of style tags.

```
<head>
	<meta charset="UTF-8">
	<title>Example Pet Club</title>
	
	<style>
	/* CSS inline styles for the webpage */
		
		.bodyStyle {
						width: 960px;
						margin: 0 auto;
						overflow: auto;
						font-family: 'Lucida Grande', 'Lucida Sans Unicode', 'sans-serif';
						font-size: 15px;
		}
				
		.mainHeader {
  						font-family: "Comic Sans MS", cursive;
						font-size: 60px;
						line-height: 66px;
						color: #000;
						text-align: center;
		}
		
		.center {
  					text-align: center;
 		}
		
		.topnav {
  					background-color: green;
  					height: 31px;
  					text-align: center;
		}
		
		.topnav a {
  					color: white;
  					text-align: center;
  					vertical-align:middle;
  					font-size: 20px;
  					padding: 0 16px;
  					text-decoration: none;
		}
	</style>
</head>

<body class="bodyStyle">
	<div id="header" class="mainHeader">
		<hr>
		<div class="center">Example Pet Club</div>
	</div>
	<br>
	<hr>
	<div class="topnav">
		<a href="homePage.html">Home</a>
		<a href="#aboutUs">About Us</a>
		<a href="register.html">Join Us</a>
		<a href="#contactUs">Contact Us</a>
		<a href="members.html">Members</a>
	</div>
	<hr>
</body>
```

When an internal stylesheet is added to the HTML document, the HTML document can become too difficult to update and maintain. This is one of the main reasons that styling was decoupled from the HTML document and a new, separate stylesheet standard was implemented.

An external stylesheet makes styling and maintaining your webpage more convenient by separating the HTML document from the formatting document. You can have one stylesheet or as many as you need to accommodate your needs.

### Writing CSS Syntax

#### Forming CSS rules

CSS is organized into a series of rulesets. These rulesets, or rules, have two pieces: the selector and the declaration:

* **Selector**:  Identifies which HTML elements to format
* **Declaration**: Determines how to format the element

The following table provides examples of a basic rule. The first column indicates the selector, or the HTML element you want to modify. The second column holds the declaration. The declaration is contained within curly braces { } and identifies a property and a property value, followed by a semicolon.

The second row contains the paragraph tag p as the selector. In this example, the declaration indicates to change the value of the color property to **purple**. The next example has the header **h1** as the selector. The declaration indicates to change the value of the color property to **red**. There's an additional declaration in this example, which is setting the property of *text-align* to the *property value* of **center**.

| Selector | Declaration |
| -------- | ----------- |
| selector | {property : property value;} |
| p | {color : purple;} |
| h1 | {color : red; text-align: center;} |

### Inline, internal, and external style

CSS is added to your HTML document in one of three ways:

* Inline
* Internal
* External

#### Inline

Inline CSS defines the style for one individual HTML element inside of your HTML document. For example, if you want your <h1> header to be green, you add a <style> element inline with your HTML code.  

```
<h1 style="color:green;">All About Rabbit Breeds</h1>
```

The inline style works well for one or two elements on a small webpage. Using this style too frequently might make your HTML document too long and complex. It is difficult to maintain and negates the purpose of having a separate style sheet. 

#### Internal

Internal CSS is for formatting one HTML document. It is specified within the top <head> section of your HTML page using the same <style> element. For example, what if you want your <h1> header to be green, and the background of your page to be light yellow? You could add the <style> element into the <head> section of your HTML document.

```
<!DOCTYPE html>
<html>
<head>
<style>
    h1   {color: green;}
    p    {color: darkblue;}
    body {background-color: lightyellow}
</style>
</head>

<body>
  <h1>All About Rabbit Breeds</h1>
    <p>There are numerous rabbit breeds in the world. Scroll down to read more!</p>
</body>
</html>
```

#### External

External CSS is what's used on most modern webpages. With external CSS, you build a separate style sheet document that contains all of the formatting elements. This document ends with a .css extension, such as style.css. You then reference this style.css document in the <head> section of your webpage.

After you build a CSS file, you can use that external CSS document and apply it to any new website that you build. External CSS is more flexible, so you can completely decouple the HTML content from the CSS formatting elements. This makes your HTML code more convenient to maintain and update.

```
<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="style.css">
</head>
<body>

  <h1>All About Rabbit Breeds</h1>
  <p>There are numerous rabbit breeds in the world. <br> Scroll down to read more!</p>

</body>
</html>
```

The following CSS code shows the contents of the external style.css file referenced by the HTML document.

```
body {
    background-color: lightblue;
}
h1 {
    color: darkmagenta;
}
p {
    color: blue;
}
```

### Formatting Attributes

#### Building with the <div> element

The division element groups your content. If you remember from the previous section, the <div> tag doesn't impact your content until you add formatting to it. To use the <div> tag to group content, place your text within the <div> and </div> tags.

```
<body>
      
      <div>
        <h2>Dogs</h2>
        <p>Dogs are the most popular pet in the United Kingdom (UK).</p>
        <p>The Labrador retriever is the most popular breed.</p>
      </div>        
    
</body>
```

### HTML global attributes

An attribute is a piece of additional information that determines the characteristics of a displayed element. There are many attributes that are used with specific HTML elements, but global attributes are used with all HTML elements to help identify the style, features, and formatting of your HTML content.

Two main global attributes for CSS:

* the class
* and the id attribute.

#### Using the class attribute

The class attribute is used to apply specific styling and formatting to a group of HTML elements. To do this, you assign a class selector to an element using the class HTML global attribute. You use this selector to select or choose the HTML elements that you want to format.

You then define the class selector properties either within the <head> section of the HTML document, or in a separate style sheet document.

##### Class selector properties

* Classes are case-sensitive
* They begin with a dot (.)
* Formatting applies to all of the elements that match the class being specified

Locate/create a css folder and create a pets.css file inside of it. Use this pets.css for any of the CSS or style examples. The HTML document points to this file and location: <link rel="stylesheet" href="css/pets.css">.

```
.pets {
    font-style: italic;
    font-weight: bold;
  }
  
.color {
    background: orange;
    padding: 10px;
  }
```

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="css/pets.css">
</head>


<body>
     <div class="pets">
        
      <div>
        <h2>Dogs</h2>
        <p class="color"> Dogs are the most popular pet in the United Kingdom (UK).</p>
        <p class="color"> The Labrador retriever is the most popular breed.</p>
      </div>
      
      <div>
        <h2>Cats</h2>
        <p>Cats are the second most popular pet in the UK.</p>
        <p>The British Shorthair is the most popular cat breed.</p>
      </div>
      
      <div style="background-color:lightskyblue;">
        <h2>Lizards</h2>
        <p>Lizards are third in popularity in the UK.</p>
        <p>Bearded dragons are one of the top lizards in captivity in the UK.</p>
      </div>
    
    </div>
    
</body>
</html>
```

#### The id element

The **id** element is used to change the formatting for one single HTML element. The **id** element is distinctive within the doc, and it only appears once to style one element. The **id** element begins with the **#** (hash) symbol and then the name of the **id** element.

The **id** element is also used to reference other elements in client-side JavaScript.

In the following example, the **id** element is **#banner** and changes the formatting style for one unique HTML element.

```
<!DOCTYPE html>
<html>
<head>
<style>
#banner {
  background-color: lightyellow;
  color: purple;
  padding: 20px;
  text-align: center;
} 
</style>
</head>
<body>

<h2> Don't forget hamsters...</h2>
<p>Hamsters exercise on their own, love to play, and are low maintenance.</p>

<h1 id="banner">Hamsters are great pets too!</h1>

</body>
</html>
```

#### Which attribute to choose

Both the class and id attributes are used to style HTML elements, so it's important to know the differences. When styling your document, remember the following differences:

* Use the **class** attribute when you want to style multiple HTML elements the same way.
* Use the **id** attribute when you only want to style one element separately.

Global elements are useful tools for formatting and increasing the accessibility of your webpage. There is another tag that is used in nearly all of the modern webpages, the <span> tag.

### Applying Spans

#### HTML <span> tag

The <span> tag is an inline element used to highlight or bring attention to an area of text.

Remember, inline elements are written within the HTML content and they only take up as much width as they require. They do not start the content on a new line like a block element does. Like many other HTML elements, the <span> tag needs a start and end tag: <span> and </span>.

Here is an example of a <span> tag:

```
<!DOCTYPE html>
<html>
<body>

<h1>Bearded Dragons As Pets</h1>

<p>The <span style="color:darkgoldenrod;">bearded dragon's</span> scientific name is <span style="color:rgb(255, 0, 149);font-weight:bold">Pogona Vitticeps</span>.</p>
<p>The average size of a bearded dragon is <span style="color:darkblue;font-weight:bold">12-24 inches</span> from their nose to the tip of their tails.</p>

</body>
</html>
```

### [Lab: Using CSS to Define Webpage Styles](./labs/W020Lab2UsingCSSForStyling.md)

### Knowledge Check

#### Which option best describes the use of the <span> element?

* Highlights or brings attention to an area of text

Wrong answers:

* Alters the alignment and spacing of groups
* Groups lines of text together
* Links the content to other documents

##### Explanation

The <span> tag is an inline element used to highlight or bring attention to an area of text.

The other options are incorrect because they all explain the possible behaviors of functions that do not pertain to the <span> element and its behavior. The other options are covering Grid Systems, HREF elements, and additional formatting elements.

#### The class attribute applies style and formatting to a group of HTML elements. What should a developer remember when working with class attributes? (Select TWO.)

* Classes are case-sensitive
* They begin with a dot (.)

Wrong answers:

* Formatting applies to all elements in the document
* They begin with a # (hash) symbol
* Classes need a corresponding id element

#### What are the benefits of using Cascading Style Sheets? (Select TWO.)

* Style sheets are reusable for multiple webpages.
* Style sheets improve readability of HTML code by removing style elements.

Wrong answers:

* Formatting is added to HTML only through external style sheets.
* Style sheets improve webpage loading times.
* Style sheets are the way to add images to HTML.

### Summary

* Describe the benefits of using CSS.
* Identify how to use HTML and CSS elements to style a webpage.

To make HTML visually appealing, you need to use a style sheet. A style sheet defines how the webpage looks. The style sheet identifies font type and colors, borders, backgrounds, and more. The style sheet for HTML is called Cascading Style Sheets (CSS). 

CSS makes styling and maintaining your webpage more convenient by separating the HTML document from the formatting document. You can have one style sheet or as many as you need to accommodate your needs.

CSS is organized into a series of rulesets. These rulesets, or rules, have two parts:

* **Selector**: Identifies which HTML elements to format
* **Declaration**: Determines how to format the element

CSS is added to your HTML document in the following ways:

* **Inline**: defines the style for one individual HTML element inside of your HTML document
* **Internal**: defines  formatting for one HTML document
* **External**: defines formatting in a separate style sheet document that can be applied to more than one webpage

In this section, you also learned how to use class and id elements to format multiple or single elements in your document. You also learned how to use the <div> and <span> tags to style your webpage content.
