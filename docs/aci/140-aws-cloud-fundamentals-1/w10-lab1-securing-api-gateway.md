Securing Amazon API Gateway Using an Amazon Cognito Authorizer
© 2023 Amazon Web Services, Inc. or its affiliates. All rights reserved. This work may not be reproduced or redistributed, in whole or in part, without prior written permission from Amazon Web Services, Inc. Commercial copying, lending, or selling is prohibited. All trademarks are the property of their owners.

Note: Do not include any personal, identifying, or confidential information into the lab environment. Information entered may be visible to others.

Corrections, feedback, or other questions? Contact us at AWS Training and Certification.

Lab overview
In this lab you set up an Amazon Cognito user pool with a hosted UI. You then use an Amazon Cognito authorizer to restrict API access within Amazon API Gateway to a precreated mock API.

Services used in this lab
Amazon API Gateway is a fully managed service that developers can use to create, publish, maintain, monitor, and secure APIs at any scale. APIs act as the “front door” for applications to access data, business logic, or functionality from your backend services.

Amazon Cognito is an identity platform for web and mobile apps. It’s a user directory, an authentication server, and an authorization service for OAuth 2.0 access tokens and AWS credentials

Objectives
By the end of this lab, you will be able to do the following:

Set up an Amazon Cognito user pool with a hosted UI.
Parse and understand Amazon Cognito sign-in URL components.
Create an Amazon Cognito authorizer to restrict API access.
Test the Amazon Cognito authorizer.
Prerequisites
This lab requires the following:

Access to a computer with Microsoft Windows, macOS X, or Linux (Ubuntu, SUSE, or Red Hat)
A modern internet browser such as Chrome or Firefox
A text editor of your choice (for example, Notepad, TextEdit, or VSCode)
Scenario
In this lab you have a preprovisioned mock API provided through Amazon API Gateway. You create an Amazon Cognito user pool and an Amazon Cognito authorizer within API Gateway. These work together to provide authorization and authentication for attempts to log in to the mock API.

Duration
This lab requires 60 minutes to complete.

Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Command: A command that you must run
 Expected output: A sample output that you can use to verify the output of a command or edited file
 Note: A hint, tip, or important guidance
 Additional information: Where to find more information
 CAUTION: Information of special interest or importance (not so important to cause problems with the equipment or data if you miss it, but that could result in the need to repeat certain steps)
 WARNING: An action that is irreversible and could potentially impact the failure of a command or process (including warnings about configurations that cannot be changed after they are made)
 File contents: A code block that displays the contents of a script or file you need to run that has been precreated for you
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
 You must wait for the provisioned AWS services to be ready before you can continue.

To open the lab, choose Open Console.
You are automatically signed in to the AWS Management Console in a new web browser tab.

 Do not change the Region unless instructed.

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
Task 1: Setting up and exploring Amazon Cognito
In this task, you set up your Amazon Cognito user pool for authentication.

On the AWS Management Console, in the search bar, search for and choose Cognito.

Choose Create user pool.

 Note: You can safely ignore the error message “[AccessDeniedException] Failed to fetch ACM certificates.”

In the Configure sign-in experience step, configure the following settings for Authentication providers:

For Provider types, select Cognito user pool.
For Cognito user pool sign-in options, select User name.
For User name requirements, select Allow users to sign in with a preferred user name.
Choose Next.

In the Configure security requirements step, configure the following settings:

In the Password policy section, select Cognito defaults.
In the Multi-factor authentication section, for MFA enforcement, select No MFA.
In the User account recovery section, leave the default options selected.
 CAUTION: Selecting No MFA is not a best security practice. You are only selecting this option for the sake of this lab demonstration. Using MFA in a real-world use case is a best practice.

Choose Next.

In the Configure sign-up experience step, configure the following settings:

In the Verifying attribute changes section, clear the Keep original attribute value active when an update is pending - Recommended check box.
Leave the remaining settings as is.
Choose Next.

In the Configure message delivery step, configure the following settings:

In the Email section, for Email provider, select Send email with Cognito.
Leave the remaining settings as is.
Choose Next.

In the Integrate your app step, configure the following settings:

In the User pool name section, for User pool name, enter cognito-lab-pool.

In the Hosted authentication pages section, select Use the Cognito Hosted UI.

In the Domain section, leave the default Use a Cognito Domain selection, and enter a unique domain address in the Cognito domain text box.

Example: https://lab240679
In the Initial app client section, for App client name, enter lab-api-client.

In the Initial app client section, for Allowed callback URLs, append example.com/callback to the https:// portion in the URL text box.

Expand the  Advanced app client settings section.

Choose the Select authentication flows  dropdown and choose ALLOW_CUSTOM_AUTH.

In the OAuth 2.0 grant types section, choose the Select OAuth 2.0 grant types  dropdown and choose Implicit grant.

In the same OAuth 2.0 grant types section, remove Authorization code grant by choosing the X next to it or by deselecting the checkbox.

 WARNING: You will see the message “The implicit grant flow exposes OAuth tokens in the url. We recommend that you use only the authorization code flow with PKCE for public clients.” Choosing Implicit grant is not a best practice in a real-world scenario and is only being used for demonstration in this lab environment.

 Additional information: What is the difference between normal code flow and code flow with Proof Key for Code Exchange (PKCE)?

When using code flow with PKCE, all the principles of code flow still apply (code returned on authorization request is exchanged for access or ID token). The PKCE makes this safer for native and web applications (public clients) by generating a code exchange key. This key ensures that the authorization request and the token request are done by the same client (and not intercepted by a man in the middle). Because web applications can’t store secrets, PKCE allows for creating a secret dynamically at the beginning of the authorization flow as a contrast to the static secret in code flow (which can only be used for private server clients).

Choose Next.

Choose Create user pool.

A banner message like the following is displayed at the top of the page:  User pool “cognito-lab-pool” has been created successfully. .

Task 2: Creating a user and signing in to the hosted UI
In this task, you create a user for the Amazon Cognito user pool.

In the User pools section of the new page, choose the cognito-lab-pool that you just created.

On the Users tab, choose Create user.

In the User information section, configure the following settings:

For Invitation message, select Don’t send an invitation.
For User name, enter CognitoUser.
For Email address optional, leave this blank.
Select  Mark email address as verified .
For Temporary password, select Set a password and then enter the provided password listed to the left of these lab instructions.
Choose Create user.

A banner message like the following is displayed at the top of the page:  User “CognitoUser” has been created successfully. .

On the user pool page, choose the App integration tab.

Scroll to the bottom to find the App client list section, and choose the lab-api-client link.

In the Hosted UI section, choose View Hosted UI .

On the sign-in page, enter your previously created credentials:

For Username, enter CognitoUser.
For Password, enter the provided password listed to the left of these lab instructions.
 CAUTION: If you receive an error notification when trying to log in, close out of the login page and open it from the Hosted UI option and try to log in again.

Choose Sign in.

Enter a new password that meets the password requirements, and any mock email address. Then choose Send.

 Note: The email address doesn’t have to be a valid email address because you selected the Mark email address as verified option when creating the user. You can use any mock email, for example, test1@gmail.com.

You will get an error and an unreachable page; this is the expected response after attempting sign in.

 CAUTION: If the webpage timesout, please refresh and try logging in again. If you don’t receive a 404 error page, that is ok for this lab example.

You are unable to sign in because you are not presenting a valid ID token. You will now copy the sign-in URL to retrieve this ID token for further use.

 Copy edit: Copy the entire URL from your browser tab of the Cognito sign in page, and paste it into a text editor.
Example image of the copied URL in an internet browser.

 CAUTION: This will be a very long URL string when pasted into the text editor. This is normal. The full URL in your text editor will look similar to the following code block:


https://example.com/callback#id_token=eyJraWQiOiJJR1ZrVkw5NWNrS2NKZzM5U0N3bm9GU0M0c1VsVTJ1ZHQrZ052b05hNHc4PSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiTGRITjR1VUhnWnk4RW9QYThITEZwZyIsInN1YiI6IjZhY2MxY2JjLTZlNDctNDk4My05NmJlLWEzMWQxMmNkY2M2NyIsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy13ZXN0LTIuYW1hem9uYXdzLmNvbVwvdXMtd2VzdC0yXzYyeHNuTTVmdCIsImNvZ25pdG86dXNlcm5hbWUiOiJ6YWNoIiwiYXVkIjoiZ2Fqb203b25qZm9jcnQxcWg0bDUyamJkaiIsImV2ZW50X2lkIjoiMjIwNWI3ZTItNzU0ZS00MTRiLWI4OGQtNTAzYTExODMxYTU5IiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2ODY3NzIzMjksImV4cCI6MTY4Njc3NTkyOSwiaWF0IjoxNjg2NzcyMzI5LCJqdGkiOiI2ZDA5NmExOC1kODU4LTQzNjItYTM1Ny1mNTc2MGZmNGMzMjYiLCJlbWFpbCI6InRlc3QyQGdtYWlsLmNvbSJ9.Fa35cPlyP8QGjWJE8R00sh-g6D4bA1eyygScxQf2ZyY9hnLeAX8jPxWpdQHQcoytm6HvzPAJwMWmD8YhNEgijsxO3gNnmwyd_5UblQ3MlOs0T952cJ0eDZSrh-fj0qCGYnBvqfaBGvvwFuo-de-9TwoCXw4nwaztWXl1UaLkEZSzi_uwy8Fy9sL62COS7tdSjv54acp4pALY_-hmyyedbHwwkmjGsMst--pIdzB0_-mrwTFR0iOdJm4xp109v948rhaCur6EhGVic617sw3Nzkm_lSx1dB2xUvyXClkZveYNEzGoFIpqDodkZgoxSx-4ApdznDlw54Nk2HFsVMpfvQ&access_token=eyJraWQiOiJEWXVZSEozUDBXZWU0OXYyTHR6Vm56UmpRZFBFeE9YUGVVUWxZanZ3NE1NPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI2YWNjMWNiYy02ZTQ3LTQ5ODMtOTZiZS1hMzFkMTJjZGNjNjciLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtd2VzdC0yLmFtYXpvbmF3cy5jb21cL3VzLXdlc3QtMl82Mnhzbk01ZnQiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiJnYWpvbTdvbmpmb2NydDFxaDRsNTJqYmRqIiwiZXZlbnRfaWQiOiIyMjA1YjdlMi03NTRlLTQxNGItYjg4ZC01MDNhMTE4MzFhNTkiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6InBob25lIG9wZW5pZCBlbWFpbCIsImF1dGhfdGltZSI6MTY4Njc3MjMyOSwiZXhwIjoxNjg2Nzc1OTI5LCJpYXQiOjE2ODY3NzIzMjksImp0aSI6ImY5M2VlYmRiLTY5NGMtNGQyZi05YTQwLTU1MDM3OTkyMTZkZiIsInVzZXJuYW1lIjoiemFjaCJ9.IfE5bGg5WDtrKh-DTRdMNGu3Ok7FXfdTCItc952DDZM4ffkCCvuwAkhTM8nekSmOoNwY_w17b6g78OeLNpwegUoBPacShx68tnKzIlpygkduQQnQRKING8L3H1yDJId_jDQh_TSwS9Z-E-rBFVLUr7f8TP1eqMIsZTGkSFAgVdyY9QK7hfQJHEl2K5rv0nbpIqWFHiTpN2wufZPN6KDPer1GqruYad3l5wtpJBKKVHnbuOjQVrQ3hmGdzXkTH0kX5JfOxAKwvG1Gt0nEU9dVq2UvjO_U3o0caNcd_Z9A8PZti1g1MqWy3vriNikFpcukoXzZ1KXs8oMiATjL_CNSPA&expires_in=3600&token_type=Bearer
You will now parse and separate the values of the URL so that they are easier to identify and copy and paste later in the lab.

 Note: An efficient way to parse through data like this is to use the Ctrl+F function on Windows or Cmd+F on a Mac. This helps you quickly search for the values that you are looking for.

The first value that you want to find is id_token. To do this, press Ctrl+F or Cmd+F, enter #, and press Enter.
This should take you to the id_token value.

Put your cursor right before the #id_token value, and press the Enter key twice.
Your text editor should now look similar to the following:

Example showing the spacing of the URL in the text editor after breaking up the id_token value.

Next, in the search window of the text editor, replace # with & and press Enter until you find the access_token.

Put your cursor just before the &access_token value, and press the Enter key twice.

Repeat this process for the final two ampersands (&s).

Press the Enter key in the search bar to bring you to the second ampersand, place your cursor just before it, and press the Enter key twice.

Repeat this process for the third and final ampersand (&).

The URL in your text editor should now look similar to the following image:

Example showing the end product for the separated values of the URL.

 Additional information: The values that you just parsed in this URL are as follows:

id_token: The ID token is a JSON Web Token (JWT) that contains claims about the identity of the authenticated user, such as name, email, and phone number. You can use this identity information inside your application.

access_token: The user pool access token contains claims about the authenticated user, a list of the user’s groups, and a list of scopes. The purpose of the access token is to authorize API operations. Your user pool accepts access tokens to authorize user self-service operations.

expires_in: This is the time in which this token will expire.

token_type: This is the type of token being used.

Task 3: Restricting API access
In this task, you create the Amazon Cognito authorizer to secure access to the precreated mock API. Then you attach it to the API. You can use authorizers to control access to your APIs by using Amazon Cognito user pools or an AWS Lambda function.

Adding the authorizer to the API Gateway enhances security by validating and authorizing incoming requests before they reach backend services. The authorizer ensures that only the Amazon Cognito user that you have created can interact with the API.

Task 3.1: Exploring API Gateway
On the AWS Management Console, in the search bar, search for and choose API Gateway.

Choose Mock API.

In the Resources column, choose the GET option.

Select the Test tab, then choose Test.

Here you can see at the bottom of the execution log that you get Status: 200 (which means the request was successful ), and the contents of the data in the Response Body box reads {“confidential”:“Secure, Me!!”}.

Scroll to the bottom of the Logs section and you will see messages that say Successfully completed execution and Method completed with status: 200.
This lets you know that this method execution is accessible. Now it is time to add an authorizer to it, to further secure the confidential data within.

Choose Stages in the left navigation pane.

In the Stage details section,  Copy edit: the Invoke URL into a new browser tab, then append /mock to the Invoke URL and select enter.

 Note: The updated invoke URL should look something like https://6bpdlezi1l.execute-api.us-west-2.amazonaws.com/dev/mock

This opens a page in your browser displaying the following message: confidential: “Secure Me!!”.

This lets you know that this API endpoint is accessible to the world. This will be the resource to be locked down in the following tasks.

Task 3.2: Creating an Amazon Cognito authorizer
Switch back into the API Gateway console browser tab and choose Authorizers on the left side of the page.

Choose Create authorizer and then configure the following settings:

For Name, enter lab-api-cognito-authorizer.
For Type, select Cognito.
For Cognito User Pool, choose cognito-lab-pool.
For Token Source, enter auth-token.
Choose Create authorizer.

Task 3.3: Attaching the authorizer to the API
You now have all the parts to add authentication to the API. Here you will restrict access to the /mock GET resource of the API.

From the Amazon API Gateway console, choose Resources on the left side of the page.

Choose GET and then choose the Method Request option.

In the Method request settings section, select the Edit button.

Under Method request settings configure the following option:

Authorization Select lab-api-cognito-authorizer
Select Save.

You now need to deploy this change to the dev environment.

Choose Deploy API.

In the Deploy API window, configure the following settings:

Deployment stage: Choose the dropdown and choose dev.
Deployment description: Enter testing api authentication.
Choose Deploy.

A banner message like the following is displayed at the top of the page:  Successfully created deployment for Mock API. This deployment is active for dev. .

Successfully created deployment for Mock API. This deployment is active for dev.

Task 4: Testing the Amazon Cognito authorizer
Go back to your browser tab where you had the appended Invoke URL and refresh  the page.
You should now see the following message: message: “Unauthorized”.

This confirms that the Amazon Cognito authenticator is now in place and the API resource is no longer available to the public.

 CAUTION: If you do not see this message, keep refreshing the page until the authorizer syncs and the unauthorized message appears.

You now confirm that the Cognito API authorizer is working as intended by testing the actual authorizer.

Return to the API Gateway console and choose Authorizers from the left navigation pane.

Choose the lab-api-cognito-authorizer and select Test authorizer.

You should receive an Unauthorized request message. This is because you are not presenting an id_token, which is required.

Return to your text editor where you parsed the login URL from the hosted UI earlier.

Copy the id_token value, paste it into the auth-token (header) text box in the lab-api-cognito-authorizer - Test Authorizer pop-up window, and choose Test authorizer.

 Tip: Copy just after the = sign for the #id_token=. The following image is an example of what to copy:

Image of the id_token value to copy.

Review the Response and take note of the following:

Response Code: 200 indicates successful authorization.
cognito:username verifies the Cognito user that you created and signed up with.
email verifies the test email that you used to sign up.
token_use shows the required and successful token used for authorization.
 Congratulations! You have successfully tested the Amazon Cognito authorizer and confirmed that it works!

Conclusion
 Congratulations! You now have successfully done the following:

Set up an Amazon Cognito user pool with a hosted UI
Parsed and understood Amazon Cognito sign-in URL components
Created an Amazon Cognito authorizer to restrict API access
Tested the Amazon Cognito authorizer
Additional resources
Control access to a REST API using Amazon Cognito user pools as authorizer
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End lab and then confirm that you want to end your lab.

For more information about AWS Training and Certification, see https://aws.amazon.com/training/.

Your feedback is welcome and appreciated.
If you would like to share any feedback, suggestions, or corrections, please provide the details in our AWS Training and Certification Contact Form.