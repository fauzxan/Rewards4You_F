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
from decimal import Decimal
import csv
import io
import pandas as pd
import boto3
from app.utils.aws_util import get_resource_config


def generate_csv(data):
    f = csv.writer(open('rewards.csv', 'w', newline=''))
    f.writerow(['price_value', 'type_of_product', 'preferred_merchant', 'reward_id', 'tier_status', 'target_merchant'])
    for reward in data:
        f.writerow(
            [
                reward['price_value'],
                reward['type_of_product'],
                reward['preferred_merchant'],
                reward['reward_id'],
                reward['tier_status'],
                reward['target_merchant']
            ]
        )

def send_to_s3():
    s3 = boto3.client('s3')
    s3.upload_file('./rewards.csv', 'sagemaker-studio-912ae080', 'rewards.csv')

def convert_csv_to_fileobject():
    data = pd.read_csv('./rewards.csv')
    text_file = io.StringIO()
    data.to_csv(text_file, header=None, index=None)
    print("\n\nDebug", text_file)
    return text_file
