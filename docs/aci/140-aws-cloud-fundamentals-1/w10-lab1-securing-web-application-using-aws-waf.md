Securing a Web Application Using AWS WAF
© 2024 Amazon Web Services, Inc. or its affiliates. All rights reserved. This work may not be reproduced or redistributed, in whole or in part, without prior written permission from Amazon Web Services, Inc. Commercial copying, lending, or selling is prohibited. All trademarks are the property of their owners.

Note: Do not include any personal, identifying, or confidential information into the lab environment. Information entered may be visible to others.

Corrections, feedback, or other questions? Contact us at AWS Training and Certification.

Lab overview
In this lab, you use AWS WAF web access control lists (web ACLs) and rate-based rules to secure a web application and Amazon API Gateway endpoint.

Objectives
By the end of this lab, you will be able to do the following:

Understand how AWS WAF ACLs help secure your web applications.
Create AWS WAF ACLs and rules.
Configure AWS WAF rate-based rules to limit incoming web requests.
Assign AWS WAF ACLs to API Gateway endpoints.
Test an application to verify AWS WAF rules using simulated web traffic.
Prerequisites
This lab requires the following:

To successfully complete this lab, you should have a basic knowledge of Amazon Web Services (AWS) services as defined in the AWS Cloud Practitioner Essentials course. You should be comfortable with navigating the AWS Management Console and running commands in a Linux-based command line.

Scenario
Your company recently launched a new minimum viable product named AnyProduct Transcription Application (TranscriptionApp). It is a web application that helps students keep track of the notes taken during class. After students store their notes, they can change, add, delete, search, and play the text in any audible format. TranscriptionApp is built on a serverless architecture that uses the following AWS services:

Amazon Cognito for user authentication
Amazon API Gateway to manage REST APIs
AWS Lambda functions to processes business logic
Amazon DynamoDB and Amazon Simple Storage Service (Amazon S3) to store application data
AWS Serverless Application Model (AWS SAM) to deploy the application
After receiving overwhelming acceptance from various learning academies, your company is interested in making the popular notes stored by topics in the TranscriptionApp available eventually to all registered students. This feature will introduce an imminent problem of increased number of web requests.

As the lead security engineer, you have been tasked with implementing AWS WAF to protect the TranscriptionApp from large-scale request floods. The requests could come from a specific IP address, or from a large number of varied addresses, which could negatively impact the availability of the application website.

Lab environment
Here is the architecture of the application that you will be working on. The highlighted portion is what you implement throughout this lab. It uses AWS WAF to protect the TranscriptionApp from an abnormal increase in the number of web requests.

Architecture diagram showing architecture of the applications. Highlighted portion is what you will implement as a part of this lab.

Duration
This lab requires approximately 45 minutes to complete.

Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Command: A command that you must run
 Expected output: A sample output that you can use to verify the output of a command or edited file
 Note: A hint, tip, or important guidance
 Additional information: Where to find more information
 CAUTION: Information of special interest or importance (not so important to cause problems with the equipment or data if you miss it, but that could result in the need to repeat certain steps)
 WARNING: An action that is irreversible and could potentially impact the failure of a command or process (including warnings about configurations that cannot be changed after they are made)
 File contents: A code block that displays the contents of a script or file that you need to run that has been precreated for you
 Knowledge check: An opportunity to check your knowledge and test what you have learned
 Consider: A moment to pause to consider how you might apply a concept in your own environment or to initiate a conversation about the topic at hand
 Security: An opportunity to incorporate security best practices
 Refresh: A time when you might need to refresh a web browser page or list to show new information
 Copy edit: A time when copying a command, script, or other text to a text editor (to edit specific variables within it) might be easier than editing directly in the command line or terminal
 Hint: A hint to a question or challenge
 Answer: An answer to a question or challenge
 Group effort: A time when you must work together with another student to complete a task
Start lab
To launch the lab, at the top of the page, choose Start lab.
 Caution: You must wait for the provisioned AWS services to be ready before you can continue.

To open the lab, choose Open Console.
You are automatically signed in to the AWS Management Console in a new web browser tab.

 WARNING: Do not change the Region unless instructed.

Common sign-in errors
Error: You must first sign out


If you see the message, You must first log out before logging into a different AWS account:

Choose the click here link.
Close your Amazon Web Services Sign In web browser tab and return to your initial lab page.
Choose Open Console again.
Error: Choosing Start Lab has no effect
In some cases, certain pop-up or script blocker web browser extensions might prevent the Start Lab button from working as intended. If you experience an issue starting the lab:

Add the lab domain name to your pop-up or script blocker’s allow list or turn it off.
Refresh the page and try again.
Task 1: Verifying that the TranscriptionApp is running
In this task, you get connected to your AWS Cloud9 development environment and ensure that the TranscriptionApp is working as expected.

You visit the TranscriptionApp website to verify that it deployed correctly. You then connect to the AWS Cloud9 development environment to invoke the TranscriptionApp API Lambda function.

Task 1.1: Signing in to the TranscriptionApp website
First, verify that the TranscriptionApp web application is working. The web frontend is already configured to use the deployed API.

Copy the TranscriptionAppWebsite value listed to the left of these instructions, paste it into a new web browser tab, and press Enter.
 Note: Because your connection to the TranscriptionApp site uses HTTP, your web browser might alert you to the fact that the connection is not secure. If it does, choose Continue to site.

On the TranscriptionApp page, configure the following settings:
For Username, enter student.
For Password, enter lab_password.
Choose Login.
You should see a list of five notes.

Perform one of the following actions to validate that the TranscriptionApp is working:
Add a new note.
Edit an existing note.
Delete a note.
Play the contents of a note.
Change the TranscriptionApp voice setting and note how the voice changes.
Task 1.2: Connecting to the AWS Cloud9 development environment
Next, connect to the AWS Cloud9 development environment where you run various commands throughout the remainder of the lab.

Return to your web browser tab with the AWS Management Console.

Copy the Cloud9url value listed to the left of these instructions, paste it into a new web browser tab, and press Enter.

Alternatively, you may navigate to the Cloud9 Instance this way:

In the search bar on the console, search for and choose Cloud9.
On the Environments page, for Lab 1, choose Open .
 Note: You might have to wait for the client to clone the api and web repositories the first time you connect to the development environment. The process is complete when the Lab-Is-Ready folder is displayed in the file tree pane at the left of the page.

 Note: If you receive a message that says “.c9/project.settings have been changed on disk,” choose Accept.

Task 1.3: Invoking the TranscriptionApp API using the Lambda function
Next, you use a Lambda function named LoadTest to invoke the TranscriptionApp API.

 Command: In the AWS Cloud9 terminal, run the following command to invoke the LoadTest Lambda function:

aws lambda invoke --function-name loadtest --payload '{"NumberOfCallsPerUser": "3"}' --cli-binary-format raw-in-base64-out out --log-type Tail --query 'LogResult' --output text | base64 -d
 Note: The command invokes the Lambda function and passes a payload in JSON format to extract the tail of run logs from Amazon CloudWatch. Notice that the NumberOfCallsPerUser parameter is set to 3, which causes the function to send three requests to the API Gateway endpoint.

 Expected output: The output should display the username and password used to sign in to the TranscriptionApp and the total number of notes available, similar to this:


START RequestId: fd278bb4-7a63-42b3-b5ea-2b3fb69c487b Version: $LATEST
UserName provided:student
Password provided:lab_password
API response:
b"# of notes available for 'student':5"
b"# of notes available for 'student':5"
b"# of notes available for 'student':5"
END RequestId: fd278bb4-7a63-42b3-b5ea-2b3fb69c487b
REPORT RequestId: fd278bb4-7a63-42b3-b5ea-2b3fb69c487b  Duration: 2112.24 ms    Billed Duration: 2113 ms        Memory Size: 128 MB     Max Memory Used: 67 MB  Init Duration: 280.00 ms
 Congratulations! You have successfully verified that the TranscriptionApp is running and used a Lambda function to simulate network traffic to the application.

Task 2: Creating an AWS WAF web ACL and adding a rate-based rule
In this task, you create an AWS WAF web ACL and a rate-based rule to limit the traffic that can flow to the TranscriptionApp.

Task 2.1: Creating an AWS WAF web ACL
AWS WAF uses web ACL capacity units (WCU) to calculate and control the operating resources that are required to run your rules, rule groups, and web ACLs. AWS WAF enforces WCU limits when you configure your rule groups and web ACLs. WCUs don’t affect how AWS WAF inspects web traffic.

A rate-based rule tracks the rate of requests for each originating IP address and invokes the rule action on IPs with rates that exceed a limit. You set the limit as the number of requests for a 5-minute time span. You can use this type of rule to put a temporary block on requests from an IP address that’s sending excessive requests.

 Note: By default, AWS WAF aggregates requests based on the IP address from the web request origin. But you can configure the rule to use an IP address from an HTTP header, such as X-Forwarded-For, instead.

When the rule action initiates, AWS WAF applies the action to additional requests from the IP address until the request rate falls below the limit. It can take a minute or two for the action change to go into effect.

First, you create an AWS WAF web ACL to secure the API Gateway resources.

Return to your web browser tab with the AWS Management Console.

In the search bar on the console, search for and choose WAF & Shield.

On the AWS WAF getting started page, choose Create web ACL.

On the Describe web ACL and associate it to AWS resources page, in the Web ACL details section, configure the following settings:

 Caution: If you change the Region value, the contents of all the other fields are reset to empty values. Change the Region value before you enter any other information.

For Region, choose the Region that matches the AwsRegionName value listed to the left of these instructions.
For Name, enter Notes_Rate_ACL.
For Description, enter Block actions from the API Gateway.
For CloudWatch metric name, keep the default value, which should match the text that you entered in the Name field.
For Resource type, select Regional resources.
Keep the remaining default values and then at the bottom of the page, choose Next.
Task 2.2: Adding a rate-based rule
The next step in the Create web ACL workflow is to add rules.

On the Add rules and rule groups page, in the Rules section, choose Add rules  and then choose Add my own rules and rule groups.

On the Add my own rules and rule groups page, in the Rule type section, for Rule type, select Rule builder if it is not selected already.

In the Rule builder section, configure the following settings:

For Name, enter Notes_Rate_Block_Rule.
For Type, select Rate-based rule.
In the Request aggregation section, configure the following settings:
For Rate limit, enter 200.

For IP address to use for rate limiting, select Source IP address if it is not selected already.

For Scope of inspection and rate limiting, select Consider all requests if it is not selected already.

In the Then section, for Action, select Block if it is not selected already.

At the bottom of the page, choose Add rule.

On the Add rules and rule groups page, keep the remaining default values, and then choose Next.

On the Set rule priority page, keep the default values and choose Next.

On the Configure metrics page, keep the default values and choose Next.

At the bottom of the Review and create web ACL page, choose Create web ACL.

 Congratulations! You have successfully created an AWS WAF web ACL with a rate-based rule.

Task 3: Attaching the web ACL to an API Gateway endpoint
Now that you have created the web ACL, you can attach it to the API Gateway and verify that it is functioning as intended.

Task 3.1: Attaching the web ACL
On the AWS Management Console, in the search bar, search for and choose API Gateway.

On the APIs page, choose the TranscriptionAppAPI link.

In the left navigation pane, under API: TranscriptionAppAPI, choose Stages.

In the Stages pane, choose the Prod link.

On the Settings tab, in the Web Application Firewall (WAF) section, for Web ACL, choose Notes_Rate_ACL (wafv2).

At the bottom of the page, choose Save Changes.

The web ACL is now associated with the Prod stage of the TranscriptionApp.

 Caution: If you receive an error message stating “AWS WAF couldn’t retrieve the resource that you requested, allow 1 minute for the process to complete,” close the error, refresh the page, and then attempt to save the changes again.

Task 3.2: Invoking the API endpoint to test the web ACL
Now that you have associated the AWS WAF web ACL with the TranscriptionApp API, run the LoadTest Lambda function again to verify that it’s blocking the traffic as intended.

Return to your web browser tab with the AWS Cloud9 terminal.

 Command: Run the following command to invoke the LoadTest Lambda function:


aws lambda invoke --function-name loadtest --payload '{"NumberOfCallsPerUser": "200"}' --cli-binary-format raw-in-base64-out out --log-type Tail --query 'LogResult' --output text | base64 -d
 Note: Because the function calls per user in the command that you just ran have been increased to 200, it can take approximately 5 minutes for the response to be returned in the AWS Cloud9 console. In the meantime, continue to the next step.

Task 3.3: Monitoring application logs in CloudWatch
Return to your web browser tab with the AWS Management Console.

In the search bar on the console, search for and choose CloudWatch.

In the left navigation pane, under Logs, choose Log groups.

On the Log groups page, choose the /aws/lambda/loadtest link.

 NOTE: It can take approximately 1–2 minutes for logs to appear in the log group. If you don’t see any log streams, wait for 1 minute, and then choose the refresh button .

To view the log events that were generated by the LoadTest Lambda function, choose the link for the most recent entry that appears in the Log streams list.
 Expected output: (The date and times will be different for you)

Log Group

 Note: If you do not see this output as expected, return to your AWS Cloud9 terminal and check the output. If you are unable to see the Forbidden messages, rerun the command in step 33 in the terminal and wait for the process to complete. Return to the CloudWatch console and view the latest log stream to see the expected output.

Return to your web browser tab with the AWS Cloud9 terminal.

 Expected output: You should now see responses from the Lambda function initiation that you performed earlier with Forbidden messages, similar to this:


b'{"message":"Forbidden"}'
b'{"message":"Forbidden"}'
b'{"message":"Forbidden"}'
b'{"message":"Forbidden"}'
b'{"message":"Forbidden"}'
b'{"message":"Forbidden"}'
b'{"message":"Forbidden"}'
END RequestId: 7268f3d5-15cb-4f2a-a5f5-d35a55d93662
REPORT RequestId: 7268f3d5-15cb-4f2a-a5f5-d35a55d93662  Duration: 51413.16 ms   Billed Duration: 51414 ms       Memory Size: 128 MB     Max Memory Used: 68 MB
 Note: If you receive the following error “Read timeout on endpoint URL: https://lambda.us-east-1.amazon.com/2015-03-31/functions/loadtest/invocations,” retry the command in step 33 to see the expected output.

 Congratulations! You have successfully applied a web ACL with a rate-based rule to secure your TranscriptionApp.

Task 4: Reviewing AWS WAF web ACL sampled requests
In this task, you review the sampled requests from Amazon CloudWatch on the AWS WAF web ACL details page.

Return to your web browser tab with the AWS Management Console.

In the search bar on the console, search for and choose WAF & Shield.

In the left navigation pane, under AWS WAF, choose Web ACLs.

On the Web ACLs page, choose the Notes_Rate_ACL link to view its details.

On the Notes_Rate_ACL page, choose the Overview tab if it is not active already.

Scroll down to view the Sampled requests section. On the All metrics dropdown, choose Notes_Rate_Block_Rule to view the requests what were blocked by the rate-based rule that you created.

Use the same dropdown menu to change the filter to Notes_Rate_ACL to view all the requests that were allowed.

You can use the Sampled requests section to help pinpoint specific IP addresses that might be causing issues for your applications and block them specifically, or to verify if certain IPs are being blocked when they shouldn’t be.

 Congratulations! You have successfully reviewed the web ACL sampled requests to determine which requests were allowed and which were blocked.

Conclusion
 Congratulations! You now have successfully done the following:

Understood how AWS WAF ACLs help secure your web applications
Created AWS WAF ACLs and rules
Configured AWS WAF rate-based rules to limit incoming web requests
Assigned AWS WAF ACLs to API Gateway endpoints
Tested an application to verify AWS WAF rules using simulated web traffic
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End lab and then confirm that you want to end your lab.

Additional resources
Web access control lists (web ACLs).
For more information about AWS Training and Certification, see https://aws.amazon.com/training/.

Your feedback is welcome and appreciated.
If you would like to share any feedback, suggestions, or corrections, please provide the details in our AWS Training and Certification Contact Form.