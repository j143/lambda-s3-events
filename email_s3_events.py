import boto3
import json

def lambda_handler(event, context):
    
    print(event)
    
    # Get the S3 event details
    # https://docs.aws.amazon.com/AmazonS3/latest/userguide/notification-content-structure.html
    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']
        # object_size = record['s3']['object']['size']
        # object_type = record['s3']['object']['contentType']
    

    # Construct the email message
    email_body = "A new object has been uploaded to S3:\n\n"
    email_body += "S3 URI: s3://" + bucket_name + "/" + object_key + "\n"

    # Send the email to the select user
    ses_client = boto3.client('ses')
    
    # verify email: https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html
    ses_client.send_email(
        Source='"No-Reply" <a@example.com>',
        Destination={
            'ToAddresses': ['b@example.com']
        },
        Message={
            'Body': {
                'Text': {
                    'Data': email_body
                }
            },
            'Subject': {
                'Data': 'New object uploaded to S3'
            }
        }
    )


