import json
import boto3
import os
import requests

sns = boto3.client('sns', region_name=os.environ['REGION'])

def publish_to_sns(message):
    return sns.publish(
        TopicArn=os.environ['SNS_TOPIC_ARN'],
        Message=message
    )

def build_email_body(identity, form):
    return f"""
         Message: {form['message']}
         Name: {form['name']}
         Email: {form['email']}
         Service information: {identity['sourceIp']} - {identity['userAgent']}
      """

def static_mailer(event, context):
    print("EVENT::", event)
    data = json.loads(event['body'])
    email_body = build_email_body(event['requestContext']['identity'], data)

    try:
        publish_to_sns(email_body)
    except Exception as e:
        print(f"Error publishing to SNS:: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': 'false',
            },
            'body': json.dumps({'message': 'Internal Server Error'})
        }

    try:
        response = requests.post(
            " https://5seuy8safdhr6sr2l.execute-api.us-east-1.amazonaws.com/dev/subscribe",
            json={'email': data['email']}
        )
        print(response)
    except Exception as e:
        print(f"Error subscribing user:: {str(e)}")

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': 'false',
        },
        'body': json.dumps({'message': 'OK'})
    }
