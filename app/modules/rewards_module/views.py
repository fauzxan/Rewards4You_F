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
# from decimal import Decimal
import csv

def generate_csv(data):
    f = csv.writer(open('rewards.csv', 'w', newline=''))
    f.writerow(['price_value', 'type_of_product', 'merchant_id', 'reward_id', 'tier_status', 'target_merchant'])
    for reward in data:
        f.writerow(
            [
                reward['price_value'],
                reward['type_of_product'],
                reward['merchant_id'],
                reward['reward_id'],
                reward['tier_status'],
                reward['target_merchant']   
            ]
        )

# data = [{'price_value': 276, 'type_of_product': 'electronics', 'merchant_id': Decimal('1'), 'reward_id': Decimal('1'), 'tier_status': Decimal('1'), 'target_merchant': [1, 1, 0]}, {'price_value': 268, 'type_of_product': 'sports', 'merchant_id': Decimal('1'), 'reward_id': Decimal('1'), 'tier_status': Decimal('1'), 'target_merchant': [0, 0, 2]}, {'price_value': 376, 'type_of_product': 'home', 'merchant_id': Decimal('1'), 'reward_id': Decimal('1'), 'tier_status': Decimal('1'), 'target_merchant': [2, 0, 1]}, {'price_value': 47, 'type_of_product': 'apparel', 'merchant_id': Decimal('1'), 'reward_id': Decimal('1'), 'tier_status': Decimal('1'), 'target_merchant': [0, 1, 1]}, {'price_value': 361, 'type_of_product': 'sports', 'merchant_id': Decimal('1'), 'reward_id': Decimal('1'), 'tier_status': Decimal('1'), 'target_merchant': [1, 0, 2]}, {'price_value': 230, 'type_of_product': 'apparel', 'merchant_id': Decimal('1'), 'reward_id': Decimal('1'), 'tier_status': Decimal('1'), 'target_merchant': [0, 0, 2]}, {'price_value': 433, 'type_of_product': 'books', 'merchant_id': Decimal('1'), 'reward_id': Decimal('1'), 'tier_status': Decimal('1'), 'target_merchant': [1, 2, 2]}, {'price_value': 487, 'type_of_product': 'food', 'merchant_id': Decimal('1'), 'reward_id': Decimal('1'), 'tier_status': Decimal('1'), 'target_merchant': [1, 2, 2]}, {'price_value': 432, 'type_of_product': 'books', 'merchant_id': Decimal('1'), 'reward_id': Decimal('1'), 'tier_status': Decimal('1'), 'target_merchant': [1, 0, 2]}, {'price_value': 164, 'type_of_product': 'sports', 'merchant_id': Decimal('1'), 'reward_id': Decimal('1'), 'tier_status': Decimal('1'), 'target_merchant': [0, 1, 0]}]
# generate_csv(data)