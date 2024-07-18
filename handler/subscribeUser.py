import json
import boto3
import os
import uuid
from datetime import datetime

dynamodb = boto3.client('dynamodb', region_name=os.environ['REGION'])
table_name = os.environ['USERS_TABLE']

def subscribe_user(event, context):
    data = json.loads(event['body'])
    print("EVENT:::", data)

    timestamp = int(datetime.utcnow().timestamp() * 1000)

    if 'email' not in data or not isinstance(data['email'], str):
        print("Validation Failed")
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Validation Failed: Email must be a string'}),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Methods': '*',
                'Access-Control-Allow-Origin': '*',
            }
        }

    item = {
        'userId': {'S': str(uuid.uuid4())},
        'email': {'S': data['email']},
        'subscriber': {'BOOL': True},
        'createdAt': {'N': str(timestamp)},
        'updatedAt': {'N': str(timestamp)},
    }

    params = {
        'TableName': table_name,
        'Item': item
    }

    try:
        dynamodb.put_item(**params)
        response = {
            'statusCode': 200,
            'body': json.dumps(item),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Methods': '*',
                'Access-Control-Allow-Origin': '*',
            }
        }
        return response
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Methods': '*',
                'Access-Control-Allow-Origin': '*',
            }
        }
