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

* **Self-consistency** - prompts the model to sample a variety of reasoning paths. Then, the model aggregates the final answer based on multiple data points from the various paths.
* **Tree of thoughts** - samples thoughts sequentially, but ToT prompting follows a tree-branching technique.
* **Retrieval Augmented Generation (RAG)** - retrieves a small set of relevant documents from a large corpus and uses that to provide context to answer the question.
* **Automatic Reasoning and Tool-use (ART)** - deconstructs complex tasks by having the model select demonstrations of multiple, or few-shot, examples from the task library.
* **ReAct prompting** - generate both reasoning traces and task-specific actions that are based on external tools, such as Wikipedia pages or SQL databases.

### Self-consistency

Self-consistency is a prompting technique that is similar to chain-of-thought prompting. However, instead of taking the obvious step-by-step, or greedy path, self-consistency prompts the model to sample a variety of reasoning paths. Then, the model aggregates the final answer based on multiple data points from the various paths. According to the article "Self-Consistency Improves Chain of Thought Reasoning in Language Models" by Xuezhi Wang and others, self-consistency improves CoT reasoning prompting when used in a range of common arithmetic and common-sense reasoning benchmarks.

**Consider the following prompts using the Jurassic-2 (J2) model. The first prompt example uses a single CoT prompt, and the second example uses self-consistency.**

#### Example with Jurassic-2 (J2) model. The prompt example uses a single CoT prompt resulting in an incorrect output

* Prompt

```prompt
When I was 10, my sister was half my age.
Now I’m 40.
How old is my sister?
```

* Output (J2)

```output
When you were 10, your sister was half your age, which means she was 5 years old (half of 10).

Now, you are 40, which means 20 years have passed since you were 10. Therefore, your sister has also aged by 20 years, and she is now 20 + 5 = 25 years old.

So, your sister is 25 years old now.
```

#### Example  with Jurassic-2 (J2) model. The example uses self-consistency resulting in a correct output

* Prompt

```prompt
Q. Terry had 12 apples. He gave half to Jane. John gave Terry three more apples. How many apples does Terry have?
A. Terry originally had 12 apples. He gave half to Jane, which means he gave 6 away. So now, Terry has 12 − 6 = 6 apples. John gave Terry three more apples, which means 3 + 6, so Terry now has 9 apples.

Q. When I was 10, my sister was half my age. Now I’m 40 years old. How old is my sister?
A.
```

* Output (J2)

```output
When I was 10, my sister was 10/2 = 5 years old.

Now, I’m 40, so my sister is 40 − 5 = 35 years old.
```

Using the self-consistency technique, the model can separate the appropriate data points and then aggregate them into the correct answer.

### Tree of thoughts (ToT)

![Tree of thoughts (ToT) diagram](./images/W03Img020TreeOfThoughtsPrompting.png)

Tree of thoughts (ToT) is another technique that builds on the CoT prompting technique. CoT prompting samples thoughts sequentially, but ToT prompting follows a tree-branching technique. With the ToT technique, the LLM can learn in a nuanced way, considering multiple paths instead of one sequential path.

ToT prompting is an especially effective method for tasks that involve important initial decisions, strategies for the future, and exploration of multiple solutions. Most LLMs make decisions by following a standard left-to-right token-level inference, but with ToT, LLMs can self-evaluate choices.

According to the article, "Tree of Thoughts: Deliberate Problem Solving with Large Language Models," by Shunyu Yao and others, ToT significantly improves performance on tasks that require nontrivial planning. Yao and other researchers tested the ToT method on three tasks: creative writing, mini crosswords, and Game of 24, a mathematical learning game. For Game of 24, Generative Pre-trained Transformer 4 (GPT-4) achieved a 4 percent success with CoT prompting. However, the model reached 74 percent success with a ToT prompting method.

![Tree of Thoughts versus Cain of Thoughts](./images/W03Img030TreeOfThoughtsVsChainOfThoughtsPrompting.png)

Consider the following process of using ToT techniques in a Game of 24. This is explained in the research paper, "Tree of Thoughts: Deliberate Problem Solving with Large Language Models."

#### Game of 24

Game of 24 is a mathematical reasoning challenge. The goal is to use four numbers and basic arithmetic operations, including addition (+), subtraction (−), multiplication (*), and division (/), to achieve the number 24.

Consider the following example:

* Input: 4, 9, 10, and 13,
* 10 − 4 = 6 (left: 6, 9, 13)
* 13 - 9 = 4 (left: 4, 6)
* 4 * 6 = 24 (left: 24)

The solution is **(10 − 4) * (13 − 9) = 24**.

1. Step 1: Tree

    ![A tree of decision points during a game of 24.](./images/W03Img040TreeOfThoughtsGame24Tree.png)

    To frame Game of 24 into ToT, it is natural to decompose the thoughts into three steps, each an intermediate equation. At each tree node, you record the remaining, or the left, numbers and prompt the model to propose some possible next steps.

2. Step 2: Propose prompt

    ![Illustration of the tree of decision points during a game of 24.](./images/W03Img042TreeOfThoughtsGame24ProposePrompt.png)

    The same propose prompt is used for all three thought steps; however, it only has one example with four input numbers.

3. Step 3: Value prompt

    ![A value prompt that performs a breadth-first search. The model evaluates each thought candidate using this method.](./images/W03Img044TreeOfThoughtsGame24ValuePrompt.png)

    Perform a breadth-first search (BFS) in ToT, where at each step you keep the best five candidates (b = 5). To perform deliberate BFS in ToT, you prompt the model to evaluate each thought candidate as sure/maybe/impossible with regard to reaching 24.

4. Step 4: Evaluate

    ![A model's evaluation of each decision point. The model eliminates impossible options.](./images/W03Img046TreeOfThoughtsGame24Evaluate.png)

    The aim is to promote correct partial solutions that can be vindicated in a few look-ahead trials. Then, you can eliminate impossible partial solutions based on **"too big/small"** common sense, and keep the rest "maybe." You sample values three times for each thought.

___

### Retrieval Augmented Generation (RAG)

Retrieval Augmented Generation (RAG) is a prompting technique that supplies domain-relevant data as context to produce responses based on that data and the prompt. This technique is similar to fine-tuning. However, rather than having to fine-tune an FM with a small set of labeled examples, RAG retrieves a small set of relevant documents from a large corpus and uses that to provide context to answer the question. **RAG will not change the weights of the foundation model, whereas fine-tuning will change model weights.**

![RAG Simplified Diagram](./images/W03Img050RetrievalAugmentedGenerationSimplified.png)

This approach can be more cost efficient than regular fine-tuning because the RAG approach doesn't incur the cost of fine-tuning a model. RAG also addresses the challenge of frequent data changes because it retrieves updated and relevant information instead of relying on potentially outdated sets of data.

In RAG, the external data can come from multiple data sources, such as a document repository, databases, or APIs. Before using RAG with LLMs you must prepare and keep the knowledge base updated. The following diagram shows the conceptual flow of using RAG with LLMs and highlights the steps that the model uses to learn when the knowledge base has been prepared.

![RAG LLm Flow](./images/W03Img052RetrievalAugmentedGeneration.png)

1. Encode the input text using a language model like GPT-J or Amazon Titan Embeddings.
2. Retrieve relevant examples from a knowledge base that matches the input. These examples are encoded in the same way.
3. Provide the enhanced prompt with question and context to the foundation model to generate a response.
4. The generated response is conditioned on both the input and the retrieved examples, incorporating information from multiple relevant examples into the response.

___

### Automatic Reasoning and Tool-use (ART)

Like the self-consistency and ToT prompt techniques, ART is a prompting technique that builds on the chain-of-thought process. The ART technique, discussed in detail in Bhargavi Paranjape's article "ART: Automatic Multi-Step Reasoning and Tool-Use for Large Language Models," is used specifically for multi-step reasoning tasks.

![Automatic Reasoning and Tool-use (ART) Diagram](./images/W03Img060AutomaticReasoningAndToolUse.png)

This technique essentially deconstructs complex tasks by having the model select demonstrations of multiple, or few-shot, examples from the task library. At the same time that the model is using this few-shot breakdown, it uses predefined external tools such as search query and code generation to carry out the task.

Research shows that ART performs substantially better than few-shot prompting and automatic CoT for unseen tasks and matches the performance of handcrafted CoT prompts on a majority of tasks. ART also makes it more efficient for humans to update information in the task libraries, which can correct errors and ultimately improve performance.

___

### ReAct prompting

With ReAct prompting, an LLM can combine reasoning and action. According to Shunyu Yao's article "ReAct: Synergizing Reasoning and Acting in Language Models," models are often used for reasoning or for acting, but they are not always effectively used for both at the same time.

CoT prompting shows promise for an LLM to reason and generate actions for straightforward tasks, like mathematics. However, the inability to update information or access external contexts with CoT prompting can lead to errors in the output, such as fact hallucination. With a ReAct framework, LLMs can generate both reasoning traces and task-specific actions that are based on external tools, such as Wikipedia pages or SQL databases. This external context leads to more accurate and reliable output.

This diagram highlights the key steps in a ReAct workflow.

![ReAct workflow key steps](./images/W03Img070ReActPrompting.png)

1. **Initial prompt**. The input of a prompt is sent to a foundation model (FM). The prompt could include instructions on tool usage to direct the model on how to proceed.
2. **First interval**. The model observes that it cannot produce the correct response. The model uses reasoning to determine that it needs a tool. This assessment turns into a thought output.
3. **Tool selection**. The model chooses the appropriate tool based on the previous thought.
4. **Tool usage**. The model observes the result of applying the selected tool. It determines that it needs to use another tool because it has not reached the correct response.
5. **Output**. The ReAct cycle continues until the model determines the correct response. The final action is to send back the response output to the requester.

Consider the following prompts. In the first example, a calculator tool is provided to the LLM. In the second example, the prompt adds a SQL database tool to query stock prices.

#### Example prompt and output providing the LLM with a calculator tool

* **Prompt**

```prompt
What is 3.14 raised to the power of 0.12345?
```

* **Output (Anthropic Claude v1 without calculator) – wrong answer**

```output
3.14^(0.12345) = 2.8337112781979765
So the answer is: 2.8337112781979765
```

* **Output (Anthropic Claude v1 with calculator) – right answer**

```output
Entering new AgentExecutor chain...
I will need to use the calculator for this.
Action: Calculator
Action Input: 3.14^0.12345
Observation: Answer: 1.1517174978619817
Thought: I have the final answer.
Final Answer: 1.1517174978619817
> Finished chain.
```

#### Example using a SQL database to query stock prices

**Now you can extend this to use a SQL database tool for querying stock prices (with daily prices for the ABC stock).**

* **Prompt  (LLM, Math, and SQL tool)**

```prompt
Calculate the price ratio for the ABC stock between 2023-01-03 and 2023-01-04.

>> Corresponding prompt template:
Answer the following questions as best you can.

You have access to the following tools:
Calculator: Useful for when you need to answer questions about math.
Stock DB: Useful for when you need to answer questions about stocks and their prices. Use the following format:

Question: the input question you must answer 

Thought: you should always think about what to do

Action: the action to take should be one of [Calculator, Stock DB] Action

Input: the input to the action 

Observation: the result of the action ... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final answer: the final answer to the original input question

Begin!
Question: {input}
Thought:{agent_scratchpad}
```

* **Output (Anthropic Claude v1 with Math and SQL tool)**

```output
> Entering new AgentExecutor chain...
I will need historical stock price data for the two dates
Action: Stock DB Action

Input: Price of the ABC stock on 2023-01-03 and 2023-01-04

> Entering new SQLDatabaseChain chain...Price of the ABC stock on 2023-01-03 and 2023-01-04 SQLQuery:SELECT price FROM stocks WHERE stock_ticker = "ABC" AND date BETWEEN "2023-01-03" AND "2023-01-04"

SQLResult: [(232.0,), (225.0,)]

Answer: The price of the ABC stock on January 03, 2023 was 232.0 and on January 04, 2023 was 225.0.

> Finished chain.

Observation: The price of the ABC stock on January 03, 2023 was 232.0 and on January 04, 2023 was 225.0.

Thought: Now I can compute the price ratio 

Final Answer: The price ratio for the ABC stock between 2023-01-03 and 2023-01-04 is 232.0/225.0 = 1.0311
```

___

The preceding ReAct examples contains lines such as `> Entering new AgentExecutor chain...` and `> Finished chain`. These lines refer to autonomous agents in an application. Agents orchestrate interactions between foundation models, data sources, software applications, and user conversations.

## Model-Specific Prompt Techniques

In the process of developing a model, developers intend for a specific way of using prompts with their respective model. That means that interacting with models from different organizations requires a custom prompting approach. In this section, you learn how to engineer prompts for three models available on Amazon Bedrock. Amazon Bedrock is a managed service that makes foundation models from leading AI startups available through an API.

* **Amazon Titan FMs** – Amazon Titan FMs are pre-trained on large datasets, making them powerful, general-purpose models. Use them as is or customize them with your own data for a particular task without annotating large volumes of data.
* **Anthropic Claude** – Claude is an AI chat-based assistant built by Anthropic, which you can access through chat or API in a developer console. Claude can process conversation, text, summarization, search, creative writing, coding, question answering, and more. Claude is designed to respond conversationally and can modify character, style, and conduct to best suit output needs.
* **AI21 Jurassic-2** – Jurassic-2 is trained specifically to process instructions-only prompts with no examples, or zero-shot prompts. Using only instructions in the prompt can be the most natural way to interact with large language models.

### Parameters that influence models output

* Determinism parameters
* Token count
* Stop sequences
* Number of results
* Penalties

When interacting with LLMs through API or directly, you can configure prompt parameters to get customized results. Generally, you should only adjust one parameter at a time, and results can vary depending on the LLM.

The following parameters can be used to modify the output from the LLMs. Not all parameters are available with all LLMs.

#### Determinism parameters

Choosing lower values for each parameter provides factual results, and choosing higher values provides diverse and creative results. The following parameters control determinism:

* **Temperature** controls randomness. Lower values focus on probable tokens, and higher values add randomness and diversity. Use lower values for factual responses and higher values for creative responses.
* **Top-P** adjusts determinism with nucleus sampling. Lower values give exact answers, and higher values give diverse responses. This value controls the diversity of the model's responses.
* **Top-K** is the number of the highest-probability vocabulary tokens to keep for top-k filtering. Similar to the top-p parameter, top-k defines the cutoff where the model no longer selects the words.

#### Token count

Token count parameters include the following:

* **MinTokens** is the minimum number of tokens to generate for each response.
* **MaxTokenCount** is the maximum number of tokens to generate before stopping.

#### Stop sequences

* **StopSequences** is a list of strings that will cause the model to stop generating.

#### Number of results

* **numResults** is the number of responses to generate for a given prompt.

#### Penalties

These penalties are only available in **Jurassic**. Penalties parameters include the following:

* **FrequencyPenalty** is a penalty applied to tokens that are frequently generated.
* **PresencePenalty** is a penalty applied to tokens that are already present in the prompt.
* **CountPenalty** is a penalty applied to tokens based on their frequency in the generated responses.

___

### Comparing parameters

| Model Provider | Model Name | Parameters |
| -------------- | ---------- | ---------- |
| Amazon | Amazon Titan | temperature<br>topP<br>maxTokenCount<br>stopSequences |
| Anthropic | Claude | temperature<br>top_p<br>top_k<br>max_tokens_to_sample<br>stop_sequences |
| AI21 Labs | Jurassic-2 | temperature<br>topP<br>topKReturn<br>maxTokens<br>stopSequences<br>numResults minTokens<br>frequencyPenalty<br>presencePenalty<br>countPenalty |

___

Parameter interaction can be complex. Remember that results depend on the model and language model version, so be sure to adjust carefully and test thoroughly to achieve the best results.

___

### Prompt guidance for first-party (1P) models

At Amazon, the Amazon Titan family of models are 1P foundation models. When it comes to Amazon Titan, the format of the prompt depends on the intended purpose. The basic elements of a prompt are as follows:

* **Instruction** describes what you are asking of the model, such as summarization or question answering.
* **Context** sets the scene for the model, such as making suggestions like this one: "The following data is a medical text."
* **Input** provides the actual input text for summaries or retrieval tasks.
* **Output indicator** constrains the output from the model. For example, you might want the model to limit the output to a certain number of words or sentences while summarizing a passage.

### Best practices for using Amazon Titan

#### Specify output length

Be specific about the number of sentences, bullet points, and paragraphs that you expect in the output. Specifying a certain number of words does not work as well as specifying the number of sentences, bullet points, and paragraphs.

#### Provide simple, clear, and complete instructions

Amazon Titan generates the best responses when the prompt includes unambiguous expectation of the task.

| Prompt | Output |
| ------ | ------ |
| The most common cause of color blindness is an inherited problem or variation in the functionality of one or more of the three classes of cone cells in the retina, which mediate color vision.<br><br>What is this text about? <br>a) biology<br>b) history <br>c) geology<br> | a) biology |

#### Add context to the prompt for more detailed answers

You will achieve better results if you add context and provide the instruction or output indicator at the end of the prompt. The following is an example.

| Prompt | Output |
| ------ | ------ |
| Use the following requirements to prepare a dessert:<br><br>Serving size: 10<br>Ingredients: no egg<br><br>Generate one recommendation and explain. Include a recipe: | Based on the ingredients and serving size, I recommend baking an eggless chocolate cake. Here is a recipe for eggless chocolate cake:<br>Ingredients:<br>•    1 1/2 cups all-purpose flour<br>•    1 cup granulated sugar<br>•    1/2 cup unsweetened cocoa powder<br>•    1 tsp baking powder<br>•    1 tsp baking soda<br>•    1/2 tsp salt<br>•    1 cup milk<br>•    1/2 cup vegetable oil<br>•    2 tsp vanilla extract<br>•    1 cup boiling water<br><br>Instructions:<br>1)    Preheat the oven to 350°F (175°C). Grease a 9-inch cake pan with butter or oil and dust with flour.<br>2)    In a large bowl, whisk together the flour, sugar, cocoa powder, baking powder, baking soda, and salt until well combined.<br>3)    In a separate bowl, mix together the milk, vegetable oil, and vanilla extract until well combined.<br>4)    Add the boiling water to the milk mixture and stir until combined.<br>5)    Add the wet ingredients to the dry ingredients and whisk until just combined. The batter may be thin and runny.<br>6)    Pour the batter into the prepared cake pan and smooth the top with a spatula.<br>7)    Bake for 30-35 minutes, or until a toothpick inserted into the center of the cake comes out clean.<br>8)    Remove the cake from the oven and let it cool in the pan for 10 minutes.<br>9)    When cooled, remove the cake from the pan and let it cool completely on a wire rack.<br>10)    Serve and enjoy your delicious eggless chocolate cake! |

#### Provide default output when necessary

You can provide default output for the model to present if it is unsure about how to answer. This will prevent the model from returning answers that sound correct, but might not answer the question. The following is an example.

| Prompt | Output |
| Provide a proof of the Riemann hypothesis. If you don't know a proof, respond by saying, "I don't know." | I don't know. |

#### Use separator characters for API calls

For Amazon Titan models, adding \n (new line character) at the end of a prompt will most likely improve the performance of the model. For classification tasks or questions with answer options, you can also separate the answer options by \n for Amazon Titan models. The following example shows how the presence of newline characters between choices and at the end of a prompt help Amazon Titan produce the desired response.

| Prompt | Output |
| --------------- | ------------------------------------------- |
| Terry Whitlock was a physicist, engineer, astronomer, and inventor. Although few details of his life are known, he is regarded as one of the leading scientists of modern times.<br><br>Who was Terry Whitlock?<br><br>Choose one of the options below.<br>a) physicist<br>b) farmer<br>c) sailor | a) physicist |

#### Personalize responses

You can personalize responses by including a role in the prompt. This prompting technique is useful for generating personalized responses. The following is an example.

| Prompt | Output |
| --------------- | ------------------------------------------- |
| Please write an email in the voice of a friend congratulating someone on a new job. | Hey \[Name\],<br><br>I just found out about your new job, and I'm so happy for you! Congratulations! You deserve this opportunity since you worked so hard to get it. I know you'll do great and make a positive impact on your team. I'm here to support you every step of the way. Wishing you all the best in this exciting new chapter of your life!<br><br>Cheers,<br>\[Your Name\] |

#### Generate code

You can generate code samples, such as SQL, Python, HTML, or Java. The following example instructs an Amazon Titan model to write Python code. The code should download a file from an Amazon Simple Storage Service (Amazon S3) bucket to a local disk.

<table>
  <thead>
    <tr>
      <th>Prompt</th>
      <th>Output</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Write a Python function to download an Amazon S3 file to local disk.</td>
      <td>
        <p>The following code can be used to download an S3 file to the local disk:</p>
        <pre><code class="language-python">
import boto3
# Creates a boto3 client object
s3 = boto3.client('s3')
def download_file(bucket_name, object_key, file_path):
    try:
        # Downloads the s3 file to the specified file path
        s3.download_file(bucket_name, object_key, file_path)
    except Exception as e:
        print(e)
# Specifies the values of bucket_name, object_key, and file_path
bucket_name = "samplebucketname"
object_key = "sampleobjectkey"
file_path = "/samplefilepath"
download_file(bucket_name, object_key, file_path)
        </code></pre>
        <p>The given code uses the download_file function to download an S3 file to the local disk. The download_file function takes the bucket name, object key, and file path as input parameters. The bucket name is the name of the S3 bucket where the file is located, the object key is the unique identifier of the file within the bucket, and the file path is the destination path on the local disk where the file will be downloaded. The function uses the download_file method of the S3 client to download the file from the specified bucket and write it to the specified file path.</p>
      </td>
    </tr>
  </tbody>
</table>

___

### Prompt guidance for third-party (3P) models

At Amazon, 3P foundation models are those that are created by other organizations. Claude, a model created by Anthropic, and Jurassic-2, created by AI21 are 3P models.

### Best practices for using Anthropic Claude

#### Add tags in the prompts

Prompts sent to Claude models must contain `\n\nHuman:` and `\n\nAssistant:` as the signals of who is speaking.

Adding human and assistant tags in the prompts guides Anthropic models to generate desired outputs. Also, you can include an optional `\n\nAssistant:` preamble to the response.

Why do we need those tags in API?<br>
Claude has been trained and fine-tuned using reinforcement learning from human feedback (RLHF) methods on `\n\nHuman:` and `\n\nAssistant:` data like this. So you need to use these prompts in the API to get the expected results.

#### Include detailed descriptions

Claude model responses can be chatty, so it is important to give a detailed task description, including rules and exceptions. Explain it as you would to a new employee with no context. Give example inputs and outputs (optional, but improves formatting and accuracy).

Provide the specific input to process and demonstrate the output formatting that you want. You can also deal with Claude’s natural chattiness by asking it to enclose the output in a specific format.

#### Limit the response by prefilling

Claude provides verbose responses. To limit the amount of information in each response, you can prefill the response yourself. This will help Claude respond more quickly because processing input is less complicated than generating output. Review the following example.

| Prompt | Response |
| ------ | -------- |
| Human: Give me five synonyms of the word dust. I mean the verb, not the noun.<br><br>Assistant: Here are the five synonyms of the verb dust: **← prefilled the response** | <br>1. Sprinkle<br>2. Powder<br>3. Scatter<br>4. Sift<br>5. Disperse |

#### Use XML tags

XML tags like `<tag>this</tag>` can be useful for defining structure in your prompt and also in Claude's response. For example, if you want to reference a long piece of text, such as an article, tell Claude that you wrapped it in tags. This makes it obvious where the article starts and ends.

If your prompt includes a reference to a long piece of text, such as an article, put your instruction after the article rather than before it. Consider the following useful tips:

* **Tip 1**: You can ask Claude to use XML tags in the response to make it easy for you to extract key information. You can also end your prompt with the opening XML tag as a good method for skipping the preamble.
* **Tip 2**: You can use tags for few-shot learning.

#### Specify output length

For the best results, specify an approximate number of words, paragraphs, or items in a list. Asking for a specific number of characters is typically less effective.

#### Set clear expectations

Make sure to set the right expectation with Claude, because the model might give you information that is not relevant to the question. If Claude provides responses with hallucinations, or incorrect responses, try to fully explain the task with more clarity. It also helps to anticipate failure in the prompt and explain why a certain response would be a failure.

#### Break up complex tasks

Divide complex tasks into subtasks, break the prompt into multiple prompts, or ask the model if it understands the instructions. As you learned earlier, asking the model to think step by step can also assist with complex tasks.

___

### User prompt examples that follows Anthropic Claude guidelines

The prompt example instructs Claude to classify text.

#### Anthropic Claude

Instructions to classify text.

| User prompt | Output |
| -------------------- | ---------------------------------------- |
| Human: Classify the given product description into given categories. Output the category label in \<output\>\</output\> tags.<br><br>Here is the product description.<br><br>\<text\><br>Safe, made from child-friendly materials with smooth edges. Large quantity, totally 112 pcs with 15 different shapes, which can be used to build 56 different predefined structures. Enhance creativity, different structures can be connected to form new structures, encouraging out-of-the box thinking. Enhance child-parent bonding, parents can play with their children together to foster social skills.<br>\</text\><br><br>Categories are:<br>(1) Toys<br>(2) Beauty and health<br>(3) Electronics<br><br>Assistant: | \<output\>Toys\</output\> |

___

### AI21 Labs Jurassic-2

Jurassic-2 models work well with text summarization, text generation, and question-answering tasks. If you need a response to reflect a certain number of sentences, be sure to include that request in your prompt.

Jurassic-2 models work well with zero-shot and few-shot prompts. Try both methods to decide which technique performs better for your specific scenario.

### Sest practices for using the Jurassic-2 model

#### Specify output length

It is best to specify an approximate number of words, paragraphs, or items of the output. The following is an example.

| Prompt | Output |
| -------------------- | ---------------------------------------- |
| Using the following data, summarize the reasons why customers should have a medicine ball at home in one sentence:<br><br>A weighted medicine ball can be used for upper, lower, and full body exercises. The ball has a lightly textured surface and provides a superior grip. The ball's weight is clearly labeled on both sides of the ball. A medicine ball is ideal for classic workouts, including ball tosses, weighted twists, squats, sit-ups, and more. It is a personal tool to help you develop core strength, balance, and coordination. | A medicine ball is a versatile and effective tool for improving overall strength and conditioning, and can be used for a wide range of exercises to target different muscle groups. |

#### Avoid ambiguity

Include a short but detailed description of the task. AI21 Instruct models are designed to follow instructions. Keep those instructions as clear and concise as possible. Jurassic-2 models perform well for complex tasks, but clear instructions are key for effective results.

You need to provide instruction on what the model should do if it can't find the answer using the documentation you provided. Otherwise, the model will try to generate an answer that is not based on the provided documentation.

| Prompt | Output |
| -------------------- | ---------------------------------------- |
| In a given week, the viewers for a TV channel were as follows:<br>Monday: 6,500 viewers<br>Tuesday: 6,400 viewers<br>Wednesday: 6,300 viewers<br><br>Question: How many viewers can we expect on Friday?<br><br>Answer: Based on the numbers given, and without any more information, there is a daily decrease of 100 viewers. If we assume this trend will continue during the following days, we can expect 6,200 viewers on the next day, that would be Thursday, and therefore 6,100 viewers on the next day, that would be Friday.<br><br>Question: How many viewers can we expect on Saturday?<br><br>Answer: | Friday's viewers = 6,100 viewers<br><br>Saturday's viewers = Friday's viewers − 100 viewers<br>Saturday's viewers = 6,100 − 100<br>Saturday's viewers = 6,000 viewers<br><br>Based on the numbers given, and without any more information, there is a daily decrease of 100 viewers. If we assume this trend will continue during the following days, we can expect 6,200 viewers on the next day, that would be Thursday, and therefore 6,100 viewers on the next day, that would be Friday.<br><br>Friday's viewers = 6,100 viewers<br>Saturday's viewers = Friday's viewers − 100 viewers<br>Saturday's viewers = 6,100 − 100<br>Saturday's viewers = 6,000 viewers<br><br>(We can follow the same logic for the rest of the week.)<br><br>Monday's viewers = 6,500 viewers<br>Tuesday's viewers = Monday's viewers − 100 viewers<br>Tuesday's viewers = 6,500 − 100<br>Tuesday's viewers = 6,400 viewers<br><br>Wednesday's viewers = Tuesday's viewers − 100 viewers<br>Wednesday's viewers = 6,400 − 100<br>Wednesday's viewers = 6,300 viewers<br><br>Thursday's viewers = Wednesday's viewers − 100 viewers<br>Thursday's viewers = 6,300 − 100<br>Thursday's viewers = 6,200 viewers<br><br>Friday's viewers = Thursday's viewers − 100 viewers<br>Friday's viewers = 6,200 − 100<br>Friday's viewers= 6,100 viewers<br><br>Saturday's viewers = Friday's viewers − 100 viewers<br>Saturday's viewers = 6,100 − 100<br>Saturday's viewers = 6,000 viewers<br><br>So, based on the given information, we can expect 6,000 viewers on Saturday. |

#### Include additional context or instructions

You can introduce additional instruction by using the term *Instruction:*. If there is more than one section of the prompt, separate the different parts with a new line. The following is an example.

| Prompt |
| -------------------------------------------------------------------------------- |
| Instruction:<br>Summarize the following text in five sentences as bullet points. Style should be appropriate for a high-school student.<br><br>{example_text}<br><br>The text is about: |

#### Avoid negative formulations

Avoid using phrases that suggest a negative range, such as "No more than five sentences." Instead, identify the target response. The following is an example.

| Prompt | Output |
| -------------------- | ---------------------------------------- |
| Instruction:<br><br>Generate a list of reasons why customers should have a medicine ball at home using the following data in two sentences.<br><br>A weighted medicine ball can be used for upper, lower, and full body exercises. The ball has a lightly textured surface and provides a superior grip. The ball's weight is clearly labeled on both sides of the ball. A medicine ball is ideal for classic workouts, including ball tosses, weighted twists, squats, sit-ups, and more. It is a personal tool to help you develop core strength, balance, and coordination. | A medicine ball is a versatile piece of equipment that can be used for a variety of exercises, including upper, lower, and full body exercises. The ball has a lightly textured surface that provides a good grip, and the weight is clearly labeled on both sides. |

#### Switch the order of instructions when including text

When including a lengthy amount of text in a prompt, try switching the order of the prompt instructions. Provide the text first, then provide the instructions. Finally, provide the output indicator. The following is an example.

| Prompt |
| -------------------------------------------------------------------------------- |
| Based on the following data, complete the instructions provided:<br><br>Data:<br>2023.12.9 Release Notes<br><br>Autopilot features<br>Your vehicle is now equipped with Traffic-Aware Cruise Control, Autosteer (Beta), and Navigate on Autopilot (Beta). Go to Controls > Autopilot to turn on and turn off Autopilot features and customize your preferences. Remember to keep your hands on the wheel and be attentive at all times.<br><br>Stopping mode<br>Stopping mode is now set to Creep by default after performing a factory reset.<br><br>When stopping mode is set to Creep, your car continues to move slowly forward (in drive) or backwards (in reverse) when close to a complete stop. To change the stopping mode, go to Controls > Pedals and Steering > Stopping Mode.<br><br>Refresh your data sharing settings<br>Turn on or turn off data sharing and learn more about how AnyCompany uses anonymous data to improve existing safety and convenience features and create new ones. Go to Controls > Software > Data Sharing. For more information about how we protect your data, go to example.com.<br><br>Support for other languages – AI21 models work well with other languages, such as Spanish.<br><br>Techniques – AI21 models seem to work well with zero-shot and few-shot. Try both to decide which performs better based on your use case scenario.<br><br>Instructions:<br>Create five questions and answers based on the provided data.<br><br>Answer to Instructions: |

___

The following example shows a user prompt that follows AI21 Labs Jurassic-2 guidelines. The prompt example instructs the model to make logical deductions and explain its answer.

### AI21 Labs Jurassic-2 prompt example

#### Instructions to make a logical deduction and explain its answer

| User prompt | Output |
| -------------------- | ---------------------------------------- |
| Question:<br>Which word is the odd one out?<br><br>A. accomplished<br>B. good<br>C. horrible<br>D. outstanding<br><br>Please output the answer and then explain your answer: | The odd one out is<br><br>C. horrible<br><br>The other three words describe positive qualities or achievements, whereas horrible is a negative adjective. |

___

### [Lab: Practicing Prompt Engineering Methods](./labs/W030Lab1PromptEngineeringMethods.md)

Practicing with different prompting techniques such as zero-shot, few-shot, and in-context prompting. The lab provides you access to the chat playground function in Amazon Bedrock.

### Knowledge Check

#### How does the Retrieval Augmented Generation (RAG) technique address the challenge of large language models (LLMs) producing output from outdated data sets?

* A RAG prompt includes updated and relevant information for the LLM to use to generate optimal output.

Wrong answers:

* A RAG prompt fine-tunes the LLM on the latest data before generating output.
* A RAG prompt directs a search of the internet for the latest information to update the language model's knowledge base.
* A RAG prompt instructs the LLM to disregard its pretrained knowledge and rely solely on user-provided information.

##### Explanation

The correct response is A RAG prompt includes updated and relevant information for the LLM to use to generate optimal output. This allows the LLM to generate output based on the most recent and relevant information, rather than relying solely on its training data.

The other responses are incorrect because of the following:

* RAG does not involve fine-tuning the LLM itself. Instead, it retrieves relevant information from an external data source and provides that information to the language model to generate output.
* RAG does not involve searching the internet to update the LLM's knowledge base.
* RAG does not involve instructing the LLM to disregard its pre-trained knowledge. RAG supplements the model's existing knowledge with additional, relevant information.

#### How does the token count parameter impact a large language model's (LLM's) response?

* It sets the number of word fragments to generate for a response.

Wrong answers:

* It determines the language model's confidence level in its response.
* It specifies the maximum number of topics or concepts that the model should cover in its response.
* It adjusts the level of detail or specificity in the model's response.

##### Explanation

A token is a meaningful unit of text, typically a word or subword. Specifying a token count sets the maximum length of an LLM's response.

The other responses are incorrect because of the following:

* The token count parameter is not related to LLM's confidence level.
* The token count parameter does not control the topical coverage or concepts in an LLM response.
* Although a higher token count might allow for a detailed response, the parameter itself does not directly control the level of detail or specificity.

#### A developer is writing a prompt to submit to a large language model (LLM). The developer sets the temperature to 0. What kind of response should the developer expect from the LLM?

* The developer should expect a response that is biased towards a particular viewpoint or ideology.

Wrong answers:

* The developer should expect a creative and diverse set of responses from the LLM.
* The developer should expect a random and unpredictable response from the LLM.
* The developer should expect a factual response from the LLM.

##### Explanation

Setting the temperature to 0 instructs the model to prioritize the most probable or likely outputs based on its training data.

The other responses are incorrect because of the following:

* A temperature of 0 minimizes creativity and diversity in the output. A higher temperature is more likely to produce creative and diverse responses.
* Random and unpredictable responses are more likely to occur with higher temperature settings, which increase the model's willingness to take risks and produce less probable outputs.
* The temperature setting does not directly influence the ideological or viewpoint bias of the model's output.

### Summary

* Advanced prompting techniques help with getting desired results from language models.
* Configuring prompt parameters is a simple way of getting customized results from a language model.
* Different large language models (LLMs) have custom parameters and prompting practices.
* Adversarial prompts are meant to purposefully mislead models and require guardrails to mitigate against them.

#### Advanced prompt engineering techniques

Foundation models present the challenge of handling outdated training data sets. Fine-tuning is an option to address this challenge but has a high cost in terms of time and resources. Another option is to use advanced prompt engineering techniques such as Retrieval Augmented Generation (RAG).

#### Various advanced prompt engineering techniques

* **Self-consistency prompting** instructs the model to sample a variety of reasoning paths. The language model then aggregates the final answer based on multiple data points from the various paths.
* **Tree of thoughts (ToT) prompting** follows a tree-branching technique. With the ToT technique, the LLM can learn in a nuanced way, considering multiple paths instead of one sequential path.
* **RAG prompting** is a prompting technique that supplies domain-relevant data as context to produce responses based on that data and the prompt.
* **Automatic Reasoning and Tool-use (ART) prompting** is a prompting technique that breaks down complex tasks by having the language model select demonstrations of multiple examples from a task library.
* **Reasoning and acting (ReAct) prompting** is a technique that enables language models to generate both reasoning traces and task-specific actions that are based on external tools. External tool usage leads to more accurate responses.

### Additional Resources

* [Claude documentation](https://docs.anthropic.com/claude/docs/introduction-to-prompt-design)
* [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
* [Jurassic-2 documentation](https://docs.ai21.com/docs/prompt-engineering)
* [Self-Consistency Improves Chain of Thought Reasoning in Language Models](https://arxiv.org/abs/2203.11171)
* [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://arxiv.org/abs/2305.10601)
* [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)
* [ART: Automatic Multi-Step Reasoning and Tool-Use for Large Language Models](https://arxiv.org/abs/2303.09014)
* [High-Resolution Image Synthesis with Latent Diffusion Models](https://arxiv.org/abs/2112.10752#)
