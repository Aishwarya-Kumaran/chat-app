
from fastai.vision import *
from fastai.metrics import error_rate, accuracy
import warnings
warnings.filterwarnings('ignore')
import fastai
import emoji
import io
import os
from PIL import Image
import base64
from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
from emojify import emojize
from updateAvatar import updateAvatar

warnings.filterwarnings('ignore')

app = Flask(__name__)
CORS(app)


def get_model():
    global model;
    model = load_learner('model1')
    print("model loaded")

def preprocess_image():
    print("image preprocessed")


print("loading model")
get_model()


@app.route('/predict', methods=['POST'])
def predict():
    message = request.get_json(force=True)
    encoded = message['image']
    userName = message['userName']
    password = message['password']
    imgdata = base64.b64decode(encoded)
    filename = 'some_image.jpg'  
    with open(filename, 'wb') as f:
        f.write(imgdata)
    
    path = "some_image.jpg"
    img = open_image(path)
    print("opened the image")

    pred_class, pred, y = model.predict(img)
    print(pred_class)
    print(pred)
    pred_class = str(pred_class)
    updateAvatar(userName, password, pred_class)
    response={
        "emoji": pred_class
    }
    return jsonify(response)