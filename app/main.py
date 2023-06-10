
from fastapi import Request
from fastapi import FastAPI
import json
app = FastAPI()
import numpy as np

import os
from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
# from fastapi.encoders import jsonable_encoder
# from fastapi.responses import JSONResponse

from json import JSONEncoder

class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

# os.environ["CUDA_VISIBLE_DEVICES"] = "0"
# os.environ["SUNO_USE_SMALL_MODELS"] = "0"
# os.environ["SUNO_OFFLOAD_CPU"] = "1"

# # download and load all models
# preload_models()

@app.post('/')
async def main(request: Request):
    content_type = request.headers.get('Content-Type')
    
    if content_type is None:
        return 'No Content-Type provided.'
    elif content_type == 'application/json':
        try:
            JSON = await request.json()
            audio_array = generate_audio(JSON['text_prompt'])
            numpyData = {"array": audio_array}
            encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)
            return encodedNumpyData
        except JSONDecodeError:
            return 'Invalid JSON data.'
    else:
        return 'Content-Type not supported.'



@app.post('/test')
async def main(request: Request):
    content_type = request.headers.get('Content-Type')
    
    if content_type is None:
        return 'No Content-Type provided.'
    elif content_type == 'application/json':
        try:
            json = await request.json()
            return len(json['text_prompt'])
        except JSONDecodeError:
            return 'Invalid JSON data.'
    else:
        return 'Content-Type not supported.'