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

