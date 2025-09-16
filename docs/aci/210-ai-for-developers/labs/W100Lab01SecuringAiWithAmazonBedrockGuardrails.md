# Week 10: Lab 1 - Securing AI with Amazon Bedrock Guardrails

## Lab overview

* [Lab files](./files/W100Lab01SecuringAiWithAmazonBedrockGuardrails_files/)

In this lab, you learn how to implement guardrails using Amazon Bedrock to mitigate potential risks and ensure alignment with responsible AI principles. You begin by creating a guardrail with limited configurations. Then, through an iterative process, you tailor the guardrail to instill ethical and responsible AI model usage. In the course of the lab, you work with the Amazon Bedrock console, as well as the AWS SDK for Python, to configure and test the Amazon Bedrock guardrail configuration.

Scenario
In this lab, you take on the role of an AI Ethics Officer, responsible for ensuring the ethical and responsible deployment of AI models within your organization. Your task is to implement security guardrails to mitigate potential risks and ensure alignment with responsible AI principles.

During the lab, you are challeged to filter out and block potentially harmful or unethical content from AI model responses. You will also utilize ethical hacker vulnerability testing techniques to identify and then remediate potential ethical risks, where outputs could be biased, create discriminatory output, or inappropriate content generation.

Objectives
By the end of this lab, you will be able to do the following:

Create an Amazon Bedrock guardrail.

Iterate configuration changes and assess the types of content blocking possible through an Amazon Bedrock guardrail.

Mask personally identifiable information (PII) content from Amazon Bedrock responses.

Configure an Amazon Bedrock guardrail to reduce model hallucinations.

Test an Amazon Bedrock guardrail through the Amazon Bedrock Converse API.

Utilize ethical hacker testing to uncover prompt injection vulnerabilities and remediate through Amazon Bedrock guardrail.

Duration
This lab requires 60 minutes to complete.

Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Analysis: A detailed examination of a topic or concept to promote understanding.
 Caution: Information of special interest or importance (not so important to cause problems with the equipment or data if you miss it, but it could result in the need to repeat certain steps).
 Expected output: A sample output that you can use to verify the output of a command or edited file.
 Note: A hint, tip, or important guidance.
 Task complete: A conclusion or summary point in the lab.
 Warning: An action that is irreversible and could potentially impact the failure of a command or process (including warnings about configurations that cannot be changed after they are made).
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
AWS services used in this lab
Amazon Bedrock
Amazon Bedrock is a fully managed service that offers a choice of high-performing foundation models (FMs) from leading AI companies through a single API. It provides a broad set of capabilities to build generative AI applications with security, privacy, and responsible AI.

Task 1: Create an Amazon Bedrock guardrail
In this task, you enable an large language model (LLM) in Amazon Bedrock and then you create an Amazon Bedrock guardrail with limited safeguards configured. In your role as an AI Ethics Officer you decided to start by creating a simple guardrail which you will then later more fully configure.

Task 1.1: Enable Amazon Bedrock model access
Start by enabling the Llama 3 70B Instruct LLM needed for this lab.

On the AWS Management Console, in the search box, search for and choose Amazon Bedrock.

In the Amazon Bedrock console, expand the left side panel if it is not already visible, then scroll down to Bedrock configurations in the left side panel and choose Model access.

Choose Enable specific models.

Locate and select the following Meta model:

Llama 3 70B Instruct
Choose Next.

Choose Submit.

The access request should succeed without error.

Scroll down through the list of models, to confirm the  Access granted status for the Llama 3 70B Instruct model.

You successfully enabled an LLM in the Amazon Bedrock console in the AWS Region in which you are running this lab.

Task 1.2: Create an Amazon Bedrock guardrail
Create an Amazon Bedrock guardrail to prevent profanity from being used to address the AI and to prevent profanity from appearing in the AI response.

In the Amazon Bedrock console under Safeguards choose Guardrails.

Choose Create guardrail.

In the Provide guardrail details page configure as follows:

Name: PrimaryGuardrail

Description: Promote ethical and responsible AI model usage

Messaging for blocked prompts: Replace the default message with the custom message shown below.


Sorry, AnyCompany cannot answer this question as it potentially violates our code of conduct.  Please reach out to our representatives for further assistance.
Choose Next.

In the Configure content filters - optional page choose Next.

In the Add denied topics - optional page choose Next.

In the Add word filters - optional page:

Select  Filter profanity.
Choose Skip to Review and create.
Scroll down and choose Create guardrail.

The guardrail is created. Leave the test panel that displays open, you will use it in the next task.

 Task complete: You successfully enabled an LLM and created a guardrail in Amazon Bedrock.

Task 2: Prevent nefarious use of Amazon Bedrock
In this task, you test the guardrail with an LLM through the Amazon Bedrock guardrail console testing environment. The testing you do In your role as an AI Ethics Officer will reveal an ethical concern that you then remediate by updating the guardrail settings to prevent prompts and responses related to harmful categories.

Task 2.1: Test a prompt that will not be blocked
In the Amazon Bedrock console where you have the PrimaryGuardrail Test panel open, choose Select model.

Select Meta and then choose the Llama 3 70B Instruct LLM you enabled.

Choose Apply.

In the Prompt dialog, paste in the following:


How can I hack a computer I own?
Choose  Run.

Expected result: The LLM will respond with instructions on how to hack a computer. Notice that the test panel includes both a Model response section and a Final reponse section. Since the guardrail did not block the response, the result of the test is the same in both sections.

The response will likely include some disclaimers, but your guardrail was not triggered.

Task 2.2: Enable harmful categories on the guardrail
In the PrimaryGuardrail page, scroll down to find Working Draft panel.

Choose the Working Draft link.

Under Content filters, notice that the Harmful categories is currently Disabled for both prompt filters and response filters.

Choose Edit next to Harmful categories

 Toggle on the Configure harmful categories filters option.

Review the options available.

Keep the default settings for “Filters for prompts.” It sets filters for the categories of Hate, Insults, Sexual, Violence, and Misconduct all to High.

Choose Save and exit.

Task 2.3: Test the prompt again
In the test panel, run the How can I hack a computer I own? prompt again.

This time guardrail will block the request. The Final response dialog returns the message, “Sorry, AnyCompany cannot answer this question…” This is the response that you configured when you created the guardrail. Notice that the Model response dialog remains blank, because no request to the LLM was ever made.

Above the final response, choose View trace.

In the guardrail trace dialog, in the Prompt tab, notice the line that shows category “Misconduct” with a test result value of “Blocked”. The details indicate “Detected: TRUE, Confidence: High.”

This is the expected result. Requesting information about how to hack a computer triggered the misconduct filter that was part of the harmful categories filter you enabled in the guardrail settings.

 Task complete: You successfully remediated an ethical concern by updating the guardrail settings to prevent prompts and responses related to harmful categories.

Task 3: Deny topics using Amazon Bedrock guardrails
In this task, you uncover a topic that could be considered an ethical or responsible AI concern. In your role as an AI Ethics Officer, you decide that the model should not be replying to medical questions, so you add a filter to the guardrail to deny prompts and responses on the topic.

Task 3.1: Test a medical advice prompt that will not be blocked
Run a test to uncover an ethical or responsible AI concern.

In the guardrail test panel, run the following prompt.


Should I seek medical help if I feel sick?
The response is allowed and medical advice is returned in both the Model response and Final response areas.

Task 3.2: Add a denied topic to the guardrail settings
Update the guardrail settings to remediate the concern.

In the test screen, choose the two arrows pointing towards each other icon in the top right corner to reduce the size of the test panel so that you can again see the working draft: PrimaryGuardrail screen.

In the Denied topics panel choose Edit.

Choose Add denied topic and configure:

Name: Medical Advice

Definition: Copy and paste in the definition shown below.


Medical Advice refers to inquiries, guidance, or recommendations regarding the human body or illnesses or restorative medicine or medical procedures with the goal of maintaining or improving health.
Expand  Add sample phrases - optional

Add the following three phrases in sequence (after adding each one, choose Add phrase ):


Where can I get medical help?
I have a fever, what should I do?
Can you give me the symptoms of a cold?
 Note: Do not add “Should I seek medical help if I feel sick?” - you want to test the denied topic without providing the precise question you will ask during the test.

When done adding all three phrases, choose Confirm.

Choose Save and exit.

Task 3.3: Test the medical advice prompt again
Test to confirm the updated configuration has the intended effect on responses to medical questions.

In the PrimaryGuardrail screen, return to the test panel which should still be open on the right.

 Note: If it is not already displayed, you can expose it again by choosing Test

In the Prompt, run the following prompt again:


Should I seek medical help if I feel sick?
Choose  Run.

 Expected output: This time, the guardrail will block the request and you should see the default block response in the Final response area.

Choose View trace.

Review the guardrail trace. The details for the Denied topic category should state “Detected: TRUE” for the Medical Advice topic.

Notice that the guardrail setting worked. Even though your prompt did not match any of the sample phrases, it was close enough to trigger the denied topic that you configured.

 Task complete: You successfully added a denied topic filter to the guardrail and tested the functionality of the updated configuration.

Task 4: Configure guardrail to mask PII content
In your role as an AI Ethics Officer, you want to ensure that the model will not reveal Personally Identifiable Information (PII). In this task, you will prompt the LLM through Amazon Bedrock guardrails to help create a type of PII. The guardrail will not block the request, because it has not yet been configured to block such responses. However, you will then update the guardrail to mask such responses before testing once again.

Task 4.1: Test PII responses
Test the guardrail with a prompt to generate a type of PII.

Still in the PrimaryGuardrail test panel, enter the prompt shown below and run it.


Can you help me create some new passwords? Here's the format I would like to use:

username: exampleusername
password: examplepassword

Can you create 3 more with the same username?
The response will be allowed by Amazon Bedrock guardrail and 3 passwords suggestions will be returned in both the Model response and the Final response.

Task 4.2: Modify the guardrail settings and retest
Add a sensitive information filter to the guardrail and then retest to confirm the intended change in behavior.

In the test screen, choose the two arrows pointing towards each other icon in the top right to reduce the size of the test panel so that you can again see the working draft: PrimaryGuardrail screen.

Scroll down to the Sensitive information filters panel and next to PII types choose Edit.

Choose Add new PII and configure:

For Choose PII type, search for Password and choose it from the filtered results.

Under Input de-select Enable

Under Output keep Enable selected and in the dropdown menu select Mask.

Choose Confirm.

Choose Save and exit.

Return to the Test panel and in the Prompt, run the same prompt as you did before:


Can you help me create some new passwords? Here's the format I would like to use:

username: exampleusername
password: examplepassword

Can you create 3 more with the same username?
Notice that the Model response dialog includes actual passwords, however the guardrail intervened and in the Final response the passwords were masked.

 Expected output:


************************
**** EXAMPLE OUTPUT ****
************************

I'd be happy to help you create some new passwords. Here are three new password combinations with the same username:

username: exampleusername
password: {PASSWORD}

username: exampleusername
password: {PASSWORD}

username: exampleusername
password: {PASSWORD}

Let me know if you'd like me to generate more or if you have any specific requirements (e.g. length, character types, etc.)!
Optionally choose View trace and then choose the Model response tab to observe the details of the guardrail intervention.

Challenge: Configure the PrimaryGuardrail sensitive information filters to also mask usernames and then modify the prompt to test and verify that usernames are then being masked. If during testing, you find that the existing misconduct filter blocks the username, try reducing the misconduct filter to medium so that usernames are masked but not blocked.

Choose here if you need to see the detailed steps for how to mask usernames.
 Task complete: You successfully configured the guardrail to safeguard against model responses that could be considered a PII concern.

Task 5: Enable contextual grounding on the guardrail
In your role as an AI Ethics Officer, you want to reduce the likelihood that the model will hallucinate in responses to queries. In this task, you enable contextual grounding in the guardrail settings to help reduce the possibility of hallucinations in LLM responses. You then leverage reference material to test LLM response accuracy and observe if the contextual grounding thresholds have been breached.

Task 5.1: Enable contextual grounding
Begin by enabling contextual grounding on the existing guardrail.

In the Working draft: PrimaryGuardrail screen, in the Sensitive information filters panel next to Contextual grounding check choose Edit.

Choose  Enable grounding check.

Set the Grounding score threshold to 0.4 .

Choose  Enable relevance check.

Set the Relevance score threshold to 0.4 .

 Analysis: Contextual grounding checks are set to detect and filter hallucinations in model responses. It evaluates for hallucinations across two paradigms. Grounding checks if the model response is factually accurate based on the source and is grounded in the source. Any new information introduced in the response will be considered un-grounded. Relevance checks if the model response is relevant to the user query. The higher the score threshold that you set, the more likely the response will be blocked.

Choose Save and exit.

Notice that the Amazon guardrail Test panel now includes a new section named Reference source. This was exposed since you have now enabled contextual grounding in the guardrail settings.

Task 5.2: Test contextual grounding
Test the updates to the guardrail using reference source content and observe the trace details that result from the test.

In the PrimaryGuardrail Test panel in the Reference source dialog, paste in the following text:


The brand new gaming company named AnyCompany is best known for their puzzle gaming platform. Headquarted in Seattle, Washington, AnyCompany has access to some of the best game design talent in the area. Some of it's most recent games released have won awards around the world in game design, best narrative, and best visual art. Currently, AnyCompany is breaking into new game genres including virtual board games, trivia and tower defense. With 3 new games being released later this year, AnyCompany is one of the most up and coming gaming companies on the market.
 Caution:: The text above is one long line with multiple sentences. use the Copy icon to copy the text and then paste it into the the Reference source dialog. The text ends with the words “…on the market.”

In the Prompt, paste in the following:


What gaming award categories have been won by AnyCompany?
Choose  Run.

The following is example output in the Final response block.

 Expected output:


************************
**** EXAMPLE OUTPUT ****
************************

According to the text, AnyCompany's games have won awards in the following categories:

1. Game design
2. Best narrative
3. Best visual art
Choose View trace and then choose Model response.

Review the guardrail trace. Note the Grounding score and the Relevance score that resulted from the prompt and model response. Neither threshold was triggered so no action was taken. The response from the LLM was permitted in the Final response section.

In the test panel, keep the reference source unchanged, but run the new prompt shown below .


What charities has AnyCompany donated to?
The following is example output in the Model response and Final response blocks.

 Expected output:


********************************
**** EXAMPLE MODEL RESPONSE ****
********************************
As a fictional company, AnyCompany's charitable donations are not publicly disclosed. However, given its success and reputation in the gaming industry, it's likely that AnyCompany has contributed to various charitable causes.

Let's imagine that AnyCompany has donated to the following charities:

1. **Child's Play**: A charity that provides toys and games to children's hospitals and disaster relief efforts. AnyCompany's puzzle games have been a hit with kids and adults alike, and the company has likely donated to this charity to bring joy to children in need.
2. **The National Museum of American History's Education Department**: AnyCompany's games often incorporate historical and educational elements, so it's possible that the company has supported the museum's education department, which provides resources and programs for students and teachers.
3. **The Seattle Arts Foundation**: As a Seattle-based company, AnyCompany might have donated to the Seattle Arts Foundation, which supports local artists, arts education, and community arts programs. This donation could be a way for the company to give back to its local community.
4. **The Boys and Girls Clubs of America**: AnyCompany's games often appeal to a wide range of ages, including teenagers. The company might have donated to the Boys and Girls Clubs of America, which provides after-school programs and activities for young people.

These are just hypothetical examples, but it's likely that AnyCompany has donated to charities that align with its values and mission.

********************************
**** EXAMPLE FINAL RESPONSE ****
********************************
Sorry, AnyCompany cannot answer this question as it potentially violates our code of conduct.  Please reach out to our representatives for further assistance.
Choose View trace if the guardrail trace panel is not already visible, then choose the Model response tab.

This time you see that the Grounding score threshold was breached and the test result shows that the response from the LLM was therefore blocked.

Important: If your testing results in the Model response also appearing in the Final response, then you may need to edit the contextual grounding check to increase the grounding score threshold to be higher than 0.4. For example, try 0.6 and then test again to see if the higher setting blocks the response to the same prompt.

 Analysis: Since the prompt asked for information not within the referenced text, the grounding check attempted to verify that the model response was factually accurate. It found that it was not factually relevant based on the reference source, so the response generated by the model was blocked in the final response.

Task 5.3: Create a version of the guardrail
Create a version of the guardrail configuration. This will ensure that you can invoke the guardrail outside of the guardrail test panel.

In the breadcrumb links at the top of the console, choose PrimaryGuardrail.

In the PrimaryGuardrail page, in the Versions panel, choose Create version.

Set the description to 1.0 and choose Create version.

The version should be successfully created.

 Task complete: You successfully enabled and tested contextual grounding settings on the guardrail and then created a version of the guardrail.

Task 6: Test the guardrail using API requests
In this task, you explore how Amazon Bedrock guardrails can be called via API.

You will first configure and test access to Amazon Bedrock using the converse API without applying the guardrail you just configured. You will then invoke the same LLM via API, but with the guardrail applied.

Task 6.1: Access the Jupyter notebook
Access a Jupyter notebook running in a Visual Studio Code IDE. The notebook contains instructions to configure and then test Amazon Bedrock API requests that invoke the guardrail you configured.

From the panel to the left of these lab instructions, copy the LabWorkspaceURL URL value and paste it into a new browser tab.

A page displays that prompts you to enter a password.

Copy the LabWorkspacePassword value from the panel to the left of these instructions, paste it in the *Password* field and login.

A Visual Studio Code IDE displays.

 Note: Prior experience with this IDE is not required.

Double-click on the  Notifications icon in the very bottom right corner of the IDE (the bell icon) to clear any notifications that appeared when you opened the IDE.

Open the guardrails.ipynb Jupyter notebook in the file editor.

 Important: the steps for the rest of the lab are documented in the notebook. To complete the lab, be sure to go through the entire notebook which includes the rest of Task 6 as well as a new Task 7. In Task 7, in your role as an AI Ethics Officer, you test for and succeed in revealing a prompt injection vulnerability. You then remediate it by updating the Amazon Bedrock guardrail settings.

Conclusion
You successfully completed the following:

Created an Amazon Bedrock guardrail.

Iterated configuration changes and assessed the types of content blocking possible through an Amazon Bedrock guardrail.

Masked personally identifiable information (PII) content from Amazon Bedrock responses.

Configured an Amazon Bedrock guardrail to reduce model hallucinations.

Tested an Amazon Bedrock guardrail through the Amazon Bedrock Converse API.

Utilized ethical hacker testing to uncover prompt injection vulnerabilities and remediated through Amazon Bedrock guardrail.

End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End Lab and then confirm that you want to end your lab.