import os
import time
from sagemaker.deserializers import JSONDeserializer
from sagemaker.serializers import JSONSerializer
from sagemaker.pytorch.model import PyTorchModel

role = 'sage-maker-full-access'
# bucket = 'npx-translation-models'
# model_path = 's3://{}/model.tar.gz'.format(bucket)
model_path = 'tfs-workshop/model_artifact/model.tar.gz'
endpoint_name = 'translate-dev4'

model = PyTorchModel(model_data=model_path,
                     role=role,
                     entry_point='inference_pytorch.py', 
                     source_dir='tfs-workshop/src',
                     framework_version='1.12.0',
                     py_version='py38',
                    #  env={'SAGEMAKER_MODEL_SERVER_WORKERS': '1'}
                    )

predictor = model.deploy(
    endpoint_name=endpoint_name,
    initial_instance_count=1,
    instance_type='ml.c5.large',
    serializer=JSONSerializer(content_type='application/json'),
    deserializer=JSONDeserializer()
)
