import boto3
import json

runtime_client = boto3.client('sagemaker-runtime')

endpoint_name = 'translate-dev4'

body = ['부스럭.. 부스럭...', '부스럭.. 부스럭...']
body = json.dumps(body)

response = runtime_client.invoke_endpoint(
    EndpointName=endpoint_name, 
    ContentType='application/json',
    Accept='application/json',
    Body=body
    )

outputs = json.loads(response['Body'].read().decode())
print(outputs)