# Week 4: Networking 3 Part 2: Protecting Web Applications from Common Exploits with AWS WAF

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to [AWS Cloud Fundamentals 2](./aws-cloud-fundamentals-2.md)
* back to repo's main [README.md](../../../README.md)

## AWS WAF Overview

AWS WAF is a web application firewall that you can use to monitor the HTTP and HTTPS requests that are forwarded to Amazon CloudFront, Amazon API Gateway, an Application Load Balancer, AWS AppSync, or Amazon Cognito. AWS WAF covers the application layer (Layer 7) in the Open Systems Interconnection (OSI) model. You can use AWS WAF to temporarily patch vulnerabilities without having to make major code changes. You can also block malicious actors from coming in, filter out incoming requests, and reduce the threat vectors overall.

![AWS WAF components.](./images/W04Img090AwsWafComponents.png)

---

### AWS WAF and OWASP

AWS WAF capabilities are closely aligned with the recommendations from the Open Worldwide Application Security Project (OWASP), a community-led initiative dedicated to improving the security posture of web applications. OWASP provides a wealth of resources and guidelines that can help you understand and address the most common web application vulnerabilities.

---

There are several ways that you can configure AWS WAF to protect your applications. At the simplest level, using AWS WAF, you can choose one of the following behaviors:

* Allow all requests except the ones that you specify. This is useful when you want Amazon CloudFront, Amazon API Gateway, Application Load Balancer, or AWS AppSync to serve content for a public website, but you also want to block requests from attackers. You can filter incoming traffic based on a variety of criteria, including IP origin, geographical location, and regular expressions.
* Block all requests except the ones that you specify. This is useful when you want to serve content for a restricted website whose users are readily identifiable by properties in web requests, such as the IP addresses that they use to browse to the website.
* Count the requests that match properties that you specify. When you want to allow or block requests based on new properties in web requests, you can first configure AWS WAF to count the requests that match those properties without allowing or blocking those requests. This way, you can confirm that you didn't accidentally configure AWS WAF to block all the traffic to your website. When you're confident that you specified the correct properties, you can change the behavior to allow or block requests.

---

AWS WAF is a tool that can supplement your existing security posture, but it’s not meant to replace it. Your shared responsibility at AWS is still applicable, and you always need to think about your security in the cloud holistically.

---

### AWS WAF key benefits

#### Frictionless setup

You can deploy without changing your existing architecture, with no need to configure TLS/SSL certificates or change DNS configuration.

#### Low operational overhead

You have ready-to-use AWS CloudFormation templates, built-in SQL injection/cross-site scripting (SQLi/XSS) exploit detection, and managed rules through AWS Marketplace. You can optionally create your own custom rules.

#### Customizable security

AWS WAF has a highly flexible rule engine that can inspect any part of incoming requests under single-millisecond latency.

#### API-driven architecture

With API-driven architecture and fast rule propagation, you can detect and respond to threats in real time.

---

## AWS WAF deep dive

The challenging part with DDoS attacks is it may not always be traffic that looks malicious. If you were actually capture the packets inside, you may see perfectly normal traffic. But the key is you could be getting a flood, so much of a flood that you're not able to go ahead and perform your operations properly on the target.

### Common DDoS attack layers

![Common DDoS attack layers.](./images/W04Img100CommonDdosAttackLayers.png)

Four layers of OSI model - three, four, six, and seven - are the most common layers where you can have DDoS attacks.

### Infrastructure layers - three and four - protection with AWS Shield Standard

Shield Standard is a service that everybody gets by default as an AWS client.

![Layers 3 and 4 protection with AWS Shield Standard](./images/W04Img102DdosAttackLayers3And4WithAwsShieldStandard.png)

![AWS Shield Standard features.](./images/W04Img104AwsShieldStandardFeatures.png)

### Application layer - seven - attack protection with AWS WAF

![AWS WAF solutions.](./images/W04Img106AwsWafSolutions.png)

![AWS WAF for application layer protection.](./images/W04Img108AwsWafLayer7Protection.png)

* It has frictionless setup, no changes to the application.
* The WAF also runs out the edge locations.
* You define the rules and the ACLs inside the WAF.
* It's API driven.

![AWS WAF key benefits.](./images/W04Img110AwsWafKeyBenefits.png)

#### AWS WAF setup

![AWS WAF setup.](./images/W04Img112AwsWafSetup.png)

![AWS WAF setup: configure ACLs.](./images/W04Img114AwsWafSetupConfigureAcls.png)

#### Monitoring with CloudWatch Sending logs to Kinesis Data Firehose (and then to S3, for example)

![AWS WAF setup: CloudWatch and Kinesis Data Firehose.](./images/W04Img116AwsWafSetupCloudWatchKinesisDataFirehose.png)

#### AWS WAF rule types

![AWS WAF rule types.](./images/W04Img118AwsWafRuleTypes.png)

#### AWS WAF managed rules

![AWS WAF managed rules.](./images/W04Img120AwsWafAwsManagedRules.png)

#### AWS WAF ACLs rule statements

* IP Sets
* Rule groups
* Regex sets

These ones can be reused in different rules/regions etc.

![AWS WAF ACLs rule statements.](./images/W04Img122AwsWafAclRuleStatements.png)

![AWS WAF available rule statements.](./images/W04Img124AwsWafAclRuleAvailableStatements.png)

#### AWS WAF: Triggering CloudWatch alarm

![Triggering CloudWatch alarm.](./images/W04Img126AwsWafTriggeringCloudWatchAlarm.png)

#### Incident report with CloudWatch

![Incident report with CloudWatch.](./images/W04Img128AwsWafIncidentReportWithCloudWatch.png)

#### Visibility with logs

* A sampled log basically does random sample of the requests and place a summary inside. This is a quick view from a health check perspective, it's not a complete level of detail.

![AWS WAF: Visibility Sampled log](./images/W04Img130AwsWafVisibilitySampledLog.png)

* With the full log, we can capture the details of every single request. So the entire details are basically piped out through over the Kinesis and Kinesis Firehose out to some type of storage.
* The full log is in JSON format.
* You can retract sensitive information.

![AWS WAF: Visibility Full log](./images/W04Img132AwsWafVisibilityFullLog.png)

* Firehose allows you to send the data to S3, Redshift, Elasticsearch, and Splunk. You can start to do some analysis and search that particular data.

#### Full log analysis benefits

![Full log analysis benefits.](./images/W04Img134AwsWafFullLogAnalysisBenefits.png)

* With Kibana we can build a frontend dashboard for doing visualization.

#### AWS WAF Security Automations template

* It can have interactions with the WAF itself by changing rules that are out there, essentially all related to dynamic things that are occurring within your logs themselves.

![AWS WAF Security Automations template.](./images/W04Img136AwsWafSecurityAutomations.png)

#### Integrating GuardDuty with AWS WAF

![GuardDuty and AWS WAF integration.](./images/W04Img138AwsGuardDutyAwsWafIntegration.png)

#### AWS WAF notes

![AWS WAF notes.](./images/W04Img140AwsWafNotes.png)

---

### AWS WAF web ACLs review

You use a web access control list (web ACL) to protect a set of AWS resources. You create a web ACL and define its protection strategy by adding rules. Rules define criteria for inspecting web requests and specify how to handle requests that match the criteria.

![AWS WAF web ACLs review.](./images/W04Img142AwsWafWebAclsReview.png)

1. **Rule group**

    You can use rules individually or in reusable rule groups. AWS Managed Rules and AWS Marketplace sellers provide managed rule groups for your use. You can also define your own rule groups.

2. **Rule statements**

    This is the part of a rule that tells AWS WAF how to inspect a web request. When AWS WAF finds the inspection criteria in a web request, we say that the web request matches the statement. Every rule statement specifies what to look for and how, according to the statement type.

3. **IP set**

    This is a collection of IP addresses and IP address ranges that you can use together in a rule statement. To use an IP set in a web ACL or rule group, you first create an AWS resource, IPSet, with your address specifications. Then you reference the set when you add an IP set rule statement to a web ACL or rule group.

4. **Regex pattern set**

    This is a collection of regular expressions that you can use together in a rule statement. To use a regex pattern set in a web ACL or rule group, you first create an AWS resource, RegexPatternSet, with your regex pattern specifications. Then you reference the set when you add a regex pattern set rule statement to a web ACL or rule group. A regex pattern set must contain at least one regex pattern.

---

### AWS WAF Intelligent Threat Mitigation

#### Mitigating threats with AWS WAF

AWS WAF provides several specialized protections to mitigate advanced threats such as malicious bots. The following is an overview of some of these protections.

Account creation fraud is an illegal online activity where someone tries to create fake accounts. Attackers use these fake accounts for malicious purposes. The **AWS WAF account creation fraud prevention (ACFP)** feature helps detect fraudulent account creation attempts on your application's sign-up page. It uses a predefined set of rules to identify such attempts. These rules identify and manage requests that might be part of malicious account creation attempts. To learn more, see [AWS WAF Fraud Control Account Creation Fraud Prevention (ACFP)](https://docs.aws.amazon.com/waf/latest/developerguide/waf-acfp.html) in the *AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.

A bot, short for "robot," is a software program or application designed to perform automated tasks. Unauthorized users sometimes use bots to conduct attacks on your application. The AWS WAF Bot Control feature helps you manage and protect your web applications from unwanted bot activity. With this service, you can monitor, restrict, or limit the behavior of various types of bots. To learn more, see [AWS WAF Bot Control](https://docs.aws.amazon.com/waf/latest/developerguide/waf-bot-control.html) in the *AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.

Account takeover is an unlawful online activity where an unauthorized individual gains access to someone else's account. When the attacker has access, they can steal money, data, or services from the victim's account. The **AWS WAF Fraud Control account takeover prevention (ATP)** feature uses a predefined set of rules to block account takeover attempts on your applications. To learn more, see [AWS WAF Fraud Control Account Takeover Prevention (ATP)](https://docs.aws.amazon.com/waf/latest/developerguide/waf-atp.html) in the *AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.

You can also use AWS WAF to run additional actions to safeguard your applications from unauthorized users. The **CAPTCHA (Completely Automated Public Turing test to tell Computers and Humans Apart)** action requires the end-user to solve a simple puzzle, which is designed to be easily completed by humans but difficult for bots or automated systems. The Challenge action runs a silent verification process in the background to determine if the client session is a legitimate browser rather than a bot. To learn more, see [CAPTCHA and Challenge in AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-captcha-and-challenge.html) in the *AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.

---

### Knowledge Check

#### What is Security Automations for AWS WAF?

* It is an AWS CloudFormation template with preconfigured security automations.

Wrong answers:

* It is a set of AWS managed protections against common vulnerabilities.
* It is a set of rule groups managed by AWS Marketplace Sellers.
* It is a feature that defines the criteria for inspecting web requests.

##### Explanation

**Security Automations for AWS WAF consists of a CloudFormation template with preconfigured security automations.**

AWS Managed Rules for AWS WAF provides protection against common application vulnerabilities. AWS Marketplace managed rule groups is a set of rule groups managed by AWS Marketplace sellers. Rule statements define the criteria for inspecting web requests.

#### Which AWS WAF feature helps prevent fraudulent account creation attempts?

* Account creation fraud prevention (ACFP)

Wrong answers:

* Web access control list (web ACL)
* AWS WAF Bot Control
* Fraud Control account takeover prevention (ATP)

##### Explanation

**The account creation fraud prevention (ACFP) feature helps detect and prevent fraudulent account creation attempts on your application's sign-up page.**

You use a web ACL to protect a set of AWS resources. The AWS WAF Bot Control feature helps you manage and protect your web applications from unwanted bot activity. The AWS WAF Fraud Control account takeover prevention (ATP) feature uses a predefined set of rules to block account takeover attempts on your applications.

#### What is a regex pattern set?

* It is a collection of regular expressions that can be used together in a rule statement.

Wrong answers:

* It is a collection of IP addresses and IP address ranges that can be used together in a rule statement.
* It is a statement that dictates how to inspect web requests.
* It is a web application firewall that can be used to monitor the HTTP and HTTPS requests.

##### Explanation

**A regex pattern set is a collection of regular expressions that can be used together in a rule statement.**

An IP set is a collection of IP addresses and IP address ranges. Rule statements are statements that dictate how to inspect web requests. AWS WAF is a web application firewall that you can use to monitor the HTTP and HTTPS requests.

---

### Summary

AWS WAF is a web application firewall that you can use to monitor the HTTP and HTTPS requests that are forwarded to Amazon CloudFront, Amazon API Gateway, an Application Load Balancer, AWS AppSync, or Amazon Cognito. AWS WAF covers the application layer (Layer 7) in the OSI model. The following are some of the benefits of AWS WAF:

* **Frictionless setup**: You can deploy without changing your existing architecture, with no need to configure TLS/SSL certificates or change DNS configuration.
* **Low operation overhead**: You have ready-to-use AWS CloudFormation templates, built-in SQL injection/cross-site scripting (SQLi/XSS) exploit detection, and managed rules through AWS Marketplace. You can optionally create your own custom rules.
* **Customizable security**: AWS WAF has a highly flexible rule engine that can inspect any part of incoming requests under single-millisecond latency.
* **API-driven architecture**: With API-driven architecture and fast rule propagation, you can detect and respond to threats in real time.

#### AWS WAF overview

AWS WAF offers protection against web attacks using conditions that you specify. You can define conditions by using characteristics of web requests, such as the following:

* IP addresses that requests originate from
* The country that requests originate from
* Values in request headers
* Strings that appear in requests, either specific strings or strings that match regular expression (regex) patterns
* Length of requests
* Presence of SQL code that is likely to be malicious (known as SQL injection)
* Presence of a script that is likely to be malicious (known as cross-site scripting)

#### AWS WAF rule types

Aside from creating your own custom rules, there are three different mechanisms for automating the building and maintenance of AWS WAF rules: AWS Managed Rules, AWS Marketplace managed rule groups, and AWS CloudFormation templates.

AWS Marketplace managed rule groups are available by subscription through the AWS Marketplace console at AWS Marketplace. After you subscribe to an AWS Marketplace managed rule group, you can use it in AWS WAF. To use an AWS Marketplace rule group in an AWS Firewall Manager AWS WAF policy, each account in your organization must subscribe to it. In addition, CloudFormation templates such as AWS Security Automations can create rules automatically.

#### AWS WAF web ACLs main components

* **Rule groups**: You can use rules individually or in reusable rule groups. AWS Managed Rules and AWS Marketplace sellers provide managed rule groups for your use. You can also define your own rule groups.
* **Rule statements**: This is the part of a rule that tells AWS WAF how to inspect a web request. When AWS WAF finds the inspection criteria in a web request, we say that the web request matches the statement.
* **IP set**: A collection of IP addresses and IP address ranges that you can use together in a rule statement.
* **Regex pattern set**: A collection of regular expressions that you can use together in a rule statement.

---
