#!/usr/bin/env python
# coding: utf-8

# # Basic Steps with AWS SDK
# Regardless of the service or programming language, programming with AWS generally comes down to three steps. In this notebook, we'll be shoing an example with Python and S3, but the same general flow would apply to Java with DynamoDB for instance.

# ## 1) Import AWS Python SDK (Boto) library

# To work with AWS, you need to import the SDK for the programming language you are using. For Python, **Boto3** is the name of the AWS Python SDK. You must have installed it already, before running this program.

# In[ ]:


import boto3


# ## 2) Create an AWS client object for the service you want to use

# When programming using the AWS SDK, you will need a client object to interact with the AWS service. Depending on the service multiple types of client objects may be available. In this example, we will use the S3 service client.
# 
# You can specify login credentials when creating your client. If none are specified, the SDK will use the default AWS credentials in your environment. If you get authentication error here, make sure you check the documentation on setting up AWS credentials.

# In[ ]:


s3Client = boto3.client('s3')


# ## 3) Use client object to perform operations

# After creating a client object, you will use it to perform operations supported by the AWS service. Check the specific service API to see which operations are supported. In our case, we use the client object to list the objects in a specified S3 bucket. The response is generally in JSON format, and the AWS API reference will document for the format.
# 
# For this S3 operation, the S3 objects are are stored in a list under the "Contents" attribute. We can iterate through the list using standard Python mechanisms, and retrieve information about each object. For our demo, we will output the object name, and when it was last modified. The bucket I'm using stores images for a photo album.
# 
# **Please note** that in a real application, you would want to check for errors when calling the APIs.

# In[ ]:


# Use client object to load objects for specified bucket
response = s3Client.list_objects(Bucket='tucker-photo-album')

# Parse through response object
for content in response['Contents']:
    print("File:", content['Key']," - Last Modified: ", content['LastModified']) 

