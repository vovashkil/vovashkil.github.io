# Week 9: Lab 1 - Simplifying AI Development with LangChain

## Lab overview

* [Lab files](./files/W090Lab01AiDevelopmentWithLangChain_files/)

In this lab, you work as a contactor hired by AMusicVenue, an independent theater, to build it’s new, automated, Generative AI-powered, system for booking shows, helping the bar manager, and organizing staff shifts.

You’ll use LangChain components aimed at easing the process of productionalizing Generative AI applications. You’ll start with a LangChain chat model to interact with Amazon Bedrock. You’ll use it to ask questions about how to get more people in the venue door and build the blocks of a tool that talks to bands who want to play at the venue.

LangChain has many components aimed at extending the ability of programmatic interaction with Bedrock models. Of those, you will use messages, prompt templates, output parsers, and document loaders while creating tools for the venue’s bar manager to simplify their day to day tasks.

Finally, you’ll combine all these components while making a stateful chatbot capable of interacting with a shift availability document talking with staff who want to pick up shifts. At completion, you’ll have gained practical experience in utilizing LangChain features to develop Generative AI solutions.

Objectives
By the end of this lab, you will be able to do the following:

Generate text with Bedrock models using LangChain.
Chat with foundation models using LangChain.
Utilize LangChain messages to simplify chatbot creation.
Leverage LangChain templates to interact with chatbots.
Use LangChain output parsers for transforming model responses.
Provide context to models with LangChain document loaders.
Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

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

Task 1: Enable Bedrock model access
In this task, you request access to the models used in this lab in the Amazon Bedrock console.

At the top of the AWS Management Console, in the search bar, search for and choose Amazon Bedrock.
Challenge: Request access to the Amazon Nova Lite model
In this challenge, you will complete the necessary steps to request access to the Amazon Nova Lite model.

To view the solution to request access, expand this section.
In the left navigation pane, scroll down to Configure and learn and choose Model access.

Choose Enable specific models at the top of the screen.

Select the checkbox next to Amazon Nova Lite.

Choose Next.

Choose Submit.

 Expected output: Once the request succeeds, Amazon Bedrock changes the Access status to  Access granted.

 Task complete: You successfully requested access to the Amazon Nova Lite model.

Task 2: Launch a Python notebook
In this task, you access the Jupyter notebook from where you will continue the rest of the tasks for this lab.

From the panel to the left of the lab instructions, copy the LabWorkspaceURL URL value and paste it into a new browser tab.

A page displays that prompts you to enter a password.

Copy the LabWorkspacePassword value from the panel to the left of these instructions, paste it in the Password field and login.

A Visual Studio Code integrated development environment (IDE) displays.

 Note: Prior experience with this IDE is not required.

In the activity bar at the left of the page, choose the  Explorer icon to open the lab directory.

Choose the langchain.ipynb file.

The instructions for the rest of the lab are in the notebook.

Follow the steps documented there to complete the tasks.

 Task complete: You launched a Python notebook in an IDE.

Conclusion
 Congratulations! You successfully did the following:

Generated text with Bedrock models using LangChain.
Chatted with foundation models using LangChain.
Utilized LangChain messages to simplify chatbot creation.
Leveraged LangChain templates to interact with chatbots.
Used LangChain output parsers for transforming model responses.
Provided context to models with LangChain document loaders.
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End Lab and then confirm that you want to end your lab.
