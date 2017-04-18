from __future__ import print_function
import numpy as np
import cv2
from keras.optimizers import SGD
import os.path
from keras.models import model_from_json
import datetime
from PIL import Image
import requests
from io import BytesIO

def pic_to_np_array(count=int, kernel_width=56, kernel_height=56):
    """
    :param count: number of saved dissembled shoes locker picture
    :return numpy array of locker pictures
    """
    if(count==-1):
        print("count=-1!")

    im = cv2.imread('temp/box0.png')
    bigArray = np.asarray(im)
    # bigArray=bigArray*(1./255)
    # bigArray=np.swapaxes(bigArray,0,2)
    # bigArray=np.swapaxes(bigArray,1,2)
    for e in range(1,count):
        im = cv2.imread('temp/box%s.png'%e)
        onePicArray = np.asarray(im)
        # onePicArray=onePicArray*(1./255)
        # onePicArray=np.swapaxes(onePicArray,0,2)
        # onePicArray=np.swapaxes(onePicArray,1,2)
        bigArray= np.vstack((bigArray,onePicArray))
    bigArray= bigArray.reshape(-1,kernel_width,kernel_height,3)
    return bigArray

def predictShoe(shoeArray):
    """
    it checks the input files' state

    :param count: input count
    :return: probability that shoes exist
    """ 

    f_model = './model'
    model_filename = 'cnn_model.json'
    weights_filename = 'cnn_model_weights.hdf5'

    # 1. load model
    json_string = open(os.path.join(f_model, model_filename)).read()
    model = model_from_json(json_string)
    # sgd = SGD(lr=1e-2, decay=1e-6, momentum=0.9, nesterov=True)

    # # set compiler
    # model.compile(loss='mean_squared_error',
    #               optimizer=sgd,
    #               metrics=['accuracy'])
    model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

    model.load_weights(os.path.join(f_model, weights_filename))

    # 3. predict certainty
    # probability = model.predict_proba(shoeArray, batch_size=26, verbose=0)
    probability = model.predict(shoeArray, batch_size=26, verbose=0)
    return probability

def get_bigShoeBox_array(x, y, height, width, raspi_im="temp/raspi_pic.jpg"):
    """
    :param raspi_im
    :return : big shoe box position
    """

    image = cv2.imread(raspi_im)
    if image is None:
        print("Cannot find image %s", raspi_im)
        return
    #crop image
    crop_img = image[y : y+height, x : x+width]
    cv2.imshow("cropped", crop_img)
    cv2.waitKey(0)
    #turn crop image to np array
    npImage = np.asarray(crop_img) 
    # npImage=npImage*(1./255)
    # npImage=np.swapaxes(npImage,0,2)
    # npImage=np.swapaxes(npImage,1,2)
    return npImage

# def save_picture(self, ip_address="192.168.11.213"):
#     """
#     Save picture from raspi
#     :param ip_address
#     :param save_dir
#     :return True, False
#     """
#     time = datetime.datetime.today()
#
#     directory = "images/" + str(time.year) + "_" + str(time.month) + "_" + str(time.day)
#     savename = "images/" + str(time.year) + "_" + str(time.month) + "_" + str(time.day) + "/" \
#             + str(time.hour) + "_" + str(time.minute) + "_" + str(time.second) + ".png"
#     print(savename)
#
#     if not os.path.exists(directory):
#         os.makedirs(directory)
#
#     url= "http://" + ip_address + "/image.jpg"
#     response = requests.get(url)
#     img = Image.open(BytesIO(response.content))
#     img.save(savename)
#     img.save("recent.jpg")

