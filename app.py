import yaml

def get_yaml_data(filename):
    with open(filename, "r") as f:
        data = yaml.safe_load(f)
    return data

def lambda_handler(event, context):
    if event['httpMethod'] == 'GET':
        # Get the data from the YAML file
        data = get_yaml_data("data/ebbcarbon.yaml")
        
        # Extract the "resources" part
        resources = data.get("resources")
        
        # Return response
        return {
            "statusCode": 200,
            "body": yaml.dump(resources)
        }
    else:
        return {
            "statusCode": 405,
            "body": "Method Not Allowed"
        }