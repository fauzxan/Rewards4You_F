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
import sys
import itertools

import app.utils.aws_util as tb


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

