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

#### What is Code Coverage?

Code coverage measures how many lines, statements, or blocks of your code have been tested using automated tests. This metric helps you understand the quality of your QA efforts. Code coverage shows how much of your application is vulnerable to defects and is measured in percentage.

In software development, code coverage is important because it helps quantify the extent to which automated tests exercise the codebase. By measuring code coverage, developers gain insights into which parts of the code are tested and which are not. This information guides testing efforts, ensuring comprehensive coverage and reducing the risk of undetected bugs or errors. Ultimately, higher code coverage leads to greater confidence in the reliability and quality of the software product. To measure the lines of code using test runs, there are specific criterion that are important.

#### Function Coverage

Function coverage measures whether each function in the codebase is called and executed during testing. For example, if your application has ten functions, function coverage will check that all ten are invoked at least once in the test suite. High function coverage ensures that every function has been tested, reducing the risk of untested code paths.

#### Statement Coverage

Statement coverage assesses whether each executable statement in the code has been executed during testing. For instance, if your code has 100 lines, statement coverage will determine if all 100 lines are run during the tests. This metric helps ensure that all parts of the code are tested, identifying lines that might be skipped or ignored.

#### Path Coverage

Path coverage measures whether all possible paths through the code have been tested, including all combinations of branches and loops. For example, in a piece of code with an if-else statement, path coverage would check both the if and the else branches, as well as any other possible paths through the code. This thorough approach helps uncover complex bugs that might occur due to specific sequences of execution.

#### Branch or Decision Coverage

Branch coverage evaluates whether each possible branch (true/false) of control structures (like if-else and switch-case) is executed. For instance, in an if statement, branch coverage ensures both the true and false conditions are tested. This criterion helps verify that all logical paths in the code are tested, reducing the risk of untested branches leading to potential errors.

#### Condition Coverage

Condition coverage, also known as predicate coverage, checks whether all individual conditions within a decision have been tested for all possible outcomes. For example, in the condition if (A && B), condition coverage ensures that both A and B are tested for true and false values independently. This ensures that every logical condition is thoroughly tested, providing a finer granularity of test coverage than branch coverage alone.

### Benefits of High Code Coverage

Let's look at a quick example of code coverage. Using an online banking system, users can perform various financial transactions, such as transferring money, checking account balances, and paying bills. Given the critical nature of financial data and transactions, ensuring the reliability and security of this system is paramount.

#### Function Coverage

The banking system includes functions for user authentication, balance checking, and money transfers.

**Importance**: Function coverage ensures that each of these critical functions is tested. For example, if the user authentication function is not tested, users might experience login failures, potentially locking them out of their accounts.

#### Statement Coverage

The balance checking function includes multiple lines of code to fetch and display account details.

**Importance**: Statement coverage ensures that each line of code within this function is run during testing. If certain lines of code are not tested, there could be hidden bugs that cause incorrect balance displays or errors when fetching account details.

#### Path Coverage

The money transfer function includes multiple conditions, such as checking for sufficient funds, verifying recipient details, and confirming the transfer amount.

**Importance**: Path coverage ensures that all possible paths through the money transfer process are tested. This helps identify complex bugs that might occur when certain conditions or sequences of actions are taken, such as transferring money when funds are insufficient.

#### Branch or Decision Coverage

The bill payment function includes several decision points, like selecting the biller, choosing the payment date, and confirming the payment.

**Importance**: Branch coverage ensures that both the true and false branches of these decision points are tested. For instance, if the false branch of a condition checking for valid payment dates is not tested, users might be able to schedule payments on invalid dates, leading to payment failures.

#### Condition Coverage

The user registration function includes conditions for validating user input, such as checking email format and password strength.

**Importance**: Condition coverage ensures that all individual conditions within these validations are tested for both true and false outcomes. This ensures that all edge cases, such as invalid emails or weak passwords, are correctly handled, preventing potential security vulnerabilities.

### Non-AWS Unit Testing Code Tools

DevOps testing tools are a crucial component of the DevOps methodology, specifically designed to improve the speed and reliability of software delivery. These tools automate and streamline the testing process. This makes it effortless for teams to identify and resolve issues and continuously improve the performance of their applications. DevOps testing tools are essential for ensuring the quality and reliability of software deliverables in today's fast-paced, agile development environments.

#### GitHub

GitHub is a web-based platform used for version control and collaboration. With GitHub, developers can host and review code, manage projects, and build software alongside other developers. GitHub makes it effortless to track changes to code over time, so you can see the entire revision history of a project. With social features like discussions, wikis, and feedback tools, GitHub facilitates communication and project management for software teams. Its pull request workflow initiates code review so developers can give suggestions and approve changes before they are merged. GitHub also provides access control and several integration options to connect your external tools and services.

#### Unittest

Unittest is a unit testing framework that comes bundled with Python. It allows you to test pieces of code in isolation to make sure they behave as expected. Unittest provides useful assertion methods to check for equality, truth values, exceptions raised, and more. Tests are organized into test cases containing one or more related tests, and test suites can group together multiple test cases. The unittest module provides test runners to execute tests and report results. Unit testing with Unittest allows you to catch bugs early, before they propagate through the code.

#### Pytest

Pytest is a popular Python testing framework that makes it easy to write and run tests. It has a simple syntax that allows you to write tests quickly. One of the key features of pytest is its powerful fixture system that provides reusable test setup and teardown methods. Pytest discovers and runs test functions automatically without the need to import libraries or create test classes. It supports running tests in parallel to reduce execution time. Pytest has an active community that maintains plugins offering additional useful features like test coverage reporting.

It's important to note that the specific benefits can vary depending on the non-AWS testing code tools you choose and the requirements of your project. Conducting a thorough evaluation of your testing needs and comparing the features and capabilities of different tools can help you make an informed decision on the best fit for your organization. Using non-AWS tools can provide some of the following benefits:

1. Non-AWS testing code tools are often more flexible and portable. This means they can be used across different cloud environments, on-premises infrastructure, or even local development machines. This flexibility can be especially beneficial if you have a multi-cloud or hybrid cloud strategy.
2. Using non-AWS testing code tools can help you maintain vendor neutrality, reducing your dependence on a single cloud provider and giving you more options for your testing infrastructure. This can be important for maintaining control over your testing processes and ensuring long-term flexibility.
3. Non-AWS testing code tools can offer more cost-effective solutions, especially if you have specific requirements or a limited budget. By considering alternative options, you can potentially save on licensing fees, infrastructure costs, or other expenses associated with AWS-specific tools.
4. Certain non-AWS testing code tools can offer specialized features or capabilities that are better suited to your specific testing needs, such as advanced performance testing, specialized scripting languages, or support for specific frameworks or technologies.
5. Non-AWS testing code tools can integrate more seamlessly with a wider range of third-party tools and frameworks, such as continuous integration (CI) platforms, issue tracking systems, or collaboration tools. This can help streamline your overall testing workflow and improve cross-team collaboration.

### Knowledge Check

#### Which testing technique verifies interconnected units?

* Integration testing

Wrong answers:

* Unit testing
* End-to-end testing
* System testing

##### Explanation

Integration testing is a type of software testing that checks how different parts of a system work together. It focuses on verifying that components or modules interact correctly when combined, ensuring that the system functions as expected.

The other options are incorrect because of the following reasons:

* Unit testing focuses on individual units or components.
* End-to-end testing mimics real user experiences.
* System testing focuses on overall system requirements and behaviors.

#### What is the primary benefit of high code coverage?

* Increased confidence in the code base

Wrong answers:

* Improved performance
* Reduced technical debt
* Streamlined code maintenance

##### Explanation

High code coverage means that a larger portion of the code base is being tested. This can lead to increased confidence in the overall quality and reliability of the application.

The other options are incorrect because of the following reasons:

* Code coverage itself does not directly improve application performance. Although writing tests can sometimes lead to performance by identifying inefficiencies, high code coverage alone does not guarantee better performance.
* High code coverage can help reduce technical debt over time by making code easier to maintain and refactor, but this is not the primary benefit. Technical debt can still exist in well-tested code.
* High code coverage can make code maintenance easier by providing a safety net for changes, but this is more of a secondary benefit. Streamlined maintenance comes from the increased confidence and reduced risk of introducing bugs when making changes in a highly tested code base.

#### What is the primary purpose of the unittest module in Python?

* Unit testing

Wrong answers:

* Integration testing
* End-to-end testing
* Performance testing

##### Explanation

The unittest module in Python is primarily used for performing unit tests. It provides a framework for writing and running unit tests, which are designed to test individual units of code in isolation.

The other options are incorrect because of the following reasons:

* Integration testing focuses on testing the interaction between different modules or components of a system, rather than testing individual units of code in isolation.
* End-to-end testing is a type of testing that validates an entire system or application from start to finish, simulating real-world scenarios and user interactions.
* Performance testing is concerned with measuring the speed, response time, stability, and resource usage of a system or application under different workloads and conditions. While performance might be a consideration in unit testing, it is not the primary purpose of the unittest module.

### Summary

#### Testing Code Changes

Testing code changes is crucial to ensure the stability and correctness of software. It involves running a series of tests, both automated and manual, to verify that the new code works as expected and doesn't introduce any unintended issues. Thorough testing can:

1. Detect bugs early in the development process
2. Give developers confidence that changes work as intended before deploying to production
3. Improve your team's efficiency and productivity

#### Unit Testing in CI/CD

Unit testing is a crucial component of a robust CI/CD pipeline. It involves writing and running automated tests that verify the correctness of individual units of code, typically at the function or module level. Integrating unit tests into the CI/CD workflow ensures that new code changes do not break existing functionality, and helps catch issues early in the development process. Successful performance of unit tests is often a gating requirement before code can be deployed to production environments as part of the continuous delivery process.

Practices and benefits of unit testing include:

1. Ensures individual components work as expected which makes the network stronger, like a Lego brick.
2. If implemented thoroughly and intentionally, unit testing reduces future bugs and their associated costs in terms of time and resources.
3. Collaboration between developers can be enhanced due to clear pre-defined expectations from the code, and reduce Developer Stress!
4. You can achieve faster feedback loops with end-users, and quickly fix whatever takes first-class citizen status in your system by your team.

#### Benefits of Automated Testing Code Changes

Automated testing of code changes offers several benefits, which can significantly improve the software development and maintenance process. Here are the key benefits:

* **Efficiency**: Automated tests can consistently and thoroughly verify the behavior of the software, ensuring that new changes do not break existing functionality.
* **Repeatability**: Automated tests can be run repeatedly, ensuring that the code behaves the same way each time it is run.
* **Early Bug Detection**: Rigorous automated testing during development means fewer bugs make it past development into production.
* **Improved Code Quality**: Automated testing encourages developers to write more modular, testable code, which often leads to improved code design and better software architecture.

#### Code Coverage and its Purpose for Code Testing

The purpose of code coverage is to provide developers with a clear understanding of how much of their code is being tested. Developers can then identify areas that might need more attention. By increasing code coverage, they can improve the quality and reliability of their software, reducing the likelihood of bugs and errors. Ultimately, code coverage is a valuable tool that helps developers deliver high-quality software that meets the needs of their users.

To calculate code coverage, tools are used to track which parts of the codebase are carried out when running tests and generating a report. Many types of coverage are produced by a variety of tools, such as:

1. **Branch coverage**: Tests all code paths of the program.
2. **Statement coverage**: Requires that each code statement is run through the program at a minimum.

#### Non-AWS Testing Code Tools

Github is an essential web-based collaboration platform for developers that supports them to effortlessly share and modify code. It offers functionalities like version control, code review, documentation, and issue tracking, where team members can work together on projects. By creating pull requests, developers can contribute to projects and have their code reviewed by peers before merging it into the main codebase. Overall, Github is a favored tool for software development teams to facilitate efficient code collaboration, maintain code versions, and manage projects across their organization.

Unittest and Pytest are frameworks for Python that provides a systematic framework for designing and writing test cases. By promoting the philosophy of test-driven development, these frameworks encourage developers to first define the desired behavior of their code and then write tests to confirm whether the code actually meets those expectations. They provide utility functions, fixtures, and assert methods for conveniently creating and running test cases. This facilitates user friendly automation and organization of tests. With concise and readable test code, it becomes more efficient to identify and fix issues, ensuring robust and high-quality code.
