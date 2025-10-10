# Canvas - AI for Developers

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to repo's main [README.md](../../../README.md)
* back to [AI for Developers main page](./ai-for-developers.md)

## Welcome to AWS Cloud Institute

## Instructor(s) Information

## Week 1 - Additional Resources, Links, Diagrams,

### Examples

In AI/ML, there is a TON of terminology that can be confusing. The best thing to do is that when you encounter a new
term, read the definition and (if necessary) rewrite it in your own words so that as you encounter it later, you have a
better understanding and won't have to spend time trying to figure out it from context. Below are some terms that you
will encounter along with simple definitions. Some of these terms you've not seen in the e-learning yet, but you will in
upcoming modules.

### AI Hierarchy:

AI → Machine Learning → Deep learning → Generative AI

### General AI Terms:

* **Machine Learning:** Algorithms learning from data.
* **Neural Networks:** Simulates human brain connections.
* **Deep Learning:** Multi-layered neural network training.
* **Generative AI:** Produces original, realistic content.
* **Foundational Model:** General-purpose, pre-trained AI model.

### Types of model learning:

* **Supervised Learning:** Trained on labeled data.
* **Unsupervised Learning:** Finds patterns in unlabeled data.
* **Self-Supervised Learning:** Labels generated from input data.
* **Reinforcement Learning:** Learning via rewards and penalties.

### Types of Data:

* **Labeled Data:** Data with assigned annotations.
* **Unlabeled Data:** Data without assigned labels.
* **Structured Data:** Organized, predefined-format data.
* **Unstructured Data:** Unorganized, no predefined format.

### Types of Inference:

* **Batch Inferencing:** Processing multiple inputs simultaneously, usually offline
* **Real-Time Inferencing:** Instantaneous processing of inputs.

### Common AWS AI services:

* **Amazon Comprehend:** NLP service for text analysis.
* **Amazon Lex:** Conversational interface for chatbots.
* **Amazon Transcribe:** Speech-to-text transcription service.
* **Amazon Translate:** Language translation service.
* **Amazon Rekognition:** Image and video analysis service.

### ML pipeline steps and AWS services to use:

* **Data Gathering and Preprocessing:** Preparing raw data for analysis. (SageMaker Data Wrangler)
* **Feature Engineering:** Creating relevant input variables. (SageMaker Feature Store)
* **Model Selection and Training:** Choosing and fitting models to data. (SageMaker JumpStart)
* **Model Evaluation:** Assessing model performance and accuracy. (SageMaker Debugger, Clarify)
* **Model Tuning:** Optimizing model parameters for performance. (SageMaker AMT)
* **Model Deployment:** Implementing model for real-world use. (SageMaker Inference and Batch Transform)
* **Model Monitoring:** Tracking model performance over time. (SageMaker Model Monitoring)

### Transformer Types:

* **Encoder-only:** Processes input for representation, tasks like classification.
* **Encoder-decoder:** Encodes input, decodes output, tasks like translation.
* **Decoder-only:** Autoregressive generation, tasks like text completion.

---

## Week 2 - Additional Resources, Links, Diagrams,LLM (Large Language Model): 

* AI trained for text understanding and generation.
* FM (Foundation Model): Large, pretrained AI model adaptable for tasks.

FM vs. LLM



Inference Parameters

Temperature: Controls randomness in generated responses; higher = more creative.
Top-K: Limits choices to the top-K most probable outputs.
Top-P (Nucleus Sampling): Chooses from tokens whose probabilities sum to P.
Length: Maximum length of the generated output.
Note: Higher Temperature, TopK, TopP: More creative and unpredictable output


LLM concepts

Tokens: Pieces of text (words or characters) processed by models.
Embeddings: Numerical representations of tokens for machine understanding.
Positional Embedding: Encodes token order in sequences for contextual understanding.
Note: positional encoding is fixed, while positional embedding is learned during training. Both are used to incorporate position information in sequence models


Transformer Layers

Embedding Layer: Converts tokens into meaningful numerical vector representations.
Positional Encoding Layer: Adds position information to token embeddings.
Attention Layer: Determines relevance between tokens in a sequence.
Feedforward Layer: Refines token representations with fully connected neural networks.


Prompting

System Messages: Instructions guiding AI's behavior and response style.
User Messages: Inputs or queries provided by the user to the AI.
Assistant Messages: AI-generated responses to user inputs or queries.


Parts of a prompt

Instructions: Guidelines specifying tasks for the AI to perform.
Input Data: Information provided for processing or analysis.
Output Indicators: Signals showing the format or type of expected output.
Context: Background information aiding understanding of inputs and tasks.


Bias vs. Variance

Bias: Error due to overly simplistic assumptions in a model.
Variance: Error due to excessive sensitivity to training data noise.
High Bias: Model oversimplifies, leading to poor performance on training data.
High Variance: Model overfits, performing well on training but poorly on new data.
Hallucinations: AI generating incorrect or nonsensical information confidently.

Lab Notes: Introduction to the Amazon Bedrock Console.

As AI is evolving rapidly, the tools that are used are also changing fast. So there have been a number of UI changes since the lab was written (only a few months ago). Additionally, there were a few things that were called out in the lab, but I missed them when I was doing the lab, so I've put in reminders. Here are some notes to help you as you go through the lab:

* Step 9 – The first time I did the lab, Meta providers did not show up in the “Providers” section, but they are
* available in the “model access” at the bottom of the screen.
* Step 17…”For Throughput” – the heading is actually “Inference”
* Step 23 – The output presents a little strange where it is a numbered list and starts with Miguel and then begins the to do list for the next person as the end of the sentence for the previous person. But if you read through the output, you'll see everything is there.
* Step 26 – The model cannot create a JSON document.
* Step 47 - Note: The Top P parameter determines what percentage of the most likely next word options the model considers when generating text. A lower Top P value means the model considers the words at the top of the list - the most likely or “safe” options. This makes the generated text more predictable and conservative. A higher Top P value means the model looks further down the list, considering some less likely or more “creative” word choices. This makes the output more diverse and unexpected, but also more prone to mistakes or nonsense.
* Step 58 – this could cause responses to be truncated.
* Step 62: You can increase the response length to make this a bit more interesting - The lab does not tell you to change this parameter back, but in order to get the most out of the remaining steps, you should change "length" back to 500 (or more if you want).
* Step 72: Consider: The Amazon Titan model is much faster to respond while the Llama model’s response is more conversational and explanation-based. Also, LLMs usually do not do calculations themselves and may return wrong answers in complex math queries if they are not integrated with other tools.
* Step 87/88 – make sure to hit run
* Step 89 = Must click on one of the images first
* Step 90 – the mask tool is automatically created. To resize the mask tool, you have to go to the corners



Week 2 Summary

This week gave us a deeper insight into the Foundation models and Large Language models and how those fit into the concept of Generative AI. From there, we covered how we can interact with the models use various prompting techniques. We discussed several use cases for Gen AI as well as the different architectures. We wrapped up the discussion with a conversation around AI Business Ethics and some of the risks and benefits of using AI. All of this information sets us up well to start working through the concepts of prompt engineering next week. As a reminder, Monday is a US holiday (see important

---

## Week 3 - Additional Resources, Links, Diagrams,

Prompt Engineering vs Fine-Tuning

Prompt Engineering: Crafting effective inputs to guide a pre-trained model's output without altering its internal
parameters.
Fine-Tuning: Customizing a pre-trained model by training it further on domain-specific
data to adapt its behaviour or improve performance.


Basic Prompting

Zero-shot prompting: Model generates responses without examples, relying solely on instructions.
One-shot prompting: Model generates responses using one example in the prompt as context.
Few-shot prompting: Model generates responses using a few examples to guide its understanding.
Chain-of-Thought prompting: Prompt includes reasoning steps to improve the model’s answer accuracy and depth.
Advanced Prompting
RAG: Retrieval-Augmented Generation combines external knowledge retrieval with generative models for informed
responses.
Automatic Reasoning and Tool-use (ART): Models reason, decide, and use external tools to enhance complex problem solving.
ReAct prompting: Merges reasoning and action steps in prompts to guide interactive problem-solving behavior.
Tree of Thoughts (ToT) prompting: Explores multiple reasoning paths systematically to improve decision-making and
outputs.


RAG

RAG (Retrieval-Augmented Generation) is a method where a model combines its built-in knowledge with external
information retrieved from a database or search engine to generate better responses. Instead of relying only on what it
was trained on, the model fetches up-to-date or specific data to answer questions.

* Benefits: Up-to-date information: It can fetch recent data not included in its training.
* Specificity: Provides more accurate and relevant answers by retrieving precise external facts.
* Efficiency: Reduces the need for fine-tuning since external knowledge fills the gaps.
* Versatility: Adapts to various tasks by retrieving domain-specific knowledge dynamically.



Week 3 Summary

This week covers essential techniques and concepts used to enhance AI model performance and adaptability, focusing
on prompting strategies and methods for integrating external knowledge. We learned that effective prompting
techniques like CoT, ReAct, and ToT can significantly improve task performance. We also saw how RAG and ART methods
allow models to go beyond static knowledge, incorporating dynamic reasoning and external resources, and that
choosing the right strategy depends on the task’s complexity, knowledge requirements, and desired accuracy.

---

## Week 4 - Additional Resources, Links, Diagrams,Amazon Q Developer is an AI-powered coding assistant from AWS designed to help developers with software
development tasks. It integrates with IDEs like VS Code and JetBrains, as well as AWS tools like the AWS Management
Console, to provide AI-driven assistance.


Main Benefits of Amazon Q Developer

* Code Assistance & Autocompletion
    * Suggests code snippets, functions, and entire blocks based on context.
    * Helps speed up development and reduce errors.
* Bug Fixing & Debugging
    * Identifies and suggests fixes for coding errors.
    * Provides explanations for potential issues in the code.
* Code Generation & Refactoring
    * Can generate boilerplate code, unit tests, and documentation.
    * Assists in refactoring for better performance and readability.
* AWS Integration & Cloud Development
    * Helps with writing AWS-specific code (e.g., Lambda, S3, DynamoDB).
    * Provides guidance on AWS services and best practices.
* Security & Compliance Assistance
    * Detects security vulnerabilities and suggests fixes.
    * Helps enforce best practices for secure coding.
* Natural Language Queries
    * Developers can ask questions in plain language, and Amazon Q Developer provides relevant answers
    * based on documentation and past queries.
* Works with Existing Developer Tools
    * Supports major IDEs and integrates with AWS CodeWhisperer and other AWS development tools.



Why Use Amazon Q Developer?

* Boosts Productivity: Reduces time spent on repetitive coding tasks.
* Improves Code Quality: Offers smart suggestions and security checks.
* Enhances AWS Development: Optimized for AWS services and cloud-native applications.
* Simplifies Troubleshooting: Debugging and issue resolution are faster with AI-powered insights.



Amazon Q CLI

AI assistant inside the CLI that’s very easy to access and use.

* Use q chat to chat with the assistant.
* Use q translate to translate natural language to shell commands.



Lab Notes

I'll go through the lab in detail and call out a lot of things during labology, but if you are getting an early start, here are
some things to note:
GENERAL: There is a lot of demonstration of the Amazon Q developer functionality. In other words, they have you do a
number of steps to just look at what it's doing...without any actual impact on what you are trying to accomplish in the
lab. It's just a way to become familiar with the interface and some of the things you can accomplish with it.

* Task 1.2 – in this task, you are enabling Amazon Q and it's access to your code. There are a number of steps here that have to ALL be done or Amazon Q developer will not be enabled in the lab so make sure you are following the steps precisely.
* Step 18 – the pop up looks like an error because it's written in read. It’s simply warning you to make sure the code is the
* same as the one you received. Just continue to follow the instructions in the lab and it will work.
* Step 26 – notice that when you turn on the chat, you now have to panes (code issues and chat). In the instructions in the
* lab, it doesn’t always tell you which pane you should be looking at.
* The next steps are just going to show you some of the functionality of Amazon Q developer – really no rhyme or reason
* to it – just a demo of the functionality…and more importantly, you’re not actually trying to accomplish anything in these
* steps
* Step 27 – simply shows you all the things Amazon Q can do
* Step 28 – The steps don’t give context as to why you are doing these steps, but remember the lab overview – “Another
* developer on your team has handed over some Python, HTML, and CloudFormation files that are uncommented,
* incomplete, and potentially vulnerable.” So you are going to use Amazon Q to help fill in the gaps on all of these points.
* After you do step 28, you should scan through the result – it explains each step of the code and then gives a simple real
* world (non-code) example and then tells you what services are involved in implementing the code.
* Step 29 – The send to prompt allows you to take any of the content and use it as input for the prompts you are going to
* give (IE, allows you to ask questions about it).
* Step 31 – now have explored the functionality of Amazon Q developer, we are going to start using the application and
* finding the issues and leveraging Amazon Q developer for assistance to resolve the issues. In this step, it depends on
* which browser you are using as to whether you need to click the “Open in Browser” – in firefox you do, Chrome
* automatically opened the tab.
* Step 34 – We have now found our first error. This is demonstrating the functionality that is not working in the
* application. Now we’ll use amazon q Developer to help us find and fix this error (and others).
* Step 36 – you’ll now see “Workplace review in progress” – may need to expand the window to see the entire thing.
* Step 37 – note that there are two frames in the amazon q window– code issues and chat. The results show in the chat,
* but the actionable items (things you can click on) are in the code issues frame above the chat.
* Step 40 – you don’t right click, you can either hover over it, click the magnifying glass, or click explain – each one will
* show the reasons, but presents it different ways in the UI.
* Step 41 – when you delete lines 19 and 20, lines 24 and 25 referenced in the instructions are now 22 and 23. Also, there
* was still a comma in the code after removing lines 24 and 25....need to remove that comma.
* Step 43 – Again, no right click, either hover, or use the magnifying glass. The change here is subtle, there is a newer API
* for list_objects – list_objects_v2. Instead of copying and pasting and perhaps not indenting correctly, you may just want to add the underscoreV2 manually.
* Step 52 – had to press the space bar to get the suggestion. Remember for all of the suggestions in the steps following,
* that Amazon Q developer is non-deterministic. So what it suggests may or may not be exactly what's in the lab manual.
* Make sure you are following the code recommendations in the lab manual.
* Step 75 – To get to the Terminal, you may need to click hamburger Menu→View→Terminal if you didn't already have
* the output window open.
* Step 79 -Wait a minute or so. If you do it before a minute, the result will show “Create in progress” meaning the stack is
* not ready to be used yet. If you try to continue before you get the message "Create Complete", the remaining steps will
* notwork.
* Step 83 – Use the explorer window – may need to collapse Backend in order to see and expand front end.

---

## Week 5 - Additional Resources, Links, Diagrams,
Amazon Bedrock endpoints

* bedrock: You can use this endpoint when you want to access Amazon Bedrock itself.
* bedrock-runtime: You can use this endpoint when you want to invoke a model.

Mandatory fields

* modelId
* body

Making a call to the API

* InvokeModel: Calls a Bedrock model with input data, processes it, and returns a single response with the generated output.
* InvokeModelWithResponseStream: Streams model responses in chunks, allowing real-time processing instead of waiting for the entire output.
* Converse: Facilitates stateful interactions with models, maintaining session context to provide coherent, multiturn conversational responses.
* ConverseStream: Streams conversational responses while preserving session context, improving interactivity and responsiveness for real-time chat applications.

Lab notes

This week's lab has you build code to send a prompt to Bedrock and receive the response. I encourage you to try to code
this for yourself leveraging the boto3 documentation and Amazon Q Developer. If you get stuck, you can look at the
solution underneath each task. Make sure to compare your code to the solution to ensure you have everything you need
for the lab to work.
Just a few things to be aware of:
 You can run the code in each code window by pressing Shift-Enter. Not each segment of code has output. If no
output has been defined, when you run it, you will not see anything unless there are errors.
 Steps 11 and 12. You just need to verify that conda_python3 is the kernel in the upper right of the
Jupyter Notebook.
 Task 2.4, make sure to replace ALL instances of "YOUR-REGION-HERE" with the region specified on the left side
of the lab manual. Also replace FMI-Unique-bucket-name with the bucket name listed on the left side of the lab
manual.

---

## Week 6 - Additional Resources, Links, Diagrams,

Lab notes

In this week's lab, we are creating a flash card application leveraging a serverless backend which will integrate to a LLM
service. We’ll then connect it to the front end application. We’ll create and use a lambda function to format and pass
information to the LLM and receive and format the responses. This will enable seamless communication between the
different layers of the application.
When you have completed the lab, you can actually use the flash cards to prepare for the assessment by copying and
pasting content from the e-learning into the App and generating flash cards. For example, in the first section, it discusses
the serverless services. You could copy the text about a service, paste it into the app and generate flashcards and then
text yourself.
A few things to be aware of in the lab:


* Step 6 – it does take a minute for the output to show. You may receive a number of “deprecated” notifications. It will also show some vulnerabilities – In a production environment, you would want to address all of these, but for the lab, You can ignore them.
* Step 8 – if you are copying and pasting – remember to copy the command and replace the “INSERT_S3_BUCKET_NAME” with whatever is showing at the left side of the lab for the S3 Bucket Name. When I copied and pasted, I thought I had overwritten the “insert” part, but actually just concatenated the bucket name to what was there and didn’t notice. And I got a fatal error.
* Step 11 – You WILL get an error. This is expected because you have not specified the API Gateway endpoint Task 2 Make sure you are selecting the correct Llama model. And double check to make sure your region in the console matches the AWS region specified on the left side of your lab.
* Step 22 – make sure to do each of the subtasks including selecting the runtime and make sure you are picking the right version of Python
* Step 23- There are multiple roles that begin with Bedrock – make sure you are selecting BedrockLambdaRole
* Step 24 – the default timeout for a lambda function is 3 seconds. Think about your interactions with LLMs. After you submit a prompt, it may take a little while for the model to generate the inference, so we need to increase the timeout to 1 minute.
* Step 30 – The instructions say to save, but autosave is enabled already so you don’t need to do this.
* Step 37 – make sure to read the explanation of the output.
* Step 43 – make sure you are putting resource name into the correct field
* Step 58 – Keep expanding each section. Demo→/→Bedrock and then you will see the methods. You also need to click no POST in order to see the invoke URL.
* Step 69 – again, if you are copying and pasting ensure that you overwrite the “Insert” part of the string with the actual name of the bucket from the left side of the lab manual.

---

## Week 07 Cheat Sheet

### numpy

#### Array Creation

```python
import numpy as np

np.array([1, 2, 3])              # Create array
np.zeros((3, 3))                 # Array of zeros
np.ones((2, 4))                  # Array of ones
np.eye(3)                        # Identity matrix
np.arange(10)                    # Array from 0 to 9
np.linspace(0, 1, 5)             # 5 evenly spaced numbers from 0 to 1
np.random.rand(3, 3)             # Random values in a given shape
```

#### Array Operations

```text
arr + arr                        # Element-wise addition
arr - arr                        # Element-wise subtraction
arr * arr                        # Element-wise multiplication
arr / arr                        # Element-wise division
np.dot(arr1, arr2)               # Dot product
arr.T                            # Transpose
np.linalg.inv(arr)               # Inverse of a matrix
np.linalg.det(arr)               # Determinant of a matrix
np.exp(arr)                      # Exponential
np.log(arr)                      # Natural logarithm
np.sqrt(arr)                     # Square root
```

#### Array Indexing

```python
arr[0]                           # First element
arr[-1]                          # Last element
arr[2:5]                         # Elements from index 2 to 4
arr[1:, 2:]                      # 2D slicing
```

---

### Pandas

#### Data Structures

```python
import pandas as pd

pd.Series([1, 2, 3])             # Create a series
pd.DataFrame({'A': [1, 2], 'B': [3, 4]})  # Create a dataframe
```

#### Reading/Writing Data

```python
pd.read_csv('file.csv')          # Read CSV
pd.read_excel('file.xlsx')       # Read Excel
df.to_csv('file.csv')            # Write CSV
df.to_excel('file.xlsx')         # Write Excel
```

#### Data Inspection

```python
df.head()                        # First few rows
df.tail()                        # Last few rows
df.info()                        # Concise summary
df.describe()                    # Statistical summary
df.shape                         # Dimensions of DataFrame
```

#### Data Selection

```python
df['A']                          # Select column
df[['A', 'B']]                   # Select multiple columns
df.loc[0]                        # Select row by label
df.iloc[0]                       # Select row by integer index
df.loc[:, 'A':'C']               # Select range of columns
```

#### Data Cleaning

```python
df.dropna()                      # Drop rows with any NaN values
df.fillna(value)                 # Fill NaN values with a specified value
df.drop_duplicates()             # Remove duplicateate rows
```

#### Data Manipulation

```python
df.sort_values('A')              # Sort by values in column A
df.groupby('A').mean()           # Group by column A and calculate mean
df.merge(df2, on='key')          # Merge two DataFrames
df.pivot(columns='A', values='B')  # Pivot table
```

---

### Matplotlib

#### Basic Plotting

```python
import matplotlib.pyplot as plt
 
plt.plot(x, y)                   # Line plot
plt.scatter(x, y)                # Scatter plot
plt.bar(x, height)               # Bar plot
plt.hist(x)                      # Histogram
plt.boxplot(x)                   # Box plot
```

#### Plot Customization

```python
plt.title('Title')               # Add title
plt.xlabel('X Label')            # Add x-axis label
plt.ylabel('Y Label')            # Add y-axis label
plt.legend()                     # Add legend
plt.grid(True)                   # Add grid
plt.xlim([xmin, xmax])           # Set x-axis limits
plt.ylim([ymin, ymax])           # Set y-axis limits
```

#### Multiple Plots

```python
fig, (ax1, ax2) = plt.subplots(1, 2)  # Create subplot
ax1.plot(x, y)
ax2.scatter(x, y)
```

#### Saving Plot

```python
plt.savefig('plot.png')          # Save plot as image
```

---

### Seaborn

#### Basic Plots

```python
import seaborn as sns
sns.scatterplot(x='A', y='B', data=df)  # Scatter plot
sns.lineplot(x='A', y='B', data=df)     # Line plot
sns.barplot(x='A', y='B', data=df)      # Bar plot
sns.boxplot(x='A', y='B', data=df)      # Box plot
sns.violinplot(x='A', y='B', data=df)   # Violin plot
```

#### Distribution Plots

```python
sns.histplot(data=df['A'])       # Histogram
sns.kdeplot(data=df['A'])        # Kernel Density Estimation plot
sns.distplot(df['A'])            # Combination of histogram and KDE
```

#### Categorical Plots

```python
sns.countplot(x='A', data=df)    # Count plot
sns.swarmplot(x='A', y='B', data=df)  # Swarm plot
```

#### Matrix Plots

```python
sns.heatmap(df.corr())           # Correlation heatmap
sns.clustermap(df)               # Clustered heatmap
```

#### Regression Plots

```python
sns.regplot(x='A', y='B', data=df)  # Scatter plot with regression line
sns.lmplot(x='A', y='B', data=df)   # Scatter plot with regression line and confidence interval
```

#### Style and Color

```python
sns.set_style("whitegrid")       # Set plot style
sns.set_palette("pastel")        # Set color palette
```

---
