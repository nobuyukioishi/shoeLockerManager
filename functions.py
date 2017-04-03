from __future__ import print_function
import numpy as np
import cv2
from keras.optimizers import SGD
import os.path
from keras.models import model_from_json
from PIL import Image


def predict(fname=None, ffolder=None):
    """
    it checks the input files' state

    :param fname: file name
    :param ffolder: path of the file
    :return: probability that shoes exist
    """
    if ffolder is not None:
        fpath = ffolder + "/" + fname
    else:
        fpath = fname

    if fname is None:
        print("error: predict() should have one augment")
        return 1

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

    # 2. load picture
    im = Image.open(fpath, 'r')

    if im is None:
        print("error: Can't open", fpath, ".")
        return 1

    # if the window does not meet our desired window size, resize it
    size = (56, 56)
    window = np.asarray(cv2.resize(cv2.imread(fpath), size)).reshape(-1, size[0], size[1], 3)

    # 3. predict certainty
    probability = model.predict(window, batch_size=26, verbose=1)

    return probability
