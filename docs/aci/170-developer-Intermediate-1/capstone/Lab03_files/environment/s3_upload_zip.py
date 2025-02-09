# Import AWS boto3 module
import boto3

# Define file_name, object_name, bucket_name, and boto3 s3 client

file_name = '8d247914.zip'
object_name = 'zipped/8d247914.zip'

# Replace <DOCUMENT_BUCKET> with your DocumentBucketName value listed to the left of these instructions (keep the quotes)

bucket_name = 'documentbucket-187333211758'
s3_client = boto3.client('s3')

response = s3_client.upload_file(file_name, bucket_name, object_name)

