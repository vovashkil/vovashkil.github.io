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

### Source development environment

When you are using an IDE within AWS, you edit the source code locally on a single Amazon Elastic Compute Cloud (Amazon EC2) instance. You test the Django application on a lightweight web server, and the test data is stored in an SQLite database file.

Client < - > django Lightweight development web server < - > django application

This environment is not meant to be accessed by end users, so it is not public. It does not scale, because it is running on a single instance, and it uses a file-based database stored on the instance.

### Target production environment

When a Django application has been coded and tested locally from your IDE, you can plan how to deploy it to a production environment. A proper production architecture on AWS should follow the design principles and best practices defined in the AWS Well-Architected Framework. The framework covers different aspects of the architecture, known as pillars, including security and reliability. To learn more, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

You can start by defining some requirements for your Django application in production.

* The web application must be exposed to the internet, be highly available, and scale to hundreds or thousands of simultaneous end users.
* The application data, like vet visits, must be stored in a separate managed database that can handle high numbers of reads and writes.
* The application media files, like pet pictures, must be stored and managed in a separate, secure storage area.
* From a maintenance point of view, it should be easy to deploy the application and redeploy changes. It should be easy to manage the compute instances and the database.

This translates into several AWS services that you can use.

For the application to handle many simultaneous users, you need to run the application behind a load balancer with several Amazon EC2 instances. The number of instances should adjust automatically based on how many users are currently interacting with the website. Auto scaling is a feature of Amazon EC2 that can be managed by AWS Elastic Beanstalk.

Because the application is running on multiple instances, the application data cannot reside in an SQLite file on each instance. This would result in inconsistency because nothing would synchronize these files. In addition, the user sessions would not be shared between the instances. This would cause the application to malfunction if consecutive requests for the same user were managed by different servers.

As a consequence, the data has to be stored on an external Django compatible database. Amazon RDS is a managed relational database service that offers operational benefits. To improve performance, some data, like user sessions, can be cached in memory instead of being persisted in a database. This can be achieved by using Amazon ElastiCache, a fully managed in-memory data store and cache service.

Because the database is not the best place to store binary data, pictures and other media files can be stored on a cloud object storage area provided by Amazon S3. The pictures can be protected by using temporary links in the web application that expire.

All of the AWS services mentioned are either serverless or managed services. They provide clear operational advantages to let you focus on the application instead of the infrastructure.

### Path to a full deployment

A Django application can be configured to integrate with an external database, an external object storage area, and an external in-memory data store. Testing such integrations can be done from the test environment. The strategy is to start by applying these changes in your IDE first, before deploying the Django application to Elastic Beanstalk.

The following are the four steps, starting with three integration steps and the resulting test architecture. The last step is about deploying the Django application to Elastic Beanstalk and showing you the final production architecture.

1. **Amazon S3 integration** – An Amazon S3 bucket is created for your application. Django storage is reconfigured from local storage to point to the bucket. Some media files might have to be uploaded to Amazon S3. The Django application is run in your IDE to verify that the pictures are now served from Amazon S3.
2. **Amazon ElastiCache integration** – An ElastiCache cache is created for your application. The Django session framework is reconfigured from using a database to point to the cache. The Django application is run in your IDE to verify that everything is working.
3. **Amazon RDS integration** – An Amazon RDS database is created for your application. The Django database is reconfigured from SQLite to point to the Amazon RDS database. The Django command line interface (CLI) is used to migrate the database. Some data might have to be loaded as well. The Django application runs in your IDE to verify that everything is working and that new data is saved in Amazon RDS.
4. **AWS Elastic Beanstalk deployment** – An Elastic Beanstalk application and environment are created. The Django application is prepared and deployed to the Elastic Beanstalk environment. The environment public URL is used to access the website.

The end result is the target production environment. The Django application is deployed and managed by Elastic Beanstalk. It runs on EC2 instances, abstracted away by Elastic Beanstalk. The application integrates with Amazon S3 for storing pictures, Amazon RDS for application data, and ElastiCache for user sessions.

## Using Amazon S3 for Media Files

Amazon Simple Storage Service (Amazon S3) provides scalable object storage. A Django application's media files can be uploaded and downloaded from an Amazon S3 bucket.

### Django application files

A Django website might use different types of files. Only some types are good candidates for object storage on Amazon S3.

* **Static files** – Your Django application includes webpage templates that use static content in the form of Cascading Style Sheets (CSS) files, JavaScript files, and pictures like the application logo and header background. These files are called *static files* and they reside along with the HTML template code. They are edited and redeployed together with the templates, and are placed locally in the application folder. To learn more, see [How to Manage Static Files](https://docs.djangoproject.com/en/stable/howto/static-files/) in the Django documentation.
* **Media files** – Your application might let end users upload photos, like a profile picture. The application might also display photos, like a pet picture. These user files are called *media files* and they do not reside with the application because they are updated continuously by users. They are not static. Media files require a storage area decoupled from the application. Because databases are not appropriate for binary data, an object storage service is ideal for this scenario.

In the following example, only media files will be used for object storage on Amazon S3.

### Django file storage system

Django abstracts away file access and file management to a file storage system. This layer is a pluggable framework that lets you switch from one implementation to another. Django’s default file storage is provided by **django.core.files.storage.FileSystemStorage**.

In the project **settings.py** file, the **STORAGES** variable defines the specific storage implementations to be used by your application. By default, after creating a Django project with the CLI, that variable is missing from the settings. But it is equivalent to the values for **default** and **staticfiles**, as shown in the following code snippet. The first sets the file system for *media files*, the second for *static files*. By default, all files are stored locally in the Django application.

```python
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}
```

### Storage configuration for Amazon S3

To place media files on Amazon S3, the first task is to create an Amazon S3 bucket, which can be done from the AWS Management Console or from the AWS Command Line Interface (AWS CLI). The bucket can remain private even if media files will be served from it. But cross-origin resource sharing (CORS) must be enabled for your bucket to be able to serve these files to different hostnames.

#### [Creating an Amazon S3 Bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html)

When a specific bucket is available for your Django application, two Python packages must be installed in your Django project, **django-storages** and **boto3**. This brings a Django file system implementation that is able to integrate with the Amazon S3 API by internally using the AWS SDK for Python (Boto3).

```bash
pip install django-storages boto3
```

When the Python packages are available in a project, they can be used. The **STORAGES** value can be modified in **settings.py**. The media file storage under **default** is changed to **storages.backends.s3boto3.S3Boto3Storage** to enable storage on Amazon S3.

```python
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}
```

The Django Amazon S3 file storage uses specific variables to locate the S3 bucket. The following two variables, **AWS_STORAGE_BUCKET_NAME** and **AWS_S3_REGION_NAME**, can be set to define which bucket to use and in which AWS Region.

```bash
AWS_STORAGE_BUCKET_NAME = 'pets-project-us-west-2-123456789901'
AWS_S3_REGION_NAME = 'us-west-2'
```

The Django S3 file storage can be configured further with other variables that are optional. In particular, it can use AWS Identity and Access Management (IAM) credentials to access the S3 bucket. You should avoid hardcoding anything sensitive in the settings. Instead, the Django application will benefit from using the Amazon EC2 instance role credentials to get access to the media files on Amazon S3.

### Testing the Amazon S3 integration

During development and testing on your IDE, media files can be stored locally in the Django project or on Amazon S3. You can switch back and forth between the two storage backends by simply editing the settings if the media URLs are not hardcoded in the Django templates. For example, if a pet's model field is picture = models.ImageField(), a template can display the image as <img src="{{ raw}}{{ pet.picture.url }}{{ endraw}}" />.

The following diagram shows a running Django application using Amazon S3 as its media files storage backend.

Developer -> AWS supported IDE (django Application) -> Amazon S3 (Multimedia)

You can check that everything works as expected by starting the application and inspecting a media file URL in your browser. The easiest method is to view the webpage source code from your browser menu. The resulting HTML code is illustrated in the following two use cases.

When the **STORAGES** default backend is set to **django.core.files.storage.FileSystemStorage**, images are served locally with a relative URL as in **/media/luna.jpg**.

```html
<td><a href="/pet/2">
  <img src="/media/luna.jpeg" width="120" />
  <p>Luna</a></p>
  <p>Ana Carolina Silva</p>
</td>
```

When the **STORAGES** default backend is set to **storages.backends.s3boto3.S3Boto3Storage**, images are served with a temporary and secure URL such as **https://pets-project-us-west-2-xxxx.s3.amazonaws.com/luna.jpg?...**

Both credentials and expiration are added automatically to the URL. Even if Django sets a high number of seconds for the expiration time, Amazon S3 will enforce a maximum of 7 days.

```html
<td><a href="/pet/2">
  <img src="https://pets-project-us-west-2-649088000912.s3.amazonaws.com/luna2.jpeg?AWSAccessKeyId=AS...&amp;Signature=Lwz...&amp;x-amz-security-token=IQ...3D&amp;Expires=1714729892" width="120" />
  <p>Luna</a></p>
  <p>Ana Carolina Silva</p>
</td>
```

Another way to verify that media files are stored in Amazon S3 is to either modify one or upload a new one. If you do not have a custom webpage to upload a new picture in your application, you can visit the administration site to modify a file.

After saving this change, you can go to your Amazon S3 bucket to verify that the file has been uploaded to the correct storage backend.

## Using ElastiCache for Session Storage

The performance of an application in production is often a main concern. This section focuses on how the latency and user experience can be improved.

### HTTP sessions
