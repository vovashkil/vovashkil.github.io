# Week 1: Security 3 Part 1

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to [AWS Cloud Fundamentals 2](./aws-cloud-fundamentals-2.md)
* back to repo's main [README.md](../../../README.md)

## Coming Up

### Security 1

* Use AWS to support security
* Implement a strong identity foundation
* Maintain traceability
* Apply security at all layers
* Automate security best practices
* Protect data in transit and at rest
* Minimize your attack surface
* Prepare for security events

### Security 2

* Authentication and authorization for serverless applications
* Identified ways to control access to and protect APIs
* Identify the key differences between AWS Secrets Manager and the Systems Manager Parameter Store
* Issue and manage certificates with AWS Certificate Manager, or ACM

### Security, Monitoring, and Compliance module

* The basics of monitoring and compliance
* Deep-dive into some of the most common AWS services used for monitoring, such as Amazon CloudWatch, AWS CloudTrail, Amazon EventBridge, and AWS Config

### Next security part

* Implement security measures
* Use temporary credentials
* Apply security protocols to AWS Lambda functions
* Use access controls based on tags for efficient resource management
* Establish and maintain a data perimeter
* Use encryption to protect data in transit and at rest
* Efficiently respond to security incidents

---

## Managing Long-Term and Short-Term User Credentials

Within the AWS environment, credentials are used to verify who you are and determine which AWS resources you have been given permission to access. These credentials can be either **long-term** or **short-term** in nature, and are managed using several different mechanisms.

### Users and credentials

Credentials are associated with users. User credentials can be either long-term or short-term. Whether long-term or short-term, AWS credentials work the same way and serve the same purpose, with two important exceptions.

First, short-term credentials are temporary, lasting from just a few minutes to several hours before they expire. For this reason, short-term credentials are also referred to as temporary credentials. Contrast this with long-term credentials, which do not expire.

Second, temporary security credentials are generated dynamically when requested by the user. Long-term credentials are created when the user is created and remain the same until the user changes them. Temporary security credentials provide users access to your AWS resources without having to define an AWS identity for them, or embed long-term credentials within an application.

The following table lists four common AWS user types and the type of credential associated with those users.

| User | Description | Credential type |
| ---- | ----------- | --------------- |
| Root | Owner of the AWS account, authenticated using a password or access key | Long-term |
| IAM user | User authenticated using AWS Identity and Access Management (IAM) services, authenticated using a password or access key | Long-term |
| Federated user | User authenticated using a trusted third-party identify provider, such as a social media site | Short-term |
| AWS IAM Identity Center user | User authenticated using the IAM Identity Center single sign-on capabilities | Short-term |

---

Short-term credentials are also used with AWS IAM roles, which allow users to temporarily access AWS resources by assuming a granted role. This is a common approach to security in many application architectures.

---

The short-term nature of temporary credentials used by federated users, IAM Identity Center users, and IAM roles provides some advantages. Specifically, temporary credentials support good application security practices, and streamline the management of individual application users and application security controls.

### The advantages of temporary credentials

1. **Supports application security**. You do not have to distribute or embed long-term AWS security credentials with an application itself.
2. **Streamlines application user management**. You can provide access to your AWS resources to users without having to define an AWS identity for them.
3. **Reduces application management tasks**. You can specify how long temporary credentials are valid, so you don't have to update or explicitly revoke them.

---

### Enabling federated access to AWS accounts using a separate SAML 2.0-based corporate identity provider

Having users authenticate against an identity provider such as AWS Single Sign-On, or a third-party provider is known as identity federation. AWS STS provides different ways to federate users by landing corporate users in an IAM role based on some regular expression or mapping from the identity provider.

1. All contractors happen to be authenticated via an on-premises SAML 2.0-based identity provider.
2. With the identity provider configured in a trust relationship with the AWS account, the developer browses to your company’s identity provider portal and selects the option to access the AWS Management Console. The developer is then authenticated against the identity store.
3. The identity provider returns a SAML assertion, which includes information about the developer such as their identity and attributes that map to an IAM role. The browser then makes the **AssumeRoleWithSAML** API call to AWS STS, passing information regarding the identity provider, the role to assume, and the SAML assertion.
4. Temporary security credentials are then returned to the developer’s browser, and the developer is redirected to the AWS Management Console.

---

From the user’s perspective, the process happens transparently. The developer starts at your organization's internal portal and ends up at the AWS Management Console without ever having to supply any AWS credentials.

---

### Managing long-term credentials

Because long-term credentials do not expire, extra steps should be taken to ensure that these credentials are properly protected. Common options for protecting long-term credentials include the use of multi-factor authentication (MFA), and password and access key management techniques.

#### Multi-factor authentication

MFA adds an additional layer of protection for users with long-term credentials. MFA requires that additional authentication information, above and beyond the user's password, be supplied in order to access the user's account. A common MFA approach uses bio-based authentication mechanisms based on facial, voice, or fingerprint recognition. Another approach is mechanisms that generate short-lived, one-time access codes. These codes are sent to the user through email, text, or displayed by a smart phone application or physical hardware token.

#### Password management

Users with long-term credentials should be encouraged to adopt secure password management practices. IAM password policies can be used to ensure that user passwords are of sufficient length, uniqueness, and complexity, and that passwords expire on a regular basis. Passwords can be managed using the AWS Management Console, the AWS Command Line Interface (AWS CLI), and the AWS API.

#### Access key management

Access keys are long-term credentials for an IAM user or the AWS account root user. Access keys consist of an access key ID and a secret access key. The access key ID and secret access key must be used together to authenticate user requests. Access key IDs and secret access keys should be stored in a secure location and updated when needed, such as when an employee leaves your organization. The AWS Management Console, AWS CLI, and AWS API can be used to manage access keys.

---

### Federated identity concepts

With federated identity management, you can manage your application user identities in an external system outside of AWS. This approach grants users who sign in from those external systems access to your AWS resources using temporary credentials. AWS supports two standards for identity federation, both of which store identity information outside of AWS: **SAML 2.0** and **OpenID Connect (OIDC)**.

#### Federated identity using SAML 2.0

All AWS services used to support temporary credential management support the SAML 2.0 open standard. SAML allows **Microsoft Active Directory (Microsoft AD)** or other enterprise **identity providers (IdPs)** to authenticate users using their own internal systems. After authentication, the users gain access to AWS resources using temporary credentials. In some cases, the users might have a **single sign-on** experience. Under single sign-on, you can authenticate users using your organization's on-premises network, and then provide those users access to AWS. Single sign-on does not require you to create new AWS identities for these users, or require the users to sign in with AWS credentials.

#### Federated identity using OIDC

External systems authenticating users can also reside with trusted third-party IdPs such as social identity providers like Facebook and Google. Amazon also offers IdP services for customers who have user accounts on Amazon.com using the "Login with Amazon" service. These companies are part of the OIDC federation. The OIDC federation is a group of third-party identity providers who agree upon a set of protocols and standards related to how they manage user credentials. Because they all follow the same protocols and standards, identity providers trust each other to authenticate users. Federated identity providers do not release full login information to external users. Instead, they supply some identifying attributes that lets your application know that a user has been properly authenticated. By using federated identity management, you can accept the external authentication and skip authenticating application users yourself. AWS services used to support temporary credential management support OIDC federation for login with OIDC-compatible identity providers.

---

### AWS services for managing temporary credentials

Because of the their short-term nature, temporary credential management requires mechanisms to generate, deliver, and expire the credentials. IAM Identity Center and Amazon Cognito are two services that can be used for temporary credential management.

#### IAM Identity Center

IAM Identity Center is designed for enterprise-level identity management and federated access to AWS resources. You can centrally manage access to multiple AWS accounts and cloud resources using existing corporate identities. IAM Identity Center supports Microsoft AD and other identity providers that support the SAML 2.0 or OIDC standards.

IAM Identity Center is particularly useful for organizations that need to manage access for a large number of employees or contractors across multiple AWS accounts and applications. It acts as a broker between your corporate identity provider and AWS, providing access to AWS resources without the need for separate AWS credentials.

When a user authenticates with the corporate identity provider, IAM Identity Center can generate temporary AWS security credentials on behalf of the user. These credentials consist of an access key, a secret key, and a session token.

The temporary credentials can be configured with specific permissions and a limited lifespan. Applications use these temporary credentials to access AWS resources without needing to manage long-term AWS credentials.

IAM Identity Center uses the **Identity Store** feature as the central repository for storing and managing user identities and their associated attributes. The Identity Store acts as a directory service that integrates with existing corporate identity providers, such as Microsoft AD or third-party SAML 2.0 or OIDC identity providers.

IAM Identity Center is responsible for managing access to AWS resources based on the identities stored in the Identity Store. It acts as a broker between the connected identity providers and AWS, enabling seamless access to AWS resources without the need for separate AWS credentials. This approach streamlines the management of access to AWS resources across multiple accounts and applications. This ensures that only authorized users with the appropriate permissions can access the required resources.

#### Amazon Cognito

Amazon Cognito is a user identity and data synchronization service primarily focused on mobile and web applications. It provides user sign-up, sign-in, and access control capabilities, in addition to user data synchronization across devices. Amazon Cognito supports various authentication methods, including social identity providers. Amazon Cognito also supports SAML identity providers and custom user pools with built-in user management features.

Amazon Cognito provides temporary AWS credentials through its **Amazon Cognito identity pools** feature. When a user authenticates with Amazon Cognito, the service generates temporary AWS credentials based on the configured identity pool and associated IAM roles. These temporary credentials can be used by the application to access AWS resources on behalf of the authenticated user.

1. When a customer starts the app on their mobile device, the app asks the user to sign in and authenticate with Amazon. The app uses Amazon Cognito API operations to exchange the Amazon ID token for an Amazon Cognito token.
2. Amazon Cognito makes the exchange and requests temporary security credentials from AWS STS with the **AssumeRoleWithWebIdentity** API, passing the Amazon Cognito token for the temporary credentials. The role associated with the temporary security credentials and its assigned policy determine what can be accessed.
3. The authentication process happens seamlessly in the background, and the user is able to play your game in a secure way.

---

#### Choosing a service based on use case

Choosing between IAM Identity Center and Amazon Cognito depends on your specific requirements, your application type, and the level of control you need over the authentication and authorization processes. The following table contrasts the two services and recommended use cases for each.

| Service | Use case |
| ------- | -------- |
| IAM Identity Center | Managing federated access to AWS resources for corporate users or employees. Specifically, in enterprise environments with existing identity providers. |
| Amazon Cognito | User authentication and authorization mechanisms in mobile or web applications. Specifically, when you need to support various authentication methods such as social logins or custom user pools, and synchronize user data across devices. |

---

### [Lab: Implementing an OIDC IdP for Enhanced Security and Identity](./labs/W010Lab1ImplementingOidcIdp.md)

In this lab, you will need to secure a web application by using temporary credentials. To do this, you will set up an OIDC provider, then update the application with the proper code to receive a JSON Web Token (JWT) for access. Specifically, you will perform these activities during the lab:

* Create an OIDC identity provider using the AWS CLI.
* Review the role and trust policy.
* Update the application with OIDC information.
* Test the credentials with the application.

---

## The Role of AWS Security Token Service for Temporary Credentials

### AWS STS supports AWS identity services

The IAM Identity Center and Amazon Cognito APIs can be used to retrieve the temporary credentials for authenticated federated users. In this configuration, IAM Identity Center and Amazon Cognito act as an IdP and can be configured to establish trust relationships with external identity IdPs that support SAML or OIDC protocols. When a user authenticates with the external IdP, IAM Identity Center or Amazon Cognito receives a SAML assertion or OIDC token containing the user's identity information. This information allows AWS STS to create the user's temporary credentials.

AWS STS acts as a secure and centralized service for issuing temporary credentials with limited permissions and lifetimes.

This approach follows the principle of least privilege and reduces the risk of exposing long-term credentials, enhancing the overall security of the application.

AWS STS also provides additional features, like federated user sessions, cross-account access, and multi-factor authentication support.

#### AWS STS and IAM Identity Center

When a user authenticates with a corporate identity provider using IAM Identity Center, AWS STS generates temporary AWS security credentials on behalf of the authenticated user.

Those temporary credentials consist of an access key, a secret key, and a session token.

The credentials are issued with specific permissions and a limited lifespan. These temporary credentials are used by the application to access AWS resources on behalf of the authenticated user.

#### AWS STS and Amazon Cognito

Amazon Cognito also relies on AWS STS to issue temporary credentials for authenticated users.

When a user authenticates with Amazon Cognito through a social identity provider, Amazon Cognito uses AWS STS to obtain temporary AWS credentials. Amazon Cognito uses the same process to authenticate users based on a SAML identity provider or a custom user pool. 

These temporary credentials are based on the configured identity pool and the pool's associated IAM roles. The temporary credentials are used by the application to access AWS resources on behalf of the authenticated user.

---

### Using AWS STS for temporary credentials

AWS STS also supports direct authentication of federated users without using IAM Identity Center or Amazon Cognito. For example, AWS STS can provide application users with temporary credentials using single sign-on and SAML 2.0 from an on-premises identity management system like Microsoft AD. Alternatively, you can provide temporary credentials using the protocols and standards established by OIDC federation identity providers.

---

### Configuring AWS STS for temporary credentials

Some initial configuration steps must be completed before federated users can request and use temporary credentials for an application.

![Diagram of setup steps for configuring a SAML or OIDC request for temporary credentials.](./images/W01Img010IamStsWithExternalIdentityProviders.png)

1. **Create a mobile or web client**

    Create a mobile or web application client using the identity provider you wish to use for authentication.

    IAM supports identity providers compatible with OIDC or SAML 2.0.

2. **Create an identity provider in IAM**

    ![Screen shot of IAM Console with Identity providers and Add provider button selected from Access management menu.](./images/W01Img020CreateIdentityProvider.png)

    In the IAM console, add the identity provider that corresponds to the provider you will be using for the application.

3. **Create an IAM role**

    ![Screen shot of IAM Console with Web Identity and SAML 2.0 options highlighted on the Select Trusted Identity page.](./images/W01Img030CreateIamRole.png)

    Create a web identity IAM role or a SAML 2.0 federation IAM role.

4. **Create a trust policy**

    Give your IAM role a trust policy that will allow AWS STS to assume the role using

      * **sts:AssumeRoleWithWebIdentity**
      * **sts:AssumeRoleWithSAML**

5. **Create an IAM policy**

    Add an IAM policy to the IAM role you created. The policy is used to grant permissions for the actions you want the application user to take. For example, if you would like the user to be able to insert records into an Amazon DynamoDB table, then give the role **dynamodb:PutItem** permission on that table.

6. **Use permissions**

    The IAM policy and its associated permissions will be temporarily passed to an application user.

---

When configuring AWS STS for use with temporary credentials, **trust policies** can be used to define the trusted entities that are allowed to request temporary security credentials. These trust policies specify the SAML or OIDC identity providers that are trusted to authenticate users and request temporary credentials on their behalf. Additionally, trust policies can include conditions that further restrict the permissions granted to the temporary credentials, such as limiting the AWS services or actions that can be accessed.

---

### How AWS STS uses temporary credentials

After you have completed the initial configuration of IAM and AWS STS for federated authentication, you can get the token ID from the identity provider. Then, you can request the required AWS STS credentials for your application.

![Steps for passing SAML identity information to AWS STS to obtain temporary credentials.](./images/W01Img040SamlStsCooperation.png)

1. **Get token ID**

    The user logs into the application using the OIDC or SAML 2.0 identify provider.

    The application raises an event that sends an object to the application that contains the access token returned by the identify provider.

2. **IAM authenticates**

    The application provides the web identity or SAML token to obtain temporary credentials from AWS STS.

    To do this, the application uses an assume role function, either

      * **assume-role-with-web-identity** or
      * **assume-role-with-saml**.

3. **Application action**

    The application then uses the AWS STS temporary security credentials — **access key ID**, **secret access key**, and **session token** — to access application resources.

    The security credentials are authenticated and the actions are authorized.

---

### Requesting temporary credentials using AWS STS

As with all other AWS services, you use APIs to interact with AWS STS. The APIs commonly used for requesting temporary security credentials from AWS STS are AssumeRole, GetSessionToken, AssumeRoleWithSAML, and AssumeRoleWithWebIdentity.

#### AssumeRoleWithSAML API request

An **AssumeRoleWithSAML** request to the AWS STS API returns a set of temporary security credentials for users who have been authenticated externally through a SAML authentication response. This operation provides a mechanism for associating an on-premises enterprise identity store to role-based AWS access without user-specific credentials or configuration.

The following sample code includes most of the components available when making the **AssumeRoleWithSAML** request to the AWS STS service to assume a role using SAML authentication.

![Sample AssumeRoleWithSAML request to AWS STS API.](./images/W01Img050AssumeRoleWithSamlRequestToSts.png)

```bash
https://sts.amazonaws.com/
?Version=2011-06-15
&Action=AssumeRoleWithSAML
&RoleArn=arn:aws:iam::123456789012:role/TestSaml
&PrincipalArn=arn:aws:iam::123456789012:saml-provider/SAML-test 
&SAMLAssertion=VERYLONGENCODEDASSERTIONEXAMPLExzYW1sOkF1ZGllbmNl
PmJsYW5rPC9zYW1sOkF1ZGllbmNlPjwvc2FtbDpBdWRpZW5jZVJlc3RyaWN0aW9u
Pjwvc2FtbDpDb25kaXRpb25zPjxzYW1sOlN1YmplY3Q+PHNhbWw6TmFtZUlEIEZv
cm1hdD0idXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6Mi4wOm5hbWVpZC1mb3JtYXQ6
dHJhbnNpZW50Ij5TYW1sRXhhbXBsZTwvc2FtbDpOYW1lSUQ+PHNhbWw6U3ViamVj
dENvbmZpcm1hdGlvbiBNZXRob2Q9InVybjpvYXNpczpuYW1lczp0YzpTQU1MOjIu
MDpjbTpiZWFyZXIiPjxzYW1sOlN1YmplY3RDb25maXJtYXRpb25EYXRhIE5vdE9u
T3JBZnRlcj0iMjAxOS0xMS0wMVQyMDoyNTowNS4xNDVaIiBSZWNpcGllbnQ9Imh0
dHBzOi8vc2lnbmluLmF3cy5hbWF6b24uY29tL3NhbWwiLz48L3NhbWw6U3ViamVj
dENvbmZpcm1hdGlvbj48L3NhbWw6U3ViamVjdD48c2FtbDpBdXRoblN0YXRlbWVu
dCBBdXRoPD94bWwgdmpSZXNwb25zZT4=
&AUTHPARAMS
```

* Line 4 of the sample code shows the **RoleArn** parameter being passed, which specifies the Amazon Resource Name (ARN) of the **TestSaml** role that the caller is assuming.
* Line 5 uses the parameter **PrincipalArn** to specify ARN of the SAML provider within IAM that describes the IdP called **SAML-test**.
* Lines 6 through 16 use the **SAMLAssertion** parameter to pass the base64 encoded SAML authentication response provided by an on-premises identity store, such as Microsoft AD.

The SAML assertion is an XML document that contains security information about the user. SAML assertions are issued by an IdP and consumed by AWS to grant access to protected resources based on the information contained within the assertion.

---

#### The AssumeRoleWithSAML API response

A request to AssumeRoleWithSAML returns a set of temporary security credentials that consist of an access key ID, a secret access key, and a security token. Applications can use these temporary security credentials to sign calls to AWS services.

![Sample response from AssumeRoleWithSAML request to AWS STS API.](./images/W01Img052AssumeRoleWithSamlResponseFromSts.png)

```xml
<AssumeRoleWithSAMLResponse xmlns="https://sts.amazonaws.com/doc/2011-06-15/">
    <AssumeRoleWithSAMLResult>
        <Issuer> https://integ.example.com/idp/shibboleth</Issuer>
        <AssumedRoleUser>
            <Arn>arn:aws:sts::123456789012:assumed-role/TestSaml</Arn>
            <AssumedRoleId>ARO456EXAMPLE789:TestSaml</AssumedRoleId>
        </AssumedRoleUser>
        <Credentials>
            <AccessKeyId>ASIAV3ZUEFP6EXAMPLE</AccessKeyId>
            <SecretAccessKey>8P+SQvWIuLnKhh8d++jpw0nNmQRBZvNEXAMPLEKEY</SecretAccessKey>
            <SessionToken> IQoJb3JpZ2luX2VjEOz////////////////////wEXAMPLEtMSJHMEUCIDoKK3JH9uG
                QE1z0sINr5M4jk+Na8KHDcCYRVjJCZEvOAiEA3OvJGtw1EcViOleS2vhs8VdCKFJQWP
                QrmGdeehM4IC1NtBmUpp2wUE8phUZampKsburEDy0KPkyQDYwT7WZ0wq5VSXDvp75YU
                9HFvlRd8Tx6q6fE8YQcHNVXAkiY9q6d+xo0rKwT38xVqr7ZD0u0iPPkUL64lIZbqBAz
                +scqKmlzm8FDrypNC9Yjc8fPOLn9FX9KSYvKTr4rvx3iSIlTJabIQwj2ICCR/oLxBA== </SessionToken>
            <Expiration>2019-11-01T20:26:47Z</Expiration>
        </Credentials>
        <Audience>https://signin.aws.amazon.com/saml</Audience>
        <SubjectType>transient</SubjectType>
        <PackedPolicySize>6</PackedPolicySize>
        <NameQualifier>SbdGOnUkh1i4+EXAMPLExL/jEvs=</NameQualifier>
        <SourceIdentity>SourceIdentityValue</SourceIdentity>
        <Subject>SamlExample</Subject>
    </AssumeRoleWithSAMLResult>
    <ResponseMetadata>
        <RequestId>c6104cbe-af31-11e0-8154-cbc7ccf896c7</RequestId>
    </ResponseMetadata>
</AssumeRoleWithSAMLResponse>
```

1. **Issuer**

    This parameter contains the address of the IdP that provided the SAML assertion that was passed to the API.

2. **ARN**

    This parameter contains the ARN of the TestSaml role that the caller is assuming.

3. **AssumedRoleID**

    This parameter contains the unique identifier that contains the role ID and the role session name of the TestSaml role that the caller is assuming.

4. **AccessKeyID**

    This parameter contains the the access key ID that identifies the temporary security credentials.

5. **SecretAccessKey**

    This parameter contains the secret access key that can be used to sign requests.

6. **SessionToken**

    This parameter contains the token the caller must pass to the service API to use the temporary credentials.

---

#### AssumeRoleWithWebIdentity API request

The AssumeRoleWithWebIdentity returns a set of temporary security credentials for users who have been authenticated using a web IdP. OAuth 2.0 IdPs like Login with Amazon and social identity providers are common examples.

You can use JSON Web Tokens (JWTs) as a part of OIDC and OAuth 2.0 frameworks to restrict client access to your APIs. If you configure a JWT authorizer for a route of your API, Amazon API Gateway validates the JWTs that clients submit with API requests. API Gateway allows or denies requests based on this token validation.

The following sample code includes most of the components available when making the AssumeRoleWithWebIdentity request to the AWS STS service to assume a role using IdP authentication.

![AUsing AssumeRoleWithWebIdentity for SSO authentication.](./images/W01Img060AssumeRoleWithWebIdentityRequestToSts.png)

```bash
https://sts.amazonaws.com/
?Action=AssumeRoleWithWebIdentity
&DurationSeconds=3600
&PolicyArns.member.1.arn=arn:aws:iam::123456789012:policy/webidentitydemopolicy1
&PolicyArns.member.2.arn=arn:aws:iam::123456789012:policy/webidentitydemopolicy2
&ProviderId=www.amazon.com
&RoleSessionName=app1
&RoleArn=arn:aws:iam::123456789012:role/FederatedWebIdentityRole
&WebIdentityToken=Atza%7CIQEBLjAsAhRFiXuWpUXuRvQ9PZL3GMFcYevydwIUFAHZwXZXX
XXXXXXJnrulxKDHwy87oGKPznh0D6bEQZTSCzyoCtL_8S07pLpr0zMbn6w1lfVZKNTBdDansFB
mtGnIsIapjI6xKR02Yc_2bQ8LZbUXSGm6Ry6_BG7PrtLZtj_dfCTj92xNGed-CrKqjG7nPBjNI
L016GGvuS5gSvPRUxWES3VYfm1wl7WTI7jn-Pcb6M-buCgHhFOzTQxod27L9CqnOLio7N3gZAG
psp6n1-AJBOCJckcyXe2c6uD0srOJeZlKUm2eTDVMf8IehDVI0r1QOnTV6KzzAI3OY87Vd_cVMQ
&Version=2011-06-15
```

* Line 3 of the sample code shows the **DurationSeconds** parameter being passed with a value of 3600 seconds.
* Lines 4 and 5 use the **PolicyArns.member.n.arn** parameter to pass the list of IAM policies to be attached to the assumed role (**webidentitydemopolicy1** and **webidentitydemopolicy2**).
* The **ProviderId** parameter passed on Line 6  contains the name of the IdP that authenticated the user.
* Line 7 uses the **RoleSessionName** parameter to pass the name or identifier that is associated with the user who is using your application. The **RoleArn** parameter on Line 8 contains the ARN of the IAM role the caller is assuming. Finally, Lines 9-13 contain the value for the **WebIdentityToken** parameter. WebIdentityToken contains the OpenID Connect ID token that was provided by the IdP. Before your application makes an **AssumeRoleWithWebIdentity** call, the application must get this token by authenticating the application user with an IdP.

---

#### The AssumeRoleWithWebIdentity API response

The temporary security credentials returned by **AssumeRoleWithWebIdentity** consist of an access key ID, a secret access key, and a security token. Applications can use these temporary security credentials to sign calls to AWS service API operations.

![Sample response from AssumeRoleWithWebIdentity request to AWS STS API.](./images/W01Img062AssumeRoleWithWebIdentityResponseFromSts.png)

```xml
<AssumeRoleWithWebIdentityResponse xmlns="https://sts.amazonaws.com/doc/2011-06-15/">
  <AssumeRoleWithWebIdentityResult>
    <SubjectFromWebIdentityToken>amzn1.account.AF6RHO7KZU5XRVQJGXK6HB56KR2A</SubjectFromWebIdentityToken>
    <Audience>client.5498841531868486423.1548@apps.example.com</Audience>
    <AssumedRoleUser>
      <Arn>arn:aws:sts::123456789012:assumed-role/FederatedWebIdentityRole/app1</Arn>
      <AssumedRoleId>AROACLKWSDQRAOEXAMPLE:app1</AssumedRoleId>
    </AssumedRoleUser>
    <Credentials>
      <SessionToken>AQoDYXdzEE0a8ANXXXXXXXXNO1ewxE5TijQyp+IEXAMPLE</SessionToken>
      <SecretAccessKey>wJalrXUtnFEMI/K7MDENG/bPxRfiCYzEXAMPLEKEY</SecretAccessKey>
      <Expiration>2014-10-24T23:00:23Z</Expiration>
      <AccessKeyId>ASgeIAIOSFODNN7EXAMPLE</AccessKeyId>
    </Credentials>
    <SourceIdentity>SourceIdentityValue</SourceIdentity>
    <Provider>www.amazon.com</Provider>
  </AssumeRoleWithWebIdentityResult>
  <ResponseMetadata>
    <RequestId>ad4156e9-bce1-11e2-82e6-6b6efEXAMPLE</RequestId>
  </ResponseMetadata>
</AssumeRoleWithWebIdentityResponse>
```

1. **SubjectFromWebIdentityToken**

    This parameter is the unique user identifier that is returned by the IdP.

2. **Arn**

    This parameter contains the ARN of the IAM role that the user is assuming.

3. **AssumedRoleId**

    This parameter contains the unique identifier that contains the role ID and the role session name of the role that the caller is assuming.

4. **SessionToken**

    This parameter contains the token the caller must pass to the service API to use the temporary credentials.

5. **SecretAccessKey**

    This parameter contains the secret access key that can be used to sign requests.

6. **Expiration**

    This parameter holds the date, after which, the identity token is no longer valid.

7. **AccessKeyId**

    This parameter contains the access key ID that identifies the temporary security credentials.

8. **Provider**

    Name of the IdP who authenticated the user.

---

### Switching roles and credentials

The **AssumeRole** and **GetSessionToken** APIs are used when you already have AWS credentials but need to swap those credentials out with those of another role. The following sections show examples of how to use these APIs.

#### The AssumeRole API request

When an application or service needs to access AWS resources on behalf of an IAM user, it can call the AWS STS AssumeRole API operation. This operation returns temporary security credentials in the form of an access key ID, a secret access key, and a session token with the permissions defined by the IAM role specified in the request. These temporary credentials have a limited lifespan, typically ranging from 15 minutes to 36 hours, after which they expire and must be renewed. 

Typically, you use the **AssumeRole** request from AWS STS service within your account or for cross-account access. When you own multiple AWS accounts, you might need to access resources in both of those accounts. Instead of creating long-term credentials in each account to access those resources, you can create one set of long-term credentials in one account. Then, you can use temporary security credentials to access all the other accounts by assuming roles in those accounts.

The following sample code shows many of the components available when making the AssumeRole request to the AWS STS service.

![AssumeRole request to the AWS STS service](./images/W01Img070AssumeRoleRequestToSts.png)

```bash
https://sts.amazonaws.com/
?Version=2011-06-15
&Action=AssumeRole
&RoleSessionName=testAR
&RoleArn=arn:aws:iam::123456789012:role/demo
&PolicyArns.member.1.arn=arn:aws:iam::123456789012:policy/demopolicy1
&PolicyArns.member.2.arn=arn:aws:iam::123456789012:policy/demopolicy2
&Policy={"Version":"2012-10-17","Statement":[{"Sid":"Stmt1",
"Effect":"Allow","Action":"s3:*","Resource":"*"}]}
&DurationSeconds=3600
&Tags.member.1.Key=Project
&Tags.member.1.Value=Pegasus
&Tags.member.2.Key=Team
&Tags.member.2.Value=Engineering
&Tags.member.3.Key=Cost-Center
&Tags.member.3.Value=12345
&TransitiveTagKeys.member.1=Project
&TransitiveTagKeys.member.2=Cost-Center
&ExternalId=123ABC
&SourceIdentity=Alice
&AUTHPARAMS
```

1. **RoleSessionName**

    **Required**. This parameter identifies the assumed role session. Use the role session name to uniquely identify a session when different principals assume the same role for different reasons. In cross-account scenarios, the account that owns the role can see and log the session role name. This example uses **testAR** for the session name.

2. **RoleARN**

    **Required**. This parameter is the ARN of the role that is being assumed. This example is assuming a role called **demo**.

3. **PolicyArns.member.n.arn**

    **Optional**. This parameter includes the ARNs of the IAM managed policies. The policies must exist in the same AWS account as the role. You can provide up to 10 managed policy ARNs. This example uses two policy ARNs: **demopolicy1** and **demopolicy2**.

4. **Policy**

    **Optional**. This parameter is an IAM policy that is used as an inline policy. Inline policies, as opposed to managed policies, have a one-to-one relationship with the attached role session. This example is attaching a policy that gives the user the ability to perform any operation on Amazon Simple Storage Service (Amazon S3) resources.

5. **Duration**

    **Optional**. This parameter sets the duration of role session in seconds. This example allows the role to be assumed for **3600 seconds** (60 minutes).

6. **Tags.member.n.Key/Value**

    **Optional**. This parameter is a list of session tags that you want to pass while assuming the role. Each session tag consists of a key name and an associated value. You can pass up to 50 session tags. The plaintext session tag keys can’t exceed 128 characters, and the values can’t exceed 256 characters. This example has three key-value pairs: **Project:Pegasus**, **Team:Engineering**, and **Cost-Center:12345**.

7. **TransitiveTagKeys.member.n**

    **Optional**. This parameter is a list of key-value session tags that you want to be passable to subsequent sessions in the role chain. This example is making the key-value pairs **Project:Pegasus** and **Cost-Center:12345** transitive, so they can be passed to subsequent sessions.

8. **ExternalID**

    **Optional**. This parameter is a unique identifier that might be required when you assume a role in another account. If the administrator of the account to which the role belongs provided you with an external ID, then provide that value using the ExternalID parameter. This example is passing an ExternalID of **123ABC**.

9. **SourceIdentity**

    **Optional**. This is the source identity specified by the principal that is calling the AssumeRole operation. You can require users to specify a source identity when they assume a role. You can use source identity information in AWS CloudTrail logs to determine who took actions with a role. This example is passing a SourceIdentity of **Alice**.

---

#### The AssumeRole API response

A request to AssumeRole returns a set of temporary security credentials for users who have been authorized by AWS STS.

![Sample of the responses returned by a AssumeRole API call.](./images/W01Img072AssumeRoleResponseFromSts.png)

```xml
<AssumeRoleResponse xmlns="https://sts.amazonaws.com/doc/2011-06-15/">
  <AssumeRoleResult>
  <SourceIdentity>Alice</SourceIdentity>
    <AssumedRoleUser>
      <Arn>arn:aws:sts::123456789012:assumed-role/demo/TestAR</Arn>
      <AssumedRoleId>ARO123EXAMPLE123:TestAR</AssumedRoleId>
    </AssumedRoleUser>
    <Credentials>
      <AccessKeyId>ASIAIOSFODNN7EXAMPLE</AccessKeyId>
      <SecretAccessKey>wJalrXUtnFEMI/K7MDENG/bPxRfiCYzEXAMPLEKEY</SecretAccessKey>
      <SessionToken>
       AQoDYXdzEPT//////////wEXAMPLEtc764bNrC9SAPBSM22wDOk4x4HIZ8j4FZTwdQW
       LWsKWHGBuFqwAeMicRXmxfpSPfIeoIYRqTflfKD8YUuwthAx7mSEI/qkPpKPi/kMcGd
       QrmGdeehM4IC1NtBmUpp2wUE8phUZampKsburEDy0KPkyQDYwT7WZ0wq5VSXDvp75YU
       9HFvlRd8Tx6q6fE8YQcHNVXAkiY9q6d+xo0rKwT38xVqr7ZD0u0iPPkUL64lIZbqBAz
       +scqKmlzm8FDrypNC9Yjc8fPOLn9FX9KSYvKTr4rvx3iSIlTJabIQwj2ICCR/oLxBA==
      </SessionToken>
      <Expiration>2019-11-09T13:34:41Z</Expiration>
    </Credentials>
    <PackedPolicySize>6</PackedPolicySize>
  </AssumeRoleResult>
  <ResponseMetadata>
    <RequestId>c6104cbe-af31-11e0-8154-cbc7ccf896c7</RequestId>
  </ResponseMetadata>
</AssumeRoleResponse>
```

1. **AssumeRoleUser**

    The AssumeRoleUser section of the request response contains the ARN of the temporary credentials that were issued and the unique identifier of the role ID.

2. **Credentials**

    This section of the request response contains the temporary security credentials, consisting of an access key ID, a secret access key, and the security (or session) token.

3. **PackedPolicySize**

    The section of the request response is a percentage value. This value indicates the packed size of the session policies and session tags combined with the request. The request fails if the packed size is greater than 100 percent, which means the policies and tags exceeded the allowed space.

---

### Working with AWS STS for temporary credentials

The AWS security token contains the temporary security credentials that allow human users or systems to call AWS APIs via IAM roles.

The security token is made up of an **access key ID**, which identifies the temporary security credentials; the **secret access key**, which is used to sign API calls; and the **session token**, which must be passed along to the service API that is being accessed in order to use the assigned temporary credentials.

The AWS Security Token Service, or AWS STS, generates security tokens. When a **trusted AWS identity** assumes a role, the AssumeRole API call is made to AWS STS for the temporary security credentials.

One of the use cases for the AssumeRole API is to provide identities access to AWS resources that only other identities have access to. These resources can be located in the same account or in another account, which is known as cross-account delegation.

To provide cross-account access:

* A trust policy must first exist between the two accounts.
* The trusting account owns the resource to be accessed,
* The trusted account contains the users who need access to the resource. This is achieved by the trust policy associated with the IAM role.

---

For example, here we have an analyst from Account A who needs to assume a role in Account B to access a resource that another analyst owns.

1. The AssumeRole call is made to AWS STS
2. AWS STS in turn checks with the IAM role in Account B if a trust policy exists and if the user has the right permissions.
3. Once authorized, AWS STS sends the user from Account A the temporary security credentials required to access the resource.

---

The AssumeRole API provides a user the ability to switch their IAM role such that they have different or increased access only provided by another role. This allows you apply the principle of least privilege.

---

### Using AWS STS with MFA

You can also include MFA information when making an AssumeRole request using the SerialNumber and TokenCode parameters. Under this scenario, the trust policy of the role being assumed will also include a condition that tests for proper MFA credentials being based.

The **GetSessionToken** request to the AWS STS service is used to authenticate an MFA user. The GetSessionToken operation must be called by using the long-term AWS security credentials of an IAM user.

A request to **GetSessionToken** begins with passing two parameters to the API: **SerialNumber** and **TokenCode**. SerialNumber is the unique identifier associated with an individual user's MFA device. TokenCode is the code displayed on the MFA device at the time the two parameters are passed to GetSessionToken. MFA token codes are typically good for one minute, after which a new token code is generated.

![Using GetSessionToken for a specified MFA device](./images/W01Img080UsingGetSessionTokenForMfaDevice.png)

```bash
https://sts.amazonaws.com/
?Version=2011-06-15
&Action=GetSessionToken
&Duration=3600
&Tags.member.1.Key=Project
&Tags.member.1.Value=Unicorn
&Tags.member.2.Key=Cost-Center
&Tags.member.2.Value=101
&SerialNumber=ABCD1234EFGH5678WXYZ
&TokenCode=101165
&AUTHPARAMS
```

* The code sample shown here makes an API call to the AWS STS service to request a session token. The SerialNumber of the user's MFA device shown on line 9 is **ABCD1234EFGH5678WXYZ**. The generated MFA token code is shown on line 10, is **101165**.
* Line 4 of the sample code shows the **DurationSeconds** parameter being passed with a value of 3600. This specifies how many seconds the credentials should remain valid. Acceptable durations for IAM user sessions range from 900 seconds (15 minutes) to 129,600 seconds (36 hours), with 43,200 seconds (12 hours) as the default.
* Lines 5 though 8 use the **Tags.member.n** parameter to pass tags to the AWS STS API using key-value pairs. In this example, tags identify this session as belonging to **Project Unicorn**, and **Cost-Center 101**.

---

#### The GetSessionToken API response

A request to GetSessionToken returns a set of temporary security credentials for users who have been authorized by AWS STS using MFA.

![Sample responses returned by a call to the GetSessionToken API.](./images/W01Img082GetSessionTokenResponse.png)

```xml
<GetSessionTokenResponse xmlns="https://sts.amazonaws.com/doc/2011-06-15/">
  <GetSessionTokenResult>
    <Credentials>
      <SessionToken>
       AQoEXAMPLEH4aoAH0gNCAPyJxz4BlCFFxWNE1OPTgk5TthT+FvwqnKwRcOIfrRh3c/L
       To6UDdyJwOOvEVPvLXCrrrUtdnniCEXAMPLE/IvU1dYUg2RVAJBanLiHb4IgRmpRV3z
       rkuWJOgQs8IZZaIv2BXIa2R4OlgkBN9bkUDNCJiBeb/AXlzBBko7b15fjrBs2+cTQtp
       Z3CYWFXG8C5zqx37wnOE49mRl/+OtkIKGO7fAE
      </SessionToken>
      <SecretAccessKey>
      wJalrXUtnFEMI/K7MDENG/bPxRfiCYzEXAMPLEKEY
      </SecretAccessKey>
      <Expiration>2011-07-11T19:55:29.611Z</Expiration>
      <AccessKeyId>ASIAIOSFODNN7EXAMPLE</AccessKeyId>
    </Credentials>
  </GetSessionTokenResult>
  <ResponseMetadata>
    <RequestId>58c5dbae-abef-11e0-8cfe-09039844ac7d</RequestId>
  </ResponseMetadata>
</GetSessionTokenResponse>
```

1. **Session token**

    This long string of characters is the temporary session token that was generated by AWS STS based on the MFA credentials supplied.

2. **SecretAccessKey**

    Access keys consist of an access key ID and a secret access key. You must use both the access key ID and secret access key together to authenticate your requests. This response is the **SecretAccessKey** for the MFA user.

3. **AccessKeyID**

    Access keys consist of an access key ID and a secret access key. You must use both the access key ID and secret access key together to authenticate your requests. This response is the **AccessKeyID** for the MFA user.

---

## Using AWS CLI and AWS SDK with Temporary Credentials

API calls to AWS STS can also be made using the AWS CLI and AWS SDK. When you run commands using a profile that specifies an IAM role, the source profile's credentials are used request temporary credentials for that role by calling AWS STS. This process of retrieving and then using temporary credentials for a role is referred to as assuming a role.

### Trust policy for assuming a role

To assume a role using AWS CLI or AWS SDK, the role must have a trust relationship that allows the user in the source profile to use the role. The following trust policy grants permission to assume or take on a particular role within the AWS environment.

### Trust policy for all users in an AWS account

![Trust policy that allows users to assume a different role.](./images/W01Img090TrustPolicyForAllUsers.png)

* Line 5 of the code, **"Effect": "Allow"** grants permission for the specified actions to be performed.
* Line 6 identifies the **Principal** (entity) that the policy applies to.
* In this case, Line 7 shows the principal is AWS account ID **123456789012**.
* Line 9, **"Action": "sts:AssumeRole"** specifies the action that is allowed by the policy.

---

In summary, this trust policy grants the principal for AWS account ID **123456789012** the ability to to assume a role.

---

It's important to note that this trust policy alone doesn't grant any actual permissions or access to AWS resources. It allows the specified account to assume a role. The permissions and access associated with the target role are defined separately, using a permissions policy.

---

### Permissions policy for assuming a role

![Policy for assuming the MarketingAdmin role.](./images/W01Img092PermissionsPolicyForAssumingRole.png)

This policy grants permission to assume a role called **MarketingAdmin** within the AWS account with the ID **123456789012**.

* Line 5 of the code, **"Effect": "Allow"**, grants permission for the specified actions to be performed.
* Line 6, **"Action": "sts:AssumeRole"**, specifies the action that is allowed by the policy—assuming a specific role within AWS.
* Line 7, **"Resource": arn:aws:iam::123456789012:role/MarketingAdmin** identifies the ARN of the specific role that can be assumed (MarketingAdmin).

After it is created, any IAM user or group attached to this policy will be able to assume the MarketingAdmin role.

---

### Working with MFA using AWS CLI and AWS SDK

To use MFA with the AWS CLI or AWS SDK, you can modify the trust relationship on the IAM role to require MFA. An example of the following revised trust policy allows a specific IAM user (cli-user) to assume a role, but only if MFA is enabled for that user. This prevents anyone from using the role without first authenticating by using MFA.

![Sample trust policy code that includes MFA requirement for a user named cli-user.](./images/W01Img094CliAddingMfaPolicy.png)

* Line 6 **"Effect": "Allow"** grants permission for the specified actions to be performed.
* Line 7, **"Principal": { "AWS": "arn:aws:iam::123456789012:user/cli-user" }** identifies the principal (entity) that the policy applies to.
* Line 8, **"Action": "sts:AssumeRole"** specifies the action that is allowed by the policy—the IAM user cli-user is allowed to assume a specific role within AWS.
* Line 9 adds the condition that the user assuming the role must have previously authenticated using MFA, by setting the **multifactorAuthPresent** Boolean value to true.

---

Whether with or without MFA, you don't need to have additional permissions to run the AWS CLI or AWS SDK commands using the assumed role profile. Instead, the permissions to run the command come from those attached to the assumed role. You attach permission policies to the role to specify which actions can be performed against which AWS resources.

---

### Assuming a role using AWS CLI

Now that you have the role profile, role permissions, role trust relationship, and user permissions correctly configured, you can assume the MarketingAdmin role at the command line. You can do this by invoking the --profile option.

This example calls the Amazon S3 list command (ls) using the permissions attached to the MarketingAdmin role as defined in the previous sections.

![Output from the AWS CLI command: aws s3 ls --profile MarketingAdmin.](./images/W01Img096AssumingProfileUsingCli.png)

![Two AWS CLI commands being issued: aws iam list-mfa-devices and aws s3 ls --profile MFA-profile.](./images/W01Img098PromptingForMfaWhenAssumingRole.png)

If the role you are assuming requires MFA, then the AWS CLI will prompt you to enter the code from your MFA device before assuming the role.

In this example, the user, cli-user, first lists the SerialNumber of their MFA device using the "aws iam list-mfa-devices" command.

Then, AWS prompts you to enter the MFA device's serial number to complete the Amazon S3 list command.

---

### Assuming a role using AWS SDK

The AWS SDK can also interact with temporary credentials by using the **sts_client.assume_role** request in your application code. The Python script shown here uses the sts_client.assume_role request to assume the MarketingAdmin role. Next, the script calls the Amazon S3 list command (ls) to obtain a list of Amazon S3 buckets that are accessible using the permissions attached to the that role.

![Python program that uses AWS SDK to assume the MarketingAdmin role.](./images/W01Img100SdkAssumeMarketingAdminRoleExample.png)

```python
import boto3

# Define the AWS account ID and role name
account_id = '693202236239'
role_name = 'MarketingAdmin'

# Create a Boto3 session
session = boto3.Session()

# Create an STS client
sts_client = session.client('sts')

# Assume the role
assumed_role_object = sts_client.assume_role(
    RoleArn=f"arn:aws:iam::{account_id}:role/{role_name}",
    RoleSessionName="AssumeMarketingAdminRole"
)

# Get the temporary credentials
credentials = assumed_role_object['Credentials']

# Create a new session with the temporary credentials
assumed_role_session = boto3.Session(
    aws_access_key_id=credentials['AccessKeyId'],
    aws_secret_access_key=credentials['SecretAccessKey'],
    aws_session_token=credentials['SessionToken']
)

# Create an S3 client using the assumed role session
s3_client = assumed_role_session.client('s3')

# List all S3 buckets accessible with the MarketingAdmin role
response = s3_client.list_buckets()

# Print the list of S3 buckets
print("S3 Buckets accessible with the MarketingAdmin role:")
for bucket in response['Buckets']:
    print(bucket['Name'])
```

* Line 11 of the sample Python code uses the AWS STS client to create a session that is used to assume the **MarketingAdmin** role using the **sts_client.assume_role** request in lines 14-16.
* The temporary credentials returned by **sts_client.assume_role** are stored in the credentials variable in line 20, then passed to AWS to assume the **MarketingAdmin** role in lines 24-26. 
* The rest of the script includes syntax for listing the Amazon S3 buckets that are accessible using the MarketingAdmin role.

This sample output shows the AssumeRole.py Python script being run from the Windows command line.

The script assumes the MarketingAdmin role, then returns a list of Amazon S3 buckets that are accessible using that role.

#### Using Python script to assume the MarketingAdmin role

![Running the Python script from the Windows command line using: python AssumeRole.py.](./images/W01Img102PyScriptAssumeMarketingAdminRoleExample.png)

---

### Assuming a role with MFA using AWS SDK

Just as with the AWS CLI, the AWS SDK also offers a mechanism for requiring users to connect with MFA credentials before being allowed to assume a role. The following Python script uses the **sts_client.assume_role** request to assume the **MarketingAdmin** role while passing the **serial number** and **code** from the user's MFA device. The script then calls the Amazon S3 list command (ls) to obtain a list of Amazon S3 buckets that are accessible using the permissions attached to the MarketingAdmin role.

![Python program that uses AWS SDK with MFA to assume the MarketingAdmin role](./images/W01Img104SdkAssumeMarketingAdminRoleMfaExample.png)

```python
import boto3

# Define the AWS account ID and role name
account_id = '693202236239'
role_name = 'MarketingAdmin'

# Define the MFA device ARN and MFA code
mfa_device_arn = 'arn:aws:iam::693202236239:mfa/cli-user'
mfa_code = input('Enter the MFA code: ')

# Create a Boto3 session
session = boto3.Session()

# Create an STS client
sts_client = session.client('sts')

# Assume the role with MFA
assumed_role_object = sts_client.assume_role(
    RoleArn=f"arn:aws:iam::{account_id}:role/{role_name}",
    RoleSessionName="AssumeMarketingAdminRole",
    SerialNumber=mfa_device_arn,
    TokenCode=mfa_code
)

# Get the temporary credentials
credentials = assumed_role_object['Credentials']

# Create a new session with the temporary credentials
assumed_role_session = boto3.Session(
    aws_access_key_id=credentials['AccessKeyId'],
    aws_secret_access_key=credentials['SecretAccessKey'],
    aws_session_token=credentials['SessionToken']
)

# Now you can use the assumed_role_session to interact with AWS resources
# with the permissions granted by the MarketingAdmin role
s3_client = assumed_role_session.client('s3')
response = s3_client.list_buckets()

# Print the list of S3 buckets
print("S3 Buckets accessible with the MarketingAdmin role:")
for bucket in response['Buckets']:
    print(bucket['Name'])
```

* Line 8 defines the ARN of the MFA device for the cli-user IAM user. The Python script uses this value, and the MFA code supplied by the user when prompted, to assume the MarketingAdmin role using sts_client.assume_role in lines 19-22. The rest of the script includes syntax for listing the Amazon S3 buckets that are accessible using the MarketingAdmin role.

#### Using Python script to assume the MarketingAdmin role with MFA

![Running the Python script with MFA from the Windows command line using: python AssumeRoleMFA.py.](./images/W01Img106PyScriptAssumeMarketingAdminRoleMfaExample.png)

This sample output shows the AssumeRoleMFA.py Python script being run from the Windows command line.

The script first prompts the user to enter the code from the cli-user's MFA device, then assumes the MarketingAdmin role. After assuming the role, the command returns a list of Amazon S3 buckets that are accessible to the role.

---

## Logging AWS STS API Calls with AWS CloudTrail

CloudTrail captures all AWS service API calls as events, including calls from the console, AWS CLI, and API tools. IAM and AWS STS are integrated with CloudTrail, which can be used to create a record of the actions taken by an IAM user or role.

### Working with CloudTrail

CloudTrail is enabled on your AWS account when you create the account. The CloudTrail Event history provides a viewable, searchable, downloadable, and unchangeable record of the past 90 days of recorded management events in an AWS Region. To keep your CloudTrail data longer than 90 days, you must create a trail for CloudTrail to store the event data. After it's configured, you can set up ongoing delivery of events from CloudTrail to Amazon CloudWatch Logs. CloudWatch Logs provides mechanisms for detecting and reacting to specific CloudTrail events.

#### Creating a trail for CloudTrail

* In the AWS Management Console, search for the **CloudTrail** service.
* Choose **CloudTrail**.
* On the CloudTrail console, choose **Trails**.
* Choose **Create trail**.
* Enter **Trail name**.
* For **Storage location**, select the **Create new S3 bucket** radio button. Leave Trail log bucket and folder as the default.
* For Log file SSE-KMS encryption, select **Enable**d. For the customer managed key, choose **New**. For **AWS KMS alias**, enter **cloudtrailalias**. For Logfile validation, select **Enabled**. You can leave SNS notification delivery **unchecked**.
* For CloudWatch Logs, select **Enabled**, and then choose **New**. This will make additional configuration options available.
* For Log group name, enter **CloudTrail/DefaultLogGroup**, and then choose **New**.
* In the Role name text box, enter **CloudTrailRoleForCloudWatchLogs**. Now, scroll to the bottom of this page, and choose **Next**.
* On the **Choose log events** page, for **Event type**, select **Management** events.
* In **Management events**, check that the **API activity** for **Read** and **Write** are selected. Then, choose **Next**.
* On the Review and create page, you can review trail attributes.
* Scroll to the bottom of the page.
* To complete the process, choose **Create trail**.

A successful trail creation will populate and show a status of Logging.

---

#### AWS CloudTrail log contents

There can be dozens or even hundreds of events in one CloudTrail log file. The body of a CloudTrail log file contains multiple fields. These fields help you determine the user's or role's requested action, in addition to when and where the request was made. The following table summarizes some of the important CloudTrail fields related to AWS STS activity.

| CloudTrail log element | Log element description |
| ---------------------- | ----------------------- |
| eventTime | This element is the date and time of the event reported in Coordinated Universal Time (UTC). |
| eventType | This element is the type of event that occurred. Events related to the use of temporary credentials include:<br><br>* **AwsConsoleSignin**. A user in your AWS account (root, IAM, federated, or SAML) signed in to the AWS Management Console.<br>* **AwsServiceEvent**. The called service generated an event related to your trail. This can occur when another account made a call with a resource that you own.<br>* **AwsApiCall**. An AWS resource was called using a public API. |
| eventSource | This is the service that the request was made to. This name is typically a short form of the service name without spaces, and .amazonaws.com. as an added suffix. The following are some examples:<br><br>* AWS CloudFormation is **cloudformation.amazonaws.com**<br>* Amazon EC2 is **ec2.amazonaws.com**<br>* Amazon Simple Workflow Service is **swf.amazonaws.com**<br><br>This convention has some exceptions. For example, the eventSource for Amazon CloudWatch is **monitoring.amazonaws.com**. |
| eventName | This element is the name of the requested action, which will consist of one of the actions available in the API for that service. |
| sourceIPAddress | This element is the IP address where the request came from. If one AWS service calls another service, the DNS name of the calling service is used. |
| userAgent | Reports the tool or application through which the request was made, such as the AWS Management Console, an AWS service, the AWS SDKs, or the AWS CLI. The following are some examples:<br><br>* **signin.amazonaws.com**: Request by an IAM user with the AWS Management Console.<br>* **console.amazonaws.com**: Request by a root user with the AWS Management Console.<br>* **lambda.amazonaws.com**: Request was made with AWS Lambda.<br>* **aws-sdk-java**: Request was made with the AWS SDK for Java.<br>* **aws-sdk-ruby**: Request was made with the AWS SDK for Ruby.<br>* **aws-cli/1.3.23 Python/2.7.6 Linux/2.6.18-164.el5**: Request was made with the AWS CLI installed on Linux. |
| errorMessage | Contains any error message returned by the requested service. |
| requestParameters | This element captures the parameters that were sent with the API call, which can vary depending on the type of resource or service called. For example, in an Amazon S3 API call, you could have the bucketName and location sent as parameters. |
| resources | Represents a list of AWS resources accessed in the event. This can be the resource's ARN, an AWS account number, or the resource type. |
| userIdentity | This is a collection of fields that describe the user or service that made the call. These fields can vary based on the type of user or service. The following values are possible types of identity:<br><br>* **Root**: Request was made with your AWS account credentials. If you set an alias for your root account, the userName field will contain your account alias.<br> * **IAMUser**: Request was made with credentials of an IAM user.<br>* **AssumedRole**: Request was made with temporary security credentials that were obtained with a role through an API call to AWS STS.<br>* **FederatedUser**: Request was made with temporary security credentials that were obtained through a call to the AWS STS API.<br>* **AWSAccount**: Request was made by another AWS account.<br>* **AWSService**: Request was made by an AWS account that belongs to an AWS service. For example, AWS Elastic Beanstalk assumes an IAM role in your account to call other AWS services on your behalf. |

---

#### Logging sign-in events for temporary credentials

CloudTrail logs all authenticated API requests to AWS IAM and AWS STS API operations. CloudTrail also logs non-authenticated requests to the AWS STS actions, **AssumeRoleWithSAML** and **AssumeRoleWithWebIdentity**, and logs information provided by the identity provider.

When a principal requests temporary credentials, the principal type determines how CloudTrail logs the event. You can use the **sts:SourceIdentity** condition key in the role trust policy to require users to specify an identity when they assume a role. For example, you can require that IAM users specify their own user name as their source identity. This can help you determine which user performed a specific action in AWS. You can also use **sts:RoleSessionName** to require users to specify a session name when they assume a role. This can help you differentiate between role sessions for a role that is used by different principals when you review CloudTrail logs.

The following table shows how the CloudTrail service logs different user identity information for each of the AWS STS APIs that generate temporary credentials.

| Principal | AWS STS API | User identity in CloudTrail log for caller's account | User identity in CloudTrail log for the assumed role's account | User identity in CloudTrail log for the role's subsequent API calls |
| --------- | ----------- | --------- | --------- | --------- |
| root user | GetSessionToken | Root user identity | Role owner account is the same as the calling account | Root user identity |
| IAM user | GetSessionToken | IAM user identity | Role owner account is the same as the calling account | IAM user identity |
| IAM user | GetFederationToken | IAM user identity | Role owner account is the same as the calling account | IAM user identity |
| IAM user | AssumeRole | IAM user identity | Account number and principal ID (if a user), or AWS service principal | Role identity only (no user) |
| Externally authenticated user | AssumeRoleWithSAML | Not applicable | SAML user identity | Role identity only (no user) |
| Externally authenticated user | AssumeRoleWithWebIdentity | Not applicable | OIDC/Web user identity | Role identity only (no user) |

---

#### Examples of AWS STS API events in CloudTrail logs

CloudTrail log files contain events that are formatted using JSON. An API event represents a single API request. It includes information about the principal that requested the action, the requested action, any parameters, and the date and time of the action. You can use CloudTrail logs to get information about API requests made to AWS STS.

The following is a partial example of a CloudTrail log entry for a request made for the AWS STS **AssumeRoleWithSAML** action.

![Partial example of a CloudTrail log entry AssumeRoleWithSAML request.](./images/W01Img110CloudTrailLogAssumeRoleWithSaml.png)

1. **Who made the request?**

    The **userIdentity** section of the log file example shows the type, ID, username, and IdP for the user making the AssumerRoleWithSAML request.

    These items are shown in lines 4 through 7 in the sample log.

2. **Additional request details**

    Lines 9 through 14 provide additional details about the request. These details include the time of the request (**eventTime**), which AWS Region the request came from (**awsRegion**), and information about the client application or user agent that initiated the request to assume the role (**userAgent**).

3. **Request paramaters**

    Lines 15 through 31 show request parameters that were passed with the AWS STS API call. The ARN for the role to be assumed (**roleArn**) is shown on Line 28. Optional tags (**principalTags** and **transitiveTags**) are shown on lines 19 and 24. The specification of how long the temporary credentials will be valid (**durationSeconds**) appears on Line 30.

The request includes the SAML attributes **CostCenter** and **Project** that are passed through the SAML assertion as session tags. The request also includes the optional API parameter, **DurationSeconds**, represented as durationSeconds in the CloudTrail log, which is set to 1800 seconds. The request also includes the SAML attribute **sourceIdentity**, which is passed in the SAML assertion.

This next image shows additional output from the sample CloudTrail log entry generated by a request for the AWS STS AssumeRoleWithSAML action. The response includes the parameters needed to request the temporary credentials: **accessKeyID**, **sessionToken**, and expiration on lines 34 through 36.

![CloudTrail log entry for response to AssumeRoleWithSAML](./images/W01Img112CloudTrailLogAssumeRoleWithSamlResponse.png)

```json
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "SAMLUser",
        "principalId": "SampleUkh1i4+ExamplexL/jEvs=:SamlExample",
        "userName": "SamlExample",
        "identityProvider": "bdGOnTesti4+ExamplexL/jEvs="
    },
    "eventTime": "2023-08-28T18:30:58Z",
    "eventSource": "sts.amazonaws.com",
    "eventName": "AssumeRoleWithSAML",
    "awsRegion": "us-east-2",
    "sourceIPAddress": "AWS Internal",
    "userAgent": "aws-internal/3 aws-sdk-java/1.12.479 Linux/5.10.186-157.751.amzn2int.x86_64 OpenJDK_64-Bit_Server_VM/17.0.7+11 java/17.0.7 kotlin/1.3.72 vendor/Amazon.com_Inc. cfg/retry-mode/standard",
    "requestParameters": {
        "sAMLAssertionID": "_c0046cEXAMPLEb9d4b8eEXAMPLE2619aEXAMPLE",
        "roleSessionName": "MyAssignedRoleSessionName",
        "sourceIdentity": "MySAMLUser",
        "principalTags": {
            "CostCenter": "987654",
            "Project": "Unicorn",
            "Department": "Engineering"
        },
        "transitiveTagKeys": [
            "CostCenter",
            "Project"
        ],
        "roleArn": "arn:aws:iam::444455556666:role/SAMLTestRoleShibboleth",
        "principalArn": "arn:aws:iam::444455556666:saml-provider/Shibboleth",
        "durationSeconds": 1800
    },
    "responseElements": {
        "credentials": {
            "accessKeyId": "ASIAIOSFODNN7EXAMPLE",
            "sessionToken": "<encoded session token blob>",
            "expiration": "Aug 28, 2023, 7:00:58 PM"
        },
        "assumedRoleUser": {
            "assumedRoleId": "AROAD35QRSTUVWEXAMPLE:MyAssignedRoleSessionName",
            "arn": "arn:aws:sts::444455556666:assumed-role/SAMLTestRoleShibboleth/MyAssignedRoleSessionName"
        <SNIP>
```

The response also includes **AssumedRoleUser** event on Line 38. This output is comprised of the components on lines 39 and 40, the **assumeRoleId** and **ARN** for the role the user will assume.

---

#### CloudWatch Logs notifications and actions

You can configure CloudTrail with CloudWatch Logs to monitor your trail logs and be notified when specific activity occurs. The steps to implement this configuration are as follows:

1. **Send CloudTrail events to CloudWatch Logs.** You can do this by creating a new CloudWatch log group or using an existing one, specifying a suitable IAM role, and attaching a role policy.
2. **Tell CloudWatch what to watch for.** You can do this by defining a CloudWatch Logs metric filter that evaluates incoming log events. Filters can check log events based on terms, phrases, or values that you specify.
3. **Tell CloudWatch what to act on.** You can do this by creating metric or composite alarms for CloudWatch items identified by the metric filters.
4. **Tell CloudWatch what to do.** You can do this by creating CloudWatch alarms that are invoked according to thresholds and time periods that you specify. You can configure alarms to send notifications when alarms are raised so you can take action.
5. **Tell CloudWatch how to react.** You can do this by configuring CloudWatch to automatically perform an action when an alarm is raised. This is an alternative to notifying you when an alarm is raised.

---

#### Creating CloudWatch alarms for AWS STS CloudTrail events

There are two types of alarms available in CloudWatch: metric and composite. *Metric alarms* watch a single CloudWatch metric. *Composite alarms* take into account the alarm states of several metrics or other composite alarms.

A CloudWatch  alarm has the following possible states: OK, ALARM, or INSUFFICIENT_DATA. An **OK** state means the metric or expression is within the defined threshold. An **ALARM** state means the metric or expression is outside of the defined threshold. An **INSUFFICIENT_DATA** state means the data collection has just started, the metric is not available, or not enough data is available for the metric to determine the alarm state.

Alarms are raised whenever the criteria defined for the metric or composite alarm is met — relative to a defined threshold, and over a specific period of time. The composite alarm goes into ALARM state only if all conditions of the alarm rule are met.

---

#### Creating a CloudWatch Logs filter for AWS STS

To monitor CloudWatch Logs for events related to temporary credential activity, a metric filter for API calls to AWS STS can be created.

* In the AWS Management Console, search for and choose the **CloudWatch** service.
* On the CloudWatch Console , choose **Logs**, and then **Log groups**. Next, choose the log group to which you will apply the filter.
* In this example, you will use a log group **called aws-cloudtrail-logs-STS**.
* Perform the first step of the metric filter creation.
* In the **Create filter pattern** section, scroll to **Filter pattern** and enter the filter pattern that specifies the events you wish to filter on.
* The filter pattern shown here identifies calls to the AWS STS API that include requests for **Assume Role**, **Get Federation Token**, **Get Session Token**, **Assume Role with SAML**, and **Assume Role with Web Identity**. Each of these events are associated with the use of temporary credentials.

    ```json
    {
      $.eventSource = "sts.amazonaws.com" &&
      ($.eventName = "AssumeRole" ||
       $.eventName = "GetFederationToken" ||
       $.eventName = "GetSessionToken" ||
       $.eventName = "AssumeRoleWithSAML" ||
       $.eventName = "AssumeRoleWithWebIdentity")
    }
    ```

* After supplying the filter pattern, you can test the pattern to see if it provides the desired results. This example uses the log group ending in **us-east-1_4** to test the pattern.
* To test the pattern, choose the **Test pattern** button. Any matching filter results are displayed in the **Show test results** section of the console.
* After testing the filter pattern to confirm that it operates correctly, choose **Next** to continue.
* The **Assign metric** page appears. For **Filter name**, enter **STS-temp-credentials**.
* Move to the **Metric details** page. Choose **Create new** and then enter **STS-activity** for the **Metric namespace**. 

    A metric namespace is a logical grouping or container that organizes and categorizes related metrics, so you can filter and monitor specific aspects of your AWS resources and applications.

* For the Metric name, enter **STS-temp-credentials-usage**. Because this filter is counting occurrences of the keywords in the filter, enter **1** for the **Metric value**.

     This increments the metric by 1 for each log event that includes one of the keywords.

* For the optional **Unit value**, enter **Count**. Leave the Default value **blank**.
* On the **Metric details** page, leave the **Dimensions section** blank. Then scroll to the bottom and choose **Next**.
* The Review and create page appears. This page shows a summary of all the items that were previously configured.
* To create the filter using the parameters that you defined, scroll to the bottom of the page and choose **Create metric filter**.

The filter pattern in this example uses two criteria for matching. The pattern will match any CloudTrail log entries where the event source is the AWS STS service. The pattern will also match when the event name is one of the five API calls used to request temporary credentials: AssumeRole, GetFederationToken, GetSessionToken, AssumeRoleWithSaml, and AssumeRoleWithWebIdentity.

---

#### Creating a CloudWatch alarm for the AWS STS metric

Using the metric defined in the previous section, you can create an alarm to alert you whenever an API call is made to AWS STS for temporary credentials.

1. **Navigate to the CloudWatch page**

    ![CloudWatch page in the AWS Management Console.](./images/W01Img120CloudWatchConsole.png)

    Using the AWS Management Console, navigate to the CloudWatch page and choose **All alarms** from the menu.

2. **Start the creation of the alarm**

    ![CloudWatch All Alarms page with Create alarm highlighted.](./images/W01Img122CloudWatchConsoleCreateAlarm.png)

    From the CloudWatch alarms page, choose **Create alarm** to begin the process of creating your temporary credentials alarm.

3. **Specify the metric and conditions**

   ![CloudWatch Create alarms page with Select metric highlighted.](./images/W01Img124CloudWatchConsoleCreateAlarmSelectMetric.png)

    Choose **Select metric** to tell CloudWatch which filter metric to use for this alarm.

4. **Select the metric namespace**

    ![CloudWatch alarm Select metric page with the STS-activity metric selected.](./images/W01Img126CloudWatchConsoleCreateAlarmSelectMetricSpace.png)

    In the **Custom namespaces** section of the page, choose the **STS-activity** metric.

5. **Choose the metric name**

    ![CloudWatch alarms Select metric page with Browse tab and STS-temp-credentials-usage metric selected.](./images/W01Img128CloudWatchConsoleCreateAlarmChooseMetricName.png)

    On the **Select metric** page, navigate to the **Browse** tab and select the **STS-temp-credentials-usage** filter metric. Then, choose **Select metric** to confirm.

6. **Specify the metric conditions**

    ![CloudWatch Alarms Configure actions page with conditions section highlighted.](./images/W01Img130CloudWatchConsoleCreateAlarmMetricConditions.png)

    Next, configure the alarm by defining how often to check for the entries that match the filter metric. The threshold that will cause the metric to be raised should also be defined. For Statistic, choose **Average**. For the polling period, choose **5 minutes**. For Threshold type, choose **Static**. For Alarm condition, choose **Greater**. For the Greater than value, type **zero**. Then, choose **Next** to continue the alarm configuration.

7. **Configure notifications**

    ![CloudWatch Alarms Configure actions page with Create topic highlighted.](./images/W01Img132CloudWatchConsoleCreateAlarmConfigureNotifications.png)

    The previous step defined the criteria that will cause the alarm to be raised. In this step, you describe which actions to perform when the alarm is raised. Under Alarm state trigger, select **In alarm**. Under Send a notification to the following SNS topic, select **Create new topic**. Under Create new topic, type **STS-CloudWatch-Alarm-Topic**. Choosing these options will send notifications to subscribers of a new Amazon Simple Notification Service (Amazon SNS) topic called STS-CloudWatch-Alarm-Topic whenever the alarm is raised. Additionally, you can enter the email addresses of users who want to be notified in the Email endpoints that will receive the notification box. Choose **Create topic**.

8. **Additional metric conditions**

    ![Other configuration options in response to a CloudWatch alarm with Next highlighted.](./images/W01Img134CloudWatchConsoleCreateAlarmAdditionalMetricConditions.png)

    In addition to sending notifications, alarms can also invoke Lambda functions, perform auto-scaling or Amazon EC2 actions, create support tickets, or initiate AWS Systems Manager activities. None of these are used for this example, so choose **Next** to continue.

9. **Add name and description**

    ![CloudWatch Alarms page with name and description completed, and Next highlighted.](./images/W01Img136CloudWatchConsoleCreateAlarmAddName.png)

    The last step in the Alarm configuration process is to assign an Alarm name and an optional Alarm description. This example uses **STS activity in CloudWatch Logs** for the name, and a short description of what the alarm does. Choose **Next** to move to the alarm summary screen.

10. **Review final configuration**

    ![CloudWatch Alarm configuration summary page with Create alarm highlighted.](./images/W01Img138CloudWatchConsoleCreateAlarmReviewConfiguration.png)

    Next, a summary screen is displayed showing all the options that have been configured for the alarm. Each option can be edited from this screen as needed. After all alarm configuration items are complete, choose **Create alarm** to create the alarm.

11. **Summary***

    ![CloudWatch All Alarms page showing the successfully created message.](./images/W01Img140CloudWatchConsoleCreateAlarmCreated.png)

    The CloudWatch alarm configuration screen is displayed with a successful completion message indicating the alarm has been created.

---

### CloudWatch Logs Insights

CloudWatch Logs Insights is an interactive log analytics service for CloudWatch. CloudWatch Logs Insights gives you the ability to explore, analyze, and visualize the contents of your CloudWatch Logs. CloudWatch Logs Insights can be used to gain insights into user activity by automatically detecting unusual API activities.

For example, with Trail Insights, you can create custom queries and filters to analyze CloudTrail logs and identify API calls made to the AWS STS service for temporary credentials. This can help you monitor and audit the issuance of temporary security credentials, detect potential misuse or unauthorized access attempts, and gain insights into how your applications and services are using the AWS STS service.

---

### Activity: Monitoring Temporary Credential Use

#### If we want to track application activity that uses temporary credentials, which types of events should we watch for in the CloudTrail trail?

* API calls made to AWS STS

Wrong answers:

* API calls made to lAM
* API calls made to AWS Secrets Manager

##### Explanation

Calls made to the AWS STS API indicate the use of temporary credentials, among other activities.

#### To further enhance security, the team has decided to require administrative users to utilize MFA in order to be granted temporary credentials. Which AWS STS API request should the team look for in CloudTrail to identify these MFA credential requests?

* Requests to GetSessionToken

Wrong answers:

* Requests to AssumeRoleWithSAML
* Requests to AssumeRole

##### Explanation

A request to GetSessionToken passes two parameters to the API: The SerialNumber and TokenCode of the user's MFA device.

---

## Using IAM Roles for Amazon EC2 Instances

Applications must sign their API requests with AWS credentials. Therefore, you need a strategy for managing credentials for your applications that run on Amazon Elastic Compute Cloud (Amazon EC2) instances. You could distribute credentials to each instance to provide the applications on those instances with the credentials needed to sign requests. However, doing this securely is challenging, and this approach typically does not scale well as more instances are added to the application architecture.

Instead, these credentials can be provided to Amazon EC2 instances using instance profiles. IAM roles are assigned to the instance profile, which is then assigned to Amazon EC2 instances. Using IAM roles allows your applications to securely make API requests from your instances, even as your applications scale to hundreds or thousands of instances.

### How IAM roles work with Amazon EC2

IAM roles can be assigned to Amazon EC2 instances using instance profiles. When you create an IAM role using the IAM console, the console creates an instance profile automatically and gives it the same name as the corresponding role. If you use the AWS CLI, API, or an AWS SDK to create a role, you create the role and instance profile as separate actions, with potentially different names.

If you use the Amazon EC2 console to launch an instance with an IAM role, or attach an IAM role to an instance, you can use the instance profile that was assigned to the role by default. If you use the AWS CLI, API, or an AWS SDK to launch an instance with an IAM role, or attach an IAM role to an instance, you will need to specify the instance profile name.

After assigning an IAM role to an Amazon EC2 instance, all of the privileges allocated to that role are made available to each instance that has been assigned the instance profile. Specifically, the credentials associated with the IAM role will automatically be available to application processes on that instance that use AWS Software Development Kit (AWS SDK) components, or the AWS CLI. IAM roles can be particularly useful with well-architected applications that automatically add instances using Auto Scaling groups or Spot Instances. As these instances are dynamically added to the application architecture, they can be assigned the appropriate IAM role using an instance profile. The profile will immediately allow the application to have access to these resources.

---

You can only attach one IAM role to an instance profile, but you can attach the same role to many instances profiles.

---

1. **Specify permissions**

    ![Flow diagram showing IAM policy passing privileges to an application, with sample code for an IAM policy in JSON format.](./images/W01Img150IamRoleInstanceProfileCreateIamPolicy.png)

    You begin by creating an IAM policy in JSON format that defines the permissions to the DynamoDB table. In this example, the JSON code creates a policy called SalesAccess, that allows insert, update, and delete actions on a DynamoDB table called SALES.

2. **Attach policy to role**

    ![Flow diagram showing IAM policy attaching to a role, with sample AWS CLI command.](./images/W01Img152IamRoleInstanceProfileAttachIamPolicyToRole.png)

    Next, you can assign the **SalesAccess** IAM policy to a new or existing IAM role using the AWS CLI (shown here) or AWS SDK. This example attaches the IAM policy to an IAM role called **EC2SalesRole**.

3. **Associate the IAM role**

    ![Flow diagram showing IAM role associating with an instance, with sample AWS CLI command.](./images/W01Img154IamRoleInstanceProfileAssociateRoleWithInstance.png)

    You can now associate the IAM role **EC2SalesRole** with an instance profile using the AWS CLI (shown here) or AWS SDK. This example assigns the IAM role to an EC2 instance with the ID i-0123456789abcdef. After assigning the EC2SalesRole role to the EC2 instance, the instance will have the permissions defined in the IAM policies attached to that role.

4. **Privilege passing using role**

    ![Flow diagram showing instance passing IAM role privileges to the application.](./images/W01Img156IamRoleInstanceProfilePassingCredsToApp.png)

    Because the instance is assigned the EC2SalesRole instance profile, any applications running on this instance will have the same permissions. The permissions granted to the application are strictly limited to the specific actions allowed by the IAM policy attached to EC2SalesRole.

5. **DynamoDB table access**

    ![Flow diagram showing application accessing table using IAM role privileges from instance.](./images/W01Img158IamRoleInstanceProfileAccessWithIamRolePrivileges.png)

    Because the EC2SalesRole IAM role has been associated with the application’s EC2 instance profile, the application is able to access the SALES DynamoDB table.

6. **Propagating policy and role changes**

    ![Flow diagram showing a change made between an IAM policy and role to detach a policy, with sample AWS CLI code.](./images/W01Img160IamRoleInstanceProfilePropagatingPolicy.png)

    If you change an IAM policy assigned to a role, that change will be propagated to all instance profiles, and all instances that have been assigned that profile. In this example, the IAM policy granting access to the SALES DynamoDB table has been detached from the EC2SalesRole IAM role. This action would cause the application deployed on the instance to lose access to the SALES table.

7. **Summary**

    The application running on the instance will inherit the permissions associated with the role only if the instance has been correctly configured to use that role. This is typically done by attaching an instance profile that contains the IAM role to the instance during launch, or by associating the instance profile with an existing instance.

---

### Permissions for using roles with Amazon EC2

The following table summarizes the IAM privileges that are used to manage IAM roles assigned to Amazon EC2 instances using instance profiles.

| IAM privilege | Privilege description |
| ------------- | --------------------- |
| iam:PassRole| Grants permissions required to pass a role and its permissions to an AWS service. |
| ec2:AssociateIamInstanceProfile | Associates an IAM instance profile (which contains the IAM role) with an Amazon EC2 instance. It is required to assign an IAM role to your Amazon EC2 instances. |
| iam:GetRole | Retrieves information about an IAM role, including its policies and trust relationships. It is required to view the details of an IAM role you want to associate with your Amazon EC2 instances. |
| iam:ListRoles | Lists all the IAM roles in your AWS account. It is required to see the available roles that you can associate with your Amazon EC2 instances using instance profiles. |
| iam:ListInstanceProfiles | Lists all the instance profiles in your AWS account. |
| iam:ListAttachedRolePolicies | Lists all the policies attached to an IAM role. It is required to view the permissions granted by the role you want to associate with your Amazon EC2 instances. |
| ec2:DescribeIamInstanceProfileAssociations | Describes the IAM instance profile associations for your Amazon EC2 instances. It is required to view the IAM roles associated with your Amazon EC2 instances. |

These permissions can be granted to an IAM user, group, or role through appropriate IAM policies. It's generally recommended to follow the principle of least privilege and grant only the necessary permissions required for your use case.

If you are using the AWS Management Console, some of these permissions might be granted automatically, based on the actions you perform. However, if you are using the AWS CLI, AWS SDKs, or making API calls directly, you will need to ensure that you have the required permissions explicitly granted.

---

## Tag-based Temporary Credentials

IAM offers two different authorization models that you can use to control access to your AWS resources. The traditional model is called **role-based access control (RBAC)**. The other authorization mode is called **attribute-based access control (ABAC)**.

### Role-based and attribute-based access controls

The following table compares role-based and attribute-based IAM access controls in the AWS Cloud.

| Role-based access control | Attribute-based access controls |
| ------------------------- | ------------------------------- |
| * Access permissions are defined based on a person's job function.<br>* Controls are implemented by creating policies for each job function.<br>* Identities such as IAM users, groups of users, or an application can assume these policies through roles.<br>Each policy contains permissions that allow access to a specific set of resources. | * Access permissions are defined based on attributes called tags.<br>* Tags use customizable key-value pairs, such as a project name or an environment type, to identify IAM principals and AWS resources.<br>* Policies can also be designed to allow operations when a principal's tag matches a resource tag. |

An ABAC tag consists of two parts, or key-pair values. The example shown here uses a tag whose key-value pair consists of pt (key), which stands for project team, and ship (value) to used to indicate a shipping-related development project. Together, these values form a tag called **PT:SHIP**.

With most AWS resources, you have the option of adding tags when you create the resource. AWS also provides a Tag Editor, which can be used to add, edit, or delete tags from multiple resources at one time. By using the Tag Editor, you can search for the resources that you want to tag, and then manage tags for the resources returned by your search. 

### ABAC use cases

The following use cases are provided to strengthen your understanding of the ways that ABAC can be used to manage permissions in AWS application architectures.

#### Using ABAC with Amazon EC instances

An administrator can use a single IAM policy to grant users access to Amazon EC2 instances that match the user’s project tag. As more resources are added to projects, permissions are automatically applied based on tags. As a result, no policy update is required for each new resource. Using this approach saves time and helps improve security because you’re not relying on granular permissions rules.

![ABAC to control access to Amazon EC2 instances diagram](./images/W01Img170AbacBasedControlAccess.png)

1. **Development teams**

    In this example, three application development teams are working on separate parts of a new e-commerce application: **shopping**, **shipping**, and **billing**.

2. **IAM roles**

    Each of the three development teams has been assigned an access-based IAM role with a tag key of pt (project team).

3. **Tag key-value pairs**

    The ABAC tag assigned to each development team consists of the ABAC role tag key (**pt**) and the team's tag value (**shop**, **ship**, or **bill**).

4. **Single policy**

    A single IAM policy is used to allow access to each development team's Amazon EC2 instances. Access is based on the instance having the same tag key (**pt**) and tag key value (**shop**, **ship**, or **bill**) as the user's ABAC role.

5. **Adding new resources**

    Any new instances added to the billing development team (bill) are automatically available to the team members because those instances are assigned the pt:bill ABAC tag.

---

Using ABAC is also helpful when you use a multi-account strategy. ABAC can be used to provide multiple teams operating in the same account granular access to different resources. For example, IAM Identity Center users or IAM roles can include conditions to limit access to specific Amazon EC2 instances. Otherwise, each instance would have to be explicitly listed in each policy in order to access those instances.

If the developers sign in to AWS using SAML or OICD, the IdP can send their team name as an attribute in the AWS session. IAM will use this attribute to limit the developer's access to only their team’s project resources as indicated by the tags on those resources.

#### Using ABAC to protect shared resources

When you base permissions on attributes, you can control the level of access a user has to shared AWS resources.

For example, by using the same IAM role, you can grant one developer read-only access to another developer's AWS Secrets Manager secret.

This is possible because the IAM role permissions are based on a team name attribute, which is the same for both developers.

Additionally, the secret can be tagged as being created by the original developer, so they are granted full access to the secret.

![Diagram showing two overlapping circles for two different developers, with a secret key in the shared area.](./images/W01Img172AbacProtectingSharedResources.png)

Shared ABAC on SALES lets Developer B access a secret key

---

AWS Secrets Manager is a service that helps you securely store, manage, and retrieve sensitive information, such as passwords, API keys, and other confidential data. For more information, see [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/).

---

#### Best practices for tag naming

When you begin attaching tags to your IAM resources, you should choose your tag naming convention carefully. You should strive to apply the same convention to all of your AWS tags. This is especially important if you use tags as part of your ABAC for AWS resources.

* **Be consistent**. Define and follow a consistent tag-naming convention. Keep in mind that tags are case sensitive.
* **Have a plan**. Consider naming your tags using all lowercase letters, with hyphens separating words, and a prefix that identifies the name of the AWS organization the tag belongs to.

---

AWS uses predefined tags for its own tagging purposes. AWS tags are lowercase, with hyphens separating words, and prefixed by aws or the service name.

---

#### Rules for tagging in IAM and AWS STS

There are some specific rules that apply to the creation and application of tags in IAM and AWS STS.

The following rules apply when *creating* tag names in AWS IAM or AWS STS:

* Tag keys and values can include any combination of letters, numbers, spaces, and the symbols _ . : / = + - @.
* Tag key values for IAM users and roles are not case sensitive, but case is preserved. Therefore, the tag values Sales and sales would both be considered the same IAM role tag, and would result in only one tag (sales) being applied to the user or role.
* Tag key values for other IAM resource types are case sensitive. Therefore, the tag values, Sales and sales, would not be considered to be the same tag. This would result in both tags (Sales and sales) being applied to the resource.
* Tag keys or values cannot begin with the text aws:.
* Empty tags that do immediately assign a value are allowed, but empty tag keys are not.
* Custom multivalue structures can be stored as a single key value. For example, **key=value1:value2:valueN** is allowed.

The following rules apply when *applying* tag names in IAM or AWS STS:

* IAM groups, assumed roles, access reports, or hardware-based MFA devices cannot be tagged.
* The Tag Editor cannot be used to tag IAM resources.
* The list tags permission is required to tag or untag resources.
* The same tag can be applied to multiple IAM resources.
* Assigning a new tag to an IAM user who already has an existing tag replaces the existing tag value with the new value. A second tag is not added.
* A tag that is attached to an IAM user or role cannot be edited. Instead attach a tag with a new value to overwrite the existing tag.

---

### Benefits of an attribute-based tagging strategy

Some of the benefits of an ABAC-based approach to access control include the following:

* **ABAC permissions scale.** In environments with rapid innovation and experimentation, administrators don't have to update existing policies to allow access to new resources as they are created.
* **ABAC requires fewer policies.** Different policies do not have to be created for different job functions.
* **ABAC gives teams the ability to quickly change and grow.** Permissions for new resources are automatically granted based on their assigned attributes.
* **ABAC provides granular permissions.** Access can be allowed on all resources, but only if the resource tag matches the principal's tag.
* **ABAC can use a corporate identity directory.** SAML or OIDC protocol identity providers can pass session tags to AWS. These session tags can be used to allow or deny permissions to resources based on matches between the tags and a resource's assigned attributes.

---

RBAC is closely aligned to business logic, and is usually more straightforward to implement than ABAC. Defining the rules and policies for ABAC, in addition to identifying the attributes for all relevant access methods, can require significant upfront planning to implement effectively.

---

### Hybrid approach to access control

You can use both role-based and attribute-based authorization models at the same time to help manage flexible permissions at scale. Combining RBAC and ABAC can provide some of the advantages of both models. This hybrid approach determines access by combining the assigned permissions of a user’s role with ABAC additional attributes to make access decisions. Using both models provides streamlined administration and assignment of permissions, while also providing increased flexibility and granularity pertaining to authorization decisions.

---

### Knowledge Check

#### An application deployed in the AWS Cloud authenticates users using trusted third-party social identity providers like Facebook and Google. Which type of authentication is this an example of?

* Temporary credentials using OpenID Connect (OIDC) based on an access key ID and secret access key

Wrong answers:

* Long-term AWS Identity and Access Management (IAM) credentials based on an access key ID and secret access key
* Temporary credentials using SAML based on an access key ID and secret access key
* Temporary credentials using AWS Secrets Manager based on an access key ID and secret access key

##### Explanation

**OIDC is used by third-party web identity providers (IdP) like Amazon, Facebook, and Google.** Corporate identity stores like Microsoft Active Directory use SAML to authenticate users for single sign-on access to applications. AWS IAM Identity Center does not manage IdP accounts, the IdP provider does. Single sign-on is not based on long-term IAM credentials.

---

#### A cloud developer is using the AWS SDK to create a reporting feature for an application. When the user runs a report, they use privileges associated with an AWS Identity and Access Management (IAM) role called ReadOnlyUser to access the reporting data. The application uses temporary credentials from an on-premises identity provider using single sign-on to authenticate users. Which request should the developer use when making a call to the AWS Security Token Service (AWS STS) API to assume the required role?

* AssumeRoleWithSAML

Wrong answers:

* AssumeRole
* GetSessionToken
* AssumeRoleWithWebIdentity

##### Explanation

**AssumeRoleWithSAML is used with SAML-based, single sign-on authentication.** AssumeRoleWithWebIdentity is the AWS STS API request to use when authenticating with web-based identity providers. GetSessionToken is used with multifactor authentication. AssumeRole is used to assume an IAM role, but does not require use of a web-based identity provider.

---

#### A developer is creating a trust policy that will require the user assuming an IAM role to connect to the AWS Cloud using multi-factor authentication (MFA). What should the developer include in the policy's condition clause to enforce the MFA requirement?

* "multifactorAuthPresent": true

Wrong answers:

* "sts:ExternalId":MFA
* "multifactorAuthPresent": false
* "sts:SourceIdentity":MFA

##### Explanation

**The trust policy Condition clause should include "multifactorAuthPresent": true to enforce the MFA requirement to assume a role.** Specifying multifactorpresent:false turns off the MFA requirement. Passing MFA as a parameter to sts:ExternalId  and sts:SourceIdentity cannot be used to enforce an MFA connection requirement.

---

#### A development team has been asked to monitor the use of application logins that use temporary security credentials. Which AWS Security Token Service (AWS STS) API calls should the team watch for in CloudTrail logs to meet this request? (Select THREE.)

* AssumeRoleWIthWebIdentity
* GetFederationToken
* AssumeRoleWithSAML

Wrong answers:

* eventType
* userIdentity
* eventSource

##### Explanation

**AssumeRoleWithSAML, AssumeRoleWIthWebIdentity, and GetFederationToken are all associated with the use of temporary credentials to log in.** The other items are also related to AWS STS API calls, but not specific to logins using temporary credentials.

---

#### Two cloud architects are in a conference room discussing how to best manage security for the developers on a new project. The developers will be creating resources that all members of the team will need to be able to access. One architect is proposing the team consider using attribute-based access control (ABAC) for the project resources. What are benefits of ABAC that the architect could use to support their recommendation? (Select THREE.)

* ABAC requires fewer policies.
* ABAC permissions scale.
* ABAC gives teams the ability to quickly change and grow.

Wrong answers:

* ABAC provides less granular permissions.
* ABAC does not rely on key-value pair tagging.
* ABAC is more secure than other methods of access control.

##### Explanation

**With ABAC, different policies do not have to be created for different job functions (fewer policies). In environments with rapid innovation and experimentation, ABAC frees administrators from having to update existing policies to allow access to new resources as they are created (permissions scale). ABAC can also automatically grant permissions for new resources based on their assigned attributes (ability to quickly change and grow).** ABAC does rely on key-value pair tags for access control. ABAC provides granular permissions, and is not more secure than other access control approaches.

---

### Summary

* User credentials can be either long-term or short-term. Long-term credentials should be protected using MFA and secure password policies. Short-term, or temporary credentials, can be managed using AWS STS.
* IdPs who reside in a data center use SAML 2.0 standards to authenticate federated users using single sign-on. IdPs who reside with a third-parties use the OIDC standard to authenticate federated users.
* AWS offers Amazon Cognito and IAM Identity Center to help manage temporary credentials for federated users.
* AWS STS uses the AssumeRole, GetSessionToken, AssumeRoleWithSAML, and AssumeRoleWithWebIdentity API requests to pass temporary credentials to AWS services. Calls to these APIs, and their responses, are captured in CloudTrail and are available to CloudWatch alarms to monitor temporary credential usage.
* The AWS CLI and AWS SDK can be used with AWS STS to request temporary credentials. These tools use the AWS STS API AssumeRole request to assume roles needed to perform application activities.
* IAM roles can be associated with EC2 instances. The application running on the EC2 instance will inherit the permissions associated with the assigned role. This capability provides a convenient way to manage credentials when instances are dynamically added to an application architecture through Amazon EC2 Auto Scaling or Spot instance usage.
* ABAC is defined based on resource attributes called tags. Tags use customizable key-value pairs, such as a project name or an environment type, to identify IAM principals and AWS resources.
* Benefits of using ABAC include scalability of permission management as the environment changes, ability to pass attributes as part of corporate identity, and more granular permission granting.

---
