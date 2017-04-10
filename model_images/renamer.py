import os
from PIL import Image
import PIL.ImageOps
import urllib.parse
from itertools import count
import random


"""
    Turnes every image file to 28*28
    Also invert color
    """

iid = count()
def random_id(length):
    number = '0123456789'
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    id = ''
    for i in range(0,length,2):
        id += random.choice(number)
        id += random.choice(alpha)
    return id

def resizer(cur_path):
    for a in os.listdir(cur_path):
        if(os.path.isdir('%s/%s'%(cur_path,a))):
            # resizer('%s/%s'%(cur_path,a))
            print('%s/%s'%(cur_path,str(a)))
        else:

            # img = Image.open('%s/%s'%(cur_path,a), 'r')
            # newNameTag= random_id(6)
            # newName= newNameTag + str(next(iid)) + ".png"
            # os.rename('%s/%s'%(cur_path,a),'%s/%s'%(cur_path,newName))
            try:
                img = Image.open('%s/%s'%(cur_path,a), 'r')
                newNameTag= random_id(6)
                newName= newNameTag + str(next(iid)) + ".png"
                os.rename('%s/%s'%(cur_path,a),'%s/%s'%(cur_path,newName))
                
            except:				
                print("file not image ",str(a))


resize_size=(56,56)
cur_path = os.path.dirname(os.path.abspath(__file__))
resizer(cur_path)
