'''
- Rewards controller will ping SAGEMAKER for computation
- Get response from SAGEMAKER and send it to frontend
    (GET endpoint is in rewards)
'''
import boto3
import random

def ping_sagemaker(body):

    client = boto3.client('sagemaker-runtime')
    response = client.invoke_endpoint(
        EndpointName = 'sagemaker-scikit-learn-2023-01-15-09-33-36-140',
        Body = body.getvalue(),
        ContentType = 'text/csv',
        Accept = 'Accept'
    )

    
rewards_mapping = {
    "Cash": 0,
    "Coupon": 1,
    "Product": 2
}

payments_mapping = {
    "GrabPay": 0,
    "Revolut": 1,
    "GPay": 2
}

tiers_mapping = {
    "Member or Silver": 0,
    "Gold": 1,
    "Platinum": 2
}


def rewards_controller(preferred_merchant, reward_id, tier_status, price_value):
    """ Generate Type Of Product and Reward Value and Return JSON Value"""
    tier = tiers_mapping[tier_status]
    tier_cashback = {0: 0.003,1:0.003,2:0.004,3:0.006}
    ranking = {'3, 1, 2': 0,'3, 2, 1':1 ,'1, 3, 2':2,'1, 2, 3':3,'2, 1, 3':4,'2, 3, 1':5}
    costs = {}
    costs['Gpay'] = random.uniform(0, min(price_value,10))
    costs['Revolut'] = random.uniform(0, min(price_value,10))
    costs['GrabPay'] = tier_cashback[int(tier)] * price_value
    sort_by_value = dict(sorted(costs.items(), key=lambda item: item[1],reverse=True))
    # print(sort_by_value)
    
    # vals = [gpay, revolut,grab]
    # print(sort_by_value.keys())
    
    json_resp = {
     "rank_1": list(sort_by_value.keys())[0],
     "rank_2": list(sort_by_value.keys())[1],
     "rank_3": list(sort_by_value.keys())[2],}
    return json_resp
