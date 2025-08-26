# Week 8: Building LLM Apps with RAG

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to [AI for Developers](./ai-for-developers.md)
* back to repo's main [README.md](../../../README.md)

## RAG Overview

RAG is a technique that can significantly boost the accuracy of LLMs by pulling in relevant information from a knowledge base. There are benefits and limitations of RAG.

Amazon Bedrock can be used to build your own RAG-enabled application.

This week activities:

* Define the term Retrieval Augmented Generation (RAG).
* Describe the benefits of using RAG compared to other AI prompting methods.
* Identify how RAG can be used to increase the accuracy of a large language model (LLM) application.
* Define the components of RAG.
* Describe the limitations of RAG-based systems.
* Define Amazon Bedrock Knowledge Bases.
* Describe the process of creating an Amazon Bedrock knowledge base to support Retrieval Augmented Generation (RAG).
* Create RAG through Amazon Bedrock Knowledge Bases.
* Demonstrate how to integrate the Amazon Bedrock Knowledge Bases APIs to enable RAG in large language model (LLM) applications.

## Introduction to RAG

### The need for RAG

Large language models (LLMs) have demonstrated impressive capabilities in performing multiple natural language tasks, such as text generation, summarization, question answering, and sentiment analysis. These models are pre-trained on vast amounts of data, which enables the models to acquire extensive knowledge and language understanding. However, despite their strengths, LLMs face certain limitations and challenges that can lead to inaccurate or suboptimal responses.

One significant challenge is dealing with out-of-domain data or conversational contexts that deviate from the model's training data. Additionally, a single prompt to the LLM might not always provide the expected result, and it might require chaining multiple requests to produce accurate outputs. These limitations can result in hallucinations or inconsistencies in the model's responses. To mitigate these issues and use the full potential of LLMs, researchers and practitioners have explored various techniques, including prompt engineering.

Prompt engineering has been a popular technique for interacting with LLMs and using their capabilities in various applications. However, there are scenarios where basic prompt engineering alone might not be sufficient to achieve accurate and reliable responses. These limitations stem from the inherent nature of LLMs and the challenges associated with relying solely on the model's knowledge acquired during pre-training.

---

The following scenarios show you where basic prompt engineering might not be sufficient.

#### Complex reasoning and analysis

Although LLMs excel at natural language tasks, they might struggle with complex reasoning, analysis, or tasks that require integrating information from multiple sources. Prompt engineering alone cannot compensate for these limitations, because it primarily guides the model's output based on the provided context.

#### Domain-specific expertise

Certain domains, such as medicine, law, or scientific research, require a high level of specialized knowledge and expertise. LLMs trained on general-purpose data might not have the necessary depth of understanding to provide reliable and accurate responses in these domains, even with prompt engineering.

#### Knowledge gaps

LLMs, despite their impressive capabilities, have knowledge gaps due to the limited and potentially biased data that they were trained on. Prompt engineering cannot fill these gaps or provide accurate information for domains or topics that were not adequately represented in the training data.

#### Rapidly changing information

LLMs' knowledge is static, reflecting the state of the world at the time of training. For domains with rapidly evolving information, such as news, finance, or technology, prompt engineering might not be enough to ensure that the model's responses are up to date and accurate.

---

To address the limitations of basic prompt engineering and use the full potential of LLMs, a different approach is needed. The approach must combine the power of LLMs with external knowledge sources and retrieval mechanisms. This approach, known as Retrieval Augmented Generation (RAG), aims to provide more accurate and reliable responses by incorporating relevant information from external sources into the model's generation process.

---

### RAG overview

#### Introduction

Retrieval-Augmented Generation (RAG) is a technique designed to enhance the capabilities of **large language models (LLMs)** by incorporating **external knowledge sources** into the generation process.

By combining retrieval-based and generation-based approaches, RAG allows models to provide **more accurate, relevant, and up-to-date responses**, overcoming the limitations of traditional LLMs that are bound by their training data cutoff.

#### Why RAG Matters

Traditional language models excel at producing fluent, human-like text, but they face several limitations:

* **Training data cutoff** — Information created after the model’s training cutoff date is unavailable.
* **Lack of domain-specific knowledge** — Specialized fields like medicine, law, or finance may not be covered adequately.
* **Inaccuracy with complex queries** — Without access to external references, answers may be incomplete or misleading.

RAG addresses these challenges by augmenting the model’s reasoning with information retrieved from **external data sources** such as research papers, knowledge bases, or enterprise data systems.

---

#### How RAG Works

RAG introduces a two-step process:

#### 1. Retrieval Step

The system first retrieves **relevant documents** or **data** from an external knowledge base.
For example, in a medical virtual assistant scenario, the system might search through:

* Clinical studies
* Research papers
* Diagnostic databases

This ensures that the assistant has domain-specific and up-to-date knowledge at its disposal.

#### 2. Generation Step

Once the relevant information is retrieved, it is passed as context to a pre-trained language model.
The model then generates a response grounded in both its training data and the retrieved knowledge.

This hybrid approach allows the system to provide factually accurate, context-aware, and reliable answers.

---

#### Example: Medical Virtual Assistant

Imagine building a medical virtual assistant using RAG.

* **Scenario:**

A user reports symptoms such as "bad headache and sensitivity to light."

* **Process:**

1. **Retrieval** — The assistant searches its medical database for information related to headaches, migraines, and associated symptoms.
2. **Generation** — Using the retrieved data, the language model generates a response that suggests possible diagnoses (e.g., migraine) and provides treatment recommendations.

* **Outcome:**

The assistant produces accurate and medically informed advice, similar to how a human doctor would consult reference materials.

---

#### Benefits of RAG

RAG enhances language models by introducing **key advantages**:

* **Up-to-date knowledge** — Incorporates the latest research and data beyond the model’s cutoff.
* **Domain adaptability** — Easily applied to fields like medicine, law, customer support, and finance.
* **Improved accuracy** — Reduces hallucinations by grounding responses in verified knowledge sources.
* **Scalability** — Works with large datasets and unstructured information.

---

#### Conclusion

Retrieval-Augmented Generation (RAG) represents a major advancement in AI-driven knowledge systems.

By blending retrieval and generation, RAG enables LLMs to deliver accurate, reliable, and contextually relevant responses. This makes it particularly valuable for mission-critical applications such as medical assistants, enterprise knowledge platforms, and customer service automation.

In short, RAG empowers AI systems to reason like experts who consult references, bridging the gap between static training data and dynamic real-world knowledge.

---

### Benefits and risks of RAG

Although RAG offers promising capabilities for enhancing language models, its implementation and real-world deployment come with both benefits and risks that must be carefully considered.

#### Cost-effective implementation

Chat-based assistant development typically begins by using a foundation model (FM). FMs are API-accessible LLMs trained on a broad spectrum of generalized and unlabeled data.

The computational and financial costs of re-training FMs for organization-specific or domain-specific information are high. RAG is a more cost-effective approach to introducing new data to the LLM. It makes generative Al technology more broadly accessible and usable.

#### Current information

Even if the original training data sources for an LLM are suitable for your needs, it is challenging to maintain relevancy.
Developers can use RAG to provide the latest research, statistics, or news to the generative models. They can use RAG to connect the LLM directly to live social media feeds, news sites, or other frequently-updated information sources. The LLM can then provide the latest information to the users.

#### Enhanced user trust

RAG enables the LLM to present accurate information with source attribution. The output can include citations or references to sources. Users can also look up source documents themselves if they require further clarification or more detail. This can increase trust and confidence in your generative Al solution.

#### More developer control

With RAG, developers can test and improve their chat applications more efficiently. They can control and change the LLM's information sources to adapt to changing requirements or cross-functional usage.

Developers can also restrict sensitive information retrieval to different authorization levels and ensure that the LLM generates appropriate responses. In addition, they can also troubleshoot and make fixes if the LLM references incorrect information sources for specific questions. Organizations can implement generative Al technology more confidently for a broader range of applications.

---

### Risks of RAG

#### Data quality and bias issues

Although RAG integrates current information sources, the quality and biases in those data sources can get propagated into the model's outputs.

If the retrieval knowledge base contains inaccurate, outdated, or biased information, the LLM's responses will reflect those shortcomings. Careful curation and vetting of the retrieval data sources are crucial to maintain high-quality, unbiased outputs.

#### Intellectual property and licensing issues

Depending on the retrieval knowledge base used, there might be intellectual property (IP) or licensing restrictions. These restrictions could limit the use or distribution of the RAG model or its outputs. Careful consideration of IP and licensing terms is necessary to avoid legal complications.

#### Maintenance and updates

For RAG, maintaining consistent performance can be challenging. It's because that the underlying data sources can evolve over time. As a result, regular updates to the source data used in the RAG process might be necessary to ensure continued accuracy and relevance. This introduces additional operational overhead and costs.

#### Potential for inconsistencies and hallucinations

Despite retrieval augmentation, RAG-based LLM applications can still generate inconsistent or hallucinated outputs. This is especially true when dealing with topics not well represented in the retrieval knowledge base. It can also happen when making inferences beyond the retrieved information. This can undermine user trust and the reliability of the system.

#### Scalability and performance challenges

Integrating large-scale retrieval components with language models can introduce significant computational overhead and latency challenges. This is particularly true when dealing with frequently updated or high-volume data sources. Ensuring acceptable performance and responsiveness for production deployments might require substantial engineering efforts and resources.

#### Security and privacy concerns

Integrating external data sources into language models raises potential security and privacy concerns. Developers must implement robust access controls, data filtering, and monitoring mechanisms. This is necessary to prevent leakage of sensitive information or unauthorized access to proprietary data sources.

---

### Comparing RAG with model fine-tuning methods

Although RAG offers advantages over basic prompt engineering alone, it still has limitations compared to more robust AI customization methods, such as fine-tuning or training foundation models from scratch. Explore the following information to learn more.

#### Dependence on retrieval knowledge base

One limitation of the RAG approach is its dependence on the efficiency of the retrieval process, particularly when dealing with large knowledge bases. RAG relies on retrieving relevant information from an external knowledge base, performing data preparation, prompt augmentation, and potentially prompt engineering before generating the final output with LLMs.

When the knowledge base is large, the retrieval process can become time consuming, potentially impacting the overall performance of the system. Finding and retrieving all relevant data from a vast knowledge base can lead to longer response times.

In contrast, model fine-tuning techniques permit the incorporation of the knowledge base data directly into the model during the fine-tuning process. This approach eliminates the need for a separate retrieval step during inference, because the model already contains the relevant knowledge. As a result, fine-tuned models can potentially offer faster response times and better performance, particularly when dealing with large knowledge bases, because the retrieval overhead is eliminated.

#### Domain adaption

Fine-tuning and training foundation models from scratch can provide better adaptation to specific domains or tasks. This is because the models are directly optimized for the target domain or task.

In contrast, RAG systems rely on a more general language model and a separate information retrieval component. Although RAG systems can use external knowledge sources, they might not adapt to specialized domains or tasks as well as fine-tuned or task-specific models.

#### Static and adaptive knowledge

In RAG systems, the language model itself is pre-trained on a general corpus, and its knowledge is essentially static. The external knowledge base serves as a separate resource for retrieving relevant information during inference. Although this approach allows the RAG system to use existing knowledge bases, it also means that the model's knowledge is limited to what it was pre-trained on. This is because RAG doesn't change the parameters of the language model itself. If the knowledge base lacks coverage, RAG's performance suffers.

However, fine-tuning allows models learn knowledge directly from task-specific training data and diverse examples. Fine-tuning and training foundation models from scratch adapt the model's knowledge by modifying its parameters. This enables the models to effectively learn and embed relevant knowledge within themselves.

#### Cost consideration

From a cost perspective, the RAG approach can be less expensive compared to fine-tuning or training models from scratch in certain scenarios. RAG systems rely on an external knowledge base to retrieve relevant information. If a suitable, well-curated knowledge base already exists for a particular domain or task, RAG can use this existing resource. In such cases, RAG can be a more cost-effective solution because it avoids the computational expenses associated with fine-tuning or training large language models from scratch.

Fine-tuning and training from scratch involve intensive computational processes that can be time consuming and resource intensive, especially for large models. These approaches might incur higher costs due to the required computational power and time.

By using an existing knowledge base, RAG systems can bypass these high computational costs while still benefiting from the knowledge contained within the base. However, it's important to note that RAG systems still incur costs related to maintaining and updating the knowledge base, in addition to the retrieval process itself.

---

Despite these limitations, RAG can be useful in scenarios where a large collection of relevant information is available and the retrieval mechanism is effective. However, for more demanding tasks, fine-tuning (or even training foundation models from scratch) might be more appropriate. This approach is suitable when cost is not a concern. Additionally, fine-tuning or training models from scratch is recommended when high accuracy is very important.

It's important to note that these methods are not mutually exclusive. Hybrid approaches combining RAG with fine-tuning or other techniques can also be explored to use the strengths of different methods.

--

### How RAG Works

#### RAG components

1. retrieval

    This component is responsible for retrieving relevant information from an external knowledge source or data sources. The system takes your question or topic and searches the knowledge base. It finds the most relevant documents, passages, or facts to help answer your query. This process uses active searching to locate the best information for you.

2. augmentation

    The augmentation step combines the retrieved knowledge with the original user prompt to create an augmented context or input. This augmented input goes to the foundation model.

3. generation

    This is the final component where the foundation model takes the augmented context as input and generates a final answer or output text sequence. The model uses the augmented context containing both the original input and retrieved knowledge to produce a fluent and knowledge-grounded output.

---

In the RAG framework, external knowledge sources refer to any knowledge base or collection of information that is external to the pre-trained language model itself. Although these sources are typically large public repositories like Wikipedia, they can also be proprietary or private data silos owned by the company or organization. The key aspect is that this knowledge is not encoded within the model's parameters during pre-training. Instead, it serves as an external, potentially constantly updating knowledge source that RAG can query and retrieve relevant information from during the retrieval phase.

---

### Types of retrieval

In a RAG system, the retrieval component plays a crucial role in gathering relevant information from external knowledge sources. There are several types of retrieval techniques that can be employed, each with its own strengths and applications.

#### Rule-based

This involves extracting unstructured information based on predefined rules or patterns, such as keyword searches.

#### Transactional

Another option is retrieval from structured data sources, such as querying and retrieving information from knowledge graphs, tabular data, or other structured formats.

#### Semantic search

RAG primarily focuses on semantic search for retrieval. This involves retrieving relevant information based on the semantic meaning and context of the query, often from unstructured text data like documents or webpages.

Semantic search is a technique used in the retrieval component of RAG. Semantic search uses text embeddings to identify and fetch relevant documents or passages from the external knowledge sources. Unlike traditional keyword-based search methods, semantic search aims to understand the underlying meaning and semantic relationships within text.

---

### RAG workflow overview

So how does RAG work? RAG involves two workflows: one is data ingestion and knowledge base creation, and the other one is prompt augmentation and text generation. The following image provides a high-level overview of these two workflows.

![Illustration of two RAG workflows](./images/W08Img010TwoRagWorkflows.png)

The data ingestion and knowledge base creation workflow includes loading data, performing chunking, creating vector embeddings, storing vectors in the vector store, and finally creating an index in the vector store. The prompt augmentation and text generation workflow includes the user query, creating vector embeddings, running a similarity search, retrieving similar context, augmenting prompts, and generating responses.

---

### Data ingestion and knowledge base creation

Before you can actually ask questions about your data, the data must be optimized for a RAG use case and be stored in a knowledge base. The following diagram provides an overview of the data ingestion and knowledge base creation workflow.

![Data ingestion and knowledge base creation workflow](./images/W08Img012RagDataIngestion.png)

1. **Load data**

    The data ingestion workflow starts with loading the data from the external data sources, such as files (for example, CSV, JSON, or text files), databases, APIs, or web scraping.

2. **Perform chunking**

    You then take this data and go through the process called chunking. Chunking is the process of dividing large text data into smaller, more manageable pieces (chunks).

3. **Create vector embeddings**

    These chunks are then passed into an embedding model, such as Amazon Titan Text Embeddings, to create vector embeddings.

4. **Store vectors in a vector store**

    The vectors are then ultimately stored in a purpose-built vector database (vector store).

5. **Create an index in a vector store**

    The vector database (vector store) is optimized for indexing and retrieval of embeddings. It can maintain the relationship and semantic meaning that you get through an embedding model.

---

#### More on chunking

When dealing with large documents, it is common to break them down into smaller segments for efficient processing. This chunking can be done in different ways, such as fixed-sized chunks (for example, 512 tokens). Or it can be done with variable-sized chunks based on semantic boundaries (for example, paragraphs or sections).

Chunking is necessary because most vector embedding models have a maximum input length, and processing large texts in one go can be computationally expensive. Chunking is also useful for optimizing for things like relevancy.

For example, consider a large document containing information about a city, such as its history, landmarks, culture, cuisine, and transportation. If this document is treated as a single unit and embedded without chunking, the resulting vector embedding would represent a generalized meaning of the entire document. This makes it difficult to distinguish and retrieve specific information related to a particular aspect of the city.

However, if the document is chunked into smaller segments, each chunk can contain information about a specific aspect. For example, one chunk is for the city's history, another chunk is for its landmarks, and another chuck is for its cuisine. The vector embeddings for these individual chunks would better capture and represent the unique details and contexts of each aspect.

During a search or query related to a particular aspect, such as *famous landmarks in the city*, the vector store can retrieve the most relevant chunks. This is done by matching the query embedding with the embeddings of the chunks specifically focused on landmarks. It will not retrieve the entire document, which might contain irrelevant or unrelated information about other aspects like history or cuisine.

This targeted retrieval of relevant chunks optimizes the relevancy of the search results, and the user is presented with the most pertinent information directly related to their query.

---

#### More on embeddings

Remember the knowledge base concept that you just learned about? The knowledge itself (such as documents) must be stored as numerical vectors like [1.7, 0.6, 7.9,...]. There is a process to create those numerical representations from the text and save them for future retrieval in the RAG process. This process is called embedding. Let's first review what embedding is about.

Embeddings are a way of representing human text data (words, sentences, documents) as numerical vectors, typically high-dimensional vectors. These vector representations capture the semantic meaning and relationships between words or pieces of text. The idea is to encode the text into a dense vector space, where similar words or semantically related texts are mapped to nearby points in this vector space.

![Illustration of how embedding works. Human text inputs run through an embedding model](./images/W08Img014RagVectorEmbeddings.png)

Embedding models (models specifically designed to convert text into numerical vectors) are trained on large amounts of text data. This enables them to learn and encode various features and nuances present in the text. There are various embedding models available, each with different architectures and capabilities.

For example, Amazon Titan Text Embeddings can generate high-dimensional (1,536) vector representations that capture the semantic meaning of text inputs across over 25 languages. The Amazon Titan Text Embeddings v2 model (amazon.titan-embed-text-v2:0) can take in up to 8,192 tokens and outputs a vector of 1,024 dimensions. The model also works in more than 100 different languages. The model is optimized for text retrieval tasks, but can also perform additional tasks, such as semantic similarity and clustering. Amazon Titan Text Embeddings v2 also supports long documents. However, for retrieval tasks, it is recommended to segment documents into logical segments, such as paragraphs or sections.

These models can capture intricate relationships, such as synonymy, analogies, and contextual similarities. By learning from the distributional properties of words in the training data, embedding models can generalize and represent even unseen or rare words in a meaningful way.

---

Embedding models focus on representing text elements as fixed-length vectors that capture semantic relationships. This is different than the LLMs that you use to chat. LLMs are designed for generating human-like text and understanding natural language in an open-ended manner. Embedding models are often used as input features for other machine learning models. But LLMs can be used for a variety of language generation and understanding tasks directly.

---

#### Types of embeddings

Embedding models can operate at different levels, providing vector representations for individual words, sentences, or entire documents.

#### 1. Word embeddings

Word embeddings represent individual words as vectors, capturing their semantic and contextual relationships within the text. These embeddings capture the semantic and syntactic relationships between words, so similar words have similar vector representations.

For example, consider the words **king** and **queen**. In a word embedding space, these words would have similar vector representations because they are semantically related (both referring to monarchs).

#### 2. Sentence embeddings

Sentence embeddings represent entire sentences as vectors, encoding the meaning and relationships between words within the sentence.

For example, consider the sentences *The sun is shining brightly.* and *The night sky is filled with shining stars*.* Their sentence embeddings would capture the overall meaning and context of each sentence. This permits them to be compared or used for tasks like text classification or semantic similarity.

The first sentence's embedding would encode information about the sun being out and the day being bright. The second sentence's embedding would encode information about the night and the presence of stars in the sky. This would allow the model to distinguish between the two sentences based on their overall meanings, even though they share some common words like **The**, **is**, and **shining**.

#### 3. Document embeddings

Document embeddings represent entire documents or large pieces of text as vectors, capturing the overall semantic content and relationships within the document.

For example, consider a travel blog post about visiting Paris and a cookbook with recipes for French cuisine. Their document embeddings would capture the overall topics, context, and meanings of each document. This permits them to be compared or used for tasks like document classification or information retrieval.

The travel blog post's document embedding would encode information about the author's experiences in Paris, including descriptions of famous landmarks, local culture, and personal anecdotes. However, the cookbook's document embedding would encode information about the various French dishes, ingredients, cooking techniques, and culinary traditions. This would allow the model to distinguish between the two documents based on their overall content and context, despite the fact that they both relate to French culture in some way.

---

The size of each chunk is limited by the maximum input size of the chosen embedding model. The embedding together with the original chunk of the document and additional metadata are stored in a vector database.

---

#### More on vector stores

After the text data is converted into numerical vectors (embeddings), these vectors are stored in a specialized data structure called a vector store (or vector database). Vector stores can efficiently store and retrieve high-dimensional vectors, which enables fast similarity search and retrieval operations. This is crucial for various natural language processing tasks that require finding semantically similar documents or passages based on their vector representations.

![Vector Stor picture](./images/W08Img016RagVectorStorePicture.png)

AWS offers many services for your vector database requirements, such as the following:

* **Amazon OpenSearch Service** helps you perform interactive log analytics, real-time application monitoring, website search, and more.
* **Amazon Aurora PostgreSQL-Compatible Edition** and **Amazon Relational Database Service (Amazon RDS) for PostgreSQL** support the **pgvector** extension to store embeddings from machine learning (ML) models in your database and to perform efficient similarity searches.
* **Amazon DocumentDB (with MongoDB compatibility)** supports vector search, a capability that you can use to store, index, and search millions of vectors with millisecond response times. With vector search for Amazon DocumentDB, you can set up, operate, and scale databases for your ML applications.

---

### Prompt augmentation and text generation

Now let's look at the other RAG workflow: prompt augmentation and text generation. The following diagram provides an overview of this workflow. This workflow will use the vector store (vector database or knowledge base) that you created in the data ingestion workflow.

![Prompt augmentation and text generation workflow](./images/W08Img018RagPromptAugmentationTextGenerationWokflow.png)

#### 1. User query

After you go through the data ingestion workflow, you are now ready to ask questions.

First, you enter your question or query. This could be something like *What are the famous landmarks in Paris?*

#### 2. Create embeddings

Your question goes through the same embedding model that was used for the data ingestion workflow. The model turns your question into a vector representation, like it did for the text data.

#### 3. Run a similarity search

Next, this question vector is searched in the vector data source. This vector data source contains all the vector embeddings of the text data from the ingestion workflow.

The magic happens during this search process. Instead of relying on exact keyword matches, the system performs a vector similarity search. It looks for vector embeddings in the data source that are similar or close to the vector embedding of your question.

#### 4. Augment the prompt

After you get the search result (the retrieval part), the retrieved context and the vector version of the question (the original prompt) make the augmented prompt.

#### 5. Generate the response

Finally, the augmented prompt will be sent to a foundation model (such as an LLM) to generate the response, and this is the generation part of the RAG process.

---

#### More on finding similarity

One of the key advantages of embeddings is that they enable efficient and meaningful comparisons between text elements. This enables semantic search, which is much more powerful than traditional keyword search.

Because the embeddings encode semantic information, the cosine similarity or distance between two embedding vectors can be used as a measure of semantic similarity between the corresponding texts. This property makes embeddings useful for tasks like document clustering, information retrieval, recommendation systems, and detecting duplicate or plagiarized content.

![Cosine similarity illustration](./images/W08Img020RagVectorSimilarityIllustration.png)

Cosine similarity is a measure of the angle between two vectors. The similarity value can range between −1 and 1. A smaller angle between the two vectors generates a higher cosine value. This indicates that the vectors are more semantically related. In contrast, if the angle between the two vectors is larger (for example, close to 180 degrees), it will generate a lower cosine value. This means that the two vectors are the opposite.

Even if your question uses different words from the text data, the system can still find relevant information. This is because the system understands the underlying meaning and context behind your query based on the similarity of vector embeddings.

For example, if you ask about famous landmarks in Paris, the system might retrieve information about the Eiffel Tower, the Louvre Museum, and Notre-Dame Cathedral. The system can do this even if your question didn't explicitly mention those specific landmarks. It makes these connections because the vector embeddings capture the semantic relationships between your query and the relevant information in the data source.

This semantic search capability is incredibly useful because you can ask questions in a more natural and flexible way, without being constrained by rigid keyword matching. The system can understand the intent behind your query and provide the most relevant and meaningful information.

---

The vector provided in the following section is a mock example and does not correspond to the true sentence embedding for the given question. It is provided solely to demonstrate the concept of representing text as high-dimensional vectors. Each dimension captures some aspect of the semantic meaning of the entire sentence, rather than just individual words.

---

Let's say that you ask the question: *What are some famous landmarks in Paris?*

In the vector world, this question would be represented as a high-dimensional vector, typically hundreds or thousands of dimensions. For example, the question *What are some famous landmarks in Paris?* could be represented as a 300-dimensional embedding vector as **[-0.012, 0.038, -0.124, 0.056, ..., 0.201, -0.075, 0.119]**.

This 300-dimensional vector representation, also known as the embedding, would encode the semantic meaning of the question, capturing the relationships between words like **famous**, **landmarks**, and **Paris**. The following steps show how similarity search works.

#### Step 1: Question embedding

The first step is to convert the question, *What are some famous landmarks in Paris?* into its corresponding 300-dimensional embedding vector **[-0.012, 0.038, -0.124, 0.056, ..., 0.201, -0.075, 0.119]**. This is done by using a pre-trained embedding model.

This model has learned to map text into high-dimensional vectors based on the semantic relationships present in a large training corpus.

#### Step 2: Vector store

Imagine that you have a vector store, which is a database that stores text passages (for example, sentences or paragraphs) as embedding vectors.

In this case, the vector store would contain embeddings of various text passages related to Paris, its landmarks, history, culture, and so on.

For example, in the vector store, you might have a 300-dimensional embedding for the sentence, *The Eiffel Tower is one of the most iconic landmarks in Paris, France.* And the relevant passage embedding is: **[0.028, -0.091, 0.147, -0.032, ..., -0.108, 0.063, -0.205]**.

#### Step 3: Similarity search

With the question embedding and the vector store, you can perform a similarity search. This involves computing the cosine similarity between the 300-dimensional question embedding and all the passage embeddings in the vector store.

Based on the cosine similarity scores, you can retrieve the top-k most similar passages from the vector store. These passages are likely to contain information relevant to the question about famous landmarks in Paris.

For example, the sentence about the Eiffel Tower would likely be among the top retrieved passages due to its high semantic relevance to the question.

#### Step 4: Context

Finally, the retrieved relevant passages can be provided as context to an LLM along with the original prompt.

The LLM can then generate a response by considering both the original question and the relevant context retrieved from the vector store.

---

This process of using high-dimensional embeddings to retrieve relevant information from a vector store and providing it as context to an LLM is a powerful technique that allows the model to generate more informed and accurate responses, especially for open-ended or knowledge-intensive queries.

---

#### Updating external data

After understanding how RAG works, the next question you might have is, "What if the external data becomes stale?" To maintain current information for retrieval, asynchronously update the documents and update the embedding representation of the documents. You can do this through automated real-time processes or periodic batch processing.

---

**Without RAG, the LLM takes the user input and creates a response based on information it was trained on—or what it already knows. With RAG, an information retrieval component is introduced that uses the user input to first pull information from a new data source. The user query and the relevant information are both given to the LLM. The LLM uses the new knowledge and its training data to create better responses.**

---

## RAG Use Cases
