# Building a Serverless API with AWS Infrastructure Composer

## Lab overview

AnyCompany is a rapidly growing e-commerce business that aims to enhance its online presence and improve customer experience. As a cloud solutions architect, you are tasked with building a serverless application to serve as the backbone for AnyCompany’s new product catalog management system.

The application requires a robust and scalable backend capable of handling CRUD (Create, Read, Update, Delete) operations on a NoSQL database. Additionally, these operations are exposed through a RESTful API, allowing clients to interact with the product catalog seamlessly. To streamline the provisioning process and ensure consistent deployments, you use Infrastructure as Code (IaC) principles using AWS CloudFormation.

## Objectives

By the end of this lab, you should be able to do the following:

Use AWS CloudFormation to provision a serverless application architecture, comprising an Amazon API Gateway REST API, an Amazon DynamoDB table, and AWS Lambda functions.
Use the Boto3 Python Software Development Kit (SDK) to implement comprehensive CRUD (Create, Read, Update, Delete) functionality for seamless interaction with the DynamoDB table.
Validate the correct operation of the GET, POST, and PUT methods by thoroughly testing the corresponding API Gateway endpoints and ensuring their ability to retrieve, create, and update in the DynamoDB table, respectively. Although a DELETE method is not required for this lab, optional delete functionality is provided.
Manage the lifecycle of the CloudFormation stack, including orchestrating the creation, updating, and deletion of the stack and all its provisioned resources.
Technical knowledge prerequisites
To successfully complete this lab, you should be familiar with the following services or features:

Amazon API Gateway
Amazon DynamoDB
AWS Lambda
AWS Cloudformation
Duration
This lab requires approximately 90 minutes to complete.

Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Additional information: Where to find more information.
 Answer: An answer to a question or challenge.
 Caution: Information of special interest or importance (not important enough to cause problems with equipment or data if you miss it, but it could result in the need to repeat certain steps).
 Expected output: A sample output that you can use to verify the output of a command or edited file.
 Note: A hint, tip, or important guidance.
 Refresh: A time when you might need to refresh a web browser page or list to show new information.
 Task complete: A conclusion or summary point in the lab.
 Warning: An action that is irreversible and could potentially impact the failure of a command or process (including warnings about configurations that cannot be changed after they are made).
Start lab
To launch the lab, at the top of the page, choose Start Lab.

 Caution: You must wait for the provisioned AWS services to be ready before you can continue.

To open the lab, choose Open Console .

You are automatically signed in to the AWS Management Console in a new web browser tab.

 Warning: Do not change the Region unless instructed.

Common sign-in errors
Error: Choosing Start Lab has no effect
In some cases, certain pop-up or script blocker web browser extensions might prevent the Start Lab button from working as intended. If you experience an issue starting the lab:

Add the lab domain name to your pop-up or script blocker’s allow list or turn it off.
Refresh the page and try again.
Lab environment
Lab Environment

Image description: The diagram illustrates the serverless architecture, where users interact with Amazon API Gateway, which invokes AWS Lambda functions to perform CRUD operations on an Amazon DynamoDB table. The data flow follows: users send requests to API Gateway, which invokes the corresponding Lambda function. Lambda functions access and manipulate data in the DynamoDB table using the Boto3 SDK. Responses are sent from Lambda back through API Gateway to the users.

Services used in this lab
Amazon API Gateway
Amazon API Gateway acts as the entry point for the serverless application, providing a RESTful API that exposes the CRUD operations to clients. It integrates seamlessly with AWS Lambda functions, invoking the appropriate Lambda function based on the incoming API request method and path. This allows API Gateway to orchestrate the interaction between clients and the backend services, enabling the creation, retrieval, updating, and deletion of items in the DynamoDB table through a unified API endpoint.

Amazon DynamoDB
Amazon DynamoDB serves as the NoSQL database for storing and retrieving the application’s data, providing a fully managed service with predictable performance and seamless scalability. The DynamoDB table acts as the persistent data store, allowing the Lambda functions to perform CRUD operations on items representing the product catalog, while DynamoDB automatically handles data partitioning and scaling to meet the application’s traffic demands.

AWS CloudFormation
CloudFormation is an infrastructure as code service that allows you to model, provision, and manage AWS resources by treating infrastructure as code. In this lab, CloudFormation is used to define and deploy the complete serverless application stack, including the API Gateway, Lambda functions, and DynamoDB table, ensuring consistent and repeatable deployments.

AWS Infrastructure Composer
Infrastructure Composer is a visual designer tool that helps you build serverless applications quickly by visually creating and connecting AWS resources. It generates CloudFormation templates that can be used to deploy your application infrastructure consistently across multiple environments.

AWS Lambda
AWS Lambda functions encapsulate the application’s business logic for CRUD operations, invoked by API Gateway and interacting with the DynamoDB table using Boto3. This serverless compute layer eliminates server management overhead while enabling automatic scaling based on traffic.

Task 1: Familiarize yourself with Infrastructure Composer
In this task, you will familiarize yourself with Infrastructure Composer. You navigate to Infrastructure Composer thru CloudFormation so that once complete, you can create (or update) your CloudFormation stack.

 Note: You do not use enhanced components in Infrastructure Composer. Only selections from the Standard IaC resources function as expected with CloudFormation

At the top of the AWS Management Console, in the search bar, search for and choose CloudFormation.

On the upper right corner of the page, choose Create stack  .

Select With new resources (standard).

Choose  Build from Infrastructure Composer .

Choose Create in Infrastructure Composer to go to Infrastructure Composer.

Familiarize yourself with the Infrastructure Composer layout.

On the left navigation panel, notice Resources selected by default.
The  Search for a resource section is where you search for resources needed in this lab.
To the right you can see the Canvas, Template, and Arrange options.
The canvas view visually displays your resource(s).
The template view programmatically lists your resource(s) and shows all associated code. You use YAML code in the template, enabled by default. To delete a resource from the CloudFormation stack, you need to delete that resource from the template code.
The arrange feature, organizes the canvas layout. The canvas layout is organized every time you save resource details.
The Menu  option is located above the upper right corner of the canvas. This is where you systematically choose Save template file to save your existing template as you complete the lab and backup your work.
 Note: Periodical reviews of the template code may be useful for this lab.

 Task complete: You have successfully navigated to Infrastructure Composer through CloudFormation and familiarized yourself with the Infrastructure Composer layout. You are now ready to begin creating resources for your serverless application using the Standard IaC resources.

Task 2: Create a Rest API
In this task, you will use Infrastructure Composer to create your serverless API.

Collapse  Enhanced components by choosing the  symbol.

In the  Search for a resource text area, enter rest api.

Drag and drop the AWS::ApiGateway::RestApi resource onto the canvas.

To open the Resources properties pane section on the right side of your browser, choose the RestApi resource and then choose Details.

 Note: The Editing dropdown denotes the resource you are editing. At this time, RestApi is the only resource.

In the Logical ID field, keep the default name RestApi.

 Note: Each resource requires a logical ID. This unique identifier allows CloudFormation to reference and manage the resource during stack creation, updates, and deletion.

In the Resource configuration text-area, replace the existing code with Name: Items.

 Note: This step assigns the name Items to the API, Items will be the name visible in the API Gateway console.

In the bottom right corner of the Resources properties pane, choose Save.

 Task complete: You have successfully created the Amazon API Gateway RestApi resource in your CloudFormation template using Infrastructure Composer. The API is named Items and serves as the serverless API for your application.

Task 3: Create a DynamoDB Table
In this task, you will use Infrastructure Composer to create your Amazon DynamoDB table.

In the left navigation panel  Search for a resource text area, enter table.

Drag and drop the AWS::DynamoDB::Table resource onto the canvas.

To open the Resources properties pane, select the Table resource and then choose Details.

In the Logical ID field, enter the value ItemsTable.

In the bottom right corner of the resources properties section, choose Save.

 Note: The AWS::DynamoDB::Table resource does not have a resource configuration text-area. To add the necessary properties, you need to add code directly to the template.

Select Template view.

Under the Items resource, you see the following code:


**********************************
**** This is an EXAMPLE ONLY. ****
**********************************

Type: AWS::DynamoDB::Table
Properties:
  KeySchema:
    - KeyType: <String>
      AttributeName: <String>
Change the KeyType, from the placeholder value of <String> to HASH.

Change the AttributeName, from the placeholder value of <String> to id.

Add these additional properties:


# Defines the table name
TableName: Items

# Defines the primary key attribute and its data type
AttributeDefinitions:
  - AttributeName: id
    AttributeType: S

# Configures the read and write throughput capacity for the table
ProvisionedThroughput:
  ReadCapacityUnits: 5
  WriteCapacityUnits: 5
 Caution: YAML is sensitive to indentation and formatting. Improper indentation or incorrect use of spaces and tabs can lead to parsing errors or unintended behavior. The editor shows improper indents by using colors. Use spaces or tabs to correct the indentation. This is the only step where you copy and paste code directly into the template.

 Expected output: Current template example.


**********************************
**** This is an EXAMPLE ONLY. ****
**********************************

Resources:
  RestApi:
    Type: AWS::ApiGateway::RestApi
    Properties:
      Name: Items
  ItemsTable:
    Type: AWS::DynamoDB::Table
    Properties:
      KeySchema:
        - KeyType: HASH
          AttributeName: id

      # Defines the table name    
      TableName: Items

      # Defines the primary key attribute and its data type
      AttributeDefinitions:
        - AttributeName: id
          AttributeType: S

      # Configures the read and write throughput capacity for the table    
      ProvisionedThroughput:
        ReadCapacityUnits: 5
        WriteCapacityUnits: 5
Return to the Canvas view.

Save your work by selecting the Menu  option above the upper right corner of the canvas. Name your file RestApiTemplate and choose Save template file.

 Task complete: You have successfully created the DynamoDB table resource in your CloudFormation template using Infrastructure Composer. The table is configured with the necessary key schema, attribute definitions, and provisioned throughput settings.

Task 4: Add create functionality
In this task, you will add the API Gateway resource /items endpoint, along with the POST method, AWS Lambda, and AWS Lambda permissions necessary to facilitate create functionality. This create functionality allows you to write new records to your Amazon DynamoDB table.

Task 4.1: Add an API Gateway resource
In the left navigation panel  Search for a resource text area, enter resource.

Drag and drop the AWS::ApiGateway::Resource onto the canvas.

To open the Resources properties pane, choose the newly created Resource and then choose Details.

In the Logical ID field, change the value to ItemsResource.

In the Resource configuration text-area, replace the existing code with:


# Specifies the parent resource for the new resource being created
ParentId: !GetAtt RestApi.RootResourceId

# Defines the resource path '/items' for the API endpoint
PathPart: items

# Associates the new resource with the RestApi resource
RestApiId: !Ref RestApi
In the bottom right corner of the Resources properties section, choose Save.

 Note:

Comments are added to the template code to facilitate learning and document why this code is necessary. The Infrastructure Composer code validator may remove some of these comments from the finalized template.
Observe the changes to the canvas. ItemsResource is now grouped with RestApi.
If you need to edit details for a grouped resource, select the specific resource to edit in the Editing dropdown menu located in the Resource properties section.
Task 4.2: Add the /items POST method
In the left navigation panel  Search for a resource text area, enter method.

Drag and drop the AWS::ApiGateway::Method resource onto the canvas.

To open the Resources properties pane, choose the Method resource and then choose Details.

In the Logical ID field, change the value to PostItemMethod.

In the Resource configuration text-area replace the existing code with:


# Specifies the HTTP method for the API Gateway method resource
HttpMethod: POST

# Associates the method with the ItemsResource resource
ResourceId: !Ref ItemsResource

# Associates the method with the RestApi resource
RestApiId: !Ref RestApi

# Sets the authorization type for the method (in this case, none)
AuthorizationType: NONE

Integration:
  # Specifies the integration type as AWS_PROXY
  Type: AWS_PROXY

  # Specifies the HTTP method for the integration request
  IntegrationHttpMethod: POST

  # Constructs the URI for invoking the Lambda function
  Uri: !Sub arn:aws:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${CreateItemFunction.Arn}/invocations
In the bottom right corner of the resources properties section, choose Save.

 Note: Observe the changes to the canvas. The PostItemMethod has been grouped with your other API Gateway resources.

Task 4.3: Add AWS Lambda permission for CreateItem
In the left navigation panel  Search for a resource text area, enter permission.

Drag and drop the AWS::Lambda::Permission resource onto the canvas.

To open the Resources properties pane, choose the Permission resource and choose Details.

In the Logical ID field, change the value to CreateItemLambdaPermission.

In the Resource configuration text-area replace the existing code with:


# Specifies the Lambda function name for the permission
FunctionName: !Ref CreateItemFunction

# Specifies the allowed action
Action: lambda:InvokeFunction

# Specifies the principal (API Gateway) allowed to invoke the Lambda function
Principal: apigateway.amazonaws.com

# Specifies the source ARN (API Gateway execution ARN) allowed to invoke the Lambda function
SourceArn: !Sub arn:aws:execute-api:${AWS::Region}:${AWS::AccountId}:${RestApi}/*/*/*
In the bottom right corner of the Resources properties section, choose Save.

 Note: Observe the changes to the canvas. The CreateItemLambdaPermission has been grouped with the API Gateway resource. This permission is grouped with the API Gateway resources, because this permission grants API Gateway permission to invoke the specified AWS Lambda. A trigger is added to the CreateItem AWS Lambda.

Task 4.4: Add the AWS Lambda CreateItemFunction
So far, you have created an AWS API Gateway with an /items resource. That resource has an attached POST method, and requires a lambda function with appropriate permissions to access the DynamoDB table.

In the left navigation panel  Search for a resource text area, enter function.

Drag and drop the AWS::Lambda::Function resource onto the canvas.

To open the Resources properties pane, choose the Function resource and then choose Details.

In the Logical ID field, change the value to CreateItemFunction.

In the Resource configuration text-area replace the existing code with:


FunctionName: CreateItem
Runtime: python3.12
Handler: index.create_item_handler
Code:
  ZipFile: |
    import boto3
    import json

    def create_item_handler(event, context):
        # Connect to DynamoDB
        dynamodb = boto3.resource('dynamodb')
        # Specify the table name
        table_name = 'Items'
        table = dynamodb.Table(table_name)
        try:
            # Get the item data from the request body
            item_data = json.loads(event['body'])
            # Put the item in the DynamoDB table
            response = table.put_item(Item=item_data)
            return {
                'statusCode': 200,
                'body': str(response)
            }
        except Exception as e:
            return {
                'statusCode': 500,
                'body': str(e)
            }
Role: !ImportValue RestApiLambdaRoleARN
 Additional information: This lab includes Python code that utilizes the Boto3 library, which is the AWS SDK for Python. The Boto3 library provides convenient APIs and low-level client interfaces for interacting with various AWS services, including DynamoDB, Lambda, and API Gateway. For further understanding and exploration of the Boto3 library, refer to the Boto3 documentation listed in the Additional Resources section.

In the bottom right corner of the resources properties section, choose Save.

 Note: Observe the changes to the canvas. The AWS API Gateway resources show connection to the AWS Lambda and Amazon DynamoDB.

Save your work by selecting the Menu  option above the upper right corner of the canvas. Name your file RestApiTemplate and choose Save template file, replacing the previously saved template.

Task 4.5: Confirm create functionality
Now that the create functionality has been implemented, review and validate if it meets the expected requirements.

On the right side of the browser, choose Create Template.

Expand the  Use a different bucket option.

To replace the default bucket name, copy the S3BucketName value to the left of these instructions, and paste it into the Transfer bucket name text-area.

Choose Confirm and continue to CloudFormation.

On the Create stack page, choose Next.

In the Stack name field, enter the name RestApi.

Choose Next.

On the Configure stack options page, navigate down and choose Next.

On the Review and create page, navigate down and choose Submit.

 Note:

The RestApi stack has a status of CREATE_IN_PROGRESS.
After a few minutes, if properly configured, the status changes to  CREATE_COMPLETE.
If stack creation is not successful, troubleshoot any error messages before proceeding. A common mistake is an improperly formatted template.
If stack creation is successful, proceed to confirm functionality.
At the top of the AWS Management Console, in the search bar, search for and choose API Gateway in a new browser tab.

In the API Gateway console, choose Items Api.

On the Resources page, choose /items.

The POST method is displayed under /items.

Select POST.

The menu bar displays: Method request | Integration request | Method response |Test.

Select the Test tab.

Enter the following code into the Request body text-area:


{
    "id": "1",
    "name": "sweater",
    "color": "yellow"
}
Scroll down and choose Test.

/items - POST method test results populate. Status 200 indicates success!

 Note: If status does not indicate success, troubleshoot the error message received.

Add a second record to the Items table to assist with later testing. Replace the code in the Request body text-area with:


{
    "id": "2",
    "name": "shirt",
    "color": "green"
}
Scroll down and choose Test.

/items - POST method test results populate. Status 200 indicates success!

Confirm that your items are in the DynamoDB Items Table.

At the top of the AWS Management Console, in the search bar, search for and choose DynamoDB in a new browser tab.

From the left navigation panel, Select Tables.

Select the Items table.

On the right side of browser, choose Explore table items.

Scroll down, in the Items returned section, notice the items.

 TaskComplete: you have successfully completed and confirmed create functionality!

Task 5: Add read all functionality
In this task, you will add a get method to the API Gateway /items resource. The read all functionality you create allows you to query all records.

Task 5.1: Continue building the template
Return to CloudFormation

Confirm the  RestApi stack is selected.

From the upper right menu, choose Update.

Select  Edit in Infrastructure Composer.

Choose Edit in Infrastructure Composer.

You have returned to the Infrastructure Composer canvas and can see the previously created resources.

Task 5.2: Add the /items get method
In the left navigation panel  Search for a resource text area, enter method.

Drag and drop the AWS::ApiGateway::Method resource onto the canvas.

To open the Resources properties pane, choose the Method resource and then choose Details.

In the Logical ID field, change the value to GetItemsMethod.

In the Resource configuration text-area replace the existing code with:


# Specifies the HTTP method for the API Gateway method resource
HttpMethod: GET

# Associates the method with the ItemsResource resource
ResourceId: !Ref ItemsResource

# Associates the method with the RestApi resource
RestApiId: !Ref RestApi

# Sets the authorization type for the method (in this case, none)
AuthorizationType: NONE

Integration:
  # Specifies the integration type as AWS_PROXY
  Type: AWS_PROXY

  # Specifies the HTTP method for the integration request
  IntegrationHttpMethod: POST

  # Constructs the URI for invoking the Lambda function
  Uri: !Sub arn:aws:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${ReadItemsFunction.Arn}/invocations
In the bottom right corner of the resources properties section, choose Save.

 Note: Observe the changes to the canvas. The GetItemsMethod has been grouped with the Api Gateway resources.

Task 5.3: Add AWS Lambda permission for ReadItems
In the left navigation panel  Search for a resource text area, enter permission.

Drag and drop the AWS::Lambda::Permission resource onto the canvas.

To open the Resources properties pane, select the Permission and choose Details.

In the Logical ID field, change the value to ReadItemsLambdaPermission.

In the Resource configuration text-area, replace the existing code with:


# Specifies the Lambda function name for the permission
FunctionName: !Ref ReadItemsFunction

# Specifies the allowed action
Action: lambda:InvokeFunction

# Specifies the principal (API Gateway) allowed to invoke the Lambda function
Principal: apigateway.amazonaws.com

# Specifies the source ARN (API Gateway execution ARN) allowed to invoke the Lambda function
SourceArn: !Sub arn:aws:execute-api:${AWS::Region}:${AWS::AccountId}:${RestApi}/*/*/*
In the bottom right corner of the resources properties section, choose Save.

 Note: Observe the changes to the canvas. The API Gateway resources may no longer be visually represented on the canvas. Do not be alarmed, the API Gateway template code still exists and can be confirmed by switching to template view as necessary.

Task 5.4: Add the AWS Lambda ReadItemsFunction
In the left navigation panel  Search for a resource text area, enter function.

Drag and drop the AWS::Lambda::Function resource onto the canvas.

To open the Resources properties pane, select the Function and Choose Details.

In the Logical ID field, change the value to ReadItemsFunction.

In the Resource configuration text-area, replace the existing code with:


FunctionName: ReadItems
Runtime: python3.12
Handler: index.read_items_handler
Code:
  ZipFile: |
      import boto3
      import json

      dynamodb = boto3.resource('dynamodb')

      def read_items_handler(event, context):
          try:
              # Specify the table name
              table_name = 'Items'
              table = dynamodb.Table(table_name)

              # Scan the table to get all items
              response = table.scan()
              items = response['Items']

              # Fetch all items if there are more than 1 page of results
              while 'LastEvaluatedKey' in response:
                  response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
                  items.extend(response['Items'])

              # Return the items as a JSON response
              return {
                  'statusCode': 200,
                  'headers': {
                      'Content-Type': 'application/json'
                  },
                  'body': json.dumps(items)
              }

          except Exception as e:
              # Return an error response
              return {
                  'statusCode': 500,
                  'headers': {
                      'Content-Type': 'application/json'
                  },
                  'body': json.dumps({
                      'error': str(e)
                  })
              }
Role: !ImportValue RestApiLambdaRoleARN
In the bottom right corner of the resources properties section, choose Save.

 Note: Observe the changes to the canvas. The GetItemsFunction now has connection to the DynamoDB Items table.

Save your work by selecting the Menu  option above the upper right corner of the canvas. Name your file RestApiTemplate and choose Save template file, replacing the previously saved template.

Task 5.5: Confirm read all items functionality
On the right side of the browser, choose Update Template.

To replace the default bucket name, copy the S3BucketName value to the left of these instructions, and paste it into the Transfer bucket name text-area.

Choose Confirm and continue to CloudFormation.

On the Update stack page, choose Next.

On the Specify stack details page, choose Next.

On the Configure stack options page, scroll down and choose Next.

On the Review RestAPI page, scroll down and observe the Changes in the Change set preview section.

Choose Submit.

The RestApi stack has a status of <span style="color:#0073bb">UPDATE_IN_PROGRESS</span>.
After the RestApi stack status changes to  UPDATE_COMPLETE, navigate to API Gateway.

 Refresh: Refresh the page to see the updated API Gateway resources.

A newly created GET method is displayed under /items.

On the Resources page, choose /items.

A list of methods appear to the right. Choose GET.

Select the Test tab.

Scroll down and choose Test to get all records.

 Note: If successful, the status code of 200 and a Response body that contains the expected data.

 TaskComplete: You have successfully completed and confirmed read all functionality!

Task 6: Add read by ID functionality
In this task, you add a get method to the API Gateway /{id} resource. The read by ID functionality you create allows you to query a single record by ID.

Task 6.1: Continue building the template
Return to the CloudFormation console.

Confirm the  RestApi stack is selected.

From the upper right menu, choose Update.

Select  Edit in Infrastructure Composer.

Choose Edit in Infrastructure Composer.

You have returned to the Infrastructure Composer canvas and can see the previously created resources.

Task 6.2: Add the items/{id} resource
In the left navigation panel  Search for a resource text area, enter resource.

Drag and drop the AWS::ApiGateway::Resource onto the canvas.

To open the Resources properties pane, select the Resource and Choose Details.

In the Logical ID field, change the value to ItemsIdResource.

In the Resource configuration text-area replace the existing code with:


# Specifies the parent resource for the new resource being created
ParentId: !Ref ItemsResource

# Defines the resource path '/{id}' for the API endpoint
PathPart: '{id}'

# Associates the new resource with the RestApi resource
RestApiId: !Ref RestApi
In the bottom right corner of the resources properties section, choose Save.

 Note: Observe the changes to the canvas. ItemsIdResource has disappeared along with the other RestApi resources.

Task 6.3: Add the /items/{id} get method
In the left navigation panel  Search for a resource text area, enter method.

Drag and drop the AWS::ApiGateway::Method resource onto the canvas.

To open the Resources properties pane, choose the Method resource and then choose Details.

In the Logical ID field, change the value to GetItemByIdMethod.

In the Resource configuration text-area replace the existing code with:


# Specifies the HTTP method for the API Gateway method resource
HttpMethod: GET

# Associates the method with the ItemsIdResource resource
ResourceId: !Ref ItemsIdResource

# Associates the method with the RestApi resource
RestApiId: !Ref RestApi

# Sets the authorization type for the method (in this case, none)
AuthorizationType: NONE

Integration:
  # Specifies the integration type as AWS_PROXY
  Type: AWS_PROXY

  # Specifies the HTTP method for the integration request
  IntegrationHttpMethod: POST

  # Constructs the URI for invoking the Lambda function
  Uri: !Sub arn:aws:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${ReadItemByIdFunction.Arn}/invocations
In the bottom right corner of the resources properties section, choose Save.

 Note: Observe the changes to the canvas. GetItemByIdMethod has disappeared along with the other RestApi resources.

Task 6.4: Add AWS Lambda permission for ReadItemById
In the left navigation panel  Search for a resource text area, enter permission.

Drag and drop the AWS::Lambda::Permission resource onto the canvas.

To open the Resources properties pane, select the Permission and choose Details.

In the Logical ID field, change the value to ReadItemByIdLambdaPermission.

In the Resource configuration text-area, replace the existing code with:


# Specifies the Lambda function name for the permission
FunctionName: !Ref ReadItemByIdFunction

# Specifies the allowed action
Action: lambda:InvokeFunction

# Specifies the principal (API Gateway) allowed to invoke the Lambda function
Principal: apigateway.amazonaws.com

# Specifies the source ARN (API Gateway execution ARN) allowed to invoke the Lambda function
SourceArn: !Sub arn:aws:execute-api:${AWS::Region}:${AWS::AccountId}:${RestApi}/*/*/*
In the bottom right corner of the resources properties section, choose Save.

 Note: Observe the changes to the canvas. GetItemByIdLambdaPermission has disappeared along with the other RestApi resources.

Task 6.5: Add the AWS Lambda ReadItemByIdFunction
In the left navigation panel  Search for a resource text area, enter function.

Drag and drop the AWS::Lambda::Function resource onto the canvas.

To open the Resources properties pane, select the Function and Choose Details.

In the Logical ID field, change the value to ReadItemByIdFunction.

In the Resource configuration text-area replace the existing code with:


FunctionName: ReadItemById
Runtime: python3.12
Handler: index.read_item_by_id_handler
Code:
  ZipFile: |
      import boto3
      import json

      dynamodb = boto3.resource('dynamodb')

      def read_item_by_id_handler(event, context):
          try:
              # Specify the table name
              table_name = 'Items'
              table = dynamodb.Table(table_name)

              # Get the item ID from the event
              item_id = event['pathParameters']['id']

              # Get the item from the DynamoDB table
              response = table.get_item(Key={'id': item_id})
              item = response.get('Item')

              # If the item exists, return it
              if item:
                  return {
                      'statusCode': 200,
                      'headers': {
                          'Content-Type': 'application/json'
                      },
                      'body': json.dumps(item)
                  }
              else:
                  # If the item doesn't exist, return a 404 error
                  return {
                      'statusCode': 404,
                      'headers': {
                          'Content-Type': 'application/json'
                      },
                      'body': json.dumps({'error': 'Item not found'})
                  }

          except Exception as e:
              # Return an error response
              return {
                  'statusCode': 500,
                  'headers': {
                      'Content-Type': 'application/json'
                  },
                  'body': json.dumps({
                      'error': str(e)
                  })
              }
Role: !ImportValue RestApiLambdaRoleARN
In the bottom right corner of the resources properties section, choose Save.

 Note: Observe the changes to the canvas. The ReadItemByIdFunction now has connection to the DynamoDB Items table.

Save your work by selecting the Menu  option above the upper right corner of the canvas. Name your file RestApiTemplate and choose Save template file, replacing the previously saved template.

Task 6.6: Confirm read items by id functionality
On the right side of the browser, choose Update Template.

To replace the default bucket name, copy the S3BucketName value to the left of these instructions, and paste it into the Transfer bucket name text-area.

Choose Confirm and continue to CloudFormation.

On the Update stack page, choose Next.

On the Specify stack details page, choose Next.

On the Configure stack options page, scroll down and choose Next.

On the Review RestAPI page, scroll down and observe the Changes in the Change set preview section.

Choose Submit.

The RestApi stack has a status of UPDATE_IN_PROGRESS.

After the RestApi stack status changes to  UPDATE_COMPLETE, navigate to API Gateway.

 Refresh: Refresh the page to see the updated API Gateway resources.

A newly created GET method is displayed under /{id}.

On the Resources page, choose /{id}.

A list of methods appears to the right. Choose GET.

Select the Test tab.

 Note: The path ID text area is enabled by the path variable {id}.

In the id text-area, enter the value of 1.

Scroll down and choose Test to get the yellow sweater item.

 Note: If successful, notice the status code of 200 and a response body that contains the expected data.

 TaskComplete: You have successfully completed and confirmed the get item by ID functionality!

Task 7: Add update by id functionality
In this task, you add a PUT method to the API Gateway /{id} resource. The PUT functionality allows you to update a single record by id.

Task 7.1: Continue building the template
Return to the CloudFormation console.

Confirm the  RestApi stack is selected.

From the upper right menu, choose Update.

Select  Edit in Infrastructure Composer.

Choose Edit in Infrastructure Composer.

You have returned to the Infrastructure Composer canvas and can see the previously created resources.

Task 7.2: Add the /items/{id} PUT method
In the left navigation panel  Search for a resource text area, enter method.

Drag and drop the AWS::ApiGateway::Method resource onto the canvas.

To open the Resources properties pane, choose the Method resource and then choose Details.

In the Logical ID field, change the value to UpdateItemMethod.

In the Resource configuration text-area replace the existing code with:


# Specifies the HTTP method for the API Gateway method resource
HttpMethod: PUT

# Associates the method with the ItemsIdResource resource
ResourceId: !Ref ItemsIdResource

# Associates the method with the RestApi resource
RestApiId: !Ref RestApi

# Sets the authorization type for the method (in this case, none)
AuthorizationType: NONE

Integration:
  # Specifies the integration type as AWS_PROXY
  Type: AWS_PROXY

  # Specifies the HTTP method for the integration request
  IntegrationHttpMethod: POST

  # Constructs the URI for invoking the Lambda function
  Uri: !Sub arn:aws:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${UpdateItemFunction.Arn}/invocations
In the bottom right corner of the resources properties section, choose Save.

 Note: Observe the changes to the canvas. UpdateItemMethod has disappeared along with the other RestApi resources.

Task 7.3: Add AWS Lambda permission for UpdateItem
In the left navigation panel  Search for a resource text area, enter permission.

Drag and drop the AWS::Lambda::Permission resource onto the canvas.

To open the Resources properties pane, select the Permission and choose Details.

In the Logical ID field, change the value to UpdateItemLambdaPermission.

In the Resource configuration text-area replace the existing code with:


# Specifies the Lambda function name for the permission
FunctionName: !Ref UpdateItemFunction

# Specifies the allowed action
Action: lambda:InvokeFunction

# Specifies the principal (API Gateway) allowed to invoke the Lambda function
Principal: apigateway.amazonaws.com

# Specifies the source ARN (API Gateway execution ARN) allowed to invoke the Lambda function
SourceArn: !Sub arn:aws:execute-api:${AWS::Region}:${AWS::AccountId}:${RestApi}/*/*/*
In the bottom right corner of the resources properties section, choose Save.

 Note: Observe the changes to the canvas. UpdateItemLambdaPermission has disappeared along with the other RestApi resources.

Task 7.4: Add the AWS Lambda UpdateItemFunction
In the left navigation panel  Search for a resource text area, enter function.

Drag and drop the AWS::Lambda::Function resource onto the canvas.

To open the Resources properties pane, select the Function and Choose Details.

In the Logical ID field, change the value to UpdateItemFunction.

In the Resource configuration text-area replace the existing code with:


FunctionName: UpdateItem
Runtime: python3.12
Handler: index.update_item_handler
Code:
  ZipFile: |
      import boto3
      import json

      dynamodb = boto3.resource('dynamodb')

      def update_item_handler(event, context):
          try:
              # Specify the table name
              table_name = 'Items'
              table = dynamodb.Table(table_name)

              # Get the item ID and updated data from the event
              item_id = event['pathParameters']['id']
              updated_data = json.loads(event['body'])

              # Prepare the AttributeUpdates dictionary
              attribute_updates = {
                  key: {'Value': value, 'Action': 'PUT'}
                  for key, value in updated_data.items()
              }

              # Update the item in the DynamoDB table
              response = table.update_item(
                  Key={'id': item_id},
                  AttributeUpdates=attribute_updates
              )

              # Return a success response
              return {
                  'statusCode': 200,
                  'headers': {
                      'Content-Type': 'application/json'
                  },
                  'body': json.dumps({
                      'message': 'Item updated successfully'
                  })
              }

          except Exception as e:
              # Return an error response
              return {
                  'statusCode': 500,
                  'headers': {
                      'Content-Type': 'application/json'
                  },
                  'body': json.dumps({
                      'error': str(e)
                  })
              }
Role: !ImportValue RestApiLambdaRoleARN
In the bottom right corner of the resources properties section, choose Save.

 Note: Observe the changes to the canvas. The UpdateItemFunction now has connection to the DynamoDB Items table.

Save your work by selecting the Menu  option above the upper right corner of the canvas. Name your file RestApiTemplate and choose Save template file, replacing the previously saved template.

Task 7.5: Confirm update item by ID functionality
On the right side of the browser, choose Update Template.

To replace the default bucket name, copy the S3BucketName value to the left of these instructions, and paste it into the Transfer bucket name text-area.

Choose Confirm and continue to CloudFormation.

On the Update stack page, choose Next.

On the Specify stack details page, choose Next.

On the Configure stack options page, scroll down and choose Next.

On the Review RestAPI page, scroll down and observe the Changes in the Change set preview section.

Choose Submit.

The RestApi stack has a status of UPDATE_IN_PROGRESS.

After the RestApi stack status changes to  UPDATE_COMPLETE, navigate to API Gateway.

 Refresh: Refresh the page to see the updated API Gateway resources.

Under /{id}, a newly created PUT method is displayed.

On the Resources page, choose /{id}.

A list of methods appear to the right. Choose PUT.

Select the Test tab.

 Note: The path ID text area is enabled by the path variable {id}.

In the id text-area, enter the value of 1.

In the Request body text-area, enter the following code:


{
    "name": "sweater",
    "color": "blue"
}
Scroll down and choose Test.

 Note:

If successful, notice the status code of 200 and a response body that contains {“message”: “Item updated successfully”}.
You can also get all items or get item by ID to confirm that the color has been changed from yellow to blue.
 TaskComplete: you have successfully completed and confirmed update item by ID functionality!

Task 8: Optional delete functionality
Although delete functionality is not a requirement for this lab, this feature can be added by referencing documentation listed in the Additional Resources section. Alternatively, the template code below, can be added at the end of your CloudFormation template file.

Delete functionality template code:

  # Delete Functionality
  DeleteItemMethod:
    Type: AWS::ApiGateway::Method
    Properties:
      HttpMethod: DELETE
      ResourceId: !Ref ItemsIdResource
      RestApiId: !Ref RestApi
      AuthorizationType: NONE
      Integration:
        Type: AWS_PROXY
        IntegrationHttpMethod: POST
        Uri: !Sub arn:aws:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${DeleteItemFunction.Arn}/invocations
  DeleteItemLambdaPermission:
    Type: AWS::Lambda::Permission
    Properties:
      FunctionName: !Ref DeleteItemFunction
      Action: lambda:InvokeFunction
      Principal: apigateway.amazonaws.com
      SourceArn: !Sub arn:aws:execute-api:${AWS::Region}:${AWS::AccountId}:${RestApi}/*/*/*
  DeleteItemFunction:
    Type: AWS::Lambda::Function
    Properties:
      FunctionName: DeleteItem
      Runtime: python3.12
      Handler: index.delete_item_handler
      Code:
        ZipFile: |
          import boto3
          import json
          dynamodb = boto3.resource('dynamodb')
          def delete_item_handler(event, context):
              try:
                  # Specify the table name
                  table_name = 'Items'
                  table = dynamodb.Table(table_name)
                  # Get the item ID from the event
                  item_id = event['pathParameters']['id']
                  # Delete the item from the DynamoDB table
                  response = table.delete_item(Key={'id': item_id})
                  # Return a success response
                  return {
                      'statusCode': 200,
                      'headers': {
                          'Content-Type': 'application/json'
                      },
                      'body': json.dumps({
                          'message': 'Item deleted successfully'
                      })
                  }
              except Exception as e:
                  # Return an error response
                  return {
                      'statusCode': 500,
                      'headers': {
                          'Content-Type': 'application/json'
                      },
                      'body': json.dumps({
                          'error': str(e)
                      })
                  }
      Role: !ImportValue RestApiLambdaRoleARN
Task 9: Confirm all functionality
In the API Gateway console, navigate to the Items API.

Select the Items API.

On the Resources page, choose the /items resource.

A list of methods appear to the right. Choose GET.

Select the Test tab.

Scroll down and choose Test.

Verify that the response body contains the green shirt item you created earlier.

On the Resources page, choose the /items resource.

A list of methods appear to the right. Choose POST.

Select the Test tab.

Enter the following code into the Request body text-area:


{
    "id": "3",
    "name": "hat",
    "color": "red"
}
Choose the Test button and verify that the response has a status code of 200.

Test the GET method again to confirm that the new item has been added to the list.

On the Resources page, select the /{id} resource.

A list of methods appear to the right. Choose Get.

Select the Test tab.

In the id text-area, enter the value of 2.

Scroll down and choose Test to get the green shirt item.

Verify that the response body contains the details of the specified item.

On the Resources page, choose /{id}.

A list of methods appear to the right. Choose PUT.

Select the Test tab.

In the id text-area, enter the value of 2.

In the Request body text-area, enter the following code:


{
    "name": "t-shirt",
    "color": "blue"
}
Choose the Test button and verify that the response body contains {“message”: “Item updated successfully”}.

To confirm that the changes were applied, test the /{id} GET method again for the item ID 2.

 Task Complete: You have successfully confirmed the functionality of all CRUD operations using the serverless API you built.

Task 10: Delete the CloudFormation Stack
In the AWS Management Console, navigate to the CloudFormation service.

Select the RestApi stack from the list of stacks.

From the upper right menu, choose Delete.

When prompted to Delete stack, choose Delete.

Choose Delete Stack.

The stack has a status of DELETE_IN_PROGRESS while it is being deleted.

After a few minutes, if the deletion is successful, the stack is removed from the list of stacks.

 Task complete: You have successfully deleted the CloudFormation stack and all of its provisioned resources.

Conclusion
In this lab, you have successfully done the following:

Used CloudFormation to provision a serverless application architecture, comprising an Amazon API Gateway REST API, an Amazon DynamoDB table, and AWS Lambda functions.
Used the Boto3 Python Software Development Kit (SDK) to implement comprehensive CRUD (Create, Read, Update, Delete) functionality for seamless interaction with the DynamoDB table.
Validated the correct operation of the GET, POST, PUT, and DELETE methods by thoroughly testing the corresponding API Gateway endpoints and ensured their ability to retrieve, create, update, and delete items in the DynamoDB table, respectively.
Managed the lifecycle of the CloudFormation stack, including orchestrating the creation, updating, and deletion of the stack and all its provisioned resources.
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End Lab and then confirm that you want to end your lab.

Additional Resources
AWS Lambda Documentation
Amazon API Gateway Documentation
Amazon DynamoDB Documentation
Boto3 DynamoDB Documentation
AWS CloudFormation Documentation
AWS Infrastructure Composer Documentation
AWS Identity and Access Management (IAM) Documentation
Python is property of the Python Software Foundation (PSF). Reference in this lab to any specific commercial product, process, or service, or the use of any trade, firm or corporation name is provided for informational purposes, and does not constitute endorsement, recommendation, or favoring by Amazon Web Services.