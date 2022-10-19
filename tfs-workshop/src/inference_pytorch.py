
# Built-Ins
import io, os, sys
import json
import subprocess, time

import numpy as np
from base64 import b64decode
from PIL import Image

import torch
import torchvision
from torchvision import datasets, transforms, models
from torchvision.models.detection import FasterRCNN
import torchvision.transforms as transforms
from fairseq.models.transformer import TransformerModel

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    
def model_fn(model_dir=None):
    '''
    Loads the model into memory from storage and return the model.
    '''
    model = TransformerModel.from_pretrained(
        model_dir,
        checkpoint_file='checkpoint_best.pt',
        data_name_or_path=model_dir,
        bpe='sentencepiece',
        sentencepiece_model=f'{model_dir}/subword_tokenizer_ko.model',
        source_lang='ko', target_lang='en'
    )
    # model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
    # load the model onto the computation device
    model = model.eval().to(device)    
    return model


def transform_fn(model, request_body, content_type='application/json', accept_type=None):
    '''
    Deserialize the request body and predicts on the deserialized object with the model from model_fn()
    '''
    t0 = time.time()
    
    input = json.loads(request_body)
    with torch.no_grad():    
        result = model.translate(input)

    t1 = time.time() - t0
    print("--- Elapsed time: %s secs ---" % t1)
    
    outputs = json.dumps({'result': result})
    
    return outputs
