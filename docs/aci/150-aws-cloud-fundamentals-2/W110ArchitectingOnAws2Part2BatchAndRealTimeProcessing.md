# Week 11: Architecting on AWS 2 Part 2: Batch and Real-Time Processing Architectures

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to [AWS Cloud Fundamentals 2](./aws-cloud-fundamentals-2.md)
* back to repo's main [README.md](../../../README.md)

## DESIGNING A BATCH PROCESSING APPLICATION ARCHITECTURE

### Batch Processing Architectures

When a task must be repeated multiple times, it's often more efficient to perform it in batches rather than individually. For instance, when doing laundry, it's better to wash clothes of the same color or fabric type together in one load, instead of washing each item separately. This batch processing approach saves time and effort. Similarly, applications process data in batches to achieve greater efficiency.

#### Understanding batch processing

When applications have to perform the same operation on a lot of data, it is generally more efficient to break those operations into one or more batch processing jobs.

Batch processing is a way to automate a series of application tasks and minimize the need for human intervention. Batch processing is commonly used in industries where large volumes of data need to be processed for non-time sensitive workloads, such as financial services, scientific computing, and media production.

Batch processing offers several key benefits, including improved efficiency, reduced costs, and the ability to handle large scale data processing tasks.

For example, the property management company for an apartment building collects rents from tenants on a monthly basis, then uses that income to pay its operating costs. Some apartment tenants may pay their rent by mail using a check. Others may pay online using a credit card, and some may pay their rent in person using cash. Rather than process each of these payments separately, it is more efficient for the apartment management company to hold all the rent payments as they arrive. Then all the payments are processed together at one time before sending the payment data to the company's financial management systems.

The AWS Cloud offers several services that support batch processing for applications.

* **AWS Batch** is a fully-managed batch processing service, which makes it easy to run batch computing workloads on the AWS Cloud.
* **AWS Step Functions** is a visual workflow service that helps developers use AWS services to support batch processing for applications.
* **AWS Lambda functions** can be used to initiate and perform batch processing activities.
* **Amazon Elastic Map Reduce, or Amazon EMR** is a data analytics service, specifically designed to perform batch processing on very large data sets.
* **Amazon EC2 spot instances** can be used to temporarily add additional low cost compute resources that are needed only during batch processing.

#### Examples of batch processing workloads

Batch processing is the method that computers systems use to periodically complete high-volume repetitive tasks. These types of systems process such tasks in batches, often in off-peak times when computing resources are more commonly available, such as at the end of the day or overnight. The following sections describe some scenarios where applications and their infrastructure use batch processing.

##### Batch processing for applications

Applications take in data from many sources for processing. With shopping or messaging applications, users enter, update, and process application data in real time. However, there are also scenarios where real-time application data input and processing are not required. These situations are well suited for batch processing of application data.

###### Processing data

Batch processing is often performed on transactional application data after the transactional data has been collected. For example, a utility company that collects real-time utility usage data runs a monthly batch process to summarize that real-time usage data and prepare the customer's billing statement. After this is calculated, the billing statements might go through additional batch processing to help the utility company identify overall usage patterns for a specific group of customers, geographic region, or time of year.

###### Filtering, sorting, and converting application data

Sometimes the data provided to an application has to be filtered, sorted, or converted before it is suitable for use by the target application. For example, prices that use local currencies might have to be converted to a different currency before being loaded into a data analytics environment. The transform step of the extract, transform, and load (ETL) process that is used when moving data from source systems into a data analytics environment would be responsible for this type of batch processing.

###### Loading application data

Not all application data is entered by users. Application data related to merchandise pricing, workforce scheduling, or product shipping costs usually only changes on a daily, weekly, monthly, or even annual basis. This data might come from external systems and not be created in the application itself. For example, daily work start and end times might be captured by an employee time clock system but only loaded into the payroll application once a month. Loading data of this type can be performed in batch, with the frequency of the availability of new data, and the needs of the application, driving the data loading schedule.

##### Batch processing for infrastructure

Batch processing can also be used on the data related to monitoring and managing the infrastructure on which applications reside.

###### Infrastructure backups

Application databases contain data that can be constantly changing. However, backing up the database after each individual data change is not practical. Modern databases incorporate recovery mechanisms in their architectures to prevent the loss of application data, but regular database backups are still required for maximum recoverability. Running batch jobs to back up important database files on an hourly, daily, or weekly basis limits the impact of the backup operation on the database resources and application users.

###### Log management

Most technology stack software components like databases, application servers, and web servers generate logs to record their activity, errors, and events.

Applications themselves also generate logs related to application activity. Batch processes are used to archive, truncate, or remove logs on a regular basis. This keeps only the most recent and relevant data in the logs.

```text
Amazon CloudWatch and AWS CloudTrail provide automated mechanisms for monitoring and managing infrastructure logs using both batch and real-time techniques.
```

###### Software patching

Like applications, the database, web server, and application server software that support applications requires regular patching to maintain optimum reliability and security. Patches are usually released on a monthly, quarterly, or annual basis, unless there is a specific, serious bug that must be fixed. Batch processing is well suited to patching, because many environments might require patching at once, and batch automation allows for consistent patching application across environments.

#### Batch processing aligns to the Well-Architected Framework

The AWS Well-Architected Framework includes multiple recommendations that can be implemented by incorporating batch processing in an application architecture.

##### Operational excellence

Adding or removing batch processing environments to meet the demands of an application helps keep applications running smoothly. However, to deliver this capability with operational excellence, the deployment and management of batch environments must be automated.

Effectively delivering this automation requires two elements. First is the monitoring of the utilization of the batch processing resources. This data is required to know when additional resources should be added or removed. Second is accurately monitoring and logging the status of each batch process. This data tells you if a process is running longer than expected or if it fails entirely due to a lack of resources.

If a bank is using batch processing for facilitating credit card purchases, the number of transactions that have to be processed will vary widely based on the time of year. For example, shopping activity around major gift-giving holidays will produce more credit card activity than other times of the year. By monitoring the resources that perform the batch processing, additional resources can be added to handle the increased processing that holiday activity brings. Likewise, regardless of the activity level, any failures during credit card processing must be retried so that the card transaction is properly documented.

##### Security

Batch processing can also be used to dedicate processing environments for batch operations, separate from the normal transactional application environment. The data used for the batch operations can also be stored separately from transactional application data. Operating in this manner provides an additional layer of security for batch operations. Access to data between the transaction and batch environments can be controlled using access permissions or encryption.

For example, to determine the types of surgical equipment in which they should invest., a hospital performs batch analytics on sensitive patient data. The required security controls around this data would be high, and might differ from the transactional system that the data originates from. Moving this batch processing to a secondary environment, with special access controls and data encryption capabilities, helps meet the unique security requirements.

##### Reliability

Batch processing can be used to improve application reliability through implementation of a resilient queuing model. This architecture model builds in mechanisms that allow failed batch processing jobs to be automatically resubmitted for processing. If the failed batch job fails multiple times, it can be marked for further investigation, while other batch jobs can continue to be submitted and processed.

One reason that a batch process can fail is a lack of available resources to complete the required processing. Dynamically scaling the application architecture to add additional resources to meet batch processing demands helps enhance application reliability. Coupling scaling with resilient queueing allows the application to retry the failed batch process after the additional resources have been allocated.

Video hosting services are a good example of applications that uses queued batch jobs to improve resiliency. When a user uploads a video to the platform, the video file must be converted into multiple formats and resolutions to support different devices and bandwidth conditions. This conversion process is computationally intensive and can take a significant amount of time, especially for longer videos or high-resolution files. Instead of making the user wait for the conversion to finish before their video is available, these platforms use a queued batch job system that notifies the user when their video is ready. Additionally, if there is a failure or interruption during transcoding, the job can be retried or moved to a different server without impacting the user experience.

##### Performance efficiency

Auto scaling is one mechanism for adding resources until the desired performance during large batch operations is achieved. This real-time right-sizing capability is particularly useful when the size of batch operations varies from one job to the next.

Additionally, monitoring CPU, memory, and I/O for Amazon Elastic Compute Cloud (Amazon EC2) instances will help you determine if the resources that you have allocated to the batch processes are being fully utilized. If the resources are underutilized, consider decreasing their capacity or adding additional workload to the batch process so that the available resources are fully utilized.

Choosing optimal data formats, compression techniques, and partitioning based on the source data and target environments is also important when performing batch data loading operations.

##### Cost optimization

One of the benefits of the pay-per-use model of cloud computing is only paying for resources when you need them. By running large data processing, loading, or transformation jobs in batch, you can add additional resources to your environment during the batch operation, then release those resources when the batch process is complete. Even large, memory-rich or CPU-rich Amazon EC2 instances can be cost effective for batch processing when used in this manner. EC2 Spot Instances are another way to reduce the cost of adding resources during batch processing.

You should also monitor the batch resources to optimize and reduce costs. Examine how changing capacity or using reserved instances or savings plans might contribute to reducing batch operation costs.

##### Sustainability

Batch processing can help optimize resource utilization by processing data in batches during off-peak hours. This reduces the application's overall carbon footprint and energy consumption. Batch processing tasks can be scheduled and executed in parallel, minimizing idle time and maximizing resource utilization.

AWS services like AWS Batch and AWS Lambda can automatically scale resources up or down based on demand, ensuring that only the necessary resources are provisioned. This further contributes to sustainability.

#### Batch processing patterns

The previous sections described the concepts of batch processing, and potential benefits that batch processing can provide an application. The following sections describe three common batch processing architecture patterns:

* Fan-out pattern
* Fan-in pattern
* Dynamic parallelism

##### Fan-out pattern

The fan-out pattern is a parallel processing model where a single input is divided into multiple smaller tasks, which are then processed concurrently by multiple workers or services. The fan-out pattern is useful when you have a large amount of data or a computationally intensive task that can be divided into smaller, independent units of work.

The following image shows a conceptual example of how the fan-out pattern works.

![Image showing a large batch dataset going into a fan-out operation, which creates four separate batch processing jobs.](./images/W11Img010BatchProcessingFanOut.png)

Fan-out operation for batch processing.

In this pattern, a task to process a large batch data set is split into four smaller batch processing jobs by a fan-out operation. Then each smaller batch processing job runs in parallel to complete the batch operation.

##### Fan-in pattern

The fan-in pattern is the complementary pattern to the fan-out pattern. It is used to consolidate the results of multiple parallel tasks into a single output or result. This pattern is often used in conjunction with the fan-out pattern to handle the aggregation and post-processing of the results from parallel tasks.

The following image shows a conceptual example of how the fan-in pattern works.

![Image showing four separate batch processing jobs going into a fan-in operation to create a large batch dataset.](./images/W11Img012BatchProcessingFanIn.png)

Fan-in operation for batch processing.

After the subtasks have been processed in parallel by the workers or services, the fan-in pattern collects and combines the individual results into a final output.

```text
The fan-out and fan-in patterns are complementary and often used together to achieve parallel processing and result consolidation. The fan-out pattern focuses on dividing the input into smaller tasks for parallel implementation, and the fan-in pattern focuses on combining the results of those parallel tasks.
```

##### Dynamic parallelism

The dynamic parallelism pattern is an extension of the fan-out pattern, where the number of parallel tasks is not fixed but can dynamically adjust based on the input data or the available resources. However, the dynamic parallelism pattern extends the fan-out pattern by allowing for dynamic and recursive task subdivision. This allows for efficient utilization of resources by adapting the level of parallelism based on the complexity of the input data or the available computing resources.

The following image shows a conceptual example of how the dynamic parallelism pattern works.

![Very large batch dataset uses fan-out operation to create 2 batch processing jobs, which use fan-out operations to create 3 sub-jobs.](./images/W11Img014BatchProcessingDynamicParallelism.png)

Dynamic parallelism for batch processing.

In this pattern, the input data is divided into tasks, and each task can further subdivide itself into smaller subtasks if necessary, creating a recursive tree-like structure of parallel tasks.

##### Choosing a batch processing pattern

The fan-out and fan-in patterns are suitable for scenarios where the input data can be easily divided into independent tasks. The dynamic parallelism pattern is more suitable for scenarios where the complexity of the input data varies and requires adaptive task subdivision.

For example, in some applications, the data that must be processed by a batch job always has the same volume and type of data. Processing lab results for a biotechnology research facility is one such scenario. The number of experiments conducted each day is fairly consistent, because the number of scientists performing experiments is fixed. Based on past experience, a fan-out or fan-in pattern can be configured that will use a predefined number of sub-jobs to process the research data according to the lab's needs.

Alternatively, some applications do not have consistent data volumes or data types being held for batch processing. For example, a batch processing cycle for a car rental agency might run every 10 minutes, but the amount of data needing to be processed might vary from no data to huge amounts of data on busy days.  Dynamic parallelism is helpful in this scenario because the number of sub-jobs can be increased or decreased based on the volume of data that has to be processed.

### Implementing Batch Processing with AWS

AWS offers several services that can be used to implement fan-out, fan-in, and dynamic parallelism batch processing patterns for applications. These services are used to manage both the orchestration and scheduling of batch processing in applications.

#### Data orchestration services

**Data orchestration** refers to the automated coordination and management of data flows between application systems and components. It typically involves streamlining the movement, transformation, and integration of data from multiple sources for efficient processing. The AWS services used for orchestration of batch data processing include AWS Step Functions and Amazon EMR.

##### AWS Step Functions

Step Functions is a serverless function orchestrator that allows you to coordinate multiple AWS services into a series of steps, so you can build and run complex, distributed applications.

Step Functions operates on the concept of a **state machine**, or workflow. A state machine defines a series of steps and their transitions. Each step can perform tasks, choice operations, or parallel operations, and support various application architectures, including fan-out, fan-in, and dynamic parallelism.

Fan-out architecture is supported by splitting a single input into multiple parallel tasks or branches using the **Parallel state**. Step Functions can provide a fan-in architecture by using the **Parallel state** in combination with the **Choice state** or by using the **Map state** to process an array of inputs. Dynamic parallelism is also supported through the use of the Map state, which can iterate over an array of inputs and run tasks in parallel for each element.

##### Amazon EMR

Amazon EMR is one of the AWS services that provides data orchestration capabilities in support of application batch processing. Many data analytics environments are based on big data frameworks such as Apache Hadoop and Apache Spark. These frameworks make use of a **distributed architecture model**. This architecture has special mechanisms in place that spread data load and data query operations across many individual compute and storage resources called **nodes** that are connected together to form a **cluster**.

Using this model, each data load and data query job is divided into smaller chunks, and each chunk is processed by a separate cluster node. This parallel processing is designed to efficiently process large datasets using a batch-based approach.

Processing that is both distributed and parallel can be difficult to manage. The management complexity arises from the multiple nodes composing the cluster and from the cluster management software used to coordinate the activities between nodes.

As with many other complex computing services, the AWS Cloud simplifies the deployment, management, and operation of a distributed parallel processing environment by automating the creation, configuration, and management of the underlying infrastructure. Amazon EMR is a fully managed, distributed parallel processing solution. An Amazon EMR cluster consists of three different Amazon EC2 node types: Primary, core, and task. Each node type has a role within the cluster, with different software components installed on each node type.

![Six-node Amazon EMR cluster consisting of a primary node, three core nodes, and two task nodes.](./images/W11Img020BatchProcessingEmrCluster.png)

1. **Primary node**

    Primary nodes manage the cluster by running software components to coordinate the distribution of data and tasks among the other nodes during processing. The primary node tracks the status of tasks and monitors the health of the cluster. Every cluster has a primary node, and it's possible to create a single-node cluster that has only a primary node.

2. **Core node**

    Core nodes run software components that perform processing tasks and store data across the available storage on the cluster. Multi-node clusters must have at least one core node.

3. **Task node**

    Task nodes are optional, but when used, task nodes run software components that only perform processing tasks and do not store data.

The six-node cluster shown here is composed of a primary node, three core nodes, and two task nodes. The lines between nodes show that every node in the cluster can communicate with every other node in the cluster. You can add task and core nodes to an Amazon EMR cluster at any time to increase the cluster's overall batch processing and store capacity.

#### Batch process scheduling services

The AWS services used for scheduling batch data processing include Lambda, AWS Batch, Amazon Elastic Container Service (Amazon ECS), and Amazon Elastic Kubernetes Service (Amazon EKS).

##### AWS Lambda

Lambda is a serverless computing service that allows you to run functions written in Java, Go, PowerShell, Node.js, C#, Python, or Ruby. There are several benefits to combining AWS Lambda for carrying out individual batch processing tasks, and AWS Step Functions for orchestrating and coordinating these tasks into complex workflows:

* Both services follow a serverless architecture, allowing you to focus on your application logic without managing underlying infrastructure.
* Lambda can automatically scale to handle high volumes of concurrent invocations, enabling parallel processing of batch jobs. Step Functions can coordinate and orchestrate these parallel operations
* Step Functions provides a way to define and manage stateful workflows, which is essential for batch processing pipelines that might involve multiple steps or conditional branching.
* Step Functions offers built-in retry and error handling mechanisms, ensuring reliable processing of batch jobs even in the face of transient failures.

##### AWS Batch

AWS Batch is a service that supports the scheduling and management of application batch job activities. It is a fully managed batch processing service that allows you to efficiently run batch computing workloads in the AWS Cloud.

AWS Batch automatically provisions the required compute resources. It manages the submission of your batch jobs, defines batch job dependencies, and uses features like automatic scaling and job monitoring to optimize your batch processing workflows.

Several key capabilities make AWS Batch a good resource for creating, running, and managing scalable batch processing operations. These capabilities include the following:

* **Job definitions** specify the container image, processing and memory requirements, and other configurations for running a batch job.
* **Job queues** are used to manage and prioritize the processing of batch jobs. You can create multiple job queues with different priority levels and associate them with specific compute environments.
* **Compute environments** define the AWS Fargate or Amazon EC2 compute resources that will be used to run your batch jobs. You can configure the instance types, minimum and maximum vCPUs, and other settings for the compute environment.
* **Job scheduling** lets you define job dependencies and automatic retries for failed jobs. Array jobs, the running of multiple copies of a job with different input parameters, are also available.
* **Job monitoring and logging** is possible using the AWS Batch integration with Amazon CloudWatch. With this integration, you can track the status and resource utilization of batch jobs, and set up alarms for specific events or thresholds.
* **Job storage** facilitates the storage of input and output data from batch jobs. AWS Batch supports using both Amazon Elastic File System (Amazon EFS) and Amazon Simple Storage Service (Amazon S3) for this purpose.
* **Job submission** operations can be performed using the AWS Batch API, AWS Command Line Interface (AWS CLI), or AWS SDKs. You can submit jobs either individually or as part of a job array.
* **Job dependencies** can be defined to ensure that jobs are processed in the correct order and that dependent jobs are only run after their prerequisites have been completed successfully.
* **Automatic job scaling** allows AWS Batch to add or remove compute resources based on the number of jobs in the job queues. This helps ensure efficient resource utilization and cost optimization.

###### Scientific Computing and Research

AWS Batch is well-suited for scientific computing and research applications that involve running complex simulations, data analysis, or computational models. These workloads often require significant computational resources and can benefit from the ability to scale resources up or down dynamically based on demand. Examples include genomic data analysis, climate modeling, and simulating liquid or gas flows using mass, momentum, and energy equations.

###### Media Transcoding and Processing

Media and entertainment companies often need to process large volumes of audio, video, or image files for various purposes, such as transcoding, watermarking, or content analysis. AWS Batch can be used to efficiently distribute these batch processing tasks across a fleet of compute resources, ensuring timely completion and optimal resource utilization. This use case is particularly relevant for video streaming platforms, post-production studios, and media content delivery networks.

###### Financial Risk Analysis and Modeling

Financial institutions and investment firms frequently run complex risk analysis, portfolio optimization, and financial modeling workloads. These batch processing tasks can be computationally intensive and might have to be executed on a recurring schedule or triggered by specific events. AWS Batch provides a scalable and reliable platform for running these financial modeling workloads, ensuring that computations are completed within the required time constraints and with the necessary compute resources.

##### Using AWS Batch with AWS Lambda

Using AWS Batch in conjunction with Lambda can be an effective architectural model for batch processing application data. This combination takes advantage of the strengths of both services, providing a scalable and cost-effective solution.

AWS Batch excels at running large-scale batch processing jobs that require significant computational resources. However, managing the submission and orchestration of these batch jobs can be a challenge, especially when dealing with complex workflows or event-driven processing. This is where AWS Lambda comes into play. Lambda functions can be invoked by various events, such as file uploads to Amazon S3, database updates, or API calls. These functions can then submit batch jobs to AWS Batch, passing the necessary input data and job configurations.

Another advantage of using AWS Batch with Lambda is the ability to implement serverless batch processing architectures. Lambda functions can be used to process and filter data before submitting batch jobs, reducing the overall compute requirements and costs. Additionally, Lambda functions can be used to handle post-processing tasks after batch jobs are complete, such as data aggregation, notification, or cleanup operations.

When AWS Batch and Lambda are combined, AWS Batch can handle the heavy lifting of running computationally intensive batch jobs. AWS Lambda provides a serverless and flexible way to manage the orchestration, preprocessing, and postprocessing tasks associated with batch processing workflows.

##### Amazon EKS and Amazon ECS

Amazon EKS and Amazon ECS are two more AWS services that provide data scheduling capabilities in support of application batch processing.

Amazon EKS is based on the open-source Kubernetes container management platform. Amazon EKS streamlines the deployment, scaling, and management of containerized applications on AWS. Amazon EKS provides a fully managed Kubernetes control plane, which allows you to build and run containerized applications without managing the underlying infrastructure.

Amazon ECS is a proprietary, fully managed container orchestration service that simplifies running and scaling containerized applications on AWS. It supports Docker containers and allows you to use API calls to launch and stop container-based applications.

Amazon ECS is tightly integrated with other AWS services. It is generally considered simpler to set up and manage than a Kubernetes-based containerization environment.

Both Amazon EKS and Amazon ECS can be used to schedule batch processing in an application architecture. With Amazon EKS, you can use Kubernetes jobs to run batch processing tasks on a schedule or on demand. These jobs can be configured to run on a specific set of nodes or using the auto scaling capabilities of Kubernetes to dynamically provision resources as needed. In Amazon ECS, you can use the batch service to run batch processing jobs on AWS Fargate or Amazon EC2 instances. The batch service automatically provisions the required compute resources, schedules the jobs, and monitors their processing, providing a seamless batch processing experience.

```text
Although similar to the Amazon ECS batch feature, the AWS Batch service offers more advanced job scheduling, management, and monitoring capabilities than those provided by Amazon ECS.
```

#### Combining orchestration and scheduling services

None of the AWS services described in the preceding sections are entirely dedicated to either data orchestration or batch process scheduling. Instead, each of these services can deliver both of these capabilities to varying degrees. The stacked bar graph shown here provides a visualization of how much of each capability these services provide.

![Stacked bar graph showing how much data orchestration and batch process scheduling capability each AWS service delivers.](./images/W11Img030BatchProcessingDataOrchestration.png)

Comparison of the data orchestration and batch process scheduling capabilities of AWS services.

The graph shows that AWS Step Functions is predominantly used to deliver data orchestration capabilities. Conversely, AWS Batch, Amazon EKS, and Amazon ECS are predominantly used to deliver batch process scheduling capabilities. Amazon EMR and AWS Lambda fall in between, with Amazon EMR providing more data orchestration capabilities, and AWS Lambda providing more batch process capabilities. When services are combined in an application architecture, you can use the strongest aspect of each service's capabilities to deliver your application's desired functionality for batch processing.

##### Combining AWS Step Functions and AWS Lambda

The following example shows how Step Functions and Lambda functions can be used to orchestrate and schedule the individual components of an application's batch processing workflow. In this example, the batch process uses the Amazon Comprehend service to perform sentiment analysis on files stored in an Amazon S3 bucket. When the sentiment has been determined, the sentiment results are stored in an Amazon DynamoDB table. The batch aspect of this workflow can be built into the two Lambda functions.

![Step Functions workflow that uses Lambda functions.](./images/W11Img032StepFunctionsWithLambda.png)

1. **State machine**

    Define the state machine in the Amazon States Language (ASL) using the AWS Step Functions console or AWS CloudFormation.

2. **Initiate state**

    Use the S3Source service integration to initiate the state machine whenever 100 or more files have been uploaded to the S3 bucket.

3. **Sentiment analysis state**

    Invoke a Lambda function that uses Amazon Comprehend to perform sentiment analysis on the preprocessed text.

4. **Storage state**

    Invoke a Lambda function to store the sentiment analysis results in a database table.

Using AWS Step Functions and AWS Lambda functions, you can orchestrate this batch processing workflow, handle error conditions, and monitor the completion of each step. Additionally, you could extend this workflow to include more complex processing steps or integrate with other AWS services as needed.

```text
AWS Step Functions used in conjunction with AWS Lambda and the Kinesis family of services creates a solid base for building batch-based applications. These services will be the focus of subsequent sections.
```

### How Step Functions Supports Batch Processing

AWS Step Functions is a visual workflow service that helps you build distributed applications, automate processes, orchestrate microservices, and create data and machine learning pipelines. Step Functions can also be used to provide orchestration for processing batch jobs. The orchestration process centrally manages a batch job workflow by breaking it into multiple steps, adding flow logic, and tracking the inputs and outputs between the steps. As your batch jobs run, Step Functions maintains the job's state, tracks exactly which workflow step your batch job is in, and stores an event log of the data that is passed between batch job components. This event log allows your batch job to pick up where it left off if the workflow is interrupted.

#### Step Functions states

![Diagram representing a state machine workflow, consisting of three states.](./images/W11Img040StepFunctionsStates.png)

State machines workflows consist of event-driven states.

Step Functions is based on **state machines** and **tasks**. A state machine defines a series of steps and their transitions. Each step in a state machine is called a **state**. States are referred to by their names, which can be any string, but must be unique within the scope of the entire state machine. Each individual state can make decisions based on its input, perform actions, and pass output to other states.

State machines are interchangeably referred to as workflows, because they direct the flow of operations from one state to the next within the state machine.

Step Functions supports eight different types of states.

##### Task, Choice, and Parallel state types

![Conceptual diagram showing Task, Choice, and Parallel states in state machine workflows.](./images/W11Img042StepFunctionsStatesTaskChoiceParallel.png)

1. **Task state**

    A Task state represents a single unit of work performed by a state machine. Tasks perform all the work in your state machine. A task performs work by using an activity, invoking a Lambda function, or passing parameters to an API for another AWS service.

2. **Choice state**

    A Choice state adds branching logic to a state machine.

3. **Parallel state**

    A Parallel state can be used to create parallel branches of activity in your state machine.

    * **Map, Succeed, and Fail state types**

    ![Conceptual diagram showing Map, Succeed, and Fail states in state machine workflows.](./images/W11Img044StepFunctionsStatesMapSucceedFail.png)

4. **Map state**

    The Map state can be used to run a set of steps for each element of an input array. The Parallel state invokes multiple branches of steps using the same input. But a Map state will invoke the same steps for multiple entries of an array in the state input.

5. **Succeed state**

    A Succeed state stops an activity successfully. The Succeed state is a useful target for Choice state branches that do not do anything except stop the activity. Because Succeed states are terminal states, they have no Next field, and do not need an End field.

6. **Fail state**

    A Fail state stops the activity of the state machine and marks it as a failure, unless it is a caught by a Catch block.

    * **Wait and Pass state types**

    ![Conceptual diagram showing a Wait and a Pass state in state machine workflows.](./images/W11Img046StepFunctionsStatesWaitPass.png)

7. **Wait state**

    A Wait state delays the machine from continuing for a specified time. You can choose either a relative time, specified in seconds from when the state begins, or an absolute end time, specified as a timestamp.

8. **Pass state**

    A Pass state passes its input to its output, without performing work. Pass states are useful when construction and debugging state machines.

#### Benefits of AWS Step Functions for batch processing

The three use cases in this section help to demonstrate some key benefits that AWS Step Functions provides.

##### Flexibility

The Lambda functions and microservices that are called by AWS Step Functions can be quickly revised when needed. Changes to one Lambda function or microservice does not impact the rest of the workflow. Additionally, the tasks in your workflow can run anywhere, including EC2 instances or containers. Step Functions also allows you to interact with other AWS services as part of state events, in addition to your own functions and microservices.

##### Separation of application logic

AWS Step Functions keeps your application logic strictly separated from the implementation of your application. You can add, move, swap, and reorder steps without having to make changes to your business logic. Through this separation, your workflows gain modularity, simplified maintenance, scalability, and reuse of code.

##### Alignment with Well-Architected Framework

The two use cases that include Parallel and Map state events automatically start sub-workflows to perform the required processing steps. This dynamic parallelism is a key capability of AWS Step Functions, and helps to deliver on two of the objectives of the Well-Architected Framework:

* **Performance efficiency** – By automatically scaling resources, dynamic parallelism helps optimize resource usage, which can lead to cost savings.
* **Scalability** – Dynamically adding and removing resources allows applications to handle changing workloads efficiently, ensuring consistent performance.

#### Creating and using a Step Functions state machine

In this demonstration, you learn how to create an AWS Step Functions state machine using the AWS Step Functions Workflow Studio. For the most up-to-date information on this topic, see [What Is Step Functions?](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)

In this scenario, the state machine will model the functionality of a donut shop that receives and processes donut orders for customer delivery.

Each donut order will be for a particular type and quantity of donut. The state machine must check the inventory, and if the ordered donut is available in the quantity requested, process the payment for the order.

* Go to the AWS Services console, and select Step Functions.

![AWS Services console.](./images/W11Img050StepFunctionsAwsConsole.png)

* Now select **Create State Machine** and, for this demo, use the **Design your workflow visually** option.

![AWS Step Functions Create State Machine.](./images/W11Img052StepFunctionsCreateStateMachine.png)

* Leave the **Type** set to **Standard** and choose **Next**.

![AWS Step Functions Create State Machine: Choose Type.](./images/W11Img054StepFunctionsStateMachineAuthoringMethod.png)

* Here is the visual workflow using **Workflow Studio**. With Workflow Studio, you can build a workflow by dragging and dropping in the tasks you need.

![AWS Step Functions Create State Machine Workflow Studio.](./images/W11Img056StepFunctionsStateMachineDesignWorkflow.png)

* You can delete the **HelloWorld** task.

* The first step for this demo workflow is to get an item from a donut database, to verify that the incoming order can be obtained from inventory. You can scroll down to find the Amazon DynamoDB GetItem object on the left, and drag it into the workflow. The pane on the right is where you enter the specific data for this database call.

![AWS Step Functions Create State Machine: Add DynamoDB.](./images/W11Img058StepFunctionsStateMachineDesignWorkflowDynamoDb.png)

* A DynamoDB table called **DonutInventory** has already been created and populated with items. In the pane on the right, you can replace the default text in the parameters pane with the names of the actual table, primary key, and the value you are looking for.

![AWS Step Functions Create State Machine: DynamoDB GetItem.](./images/W11Img060StepFunctionsStateMachineDesignWorkflowDynamoDbEdit.png)

* This table has a primary key of **DonutName**. The value itself will come from the workflow input. You can reference values that are passed into Step Functions by adding the dollar sign character in the appropriate place. For this request, it is a string value that will come from the input, and you must reference the particular variable from the incoming JSON.

* You need to add the original order data to the output of the DynamoDB item information so that a later task can read all of it.

![AWS Step Functions Create State Machine: DynamoDB GetItem Output.](./images/W11Img062StepFunctionsStateMachineDesignWorkflowDynamoDbOutput.png)

* To do this, select the Output tab and then choose the Add original input to output using **ResultPath** option. When choosing this option, the task will pass on the original input and add the result of the **GetItem** call as a new item within the larger JSON structure. You must name this added item. For this demo, DynamoDB is the string used to show that it is the result of the DynamoDB action.

![AWS Step Functions Create State Machine: DynamoDB GetItem Output configuration.](./images/W11Img064StepFunctionsStateMachineDesignWorkflowDynamoDbOutputEdit.png)

* It is always a good practice to add an error handling mechanism to tasks in case errors occur. For this demo, select the **Error handling** tab and select the **Add new catcher** button. Then choose the Errors entry and choose the generic **States.ALL** error. This will add a single catcher that will cover all errors that might come from the task. For the **Fallback** state, select the **Add new state** option, which will create a new placeholder in the diagram.

![AWS Step Functions Create State Machine: Error Catcher.](./images/W11Img066StepFunctionsStateMachineDesignWorkflowDynamoDbCatchErrors.png)

* For this generic error state, choose the **Flow tab** in the upper left portion of the **Workflow Studio** pane and add the generic **Fail** task. A more robust state machine could have multiple options based on the type of exception, but just use one for now.

![AWS Step Functions Create State Machine: Fail State.](./images/W11Img068StepFunctionsStateMachineDesignWorkflowFailState.png)

* The next step is to add an **AWS Lambda function** that will both verify that inventory exists, to supply the order, and process the payment. This Lambda function, called **CheckDonutPayment**, was created earlier. Note that it contains separate error conditions to return to the state functions call. One condition is for when the function failed because there is insufficient inventory, and one condition is for when the payment failed.

![AWS Step Functions Create State Machine: Add Lambda Function.](./images/W11Img070StepFunctionsStateMachineDesignWorkflowAddLambda.png)

* This simple function reads the values sent on by the Step Functions call through the event object to calculate the total cost for the order. It then compares the order quantity to the inventory as returned by the DynamoDB call. If there is enough inventory, the function will process the payment, although in this simplified function it will just compare the calculated cost to a maximum of 50.
* To add this Lambda function to the workflow, go back to the **Actions** tab and select the **AWS Lambda** task. Insert it into the workflow after the DynamoDB task and it automatically becomes the next state. Now specify the name of the function. When making your selection, the menu will show all of your eligible Lambda functions.

![AWS Step Functions Create State Machine: Lambda Function.](./images/W11Img072StepFunctionsStateMachineDesignWorkflowLambdaInvoke.png)

* The **CheckDonutPayment** Lambda function created unique error classes that can be used by the Step Functions workflow. Select the **Error handling** tab on the right and add three catchers. The first catcher will be for the **NotEnoughInventory** error class. This catcher will be activated when the order is for a quantity of donuts greater than the inventory returned by the DynamoDB call. The second catcher will be for the **NotEnoughFunds** error class. This catcher will be activated when the total cost of the order is greater than 50. Use the exact names of the exception classes created by the Lambda function. The third catcher will be a generic catch for any other types of errors.

![AWS Step Functions Create State Machine: Lambda Function Error Catching.](./images/W11Img074StepFunctionsStateMachineDesignWorkflowLambdaErrorHandling.png)

![AWS Step Functions Create State Machine: Catchers.](./images/W11Img076StepFunctionsStateMachineDesignWorkflowMultipleCatch.png)

* For the rest of this simple demo workflow, add a **Success** state and fill in **Pass** states for the two types of processing failure caught from the Lambda task. Both of these will be considered a fail state for the overall workflow.

![AWS Step Functions Create State Machine: Pass State.](./images/W11Img078StepFunctionsStateMachineDesignWorkflowPass.png)

* It is a good idea to identify the names of states even if they are passing information through and taking no other action.
* To complete this workflow, choose the **Next** button and advance to the code view of the workflow.

![AWS Step Functions Create State Machine: Review Code.](./images/W11Img080StepFunctionsStateMachineDesignWorkflowReview.png)

* Choose the **Next** button again to specify some final settings. Here you must name the state machine. Then you can let the Step Function service create a new AWS Identity and Access Management, or IAM, role to use for this state machine. The service will review the workflow and choose appropriate permissions, and then you can review them here at the bottom of the pane.

![AWS Step Functions Create State Machine Settings.](./images/W11Img082StepFunctionsStateMachineName.png)

* Choose the **Create state machine** button to finish creating the state machine.

![AWS Step Functions Create State Machine.](./images/W11Img084StepFunctionsStateMachineCreate.png)

![AWS Step Functions State Machine created.](./images/W11Img086StepFunctionsStateMachineStartExecutionReady.png)

* Then choose the **Start Execution** button to start the worfklow. You can use the pop-up window to enter the order data needed for the workflow. Follow JSON formatting. For this scenario, enter an order of 25 Glazed donuts, and then choose the Start execution button.

![AWS Step Functions State Machine: Start Execution.](./images/W11Img088StepFunctionsStateMachineStartExecution.png)

* The workflow ran successfully, so there were enough donuts in the inventory and the payment was sufficient.

![AWS Step Functions State Machine: Succeeded Execution.](./images/W11Img090StepFunctionsStateExceutionSucceeded.png)

* Different order inputs should result in different results, such as an order for 500 Chocolate donuts, for which there is not sufficient inventory, or an order for 30 Jelly Bismarck donuts, which are too expensive for the $50 limit specified in the Lambda function.

![AWS Step Functions State Machine: Failed Execution.](./images/W11Img092StepFunctionsStateExceutionFailed.png)

---

#### Orchestrating AWS Batch jobs and Lambda functions with Step Functions

The previous video showed how AWS Lambda functions can be used with a Step Functions state machine to orchestrate the flow of microservice processing tasks. Similarly, this video shows how Lambda functions and Step Functions state machines can be used with the AWS Batch service to perform batch processing. This video will take you through the process of creating a sample project that uses a Step Functions state machine to invoke a Lambda function to do simple preprocessing, then invokes multiple AWS Batch jobs in parallel using the Map state.

A sample state machine created using AWS Step Functions is to invoke an AWS Lambda function for pre-processing of inputs. After pre-processing, Step Functions invokes multiple AWS Batch jobs in parallel using the **Map** workflow state.

* To begin, set up a state machine in AWS Step Functions. Open the AWS Management Console, search for `step`,  and then choose `Step Functions` in the search results.

![AWS Management Console Step Functions.](./images/W11Img100AwsConsoleStepFunctions.png)

* On the State Machines console page, choose `Create state machine`.
* Next, you’ll choose a template. Type `fan` in the search box, and choose `Fan out a batch job` in the search results. Choose `Next` to continue.

![AWS Step Functions Choose Template.](./images/W11Img102StepFunctionsFanOutBatchJob.png)

* Here, Step Functions lists the AWS services used in the `Fan out a batch job` template. In the `Choose how to use this template` section, choose `Run a demo`. And then choose `Use template` to continue.

![AWS Step Functions Template Use.](./images/W11Img104StepFunctionsTemplateUse.png))

* This is the **Workflow Studio**. Notice the workflow graph, which shows:

  * A Lambda function
  * An AWS Batch job queue
  * An AWS Step Functions state machine with a **Map** state to Fan-Out AWS Batch jobs, and
  * Related AWS Identity and Access Management, or IAM, roles

![AWS Step Functions State BatchJobFanOut Design.](./images/W11Img106StepFunctionsJobDesign.png)

* At this point, **Workflow Studio** is in `Design mode` and it displays the workflow prototype for the state machine. `Design mode` allows you to visualize the state machine by choosing `Design` or review its Amazon States Language definition by choosing `Code`. Amazon States Language is a JSON-based, structured language used to define a state machine.

![AWS Step Functions State BatchJobFanOut Code.](./images/W11Img108StepFunctionsJobCode.png)

* To see how the batch job is configured, choose the `Submit Batch Job` step in the workflow, and then choose `Code`. This highlights the part of the Amazon States Language definition associated with the `Submit Batch Job` workflow step in the Code editor for the state machine.

![AWS Step Functions State BatchJobFanOut Details.](./images/W11Img110StepFunctionsJobCodeDetails.png)

* To deploy the state machine and create the resources, choose `Deploy and run`. It can take up to 10 minutes for the resources and related IAM permissions to be created. While you wait, you can monitor which resources AWS CloudFormation is provisioning. At the top of the page, in the `Deploying CloudFormation stack` banner, choose the `View in CloudFormation` link.

![AWS Step Functions State BatchJobFanOut Deploying.](./images/W11Img112StepFunctionsJobDeploying.png)

* All the resources for the state machine are now created, and a new window provides an option to execute the newly deployed state machine. Choose `Start execution`.

![AWS Step Functions State BatchJobFanOut Start Execution.](./images/W11Img114StepFunctionsJobStartExecution.png)

* The Step Functions page displays in the console and a message indicates that the execution of the batch job has started successfully. The sample batch job can take 1 to 5 minutes to complete, so the `Status` portion of the page initially displays as `In progress`.

![AWS Step Functions State BatchJobFanOut Execution.](./images/W11Img116StepFunctionsJobExecutionStarted.png)

* When the job completes, the `Status` changes to `Succeeded`.

![AWS Step Functions State BatchJobFanOut Execution Succeeded.](./images/W11Img118StepFunctionsJobExecutionStatus.png)

* You can view details about what happened during the state machine's execution by choosing the `Execution input and output` tab on the state machine. These details include the name of each job, the start and end times of batch tasks, and each job’s log information—among other details.

![AWS Step Functions State BatchJobFanOut Execution Inputs and Outputs.](./images/W11Img120StepFunctionsJobExecutionInputsOutputs.png)

* To access details about a specific stage of the workflow, scroll to the visual representation of the batch job, select one of the workflow stages, and then choose the `Output` tab.

![AWS Step Functions State BatchJobFanOut Execution Output.](./images/W11Img122StepFunctionsJobExecutionOutput.png)

* At the bottom of the state engine page, you can use the `Event view` tab to view the events performed by the batch job. Or, you can choose the `State view` tab to view the states the batch job passed through during processing.

![AWS Step Functions State BatchJobFanOut Execution GraphView.](./images/W11Img124StepFunctionsJobExecutionGraphView.png)

![AWS Step Functions State BatchJobFanOut Execution Table View.](./images/W11Img126StepFunctionsJobExecutionStateTableView.png)

* In the `State view` tab, you can drill into the details of the AWS Batch job that was started during processing. To do this, choose the `Batch job` link. This link takes you to the AWS Batch console page, where you can find general information, as well as specific details, about the job and the container in which the job ran.

![AWS Step Functions State BatchJobFanOut: AWS Batch Job View.](./images/W11Img128AwsBatchJobDetails.png)

---

The example in the video is taken from the [Run an AWS Batch job with Lambda](https://docs.aws.amazon.com/step-functions/latest/dg/sample-batch-lambda.html) section of the AWS documentation. Use the link to view the most up-to-date steps for creating the items shown in the video.

---

### Use Cases: Step Functions for Batch Processing

These three example use cases are provided to show how the eight state machine types can be used to support application workflows.

#### Offering customers a line of credit

An application developer works for a company that sells parts for ocean-going container ships. Most customer orders are for large dollar amounts, so the company grants customers some type of line of credit that the customers can use to defer payment of their order invoices for up to 90 days.

The line of credit amount is determined when the customer places their first order. All customers receive some amount of credit. In some cases, the line of credit might be sufficient to cover the customer's entire order amount, and other times the line of credit might cover only part of the customer's order amount.

When the credit line does not cover the entire order, the customer typically declines the credit line and cancels their order. However, regardless of whether the customer accepts the credit line, an activity report is generated for regulatory purposes to document that a credit line was offered.

The developer is planning to use AWS Step Functions to create an microservice-based approval process for customer credit lines. The credit lines are offered to new customers as part of their initial order with a vendor. The following diagram shows the workflow that the developer is suggesting.

![Conceptual diagram showing a customer credit line approval using AWS Step Functions.](./images/W11Img130StepFunctionsUseCaseCreditApproval.png)

AWS Step Functions workflow for a credit approval process.

The workflow begins with a `Task` state that invokes a microservice to get the total amount of the customer's order from the company's online ordering application. Next, a `Task` state uses a microservice to retrieve information about the customer's creditworthiness from available sources. These sources include credit reporting agencies, public records, and private data aggregation vendors. The next microservice is invoked by a `Task` state to calculate the customer's maximum allowable line of credit based on analysis of the customer's available information.

The next `Task` state uses a microservice to offer the credit line amount to the customer in real time. The customer's decision to accept or decline the offered credit limit is captured by a `Choice` state.

If the customer accepts the offered credit line, the `Choice` state invokes a `Task` state that accepts the line of credit by updating the customer's profile in the online ordering application.

If the customer declines the offered credit line, the `Choice` state invokes a `Task` state that cancels the customer's order.

The final `Task` state invokes a microservice that generates a customer activity report, showing the amount of the credit line that was offered to the customer, and whether or not the customer accepted the credit line. The workflow state machine ends after this final operation.

#### Using parallel processes to load machinery data

The next example of using Step Functions state types to support an application focuses on loading data collected from Internet of Things (IoT) devices. In this scenario, a company uses IoT devices to continuously collecting data from 120 machines in their factory. The devices first collect the data locally, then upload that data to one of three Amazon S3 buckets on an hourly basis. Each bucket contains data files for 40 machines. Each machine uploads ten gigabytes of collected data per hour.

When the IoT data is stored in Amazon S3, it is loaded into a relational database. Then consolidated reports are prepared comparing current, summarized IoT data to historical data from the same period. This report helps the factory managers determine if the factory machines are experiencing any anomalies.

An application architect is planning to use AWS Step Functions to create an microservice-based data loading and reporting process for this IoT data. The following diagram shows the workflow that the architect has proposed.

![Conceptual diagram showing a parallel data load workflow using AWS Step Functions.](./images/W11Img132StepFunctionsUseCaseParallelDataLoad.png)

AWS Step Functions workflow for a data load and report preparation process.

The workflow begins with a `Task` state that invokes a microservice to determine whether the hourly data files have been uploaded to the three Amazon S3 buckets by the factory devices. A Parallel state then invokes one `Task` state for each S3 bucket. These `Task` states load the contents of the data files from each S3 bucket into the relational database.

Following the data load operation, a `Choice` state is used in the workflow to determine whether each prior `Task` state has been completed successfully.

If a prior `Task` state failed with an error, a `Task` state invokes a microservice to stop processing and control passes to a `Fail` state event where processing ends.

If a prior `Task` state to load data has been competed successfully, a subsequent `Task` state calls a microservice that summarizes the data that was loaded to the relational database.

Next, another `Task` state retrieves historical data for the same time period from a data lake. Another `Task` state creates a report that consolidates the summarized data and the historical data collected into a report. A final `Task` state event then emails the report to the company leadership team, ending the workflow.

#### Using dynamic parallelism to process spikes in customer orders

An online retailer is planning to offer a special 3-day-only shopping event where products will be sold at up to 50% off their regular prices.

This special pricing is expected to increase the number of online sales from the typical 5,000 per day to 30,000 per day or more. The retailer is concerned that their shipping application might not be able to handle the expected spike in traffic during the sale.

Specifically, the retailer is concerned that the Step Functions workflow related to shipping orders could have performance issues, which could result in shipping delays. The current shipping microservice workflow begins by receiving a comma separated value (CSV) file from the sales application. The rest of the current shipping workflow is shown in the following diagram.

![Diagram showing data processing workflow using Step Functions with a Choice state event.](./images/W11Img134StepFunctionsUseCaseDynamicParallelism.png)

Shipping process workflow using a Choice state event.

The first step in the shipping workflow is a `Task` state event that confirms that the format of the CSV file is correct. If it is, a `Task` state event loads the contents of the CSV file into an Amazon DynamoDB table. The next `Task` state event reads a record from the DynamoDB table and passes the data to a subsequent `Task` state event to calculate the weight, size, and delivery zone information for that order. When this is complete, the remaining two `Task` state events calculate the cost of shipping the order, and update the sales data to include this shipping cost. Finally, a `Choice` state event checks to see if there are additional orders in the DynamoDB table that require processing. If so, the workflow is repeated for the next order. If not, the workflow ends.

The Task state event that calculates the weight, size, and delivery zone for the order relies on several external, third-party applications to determine the cost to ship the ordered items. Sometimes this event can take up to a minute to complete.

This potential delay and the serial nature of the workflow is almost certainly not going to scale efficiently when orders go from 5,000 per day to the expected 30,000 per day.

To avoid any problems related to the shipping calculations during the sale, a developer has proposed a new microservice workflow that uses a `Map` state event in place of the existing workflow.

With `Map` states in Step Functions, you can run a set of tasks in parallel for each element of an array. When the `Map` state is encountered, the workflow will iterate over the array and execute the specified tasks for each record in the array, potentially in parallel. `Map` states can iterate over a set of records in a CSV file by first converting the CSV data into an array. The resulting output of the `Map` state would be an array containing the outputs of each individual iteration, ordered in the same sequence as the original input array. In this workflow, the output of the `Map` state would be an array of order numbers, with each order's associated shipping cost. The developer's proposed new workflow is shown in the following diagram.

![Diagram showing a processing workflow using Step Functions with a Map state event.](./images/W11Img134StepFunctionsUseCaseDynamicParallelismMapState.png)

Proposed shipping process workflow using a Map state event.

In this workflow, the `Map` state event reads the entire CSV file into an array after the previous `Task` state event has confirmed that the CSV file is in the proper format. Then the `Map` state iterates through the array file, launching each of the sub-workflows for each order record in the array. These processes can run in parallel until completion. When all sub-workflows are complete, the `Map` state will return an array containing the output for each item processed by the Iterator. This array can be used by the last `Task` state event to update the sales data with the calculated shipping cost, after which the workflow ends.

```text
You can configure an upper limit on how many parallel sub-workflows a Map task event can start. The default value is zero, which places no limit on parallelism and iterations are invoked as concurrently as possible.
```

---

### Knowledge Check

#### A developer is designing a microservice that sends monthly billing statements for printing. There are ten printers available to print the billing statements. The developer wants to start ten parallel processes to print the statements, each with an equal number of statements. Which batch processing model is this an example of?

* Fan-out

Wrong answers:

* Fan-in
* Dynamic parallelism
* Load balanced

##### Explanation

**Fan-out** type of batch processing creates a batch job based on a fixed number of parallel tasks.

The other options are incorrect because:

* Fan-in is the process of combining multiple separate batch processes into one result.
* The approach described uses a fixed number of processes, which is not consistent with dynamic parallelism processing.
* Load balancing is also a dynamic activity, which is typically applied at the instance level, not the microservice level.

#### Which AWS services are frequently used to support batch processing in microservice applications? (Select THREE.)

* Amazon Elastic Container Service (Amazon ECS)
* AWS Step Functions
* AWS Lambda

Wrong answers:

* Elastic Load Balancing
* Amazon API Gateway
* Amazon CloudFront

##### Explanation

**Amazon ECS**, **Step Functions**, and **Lambda** services are architected specifically to run batch processing for microservice applications.

The other options are incorrect because:

* Elastic Load Balancing adds or removes resources at the instance level, not the container or microservice level.
* API Gateway is not a batch processing service.
* CloudFront is not a batch processing service.

#### Which statement about AWS Step Functions state machines is correct?

* State machines are called workflows, which consist of a series of event-driven steps.

Wrong answers:

* Each event-driven step is called a machine.
* State machines are called events, which consist of a series of workflow-driven steps.
* Each event-driven step is called a workflow.

##### Explanation

Each event-driven step is called a state.

The other options are incorrect because those responses are incorrect definitions of both state machines and states.

#### A developer has created an AWS Step Functions workflow that has a state that iteratively reads customer data from a comma separated value (CSV) file. Each time that a value is read from the CSV file, the total sales, gross margin, and profit generated by that customer is calculated. Which type of state event is this an example of?

* Map state event

Wrong answers:

* Parallel state event
* Choice state event
* Task state event

##### Explanation

Map state events iterate on an array of data and perform the same subsequent processing on each item. Parallel processes can be created if needed.

The other options are incorrect because:

* Parallel state events allow two or more subsequent states to run concurrently.
* Choice state events pass control to subsequent states based on the result of an evaluation condition.
* Task state events perform an activity, run an AWS Lambda function, or call an API to an AWS service.

#### A microservice application is using AWS Step Functions. An inventory microservice sometimes fails due to short delays transmitting data between handheld scanners in the warehouse and the inventory application in the AWS Cloud. Which two state events could be used to suspend processing for 2 minutes before rerunning the inventory microservice again? (Select TWO.)

* Fail state event
* Wait state event

Wrong answers:

* Parallel state event
* Succeed state event
* Pass state event

##### Explanation

The `Fail` state event can be raised to acknowledge the process failure, and the `Wait` state event can be used to pause processing for 2 minutes before retrying the failed process.

The other options are incorrect because:

* The Parallel state event is used to run multiple processes concurrently.
* The Succeed state event is used when preceding processes work correctly.
* The Pass state event does nothing except pass a value through to a subsequent state.

---

### Summary

Applications that must perform the same operation on a lot of data are generally more efficient when those operations are broken down into one or more batch processing jobs.

#### Batch processing

`Batch processing` aligns with the operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability pillars of the AWS Well-Architected Framework.

Flexibility and separation of application logic from the application implementation are also key benefits of batch processing models.

The `fan-out pattern` is a parallel processing model where a single input is divided into multiple smaller tasks, which are then processed concurrently by multiple workers or services. The `dynamic parallelism` pattern is an extension of the fan-out pattern, where the number of parallel tasks is not fixed but can dynamically adjust based on the input data or the available resources.

The `fan-in` pattern is the complementary pattern to the `fan-out` pattern. It is used to consolidate the results of multiple parallel tasks into a single output or result.

##### AWS Services for Batch processing

Popular AWS services for implementing batch processing patterns include `AWS Step Functions`, `AWS Lambda`, `Amazon EMR`, `Amazon Elastic Kubernetes Service (Amazon EKS)`, and `Amazon Elastic Container Service (Amazon ECS)`.

`AWS Batch` is a service that is purpose-built for defining, scheduling, monitoring, and logging batch processing jobs.

`AWS Step Functions` offers eight state event types than can be useful for batch processing jobs. These include `Task`, `Choice`, `Parallel`, `Map`, `Succeed`, `Fail`, `Wait`, and `Pass` state events.

`Choice` state events take an action based on the results of a previous state. `Parallel` state events start a fixed number of subsequent states that concurrently perform processing tasks. Map state events iterate on an array of inputs, starting one or more parallel subsequent states to perform processing tasks.

The AWS Management Console can be used to create combinations of AWS Step Functions workflows, AWS Batch jobs, and AWS Lambda functions to perform batch processing for applications.

---

## DESIGNING A REAL-TIME PROCESSING APPLICATION ARCHITECTURE

---

### Lab Environment: Navigating Through Kinesis

---

### Real-Time Processing Architectures

### Implementing Real-Time Processing with AWS

### Use Cases: Using AWS Services for Real-Time Processing

### Kinesis Data Streams and OpenSearch Service

---

### Lab: Navigating Through Kinesis

---

### Real-Time Data Storage Options

### Evaluating Storage Options

### Activity: Selecting the Appropriate Storage Option

---

### Knowledge Check

---

### Summary

---

### Additional Resources

---
