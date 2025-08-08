# Week 5: Developing AI Apps with Amazon Bedrock API

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to [AI for Developers](./ai-for-developers.md)
* back to repo's main [README.md](../../../README.md)

## Amazon Bedrock Overview

**Amazon Bedrock** is a fully managed AWS service that enables developers to build, deploy, and scale generative AI applications using foundation models (FMs). It provides the necessary infrastructure, tools, and capabilities to support AI development with a strong focus on **security**, **privacy**, and **responsible AI**.

---

### 🔹 Key Capabilities of Amazon Bedrock

#### ✅ Model Choice

Amazon Bedrock offers access to **multiple high-performing foundation models** from leading AI providers, including:

* **Anthropic**
* **Cohere**
* **Meta**
* **Mistral AI**
* **Stability AI**
* **AI21 Labs**
* **Amazon**

With a **single API**, developers can easily switch between models or upgrade to newer versions with minimal code changes—enabling flexibility and agility.

---

#### ✅ Customization

Bedrock supports **private fine-tuning** of models using your own data:

* Fine-tune models (e.g., **Titan Text**) using **labeled datasets** for specific tasks.
* Continue pretraining with **unlabeled data** to adapt models to your domain or industry.
* Your data remains private—Bedrock creates a **separate instance** of the base model, and your data is **never used** to train shared models.

---

#### ✅ Retrieval-Augmented Generation (RAG)

Amazon Bedrock includes **Knowledge Bases** to support Retrieval-Augmented Generation:

* Enhance FM responses with **contextual company data**.
* Automate the **entire RAG workflow**, including data ingestion, retrieval, prompt augmentation, and citation generation.
* Eliminates the need for custom integration code, speeding up development and reducing complexity.

---

#### ✅ Agents

**Bedrock Agents** can automate **complex, multi-step workflows** across systems:

* Securely access and execute APIs.
* Retrieve and process data from internal systems.
* Analyze requests, orchestrate actions, and ensure secure execution.

This reduces manual effort and increases process efficiency while maintaining high standards for **privacy and security**.

---

### 🔹 Real-Life Applications of Amazon Bedrock LLMs

#### ✈️ Building Conversational AI Applications

* Developers at an airline can build **chat-based AI assistants** to help customers with:
  * Booking flights
  * Providing flight information
  * Answering common questions
* These assistants can be integrated into websites or mobile apps for **seamless, personalized customer experiences**.

---

#### 🛍️ Automating Customer Service

* E-commerce companies can use AI assistants to:
  * Automate support tickets via chat
  * Access purchase history, order status, and complaint details
* Assistants can verify users and provide **real-time updates**, improving response time and customer satisfaction.

---

#### 🏢 Enhancing Business Processes

* Media companies can deploy AI assistants to:
  * Automate tasks like meeting scheduling, report generation, and data retrieval from disconnected systems.
  * Support content creators with research, draft generation, and trend insights.
* This enhances **productivity** and **streamlines internal operations**.

---

### ✅ Summary

Amazon Bedrock provides a powerful platform to build secure, scalable, and customizable generative AI solutions. It supports a wide range of use cases across industries, enabling organizations to innovate faster while maintaining control over data and privacy.




## Amazon Bedrock API and its parameters
