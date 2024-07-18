import json
import boto3
import os

dynamodb = boto3.client('dynamodb', region_name=os.environ['REGION'])
table_name = os.environ['USERS_TABLE']

def get_subscribers(event, context):
    params = {
        'TableName': table_name,
    }

    try:
        response = dynamodb.scan(**params)
        items = response.get('Items', [])

        return {
            'statusCode': 200,
            'body': json.dumps(items),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Methods': '*',
                'Access-Control-Allow-Origin': '*',
            }
        }
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
