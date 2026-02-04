# DI2 Week 5: Securing the Application

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to [Developer Intermediate 2](./developer-intermediate-2.md)
* back to repo's main [README.md](../../../README.md)

## Securing the Application

### Weekly Overview

AnyCompany Pet Shelter needs to prevent `personally identifiable information (PII)` from falling into the wrong hands. To do this, the pet shelter wants to restrict access to adoption applications to only employees of the shelter.

There are two parts to accomplishing this. One part involves `authenticating` users so the application knows they are employees. The other part involves `authorizing` employees to view the list of applications and specific details on the applications. Authentication involves establishing either identity or membership in a group. Authorization involves allowing or disallowing access to resources based on identity or group membership.

With `Amazon Cognito`, you can focus on which authentication and authorization rules you want to enforce in a secure manner. In this module, you will use Amazon Cognito to manage your `pool` of employees and Amazon API Gateway to apply your rules to requests for application information.

First, you will create a `user pool` in Amazon Cognito to store and authenticate the employees you add. This pool includes specific details, such as how users will be authenticated and which password rules to enforce. You will then integrate this pool with the AnyCompany Pet Shelter application.

Next, you will update the application to work with Amazon Cognito and make it possible for users to log in. A different version of the website displays for users who log in compared to those who do not.

Finally, you will create an `authorizer` in API Gateway that you will apply to the `/adoptions` endpoint. Then, you will configure the application to use the authorizer so that API calls to the backend resources for adoption applications require proof of being logged in.

## AUTHENTICATING AND AUTHORIZING WITH AMAZON COGNITO

### Securing an Application

Securing an application can include many interrelated components. Application architecture, network configuration, password rules, and encryption decisions are all common parts of securing an application.

This lesson focuses on two critical processes for securing an application—authentication and authorization.

#### What to secure

AnyCompany Pet Shelter's primary concern is ensuring the confidentiality of pet adoption applications submitted by users. These applications contain sensitive information, including personally identifiable information (PII) such as names and contact details. PII is particularly important to safeguard because unauthorized access or exposure can lead to identity theft, fraud, and other privacy breaches.

To mitigate these risks, AnyCompany Pet Shelter must implement strong security measures that focus on both `authentication` (verifying who the user is) and `authorization` (ensuring that users can only access the appropriate resources).

##### Confidentiality

Confidentiality is a core principle of security. It means that information should only be accessible to users or other entities who have a need to access that information. It is closely tied to the concept of secrecy — of hiding things that one doesn't want others to know. Confidentiality is a common concern in everyday life, and like organizations, people have policies about whether their information is confidential and how well protected it is.

For instance, where you bank is generally not highly confidential. It's printed on your debit card and shows up on electronic funds transfers. A lot of other financial entities need to know where you bank and what your account number is, from your place of work to your credit cards.

However, your balances and transactions are generally much more restricted. Besides credit reporting agencies and situations where you have to prove that you have a certain amount of money (such as to enter the US under a student visa), that information is highly confidential, by default. You could have a policy of sharing that information far and wide, but you probably don't.

Protecting the confidentiality of your bank account information is one of the more serious pieces of digital security that people typically have. Banks are expected to have strict controls in place to prevent anyone other than you from seeing, much less doing something with, your money or credit. Authentication and authorization systems are key components of this. The bank is responsible for maintaining systems that restrict access to someone who's authenticated as you. You're responsible for ensuring that no one else can authenticate as you, such as through good password management or promptly reporting lost or stolen cards.

##### Personally identifiable information

Personally identifiable information (PII) is a category of data that is frequently considered confidential. PII includes any information that can be used to identify a specific person. This could be their name, address, tax ID, email address, phone number, or other context-specific pieces of information. In addition, PII goes beyond pieces of data that are highly identifying on their own. For instance, gender, zip code, and birth date are considered PII, even though each piece of data can apply to many people.

PII includes a wide range of data categories that can be used to directly or indirectly identify an individual.

In 2000, computer scientist and technologist Dr. Latanya Sweeney published a study of data from the 1990 US census showing that combinations of widely used, non-identifying pieces of information could be used to uniquely identify many people.

Gender, zip code, and birth date are all common aggregating data used in studies in many fields, such as medicine or economics. Sweeney found that 216 million Americans (87 percent) could be uniquely identified in the 1990 census from those three pieces of data.

The important takeaway here is that PII is a much bigger category than it appears, and it's impossible to anticipate the information that might be relevant to a malicious actor. When you're deciding on what personal information to secure, the starting point should always be `all of it`. Then, you identify types of users who need access to the PII and the minimum access that they need. Then, you grant those users exactly that access. This is known as `the principle of least privilege`.

At AnyCompany Pet Shelter, most employees are multifunctional and need full access to the adoption applications. There are also clients who, at this point, should have no access. It might make sense for clients to be able to see their own applications, but you won't be implementing that during this part. This approach is consistent with the principle of least privilege. AnyCompany Pet Shelter doesn't know whether online access to applications will matter to clients. Granting access should only be done when it's known to be necessary.

#### Authentication and authorization

The combination of authentication and authorization controls access to your application. Together, they answer the question, "Who can do what in my application?" Authentication verifies who a user is. Authorization determines what that user can access and what they can do with it. If you're a traveler entering a country, your authentication is your passport and possibly some additional biometrics. Your authorization—what you can do in the country—is a matter of your visa, residency status, or citizenship.

##### Authentication

Authentication is any process used to determine who someone is. It's important to understand that `who someone is` is often not the same as `identity verification`. Registering for a bank account requires identity verification. Registering for a social media account usually does not. Whether identity is being verified and with what degree of rigor is a matter of account creation, not authentication. Authentication is a matter of what account is accessing the application.

`Who` doesn't always refer to a person. It could represent another system, and in some cases, multiple people might share a single authentication, as seen with streaming services.

It's also common for systems to authenticate users with generic credentials like user when no specific authentication is provided, making authorization decisions based on those default credentials.

Consider the following real-world examples of authentication.

###### Host a party

If you're hosting a small party, everyone who attends is authenticated individually, by one of two methods:

* You know them personally and use the process of recognizing their face.
* They're with someone you know, and you use the process of trusting someone that you have otherwise authenticated.

Most likely, you're not using identity verification.

This is similar to the behavior of some decentralized systems that rely on a [web of trust](https://en.wikipedia.org/wiki/Web_of_trust). A web of trust is a form of public-key encryption, as would be used to authorize a website, but without a centralized certificate authority responsible for verification. Instead, everyone has their own list of public keys and assign a level of trust to them. This can be based on knowing them personally or trusting others that you know who trust them, like being introduced to a friend's date.

###### Get medical help

If you're at an outdoor event and someone gets injured, you might look around to find a prominently labeled medical tent. This authenticates to you that the people working that tent can help with your problem. After approaching them, you will share who you are individually and share a level of identity verification. The medic will need to show you their credentials as an individual, and you might be asked to provide identification for the incident report.

This is similar to the authentication required to open an account with a bank. The medical tent is putting its authentication out into the world for anyone to see, rather like a bank website's certificate. Initially, you're authenticated as just a user of the site, just like you're just an attendee of the event. This is sufficient to `authorize` some activities, such as checking loan rates or asking for water. Creating an account or receiving care, however, requires further authentication, including identity verification. For some accounts, a specific employee of the bank will authenticate themselves to you as your point of contact for the account, just like a medic needs to show credentials before providing aid.

###### Go out to eat

If you're dining at a busy restaurant, you might make a reservation ahead of time and then provide authentication when you arrive by providing the name that you made the reservation for. If you don't have a reservation, authentication is merely providing your name for the wait list and being the only person who responds when your name is called. There's no identity verification here, but the process is sufficient for the needs of the restaurant.

This is similar to the authentication used by many comment portions of websites. Being a logged-in user simplifies the process of commenting and might let you bypass reviews needed before posting a comment. On many sites, you can comment as a guest by providing a name to attach to your comment, just like adding your name to a wait list at a restaurant. Neither the restaurant nor the website in this case is particularly concerned with who you actually are.

##### Authorization

Authorization is the assignment of privileges to users based on identity. A privilege contains two main parts — `When can a user do something?` and `How does that thing behave for the user?`

`When can a user do something?` is the question of whether and under what circumstances can an authenticated user do a thing. Consider an operation to add users to groups in a system. Perhaps there's an administrative role that can always add any user to any group regardless of details (such as which group it is). Other users can only add users to a group if they're the owner of the group. Still others might have a role that's defined to allow them to add users to a particular set of groups. And everyone else can't add anyone to any group.

`How does that thing behave for the user?` is the question of what happens when an authenticated user does a thing. Consider viewing a user's profile on a website, for instance. Several outcomes can happen based on the specific circumstances.

* The user who owns a profile sees everything in the profile and has edit options for everything that's mutable.
* Regular users can view any profile, but what they see is the collection of items that the owner of the profile made public. Some items are never visible to other users as a matter of policy, such as payment information. Viewers might see nothing if the profile is set to private.
* An employee in a billing department should be able to view full contact information, even if not public, and billing information. Depending on the website's processes, they might have the ability to add or edit this information for a user.

Consider the following real-world example of authorization.

###### Enter a country

Authentication when entering a country is straightforward. If you are traveling between countries with an open border agreement — such as in the EU — no authentication is required. Otherwise, authentication requires presentation of a passport and possibly a biometric scan of some sort.

However, authentication gets you nowhere by itself. You also need authorization to enter a country, and that authorization can be highly complex.

* The country might require you to have a visa or permit.
* The country might limit the length of time that you can stay.
* The country might not authorize you to work.
* The country might not authorize you to take classes.
* The country might authorize you to work, but only for a company that sponsors you.
* The country might not authorize you to purchase property.
* The country might provide limited immunity from prosecution for diplomatic reasons.
* You might be a citizen with the automatic authorization to do anything otherwise lawful.

This is just a fraction of possible situations. Authorization is one of the more complex aspects of any system that isn't completely open.

#### Activity: Comparing authentication and authorization

* `Authentication` is about proving your identity, like when you log in to your online banking account with your username and password. That's you showing that you are who you say you are. `Authorization`, on the other hand, is about what you're allowed to do once you're in. For example, after you've logged in, the bank's system decides what you can access, like checking your balance or making a payment.
* `Authentication` is like a key that unlocks the door, and `authorization` decides which doors the key can open. For instance, in a computer system, entering correct login credentials authenticates you. Then, the computer authorizes you to access specific files or complete certain actions, which reflects authorization.

##### Working with authentication and authorization

Although authentication is generally straightforward, even if it involves a lengthy process due to a strong need for identity verification, authorization can be quite complicated. Even capturing all the business requirements for authorization can be a virtual impossibility. Implementing them can be more so if the permissions tools available (users, groups, roles, and the like) don't reflect the way the business rules organize the permissions.

For applying the authorization rules in this task, you will be using a service called `Amazon Cognito` to provide `authenticatio`n and `authorization`. `Amazon Cognito` handles the heavy lifting of securely managing users, letting you focus on the business rules of which users should be able to access what information.

```text
You will learn how to use Amazon Cognito to apply authorization rules in your applications' specifications. You will also have the option to dive a bit deeper into the options that Amazon Cognito provides. Consider what other rules might be appropriate to the application. Consider where the rules that you're enforcing could be better, and what other capabilities of Amazon Cognito could be used to improve authorization.
```

#### Amazon Cognito

`Amazon Cognito` is a fully managed, reliable, and scalable customer identity and access management tool. It lets you configure and manage `authentication` and `authorization` rules for your entire application.

`Amazon Cognito` supports several common authentication methods. This includes logging in using a social media account, username and password, or enterprise identity provider. It also includes support for multi-factor authentication (MFA).

Amazon Cognito integrates with your applications to control access to specified endpoints. Endpoints can be associated with groups of users, called user pools, with access granted or denied based on a user's presence in the associated pool.

Amazon Cognito also provides `identity pools`, which can be used to authorize authenticated or anonymous users to access AWS resources. Amazon Cognito identity pools provide temporary AWS credentials for users who are guests (unauthenticated) and for users who have authenticated and received a token. With those AWS credentials, the application can access AWS resources, such as a backend in AWS.

Amazon Cognito also streamlines user access to AWS services made through your applications. Role-based privileges can be granted to services such as Amazon Simple Storage Service (Amazon S3), Amazon DynamoDB, and AWS Lambda.

### Activity: Pet Shelter – Authentication and Authorization Part 1

### Access Tokens

### Activity: Pet Shelter – Authentication and Authorization Part 2

### Activity: Pet Shelter – Authentication and Authorization Part 3

### Knowledge Check

### Summary

### Additional Resources

## HANDS-ON LAB ACTIVITY

### Lab: Adding Authentication and Authorization to an App
