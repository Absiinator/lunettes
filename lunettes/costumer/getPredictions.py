from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import cv2
import os
import cvlib as cv
import pickle
from pathlib import Path

def get_file_path(costumer_image):
    BASE_DIR = Path(__file__).resolve().parent.parent
    IMAGE_DIR = os.path.join(BASE_DIR, 'media/costumers/images')
    filename = costumer_image.split('/')[-1]
    image = os.path.join(BASE_DIR, f'.{costumer_image}/')
    image = os.path.join(IMAGE_DIR, filename)  

    return image


def get_prediction(image, model):
    
    classes = ['Male','Female']

    frame = cv2.imread(image)
    face, confidence = cv.detect_face(frame)
    for idx, f in enumerate(face):
        # get corner points of face rectangle        
        (startX, startY) = f[0], f[1]
        (endX, endY) = f[2], f[3]

        # crop the detected face region
        face_crop = np.copy(frame[startY:endY,startX:endX])

        if (face_crop.shape[0]) < 10 or (face_crop.shape[1]) < 10:
            continue

        # preprocessing for gender detection model
        face_crop = cv2.resize(face_crop, (128,128))
        face_crop = face_crop.astype("float") / 255.0
        face_crop = img_to_array(face_crop)
        face_crop = np.expand_dims(face_crop, axis=0)

        # apply gender detection on face
        conf = model.predict(face_crop)[0] # model.predict return a 2D matrix, ex: [[9.9993384e-01 7.4850512e-05]]

        # get label with max accuracy
        idx = np.argmax(conf)
        label = classes[idx]

        return idx, label
