'''
Rewards endpoint:
This will be a put request, where the body is a json file
1. Once dummy data is generated, it will call the rewards
endpoint to send to SAGEMAKER
2. This endpoint will also call the function to generate
    the csv file from json data.
3. GET endpoint exposed to the get recommendation list button
    (Called from frontend)
    Takes data from SAGEMAKER
'''
from flask import request, json
from app.utils.aws_util import get_resource_config
from boto3.dynamodb.conditions import Key
from app.controller.rewards_controller import rewards_controller

dynamoDB = get_resource_config('dynamodb')
table = dynamoDB.Table('user')

def rewards():
    data = json.loads(request.data)

    email = data.get('email')
    password = data.get('password')

    response = table.query(
                KeyConditionExpression=Key('email').eq(email)
        )
    items = response['Items']

    preferred_merchant = items[0]['merchant_preference_id']
    reward_id =    items[0]['rewards_preference_id']
    tier_status = items[0]['tier_status_id']
    price_value = items[0]['price']

    return rewards_controller(preferred_merchant, reward_id, tier_status, price_value)