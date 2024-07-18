import json
import boto3
import os

s3 = boto3.client('s3', region_name=os.environ['REGION']) 

def get_quotes(event, context):
    print("Incoming:::", event)

    try:
        response = s3.get_object(Bucket="ramesh-jk-bucket", Key="quotes.json")
        data = response['Body'].read().decode('utf-8')
        json_data = json.loads(data)
        print("JSON:::", json_data)

        response = {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Methods": "*",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps(json_data)
        }
        
        return response
    except Exception as e:
        print(e)
        response = {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
        return response

