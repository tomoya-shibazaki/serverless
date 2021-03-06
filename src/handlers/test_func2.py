import json
import boto3

# バケット名,オブジェクト名
BUCKET_NAME = 'subsystem-storage'
OBJECT_KEY_NAME = 'hello.json'

s3 = boto3.resource('s3')

def handler(event, context):
    bucket = s3.Bucket(BUCKET_NAME)
    obj = bucket.Object(OBJECT_KEY_NAME)

    response = obj.get()    
    body = response['Body'].read()

    return {
        'isBase64Encoded': False,
        'statusCode': 200,
        "headers": {
            "Access-Control-Allow-Headers" : "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
            "Access-Control-Allow-Origin" : "*",
            "Access-Control-Allow-Methods": "OPTIONS,POST"
        },
        'body': str(json.loads(body.decode('utf-8')))
    }