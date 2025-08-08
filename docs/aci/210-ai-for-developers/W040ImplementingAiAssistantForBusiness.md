# Week 4: Implementing an AI-Powered Assistant for Business

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to [AI for Developers](./ai-for-developers.md)
* back to repo's main [README.md](../../../README.md)

## Meeting AnyCompany Hotels

AnyCompany Hotels: Overcoming growth challenges with AI

AnyCompany Hotels, a growing chain with hotels in cities and resorts, is facing problems with managing information and employee efficiency. Martha, the chief innovation officer, wants to use AI to help staff quickly find and use company information, including booking data, work procedures, and guest service rules.

During her visits to different AnyCompany hotels, Martha saw many of the following issues.

1
2
3
4
5
6
7
8
9


Issue 1

At the city hotel, Martha noticed managers struggling to make informed decisions about guest experience improvements.

A trend of declining satisfaction scores in their food and beverage service had been identified. The scores had dropped to 8.5 out of 10 from 9.0 out of 10 last quarter. To investigate, managers had to manually search through guest feedback comments, incident reports, staff training records, and departmental performance data to understand the root causes.

The management team spent days gathering and analyzing this information, making it difficult to respond quickly to emerging guest satisfaction trends.











Three main challenges

Martha recognizes that solving these problems might require an AI-powered solution. However, she identified three critical challenges that must be addressed.

Accuracy

Any AI tool implemented must provide precise, up-to-date information specific to AnyCompany Hotels' operations and policies. Generic hospitality information will not suffice because each property has its unique procedures and offerings. Martha needs a solution that can accurately reflect AnyCompany Hotels' distinct practices across all its properties.


Security and control

With sensitive business data and guest information at stake, data protection is crucial. The ideal solution will have robust security measures, allowing appropriate access to employees based on their roles and responsibilities.

For example, front desk staff should access guest preferences but not financial data, whereas management would need broader access.


Time to value

AnyCompany Hotels' IT team is small and already overextended. Implementing a new AI solution cannot require extensive technical expertise or long development cycles. Martha needs a system that can be deployed quickly and start providing value almost immediately, without putting additional strain on the IT department.


Initial experiment

Martha initially tried addressing these issues using a general AI chat service. She used an open source large language model (LLM), which was privately hosted on AnyCompany Hotels' servers. However, this approach revealed the following problems.


Continuous updates
It was challenging to keep the AI updated with the latest AnyCompany Hotels information because it required frequent retraining of the entire model. This was time-consuming and resource intensive.

For example, when AnyCompany Hotels changed its seasonal room rates, the IT team had to shut down the system. They then fine-tuned the model with updated pricing that was taking 2–3 days. Finally, IT had to verify all other information remained accurate before bringing the system back online. During this downtime, staff had to resort to manual lookups for current rates and policies.


Data unavailability
The general AI chat service didn't have access to AnyCompany Hotels' confidential and proprietary information. This meant it couldn't provide accurate answers about specific hotel policies, current pricing, or guest data because this information wasn't part of its training data.

For example, when asked about loyalty program benefits, the general AI couldn't provide AnyCompany Hotels' specific tiers and benefits such as the following:

Silver: 10 percent discount

Gold: 15 percent discount and welcome drink

Platinum: 20 percent discount and room upgrade


Hallucinations
In attempts to answer questions about AnyCompany Hotels' services and policies, the AI sometimes generated plausible but incorrect information. This posed a significant risk of misinforming staff or guests if relied on.

For example, when asked about room types, the AI provided incorrect pricing, stating all deluxe rooms were $150 per night. However, AnyCompany Hotels' actual rates started at $200 for deluxe rooms with partial ocean views.


Infrastructure costs
Hosting and running the LLM on AnyCompany Hotels servers proved to be computationally intensive and expensive, especially when trying to scale the solution across all properties.

For example, just running the AI system for their city location required a $50,000 server investment plus $10,000 in monthly GPU costs for model training and operation. When they attempted to expand to their resort location, they discovered they would need to double this infrastructure investment, making it financially unfeasible for their budget.


Lack of context
The general AI couldn't understand AnyCompany Hotels' specific terminology, organizational structure, or unique operational procedures, leading to irrelevant or confusing responses.

For example, when asked about housekeeping procedures, the AI couldn't understand that Room Deep Clean at AnyCompany Hotels specifically meant thorough cleaning of all surfaces, upholstery, and carpets performed quarterly.


Long implementation time
Setting up and customizing the open source LLM proved time-consuming and technically challenging for the small IT team, delaying the realization of any benefits.

For example, with only three IT staff members, AnyCompany Hotels spent 6 months preparing data, training the model, and testing the system. During this period, they could only focus on basic hotel policies, leaving critical areas like guest services and operational procedures for a future phase that never materialized because of resource constraints.


Security concerns
Despite being privately hosted, there were ongoing concerns about the security of potentially adding sensitive company information to the AI system. The team worried that if they trained the AI with their data, they wouldn't have proper controls over who could access sensitive information like financial data, guest records, or proprietary procedures.

For example, if they were to add financial data to the system, a front desk employee asking about room availability might accidentally receive sensitive RevPAR (Revenue Per Available Room) information that should only be accessible to management. Without proper role-based access controls, the AI wouldn't know to restrict this type of sensitive data from certain users.

These challenges led Martha to realize they needed a more specialized, business-oriented AI solution. They needed one that could securely handle proprietary data, integrate with existing systems, and provide accurate, context-aware responses without the high infrastructure costs of hosting a full LLM. This realization prompted her to explore other options, eventually leading her to consider Amazon Q Business as a potential solution.

### Knowledge Check

#### When defining a business problem for Amazon Q Business implementation, which elements must be included for proper SMART goal formulation? (Select TWO.)

* Quantifiable metrics for measuring success  
* Specific timeframe for achieving the objective

Wrong answers:

* General improvement goals without specific targets
* Technology implementation requirements
* Budget allocation details

##### Explanation

**Quantifiable metrics for measuring success** and **Specific timeframe for achieving the objective** make the problem statement is measurable and time-bound to track progress and success.

The other options are incorrect for the following reasons:

* General improvement goals without specific targets lack the measurability required for SMART objectives.
* Technology implementation requirements are secondary to defining the business problem.
* Budget allocation details are part of project planning, not problem definition.

#### What are the key benefits of using Amazon Q Business compared to traditional methods of information management? (Select TWO.)

* Natural language query processing for intuitive information retrieval
* Centralized access to enterprise knowledge with role-based security

Wrong answers:

* Real-time integration with operational systems
* Direct customer interaction capabilities
* Automated financial transaction processing

##### Explanation

These features represent key advantages over traditional information management methods.

The other options are incorrect for the following reasons:

* Real-time integration with operational systems is not a primary feature of Amazon Q Business.
* Direct customer interaction capabilities are not part of the core functionality of Amazon Q Business.
* Automated financial transaction processing is outside the scope of Amazon Q Business.

#### A hotel IT administrator is implementing Amazon Q Business and needs to make sure that front desk staff cannot access financial data while managers can view all information. Which component should they configure to achieve this access control?

* Topic-level controls

Wrong answers:

* Data source connector
* Web experience
* Document attributes

##### Explanations

Administrators can use topic-level controls to define specific rules for how Amazon Q Business handles different types of information and which user groups can access them. This provides precise control over sensitive data access based on user roles.

The other options are incorrect for the following reasons:

* Data source connectors handle synchronization between data sources and Amazon Q Business but don't manage access permissions between different user groups.
* Web experience refers to the chat interface that users interact with. The web experience doesn't control access permissions to different types of information.
* Document attributes are metadata associated with documents that help with organization and filtering but don't manage user access permissions.

### Summary

* Defining business problems with the SMART method
* Identifying suitable business problems for Amazon Q Business solutions
* Understanding the advantages of Amazon Q Business over traditional problem-solving methods
* Examining the basic components of Amazon Q Business
* Exploring Amazon Q Business workflows for admins and end users

## Implementing Amazon Q Business to address business challenges

### Creating Effective Problem Statements for Amazon Q Business

### Knowledge Check

#### A hotel manager notices that Amazon Q Business provides vague responses when asked about room service performance. What should they do to improve the quality of responses?

* Add specific metrics and time periods to the query.

Wrong answers:

* Upload more historical data to the system.
* Create a new application environment.
* Enable the general knowledge source.

##### Explanation

Refining queries with specific details like performance metrics and timeframes helps Amazon Q Business provide more focused and relevant responses instead of general information.

The other options are incorrect for the following reasons:

* Uploading more historical data might help but doesn't address the immediate need to get more specific responses from existing data.
* Creating a new application environment doesn't improve query specificity and wastes resources by duplicating existing setups.
* Enabling the general knowledge source would provide less specific information rather than more targeted responses about room service performance.

#### A front desk manager at the hotel wants to create an Amazon Q App to handle frequent guest inquiries about spa services and amenities. They have found a relevant conversation that is suitable for this Q App in the chat history. What should they do next?

* Choose the Create Amazon Q App icon from the chat history.

Wrong answers:

* Navigate to the Library section to search for similar spa service apps.
* Copy the conversation text to the hotel's service manual.
* Start a new conversation about spa services.

##### Explanation

This is the direct method to create a standardized response system for spa service inquiries.

The other options are incorrect for the following reasons:

* Navigating to the Library section only allows viewing existing apps, not creating new ones.
* Copying to the service manual doesn't create an automated response system.
* Starting a new conversation would only repeat the query without creating a solution.

#### A hotel chain is evaluating Amazon Q Business responses about operational procedures. What are the key limitations they should consider? (Select TWO.)

* The system requires human judgment for complex situational decisions.
* Response accuracy depends on the quality and currency of uploaded data.

Wrong answers:

* The system cannot process multiple follow-up queries in the same conversation.
* The system has limited storage capacity.
* The system requires constant internet connectivity.

##### Explanation

**The system requires human judgment for complex situational decisions** and **Response accuracy depends on the quality and currency of uploaded data** represent fundamental limitations of AI-powered systems that organizations need to consider when implementing Amazon Q Business.

The other options are incorrect for the following reasons:

* The system can process multiple queries in the same conversation as part of its core capabilities.
* Storage capacity is not a significant limitation of the system because it can connect to cloud storage such as Amazon S3.
* Internet connectivity requirements are standard for cloud-based solutions and not a key limitation.

### Summary

* Building an Amazon Q Business application with different content filtering methods
* Understanding the importance of providing context to your query
* Analyzing responses and practicing how to refine queries for better results
* Evaluating if Amazon Q Business can solve a specific business problem
* Understanding the potential limitations of using Amazon Q Business for problem solving
