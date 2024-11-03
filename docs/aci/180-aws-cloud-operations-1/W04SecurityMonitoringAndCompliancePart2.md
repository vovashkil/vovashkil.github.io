# Security, Monitoring, and Compliance Part 2

* **back to AWS Cloud Institute repo's root [aci.md](../aci.md)**
* **back to repo's main [README.md](../../../README.md)**

## EventBridge Deep Dive

### Security and compliance benefits of EventBridge

* **Centralized auditing and logging:** With EventBridge, you can centrally log events and API calls from various AWS services and your applications. This provides a unified view of activity for auditing and compliance.
* **Fine-grained access controls:** You can set detailed permissions about who can publish events to, and consume events from, an event bus for strict access controls.
* **Encryption of data in transit and at rest:** EventBridge encrypts all data as it travels between EventBridge services and it encrypts data at rest. This helps prevent unauthorized access.
* **Compliance with various standards:** EventBridge is compliant with various standards and regulations like SOC, ISO, and PCI DSS. This makes it suitable for building compliant applications.
* **Integration with CloudTrail:** EventBridge API calls are logged in CloudTrail to provide further auditing visibility. CloudTrail is widely used for compliance.
* **Security monitoring and alerting:** With EventBridge, you can detect security incidents and threats by creating rules that match events and initiate alerts or actions.
* **Serverless:** EventBridge is fully managed and serverless. This removes considerable security and compliance burdens related to infrastructure management.

EventBridge is a serverless service provided by AWS. You can use it to connect application components in a scalable and event-driven architecture. It uses events to initiate actions in connected applications, which makes it easier for developers to build applications that are more agile and reliable.

Event-driven architecture is a style of building software that is loosely coupled. By using EventBridge, developers can quickly build and deploy applications that are more scalable and easier to maintain.

### Key concepts

#### Events

An EventBridge event is a JSON object sent to an event bus or pipe. In the context of event-driven architecture (EDA), an event often represents an indicator of a change in a resource or environment.

#### Event buses

An event bus is a router that receives events and delivers them to zero or more destinations or targets. Use an event bus when you need to route events from many sources to many targets with optional transformation of events before delivery to a target.

#### Event sources

EventBridge can receive events from event sources including the following:

* AWS services
* Custom applications
* SaaS partners

#### Rules

A rule receives incoming events and sends them as appropriate to targets for processing. You can specify how each rule invokes its targets based on either of the following:

* An event pattern, which contains one or more filters to match events. Event patterns can include filters that match on the following:
* Event metadata: Data about the event, such as the event source, or the account or Region in which the event originated
* Event data: The properties of the event itself—these properties vary according to the event
* Event content: The actual property values of the event data
* A schedule to invoke the targets at regular intervals. You can specify a scheduled rule within EventBridge or by using EventBridge Scheduler.

**EventBridge offers EventBridge Scheduler, a serverless scheduler you can use to create, run, and manage tasks from one central, managed service. EventBridge Scheduler is highly customizable and offers improved scalability over EventBridge scheduled rules. It has a wider set of target API operations and AWS services. We recommend you use EventBridge Scheduler to invoke targets on a schedule.**

Each rule is defined for a specific event bus and only applies to events on that event bus. A single rule can send an event to up to five targets.

By default, you can configure up to 300 rules per event bus. This quota can be raised to thousands of rules in the Service Quotas console. Because the rule limit applies to each bus, if you require even more rules, you can create additional custom event buses in your account.

You can customize how events are received in your account by creating event buses with different permissions for different services. To customize the structure or date of an event before EventBridge passes it to a target, use the input transformer to edit the information before it goes to the target.

#### Targets

A target is a resource or endpoint to which EventBridge sends an event when the event matches the event pattern defined for a rule. A target can receive multiple events from multiple event buses. The following are examples of EventBridge targets:

* API gateway
* AWS CodePipeline
* Amazon EC2 TerminateInstances API call
* Amazon Elastic Container Service (Amazon ECS) task
* Lambda function (ASYNC)

### EventBridge pricing

With EventBridge, customers pay for events published to an event bus and events ingested for Schema Discovery and event replay. There are no additional charges for rules or event delivery. There are no minimum fees or upfront commitments. All state change events published by AWS services have no charge.

#### Event buses

AWS Free Tier: All state change events published by AWS services by default have no charge.

The pricing of custom events, third-party SaaS events, and cross-account events varies by Region.

Size of payloads: Each 64 KB chunk of a payload is billed as 1 event. For example, an event with a 256 KB payload is billed as 4 requests.

Customers can incur additional data transfer charges among Regions for cross-Region invocations. You will be billed at standard AWS Data Transfer Charges. There is no additional charge for global endpoints. Custom events published to the global endpoint are billed according to the custom events pricing.

**Pricing example:**

If your SaaS application published 5 million events in 1 month, your charges would be calculated as follows:

* Monthly events = 5 M events (all equal to or less than 64 KB each)
* Monthly events charges = 5 M * $1.00/M = $5.00 per month

#### Pipes

EventBridge pipes help customers create point-to-point integrations between event producers and consumers with optional transform, filter, and enrich steps. Pricing varies by Region.

**Size of payload:** Each 64 KB chunk of payload is billed as 1 request. For example, a batch of events with a 256 KB payload is billed as 4 requests.

**Pricing example:**

If your source Amazon SQS queue receives 10 million events in 1 month, you apply a filter that matches 25 percent of your records, and you batch 5 events per request, your charges for sending those matching records to a target would be as follows:

*Usage:*

* Monthly requests sent = 10,000,000 * 25%/5 = 500,000
* Requests after filtering = 500,000

*Charges:*

* Requests after filtering = 0.5 M * $0.40/M = $0.20
* Total monthly EventBridge charges = $0.20

#### Scheduler

**Free Tier:** As part of the Free Tier, customers can get started with EventBridge Scheduler at no cost. You can make 14,000,000 invocations per month for free. Some applications can operate within the Free Tier. Pricing for additional invocations varies by Region.

**Pricing example:**

If your application schedules 10 million recurring schedules that invoke twice each month in Region US West, your charges would be as follows:

*Usage:*

* Monthly recurring schedules = 10 M * 2 = 20 M
* Monthly invocations = 20 M

*Charges:*

* Monthly invocations: (20 M – 14 M Free Tier) * $1.00/M = $6.00
* Total charges: $6.00 per month

*The usage of the Free Tier is calculated each month across all Regions (except AWS GovCloud) and is applied to the bill automatically. Unused Free Tier usage does not roll over to the next month.

#### API destinations

API destinations help you send events from an EventBridge event bus to any web-based application.

**Size of payloads:** Each 64 KB chunk of a payload is billed as 1 event (for example, an event with a 256 KB payload is billed as 4 requests). You might incur additional data transfer charges for data out to the internet. You will be billed at standard AWS data transfer charges.

**Pricing example:**

If you invoke 2 million events in 1 month from your event bus endpoint to an HTTP endpoint, your charges would be as follows:

* Monthly events = 2 M events
* Monthly API destination charges = 2 M * $0.20/M = $0.40 per month

#### Event replay

Customers can specify event patterns to determine which events they want to archive for replay. The pricing of archival processing varies by Region. For replay, customers are billed as per the custom events pricing.

**Pricing example:**

If your application published 2 million events in 1 month, each averaging 6 KB, and you enabled archiving on your development event bus for replay, and you replay all of them, your charges would be calculated as follows:

* Monthly events = 2 M events * $1.00/M = $2.00 per month
* Archive processing = 2 M events * 6 KB/(1024 * 1024) * $0.10/GB = $1.14
* Storage costs = 2 M events * 6 KB/(1024*1024) * $0.023/GB = $0.26 per month
* Replayed events = 2 M * $1.00/M = $2.00 per month

* Total monthly EventBridge charges = $2 (event publishing) + $1.14 (archive processing) + $0.26 (storage) + $2.00 (replaying) = $5.40 per month

#### Schema registry

Usage of the Schema Registry for AWS and custom schemas is free. The Schema Discovery feature of the Schema Registry includes a Free Tier of 5 million ingested events per month. In most development use cases where you use discovery in your development environment, your usage should stay within the Free Tier.

For additional usage outside of the Free Tier, such as if you wanted to use Schema Discovery to audit all events passing through your production event bus, you will be charged at a price dependent on the Region.

**Size of payloads:** Each 8 KB chunk of a Schema Discovery payload is billed as 1 ingested event (for example, an event with a 16 KB payload is billed as 2 ingested events).

The EventBridge Schema Registry is available in the following regions: US East (Ohio), US East (N. Virginia), US West (N. California), US West (Oregon), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Canada (Central), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Europe (Stockholm), and South America (São Paulo).

**Pricing example:**

If your development environment published 2 million events in 1 month, each averaging 2 KB, and you enabled Schema Discovery on your development event bus, your charges would be calculated as follows:

* Monthly events = 2 M events * $1.00/M = $2.00 per month
* Schema Registry = Free
* Schema Discovery = 2 M events. No additional discovery costs (5 M events included in Free Tier)

* Total monthly EventBridge charges = $2.00 (event publishing) + $0 (Schema Registry) + $0 Schema Discovery = $2.00 per month

### Securing applications through decoupling architectures

With decoupling, a builder creates individual IAM roles that can be used to follow the principle of least privilege for the services to which the role is assigned. For example, you can create a monolithic application that needs permissions to read, write, modify, and create. This means you would need an IAM role that allows all those actions. 

You can break up that monolithic app into several microservices, each with its individual role and policies that allow it to carry out its actions. If one microservice is exposed to an attack, the attacker would only be able to use the permission level assigned to that service. Additionally, event-driven architectures make it possible to analyze attacks using services such as CloudTrail logs.

### Event Buses

An event bus is a router that receives events and delivers them to zero or more destinations or targets. Event buses are well-suited for routing events from many sources to many targets with optional event transformation before delivering to a target. When you create rules in EventBridge, these are associated with a single event bus.

#### Default event bus

AWS accounts include a default event bus that automatically receives events from AWS services.

#### Custom event bus

Custom event buses can be created to receive only specific events.

#### Partner event bus

These events receive events from SaaS partners.

### Event buses in action

With event buses, you can route events from multiple sources to multiple destinations or targets.

1. An event source, which can be an AWS service, your custom application, or an SaaS provider, sends an event to an event bus.
2. EventBridge then evaluates the event against each rule defined for that event bus.
3. For each event that matches a rule, EventBridge sends the event to the targets specified for that rule.
 a. Optionally, as part of the rule, you can also specify how EventBridge should transform the event before sending it to the targets. An event might match multiple rules, and each rule can specify up to five targets. An event might not match any rules, in which case EventBridge takes no action.

### Event bus example

Consider an example using the EventBridge default event bus, which automatically receives events from AWS services.

#### Create a rule

You create a rule on the default event bus for the **EC2 Instance State-change Notification** event.

You specify that the rule matches events where an EC2 instance has changed its **state** to **running**.

You do this by specifying JSON that defines the attributes and values that an event must match to activate the rule. This is called an *event pattern*. You specify the target of the rule to be a given Lambda function.

```
{
  "source": ["aws.ec2"],
  "detail-type": ["EC2 Instance State-change Notification"],
    "detail": {
      "state": ["running"]
  }
}
```

#### Event is sent

Whenever an EC2 instance changes state, Amazon EC2 (the event source) automatically sends that event to the default event bus.

#### Event is evaluated

EventBridge evaluates all events sent to the default event bus against the rule you've created.

If the event matches your rule (that is, if the event was an EC2 instance changing state to running), EventBridge sends the event to the specified target. In this case, that's the Lambda function.

### Using Event Buses

#### Sending events to a target service

You can configure EventBridge to send and receive events between event buses in the same AWS account and Region. When you configure EventBridge to send or receive events between event buses, you use IAM roles on the sender event bus to give the sender event bus permission to send events to the receiver event bus.

You use resource-based policies on the receiver event bus to give the receiver event bus permission to receive events from the sender event bus. You can also allow or deny events from certain event buses, specific rules associated with the event bus, or events from specific sources. For more information about event bus permissions, including example policies, see [Permissions for Amazon EventBridge event buses](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus-perms.html).

These are the steps to configure EventBridge to send events to, or receive events between, event buses in your account:

* To use an existing IAM role, you need to give either the sender event bus permissions to the receiver event bus or the receiver event bus permissions to the sender event bus.
* On the sender event bus, set up one or more rules that have the receiver event bus as the target and create an IAM role. For an example of the policy that should be attached to the role, see Example policy: Send events to an event bus in the same account.
* On the receiver event bus, edit the permissions to allow events to be passed from the other event bus.
* On the receiver event, set up one or more rules that match events that come from the sender event bus.

**EventBridge can not route events received from a sender event bus to a third event bus.**

#### Creating an event bus

##### Provide a name

##### Event archive

Archiving events is a good way to troubleshoot errors or test new functionality by replaying the events in the archive. You can archive all events on the event bus or define an event pattern and only archive specific events. Events are encrypted using 256-bit Advanced Encryption Standard (AES-256) to protect against unauthorized access to your data.

##### Schema

When you enable Schema Discovery, the schema or structure of all events that get processed by the event bus are stored in the Schema registry. After they are in the registry, you can download them and use them to speed up the development of new features.

When a rule runs in EventBridge, all the targets associated with the rule are invoked. Rules can invoke Lambda functions, publish to SNS topics, or relay the event to Amazon Kinesis Data Streams. To make API calls against the resources you own, EventBridge needs the appropriate permissions. For Lambda, Amazon SNS, Amazon SQS, and CloudWatch Logs resources, EventBridge uses resource-based policies. For Data Streams, EventBridge uses identity-based policies.

#### Routing events

A rule matches incoming events and sends them to targets for processing. A single rule can send an event to multiple targets, which then run in parallel. Rules are based either on an event pattern or a schedule. An event pattern defines the event structure and the fields that a rule matches. Rules that are based on a schedule perform an action at regular intervals.

AWS services can create and manage EventBridge rules in your AWS account that are needed for certain functions in those services. These are called managed rules.

When a service creates a managed rule, it can also create an IAM policy that grants permission to that service to create the rule. IAM policies created this way are scoped narrowly with resource-level permissions to allow the creation of only the necessary rules.

You can delete managed rules by using the Force delete option, but you should only delete them if you're sure that the other service no longer needs the rule. Otherwise, deleting a managed rule can cause the features that rely on it to stop working.

This allows you to build event-driven applications where you can perform custom logic when specified events occur. If you have more than one target, the event is sent to the targets in parallel. If the event is not delivered successfully to the target, EventBridge retries for up to 24 hours. You can have up to 300 rules per AWS account per Region, which can be increased upon request.

For more resources on learning about events, go to [s12d.com/aboutevents](https://s12d.com/aboutevents).

##### Routing using an event pattern

To create an event pattern, you specify the fields of an event that you want the event pattern to match. Only specify the fields that you use for matching. EventBridge ignores all the other fields in the event when applying the rule.

For an event pattern to match an event, the event must contain all the field names listed in the event pattern. The field names must also appear in the event with the same nesting structure.

When you write event patterns to match events, you can use the TestEventPattern API or the test-event-pattern CLI command to test that your pattern matches the correct events. For more information, see [TestEventPattern](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_TestEventPattern.html).

EventBridge supports declarative event content filtering using event patterns. This allows you to create complex patterns that only match under specific circumstances. In the EventBridge console, when you create a rule, there's a section on matching events that's based upon predefined patterns by AWS service.

By building highly specific event patterns, you can have the EventBridge service perform event filtering for you, reducing the amount of downstream work for your rule targets. This can help reduce the amount of custom code in your application.

For a list of resources shown in this video and more information about events, visit [s12d.com/aboutevents](https://s12d.com/aboutevents).

##### Routing using an event that runs on a schedule

EventBridge runs these rules at specific times and dates; for example, 8:00 AM PST on the first Monday of every month. To specify the time and dates a scheduled rule runs, you define a cron expression.

Rate expressions are simpler to define, while cron expressions offer detailed schedule control. For example, with a cron expression, you can define a rule that runs at a specified time on a certain day of each week or month. In contrast, rate expressions run a rule at a regular rate, such as once every hour or once every day.

Rules can be triggered by a scheduled event. For example, you can invoke a Lambda function every 15 minutes using an EventBridge rule. You define a schedule by either using a rate or a cron expression. Rate expressions allow you to select regular intervals using minutes, hours, or days. These are ideal for simple schedules. Cron expressions are more powerful. These consist of six required fields that represent the minute, hour, day of month, month, day of week, and year.

If you're using the AWS Serverless Application Model to develop serverless applications, there's a pattern available in the Serverless Land Patterns collection. This pattern creates a scheduled EventBridge rule to invoke a Lambda function.

You can find this pattern and the deployment instructions at [s12d.com/events-7](https://s12d.com/events-7).

For more information about events, visit [s12d.com/aboutevents](https://s12d.com/aboutevents).

### [Lab: Using Amazon EventBridge](./W04Lab1-EventBridge.md)

### Using API Destinations

With the API destinations feature, EventBridge can integrate with services outside of AWS by using REST API calls. This enables developers to route events to existing SaaS providers that integrate with EventBridge, like Zendesk, PagerDuty, TriggerMesh, or MongoDB.

#### Steps to integrate external services using API calls and EventBridge

API destinations are third-party partner targets that you can invoke using an HTTP endpoint. This lets you seamlessly integrate your applications with a range of SaaS partners without having to write code or deploy additional infrastructure.

With API destinations, you can easily build modern SaaS-connected solutions, and reduce data silos by simplifying information exchange between applications.

##### Navigate to the AWS EventBridge console

In the Integration section, choose API Destinations. Next, choose Create API destination.

On the next screen, perform the following actions:

* Provide a name and optional description
* Set an API destination point—this is the URL endpoint to invoke as the target
* Set the HTTP method, such as GET, POST, or PUT
* Set an invocation rate limit if you want
* And finally, either use an existing connection or create a new one

Each API destination uses a Connection that defines the authorization method and credentials to use to connect to the HTTP endpoint. Here we will fill out the connection details. First provide a name and optional description for the connection.

Next, set the authorization destination type—this is the type of destination this connection will authorize. You have two options, Partners and Other. We are going to choose [INSERT CHOICE]

Next, we need to provide the authorization type that will access the API destination. A secret for this connection will be stored in AWS Secrets Manager. We have the following choices:

* Basic, which is a username and password
* OAuth client credentials
* And an API Key

Now, choose Create. Once the connection is authorized, create the API Destination itself.

Specify the endpoint URL, choose an HTTP method such as POST or GET, and set an invocation limit to prevent overloading the third-party service. Now that we have an API Destination with a connection set up, let's create a rule to route events to it.

#### Creating a rule

In the EventBridge console, under the Buses section, choose Rules and then Create rule.

We are going to provide a name and description for our rule. Next, we will select an event bus for the rule – let’s use the default bus. We are going to create our rule based on an event pattern, so let’s leave rule type at its default and choose Next.

On the next page, I’m going to leave the Event source at the default setting—AWS events or EventBridge partner events. Next, there is a section where you can view sample events. These can be used to help you create your own event pattern. Now, let’s set up our event pattern. We are going to keep the source set to AWS services and then choose EC2 as the service for our rule.

Now, I am going to define a custom event pattern here for EBS Snapshot Notifications. This rule will send an event whenever a snapshot is shared—whether the share succeeded or failed. Now that I have my event pattern, I’m going to choose Next. Here, I’ll specify the target as the API Destination I created earlier. Notice that Amazon EventBridge automatically picks up the endpoint and connection details.

Similar to how I was able to create the connection when creating the API destination, I can also choose to create a new API destination here. Once we have selected the API destination, we need to choose an execution role. This is the role that will send events to the API destination. We can create a new role for this or use an existing role. Let’s use an existing one.

Now, I’m going to choose Next. On this page, I could elect to configure some tags for this rule. Tags can help you search and filter your resources or track your AWS costs. Let’s choose Next. On this finale page, you can review your rule for accuracy, and then choose Create rule.

We have successfully set up an API Destination in Amazon EventBridge to integrate with external services via a REST API call. Now, whenever an EBS snapshot notification occurs in my account EventBridge will automatically deliver this to the API endpoint.

### Demo: Archiving and Replaying EventBridge Events

Sometimes you need to reprocess past events. You can create an encrypted archive of the events published to an event bus. You can archive all events or filter them using the same pattern-matching syntax used by EventBridge rules. You can store events indefinitely or set up a retention period after which older events are automatically removed from the archive.

You can also replay the events stored in an archive. Events are replayed to all rules defined for the event bus (but not to managed rules created by other AWS services) or the rules you specify. Replayed events contain an extra replay-name field in case you need to recognize them. When starting a replay, you define a time frame. Only the events within that time frame are replayed. Currently, you can only replay events to the same event bus from which they were archived.

There are many use cases where this is useful, for example:

* After you fix a bug, you can reprocess the impacted events to get the correct result. This approach assumes that your application can process the same event multiple times.
* When you release a new feature, you can reprocess previous events to extend the reach of the feature to past data. For instance, a fraud detection system that has been added to your application can have access to new accounts and past accounts that were created in the previous weeks or months.

Archives and replays work with all events processed by EventBridge, including events from the AWS services, from SaaS integrations, and your custom events.

Event Replay can be incredibly useful in various scenarios:

* **Code testing:** After making code fixes, you can replay historical events to test how your changes affect behavior.
* **Testing new features:** When testing new features, using historical production data from event archives allows you to measure performance under real-world conditions. 
* **Development and testing:** You can use event replay to hydrate development or test environments. Hydrating an environment makes it more realistic and closer to the production setup.

#### Event Archive and replaying events

##### Creating an Archive

Navigate to the Amazon EventBridge console and under the Buses section, choose Archive.

* On the next page, choose Create archive.
* Give the archive a name — it’s important to note that once the archive is created, you cannot change the name.
* Choose the source bus. Each archive can be attached to only one source bus. Use the my-workload bus which has been already configured.
* Set the retention period which is the number of days the archive of events will be retained.  If it is set to 0, it is the same as indefinite. The maximum number of days it can retain is 2 billion years. Set it to 7 days.
* Choose Next. This an optional page where an event pattern for filtering can be provided. Skip this step and choose Create archive.
* Any events that goes through the my-workload custom bus will be automatically added to this archive. To observe the events, create a rule on the my-workload custom event bus.

##### Creating a rule

* Navigate to Rules under the Buses section and choose Create rule. Give it a name, my-rule, choose the my-workload bus, and choose Rule with an event pattern. Choose Next.
* For the event source, keep it at the default AWS events or EventBridge partner events. For the event, choose Use pattern form for the Creation method. Choose Next.
* Choose a target - CloudWatch log group, and enter my-group for the log group. We can now navigate to the next page by choosing Next. Skip the Tag group and choose Next.
* Review our rule, and choose Create. Now everything going through the my-workload bus will be logged in the Amazon CloudWatch log group my-group. 

Send some test events by navigating to the Event buses page in the Buses section and choosing Send events.

* Select the my-workload custom bus and give it an event source, detail type and event detail. Duplicate this event so we have multiple events being sent. Next, choose Send and see a confirmation page.
* These events have now been logged according to the rule just set up. 

##### Creating a replay

* Go to Replays, which is under the Buses section and choose Start new replay. Give it a name, my-replay, and then choose a source. Every time you replay an archive, it must be sent to the same bus the event came from.
* You can either have all the rules or specify which rules run on the event bus. Choose All rules. Provide a timeframe. Set it to two days in the past through the end of today.
* Start the Replay. The replay is now in a starting status. Replay is not immediate; it can take a couple of minutes. The statuses it can be are Starting, Running, Completed, Failed, Cancelling, and Canceled. For this archive we have only two events, so now with the Replay we will have four total events now.

##### Navigating events on the bus

* Navigate to the original rule and the event bus. Go to my Buses and my logging rule, which is logging in CloudWatch logs. You can see the original events and replayed events. the last have the my-replay name attribute.

### EventBridge Schemas

EventBridge includes schemas for all AWS services that generate events.

A schema defines the structure of events that are sent to EventBridge. EventBridge provides schemas for all events that are generated by AWS services, but you can also create or upload custom schemas or infer schemas directly from events on an event bus.

After you have a schema for an event, you can download code bindings for popular programming languages and speed up development. You can work with code bindings for schemas and manage schemas from the EventBridge console, by using the API, or directly in your IDE by using the AWS toolkits. To build serverless apps that use events, use AWS Serverless Application Model (AWS SAM). EventBridge supports both OpenAPI 3 and JSONSchema Draft4 formats.

You can find these schemas in the EventBridge console, or you can find them by using the API action, SearchSchemas.

#### Schema registries

Schema registries are containers for schemas. Schema registries collect and organize schemas so that your schemas are in logical groups. The following are the default schema registries:

* **All schemas:** All the schemas from the AWS event, the discovered schemas registry, and custom schema registries
* **AWS event schema registry:** The built-in schemas
* **Discovered schema registry:** The schemas discovered by Schema discovery

You can create custom registries to organize the schemas you create or upload.

1. **Navigate to EventBridge.** Open the [Amazon EventBridge](https://console.aws.amazon.com/events/) console.
2. **Create registry.** In the navigation pane, choose **Schemas** and then **Create registry**.
3. **Fill in details.** On the **Registry details** page, enter a **Name**. You can also enter a **Description**, but this is optional. Then choose **Create**.
4. **Add schema.** To create a custom schema in your new registry, choose **Create custom schema**. To add a schema to your registry, select that registry when you're creating a new schema.
5. **Create the schema.** Enter a **Schema name**. You can optionally enter a **Description**. Choose your schema format, OpenAPI 3.0 or JSON Schema Draft 4. Enter your schema. There are templates available to get you started. Then, choose **Create**.
6. The schema and registry will now be visible on the Schemas page in the EventBridge console.

### PutEvents API

After events are sent to another service, you can receive them through either the public endpoint or a VPC endpoint for that service. For example, if you create a rule to send events to an Amazon SQS queue, you can configure an interface VPC endpoint for Amazon SQS to receive messages from that queue in your VPC without using the public endpoint.

From an application development point-of-view, this is all accomplished using the PutEvents API that sends custom events to EventBridge so they can be matched to rules.

The maximum size for a PutEvents event entry is 256 KB. The entry size calculation includes the event and any necessary characters and keys of the JSON representation of the event. PutEvents accepts the data in JSON format. The EndpointID parameter is a string and contains the URL subdomain of the endpoint. It can be 1–50 characters long. After you have created a global endpoint, you will need to add the EndpointId and EventBusName to any PutEvents calls that you use. The Entries parameter defines the event in the system. This parameter is an array of the following PutEventsRequestEntry objects.

#### Source

The Source object is the source of the event. It is a string.

#### DetailType

The DetailType object is a free-form string.

#### Detail

The Detail object is a valid JSON object with no imposed schema and can contain fields and nested sub-objects.

#### EventBusName

The EventBusName object is a string containing the name or Amazon Resource Name (ARN) of the event bus that receives the event.

### Establishing Global Endpoints

You can improve your application's availability with EventBridge global endpoints. Global endpoints help make your application Regional-fault tolerant at no additional cost. To start, you assign an Amazon Route 53 health check to the endpoint. When failover is initiated, the health check reports an “unhealthy” state.

Within minutes of failover initiation, all custom events are routed to an event bus in the secondary Region and are processed by that event bus. After the health check reports a “healthy” state, events are processed by the event bus in the primary Region. Application availability relates to regulatory compliance in a few key ways:

* Many regulations require organizations to maintain high availability of critical systems and data. For example, financial regulations often mandate high uptime for trading systems or access to customer account data. Healthcare regulations also often require high availability of systems like electronic health records.
* Outages and downtime of critical systems can equate to non-compliance with availability requirements in regulations. Organizations have to architect their systems and implement measures like redundancy to try to avoid outages that could violate regulatory standards.
* Logging and auditability are important for compliance. If systems go down, the ability to reconstruct activities leading up to the outage using logs and backups becomes important for demonstrating compliance.
* Following defined change management procedures and processes is also often required for compliance. Unplanned outages because of improper changes or maintenance can violate change control policies that are part of compliance regimes.
* Organizations subject to regulations are often required to implement incident response and disaster recovery plans that focus on bringing systems back online in a timely manner in the event of an outage. These are critical for availability and related compliance.

When you use global endpoints, you can enable event replication. Event replication sends all custom events to the event buses in the primary and secondary Regions using managed rules.

**If you're using custom buses, you will need a custom bus in each Region with the same name and in the same account for failover to work properly.**

#### Creating an EventBridge global endpoint

##### Prior to set up

Complete the following steps to set up a global endpoint:

* Make sure that you have matching event buses and rules in both the primary and secondary Region.
* Create a Route 53 health check to monitor your event buses. For assistance in creating your health check, choose New Health Check when creating your global endpoint.

##### Navigate to EventBridge

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events](https://console.aws.amazon.com/events).
2. In the navigation pane, choose **Global endpoints**.

##### Create endpoint

Choose **Create Endpoint**.

##### Name and describe your global endpoint

Enter a name and description for the endpoint.

##### Choose an event bus

For Event bus in a Primary Region, choose the event bus you would like the endpoint to be associated with.

##### Secondary Region

For Secondary Region, choose the Region you'd like to direct events to in the event of a failover.

##### Choose a health check

For Route 53 health check for triggering failover and recovery, choose the health check that the endpoint will monitor. If you don't already have a health check, choose **New Health check** to open the AWS CloudFormation console, and create a health check using a CloudFormation template.

##### (Optional) Event replication

For Event replication, do the following:

1. Select **Event replication enabled**.
2. For Execution role, choose whether to create a new IAM role or use an existing one. Do the following:
 * Choose **Create a new role** for this specific resource. Optionally, you can update the Role name to create a new role.
 * Choose **Use existing role**. Then, for Execution role, choose the desired role to use.

##### Create the global endpoint

Choose **Create**.

### Activity: Amazon EventBridge Use Cases

#### One of our biggest challenges is that we have separate security processes for everything. Our custom applications use different ones, and then we have processes specific to the AWS services in use. Is there a way EventBridge can help with this?

* EventBridge provides a central event bus that can integrate events and triggers from all AWS services as well as custom applications.

#### Are there ways EventBridge could help us with security events after they happen?

* If an application is built on EventBridge, the logs application's events could be sent tp CloudTrail Logs. When there, the events could be analyzed to see what vulnerability was exploited.

EventBridge is great for securing applications through decoupling and creating events that can be analyzed to pinpoint security vulnerabilities in other AWS services.

The following are some other use cases:

* **Audit trails:** EventBridge can track important events happening across an infrastructure and applications. This provides detailed audit trails that can help demonstrate compliance with regulations.
* **Separation of duties:** EventBridge can help segment and control access to event busses and rules. This supports the principle of least privilege and separation of duties for compliance.
* **Remediation workflows:** EventBridge can initiate automated remediation workflows if a compliance violation or security risk is detected in application events. This enables a faster response.

### Knowledge Check

#### Which part of Amazon EventBridge enables event routing and processing?

* Rules

Wrong answers:

* Amazon Kinesis Data Streams
* EventBridge pipes
* Partner event sources

The other options are incorrect for the following reasons:

* Data Streams are real-time streams from a different service —Amazon Kinesis.
* EventBridge pipes provide a seamless means of integrating supported AWS and self-managed services, which favors configuration over code.
* Partner event sources are used to receive events from software as a service (SaaS) partner applications.

#### Which language is used to define custom schema registries in Amazon EventBridge?

* JSON

Wrong answers:

* HTML
* XML
* Python

You can create schemas by using JSON files with either the OpenAPI Specification or the JSONSchema Draft4 specification. You can create or upload your own schemas in EventBridge by using a template or generating a schema based on an event’s JSON code.

#### Which language is used to define an event pattern in Amazon EventBridge?

* JSON

Wrong answers:

* HTML
* XML
* Python

### Summary

#### Events

At its simplest, an EventBridge event is a JSON object sent to an event bus or pipe. In the context of EDA, an event often represents an indicator of a change in a resource or environment.

Event sources send events to EventBridge. They are then routed using Event buses to targets.

##### Event buses

An event bus is a router that receives events and delivers them to zero or more destinations or targets.

##### Event sources

EventBridge can receive events from event sources including AWS services, custom applications, and SaaS partners.

##### Targets

A target is a resource or endpoint to which EventBridge sends an event when the event matches the event pattern defined for a rule. A target can receive multiple events from multiple event buses.

#### Rules

A rule receives incoming events and sends them as appropriate to targets for processing. You can specify how each rule invokes their targets based on either of the following:

* An event pattern
* A schedule

#### API destinations

With the API destinations feature, EventBridge can integrate with services outside of AWS by using REST API calls. Developers can route events to existing SaaS providers that integrate with EventBridge, like Zendesk, PagerDuty, TriggerMesh, or MongoDB.

#### Archives and replays

You can create an encrypted archive of the events published to an event bus. You can archive all events or filter them using the same pattern-matching syntax used by EventBridge rules. You can store events indefinitely or set up a retention period after which older events are automatically removed from the archive.

You can also replay the events stored in an archive. Events are replayed to all rules defined for the event bus (but not to managed rules created by other AWS services) or the rules you specify. Replayed events contain an extra replay-name field in case you need to recognize them. 

When starting a replay, you define a time frame, and only events within that time frame are replayed. Currently, you can only replay events to the same event bus from which they were archived.

#### Schemas

A schema defines the structure of events that are sent to EventBridge. EventBridge provides schemas for all events that are generated by AWS services, but you can also create or upload custom schemas or infer schemas directly from events on an event bus.

Schema registries are containers for schemas. Schema registries collect and organize schemas so that your schemas are in logical groups. The following are the default schema registries:

* **All schemas:** All the schemas from the AWS event, discovered schema registry, and custom schema registries
* **AWS event schema registry:** The built-in schemas
* **Discovered schema registry:** The schemas discovered by Schema Discovery

#### PutEvents API

The PutEvents API sends custom events to EventBridge so they can be matched to rules. It contains the following parts:

* Detail
* DetailType
* EventBusName
* Resources
* Source
* Time
* TraceHeader

#### Global endpoints

You can improve an application's availability with EventBridge global endpoints. Global endpoints help make your application Regional-fault tolerant at no additional cost. To start, you assign a Route 53 health check to the endpoint. When failover is initiated, the health check reports an unhealthy state.

Within minutes of failover initiation, all custom events are routed to an event bus in the secondary Region and are processed by that event bus. When the health check reports a healthy state, events are processed by the event bus in the primary Region.

#### Lab recap

In the Utilizing EventBridge lab, you performed the following tasks:

* Created Lambda functions to log events and reboot EC2 instances.
* Enabled EventBridge to log auto scaling events.
* Created an EventBridge Schedule to reboot EC2 instances monthly.
* Tested an EventBridge rule by manually updating the Auto Scaling group.

## AWS Config

### Pre-assessment

#### What is an AWS Config conformance pack?

* A collection of AWS Config rules and remediation actions that can be quickly deployed

Wrong answers:

* A snapshot of the AWS resources that AWS Config is recording
* A visual dashboard to help you quickly spot noncompliant resources and take appropriate action
* A resource type that collects AWS Config data from multiple accounts and Regions

The other options are incorrect for the following reasons:

* Configuration snapshots are snapshots of the AWS resources that AWS Config is recording.
* The cloud governance dashboard is a visual dashboard to help you quickly spot noncompliant resources and take appropriate action.
* Aggregators are a resource type that collects AWS Config data from multiple accounts and Regions.

#### Which service can use AWS Config evaluations as a data source for automated evidence?

* AWS Audit Manager

Wrong answers:

* AWS Security Hub
* AWS Step Functions
* AWS Lambda

You can use Audit Manager to capture AWS Config evaluations as evidence for audits. When you create or edit a custom control, you can specify one or more AWS Config rules as a data source mapping for evidence collection. AWS Config performs compliance checks based on these rules, and Audit Manager reports the results as compliance check evidence.

#### What contributes to the cost of AWS Config?

* The number of AWS Config rule evaluations recorded

Wrong answers:

* The number of aggregators used in AWS Config
* The number of configuration snapshots created in AWS Config
* The number of remediation actions taken using AWS Config evaluations

Customers are charged based on the number of AWS Config rule evaluations recorded. A rule evaluation is recorded every time a resource is evaluated for compliance against an AWS Config rule. Rule evaluations can be run in detective mode or in proactive mode, if available  (or both).

### Security and compliance benefits of AWS Config

* **Security analysis:** Identify misconfigurations that could lead to  vulnerabilities. Continuously monitor and record your AWS resource configurations. This helps ensure resources are not unintentionally modified, which can improve security.
* **Continuous monitoring:** Get real-time alerts on configuration changes so you can quickly review and respond. This will help identify configuration drift. AWS Config can detect when resources deviate from desired configurations, allowing you to correct issues before they affect security or compliance.
* **Continuous assessment:** Check compliance of resource configurations against policies. Use rules and conformance packs to enforce compliance. Assess security and compliance of resource configurations against baseline requirements. AWS Config continuously validates resources against configured rules and policies.
* **Change management:** Understand how changes impact other resources to minimize incidents. You can also elect to get notifications about changes to critical resources. This helps detect unintended changes that could affect security or compliance.
* **Enterprise-wide compliance:** View compliance status across all accounts and regions from one central account.
* **Support frameworks:** Support compliance frameworks. AWS Config rules support common compliance standards like PCI DSS, ISO, HIPAA, and others.
* **Simplify the audit process:** AWS Config makes it easier to prepare for audits by recording resource configurations and changes over time. Prove compliance at any point in time. AWS Config records provide an audit trail of changes over time, which can help demonstrate compliance with regulations.
* **Integration:** Integrate with security tools. AWS Config can integrate with AWS security services like AWS Security Hub to help identify potential security issues.

With AWS Config, you can evaluate and audit the configurations of your AWS resources. It continuously monitors your resources and records configuration changes. You can review changes, track resource relationships, and check configuration histories.

Overall, AWS Config simplifies compliance auditing, security analysis, change management, and troubleshooting by recording configurations and allowing automation of compliance checks.

1. **Configuration change.** If a configuration change occurs in an AWS resource, information is sent to AWS Config.
2. **AWS Config receives the change.** AWS Config records and normalizes the changes into a consistent format.
3. **AWS Config evaluates configuration.** AWS Config automatically evaluates the recorded configurations against the configurations you specify.
4. **You are notified of the change.** Access change history and compliance results by using the console or APIs. CloudWatch events or Amazon SNS alerts you when changes occur. Deliver change history and snapshot files to your S3 bucket for analysis.

### AWS Config managed rules

AWS Config provides AWS managed rules, which are predefined, customizable rules that AWS Config uses to evaluate whether your AWS resources comply with common best practices. For example, you could use a managed rule to quickly start assessing whether your EBS volumes are encrypted or whether specific tags are applied to your resources. The AWS Config console guides you through the process of configuring and activating a managed rule. You can also use the AWS CLI or AWS Config API to pass the JSON code that defines your configuration of a managed rule.

You can customize the behavior of a managed rule to suit your needs. For example, you can define the rule's scope to constrain which resources initiate an evaluation for the rule, such as EC2 instances or volumes. You can customize the rule's parameters to define attributes that your resources must have to comply with the rule. For example, you can customize a parameter to specify that your security group should block incoming traffic to a specific port number.

### Resource relationships tracking

AWS Config discovers, maps, and tracks AWS resource relationships in your account. For example, if a new Amazon EC2 security group is associated with an EC2 instance, AWS Config records the updated configurations of both the Amazon EC2 security group and the EC2 instance.

AWS Config tracks these changes by calling the Describe or List API for resources. The same calls get details for related resources too. For example, changing a security group's egress rule causes a Describe call on it. Then instances using that group are checked. Updated configurations for the security group and instances are recorded as items and delivered to Amazon S3. AWS Config also finds changes not through the API by periodically checking configurations. Any changed configurations have items created.

### Cloud Governance dashboard

AWS Config provides the following three types of dashboards:

* AWS account-specific and AWS Region-specific dashboards that display your resources' compliance posture, which your IT administrators, security experts, and compliance officers use to quickly spot noncompliance resources and take appropriate action.
* A high-level dashboard per aggregator that shows insights, such as the total count of non-compliant rules across your AWS Organization, the top 5 non-compliant rules by the number of resources, and the top 5 AWS accounts that have the highest number of non-compliant rules.
* Detailed dashboards for each aggregator that dive deep into inventory and compliance details, such as compliance summary by resources, top 10 accounts with non-compliant resources, top 10 accounts by noncompliant rules across conformance packs, comparison of running compared to stopped EC2 instances by type, and EBS volumes by volume type and size.

You can also dive deeper into resource details by accessing the underlying AWS Config advanced queries for each widget in all three types of dashboards. You can use all of the available dashboards to gain insights into your resource configuration metadata.

### Certifications

#### ISO 9001:2015 Compliance

ISO 9001:2015 outlines a process-oriented approach to documenting and reviewing the structure, responsibilities, and procedures required to achieve effective quality management within an organization. To learn more, visit the [FAQ page](https://aws.amazon.com/compliance/iso-9001-faqs/).

#### ISO/IEC 27018:2019 Compliance

ISO/IEC 27018:2019 is a code of practice that focuses on protection of personal data in the cloud. It is based on ISO/IEC information security standard 27002 and provides implementation guidance on ISO/IEC 27002 controls applicable to public cloud Personally Identifiable Information (PII). It also provides a set of additional controls and associated guidance intended to address public cloud PII protection requirements not addressed by the existing ISO/IEC 27002 control set. To learn more, visit the [FAQ page](https://aws.amazon.com/compliance/iso-27018-faqs/).

#### PCI DSS

The PCI DSS is a proprietary information security standard administered by the PCI Security Standards Council.

PCI DSS applies to entities that store, process, or transmit cardholder data (CHD) or sensitive authentication data (SAD), including merchants, processors, acquirers, issuers, and service providers. The PCI DSS is mandated by the card brands. To learn more, visit the [FAQ page](https://aws.amazon.com/compliance/pci-dss-level-1-faqs/).

#### ISO/IEC 27001:2013

ISO/IEC 27001:2013 is a security management standard that specifies security management best practices and comprehensive security controls following the ISO/IEC 27002 best practice guidance. The basis of this certification is the development and implementation of a rigorous security program, which includes the development and implementation of an Information Security Management System (ISMS). ISMS defines how AWS perpetually manages security in a holistic, comprehensive manner. To learn more, visit the [FAQ page](https://aws.amazon.com/compliance/iso-27001-faqs/).

#### ISO/IEC 27017:2015 Compliance

ISO/IEC 27017:2015 provides guidance on the information security aspects of cloud computing, recommending the implementation of cloud-specific information security controls that supplement the guidance of the ISO/IEC 27002 and ISO/IEC 27001 standards. This code of practice provides additional information security controls implementation guidance specific to cloud service providers.  To learn more, visit the [FAQ page](https://aws.amazon.com/compliance/iso-27017-faqs/).

#### HIPAA compliance

For a list of AWS services that are certified by HIPAA, visit the [HIPAA Eligible Services Reference page](https://aws.amazon.com/compliance/hipaa-eligible-services-reference/).

### [Conformance pack sample templates](https://docs.aws.amazon.com/config/latest/developerguide/conformancepack-sample-templates.html)

Here are the conformance pack YAML templates that you see in the AWS Config console. Within each conformance pack template, you can use one or more AWS Config rules and remediation actions. The AWS Config rules listed within the conformance pack can be AWS Config managed rules or AWS Config custom rules.

### Application Load Balancer

AWS Config integrates with the Elastic Load Balancing (ELB) service to record configuration changes to Application Load Balancers. AWS Config also includes relationships with associated EC2 security groups, VPCs, and subnets. You can use this information for security analysis and troubleshooting. For example, you can check which security groups are associated with your Application Load Balancer at any point in time. You can navigate to the AWS Config timeline from the ELB console to view the configuration changes of your Application Load Balancers.

### Amazon EC2 Dedicated Host

AWS Config integrates with Amazon EC2 Dedicated Hosts to assess license compliance. AWS Config records when instances are launched, stopped, or shut down on a Dedicated Host, and pairs this information with host and instance level information relevant to software licensing, such as Host ID, Amazon Machine Image (AMI) IDs, number of sockets, and physical cores. This helps you use AWS Config as a data source for your license reporting. You can navigate to the AWS Config timeline from the EC2 Dedicated Hosts console to view the configuration changes of your Dedicated Hosts.

### [AWS Config pricing](https://aws.amazon.com/config/pricing/)

AWS Config charges are based on the number of configuration items recorded, the number of active AWS Config rule evaluations, and the number of conformance pack evaluations in your account.

### Using Aggregators with AWS Config and AWS Organizations

An aggregator is an AWS Config resource type that collects AWS Config configuration and compliance data from the following:

* Multiple accounts and multiple Regions
* Single account and multiple Regions
* An organization in AWS Organizations and all the accounts in that organization that have AWS Config enabled

Use an aggregator to view the resource configuration and compliance data recorded in AWS Config.

Although AWS Config can run in a single account, the ability to run AWS Config on AWS Organizations supports enterprise-wide compliance monitoring.

1. **Adding an aggregator:** Create an aggregator account and an aggregator (resource) to collect configuration and compliance data from multiple accounts or Regions. Select the source accounts and Regions from where you want to collect AWS Config data.
2. **Authorizing the aggregator account:** Authorization is required when your source accounts are individual accounts. Authorization is not required if you are aggregating source accounts that are part of AWS Organizations. The aggregator account is commonly used or owned by an organization's security team or a managed service provider.
3. **Monitoring in an aggregated view:** The dashboard on the aggregators page displays the configuration data for AWS resources in scope, provides an overview of your rules and conformance packs, and displays their compliance states.

### Using AWS Config Conformance Packs and Scores

A conformance pack is a collection of AWS Config rules and remediation actions that can be easily deployed as a single entity in an account and a Region or across an organization in AWS Organizations.

Conformance packs are created by authoring a YAML template that contains the list of custom rules or rules managed by AWS Config and the remediation actions. You can also use Systems Manager documents to store your conformance pack templates on AWS and directly deploy conformance packs using System Manager document names.

To start using conformance packs in the console, choose the **Deploy conformance pack** button.

From there, specify a conformance pack template using the following options:

* You can use a sample template created by AWS to quickly get started and to evaluate your AWS environment.
* You can also create a new conformance pack YAML file stored in a Systems Manager document, S3 bucket, or a YAML file you upload.

#### [Creating a baseline and then automatically remediating](https://aws.amazon.com/blogs/mt/deploying-conformance-packs-across-an-organization-with-automatic-remediation/)

AWS Config conformance packs help organizations manage configuration compliance of its AWS resources at scale; from policy definition to auditing and aggregated reporting using a common framework and packaging model.

Use templates created by AWS to quickly establish a common baseline for resource configuration policies and best practices across multiple accounts in an organization. Those can then be used for automatic remediation.

### Compliance score

AWS accounts can have hundreds of resources and be subject to numerous AWS Config rule checks. It can be a challenge for our customers’ compliance teams to validate and quantify the AWS resources’ compliance posture. Furthermore, reporting on the progress of remediation efforts can be time-consuming.

AWS Config compliance scores for conformance packs address this challenge and help quantify an organization's compliance posture as a CloudWatch metric. It’s a quantitative measure of compliance status.

#### Compliance score calculation

A compliance score is calculated by taking the number of rule-to-resource combinations that are compliant and dividing it by the total scope of a conformance pack. This number is then multiplied by 100 to give a percentage.

This score can be viewed in two parts of the AWS Config console:

1. AWS Config **Conformance packs** page.
2. AWS Config **Dashboard**.

#### Compliance score calculation example

You have an account that has 3 S3 buckets and 4 EC2 instances.

Your conformance pack contains the following three rules:

* **EC2 instance rules:** *ebs-optimized-instance* (Rule 1) and *ec2-ebs-encryption-by-default* (Rule 2)
* **S3 bucket rule:** *s3-bucket-acl-prohibited*  (Rule 3)

```
#############################################################################
#
# Conformance Pack:
#  Sample Conformance Pack
#
#############################################################################
Resources:
 EbsOptimizedInstance:
  Properties:
   ConfigRuleName: ebs-optimized-instance
   Scope:
    ComplianceResourceTypes:
    - AWS::EC2::Instance
   Source:
    Owner: AWS
    SourceIdentifier: EBS_OPTIMIZED_INSTANCE
  Type: AWS::Config::ConfigRule
 Ec2EbsEncryptionByDefault:
  Properties:
   ConfigRuleName: ec2-ebs-encryption-by-default
   Source:
    Owner: AWS
    SourceIdentifier: EC2_EBS_ENCRYPTION_BY_DEFAULT
  Type: AWS::Config::ConfigRule
 S3BucketAclProhibited:
  Properties:
   ConfigRuleName: s3-bucket-acl-prohibited
   Scope:
    ComplianceResourceTypes:
    - AWS::S3::Bucket
   Source:
    Owner: AWS
    SourceIdentifier: S3_BUCKET_ACL_PROHIBITED
  Type: AWS::Config::ConfigRule
```

AWS Config then evaluates your resources against your conformance pack. It finds that all EC2 instances are compliant with Rule 1, but only two are compliant with Rule 2. All S3 buckets are compliant with Rule 3. The following table represents these findings.

| Resource | Rule 1 | Rule 2 | Rule 3 | Total |
| -------- | ------ | ------ | ------ | ----- |
| S3 buckets | 0 | 0 | 3 | 3 |
| EC2 instances | 4 | 2 | 0 | 6 |
| Totals | 4 | 2 | 3 | 9 |

The following table shows the number of resources that could be compliant.

| Resource | Rule 1 | Rule 2 | Rule 3 | Total |
| -------- | ------ | ------ | ------ | ----- |
| S3 buckets | 0 | 0 | 3 | 3 |
| EC2 instances | 4 | 4 | 0 | 8 |
| Totals | 4 | 4 | 3 | 11 |

Using the equation from earlier, you have the following equation: 9/11 * 100 = 81 percent. This score can be viewed in the AWS Config dashboard.

#### Sample use cases for AWS Config compliance scores

* AWS Config compliance scores for conformance packs help organizations see the impact of change or deployment on their overall compliance posture. If the compliance score fluctuates with time as highs and lows, then this is indicative of ephemeral resources that might be out of compliance.
* Compliance scores can help organizations set up their overall compliance goals. Compliance scores are also provided as CloudWatch metrics, which allows for tracking over time.
* Organizations can build CloudWatch dashboards based on the compliance score metric to compare the compliance scores for conformance packs across Regions and other conformance packs.

**For deployments across different Regions:** The API call to deploy rules and conformance packs across accounts is Region-specific. At the organization level, you need to change the context of your API call to a different Region if you want to deploy rules in other Regions. For example, to deploy a rule in US East (N. Virginia), change the Region to US East (N. Virginia) and then call **PutOrganizationConfigRule.**

* Compliance scores are published to CloudWatch as metrics, and organizations can set up CloudWatch alarms to notify a team when the score drops below a certain threshold for an extended time.

### Delivering and Viewing Configuration Snapshots

AWS Config generates configuration snapshots when you invoke the **DeliverConfigSnapshot** action or run the **AWS CLI deliver-config-snapshot** command. AWS Config stores configuration snapshots in the S3 bucket that you specified when you enabled AWS Config.

Type the **deliver-config-snapshot** command by specifying the name assigned by AWS Config when you configured your delivery channel. The following is an example.

```
$ aws configservice deliver-config-snapshot --delivery-channel-name default
{
    "configSnapshotId": "94ccff53-83be-42d9-996f-b4624b3c1a55"
}
```

#### Why would you use a configuration snapshot?

A snapshot can be used to check the historical configuration; for example, which ports did this security group allow during the outage last month?

#### Example of a configuration snapshot

The snapshot describes the configuration for the resources that AWS Config is recording in the current Region for your AWS account. It describes the relationships between these resources.

The configuration snapshot can include references to resources types and resource IDs that are not supported.

```
{
    "fileVersion": "1.0",
    "requestId": "asudf8ow-4e34-4f32-afeb-0ace5bf3trye",
    "configurationItems": [
        {
            "configurationItemVersion": "1.0",
            "resourceId": "vol-ce676ccc",
            "arn": "arn:aws:us-west-2b:123456789012:volume/vol-ce676ccc",
            "accountId": "12345678910",
            "configurationItemCaptureTime": "2014-03-07T23:47:08.918Z",
            "configurationStateID": "3e660fdf-4e34-4f32-afeb-0ace5bf3d63a",
            "configurationItemStatus": "OK",
            "relatedEvents": [
                "06c12a39-eb35-11de-ae07-adb69edbb1e4",
                "c376e30d-71a2-4694-89b7-a5a04ad92281"
            ],
            "availibilityZone": "us-west-2b",
            "resourceType": "AWS::EC2::Volume",
            "resourceCreationTime": "2014-02-27T21:43:53.885Z",
            "tags": {},
            "relationships": [
                {
                    "resourceId": "i-344c463d",
                    "resourceType": "AWS::EC2::Instance",
                    "name": "Attached to Instance"
                }
            ],
            "configuration": {
                "volumeId": "vol-ce676ccc",
                "size": 1,
                "snapshotId": "",
                "availabilityZone": "us-west-2b",
                "state": "in-use",
                "createTime": "2014-02-27T21:43:53.0885+0000",
                "attachments": [
                    {
                        "volumeId": "vol-ce676ccc",
                        "instanceId": "i-344c463d",
                        "device": "/dev/sdf",
                        "state": "attached",
                        "attachTime": "2014-03-07T23:46:28.0000+0000",
                        "deleteOnTermination": false
                    }
                ],
                "tags": [
                    {
                        "tagName": "environment",
                        "tagValue": "PROD"
                    },
                    {
                        "tagName": "name",
                        "tagValue": "DataVolume1"
                    }
                ],
                "volumeType": "standard"
            }
        },
        {
            "configurationItemVersion": "1.0",
            "resourceId": "i-344c463d",
            "accountId": "12345678910",
            "arn": "arn:aws:ec2:us-west-2b:123456789012:instance/i-344c463d",
            "configurationItemCaptureTime": "2014-03-07T23:47:09.523Z",
            "configurationStateID": "cdb571fa-ce7a-4ec5-8914-0320466a355e",
            "configurationItemStatus": "OK",
            "relatedEvents": [
                "06c12a39-eb35-11de-ae07-adb69edbb1e4",
                "c376e30d-71a2-4694-89b7-a5a04ad92281"
            ],
            "availibilityZone": "us-west-2b",
            "resourceType": "AWS::EC2::Instance",
            "resourceCreationTime": "2014-02-26T22:56:35.000Z",
            "tags": {
                "Name": "integ-test-1",
                "examplename": "examplevalue"
            },
            "relationships": [
                {
                    "resourceId": "vol-ce676ccc",
                    "resourceType": "AWS::EC2::Volume",
                    "name": "Attached Volume"
                },
                {
                    "resourceId": "vol-ef0e06ed",
                    "resourceType": "AWS::EC2::Volume",
                    "name": "Attached Volume",
                    "direction": "OUT"
                },
                {
                    "resourceId": "subnet-47b4cf2c",
                    "resourceType": "AWS::EC2::SUBNET",
                    "name": "Is contained in Subnet",
                    "direction": "IN"
                }
            ],
            "configuration": {
                "instanceId": "i-344c463d",
                "imageId": "ami-ccf297fc",
                "state": {
                    "code": 16,
                    "name": "running"
                },
                "privateDnsName": "ip-172-31-21-63.us-west-2.compute.internal",
                "publicDnsName": "ec2-54-218-4-189.us-west-2.compute.amazonaws.com",
                "stateTransitionReason": "",
                "keyName": "configDemo",
                "amiLaunchIndex": 0,
                "productCodes": [],
                "instanceType": "t1.micro",
                "launchTime": "2014-02-26T22:56:35.0000+0000",
                "placement": {
                    "availabilityZone": "us-west-2b",
                    "groupName": "",
                    "tenancy": "default"
                },
                "kernelId": "aki-fc8f11cc",
                "monitoring": {
                    "state": "disabled"
                },
                "subnetId": "subnet-47b4cf2c",
                "vpcId": "vpc-41b4cf2a",
                "privateIpAddress": "172.31.21.63",
                "publicIpAddress": "54.218.4.189",
                "architecture": "x86_64",
                "rootDeviceType": "ebs",
                "rootDeviceName": "/dev/sda1",
                "blockDeviceMappings": [
                    {
                        "deviceName": "/dev/sda1",
                        "ebs": {
                            "volumeId": "vol-ef0e06ed",
                            "status": "attached",
                            "attachTime": "2014-02-26T22:56:38.0000+0000",
                            "deleteOnTermination": true
                        }
                    },
                    {
                        "deviceName": "/dev/sdf",
                        "ebs": {
                            "volumeId": "vol-ce676ccc",
                            "status": "attached",
                            "attachTime": "2014-03-07T23:46:28.0000+0000",
                            "deleteOnTermination": false
                        }
                    }
                ],
                "virtualizationType": "paravirtual",
                "clientToken": "aBCDe123456",
                "tags": [
                    {
                        "key": "Name",
                        "value": "integ-test-1"
                    },
                    {
                        "key": "examplekey",
                        "value": "examplevalue"
                    }
                ],
                "securityGroups": [
                    {
                        "groupName": "launch-wizard-2",
                        "groupId": "sg-892adfec"
                    }
                ],
                "sourceDestCheck": true,
                "hypervisor": "xen",
                "networkInterfaces": [
                    {
                        "networkInterfaceId": "eni-55c03d22",
                        "subnetId": "subnet-47b4cf2c",
                        "vpcId": "vpc-41b4cf2a",
                        "description": "",
                        "ownerId": "12345678910",
                        "status": "in-use",
                        "privateIpAddress": "172.31.21.63",
                        "privateDnsName": "ip-172-31-21-63.us-west-2.compute.internal",
                        "sourceDestCheck": true,
                        "groups": [
                            {
                                "groupName": "launch-wizard-2",
                                "groupId": "sg-892adfec"
                            }
                        ],
                        "attachment": {
                            "attachmentId": "eni-attach-bf90c489",
                            "deviceIndex": 0,
                            "status": "attached",
                            "attachTime": "2014-02-26T22:56:35.0000+0000",
                            "deleteOnTermination": true
                        },
                        "association": {
                            "publicIp": "54.218.4.189",
                            "publicDnsName": "ec2-54-218-4-189.us-west-2.compute.amazonaws.com",
                            "ipOwnerId": "amazon"
                        },
                        "privateIpAddresses": [
                            {
                                "privateIpAddress": "172.31.21.63",
                                "privateDnsName": "ip-172-31-21-63.us-west-2.compute.internal",
                                "primary": true,
                                "association": {
                                    "publicIp": "54.218.4.189",
                                    "publicDnsName": "ec2-54-218-4-189.us-west-2.compute.amazonaws.com",
                                    "ipOwnerId": "amazon"
                                }
                            }
                        ]
                    }
                ],
                "ebsOptimized": false
            }
        }
    ]
}
```

#### Verifying delivery status

Use the **describe-delivery-channel-status** command to verify that the AWS Config has started delivering the configurations to the specified delivery channel.

```
$ aws configservice describe-delivery-channel-status
{
    "DeliveryChannelsStatus": [
        {
            "configStreamDeliveryInfo": {
                "lastStatusChangeTime": 1415138614.125,
                "lastStatus": "SUCCESS"
            },
            "configHistoryDeliveryInfo": {
                "lastSuccessfulTime": 1415148744.267,
                "lastStatus": "SUCCESS",
                "lastAttemptTime": 1415148744.267
            },
            "configSnapshotDeliveryInfo": {
                "lastSuccessfulTime": 1415333113.4159999,
                "lastStatus": "SUCCESS",
                "lastAttemptTime": 1415333113.4159999
            },
            "name": "default"
        }
    ]
}
```

#### View a snapshot in an S3 bucket using the AWS Management Console

1. **Navigate to Amazon S3.** Sign in to the AWS Management Console, and open the Amazon S3 console.
2. **Locate the AWS Config S3 bucket.** In the Amazon S3 console Buckets list, select the name of your S3 bucket.
3. **Locate the file**, a test file is initially created. View the nested folders in your bucket until you see the **ConfigSnapshot** object with a snapshot ID that matches the ID returned by the command. Download and open the object to view the configuration snapshot.

The S3 bucket also contains an empty file named **ConfigWritabilityCheckFile**. AWS Config creates this file to verify that the service can successfully write to the S3 bucket.

### AWS Config Integrations

* AWS Security Hub
* AWS Audit Manager
* AWS Systems Manager
* IT Service Management (ITSM)

#### AWS Security Hub

Security Hub centralizes security checks from other AWS services, including AWS Config rules. Security Hub enables and controls AWS Config rules to verify that your resource configurations are aligned to best practices. Enable AWS Config on all accounts in all Regions where Security Hub is to run security checks on your environment’s resources.

#### AWS Audit Manager

With Audit Manager, you can continuously audit your AWS usage to streamline how you assess risk and compliance with regulations and industry. Audit Manager automates evidence collection, so you can configure a control data source, such as AWS Config, to collect automated evidence.

#### AWS Systems Manager

AWS Config integrates with Systems Manager to record configuration changes to software on your EC2 instances and servers in your on-premises environment. With this integration, you can gain visibility into operating system (OS) configurations, system-level updates, installed applications, network configuration, and more. AWS Config also provides a history of OS and system-level configuration changes alongside infrastructure configuration changes recorded for EC2 instances. You can navigate to the AWS Config timeline from the Systems Manager console to view the configuration changes of your managed EC2 instances. You can use AWS Config to view Systems Manager inventory history and track changes for all your managed instances.

#### IT Service Management (ITSM)

IT Service Management (ITSM) tools, such as Jira Service Desk, can connect with AWS Config so ITSM users can request and manage AWS services and resources. The AWS Service Management Connector (SMC) for Jira Service Desk provides Jira Service Desk administrators governance and oversight over their AWS products.

### [Lab: Automating Compliance and Security With AWS Config](./W04Lab2-ComplianceAndSecurityAWSConfig.md)

### [Lab: Auditing Your AWS Resources With Systems Manager and AWS Config](./W04Lab3-AuditSystemsManagerAWSConfig.md)

### Activity: AWS Config Use Cases

#### How to automate compliancy audit with AWS Config?

* AWS Config has a feature called conformance packs that contain a collection of rules and remediation actions. You can deploy that across multiple Regions through AWS Organizations.

A conformance pack is a collection of AWS Config rules and remediation actions that can be deployed as a single entity in an account and a Region or across an organization in AWS Organizations.

#### Is there a way to track how the conformance packs are performing throughout an organization?

* AWS Config has a feature called compliance scores for conformance packs, which can help you see the impact of configuration changes or deployments to your overall compliance posture.

AWS Config compliance scores for conformance packs help organizations see the impact of change or deployment to its overall compliance posture. If its compliance score fluctuates with time with highs and lows, then this is indicative of ephemeral resources that might be out of compliance.

AWS Config helps organizations deploy rules and remediation actions that can be easily deployed as a single entity in an account and a Region or across an organizations in AWS Organizations. The following are some other Config use cases:

* **Detect suspicious configuration changes:** Get alerts on changes like S3 bucket policies being opened up or EC2 security rules being added.
* **Monitor resource deletions:** Get notified if critical resources like IAM roles, security groups, etc. are deleted.
* **Forensic analysis:** Reconstruct historical resource configurations to analyze root cause after a security incident.
* **Audit preparation:** Provide audit history and evidence of compliance over time for auditors.

### Knowledge Check

#### What is a primary benefit of AWS Config?

* It tracks and manages resource configurations.

Wrong answers:

* It is a unified software development service.
* It is a cloud-based integrated development environment.
* It optimizes existing code for efficiency.

The other options are incorrect for the following reasons:

* AWS Cloud9 is a cloud-based integrated development environment.
* Amazon CodeCatalyst is a unified software development service.
* Amazon CodeGuru can help you optimize existing code for efficiency.

#### How can an AWS Config rule benefit application developers?

* It can check whether an AWS resource complies with the desired configurations needed in an application’s code.

Wrong:

* It can define the coding standards used for an application and then enforce compliance.
* It can enforce compliance of an application’s architecture with an organization’s standards.
* It can review code before it is deployed, and then alert developers if any of the code is not compliant with required standards.

#### Which service can AWS Config integrate with to evaluate whether AWS resource configurations comply with your custom AWS Config rules?

* AWS Lambda

Wrong answers:

* Amazon EventBridge
* AWS Step Functions
* AWS Fargate

The other options are incorrect for the following reasons:

* Amazon EventBridge makes possible the creation of event-driven architecture.
* AWS Step Functions creates visual workflows that helps developers use AWS services to build distributed applications, automate processes, orchestrate microservices, and create data and machine learning pipelines.
* AWS Fargate is a serverless, pay-as-you-go compute engine.

### Summary

AWS Config is a service you can use to evaluate and audit the configurations of your AWS resources. It continuously monitors your resources and records configuration changes. You can review changes, track resource relationships, and check configuration histories. Overall, AWS Config streamlines compliance auditing, security analysis, change management, and troubleshooting by recording configurations and allowing automation of compliance checks. 

#### Resource relationships tracking

AWS Config discovers, maps, and tracks AWS resource relationships in your account. For example, if a new EC2 security group is associated with an EC2 instance, AWS Config records the updated configurations of both the EC2 security group and the EC2 instance. AWS Config tracks these changes by calling the Describe or List API for resources. The same calls also get details for related resources.

#### Cloud Governance dashboard types

* AWS account-specific and AWS Region-specific dashboards that display your resources' compliance posture, which your IT administrators, security experts, and compliance officers use to quickly spot noncompliance resources and take appropriate action.
* High-level dashboards for each aggregator that show insights, such as the total count of non-compliant rules across your AWS Organization, the top five non-compliant rules by the number of resources, and the top five AWS accounts that have the highest number of non-compliant rules.
* Detailed dashboards for each aggregator that dive deep into inventory and compliance details, such as compliance summary by resources, top 10 accounts with non-compliant resources, top 10 accounts by noncompliant rules across conformance packs, comparison of running versus stopped EC2 instances by type, and EBS volumes by volume type and size.

#### Aggregators

An aggregator is an AWS Config resource type that collects AWS Config configuration and compliance data from the following:

* Multiple accounts and multiple Regions
* Single accounts and multiple Regions
* An organization in AWS Organizations and all the accounts in that organization that have AWS Config enabled

Use an aggregator to view the resource configuration and compliance data recorded in AWS Config. The following image displays how an aggregator collects AWS Config data from multiple accounts and Regions. Although AWS Config can run in a single account, the ability to run AWS Config on AWS Organizations supports enterprise-wide compliance monitoring.

#### Conformance packs and compliance scores

##### Conformance packs

A conformance pack is a collection of AWS Config rules and remediation actions that can be deployed as a single entity in an account and a Region or across an organization in AWS Organizations.

##### Compliance scores

A compliance score is calculated by taking the number of rule-to-resource combinations that are compliant and dividing it by the total scope of a conformance pack. This number is then multiplied by 100 to give a percentage.

#### Configuration snapshots

AWS Config generates configuration snapshots when you invoke the **DeliverConfigSnapshot** action or run the AWS CLI **deliver-config-snapshot** command. AWS Config stores configuration snapshots in the S3 bucket that you specified when you enabled AWS Config.

#### AWS Config integrations

##### Security Hub

Security Hub centralizes security checks from other AWS services, including AWS Config rules. Security Hub enables and controls AWS Config rules to verify that your resource configurations are aligned with best practices. Enable AWS Config on all accounts in all Regions where Security Hub is to run security checks on your environment’s resources.

##### Audit Manager

Audit Manager helps you continuously audit your AWS usage to simplify how you assess risk and compliance with regulations and industry standards. Audit Manager automates evidence collection, so you can configure a control data source, such as AWS Config, to collect automated evidence.

##### Systems Manager

AWS Config integrates with Systems Manager to record configuration changes to software on your EC2 instances and servers in your on-premises environment. With this integration, you can gain visibility into OS configurations, system-level updates, installed applications, network configuration, and more. AWS Config also provides a history of OS and system-level configuration changes alongside infrastructure configuration changes recorded for EC2 instances. You can navigate to the AWS Config timeline from the Systems Manager console to view the configuration changes of your managed EC2 instances. You can use AWS Config to view Systems Manager Inventory history and track changes for all your managed instances.

##### ITSM

ITSM tools, such as Jira Service Desk, can connect with AWS Config to make it easier for ITSM users to request and manage AWS services and resources. The AWS Service Management Connector (SMC) for Jira Service Desk provides Jira Service Desk administrators governance and oversight over their AWS products.

#### Lab recap

In the *Automating Compliance and Security With AWS Config* lab, you performed the following tasks:

* Defined security rules and compliance requirements.
* Monitored infrastructure against the rules and requirements.
* Detected violations.
* Rapidly acted on violations with automation.

In the *Auditing Your AWS Resources With Systems Manager and AWS Config* lab, you performed the following tasks:

* Set up Systems Manager Inventory for an AWS infrastructure.
* Used Systems Manager to securely log in to EC2 instances.
* Set up AWS Config for an AWS infrastructure.
* Used AWS Config to audit AWS resources for organizational-level compliance.
* Used Systems Manager Inventory to view the metadata on your managed instances.
