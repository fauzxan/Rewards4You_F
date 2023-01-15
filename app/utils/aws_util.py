import boto3


'''
Input: the name of the resource that you want to connect to
Output: An open connection to that specified resource
'''
def get_resource_config(resource, region='ap-southeast-1'):
    return boto3.resource(
        service_name = resource,
        region_name = region
        )

'''
input:
    table name: string
    values: list of values
output:
    None
'''

def insert_items(table, values):
    table = get_resource_config('dynamodb').Table(table)
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
    table = get_resource_config('dynamodb').Table(table)
    response = table.scan()
    data = response['Items']
    
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])
    return data
