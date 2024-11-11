import boto3
import os

# DynamoDBリソースを取得
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['tableName'])

def lambda_handler(event, context):
    # 顧客の電話番号と最後に担当したエージェントのIDを取得
    phoneNumber = event['Details']['ContactData']['CustomerEndpoint']['Address']
    lastAgent = event['Details']['Parameters']['lastAgent']

    # DynamoDBテーブルから該当する電話番号のアイテムを取得
    response = table.get_item(Key={'phoneNumber': phoneNumber})

    # アイテムが存在する場合、更新処理を行う
    if 'Item' in response:
        table.update_item(
            Key={'phoneNumber': phoneNumber},
            UpdateExpression="SET lastAgent = :agent",
            ExpressionAttributeValues={
                ':agent': lastAgent
            }
        )
        return {'Message': 'updated'}

    # アイテムが存在しない場合、新規作成
    else:
        table.put_item(
            Item={
                "phoneNumber": phoneNumber,
                "lastAgent": lastAgent
            }
        )
        return {'Message': 'added'}