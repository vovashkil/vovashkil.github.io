# Week 9: Getting started with LangChain

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to [AI for Developers](./ai-for-developers.md)
* back to repo's main [README.md](../../../README.md)

## LangChain – Framework for LLM Applications

---

LangChain connects large language models (LLMs) with other data sources to improve the accuracy of responses.

---

### LangChain overview

LangChain is a software development framework. It provides the software building blocks to reduce the complexity of building large language model (LLM) applications.

### LLM performance challenges

LLMs are pre-trained on large data collections. They're generalized and can perform multiple tasks

* text generation
* text summarization
* question answering
* sentiment analysis

Challenges:

* Out-of-domain data or remembering conversational context.
* Hallucinations or inaccurate response.

*LangChain* is a tool that reduces the complexity of building RAG, a prompt history store, or a conversational history store functionality from scratch.

Large language models or foundation models in general are stateless. They don't retain state between invocations. So if we want to provide past context to a large language model, for example, that needs to be managed by the application and passed back into the model with the next prompt.

Large language models can also develop reasoning to solve problems, such as multistep problems, where the application needs to find information in steps to solve a problem.

LangChain provides components to make it more efficient to perform common tasks:

* managing context
* maintaining conversational history
* the sequencing of steps when interacting with a large language model
* building language model applications

### LangChain availability

* Python
* TypeScript
* JavaScript

LangChain chains are a sequence of components that work together to process input, generate language, and handle output in various ways.

LangChain provides components for both the retrieval and generation.

---

### Optimizing LLM performance

LLMs are pre-trained on large data collections, and they can perform multiple tasks, such as text generation, text summarization, question answering, and sentiment analysis.

LLMs don't perform well when the task requires dealing with out-of-domain data or remembering conversational context. These types of tasks can lead to hallucinations or inaccurate responses. In addition, a single prompt to an LLM might not always provide the expected result. It might require providing a sequence of requests—known as chaining—to the model to produce accurate results.

As a developer, you must consider how to handle the application workflow and decide which development approach helps reach your application's goals. A manual approach involves writing the code that handles each task that the application must perform. Alternatively, you could use a software framework that provides existing code that could handle the logic for you.

### Simplifying LLM development with LangChain

LLMs don't retain state between invocations. This requires the LLM application to manage any conversation context. For example, to provide a chat experience, an LLM needs the whole conversation as part of the context to produce the desired results. The whole conversation allows the LLM to provide answers based on previous questions from the user.

Additionally, LLMs can develop reasoning to solve complex problems, such as multistep problems where the application needs to find information in steps to solve a problem. LangChain provides components to make it more efficient to perform the common tasks of managing context or the sequencing of steps when interacting with an LLM.

![LangChain components](./images/W09Img010LangChainComponents.png)

LangChain components help with writing the logic of an application.

A Retrieval Augmented Generation (RAG) application can be built with Amazon Bedrock. LangChain has components that help you build a RAG application from scratch. Or, if you prefer, LangChain helps you build LLM applications that follow other advanced prompting techniques. You can also use these components for text summarization, code generation, and interacting with various APIs.

### Supported languages

LangChain provides support for a variety of programming and markup languages. This allows you to work in the language of your choice for various tasks, such as parsing source code and text splitting.

LangChain supports languages such as JavaScript, Python, and TypeScript. For text splitting, it supports HTML, LaTeX, and Markdown. Because LangChain is open source and continually evolving, always refer to the LangChain documentation for updated lists of supported languages and features.

### LangChain limitations and challenges

As with all technology, ensure that you understand what LangChain can do and what is out of scope. Understanding the framework's limitations helps you develop a more robust development approach to building your LLM application.

#### Performance overhead

The modular design and comprehensive features of LangChain might introduce some performance overhead, particularly in applications that require real-time responses.

For example, complex chaining of components could introduce latency in your application. Integrating multiple external tools or services increases processing and wait times. It's best to carefully optimize your implementation and monitor any performance impact.

#### Incomplete documentation

LangChain is an ever-evolving software development framework for building LLM applications. A small team is focused on building and improving its functionality. Often, the team depends on the LangChain community to help improve the documentation for accuracy, clarity, and typographical errors. This means that the LangChain documentation doesn't consistently provide exhaustive details and explanations about how to use available components.

For example, when reading about the *LLMChain* class, you might overlook important parameters like *temperature* or *max_tokens* because their descriptions and default values are not clearly stated in the documentation. You might have to go outside of the documentation to learn how to use several components.

#### Debugging complexity

Troubleshooting issues with multiple LangChain components can be challenging, especially when you consider how those components are orchestrated. Each LangChain component adds a layer of abstraction to your coding.

To benefit from LangChain, you need to use multiple components because you are adding layers of abstraction between your code and the underlying service APIs that your application uses. Orchestrating a complex component sequence introduces many potential points of failure that you must debug to resolve the source of an error. You could be in a situation where you will have to look into the LangChain source code to isolate application errors.

#### LangChain evolution

LangChain is a relatively new framework that's still in development. As such, there is a high frequency of updates and potential changes, some of which might break your application.

---

Being aware of both the functionality of LangChain and its limitations can help guide your decisions around using LangChain in your LLM application projects. Limitations discussed are based on the current version, and capabilities might change in future releases.

It is a good practice to stay updated with the latest LangChain documentation and community resources as you build your LLM application.

By using a framework like LangChain, you can simplify application development. LangChain abstracts away many of the complexities involved in building LLM applications, allowing you to focus on the high-level application logic.

---

## LangChain Architecture

Large language model (LLM) applications provide a unique set of components that differ from traditional software architecture models. Not every LLM application requires each component. The following diagram illustrates available components that you might want to include in your application. The goal of your LLM application determines which components are appropriate to use. 

Take a moment to learn more about the LLM software architecture.

![LLM software architecture](./images/W09Img012LangChainLlmSoftwareArchitecture.png)

### 1. User interface

Similar to traditional applications, LLM applications require a user interface for interaction. However, you should design the user interface to handle natural language inputs and outputs effectively.

### 2. Prompt

LLM applications require careful assembly of user inputs, system prompts, and chat history.
After assembly, the combined information is sent to the LLM to generate an appropriate response.

### 3. Knowledge base

Your LLM app might need to access external knowledge bases. You can implement interfaces to retrieve relevant information that
complements the LLM's inherent knowledge.

### 4.Memory

Unlike stateless traditional applications, LLM apps often require memory components to maintain context across interactions. You might need to implement mechanisms to store and retrieve conversation history.

### 5. Data preparation

When you use a knowledge base, you must first preprocess and format the data before storing it in the knowledge base for LLM consumption.

This step involves cleaning, structuring, and optimizing data to improve the LLM's performance.

### 6. Orchestration

When you want your application to handle complex tasks, you need a mechanism to orchestrate the sub-tasks. The mechanism needs to manage the interactions with an LLM or other application interfaces.

### 7. Plugins

To extend functionality, you can develop plugins that connect your LLM application to external APls. These integrations allow for realtime data access and additional capabilities.

### 8. LLM

Your application might interact with the LLM multiple times before it sends a response back to the user. You also might want your application to interact with multiple LLMs from a single prompt.

---

Developing each application component for your LLM application adds complexity challenges and a long list of tasks to complete. As a developer, you could either build each one yourself, or you could use a software framework to help you. A software development framework that helps with building LLM applications should provide tooling that aligns to this LLM software architecture. 

---

### LangChain architecture

The architecture of the LangChain framework consists of open source software packages. These packages align with the application components of the preceding LLM software architecture diagram. The LangChain architecture can be extended with other packages developed and maintained by the LangChain company.

The extended LangChain architecture is described in the following diagram.

![LangChain architecture diagram](./images/W09Img014LangChainArchitecture.png)

### 1. langchain

The main package offers a wide range of tools and utilities for LLM application development. You will find pre-built chains, agents, output parsers, and other high-level abstractions here.

### 2. langchain-core

This package contains the fundamental building blocks (the base abstractions) for LangChain applications. You use it to create core components and define basic interfaces.

Example components in this package include prompt templates, language models, and document loaders.

### 3. Partner packages

LangChain provides additional packages developed in collaboration with partners. These extend the framework's capabilities and offer specialized functionalities for specific use cases.

The *langchain_aws* package is an example of a partner package.

### 4. langchain-community

This package provides community-contributed integrations and extensions of core LangChain components. You can use it to incorporate additional functionalities and connect to various services.

### 5. langgraph

Lang Graph (the langgraph package) helps you build complex, multistep workflows for your LLM applications. You use it to create sophisticated reasoning and decision-making processes.

### 6. langserve

With LangServe (the langserve package), you can deploy your LangChain applications as API endpoints. It simplifies the process of making your LLM apps accessible over the network.

### 7. LangSmith

LangSmith offers tools for testing, monitoring, and debugging your LLM applications. You use it to ensure the quality and reliability of your LangChain-based projects. LangSmith is a commercial offering from LangChain.

---

LangChain provides additional functionalities to help developers with integrating LangChain components. Specifically, LangChain offers the LangChain Expression Language (LCEL).

---

## LangChain Components
