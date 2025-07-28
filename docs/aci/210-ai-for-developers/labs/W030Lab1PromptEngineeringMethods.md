# Practicing Prompt Engineering Methods

## Lab Overview

In this lab, you explore various prompting techniques with large language models (LLMs). You start by editing the prompt after every invocation in the Bedrock text playground to understand the impact of various prompting strategies.

You explore in-context learning, which involves providing the model with examples before posing a query. You explore zero-shot prompting, where no examples are provided, one-shot prompting with a single example, and few-shot prompting with multiple examples. Additionally, you will learn about chain-of-thought prompting, which encourages the model to demonstrate its reasoning process.

You will work to reduce their team’s cloud costs. Using a simple prompt and progressively enhancing it by adding delimiters, context, instructions, and data, they will get to a helpful answer to their cloud problem. You will then experiment with summarizing texts, answering questions, and generating content using different prompting approaches.

Throughout the lab, the learner will have opportunities to modify prompts, adjust temperature settings, and create their own prompts to gain hands-on experience in prompt engineering for various tasks and scenarios.

Objectives
By the end of this lab, you will be able to do the following:

Utilize iterative development to create a well-defined prompt.
Demonstrate zero-shot prompting.
Utilize the strengths of one-shot and few-shot prompting.
Obtain semi-deterministic responses using chain-of-thought prompting.
Technical knowledge prerequisites
This lab requires the following:

Familiarity of basic navigation of the AWS Management Console
Completion of ACI Developer Fundamentals 1
Completion of ACI Introduction to Cloud Foundations
No AI/ML experience is necessary
Duration
This lab requires approximately 60 minutes to complete.

Services used in this lab
Amazon Bedrock
Amazon Bedrock is a fully managed service that makes high-performing foundation models (FMs) from leading AI startups and Amazon available for your use through a unified API. You can choose from a wide range of foundation models to find the model that is best suited for your use case.

Amazon Bedrock also offers a broad set of capabilities to build generative AI applications with security, privacy, and responsible AI.

Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 CAUTION: Information of special interest or importance (not so important to cause problems with the equipment or data if you miss it, but it could result in the need to repeat certain steps).
 Expected output: A sample output that you can use to verify the output of a command or edited file.
 Note: A hint, tip, or important guidance.
 Task complete: A conclusion or summary point in the lab.
 WARNING: An action that is irreversible and could potentially impact the failure of a command or process (including warnings about configurations that cannot be changed after they are made).
Start lab
To launch the lab, at the top of the page, choose Start Lab.

 Caution: You must wait for the provisioned AWS services to be ready before you can continue.

To open the lab, choose Open Console .

You are automatically signed in to the AWS Management Console in a new web browser tab.

 Warning: Do not change the Region unless instructed.

Common sign-in errors
Error: Choosing Start Lab has no effect
In some cases, certain pop-up or script blocker web browser extensions might prevent the Start Lab button from working as intended. If you experience an issue starting the lab:

Add the lab domain name to your pop-up or script blocker’s allow list or turn it off.
Refresh the page and try again.
Lab environment
AWS services used in this lab
Amazon Bedrock
Amazon Bedrock is a fully managed service that offers a choice of high-performing foundation models (FMs) from leading AI companies through a single API, along with a broad set of capabilities you need to build generative AI applications with security, privacy, and responsible AI.

Task 1: Enable Bedrock model access
In this task, you request access to the models used in this lab in the Amazon Bedrock console.

At the top of the AWS Management Console, in the search bar, search for and choose Amazon Bedrock.
Challenge: Request access to Meta Llama 3 8B Instruct and Amazon Titan Text models
In this challenge, you will complete the necessary steps to request access to Meta Llama 3 8B Instruct and Amazon Titan Text models.

To view the solution to request access, expand this section.
In the left navigation pane, scroll down to Bedrock configurations and choose Model access.

Choose Enable specific models at the top of the screen.

Select the checkbox next to Amazon Titan Text G1 - Express and Meta Llama 3 8B Instruct.

Choose Next.

Choose Submit.

 Expected output: Once the request succeeds, Amazon Bedrock changes the Access status to  Access granted.

 Task complete: You successfully requested access to the Meta Llama 3 8B Instruct and Amazon Titan Text models.

Task 2: In-context learning
In this task, you learn about in-context learning capability with some examples. Depending on the level of information presented to the model, you can use zero-shot, one-shot or few-shot learning.

Task 2.1: Zero-shot learning
Zero-shot learning involves training a model to generalize and make predictions on unseen classes or tasks. To perform prompt engineering in zero-shot learning environments, you construct prompts that explicitly provide information about the target task and the desired output format.

In this task, you are trying to accomplish the definition of a candle which is described by what it’s not, similar to this statement A candle is not a vehicle/backpack/headphone.

Now that you know what you are trying to accomplish, let’s use the zero-shot prompt technique and observe if you can achieve the desired result.

In the left navigation pane, under Playgrounds, choose Chat/text.

For Mode, choose Single prompt from the dropdown options.

Choose Select model.

In the Select model pop-up window which appears, choose the following options:

For Category, choose Amazon.
For Model, choose Titan Text G1 - Express v1.
For Throughput, choose On-demand.
Choose Apply.

Now you have a prompt text box available to train the model by giving different prompts.

In the prompt text box, enter the following prompt:


Question: What is a candle?
Answer:
Choose Run.

 Expected output: Notice that the output about candle is good, but not what you are looking to accomplish.


************************
**** EXAMPLE OUTPUT ****
************************

A candle is a light that is typically made of wax, which is burned to produce light and heat. It is often used for illumination, decoration, or as a source of heat. Candles come in various shapes, sizes, and colors and can be made from different types of wax, including beeswax, soy wax, and paraffin wax.
As you observed, you did not accomplish the desired output using zero-shot prompting technique. Now, let’s to achieve the desired output using one-shot prompting technique.

Task 2.2: One-shot learning
One-shot learning involves training a model by giving it an example and letting it learn from that example to solve a problem statement.

In this task, you continue to accomplish the definition of a candle described in previous sub-task using one-shot prompt technique.

Clear the response by choosing the sweep button in the top-right corner.

Clear the prompt text box by deleting all the text you entered.

 Note: Here you are learning about prompt techniques which do not involve context learning, hence you are using a text playground. If you used the chat playground or did not sweep the results of the last invocation, the context of the last entered prompt would affect the next question asked, and you could eventually run out of input tokens.

In the prompt text box, enter the following prompt:


Answer the last question

Question: What is a car
Answer: A car is not a dog

Last Question: What is candle?
Answer:
Choose Run.

 Expected output: Notice in the output below that the model answer is closer to the format required but not quite perfect.


************************
**** EXAMPLE OUTPUT ****
************************

A candle is a light.
 Note: The model’s response may not be an exact match of the expected output, and that is fine. If you recieved a response that is significantly different from what is expected, you can choose the sweep button in the top-right corner, and enter the prompt again to get a new response. If you run into issues, try refreshing the page on your browser.

As you observed, you got closer to the desired output using one-shot prompting technique, but not quite perfect. Hence, let’s try to achieve the perfect output using the few-shot prompting technique.

Task 2.3: Few-shot learning
Few-shot learning involves training a model with a limited amount of data for new classes or tasks. Prompt engineering in few-shot learning environments focuses on designing prompts that effectively use limited available training data.

In this task, you continue to accomplish the definition of a candle described in previous sub-task using few-shot prompt technique.

For Mode, ensure Single prompt is still selected.

Clear the response by choosing the sweep button in the top-right corner.

Clear the prompt text box by deleting all the text you entered.

In the prompt text box, enter the following prompt:


Answer the last question
question: What is a car?
answer: A car is not an animal.

question: What is a dog?
answer: A dog is not a vehicle.

last question: What is a candle?
answer:
Choose Run.

 Expected output: As you can notice in the below output, the model finally gave an answer with style which the model learnt from the example which was provided to it.


************************
**** EXAMPLE OUTPUT ****
************************

A candle is not a vehicle.
As you have observed, the model has now responded with the desired output using few-shot prompting technique.

Next, you run the same prompt again with an increased temperature value.

 Note: The temperature value affects the shape of the probability distribution for the predicted output and influences the likelihood of the model selecting lower-probability outputs.

Choose a lower value to influence the model to select higher-probability outputs.
Choose a higher value to influence the model to select lower-probability outputs.
In technical terms, the temperature modulates the probability mass function for the next token. A lower temperature steepens the function and leads to more deterministic responses, and a higher temperature flattens the function and leads to more random responses.

In the Configurations section, change the Temperature value to 1.

Clear the response by choosing the sweep button in the top-right corner.

Clear the prompt text box by deleting all the text you entered.

In the prompt text box, enter the following prompt:


Answer the last question
question: What is a car?
answer: A car is not an animal.

question: What is a dog?
answer: A dog is not a vehicle.

last question: What is a candle?
answer:
Choose Run.

Review the output generated by the model, due to change in temperature configurations the explanation of candle is much more comprehensive.

 Note: If you recieved a response that is significantly different from what is expected, you can choose the sweep button in the top-right corner, and enter the prompt again to get a new response. If you run into issues, try refreshing the page on your browser.

In the Configurations section, change the Temperature value back to 0.
Task 2.4: Chain-of-thought
Chain-of-thought prompting breaks down a problem into a series of intermediate reasoning steps. This way of thinking significantly improves the quality of the outputs generated by the LLMs.

Start with a simple problem. Although many problems seem intuitive to humans, some may be challenging to LLMs if they require solving intermediate steps before giving the final answer.

Clear the response by choosing the sweep button in the top-right corner.

Clear the prompt text box by deleting all the text you entered.

In the prompt text box, enter the following prompt:


Answer the following question by thinking step-by-step.
Question: When I was 16, my sister was half of my age. \
Now, I’m 42. How old is my sister now?
Answer:
Choose Run.

Review the generated output by the model. The correct answer is 34, but the output will likely be incorrect: however, the result can be improved using chain-of-thought prompting.

Now, modify the prompt by make use of chain-of-thought concept with one-shot prompting to solve the same problem.

Clear the response by choosing the sweep button in the top-right corner.

Clear the prompt text box by deleting all the text you entered.

In the prompt text box, enter the following prompt which makes use of chain-of-thought prompting:


Answer the following question by thinking step-by-step.
Question: When I was 10, my sister was half of my age. \
Now, I’m 70. How old is my sister now?
Answer: When I was 10 years old, my sister was half of my age. \
So, the age of the sister at that time = 10/2 = 5 \
This implies that my sister is 5 years younger. \
Now, when I’m 70 years old, the age of my sister = 70 - 5 \
Age of my sister = 65. \
Question: When I was 16, my sister was half of my age. \
Now I’m 42. How old is my sister now?
Answer:
 Note: Notice how the prompt is using the chain-of-thought concept along with the use of one-shot prompting by providing the model with similar problem and a solution for the same.

Choose Run.

 Expected output: Review the generated output by the model. This time the model is much more likely to respond with correct answer to the problem.


************************
**** EXAMPLE OUTPUT ****
************************

When I was 16 years old, my sister was half of my age. 

So, the age of the sister at that time = 16/2 = 8 

This implies that my sister is 8 years younger. 

Now, when I’m 42 years old, the age of my sister = 42 - 8 

Age of my sister = 34.
 Note: If you recieved a response that is significantly different from what is expected, you can choose the sweep button in the top-right corner, and enter the prompt again to get a new response. If you run into issues, try refreshing the page on your browser.

 Task complete: You successfully learnt about in-context learning capability with some examples utilizing zero-shot, one-shot, and few-shot learning.

Task 3: Basics of prompting
In this task, you learn and use basic prompting techniques in different scenarios.

Task 3.1: Change model to Meta Llama 3 8B Instruct
For the initial part of this task, you make use of the Meta Llama 3 8B Instruct model.

In the Configurations section, near the Titan Text G1 - Express model name, choose Change.

In the Select model pop-up window which appears, choose the following options:

For Category, choose Meta.
For Model, choose Llama 3 8B Instruct v1.
For Throughput, choose On-demand.
Choose Apply.

Now you have a prompt text box available to train the model by giving different prompts.

Task 3.2: Give prompts and context the new model
For this task, you are the go-to-person for cloud questions and solutions in your organization, a cloud photo storage company. Your Chief Technology Officer has sent you an email stating that your company is overspending on AWS S3 storage by approximately $4 million a quarter. Utilize basic prompt engineering techniques to form a strategy for lowering cloud costs.

Clear the response by choosing the sweep button in the top-right corner.

Clear the prompt text box by deleting all the text you entered.

In the Configurations section, change the Temperature value back to 0 so that the output is more deterministic.

In the prompt text box, enter the following prompt:


How can we lower cloud costs?
Choose Run.

Review the output generated by the model. The answer provides different strategies to lower cloud costs.

Now, add more context to your prompt by including information such as what your company supplies to consumers. In this case, your company is a cloud photo storage company.

Clear the response by choosing the sweep button in the top-right corner.
Clear the prompt text box by deleting all the text you entered.
 Note: Clearing or sweeping the results of the last invocation clears the context used during the last entered prompt so that it does not affect the next question asked.

In the prompt text box, enter the following prompt:


Our company supplies cloud photo hosting to consumers by using S3. How can we lower cloud costs?
Choose Run.

Review the output generated by the model. The answer provided now is more focused around optimizing data storage.

Next, you make use of delimiters and instructions. In the context of prompt engineering, delimiters are characters or sequences of characters that mark the beginning and end of various sections within a prompt.

Clear the response by choosing the sweep button in the top-right corner.

Clear the prompt text box by deleting all the text you entered.

In the prompt text box, enter the following prompt:


Our company supplies cloud photo hosting to consumers by using S3. How can we lower cloud costs? Provide the top 3 answers in a one paragraph summary.
Choose Run.

Review the output generated by the model, the answer provides top 3 different strategies to lower cloud costs in a single paragraph.

Now, you make prompt by adding more effective context, instructions, and data about your company in your prompt, so that the model provides you with a more appropriate answer to lower cloud costs.

Clear the response by choosing the sweep button in the top-right corner.

Clear the prompt text box by deleting all the text you entered.

In the prompt text box, enter the following prompt:


Our company supplies cloud photo hosting to consumers by using S3. Typically customers do not access their photos after one year. We spent $4 million on AWS S3 buckets last quarter. We are looking to lower cloud cost. Provide a numbered list of your top 3 answers, providing an estimated cost savings for each suggestion.
Choose Run.

Review the output generated by the model. The answer provides the top 3 strategies to lower cloud costs. As requested in the prompt, it also provides an estimated amount of savings which you can achieve using these strategies.

 Task complete: You successfully learnt and used basic prompting techniques in different scenarios.

Task 4: Use-cases of prompt engineering
In this task, you learn about different use-cases of prompt engineering.

Task 4.1: Text Summarization
Summarization is the prompting technique in which you provide an LLM a passage of text and the model must respond with a shorter passage that captures the main points of the input.

For the remaining exercises, revert back to the Titan Text G1 - Express model.

In the Configurations section, near the Llama 3 8B Instruct model name, choose Change.

In the Select model pop-up window which appears, choose the following options:

For Category, choose Amazon.
For Model, choose Titan Text G1 - Express v1.
For Throughput, choose On-demand.
Choose Apply.

Clear the response by choosing the sweep button in the top-right corner.

Clear the prompt text box by deleting all the text you entered.

In the prompt text box, enter the following prompt:


The following is a text about S3 storage storage classes. Summarize it. 
Text: Do you have data that becomes infrequently accessed after a definite period of time? Take, for example, user-generated content like social media apps. We share videos and pictures with our network that gets frequently accessed right after we upload it but becomes infrequently accessed a few weeks later or even a few days/hours. For use cases like these, many customers know when data becomes infrequently accessed or can usually pinpoint the right time they should move data from S3 Standard to a lower-cost storage class optimized for infrequent or archive access.
Many customers that have predictable access patterns get started with S3 Storage Lens to gain a detailed understanding of their usage for all of their buckets within an account. If you have enabled S3 Storage Lens advanced metrics, you have access to activity metrics to identify datasets (buckets) that are frequently, infrequently, or rarely accessed. There are metrics like GET requests and download bytes that indicate how often your datasets are accessed each day. You can trend this data over several months (extended data retention is available with advanced tier) to understand the consistency of the access pattern and to spot datasets that become infrequently accessed.
Once you know when a dataset becomes infrequently accessed or can be archived, you can easily configure an Amazon S3 Lifecycle rule to automatically transition objects stored in the S3 Standard storage class to the S3 Standard-Infrequent Access, S3 One Zone-Infrequent Access, and/or S3 Glacier storage classes based on the age of the data. You can set up and manage Lifecycle policies in the AWS Management Console, S3 REST API, AWS SDKs, or AWS Command Line Interface (CLI). You can specify the policy at the prefix or at the bucket level. For example, you might choose to transition objects to the S3 Standard-IA storage class 30 days after you created them, or archive objects to the S3 Glacier storage class one year after creating them.
Choose Run.

Review the output generated. The inserted text is summarized into a few lines successfully by the model.

Now, try another prompt with more context.

Clear the response by choosing the sweep button in the top-right corner.

Clear the prompt text box by deleting all the text you entered.

In the prompt text box, enter the following prompt:


The following is a text about S3 storage storage classes. Write a one sentence summary of the most important point.
Text: Do you have data that becomes infrequently accessed after a definite period of time? Take, for example, user-generated content like social media apps. We share videos and pictures with our network that gets frequently accessed right after we upload it but becomes infrequently accessed a few weeks later or even a few days/hours. For use cases like these, many customers know when data becomes infrequently accessed or can usually pinpoint the right time they should move data from S3 Standard to a lower-cost storage class optimized for infrequent or archive access.
Many customers that have predictable access patterns get started with S3 Storage Lens to gain a detailed understanding of their usage for all of their buckets within an account. If you have enabled S3 Storage Lens advanced metrics, you have access to activity metrics to identify datasets (buckets) that are frequently, infrequently, or rarely accessed. There are metrics like GET requests and download bytes that indicate how often your datasets are accessed each day. You can trend this data over several months (extended data retention is available with advanced tier) to understand the consistency of the access pattern and to spot datasets that become infrequently accessed.
Once you know when a dataset becomes infrequently accessed or can be archived, you can easily configure an Amazon S3 Lifecycle rule to automatically transition objects stored in the S3 Standard storage class to the S3 Standard-Infrequent Access, S3 One Zone-Infrequent Access, and/or S3 Glacier storage classes based on the age of the data. You can set up and manage Lifecycle policies in the AWS Management Console, S3 REST API, AWS SDKs, or AWS Command Line Interface (CLI). You can specify the policy at the prefix or at the bucket level. For example, you might choose to transition objects to the S3 Standard-IA storage class 30 days after you created them, or archive objects to the S3 Glacier storage class one year after creating them.
Choose Run.

Review the output generated. The response is a one sentence summary of the most important point of the text, or at least it is significantly shorter than the prior response.

Task 4.2: Question and Answer
For this prompt, you provide input text with a question. The model must answer the question based on information provided within the input text.

Clear the response by choosing the sweep button in the top-right corner.

Clear the prompt text box by deleting all the text you entered.

In the prompt text box, enter the following prompt:


Where are S3 Storage Lens metrics displayed?
Text: (Amazon S3 Storage Lens is a cloud-storage analytics feature that you can use to gain organization-wide visibility into object-storage usage and activity. You can use S3 Storage Lens metrics to generate summary insights, such as finding out how much storage you have across your entire organization or which are the fastest-growing buckets and prefixes. You can also use S3 Storage Lens metrics to identify cost-optimization opportunities, implement data-protection and security best practices, and improve the performance of application workloads. For example, you can identify buckets that don't have S3 Lifecycle rules to expire incomplete multipart uploads that are more than 7 days old. You can also identify buckets that aren't following data-protection best practices, such as using S3 Replication or S3 Versioning. S3 Storage Lens also analyzes metrics to deliver contextual recommendations that you can use to optimize storage costs and apply best practices for protecting your data.
S3 Storage Lens aggregates your metrics and displays the information in the Account snapshot section on the Amazon S3 console Buckets page. S3 Storage Lens also provides an interactive dashboard that you can use to visualize insights and trends, flag outliers, and receive recommendations for optimizing storage costs and applying data-protection best practices. Your dashboard has drill-down options to generate and visualize insights at the organization, account, AWS Region, storage class, bucket, prefix, or Storage Lens group level. You can also send a daily metrics export in CSV or Parquet format to an S3 bucket. You can create and manage S3 Storage Lens dashboards by using the Amazon S3 console, AWS Command Line Interface (AWS CLI), AWS SDKs, or Amazon S3 REST API.)
Choose Run.

Review the output generated, the model answers the question asked using the inserted text as a reference.

Next, try a few more question answer prompts.

Clear the response by choosing the sweep button in the top-right corner.

Clear the prompt text box by deleting all the text you entered.

In the prompt text box, enter the following prompt:


What file formats can I send Storage Lens reports in?
Text: Amazon S3 Storage Lens is a cloud-storage analytics feature that you can use to gain organization-wide visibility into object-storage usage and activity. You can use S3 Storage Lens metrics to generate summary insights, such as finding out how much storage you have across your entire organization or which are the fastest-growing buckets and prefixes. You can also use S3 Storage Lens metrics to identify cost-optimization opportunities, implement data-protection and security best practices, and improve the performance of application workloads. For example, you can identify buckets that don't have S3 Lifecycle rules to expire incomplete multipart uploads that are more than 7 days old. You can also identify buckets that aren't following data-protection best practices, such as using S3 Replication or S3 Versioning. S3 Storage Lens also analyzes metrics to deliver contextual recommendations that you can use to optimize storage costs and apply best practices for protecting your data.
S3 Storage Lens aggregates your metrics and displays the information in the Account snapshot section on the Amazon S3 console Buckets page. S3 Storage Lens also provides an interactive dashboard that you can use to visualize insights and trends, flag outliers, and receive recommendations for optimizing storage costs and applying data-protection best practices. Your dashboard has drill-down options to generate and visualize insights at the organization, account, AWS Region, storage class, bucket, prefix, or Storage Lens group level. You can also send a daily metrics export in CSV or Parquet format to an S3 bucket. You can create and manage S3 Storage Lens dashboards by using the Amazon S3 console, AWS Command Line Interface (AWS CLI), AWS SDKs, or Amazon S3 REST API.
Choose Run.

Review the output generated. The model answers the question asked using the inserted text as a reference.

Now you will ask the model couple of follow up questions related to the CSV format.

Clear the response by choosing the sweep button in the top-right corner.

Clear the prompt text box by deleting all the text you entered.

In the prompt text box, enter the following prompt:


What is CSV format?
Can I convert CSV to Parquet?
 Note: You can observe that the above prompt does not have any input data as these are plain questions which are asked to the model.

Choose Run.

Review the output generated, the model answers about the question asked, by providing detailed explanation of CSV format and ways to convert it to Parquet.

Task 4.3: Prompt interrogation
In this section, you will learn how to increase effectivity of your prompts by beginning prompts with words such as who, what, where, when, why, and how. Here, you will start by using a less effective prompt. Then, you follow it up by using a more effective prompt to check the difference in the generated outputs.

Clear the response by choosing the sweep button in the top-right corner.

Clear the prompt text box by deleting all the text you entered.

In the prompt text box, enter the following prompt:


Summarize the following:
Text: There’s very little to write about regarding the migration effort, which is an engineer’s dream! We applied a lifecycle policy to each of the buckets, and quickly migrated nearly 80 billion objects in approximately two days. At the time of writing this blog, roughly 130 petabytes of Canva’s total 230 petabytes of data in S3 resides in S3 Glacier Instant Retrieval. We have found it extremely valuable as a tool for reducing costs on our infrequently accessed user data. It offers the best of both worlds from S3 Standard-IA and S3 Glacier Flexible Retrieval.
Canva saves roughly $300,000 per month ($3.6 million annually) thanks to these changes, and given the ever-growing amount of user-generated data we store, these savings continue to grow over time. It’s very important to remember that these savings required us to first understand the access patterns for our data, as well as a one-off spend of $1.6 million to transition roughly 80 billion objects. Overall this meant that we saw a positive ROI after only a few months of making the transition, which is still pretty fantastic!
AWS has been a great partner through all of this work and continues to invest in fit-for-purpose storage classes, to help customers with use cases at any scale. Thanks for reading this blog post! Don’t hesitate to leave your feedback in the comments section.
Choose Run.

Review the output generated, the model summarizes the text.

 Note: This is not an effective way of prompting as the output is just a summary of the text provided.

To make the prompt more effective, use the following prompt which makes use of keyword How at the beginning.

Clear the response by choosing the sweep button in the top-right corner.

Clear the prompt text box by deleting all the text you entered.

In the prompt text box, enter the following prompt:


How did Canva reduce S3 cost?
Text: There’s very little to write about regarding the migration effort, which is an engineer’s dream! We applied a lifecycle policy to each of the buckets, and quickly migrated nearly 80 billion objects in approximately two days. At the time of writing this blog, roughly 130 petabytes of Canva’s total 230 petabytes of data in S3 resides in S3 Glacier Instant Retrieval. We have found it extremely valuable as a tool for reducing costs on our infrequently accessed user data. It offers the best of both worlds from S3 Standard-IA and S3 Glacier Flexible Retrieval.
Canva saves roughly $300,000 per month ($3.6 million annually) thanks to these changes, and given the ever-growing amount of user-generated data we store, these savings continue to grow over time. It’s very important to remember that these savings required us to first understand the access patterns for our data, as well as a one-off spend of $1.6 million to transition roughly 80 billion objects. Overall this meant that we saw a positive ROI after only a few months of making the transition, which is still pretty fantastic!
AWS has been a great partner through all of this work and continues to invest in fit-for-purpose storage classes, to help customers with use cases at any scale. Thanks for reading this blog post! Don’t hesitate to leave your feedback in the comments section.
Choose Run.

Review the output generated. The model now answers with a better explanation about the text and the question which was asked.

Task 4.4: Text Generation
In this section, you give a prompt and the model must respond with a passage of original text that matches the description. This also includes the generation of creative text such as stories, poems, or movie scripts.

Start with an example which writes a response to an email sent by the Chief Technology Officer.

Clear the response by choosing the sweep button in the top-right corner.

Clear the prompt text box by deleting all the text you entered.

In the prompt text box, enter the following prompt:


Write an email to the Chief Technology Officer of the photo storage company I work for. It should explain that we will be implementing S3 Storage Lens and S3 Lifecycle policies. It should respond to the following email he sent me. Chief Technology Officer email: We spent $4 million last quarter on S3 buckets. Can we get that down? -María
Choose Run.

Review the output generated. The model responded with a draft of the email you requested.

Next example is to write creative product descriptions for our products. In the example below, you create three product descriptions for an internal project related to S3 Storage Lens and Lifecyle policies.

Clear the response by choosing the sweep button in the top-right corner.

Clear the prompt text box by deleting all the text you entered.

In the prompt text box, enter the following prompt:


Project: Implement S3 Storage Lens and Lifecyle policies. Keywords: cost-savings, photo storage. List three potential clever internal project names.
Choose Run.

Review the output generated, the model responded with 3 different project names to implement S3 Storage Lens and Lifecyle policies.

Challenge: Generate text with exclamation points
In this challenge, you will ask the model to generate an email in the voice of a friend congratulating someone about a new job.

To view the solution of a more effective prompt, expand this section.
Clear the response by choosing the sweep button in the top-right corner.

Clear the prompt text box by deleting all the text you entered.

In the prompt text box, enter the following prompt:


Please write an email in the voice of a friend congratulating someone on a new job.
Choose Run.

 Task complete: You successfully learnt about different use-cases of prompt engineering.

Conclusion
 Congratulations! You now have successfully:

Utilized iterative development to create a well-defined prompt.
Demonstrated zero-shot prompting.
Utilized the strengths of one-shot and few-shot prompting.
Obtained semi-deterministic responses using chain-of-thought prompting.
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End Lab and then confirm that you want to end your lab.

Additional Resources
For more information about What is a prompt?, see What is a prompt?.
For more information about What is prompt engineering?, see What is prompt engineering?.
