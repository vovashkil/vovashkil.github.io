import boto3


def lambda_handler(event, context):
    print(event)
    id = event["queryStringParameters"]["id"]
    firstname = event["queryStringParameters"]["firstname"]
    lastname = event["queryStringParameters"]["lastname"]
    dynamodb = boto3.client("dynamodb")
    query_response = dynamodb.scan(TableName="LabCustomers")
    put_response = dynamodb.put_item(
        TableName="LabCustomers",
        Item={
            "ID": {"S": id},
            "firstname": {"S": firstname},
            "lastname": {"S": lastname},
        },
    )
    return {"result": "Saved"}
