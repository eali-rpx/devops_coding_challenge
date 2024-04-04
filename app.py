import yaml

def lambda_handler(event, context):
    # Read YAML file
    with open('data/ebbcarbon.yaml', 'r') as file:
        yaml_content = yaml.safe_load(file)
    
    # Prepare response
    response = {
        'statusCode': 200,
        'body': yaml.dump(yaml_content),
        'headers': {
            'Content-Type': 'text/yaml'
        }
    }
    
    return response
