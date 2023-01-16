'''
- User table on dynamoDB updated from here
- Contains dummy_data_generation()
'''

'''
Dummy Data Generation: Generates dummy data to be stored in S3
    as CSV

input: user ID and reward preferences as list,
output: JSON
    format: [{},{},{}...]
'''
'''
Sample structure of JSON for reference:
{
    price_value: Integer,
    type of Product: String,
    merchant_id: Integer,
    reward_id: Integer,
    tier_status: Integer,
    target_merchant: Integer
}
'''

import random
import itertools
import csv
from io import BytesIO
import pandas as pd
import numpy as np
import boto3

import app.utils.aws_util as tb

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
    data = pd.read_csv('./train.csv')
    buffer = BytesIO()
    np.save(buffer, data.values)
    #Body= data.to_csv(header=False,index=False).encode("utf-8")
    # text_file = io.StringIO()
    # data.to_csv(text_file,index=None)
    # print("")
    # print("DEBUG:", text_file.getvalue())
    return buffer.getvalue()

def load_dataset(csv_path, target_feature):
    dataset = pd.read_csv(csv_path)
    t = dataset[target_feature]
    X = dataset.drop([target_feature], axis=1)
    return X, t
def dummy_data_generation(size, userID):
    targets = list(itertools.permutations([1, 2, 3]))
    print(targets)
    product_types = [
        "electronics",
        "food",
        "apparel",
        "home",
        "books",
        "sports"
    ]
    user_data = tb.retrieve_all_items('user')
    index = -1
    for user in user_data:
        index += 1
        if user['user_id'] == userID:
            break
    user = user_data[index]
    user = user_data[index]
    table = []
    for i in range(size):
        data = {}
        data['price_value'] = random.randint(1,500)
        data['type_of_product'] = product_types[random.randint(0, len(product_types)-1)]
        data['preferred_merchant'] = user['merchant_preference_id'] # User preference
        data['reward_id'] = user['rewards_preference_id']
        data['tier_status'] = user['tier_status_id']
        data['target_merchant'] = str(targets[random.randint(0,len(targets)-1)]).replace("(","").replace(")","")
        table.append(data)
    return table


# print(dummy_data_generation(100, '411228e5-53c8-4350-89a9-89436b5b6297'))

