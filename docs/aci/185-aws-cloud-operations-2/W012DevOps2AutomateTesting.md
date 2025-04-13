# Week 1: DevOps 2: Automate Testing with Continuous Integration

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to [AWS Cloud Operations 2](./aws-cloud-operations-2.md)
* back to repo's main [README.md](../../../README.md)

## DevOps2: Automate Testing with Continuous Integration

### Pre-assessment

#### Which method involves moving testing earlier in the software development lifecycle to catch bugs and issues as early as possible?

* Shift-left approach

Wrong answers:

* Unit testing
* Functional testing
* Trunk-based development

##### Explanation

The shift-left approach is a software testing approach where testing activities are moved earlier in the software development lifecycle (SDLC). The goal is to catch bugs and issues as early as possible, instead of waiting until the later stages of development.

The other options are incorrect because of the following reasons:

* Unit testing involves testing individual units of code.
* Functional testing involves verifying the software system's behavior.
* Trunk-based development involves committing changes to the main branch of a version control system.

#### Which tool is an AWS service that developers can use  to run tests?

* CodeBuild

Wrong answers:

* GitHub
* unittest
* pytest

##### Explanation

AWS CodeBuild is a fully managed continuous integration service that compiles source code, runs tests, and produces software packages that are ready to deploy.

The other options are incorrect because of the following reasons:

* GitHub is a platform for hosting code in Git repositories.
* unittest is a Python testing framework for unit testing.
* pytest is a Python testing framework used to write various types of tests.

#### What is a key benefit of automated unit testing for development teams?

* Provides more time for coding and development

Wrong answers:

* Increases the time spent on manual testing
* Reduces the need for code documentation
* Eliminates the need for integration testing

##### Explanation

With automated unit testing, developers can quickly verify that small sections of code are functioning as intended. By automating these tests, developers don't have to manually test each part of the code every time they make a change. This saves a significant amount of time compared to manual testing. With this time savings, developers can spend more time focused on writing new code instead of repeatedly testing the same code sections.

The other options are incorrect because of the following reasons:

* Automated unit testing reduces the time spent on manual testing.
* Although automated tests can serve as a form of documentation by demonstrating how code should behave, they do not replace the need for proper code documentation.
* Automated unit testing does not eliminate the need for integration testing. Unit testing and integration testing serve different purposes and complement each other.

## Testing Code Changes

### Some key principles and practices for testing code changes in DevOps

1. **Shift-Left Testing**: The idea of "shifting left" refers to moving testing earlier in the development lifecycle, instead of waiting until the end. With this, issues can be identified and addressed much sooner, reducing rework and technical debt.
2. **Automated Testing**: Relying on manual testing is inefficient and error-prone, especially as the codebase and development velocity increases. Automating as many tests as possible, from unit tests to acceptance tests, is crucial for DevOps.
3. **Continuous Integration/Continuous Deployment (CI/CD)**: A well-implemented CI/CD pipeline is the backbone of effective testing in DevOps. Each code commit should initiate an automated build, test, and deployment process so that defects can be caught early.
4. **Cross-Functional Collaboration**: Testing in DevOps is not only the responsibility of the QA team. It requires close collaboration between developers, ops engineers, and other stakeholders. Developers should be writing testable code and participating in testing activities.
5. **Continuous Improvement**: Testing processes and strategies should be regularly evaluated and refined. Analyzing test results, monitoring production incidents, and soliciting feedback can help identify areas for improvement and optimization.

## Unit Testing in CI/CD

### What is Unit Testing?

Unit testing is a method of testing individual parts, or units, of software code to ensure they work correctly in isolation. Each unit is tested independently, typically with automated tests, to verify its behavior against expected outcomes. Unit tests focus on small, specific functionalities or components of the code, making it effortless to identify and fix bugs early in the development process. This helps improve code quality, reduces the risk of regressions, and enhances overall software reliability.

### Benefits of unit testing in CI/CD

Unit testing in DevOps is continuous, comprehensive, and collaborative, and provides fast feedback to support continuous delivery of software. It facilitates reliable, rapid releases while giving developers confidence that changes will not introduce regressions.

Unit tests can be automated to run on every code change as part of the CI/CD pipeline. They make up part of the test suite alongside integration testing.

Suppose a developer is working on an e-commerce website for a clothing retailer. Their task is to implement a new feature that customers can use to filter products by size and color. Before writing any code for the feature, the developer creates a unit test suite. They write individual unit tests to verify various aspects of the filtering functionality, such as:

* Testing that the correct products are returned when filtering by size
* Testing that the correct products are returned when filtering by color
* Testing that the filtering options are displayed correctly on the user interface
* Testing that the filtering functionality gracefully handles edge cases, such as when no products match the selected criteria

After the unit tests are in place, the developer begins implementing the filtering feature. After writing each piece of code, they run the corresponding unit tests to ensure that the code behaves as expected and that any changes do not break existing functionality. Through this process of writing and running unit tests, the developer can catch bugs early, ensure the filtering feature works as intended, and maintain confidence in the reliability of the e-commerce website.

### Unit Testing Strategies

#### Logic Checks

Does the system perform the right calculations and follow the right path through the code, given a correct, expected input? Are all paths through the code covered by the given inputs?

For instance, in an e-commerce application, a logic check could ensure that a discount is applied correctly based on specific conditions, such as minimum order value or customer loyalty status.

#### Boundary Checks

For the given inputs, how does the system respond? How does it respond to typical inputs, edge cases, or inputs that are not valid?

For example, in a banking application, boundary checks could ensure that account balances are correctly updated when processing transactions near the minimum or maximum allowable amounts, preventing potential errors or system failures.

#### Error Handling

When there are errors in inputs, how does the system respond? Is the user prompted for another input? Does the software crash?

For instance, in a messaging application, error handling unit tests might simulate scenarios such as network timeouts or invalid user inputs to ensure that the application gracefully handles these situations without crashing or losing data.

#### Object oriented checks

If the state of any persistent objects is changed by running the code, is the object updated correctly?

Think about a music streaming app like Spotify. In this app, you have different objects like the user profile, the song library, and the player controls. Object-oriented testing would involve making sure these objects work together seamlessly. For instance, you'd want to test that when a user selects a song from their library, it plays correctly in the player and updates the user's listening history. This ensures that the app provides a smooth and enjoyable experience for users, without any unexpected hiccups in their music playback.

### Benefits of Automating Testing Code Changes

Automation testing is a method designed to automate repetitive but necessary tasks within a formalized testing process or to perform additional testing that would be difficult to run manually. The adoption of automation testing has been crucial for software development teams who are now able to integrate testing into the early stages of the development process.

There are many benefits of automated testing code changes:

#### Efficiency

Automated testing reduces manual effort and time spent on writing and running tests for each code change. This is because the testing process is automated, meaning it can be effortlessly and efficiently carried out several times with only one command, in contrast to manual testing, which is highly time-consuming and manual-intensive.

Imagine writing a test case in Python, and then using a tool like pytest to run that test case. You can run this test multiple times and from the command line, making the whole process highly efficient and increasing your team's velocity along with reducing human errors.

#### Repeatability

Automated tests can be executed repeatedly, ensuring that the code behaves the same way each time it is run. This is crucial for identifying and fixing regressions, which are unintended changes that cause existing features to stop working.

Imagine writing a test that checks if a user can successfully log in to a web app. If this is the case, and this test cannot run successfully with or without code changes, then this would mean that there is a regressive change or bug in the code, which needs fixing.  

#### Early Bug Detection

Automated tests run quickly and give you faster feedback, this early feedback is crucial in the development process, as it allows bugs to be fixed early, thereby reducing the cost and effort of debugging late in the development cycle.

During tests, an error might arise saying that a certain form field is not being displayed or is missing its data, this appears immediately when the code is executed, allowing the development team to easily identify where the error is and fix it immediately rather than waiting until the end of the project development cycle.

#### Improved Code Quality

Automated tests help to ensure that code is written in a way that is both reliable and maintainable. The addition of automated tests can really help improve your code and make it understandable to your peers and future selves.  

The use of new technologies and the concept of serverless will greatly benefit from automated tests, as they provide instantaneous feedback if any part of your application's functionality is negatively impacted by code changes.

### Testing Implementation Example

1. E-commerce Website Testing
        Imagine you're an online retailer like Amazon, with millions of products listed on your website. Every time a new feature or update is introduced, it's essential to ensure that the website functions correctly across various browsers, devices, and user scenarios. Manual testing would be incredibly time-consuming and prone to human error. With automation testing, you can create scripts that simulate user actions, such as adding items to the cart, checking out, and verifying order details. These scripts can be run repeatedly, ensuring that the website works seamlessly for customers, regardless of the changes made.
2. Mobile App Testing
        With the proliferation of mobile devices and operating systems, testing mobile applications manually can be a daunting task. Automation testing comes to the rescue because developers can create test scripts that run on different devices and emulators, simulating various user interactions and scenarios. For instance, an automation testing suite for a popular messaging app like Chime could include tests for sending messages, making video calls, sharing media files, and verifying notifications across multiple devices and OS versions.
3. Enterprise Resource Planning (ERP) System Testing
        ERP systems are complex software solutions that integrate various business processes, such as finance, supply chain, human resources, and customer relationship management. Testing these systems manually is incredibly time-consuming and error-prone due to the sheer number of scenarios and data combinations involved. Automation testing can help by creating scripts that can test various business workflows, data validations, and integrations between different modules. For example, an automation testing suite for an ERP system could include tests for creating purchase orders, generating invoices, tracking inventory levels, and verifying payroll calculations.
4. Web Service and API Testing
        In today's interconnected world, many applications rely on web services and APIs to exchange data and functionality with other systems. Testing these interfaces manually can be tedious and inefficient, especially when dealing with large volumes of data or complex request/response scenarios. With automation testing, developers can create scripts that can send various requests to web services or APIs, verify the responses, and validate the data integrity. For instance, an automation testing suite for a weather API could include tests for retrieving forecast data for different locations, validating the response format, and verifying the accuracy of the weather predictions.

Automated tests make maintaining and updating code effortless over time. Changing and extending well-tested code is more straightforward and safer. In summary, automated testing of code changes is beneficial due to its increased efficiency, repeatability, early bug detection, and improved code quality, thereby decreasing costs and development time and cycle.

### Code Coverage and its Purpose for Code Testing
