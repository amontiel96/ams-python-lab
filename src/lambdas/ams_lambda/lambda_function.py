def lambda_handler(event, context):
    str_result = "Hello, world! - AMontiel"
    print(str_result)
    return str_result


"""
Example to execute lambda function in your local develop
lambda_handler({}, None)
"""

