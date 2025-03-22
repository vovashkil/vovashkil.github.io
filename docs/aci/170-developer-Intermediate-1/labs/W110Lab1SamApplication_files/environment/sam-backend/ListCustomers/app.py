import boto3


def lambda_handler(event, context):

    dynamodb = boto3.client("dynamodb")
    query_response = dynamodb.scan(TableName="LabCustomers")

    lists = [
        [item["ID"]["S"], item["firstname"]["S"], item["lastname"]["S"]]
        for item in query_response["Items"]
    ]

    return {"result": lists}
