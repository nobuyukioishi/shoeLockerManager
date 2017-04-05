import numpy as np
import cv2
def get_bigShoeBox_array(x, y, height, width, raspi_im="temp/raspi_pic.jpg"):
    """
    :param raspi_im
    :return : big shoe box position
    """

    image = cv2.imread(raspi_im)
    if image is None:
        print("Cannot find image %s", raspi_im)
        return
    cv2.imshow("cropped", image)
    cv2.waitKey(0)
    #turn crop image to np array
    npImage = np.asarray(crop_img)

    return npImage

if __name__ == '__main__':
    get_bigShoeBox_array(x=10, y=10, height=800, width=800)
