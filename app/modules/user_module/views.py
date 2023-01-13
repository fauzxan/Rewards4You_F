'''
Contains registration and login endpoint definitions
- This will call dummy_data_generation() to generate csv 
    file
- This will contain the login and registration APIs
'''

'''
Login Endpoint: PUT request that recieve the input given below,
    - Calls dummy_data_generation()
    
Input: User ID and Password
Output: None
'''

'''
Registration endpoint: PUT request that recieves the input given below,
    - Updates user table in dynamoDB
    - Calls dummy_data_generation()


Input: User ID, Password, User preferences
Output: None
'''