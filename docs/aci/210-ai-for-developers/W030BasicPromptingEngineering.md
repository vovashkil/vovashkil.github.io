# Week 3: Basic Prompt Engineering

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to [AI for Developers](./ai-for-developers.md)
* back to repo's main [README.md](../../../README.md)

## Basics of Foundation Models

Although traditional ML models rely on supervised, semi-supervised, or unsupervised learning patterns, FMs are typically pre-trained through self-supervised learning.

### Foundations of prompt engineering

Generative AI is a type of artificial intelligence that can create new content and ideas, including conversations, stories, images, videos, and music. Like all other AI, generative AI is powered by machine learning (ML) models. However, generative AI is powered by very large models, commonly called foundation models (FMs). FMs are pre-trained on a vast corpus of data, usually through self-supervised learning.

### Basics of Foundational Models

#### Prompt engineering

* Creating prompts
* Optimizing prompts

#### The principles, techniques and best practices for designing effective prompts

Prompts are essentially instructions. And when we interact with a foundation model, the prompt is the input that we would give the model to generate a response.

```text
Prompt

The input that you give the model; to generate a response
```

For example, let's say we give a foundation model a prompt asking for a phrase to be translated from English to Spanish. Now, assuming the foundation model has been trained to do that, it will return the phrase in Spanish.

```text
Prompt

Translate the following text from English to Spanish

Hello, how are you today?
```

```text
Output

Hola, como estas hoy?
```

The quality and the structure of the prompt can significantly influence the foundation model's performance on a given task, and this is where prompt engineering comes into play.

The quality and structure of the prompt can significantly influence the foundation model's performance on a given task, and this is where prompt engineering comes into play. Now prompt engineering is a new and important field for optimizing how we apply, develop, and understand language models, especially large models. It's the process of carefully designing and optimizing your input prompts to effectively interact and guide AI models, especially in natural language processing.

* crafting inputs that are clear, contextually appropriate and aligned with the specific capabilities and limitations of the model in order to elicit desired responses
* the quality of the input prompt significantly influences the output of the model

##### Optimizing how we apply, develop, and understand language models

* Expand what language technologies can do
* Address their weaknesses
* Gain insights into their functioning

The models are very sensitive to the input prompt.

Although traditional machine learning models rely on supervised, semi-supervised, or unsupervised learning patterns, foundation models are typically pre-trained through self-supervised learning.

Generative AI primarily uses self-supervised learning. This is an approach where the foundational model is trained on vast amounts of unlabeled data, enabling the model to learn rich representations of language or visual input depending on the purpose of the model. Unlike supervised learning that relies on labeled datasets, self-supervised learning allows models to learn from data where the input itself provides the supervision. Essentially, the model is trained to predict parts of the input from other parts of the input.

##### Self-supervised and unsupervised learning difference

* Both approaches, unsupervised learning, self-supervised learning, learn from data without explicit labels
* The difference lies in how the learning process is structured.

##### Self-supervised learning

The system generates its own supervisory signal based on the input data. A common approach in training large language models is to remove a word from a sentence, that's in the training data, and train the model to predict the missing word based on the context provided by the other words.

For example, consider the sentence:

```text
The quick brown fox jumps over the lazy dog.
```

This is an example of unlabeled data because it is literally the data, there's no labels. This would go into the machine learning algorithm, training our large language model, and what it will do is it will remove a word. Let's say it removes the word **lazy**.

```text
The quick brown fox jumps over the xxxxxxx dog.
```

This hidden word here serves as a **pseudo label**.

What is meant by pseudo label is it is essentially trying to predict that missing word. The model tries to predict what that word should be. And then the prediction is compared against the known correct word. In other words. the pseudo label, which in this case is **lazy**. And it's through this process of prediction. The model might predict the word as **enthusiastic**. It would then compare it to the pseudo label, what the known correct word is, which is **lazy**. It would then update the parameters in the model and then try again to predict it. It's through this process of prediction and comparison, it learns to make better predictions. In essence, these pseudo labels provide a way for self-supervised learning models to train on unlabeled data by creating a supervised learning like scenario, where the model predicts parts of the data based on the rest. 

This approach harnesses the vast amounts of unlabeled data available, such as all the written texts on the Internet. It can use all of that because the data doesn't have to be labeled. And that leads to more robust and versatile models because of the amount of data that it has access to.

#### Various stages that a foundational model goes through during training to achieve the best results: training, fine-tuning, and prompt engineering

* Pre-training

  * FMs use self-supervised learning or reinforcement learning from human feedback (RLHF), to capture data from vast datasets

* Fine-training - additional training using a supervised learning approach with specific, smaller datasets to better align with the particular task that you wish to use that model for

  * Instruction fine-tuning which is prompt engineering
  * Reinforcement learning from human feedback (RLHF) - combining human feedback with reinforcement learning techniques to improve a model's performance and alignment with desired outputs

* Prompt Engineering

  * Prompts act as instructions for foundation models
  
___

For example, we're fine-tuning a chatbot to provide customer support. Initially, the chatbot is trained on a large dataset, but its responses might not always align with your company's specific customer service guidelines. To improve this, we use RLHF as follows. Human feedback, so the human feedback portion of it. Human reviewers evaluate the chatbots responses, marking or highlighting which ones are good and which ones are inappropriate or just unhelpful. Then through reinforcement learning, the chatbot uses this feedback to learn. It adjusts its algorithms to increase the likelihood of generating the kinds of responses marked as good as the reviewers, and minimizing the chance of generating responses that have been marked as not so good by the reviewers.

Finally, we have prompt engineering. Even if you fine-tune the model, you still need to provide it with specific, actionable instructions about what you want it to do. So, prompt engineering is usually always employed as part of the process to get the best results from the model.

#### Ttwo of the most common types of foundation models

* text-to-text models are also known as large language models, are pre-trained to process vast quantities of textual data and human language
* text-to-image models take natural language and produce a high-quality image that matches the input text description

#### Text-to-text models use cases

* summarize texts
* extract information
* respond to questions
* create content such as blogs, or product descriptions

##### Understanding large language model (LLM) functionality

* Neural network layers

  * Embedding Layer converts input tokens, words to the large language models, into vectors known as embeddings, allowing the meaning of those tokens to be mathematically captured
  * Attention mechanism allows the model to focus on different parts of the input sequence to understand the context and the relationship between those words or the embeddings
  * Feedforward layers further process the information, helping the model to refine its understanding and generate appropriate responses

### Foundational model functionality

The size and general-purpose nature of foundation models make them different from traditional ML models. FMs use deep neural networks to emulate human brain functionality to handle complex tasks. You can adapt them for a broad range of general tasks, such as text generation, text summarization, information extraction, image generation, chat-based assistant, and question answering. FMs can also serve as the starting point for developing more specialized models. Examples of FMs include Amazon Titan, Meta Llama 2, Anthropic Claude, AI21 Labs Jurassic-2 Ultra, and more.

![A process graphic showing the input of unlabeled data into a foundation model and then adapted to perform a variety of tasks.](./images/W03Img010FmFuncionality.png)

#### Self-supervised learning

(opens in a new tab)Although traditional ML models rely on supervised, semi-supervised, or unsupervised learning patterns, FMs are typically pre-trained through self-supervised learning. With self-supervised learning, labeled examples are not required. Self-supervised learning makes use of the structure within the data to autogenerate labels.

#### Training, fine-tuning, and prompt tuning

Foundation models go through various stages of training to achieve the best results.

##### Pre-training

During the training stage, FMs use self-supervised learning or reinforcement learning from human feedback (RLHF) to capture data from vast datasets. The FM's algorithm can learn the meaning, context, and relationship of the words in the datasets. For example, during the training stage, the model might learn whether drink means beverage, the noun, or swallowing the liquid, the verb.

In addition, RLHF technique can be used during pre-training to better align the model with human preferences. In this approach, humans provide feedback on the model outcomes, and that information is used by the model to change its behavior.

##### Fine-tuning

Though FMs are pretrained through self-supervised learning and have inherent capability of understanding information, fine-tuning the FM base model can improve performance. Fine-tuning is a supervised learning process that involves taking a pretrained model and adding specific, smaller datasets. Adding these narrower datasets modifies the weights of the data to better align with the task.

There are two ways to fine-tune a model:

1. **Instruction fine-tuning** uses examples of how the model should respond to a specific instruction. Prompt tuning is a type of instruction fine-tuning.
2. **RLHF** provides human feedback data, resulting in a model that is better aligned with human preferences.

Let's consider a use case for fine-tuning. If you are working on a task that requires industry knowledge, you can take a pretrained model and fine-tune the model with industry data. If the task involves medical research, for example, the pretrained model can be fine-tuned with articles from medical journals to achieve more contextualized results.

Although fine-tuning has its benefits, it has a significant financial and resource cost to undertake. A preferred initial approach to augmenting an FM's responses is prompt engineering.

##### Prompt engineering

Prompts act as instructions for foundation models. They are similar to fine-tuning, but you don’t need to provide labeled sample data as you would to fine-tune a model. You use various prompt techniques to achieve better performance. Prompt engineering is a more efficient way to tune LLM responses, as opposed to fine-tuning, which requires labeled data and training infrastructure.

#### Types of FMs

FMs can be categorized into multiple categories. Two of the most frequently used models are text-to-text models and text-to-image models.

##### Text-to-text models

Text-to-text models are LLMs that are pre-trained to process vast quantities of textual data and human language. These large foundation models can summarize text, extract information, respond to questions, create content (such as blogs or product descriptions), and more.

##### Text-to-image models

Diffusion is a deep learning architecture system that learns through a two-step process. The first step is called forward diffusion. Using forward diffusion, the system gradually introduces a small amount of noise to an input image until only the noise is leftover. There is a U-Net model, which tracks and predicts the noise level. In the subsequent reverse diffusion step, the noisy image is gradually introduced to denoising until a new image is generated. During the training process, the model gets the feed of text, which is added to the image vector. To learn more about diffusion architecture, review the "High-Resolution Image Synthesis with Latent Diffusion Models" article located in the Additional Resources section.

The following explains the three types of models and includes text-to-text and text-to-image models.

1. Natural language processing (NLP)

    NLP is a machine learning technology that gives machines the ability to interpret and manipulate human language. NLP does this by analyzing the data, intent, or sentiment in the message and responding to human communication. Typically, NLP implementation begins by gathering and preparing unstructured text or speech data from different sources and processing the data. It uses techniques such as tokenization, stemming, lemmatization, stop word removal, part-of-speech tagging, named entity recognition, speech recognition, sentiment analysis, and so on. However, modern LLMs don't require using these intermediate steps.

2. Recurrent neural network (RNN)

    RNNs use a memory mechanism to store and apply data from previous inputs. This mechanism makes RNNs effective for sequential data and tasks, such as natural language processing, speech recognition, or machine translation. However, RNNs also have limitations. They are slow and complex to train, and they can’t be used for training parallelization.

3. Transformer

A transformer is a deep-learning architecture that has an encoder component that converts the input text into embeddings. It also has a decoder component that consumes the embeddings to emit some output text. Unlike RNNs, transformers are extremely parallelizable, which means that instead of processing text words one at a time during the learning cycle, transformers process input all at the same time. It takes transformers significantly less time to train, but they require more computing power to speed training. The transformer architecture was the key to the development of LLMs. These days, most LLMs only contain a decoder component.

___

### LLMs

Large language models (LLMs) are a subset of foundation models. LLMs are trained on trillions of words across many natural language tasks. LLMs can understand, learn, and generate text that’s nearly indistinguishable from text produced by humans. LLMs can also engage in interactive conversations, answer questions, summarize dialogues and documents, and provide recommendations.

Because of their sheer size and AI acceleration, LLMs can process vast amounts of textual data. LLMs have a wide range of capabilities, such as creative writing for marketing, summarizing legal documents, preparing market research for financial teams, simulating clinical trials for healthcare, and writing code for software development.

#### Understanding LLM functionality

Most LLMs are based on a transformer model. They receive the input, encode the data, and then decode the data to produce an output prediction.

#### Neural network layers

Transformer models are effective for natural language processing because they use neural networks to understand the nuances of human language. Neural networks are computing systems modeled after the human brain. There are multiple layers of neural networks in a single LLM that work together to process input and generate output.

##### Embedding layer

The ***embedding layer*** converts input text to vector representations called embeddings. This layer can capture complex relationships between the embeddings, so the model can understand the context of the input text.

##### Feedforward layer

The ***feedforward layer*** consists of several connected layers that transform the embeddings into more weighted versions of themselves. Essentially, this layer continues to contextualize the language and helps the model better understand the input text's intent.

##### Attention mechanism

With the ***attention mechanism***, the model can focus on the most relevant parts of the input text. This mechanism, a central part of the transformer model, helps the model achieve the most accurate output results.

#### LLM use cases

You can use LLMs for a wide range of tasks and in almost every domain.

##### Improving customer experiences

* **Chatbots and virtual assistants**: Streamline customer self-service processes and device operational costs by automating responses for customer service queries through generative AI-powered chatbots, voice bots, and virtual assistants,
* **Call analytics**: Analyze calls from contact centers to extract valuable insights to improve customer experiences and loyalty.
* **Agent assist**: Use AI and generative AI to support and enhance the capabilities of human agents in tasks such as customer service, problem solving, and decision-making.

##### Boosting employee productivity

* **Conversational search**: Improve employee productivity by quickly and easily finding accurate information and summarizing content through a conversational interface.
* **Code generation**: Accelerate application development and improve developer productivity with code suggestions based on the developer's comments and code.
* **Automated report generation**: Automatically generate financial reports, summaries, and projections, saving time and reducing errors.

##### Enhancing creativity and content creation

* **Marketing**: Create engaging marketing content, such as blog posts. social media updates, or email newsletters, saving time and resources.
* **Product development**: AI can generate multiple design prototypes based on certain inputs and constraints, speeding up the ideation phase. AI can optimize existing designs based on user feedback and specified constraints.
* **Media and entertainment**: You can use generative AI to create scripts and dialogs. You can also use it to complete stories for films, TV shows, and games.
* **News generation**: AI can generate news articles or summaries based on raw data or events.

##### Accelerating process optimization

* **Document processing**: Improve business operations by automatically extracting and summarizing data from documents and insights through generative AI-powered question and answering.
* **Fraud detection**: Generative AI models can learn the patterns of fraudulent transactions and create synthetic fraud patterns to train more robust fraud detection systems.
* **Supply chain optimization**: Improve logistics and reduce costs by evaluating and optimizing different supply chain scenarios.

___

New use cases will arise as LLMs evolve and gain a broader audience. Generative AI will play a transformational role in every industry.

### Fundamentals of Prompt Engineering

Prompt engineering is an emerging field that focuses on developing, designing, and optimizing prompts to enhance the output of LLMs for your needs. It gives you a way to guide the model's behavior to the outcomes that you want to achieve.

#### Prompt engineering overview

Prompt engineering is different from fine-tuning.

* In fine-tuning, the weights or parameters are adjusted using training data with the goal of optimizing a cost function. Fine-tuning can be an expensive process, both in terms of computation time and actual cost.
* Prompt engineering, however, attempts to guide the trained FM, an LLM, or a text-to-image model, to give more relevant and accurate answers.

Prompt engineering is the fastest way to harness the power of large language models. By interacting with an LLM through a series of questions, statements, or instructions, you can adjust LLM output behavior based on the specific context of the output that you want to achieve.

Effective prompt techniques can help your business accomplish the following benefits:

* Boost a model's abilities and improve safety.
* Augment the model with domain knowledge and external tools without changing model parameters or fine-tuning.
* Interact with language models to grasp their full capabilities.
* Achieve better quality outputs through better quality inputs.

#### Elements of a prompt

A prompt's form depends on the task that you are giving to a model. As you explore prompt engineering examples, you will review prompts containing some or all of the following elements:

* **Instructions**: This is a task for the large language model to do. It provides a task description or instruction for how the model should perform.
* **Context**: This is external information to guide the model.
* **Input data**: This is the input for which you want a response.
* **Output indicator**: This is the output type or format.

Review the following prompt example.

##### Example prompt

* Prompt

   ```prompt
    Write a summary of a service review using two sentences.

    Store: Online, Service: Shipping.

    Review: Amazon Prime Student is a great option for students looking to save money. Not paying for shipping is the biggest save in my opinion. As a working mom of three who is also a student, it saves me tons of time with free 2-day shipping, and I get things I need quickly and sometimes as early as the next day, while enjoying all the free streaming services, and books that a regular prime membership has to offer for half the price. Amazon Prime Student is only available for college students, and it offers so many things to help make college life easier. This is why Amazon Prime is the no-brainer that I use to order my school supplies, my clothes, and even to watch movies in between classes. I think Amazon Prime Student is a great investment for all college students.

    Summary:
    ```

* Output

    ```output
    Amazon Prime Student is a fantastic option for college students, offering free 2-day shipping, streaming services, books, and other benefits for half the price of a regular Prime membership. It saves time and money, making college life easier.
    ```

___

You can break up the prompt into the following elements:

* **Instruction**: Write a summary of a service review...
* **Context**: Store: Online, Service: Shipping
* **Input data**: Review: Amazon Prime Student is a great option for students looking to save money. Not paying for shipping is the biggest save in my opinion. As a working mom of three who is also a student, it saves me tons of time with free 2-day shipping, and I get things I need quickly and sometimes as early as the next day, while enjoying all the free streaming services, and books that a regular prime membership has to offer for half the price. Amazon Prime Student is only available for college students, and it offers so many things to help make college life easier. This is why Amazon Prime is the no-brainer that I use to order my school supplies, my clothes, and even to watch movies in between classes. I think Amazon Prime Student is a great investment for all college students.
* **Output indicator**: ...using two sentences.

#### Best practices for designing effective prompts

* Be clear and concise
* Include context if needed
* Provide an example response
* Break up complex tasks

##### Be clear and concise

Prompts should be straightforward and avoid ambiguity. Clear prompts lead to more coherent responses. Craft prompts with natural, flowing language and coherent sentence structure. Avoid isolated keywords and phrases.

Bad prompt

```prompt
Compute the sum total of the subsequent sequence of numerals: 4, 8, 12, 16.
```

Good prompt

```prompt
What is the sum of these numbers: 4, 8, 12, 16?
```

##### Include context if needed

Provide any additional context that would help the model respond accurately. For example, if you ask a model to analyze a business, include information about the type of business. What does the company do? This type of detail in the input provides more relevant output. The context that you provide can be common across multiple inputs or specific to each input.

Bad prompt

```prompt
Summarize this article: [insert article text]
```

Good prompt

```prompt
Provide a summary of this article to be used in a blog post: [insert article text]
```

##### Use directives for the appropriate response type

If you want a particular output form, such as a summary, question, or poem, specify the response type directly. You can also limit responses by length, format, included information, excluded information, and more.

Bad prompt

```prompt
What is the capital?
```

Good prompt

```prompt
What is the capital of New York? Provide the answer in a full sentence.
```

##### Consider the output in the prompt

Mention the requested output at the end of the prompt to keep the model focused on appropriate content.

Bad prompt

```prompt
Calculate the area of a circle.
```

Good prompt

```prompt
Calculate the area of a circle with a radius of 3 inches (7.5 cm). Round your answer to the nearest integer.
```

##### Start prompts with an interrogation

Phrase your input as a question, beginning with words such as who, what, where, when, why, and how.

Bad prompt

```prompt
Summarize this event.
```

Good prompt

```prompt
Why did this event happen? Explain in three sentences.
```

##### Provide an example response

Use the expected output format as an example response in the prompt. Clarify that the model is to follow the format of the examples in the prompt.

Bad prompt

```prompt
Determine the sentiment of this social media post:

[insert social media post]
```

Good prompt

```prompt
Determine the sentiment of the following social media post using these examples:

post: "great pen" => Positive
post: "I hate when my phone battery dies" => Negative
post: "[insert social media post]" =>

Answer only as in the examples provided and provide no additional information.
```

##### Break up complex tasks

Foundation models can get confused when asked to perform complex tasks. Break up complex tasks by using the following techniques:

1. Divide the task into several subtasks. If you cannot get reliable results, try splitting the task into multiple prompts. 
2. Ask the model if it understood your instruction. Provide clarification based on the model's response.
3. If you don’t know how to break the task into subtasks, ask the model to think step by step.  This method might not work for all models, but you can try to rephrase the instructions in a way that makes sense for the task. For example, you might request that the model divides the task into subtasks, approaches the problem systematically, or reasons through the problem one step at a time.

Bad prompt

```prompt
Q: A juggler can juggle 16 balls. Half of the balls are golf balls and half of the golf balls are blue. How many blue golf balls are there?
A: The answer is
```

Good prompt

```prompt
Q: A juggler can juggle 16 balls. Half of the balls are golf balls and half of the golf balls are blue. How many blue golf balls are there?
A: Let's think step by step.
```

##### Experiment and be creative

Try different prompts to optimize the model's responses. Determine which prompts achieve effective results and which prompts achieve inaccurate results. Adjust your prompts accordingly. Novel and thought-provoking prompts can lead to innovative outcomes.

___

#### Evaluate the model's responses

It's important to review the model's responses to ensure that the prompts are eliciting the appropriate quality, type, and range of responses. Make changes to the prompts as needed. You can even ask one copy of the model to improve or check output from another copy of the model.

With experimentation, you will gain intuition for crafting and optimizing prompts to best suit your needs and models. Prompt engineering is an iterative skill that improves with practice.

### Basic Prompt Techniques

When crafting and manipulating prompts, there are certain techniques that you can use to achieve the response you want from AI models. In this lesson, you will learn how using various prompt engineering techniques can help you use generative AI applications most effectively for your unique business objectives.

#### Zero-shot prompting

Zero-shot prompting is a prompting technique where a user presents a task to an LLM without giving the model further examples. The user expects the model to perform the task without a prior understanding, or *shot*, of the task. Modern LLMs demonstrate remarkable zero-shot performance.

##### Tips for using a zero-shot prompting technique include the following

* The larger the LLM, the more likely the zero-shot prompt will yield effective results.
* Instruction tuning can improve zero-shot learning. You can adopt reinforcement learning from human feedback (RLHF) to scale instruction tuning, to align modern LLMs to better fit human preferences.

Review the following zero-shot example.

##### Zero-shot prompt example

Consider the following zero-shot prompt.

* **Prompt**

```prompt
Tell me the sentiment of the following social media post and categorize it as positive, negative, or neutral:

Don't miss the electric vehicle revolution! AnyCompany is ditching muscle cars for EVs, creating a huge opportunity for investors.
```

* **Output**

```output
Positive
```

**Note**: This prompt did not provide any examples to the model. However, the model was still effective in deciphering the task.

#### Few-shot prompting

Few-shot prompting is a prompting technique where you give the model contextual information about the requested tasks. In this technique, you provide examples of both the task and the output you want. Providing this context, or a *few shots*, in the prompt conditions the model to follow the task guidance closely.

##### Tips for using a few-shot prompting technique include the following

* The labels in a few-shot prompt do not have to be correct to improve model performance. Usually, applying random labels outperforms using no labels at all. However, the label space and distribution of the input text specified by the demonstrations are important. The use of the term *label* in this context refers to the output of the prompt examples. The sentiment expressed by a statement in a prompt example is an example of a label.
* If you have access to a large set of examples, use techniques to obey the token limits of your model and dynamically populate prompt templates. You can use an example selector that is based on semantic similarity to help.

Review the following few-shot prompt example.

##### Few-shot prompts example

Consider the following few-shot prompts.

* **Prompt**

```prompt
Tell me the sentiment of the following headline and categorize it as either positive, negative, or neutral. Here are some examples:

Research firm fends off allegations of impropriety over new technology.
Answer: Negative

Offshore windfarms continue to thrive as vocal minority in opposition dwindles.
Answer: Positive

Manufacturing plant is the latest target in investigation by state officials.
Answer:
```

* **Output**

```output
Negative
```

**Note**: The Amazon Titan Text model was used in this example. For other models, refer to the Model-Specific Prompt Techniques section.

#### Chain-of-thought prompting

Chain-of-thought (CoT) prompting breaks down complex reasoning tasks through intermediary reasoning steps. You can use both zero-shot and few-shot prompting techniques with CoT prompts.

Chain-of-thought prompts are specific to a problem type. You can use the phrase "Think step by step" to invoke CoT reasoning from your machine learning model.

**Tip**: Use CoT prompting when the task involves several steps or requires a series of reasoning.

Review the following CoT prompt examples that use Amazon Titan, a large language model.

##### CoT zero-shot prompt example

* **Prompt**

```prompt
Which vehicle requires a larger down payment based on the following information?

The total cost of vehicle A is $40,000, and it requires a 30 percent down payment.

The total cost of vehicle B is $50,000, and it requires a 20 percent down payment.
(Think step by step)
```

* **Output**

```output
The down payment for vehicle
A is 30 percent of $40,000, which is
(30/100) * 40,000 = $12,000.

The down payment for vehicle
B is 20 percent of $50,000, which is
(20/100) * 50,000 = $10,000.

We can see that vehicle A needs a larger down payment than vehicle B.
```

**Note**: This prompt did not provide any examples to the model. However, the model was still effective in deciphering the task.

CoT prompting can become more powerful if you combine it with few-shot prompting. Now, consider the following prompt that uses both methods.

##### CoT few-shot prompt example

* **Prompt**

```prompt
In a given week, the viewers for a TV channel are as follows:
Monday: 6,500 viewers
Tuesday: 6,400 viewers
Wednesday: 6,300 viewers

Question: How many viewers can we expect on Friday?
Answer: Based on the numbers given and without any more information, there is a daily decrease of 100 viewers. If we assume this trend will continue during the following days, we can expect 6,200 viewers on the next day that would be Thursday, and therefore 6,100 viewers on the next day that would be Friday.

Question: How many viewers can we expect on Saturday? (Think step by step)
Answer:
```

* **Output**

```output
Based on the given information, we can expect 6,100 viewers on Friday. If we assume the trend will continue, we can expect 6,000 viewers on Saturday.
```

This prompt provided both few-shot context in the form of a question-and-answer example and CoT prompting by asking the model to "Think step by step."

### Demonstration: Working with Basic Text Prompts

We're gonna use a Bedrock playground and the Titan Text G1 - Express model for this demonstration.

1. We put into the prompt quite a large slab of text, which is essentially a description of Bedrock's features.
2. We've asked our model, "What are some of the advantages of using Amazon Bedrock?"
3. It's quite chatty in its response.
4. Let's reload the playground and ask another question with the same prompt "What are the top three reasons that a developer would choose to work with Amazon Bedrock?"
5. We've gotten a much more concise response now.
6. Let's ask, "What advantage is most important for a developer?"
7. We've gotten: "Bedrock iss an important feature for a developer because it allows you to easily experiment and play around and try out these different models".

### Knowledge Check

#### Which type of foundation model summarizes lengthy articles into a short paragraph?

* Text-to-text

Wrong answers:

* Diffusion
* Text-to image
* Image-to-text

##### Explanation

Text-to-text models are used for tasks like translating text between two languages or summarizing lengthy paragraphs.

The other responses are incorrect because of the following:

* Diffusion models are used for image generation and other computer vision tasks. For example, they can introduce noise to an input image and then learn how to reverse that process. By doing this, they are capable of producing new images.
* Text-to-image models use a language model to interpret the text input and then apply a generative image model to create an image output.
* Image-to-text models output text from an image.

#### Which prompting technique does not include examples?

* Zero-shot

Wrong answers:

* Few-shot
* Chain-of-thought
* Instruction fine-tuning

##### Explanation

Zero-shot prompts do not include examples when presented to a foundation model.

The other responses are incorrect because of the following:

* Few-shot prompts include with examples when presented to a foundation model.  
* Chain-of-thought (CoT) prompts are written to focus the model to break down a complex task into step-by-step reasoning. CoT might be used in combination with zero-shot or few-shot prompts.
* Instruction fine-tuning essentially retrains the model to use specific instructions that help the model generalize for specific tasks.

#### Which type of learning pattern is used to pre-train foundation models?

* Self-supervised

Wrong answers:

* Supervised
* Semi-supervised
* Unsupervised

##### Explanation

Self-supervised learning is the dominant approach used to pre-train large foundation models like GPT-3, BERT, and others. In self-supervised learning, the model learns to predict certain aspects of the input data from other aspects of the same data.

The other responses are incorrect because of the following:

* Supervised learning requires labeled data, where the inputs are mapped to known outputs or targets. Pre-training foundation models on vast amounts of labeled data is generally impractical and expensive.
* Semi-supervised learning combines a small amount of labeled data with a large amount of unlabeled data during training. Although semi-supervised learning can be useful in certain scenarios, it is not the primary approach used for pre-training large foundation models.
* Unsupervised learning involves finding patterns and structures in data without any labeled targets or outputs. Unsupervised learning is not well suited for pre-training foundation models that require learning rich representations of data like text or images. Self-supervised learning, which involves predicting aspects of the input data itself, is more effective for this purpose.

### Summary

* Foundation models use deep neural networks to emulate human brain functionality to handle complex tasks.
* Prompt engineering is an emerging field that focuses on developing, designing, and optimizing prompts to enhance the output of large language models.
* When crafting and manipulating prompts, there are certain techniques that you can use to achieve the response you want from AI models.

#### Basic prompt engineering techniques

When working with foundation models, the recommended practice is to start with prompt engineering because it's the lowest effort way to get started. Foundation models are highly sensitive to the prompt that you provide. So even a slight change in the way that you structure the prompt could elicit a very different response. So try different types and styles of prompts and see which one gives you the best responses from the model.

This topic introduced three basic prompt engineering techniques:

* **Zero-shot prompting** is a prompting technique where a user presents a task to an LLM without giving the model further examples.
* **Few-shot prompting** is a prompting technique where you give the model contextual information about the requested tasks.
* **Chain-of-thought (CoT)** prompting breaks down complex reasoning tasks through intermediary reasoning steps.

## Advanced Prompt Techniques
