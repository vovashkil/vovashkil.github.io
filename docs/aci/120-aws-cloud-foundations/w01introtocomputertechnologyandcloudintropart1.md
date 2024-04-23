###### back to AWS Cloud Institute repo's root [aci.md](../aci.md)
###### back to repo's main [README.md](../../../README.md)
# Intro to Computer Technology and Cloud Intro Part 1
## Introduction to Computer Technology
## Introduction: Virtualization
### Ways to use virtualization
1. Server virtualization
2. Network virtualization 
3. Data virtualization
4. Desktop virtualization
5. Storage virtualization
6. Application virtualization

#### Server virtualization
Server virtualization is a process that partitions a physical server into multiple virtual servers. It is an efficient and cost-effective way to use server resources and deploy IT services in an organization. Without server virtualization, physical servers use only a small amount of their processing capacities, which leave devices idle.

#### Network virtualization
Computer networks use hardware elements such as switches, routers, and firewalls. An organization with offices in multiple geographic locations can have several different network technologies working together to create its enterprise network. Network virtualization is a process that combines all of these network resources to centralize administrative tasks. Administrators can adjust and control these elements virtually without touching the physical components, which greatly simplifies network management.

#### Data virtualization
Modern organizations collect data from several sources and store it in different formats. They might also store data in different places, such as in a cloud infrastructure and an on-premises data center. Data virtualization creates a software layer between this data and the applications that need it. Data virtualization tools process an application’s data request and return results in a suitable format. Thus, organizations use data virtualization solutions to increase flexibility for data integration and support cross-functional data analysis

#### Desktop virtualization
Most organizations have non-technical staff that use desktop operating systems to run common business applications. For instance, you might have the following staff:
* A customer service team that requires a desktop computer with Windows 10 and customer-relationship management software.
* A marketing team that requires Windows Vista for special sales applications.

You can use desktop virtualization to run these different desktop operating systems on virtual machines, which your teams can access remotely. This type of virtualization makes desktop management efficient and secure, and saves you money on desktop hardware. The following are types of desktop virtualization:
* Virtual desktop infrastructure: runs virtual desktops on a remote server. Your users can access them by using client devices.
* Local desktop virtualization: you run the hypervisor on a local computer and create a virtual computer with a different operating system. You can switch between your local and virtual environment in the same way you can switch between applications. 

#### Storage virtualization
Storage virtualization combines the functions of physical storage devices such as network attached storage (NAS) and storage area network (SAN). You can pool the storage hardware in your data center, even if it is from different vendors or of different types. Storage virtualization uses all your physical data storage and creates a large unit of virtual storage that you can assign and control by using management software. IT administrators can streamline storage activities, such as archiving, backup, and recovery, because they can combine multiple network storage devices virtually into a single storage device.

#### Application virtualization
Application virtualization pulls out the functions of applications to run on operating systems other than the operating systems for which they were designed. For example, users can run a Microsoft Windows application on a macOS device without changing configurations. 

### Containers
Containerization is a type of application virtualization. Containers share an operating system installed on the server and run as a resource-isolated process. This ensures quick, reliable, and consistent deployments, regardless of environment. Containers are a powerful way for developers to package and deploy their applications. They are lightweight and provide a consistent, portable software environment for applications to easily run and scale anywhere.

### Summary
Virtualization uses specialized software, called a hypervisor, to create several cloud instances or virtual machines on one physical computer.

## Basic IT infrastructure
### Three-tier architectur of Web services
#### Presentation tier
The presentation tier generally includes a web server, and provides a user interface. The content can be static or dynamic, and is usually developed using HTML, CSS and Javascript. 

#### Application tier
The application tier stores the business logic used to process user inputs. This layer is often developed using languages such as Python, Ruby, or PHP on a server.

#### Data tier
The data tier runs on a database where the web application stores or accesses data . You can use management software, such as MySQL, Oracle, DB2 or PostgreSQL, for example, to manage the database.

## Module Summary
### Computers
In this topic, you learned about the core components of a computer and how it collects input and produces a desired output. You also learned the basics of data measurement and sizes like bit, byte, and kilobyte and how that data is stored on computers.

### Security
The security topic provided you with the information needed to differentiate between authentication and authorization. Additionally, you learned about data encryption on the internet.

### Networking
The networking topic provided you with the basics of the OSI model, how communication occurs on a network, and networking devices.

### Virtualization
In this topic, you learned about how virtualization makes it so a computer can share its hardware resources and the six types of virtualization. This topic also covered containerization which is a type of application virtualization. 

### IT infrastructure
In this topic you learned about legacy IT infrastructure, including servers and data centers. This topic also provided an overview of the three-tier architecture and how it is used for web applications.

## Cloud Computing
Cloud computing is the on-demand delivery of IT resources with pay-as-you-go pricing.

### Glossary
1. Differentiator
A differentiator is a characteristic of a business that separates them from key competitors and gives them a perceived advantage in the eyes of their target audience.
2. Latency
Latency is the time that passes between a user request and the resulting response.
Low latency is better than high latency.

### Benefits of cloud computing
1. Trade upfront expense for variable expense
Upfront expense refers to data centers, physical servers, and other resources that you would need to invest in before using them. Variable expense means you only pay for computing resources you consume, instead of investing heavily in data centers and servers before you know how you’re going to use them.

By taking a cloud-computing approach that offers the benefit of variable expense, companies can implement innovative solutions while saving on costs.

2. Stop spending money to run and maintain data centers
Computing in data centers often requires you to spend more money and time managing infrastructure and servers. 

A benefit of cloud computing is the ability to focus less on these tasks and more on your applications and customers.

3. Stop guessing capacity
With cloud computing, you don’t have to predict how much infrastructure capacity you will need before deploying an application. 

For example, you can launch Amazon EC2 instances when needed, and pay only for the compute time you use. Instead of paying for unused resources or having to deal with limited capacity, you can access only the capacity that you need. You can also scale in or scale out in response to demand.

4. Benefit from massive economies of scale
By using cloud computing, you can achieve a lower variable cost than you can get on your own.

Because usage from hundreds of thousands of customers can aggregate in the cloud, providers such as AWS can achieve higher economies of scale. The economy of scale translates into lower pay-as-you-go prices. 

5. Increase speed and agility
In a cloud-computing environment, new IT resources are only a click away, which means that you reduce the time to make those resources available to your developers from weeks to just minutes. 

This results in a dramatic increase in agility for the organization, since the cost and time it takes to experiment and develop is significantly lower. 

6. Go global in minutes
The global footprint of the AWS Cloud enables you to deploy applications to customers around the world quickly, while providing them with low latency. This means that even if you are located in a different part of the world than your customers, customers are able to access your applications with minimal delays. 

Later in this module, you will explore the AWS global infrastructure in greater detail. You will examine some of the services that you can use to deliver content to customers around the world.

7. Democratize advanced technologies
AWS offers services that seek to democratize (make it easy to use or understand) advanced technologies. An example of this is machine learning. Currently, there are few experts in machine learning, so AWS created the Amazon SageMaker service. 

Amazon SageMaker was designed as a fully managed service that removes the complexity and guesswork from each step of the machine-learning process. This makes it so everyday developers and scientists can successfully use machine learning to perform analyses. 

With AWS, a start-up business in someone's home has access to the same infrastructure and power as a large-scale enterprise company.

### AWS Cloud Adoption Framework (AWS CAF)
AWS CAF provides guidance and best practices to help organizations identify gaps in skills and processes. It also helps organizations build a comprehensive approach to cloud computing—both across the organization and throughout the IT lifecycle—to accelerate successful cloud adoption. 

#### Transformation value chain
The Transformation value chain refers to the process of identifying and optimizing key activities and processes to create and deliver value to customers, stakeholders, and the organization. 

At the top of the diagram below, are the transformation domains. These are the areas where business outcomes are accelerated through cloud-powered organizational change. Change in these areas helps drive the key business outcomes, which are shown at the far right in the diagram: reduced business risk; improved environmental, social, and governance (ESG) performance; and increased revenue and operational efficiency.

#### Foundational capabilities
Each of the transformation domains is enabled by a set of foundational capabilities. A capability is a business's ability to use processes to deploy resources (for example, people, technology, and any other tangible or intangible assets) to achieve an outcome. AWS CAF capabilities provide best-practice guidance to help businesses improve their cloud readiness. AWS groups these capabilities into six perspectives, which are shown in the diagram.

#### Transformation Domains
##### Technological transformation
This transformation focuses on using the cloud to migrate and modernize old IT infrastructure, applications, and data and analytics platforms. Cloud Value Benchmarking shows that migrating from on-premise solutions to AWS leads to a 27% reduction in cost-per-user, a 58% increase in virtual machines managed per admin, a 57% decrease in downtime, and a 34% decrease in security events.

##### Process transformation
This transformation focuses on digitizing, automating, and optimizing business operations. This may include leveraging new data and analytics platforms to create actionable insights or using machine learning to improve things like the customer service experience, employee productivity, business forecasting, and fraud detection and prevention. Process transformations can improve operational efficiency while also lowering operating costs and improving the employee and customer experience.

##### Organization transformation
This transformation focuses on reimagining a company's operating model—how the business and technology teams work together to create customer value and meet their strategic goals.

##### Product transformation
This transformation focuses on reimagining business models by creating new value propositions and revenue models. Doing this may help a company reach new customers and enter new market segments. Cloud Value Benchmarking shows that adopting AWS leads to a 37% reduction in time-to-market for new features and applications, a 342% increase in code deployment frequency, and a 38% reduction in the time to deploy new code.

##### Business perspective
The business perspective helps ensure that cloud investments accelerate a company's digital transformation ambitions and business outcomes. Common stakeholders include chief executive officer, chief financial officer, chief operations officer, chief information officer, and chief technology officer. People in these positions are often concerned with a business's performance in the following capabilities:
* Strategy Management 
* Portfolio Management 
* Innovation Management 
* Product Management 
* Strategic Partnership 
* Data Monetization 
* Business Insight 
* Data Science

##### People perspective
The people perspective is the bridge between technology and business. The people have a goal to move a business forward with a culture of continuous growth, which means consistently learning from past outcomes and then enacting change based on those findings. Common stakeholders include chief information officer, chief operating officer, chief technology officer, cloud director, and cross-functional and enterprise-wide leaders. These people are concerned with a business's ability to perform the following capabilities: 
* Culture Evolution 
* Transformational Leadership 
* Cloud Fluency 
* Workforce Transformation 
* Change Acceleration 
* Organization Design 
* Organizational Alignment

##### Governance perspective
The governance perspective helps businesses organize cloud initiatives while maximizing organizational benefits and minimizing transformation-related risks. Common stakeholders include chief transformation officer, chief information officer, chief technology officer, chief financial officer, chief data officer, and chief risk officer. They are concerned with a business's ability to perform the following capabilities:
* Program and Project Management 
* Benefits Management 
* Risk Management 
* Cloud Financial Management
* Application Portfolio Management 
* Data Governance 
* Data Curation

##### The platform perspective helps businesses build an enterprise-grade, scalable, hybrid cloud platform, modernize existing workloads, and implement new cloud-native solutions. Common stakeholders include chief technology officer, technology leaders, architects, and engineers. They are concerned with a business's performance in the following capabilities: 
* Platform Architecture 
* Data Architecture 
* Platform Engineering 
* Data Engineering 
* Provisioning and Orchestration 
* Modern Application Development 
* Continuous Integration and Continuous Delivery

##### Security perspective
The security perspective helps a company achieve the confidentiality, integrity, and availability of data and cloud workloads. Common stakeholders include chief information security officer, chief compliance officer, internal audit leaders, and security architects and engineers. They are concerned with a business's performance in the following capabilities:
* Security Governance 
* Security Assurance 
* Identity and Access Management 
* Threat Detection 
* Vulnerability Management 
* Infrastructure Protection 
* Data Protection 
* Application Security 
* Incident Response

##### Operations perspective
The operations perspective helps ensure that cloud services are delivered at a level that meets the needs of a business. Common stakeholders include infrastructure and operations leaders, site reliability engineers,  and information technology service managers. People in these positions are often concerned with a business's ability to perform the following capabilities:
* Observability - evaluating the current state of a business 
* Event Management 
* Incident and Problem Management
* Change and Release Management 
* Performance and Capacity Management 
* Configuration Management 
* Patch Management 
* Availability and Continuity Management 
* Application Management

#### Cloud transformation journey
Each organization’s cloud adoption journey is unique. However, for any organization to successfully migrate its IT portfolio to the cloud, three elements must be in alignment (**people**, **process**, and **technology**). Business and technology leaders in an organization must understand the organization’s current state, the target state, and the transition needed to achieve the target state. This allows them to set goals and create processes for their staff. The AWS CAF recommends four iterative and incremental cloud transformation phases. 

##### Envision phase
This phase focuses on demonstrating how the cloud will help accelerate your business outcomes. It does this by identifying and prioritizing transformation opportunities across each of the four transformation domains to align with your strategic business objectives.

##### Align phase
This phase focuses on identifying capability gaps across the six AWS CAF perspectives, identifying cross-organizational dependencies, and surfacing stakeholder concerns and challenges.

###### Launch phase
This phase focuses on delivering pilot initiatives in production and on demonstrating incremental business value. Pilots should be highly impactful; if successful they will help influence future direction. Learning from pilots will help you adjust your approach before scaling to full production. 

###### Scale phase
This phase focuses on expanding production pilots and business value to desired scale and ensuring that the business benefits associated with your cloud investments are realized and sustained. 

### Three cloud service models
#### Infrastructure as a service (IaaS)
IaaS gives you the basic building blocks for cloud IT. It provides access to networking features, computers, and data-storage space. 
#### Platform as a service (PaaS)
PaaS removes the need to manage basic underlying infrastructure, such as hardware and operating systems. 

#### Software as a service (SaaS)
SaaS give you a ready-to-use product that is run and managed by a provider.

### Three types of cloud computing deployment
#### CLOUD-BASED DEPLOYMENT
* Run all parts of the application in the cloud.
* Migrate existing applications to the cloud.
* Design and build new applications in the cloud.

In a **cloud-based deployment** model, you can migrate existing applications to the cloud, or you can design and build new applications in the cloud. You can build those applications on low-level infrastructure that requires your IT staff to manage them. Alternatively, you can build them using higher-level services that reduce the management, architecting, and scaling requirements of the core infrastructure.

For example, a company might create an application consisting of virtual servers, databases, and networking components that are fully based in the cloud.

#### HYBRID DEPLOYMENT
* Connect cloud-based resources to on-premises infrastructure.
* Integrate cloud-based resources with legacy IT applications.

In a **hybrid deployment** model, cloud-based resources are connected to on-premises infrastructure. For example, you might want to use this approach if you have legacy applications that are better maintained on premises, or government regulations require your business to keep certain records on premises.

For example, suppose that a company wants to use cloud services that can automate batch data processing and analytics. However, the company has several legacy applications that are more suitable on premises, and will not be migrated to the cloud. With a hybrid deployment, the company can keep the legacy applications on premises, while benefiting from the data and analytics services that run in the cloud.

#### ON-PREMISES DEPLOYMENT
* Deploy resources by using virtualization and resource management tools.
* Increase resource utilization by using application management and virtualization technologies.

**On-premises deployment** is also known as a private cloud deployment. In this model, resources are deployed on premises by using virtualization and resource management tools.

For example, you might have applications that run on technology that is fully kept in your on-premises data center. Though this model is much like legacy IT infrastructure, its incorporation of application management and virtualization technologies helps to increase resource utilization.

### Shared responsibility model
Regardless of deployment model, security is handled by both the customer and AWS using what is called the shared responsibility model. In this model, AWS is responsible for the security of the cloud, while the customer is responsible for securing what is in the cloud.

You can think of this model as being similar to the division of responsibilities between a homeowner and a homebuilder. The builder (AWS) is responsible for constructing your house and ensuring that it is solidly built. It is the responsibility of the homeowner (the customer) to secure everything in the house by ensuring that the doors are closed and locked.

## Summary
### What is cloud computing?
Cloud computing is the on-demand delivery of IT resources over the Internet with pay-as-you-go pricing. Instead of buying, owning, and maintaining physical data centers and servers, you can access technology services, such as computing power, storage, and databases, on an as-needed basis from a cloud provider.

### Why do organizations use cloud computing?
* To trade upfront expense for variable expense, and pay only when you need to.
* To stop spending money on building and maintaining data centers.
* To no longer have to guess capacity and risk under- or over-buying resources.
* To benefit from being one of many customers, and using the economy of scale.
* To help free up resources, and decrease your time-to-market.
* To go global in minutes ,and deploy low-latency applications quickly.
* To help decrease the time-to-productivity in hard-to-learn technologies.

### How is cloud computing implemented?
### Cloud service models
#### Infrastructure as a service (IaaS)
Infrastructure as a service gives you the basic building blocks for cloud IT. It provides access to networking features, computers, and data storage space. 

#### Platform as a service (PaaS)
Platform as a service removes the need to manage basic underlying infrastructure, such as hardware and operating systems. 

#### Software as a service (SaaS)
Software as a service gives you a ready-to-use product that is run and managed by a provider. 

### Cloud deployment models
#### Cloud-based deployment
In a cloud-based deployment model, you can migrate existing applications to the cloud, or you can design and build new applications in the cloud. 

#### Hybrid deployment
In a hybrid deployment model, cloud-based resources are connected to an on-premises infrastructure.

#### On-premises deployment
In an on-premises deployment model, resources are deployed on premises by using virtualization and resource management tools.

### The AWS Cloud Adoption Framework
The AWS CAF is based on AWS's experience and best practices. The goal is to help businesses accelerate their outcomes through innovative uses of AWS. It focuses on creating transformation in the following areas:
* Technology
* Process
* Organization
* Product

Using the AWS CAF can accelerate digital transformation in businesses through cloud technology and help reduce business risk; improve environmental, social, and governance performance; and increase revenue and operational efficiency.

These transformations are made possible by capabilities (a business's ability to use processes to deploy resources to achieve an outcome) in six areas, called perspectives. Each perspective has its own set of stakeholders, which occasionally overlap. These perspectives are:
* Business
* People
* Governance
* Platform
* Security
* Operations

#### The AWS CAF recommends four iterative and incremental cloud-transformation phases. 
1. **Envision phasei**: focuses on demonstrating how the cloud will help accelerate your business outcomes. 
2. **Align phase**: focuses on identifying capability gaps across the six AWS CAF perspectives, identifying cross-organizational dependencies, and surfacing stakeholder concerns and challenges. 
3. **Launch phase**: focuses on delivering pilot initiatives in production, and on demonstrating incremental business value. 
4. **Scale phase**: focuses on expanding production pilots and business value to desired scale.
