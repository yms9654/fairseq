import os
import time
from sagemaker.deserializers import JSONDeserializer
from sagemaker.serializers import JSONSerializer
from sagemaker.pytorch.model import PyTorchModel

role = 'sage-maker-full-access'
local_model_path = f'file://{os.getcwd()}/tfs-workshop/model_artifact/model.tar.gz'

model = PyTorchModel(model_data=local_model_path,
                     role=role,
                     entry_point='inference_pytorch.py', 
                     source_dir='tfs-workshop/src',
                     framework_version='1.12.1',
                     py_version='py38',
                     env={'SAGEMAKER_MODEL_SERVER_WORKERS': '1'})

predictor = model.deploy(
    initial_instance_count=1,
    instance_type='local',
    serializer=JSONSerializer(content_type='application/json'),
    deserializer=JSONDeserializer()
)

import sagemaker
import boto3
import json

# runtime_client = boto3.client('sagemaker-runtime')
runtime_client = sagemaker.local.LocalSagemakerRuntimeClient()
endpoint_name = model.endpoint_name

response = runtime_client.invoke_endpoint(
    EndpointName=endpoint_name, 
    ContentType='application/json',
    Accept='application/json',
    Body='안녕하세요.'
    )

outputs = json.loads(response['Body'].read().decode())
print(outputs)