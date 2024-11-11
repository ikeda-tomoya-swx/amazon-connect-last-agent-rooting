import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['tableName'])

def lambda_handler(event, context):
    phoneNumber = event['Details']['Parameters']['phoneNumber']
    response = table.get_item(Key={'phoneNumber': phoneNumber})

    if 'Item' in response:
        return {
            'phoneNumber': response['Item'].get('phoneNumber'),
            'lastAgent': response['Item'].get('lastAgent')
        }
    else:
        return {'Message': 'No record found'}