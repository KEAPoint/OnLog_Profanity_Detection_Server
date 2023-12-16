from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import tensorflow as tf
import numpy as np
import pickle
from keras.preprocessing import sequence
from embedding import to_index_array, padding, decompose_string


class Item(BaseModel):
    text: str


class ProfanityChecker:
    def __init__(self, model_path, dict_path, max_len):
        self.model = tf.keras.models.load_model(model_path)
        with open(dict_path, 'rb') as f:
            self.jamodict = pickle.load(f)
        self.max_len = max_len

    def encode_review(self, text):
        text = decompose_string(text)
        text = to_index_array(text, self.jamodict)
        return padding(text, self.max_len)

    def predict(self, text):
        indices = self.encode_review(text)
        indices = np.array([indices])
        y_prob = self.model.predict(indices)
        return bool(y_prob.argmax(axis=-1) == 1)


app = FastAPI()
checker = ProfanityChecker('models/latest-yok-detect-model.h5', 'jamo.pydict', 681)

origins = [
    "http://localhost",
    "http://localhost:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post('/check-profanity')
async def check_slang(item: Item):
    is_slang = checker.predict(item.text)
    return {
        "success": True,
        "code": 0,
        "message": "string",
        "data": {
            "isSlang": is_slang
        }
    }
