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