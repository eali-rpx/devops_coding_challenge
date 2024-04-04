import json
import yaml

def lambda_handler(event, context):
    # Check if the HTTP method is GET
    if event["httpMethod"] != "GET":
        return {
            'statusCode': 405,  # Method Not Allowed
            'body': json.dumps({'error': 'Method not allowed'})
        }
    
    try:
        with open('data/ebbcarbon.yaml', 'r') as file:
            resources = yaml.safe_load(file)
        return {
            'statusCode': 200,
            'body': json.dumps(resources)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

