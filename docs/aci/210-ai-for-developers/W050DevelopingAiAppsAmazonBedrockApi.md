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

## Interacting with Amazon Bedrock Playgrounds

You can use Amazon Bedrock in the AWS Management Console to interact with foundation models (FMs) through **Chat**, **Text**, or **Image** playgrounds. Each playground allows you to select a model, enter a prompt, and receive a response.

### How It Works

Amazon Bedrock provides an interface where users or consumers can send requests via different playgrounds to the selected foundation models (like Amazon Titan FM). Below is an architecture diagram:

![Amazon Bedrock Architecture](./images/W05Img010BedrockArchitecture.png)

### Amazon Bedrock Overview and Demonstration

---

### Signing in and Accessing Amazon Bedrock

* Sign in to the **AWS Management Console**.
* Choose the **N. Virginia** Region (`us-east-1`).
* In the Services search bar, enter "Bedrock" and select **Amazon Bedrock** from the results.

![Amazon Bedrock service page](./images/W05Img020ServicePageOverview.png)

---

### Requesting Model Access

* On the Amazon Bedrock service page, choose **Get started**.
* To request access to foundation models, choose **Model access** from the side-navigation menu.
* On the **Model access** page, click **Manage model access**.

![Model access page](./images/W05Img030ModelAccessList.png)

* Select **Titan Text G1 - Express** and **Titan Image Generator G1**.
* Click **Request model access** (or **Save changes** if previously requested).
* Wait for status to change to **Access granted**.

---

### Navigating the Overview Page

* Return to the **Overview** page to see available models, use cases, playgrounds, and tools.
* Playground types:
  * **Chat playground**
  * **Text playground**
  * **Image playground**

---

### Exploring the Chat Playground

* Open the **Chat playground**.
* Select the **Titan Text G1 - Express** model (Category: Amazon, Throughput: On-demand).

![Chat playground model selection](./images/W05Img040ChatPlaygroundSelectModel.png)

* Enter prompts in the **prompt section** and click **Run**.
* The conversation retains context from earlier prompts.

```text
What are some nice places to visit in NYC?
Are there any nearby water activities?
```

* Use the **Configurations** panel to adjust:
  * **Temperature** (controls creativity/randomness)
  * **Top P** (controls diversity)
  * **Length** and **Stop sequences**

![Chat configuration settings](./images/W05Img042ChatConfigPanel.png)

* Example: Set Temperature to `1` and request:
  
```text
Write a creative blog about ways to boil an egg.
```

---

### Using the Text Playground

* The Text playground handles **single-prompt text tasks**.
* Example:
  
```text
Suggest three marketing taglines for an at home car washing service emphasizing convenience and time savings.
```

* Each prompt is independent—no context retention between queries.

![Text playground interface](./images/W05Img050TextPlaygroundView.png)

---

### Using the Image Playground

* Open the **Image playground**.
* Select **Titan Image Generator G1** (Throughput: On-demand).
* Example prompt:

```text
Cat sitting on a fence with green mountain and river in the background.
```

![Image generation interface](./images/W05Img060ImagePlaygroundMain.png)

* Adjust configuration settings to control output.
* Download, edit, or generate variations of selected images.

---

### Conclusion

Amazon Bedrock provides a unified interface to explore multiple foundation models across chat, text, and image use cases—without managing underlying infrastructure.

## Accessing Amazon Bedrock

### Ways to access Amazon Bedrock

* AWS Management Console

    When you are using Amazon Bedrock through the AWS Management Console, you can use capabilities such as safeguards, orchestration, model assessment, and deployments. This is also how you can access the Amazon Bedrock playgrounds to interact with FMs and generate text or images, or have a conversation using the chat playground. 

    By using the playgrounds in Amazon Bedrock, you can submit a natural language command (prompt) to the FM and get a response (answer). You can influence the response from the model by adjusting model inference parameters, such as temperature, to increase or decrease the randomness (or creativity) in the response. You can provide prompts to generate text, generate images, summarize text, receive answers to questions, or have a conversation by using chat.

    **Note**: Access to FMs is managed only through the AWS Management Console. It cannot be managed using the API.

* Amazon Bedrock API

    You can use an Amazon Bedrock API to securely access FMs. Using the API, you can privately pass prompts and responses between the user and the FM. The Amazon Bedrock API can be used through the AWS SDK to build a generative AI application and to integrate with other AWS services. You will learn more about this method in the next section.

---

### Access to Foundation Models (FMs)

Access to Amazon Bedrock FMs is not granted by default. To gain access to an FM, an AWS Identity and Access Management (IAM) user with sufficient permissions needs to request access to it through the console. Once access is provided to a model, it is available for all users in the account.

---

### Granting Programmatic Access to Amazon Bedrock

When you want to interact with Amazon Bedrock outside of the AWS Management Console — maybe running CLI commands, building apps with SDKs, or integrating APIs — you must grant **programmatic access**.  
This is all about *securely authenticating* your requests to AWS.  

The type of IAM identity you use determines how you set this up.

---

1. Workforce Identity. *Managed in IAM Identity Center — uses temporary credentials.*  

    These are typically **human users** in your organization, authenticated via AWS IAM Identity Center. Instead of storing permanent keys, they receive **temporary credentials** at login — much safer because the credentials automatically expire.  

    **Usage:**

    * **AWS CLI** → Configure using [AWS CLI to use AWS IAM Identity Center](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html) from the CLI User Guide.  
    * **AWS SDKs / APIs** → Use [IAM Identity Center authentication](https://docs.aws.amazon.com/sdkref/latest/guide/access-sso.html) in the SDKs & Tools Reference Guide.  

    **Key point:** *You never hardcode credentials for workforce identities — the CLI or SDK handles token retrieval for you.*

2. IAM Users (Temporary Credentials). *Issued via AWS STS (Security Token Service).*  

    Here, you still work with IAM identities, but you don’t rely on long-term access keys. Instead, you generate **short-lived credentials** from AWS STS.

    This is common for automation scripts, federated users, or workloads that assume a role.  

    **Usage:**  

    * Use the `aws sts assume-role` or `aws sts get-session-token` commands.  
    * Pass these temporary credentials to your AWS CLI profile or SDK configuration.  

    **Key point:** *Ideal for short-term jobs, CI/CD pipelines, and cross-account access.*

3. IAM Users (Long-Term Credentials). *Permanent access keys stored in AWS IAM.*  

    These are **access key ID + secret access key** pairs assigned to an IAM user.  

    They don’t expire automatically — which is why they’re **more risky** if compromised. AWS recommends rotating them regularly or replacing them with temporary credentials.  

    **Usage:**  

    * Configure directly in the AWS CLI using `aws configure`.  
    * Store in AWS SDK credentials files for persistent use.  

    **Key point:** *Avoid for human users — use only when absolutely necessary, such as for legacy integrations.*

---

✅ **Tip:**  
Whenever possible, choose **temporary credentials** (workforce identities or STS) over long-term access keys. This aligns with AWS security best practices and minimizes your exposure window if credentials are ever leaked.

### Accessing Amazon Bedrock

Before you can make an API call or use the console to interact with an FM, you need to access Amazon Bedrock itself (either over the public network, or through a more secure private connection).

#### Accessing Bedrock through a simple connection

In this scenario, the user can be in an AWS-powered office using a VPC, or gaining access another way, such as remotely from a home office. The user logs into the console or uses the Amazon Bedrock API through their local network. Their requests leave either their home network or the customer network through a NAT gateway and go over the public internet. They can perform actions from there.

![Accessing Bedrock through a simple connection](./images/W05Img070VpcNatGateway.png)

#### Accessing Amazon Bedrock using AWS PrivateLink

If using the public internet to access an Amazon Bedrock endpoint is not an option, the connection can go through a more secure private connection. You can use PrivateLink with Amazon Bedrock to establish private connectivity between FMs and a VPC without exposing traffic to the public internet.

Users who access the customer network remotely can use AWS Direct Connect. Once in the customer network, a user will use PrivateLink, and then use VPC endpoints to perform their actions. In this instance, the client is going through the AWS backbone and nothing goes over the public internet. PrivateLink is automatically supported within Amazon Bedrock.

![Accessing Amazon Bedrock using AWS PrivateLink](./images/W05Img080VpcPrivateLink.png)

#### Making requests

The following diagram shows how inferences and other actions are performed in Amazon Bedrock. This traffic can come from the console or an API. While there are ways to access FMs without Amazon Bedrock, one key benefit is that none of the customer's data is written to the Amazon Bedrock service. Customer data used with Amazon Bedrock is not used for service improvement, and is not shared with third-party model providers. The customer always holds and controls all of their data. When accessing FMs directly, however, this is not the case.

Amazon Bedrock supports multiple communication paths for sending requests to models. All incoming traffic passes through the Bedrock API endpoint.

![API calls go through an API endpoint and then to Amazon Bedrock, which is secured and monitored using IAM, CloudWatch, and Cloudtrail, for inference.](./images/W05Img090ServiceFlow.png)

1. **User account**

    The user account creates calls that travel through network traffic. These calls can come from multiple sources, such as the console, CLI, an SDK, or an API.

2. **Amazon Bedrock inference service account**

    This is where the Bedrock inference service account is used. It is the one that relays the API call to make the inference on an FM.

    This account also determines which FM to use and ensures that correct permissions are applied. This account also checks that the correct logging is used.

3. **Amazon Bedrock model service account**

    This is where the Amazon Bedrock model service account is used. This account gives the Amazon Bedrock service read permissions to data sources, like an S3 bucket.

    This account also determines whether a user makes a general on-demand request (as shown in this diagram) or a request through provision capacity.

4. **AWS IAM**

    By using AWS Identity and Access Management (IAM), you can control access to your customized FMs. You can allow or deny access to specific FMs, decide which services can get inferences, and choose who can log in to the Amazon Bedrock console.

5. **Amazon CloudWatch**

    You can use Amazon CloudWatch to track usage metrics and build customized dashboards with metrics that you might require for audit purposes.

6. **AWS CloudTrail**

    Use AWS CloudTrail to monitor API activity and troubleshoot issues as you integrate other systems into your generative AI applications.

---

### Amazon Bedrock Account Types

The following table summarizes the accounts used to access FMs through Amazon Bedrock, as well as the data sources needed by the FMs.

| Account type                               | Owned by | Used for |
|--------------------------------------------|----------|----------|
| **User account**                           | Customer | * Accessing the Amazon Bedrock service |
| **Amazon Bedrock Inference service account** | AWS      | * Determining which model is used  <br> * Applying appropriate user permissions to models  <br> * Relaying inference commands  <br> * Checking for appropriate logging |
| **Amazon Bedrock Model service account**    | AWS      | * Housing the infrastructure that hosts an FM  <br> * Granting Amazon Bedrock Inference account read permissions to data sources  <br> * Determining if a user makes a general on-demand request or a request through provision capacity |

### Knowledge Check

#### Which service should a company use if they want to secure requests coming from inside their VPC to Amazon Bedrock?

* AWS PrivateLink

Wrong answers:

* Amazon Direct Connect
* AWS Site-to-Site VPN
* AWS Client VPN

##### Explanation

Using these VPC endpoints provides resources with private connectivity so traffic is not exposed to the public internet.  

The other options are incorrect for the following reasons:

* **Amazon Direct Connect**: This service provides secure, low-latency performance to on-premises networks through dedicated hardware, without traversing the internet. This would not be used for VPC to Amazon Bedrock communication.
* **AWS Site-to-Site VPN**: This service creates a secure connection between your on-premise networks, like branch offices, to AWS resources using IPSec tunneling over the internet. This service would not be used for communication between a customer VPC and Amazon Bedrock.
* **AWS Client VPN**: This service provides a client's remote workforce with secure access from client endpoints to within both AWS and on-premises networks. While this does provide a private connection to AWS, it would not be used for communication between a customer VPC and Amazon Bedrock.

#### Which of the following can be used to access an Amazon Bedrock image playground?

* AWS Management Console

Wrong answers:

* Amazon Bedrock SDK
* AWS CLI
* Amazon SageMaker Notebook

##### Explanation

The other options are incorrect because none of them provide access to the Amazon Bedrock playgrounds.

#### Which account routes Amazon Bedrock queries to the proper foundation model?

* Amazon Bedrock Inference

Wrong answers:

* User
* Root user
* Amazon Bedrock Model

##### Explanation

**Amazon Bedrock Inference** account performs actions such as the following:

* Relaying inference commands
* Applying appropriate user permissions to models
* Checking for appropriate logging

The other options are incorrect for the following reasons:

* **User**: This account is the end user and it makes the actual inferences
* **Root user**: This account should only be used for high-level account tasks unrelated. It should not be used to access Amazon Bedrock
* **Amazon Bedrock Model**: This account performs actions such as the following:
  * Granting Amazon Bedrock Inference account read permissions to data sources
  * Determining if a user makes a general on-demand request or a request through provision capacity

### Additional Resources

* [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html)
* [Configuring IAM Identity Center authentication with the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html)
* [Use temporary credentials with AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html)
* [Authenticating using IAM user credentials for the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-authentication-user.html)
* [Manage access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html)

### Summary

Amazon Bedrock helps developers build, deploy, and scale LLMs for applications. It provides the following key benefits:

Efficient builds using foundation models 
Security of generative AI applications
Customized experiences using an organization's data
While there are ways to access FMs without Amazon Bedrock, one key benefit is that none of the customer's data is written to the Amazon Bedrock service. Customer data used with Amazon Bedrock is not used for service improvement and is not shared with third-party model providers. The customer always holds and controls all of their data.

#### Amazon Bedrock Playgrounds

You can access Amazon Bedrock with the AWS Management Console to use the text, chat, or image playgrounds. The playgrounds allow you to select an FM, enter a prompt, and generate a response.

#### Accessing Amazon Bedrock

Amazon Bedrock can be accessed using the AWS Management Console or Bedrock APIs. When you are using the APIs, access is not automatically granted if you have Amazon Bedrock access. Instead, you need to set up programmatic access, either through workforce identity or IAM.

#### Secure Amazon Bedrock access

If using the public internet to access an Amazon Bedrock endpoint is not an option, the connection can go through a more secure private connection. You can use AWS PrivateLink with Amazon Bedrock to establish private connectivity between FMs and a VPC without exposing traffic to the public internet.

#### When requests are made

There are three accounts involved in accessing FMs through Amazon Bedrock and the necessary data sources.

| Account type                               | Owned by | Used for |
|--------------------------------------------|----------|----------|
| **User account**                           | Customer | * Accessing the Amazon Bedrock service |
| **Amazon Bedrock Inference service account** | AWS      | * Determining which model is used  <br> * Applying appropriate user permissions to models  <br> * Relaying inference commands  <br> * Checking for appropriate logging |
| **Amazon Bedrock Model service account**    | AWS      | * Housing the infrastructure that hosts an FM  <br> * Granting Amazon Bedrock Inference account read permissions to data sources  <br> * Determining if a user makes a general on-demand request or a request through provision capacity |

## Amazon Bedrock API and its parameters

### Overview of the Amazon Bedrock API

As a developer, you will often access Amazon Bedrock through its API using the CLI or SDK.

AWS offers the following tools to streamline the process of setting up an environment to make Amazon Bedrock requests through the Amazon Bedrock API.

* AWS CLI
* AWS SDKs

You must ensure that you either have the most up-to-date version of the AWS CLI, or you have an SDK installed. Each SDK provides an API, code examples, and documentation that make it easier for you to build applications in your preferred language. SDKs automatically perform useful tasks for you, such as the following:

* Cryptographically signing your service requests
* Retrying requests
* Handling error responses

In its simplest format, the Amazon Bedrock API requires the following steps for invoke a model.

1. Create an endpoint connection

    The Amazon Bedrock endpoints allow you to interact with the Amazon Bedrock service and its FMs. There are several kinds of endpoints, and they provide their own unique API operations for a variety of tasks, such as the following:

    * Creating, managing, and evaluating models
    * Creating provisioned models
    * Getting foundation models
    * Getting guardrails
    * Getting model customization jobs

    ```python
    import boto3
    import json
    
    # Create the connection to Bedrock runtime
    bedrock_runtime = boto3.client(
        service_name='bedrock-runtime',
        region_name='us-east-1',
    )
    ```

2. Specify parameters

    You can set parameters for both Amazon Bedrock and for the FM you are using.

    ```python
    # Specify Amazon Bedrock parameters
    model_id = 'amazon.titan-tg1-large'
    accept = 'application/json'
    content_type = 'application/json'
    
    # Set FM specific parameters
    text_gen_config = {
        "maxTokenCount": 1000,
        "stopSequences": [],
        "temperature": 0,
    }
    ```

3. Pass a prompt and any model-specific parameters

    Next, pass your prompt to the FM and combine it with FM-specific parameters. This creates the prompt body.

    ```python
    # Define prompt and model parameters
    prompt_data = """Write an essay about why someone should drink coffee."""

    # Combine the FM specific parameters along with the prompt to create the parameter body.
    body = json. dumps ({
        "inputText": prompt_data,
        "textGenerationConfig": text_gen_config
    })
    ```

4. Invoke your FM and format the output

    Once you have entered your prompt, you need to invoke your FM and specify your preferred output format.

    ```python
    # Invoke the model
    response = bedrock_runtime.invoke_model(
        body=body,
        modelId=model_id,
        accept=accept,
        contentType=content_type
    )
    
    # Once the response is returned format it as a Python dictionary
    response_body = json.loads(response.get('body').read())
    
    # Print the response
    print(response_body['results'][0]['outputText'])
    ```
