from random import seed
from random import randint
import numpy as np
from PIL import Image
import os


dimensions = 3600, 180


def gen_musk(): #Generate musk image (60x60)
  musk_image = [
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, a1, bg, bg, bg, a1, bg, bg, a1, bg, bg, bg, bg, bg, bg, bg, a1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ],
  ]

  return musk_image

def make_image():
  pixel_list = gen_musk() #Gets list of image pixels
  pixel_array = np.array(pixel_list, dtype=np.uint8) #Turns list into array

  new_image = Image.fromarray(pixel_array) #Turns array to image
  image = new_image.resize(dimensions, resample=0)
  image.show()

for x in range(5):
  
  seed(x+21)

  bg = (randint(0,256), randint(0,256), randint(0,256))

  a1 = (randint(0,256), randint(0,256), randint(0,256))

  make_image()


