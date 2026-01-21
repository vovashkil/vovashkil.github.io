# DI2 Week 2: Building the Pets Microservice

* back to AWS Cloud Institute repo's root [aci.md](../aci.md)
* back to [Developer Intermediate 2](./developer-intermediate-2.md)
* back to repo's main [README.md](../../../README.md)

## Building the Pets Microservice

### Weekly Overview

* Using SAM teplate to create the `pets` microservice being able to pull a current list of available pets whenever a prospective adopter arrives at the shelter.
* This microservice will use API calls routed through a Lambda function to pull information from a DynamoDB table.
* Create an API Gateway to handle API requests from the frontend.
* Create a Lambda function to pull records from a DynamoDB table that stores adoptable pets.
* Use a SAM template to create a DynamoDB table with information about adoptable pets, such as name, age, species, and when they arrived at the shelter.
* Connect the Lambda function to this DynamoDB table to pull pet information.

---

## REVIEWING SERVERLESS MICROSERVICS WITH AWS SAM

### Serverless Microservices with AWS SAM

### The Pets Microservice Architecture

### Knowledge Check

### Summary

---

## SETTING UP API GATEWAY TO HANDLE REQUESTS ROUTING

### Activity: Adding an API Gateway Endpoint to the AWS SAM Template

### Activity: Adding an Implicit API to the AWS SAM Template

### Knowledge Check

### Summary

### Additional Resources

---

## BUILDING AND TESTING THE MICROSERVICE LAMBDA FUNCTION

### Activity: Updating the Lambda Function Code to Call DynamoDB

### Knowledge Check

### Summary

---

## USING DYNAMODB TO STORE DATA IN A SERVERLESS APPLICATION

### Activity: Defining a DynamoDB Table Using AWS SAM

### Activity: Populating the DynamoDB Table

### Knowledge Check

### Summary

---

## INTEGRATING THE MICROSERVICE WITH REACT FRONTEND

### Activity: Updating the React Code to Fetch Data from the API

### Activity: Uploading Images to an S3 Bucket

### Knowledge Check

### Summary

---

## HANDS-ON LAB ACTIVITY

### Lab: Creating a Get Products Microservice
