from fastapi import Request
from fastapi import FastAPI
import json
import numpy as np
import os
from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from json import JSONEncoder

class NumpyArrayEncoder(JSONEncoder):
    """
    Custom JSON encoder to handle encoding NumPy arrays.
    """
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

os.environ["CUDA_VISIBLE_DEVICES"] = "0"
os.environ["SUNO_USE_SMALL_MODELS"] = "0"
os.environ["SUNO_OFFLOAD_CPU"] = "1"

# Download and load all models
preload_models(text_use_gpu=True,
    text_use_small=True,
    coarse_use_gpu=True,
    coarse_use_small=True,
    fine_use_gpu=True,
    fine_use_small=True,
    codec_use_gpu=True,
    force_reload=False)

app = FastAPI()

@app.post('/')
async def main(request: Request):
    """
    Endpoint for generating audio based on a text prompt.

    Parameters:
        - request: Request object containing the HTTP request data.

    Returns:
        - If successful, encoded JSON data containing the generated audio array.
        - If Content-Type is not provided, returns 'No Content-Type provided.'
        - If Content-Type is not supported, returns 'Content-Type not supported.'
        - If JSON data is invalid, returns 'Invalid JSON data.'
    """
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
    """
    just a testing function of a test endpoint return the length of the string
    """
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
