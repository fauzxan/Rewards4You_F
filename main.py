from flask import Flask
import uuid

from flask import request, json
from app.utils.aws_util import get_resource_config
from app.keyfactory import KeyFactory
from boto3.dynamodb.conditions import Key
from app.controller.user_controller import dummy_data_generation
from app.controller.rewards_controller import ping_sagemaker
from app.modules.rewards.views import generate_csv, send_to_s3, convert_csv_to_fileobject
from werkzeug.routing import BaseConverter

dynamoDB = get_resource_config('dynamodb')
table = dynamoDB.Table('user')

class ListConverter(BaseConverter):

    def to_python(self, value):
        return value.split(',')

    def to_url(self, values):
        return ','.join(BaseConverter.to_url(value)
                        for value in values)

app = Flask(__name__)
app.url_map.converters['list'] = ListConverter


from app.modules import user

app.register_blueprint(user.module)

@app.route('/')
def index():
    return "App is up and running"


@app.route('/test_ping_sagemaker', methods=['GET'])
def test_ping_sagemaker():
    body = convert_csv_to_fileobject()
    response = ping_sagemaker(body)
    return response['Body'].read().decode('ascii')


if __name__ == "__main__":

    app.run(debug=True, port=5001)

