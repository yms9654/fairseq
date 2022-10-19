from src.inference_pytorch import model_fn, transform_fn
import os

local_model_path = f'tfs-workshop/model_artifact'

model = model_fn(local_model_path)
response_body = transform_fn(model, '안녕하세요.')
print(response_body)