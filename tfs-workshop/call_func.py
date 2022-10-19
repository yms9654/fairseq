from src.inference_pytorch import model_fn, transform_fn
import json

model = model_fn('tfs-workshop/model_artifact')

body = ['안녕하세요.', '반갑습니다.']
body = json.dumps(body)
response = transform_fn(model, body)
# outputs = json.loads(response['Body'].read().decode())
print(response)