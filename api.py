from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import tensorflow as tf
import numpy as np
from tensorflow import keras
import pickle
from keras.preprocessing import sequence
from embedding import to_index_array, padding, decompose_string

app = FastAPI()

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

MAX_LEN = 681

with open('jamo.pydict', 'rb') as f:
    jamodict = pickle.load(f)


def encode_review(text):
    text = decompose_string(text)
    text = to_index_array(text, jamodict)
    text = padding(text, MAX_LEN)
    
class Item(BaseModel):
  text: str


def predict(text):
  model = tf.keras.models.load_model('models/latest-yok-detect-model.h5')
  
  indices = encode_review(text)
  indices = np.array([indices])
  
  y_prob = model.predict(indices)
  result = y_prob.argmax(axis=-1)

  return result[0][0] == 1


@app.post('/check-profanity')
async def check_slang(item: Item):
    
   is_slang= predict(item.text)

   return {
     "success": True,
     "code": 0,
     "message": "string",
     "data": {
       "isSlang": is_slang 
      }
   }

