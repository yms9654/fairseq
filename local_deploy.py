import os
import time
from sagemaker.deserializers import JSONDeserializer
from sagemaker.serializers import IdentitySerializer
from sagemaker.pytorch.model import PyTorchModel

role = 'sage-maker-full-access'
endpoint_name = "local-endpoint-pytorch-{}".format(int(time.time()))
local_model_path = f'file://{os.getcwd()}/model_artifact_1017/model.tar.gz'

model = PyTorchModel(model_data=local_model_path,
                     role=role,
                     entry_point='inference.py', 
                     source_dir='code',
                     framework_version='1.6.0',
                     py_version='py3')

from sagemaker.serverless import ServerlessInferenceConfig

serverless_config = ServerlessInferenceConfig(
  memory_size_in_mb=6144,
  max_concurrency=10,
)
# predictor = model.deploy(serverless_inference_config=serverless_config)
predictor = model.deploy(initial_instance_count=1, instance_type='local')

data = '안녕하세요'
response = predictor.predict(data)
print(response)