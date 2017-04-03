from __future__ import print_function
import numpy as np
import cv2
from keras.optimizers import SGD
import os.path
from keras.models import model_from_json
from PIL import Image

def pic_to_np_array(count=int, kernel_width=56, kernel_height=56):
    """
    :param count: number of saved dissembled shoes locker picture
    :return numpy array of locker pictures
    """
    if(count==0):
        print("count=0!")

    im = cv2.imread('temp/box0.png')
    bigArray = np.asarray(im)
    bigArray=bigArray*(1./255)
    bigArray=np.swapaxes(bigArray,0,2)
    bigArray=np.swapaxes(bigArray,1,2)
    for e in range(1,count):
        im = cv2.imread('temp/box%s.png'%e)
        onePicArray = np.asarray(im)
        onePicArray=onePicArray*(1./255)
        onePicArray=np.swapaxes(onePicArray,0,2)
        onePicArray=np.swapaxes(onePicArray,1,2)
        bigArray= np.vstack((bigArray,onePicArray))
    bigArray= bigArray.reshape(-1,3,kernel_width,kernel_height)
    return bigArray

def predict(shoeArray):
    """
    it checks the input files' state

    :param count: input count
    :return: probability that shoes exist
    """
    
    # if ffolder is not None:
    #     fpath = ffolder + "/" + fname
    # else:
    #     fpath = fname

    # if fname is None:
    #     print("error: predict() should have one augment")
    #     return 1

    f_model = './model'
    model_filename = 'cnn_model.json'
    weights_filename = 'cnn_model_weights.hdf5'

    # 1. load model
    json_string = open(os.path.join(f_model, model_filename)).read()
    model = model_from_json(json_string)
    sgd = SGD(lr=1e-2, decay=1e-6, momentum=0.9, nesterov=True)

    # set compiler
    model.compile(loss='mean_squared_error',
                  optimizer=sgd,
                  metrics=['accuracy'])
    model.load_weights(os.path.join(f_model, weights_filename))

    # 3. predict certainty
    probability = model.predict(shoeArray, batch_size=26, verbose=1)

    return probability

