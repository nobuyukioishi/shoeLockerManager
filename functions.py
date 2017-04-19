from __future__ import print_function
import numpy as np
import cv2
import os.path
from keras.models import model_from_json
from PIL import Image, ImageStat
from datetime import datetime


def pic_to_np_array(count, kernel_width=56, kernel_height=56):
    """
    :param kernel_height
    :param kernel_width
    :param count: number of saved dissembled shoes locker picture
    :return numpy array of locker pictures
    """

    im = cv2.imread('temp/box0.png')
    big_array = np.asarray(im)
    for e in range(1, count):
        im = cv2.imread('temp/box%s.png' % e)
        one_pic_array = np.asarray(im)
        big_array = np.vstack((big_array, one_pic_array))
    big_array = big_array.reshape(-1, kernel_width, kernel_height, 3)
    return big_array


def predict_shoe(shoe_array):
    """
    it checks the input files' state
    :param shoe_array: all shoes array
    :return: probability that shoes exist
    """ 

    f_model = './model'
    model_filename = 'cnn_model.json'
    weights_filename = 'cnn_model_weights.hdf5'

    # 1. load model
    json_string = open(os.path.join(f_model, model_filename)).read()
    model = model_from_json(json_string)

    model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

    model.load_weights(os.path.join(f_model, weights_filename))

    # 3. predict certainty
    probability = model.predict(shoe_array, batch_size=26, verbose=0)
    return probability


def get_big_shoe_box_array(x, y, height, width, latest_pic):
    """
    :param x
    :param y
    :param height
    :param width
    :param latest_pic
    :return : big shoe box position
    """

    image = cv2.imread(latest_pic)
    if image is None:
        print("Cannot find image %s", latest_pic)
        return
    # crop image
    crop_img = image[y: y+height, x: x+width]
    cv2.imshow("cropped", crop_img)
    cv2.waitKey(0)
    # turn crop image to np array
    np_image = np.asarray(crop_img)
    return np_image


def check_image(image):
    """
    checks if input page is good
    :param image: image to be checked
    :return: True if good False if bad
    """

    # find brightness of file
    im = Image.open(image).convert('L')
    stat = ImageStat.Stat(im)
    # bright picture have value about 230
    # TODO: check both black and normal picture
    print("Mean file = %s", stat.mean[0])
    if 100 < stat.mean[0] < 250:
        return True
    else:
        return False

@staticmethod
def save_to_folder_func(image="latest_pic.jpg"):
    """
    Save image to image_backup folder /images
    :param image: name of image
    """
    time = datetime.today()

    directory = "images/" + str(time.year) + "_" + str(time.month) + "_" + str(time.day)
    savename = "images/" + str(time.year) + "_" + str(time.month) + "_" + str(time.day) + "/" \
            + str(time.hour) + "_" + str(time.minute) + "_" + str(time.second) + ".png"
    print(savename)

    if not os.path.exists(directory):
        os.makedirs(directory)
        
    img = Image.open(image)
    img.save(savename)

