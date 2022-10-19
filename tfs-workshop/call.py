import boto3
import json

runtime_client = boto3.client('sagemaker-runtime')

endpoint_name = 'translate-dev'

body = ['안녕하세요.', '반갑습니다.']
body = json.dumps(body)

response = runtime_client.invoke_endpoint(
    EndpointName=endpoint_name, 
    ContentType='application/json',
    Accept='application/json',
    Body=body
    )

outputs = json.loads(response['Body'].read().decode())
print(outputs)