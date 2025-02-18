# Week 7: Deploying a Django Web Application to AWS Elastic Beanstalk

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to repo's main [README.md](../../../README.md)

## Deploying a Django Web Application

### Pre-assessment

#### Which task should you complete before you deploy your web application to AWS Elastic Beanstalk?

* Test your website locally or on an AWS supported IDE

Wrong answers:

* Manually deploy your compute resources
* Package the application into a Docker image
* Install Python on an Amazon EC2 instance

It's important to set up a development environment for local testing of applications before deploying them to AWS Elastic Beanstalk. Some integrations with AWS storage and database services can be performed.

#### What is the AWS Elastic Beanstalk command line interface (CLI) used for?

* Creating, configuring, and managing AWS Elastic Beanstalk environments

Wrong answers:

* Managing and configuring the underlying Amazon EC2 instances
* Replacing the AWS CLI tool for managing AWS services
* Building and running serverless applications on AWS

With the Elastic Beanstalk CLI, you can create, configure, and manage Elastic Beanstalk environments, including deploying applications, viewing logs, and managing environment settings.

#### Which AWS service can be used to store Django media files provided by users persistently and in the most efficient manner?

* Amazon S3

Wrong answers:

* Amazon RDS
* Amazon ElastiCache
* Amazon Elastic Block Store (Amazon EBS)

##### Explanation

* Media files can be stored on an object storage service, such as Amazon S3, that is decoupled from the Django application instances.
* Amazon RDS is a relational database that is not suited for binary data.
* Amazon ElastiCache is used as an in-memory data store for quick access.
* Amazon EBS is a block storage service. Block volumes are attached to the Amazon EC2 instances. These volumes are not shared between instances.

## Moving from Development to Production

Working within a development environment is necessary to code, build, and test your Django project in a safe, nonproduction area.
