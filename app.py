from flask import Flask
import uuid

from flask import request, json
from app.controller.table_util import get_resource_config
from app.keyfactory import KeyFactory
from boto3.dynamodb.conditions import Key
from app.controller.user_controller import dummy_data_generation
from app.modules.rewards_module.views import generate_csv, send_to_s3

dynamoDB = get_resource_config()
table = dynamoDB.Table('user')

app = Flask(__name__)



@app.route('/')
def index():
    return "Hello World!"

@app.route('/signup', methods=['post'])
def signup():
    return "Hello World!"

@app.route('/register', methods=['post','get'])
def register():
    data = json.loads(request.data)

    user_name = data.get('user_name')
    user_id = str(uuid.uuid4())
    password = data.get('password')
    email = data.get('email')
    merchant_preference_id = data.get("merchant_preference_id")
    reward_preference_id = data.get("reward_preference_id")
    tier_status_id = data.get("tier_status_id")

    print(user_name)

    table.put_item(
                Item={
        'user_id': user_id,
        'username': user_name,
        'password': password,
        'email': email,
        'merchant_preference_id': merchant_preference_id,
        'rewards_preference_id': reward_preference_id,
        'tier_status_id': tier_status_id
            }
        )

    return data

@app.route('/login', methods=['post'])
def login():
    data = json.loads(request.data)

    email = data.get('email')
    password = data.get('password')

    response = table.query(
                KeyConditionExpression=Key('email').eq(email)
        )
    items = response['Items']

    if password == items[0]['password']:
        user_id =  items[0]['user_id']
        dataset= dummy_data_generation(10000, user_id)
        generate_csv(dataset)
        send_to_s3()
        return "Record Found", 200


    return "Record not found", 400



if __name__ == "__main__":

    app.run(debug=True)

