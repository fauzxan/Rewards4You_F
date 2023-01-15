'''
- Rewards controller will ping SAGEMAKER for computation
- Get response from SAGEMAKER and send it to frontend
    (GET endpoint is in rewards)
'''
import boto3

def ping_sagemaker(body):
    client = boto3.client('sagemaker-runtime')
    response = client.invoke_endpoint(
        EndpointName = 'sagemaker-scikit-learn-2023-01-15-09-33-36-140',
        Body = body,
        ContentType = 'text/csv',
        Accept = 'Accept'
    )