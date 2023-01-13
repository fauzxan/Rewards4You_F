import boto3

def get_resource_config():
    return boto3.resource('dynamodb', 'ap-southeast-1')

'''
input:
    table name: string
    values: list of values
output:
    None
'''

def insert_items(table, values):
    table = get_resource_config().Table(table)
    with table.batch_writer() as batch:
        for value in values:
            batch.put_item(Item=value)

'''
input:
    table: table name, string
output:
    data: list of all items in the table
'''

def retrieve_all_items(table):
    table = get_resource_config().Table(table)
    response = table.scan()
    data = response['Items']
    
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])
    return data
