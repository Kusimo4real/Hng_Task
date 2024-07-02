import json

def lambda_handler(event, context):
    visitor_name = event.get('queryStringParameters', {}).get('visitor_name', 'World')
    response = {
        "statusCode": 200,
        "body": json.dumps({
            "client_ip": event['requestContext']['identity']['sourceIp'],
            "greeting": f"Hello, {visitor_name}!"
        })
    }
    return response

