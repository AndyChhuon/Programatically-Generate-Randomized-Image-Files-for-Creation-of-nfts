from random import seed
from random import randint
import numpy as np
from PIL import Image
import os
import random




def gen_musk(): #Generate musk image (60x60) - note: could have used .convert('RGB')  .getdata() and make algorithm to replace a certain rgb value, shown beloc. Opted for matrix to have more customization freedom. (gotten by printing rgb values)

                #(ex:for item in datas:
                #if item[0] == 255 and item[1] == 222 and item[2] == 214:
                #newData.append((new_rgb))
                #else:
                #newData.append(item))
  musk_image = [
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, A1, bg, bg, bg, A1, bg, bg, A1, b1, b1, b1, b1, b1, b1, bg, A1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, A1, bg, bg, A1, A2, A2, A2, A1, A1, b1, b1, b1, b1, b1, b1, b1, b1, b1, A1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, A1, bg, A1, A1, b1, A1, A1, A1, A1, A1, b1, b1, A1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, A1, bg, A1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, A1, bg, bg, A1, A1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, A1, bg, A1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, A1, A1, A1, b1, A1, A1, b1, b1, b1, b1, b1, b1, b1, A1, A1, A1, A1, A1, b1, b1, A1, b1, b1, A1, A1, A1, b1, b1, b1, b1, A1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, A1, bg, A1, A2, A1, A1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, A1, A1, A1, A1, A1, A1, b1, A1, A1, A1, A1, A1, b1, b1, A1, A1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, bg, A1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, A1, b1, A1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, A1, A1, A1, A1, A1, b1, b1, A1, b1, b1, b1, b1, b1, b1, b1, b1, b1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, A1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, A1, A1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ],
    [bg, bg, bg, bg, bg, bg, bg, A1, A1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ],
    [bg, bg, bg, bg, bg, A1, A1, A1, A1, A1, b1, b1, b1, b1, b1, A2, A2, A2, A1, A1, A1, A1, A1, b2, b2, b2, b2, b2, b2, b2, b3, b3, b3, b3, b3, b3, b3, b3, b3, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ],
    [bg, bg, bg, bg, bg, bg, bg, b1, b1, b1, b1, b1, b1, b1, b1, b4, b4, b4, b5, b5, b5, b5, b5, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b12, b1, b1, b1, b1, b1, A1, b1, b1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ],
    [bg, bg, bg, bg, bg, bg, A1, b1, b1, b1, b1, b1, b1, b4, b4, b4, b4, b4, b5, b5, b5, b5, b5, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b12, b1, b1, b1, b1, b1, b1, b1, b1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ],
    [bg, bg, bg, bg, bg, bg, bg, A1, b1, b1, b1, b1, B9, b4, b4, b4, b4, b4, b5, b5, b5, b5, b5, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b12, b1, b1, b1, A1, b1, b1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ],
    [bg, bg, bg, bg, bg, bg, bg, A1, b1, b1, b1, b1, B9, b4, b4, b4, b4, b5, b5, b5, b5, b5, b5, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b12, b1, b1, b1, A1, b1, b1, b1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:16
    [bg, bg, bg, bg, bg, bg, A1, b1, b1, b1, b1, b1, B9, b4, b4, b4, b4, b5, b5, b5, b5, b5, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b12, b1, b1, b1, A1, b1, b1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:17
    [bg, bg, bg, bg, bg, bg, bg, b1, b1, b1, b1, b7, b4, b4, b4, b4, b4, b5, b5, b5, b5, b5, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b12, b1, b1, b1, A1, b1, b1, b1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:18
    [bg, bg, bg, bg, bg, bg, bg, b1, b1, b1, b1, b7, b4, b4, b4, b4, b4, b5, b5, b5, b5, b5, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b12, b1, b1, b1, A1, b1, b1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:19
    [bg, bg, bg, bg, bg, bg, bg, bg, b1, b1, b7, b7, b4, b4, b4, b4, b4, b5, b5, b5, b5, b5, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b12, b1, b1, b1, A1, b1, b1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:20
    [bg, bg, bg, bg, bg, bg, bg, bg, b1, b1, b7, b7, b4, b4, b4, b4, b4, b5, b5, b5, b5, b5, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b12, b1, b1, b1, b1, b1, b1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:21
    [bg, bg, bg, bg, bg, bg, bg, bg, b1, b1, b7, b7, b4, b4, b4, b4, b4, b5, b5, b5, b5, b5, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b12, b1, b1, b1, b1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:22
    [bg, bg, bg, bg, bg, bg, bg, bg, b1, b1, b7, b7, b7, b4, b4, b4, b4, b4, b5, b5, b5, b5, b5, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b12, b1, b1, b1, b1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:23
    [bg, bg, bg, bg, bg, bg, bg, bg, b1, b1, b7, b7, b7, b4, b4, b4, b4, b4, b5, b5, b5, b5, b5, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b12, b1, b1, b1, b1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:24
    [bg, bg, bg, bg, bg, bg, bg, bg, b1, b1, b7, b7, b7, b4, b4, b4, b4, b4, b5, b5, b5, b5, b5, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b12, b1, b1, b1, b1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:25
    [bg, bg, bg, bg, bg, bg, bg, bg, b1, b1, b7, b7, b7, A1, A1, A1, A1, A1, A1, A1, A1, N1, N1, N3, N3, N3, N3, N3, N3, N3, A1, A1, A1, A1, A1, A1, A1, b6, b6, b6, b6, b6, b6, b12, b1, b1, b1, b1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:26
    [bg, bg, bg, bg, bg, bg, bg, bg, b1, b1, b7, b7, A1, A1, A1, A1, A1, A1, A1, A1, A1, A1, N1, N1, N3, b6, b6, b6, N3, A1, A1, A1, A1, A1, A1, A1, A1, A1, b6, b6, b6, b6, b6, b12, b1, b1, b1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:27
    [bg, bg, bg, bg, bg, bg, bg, bg, b1, b1, b7, b7, b7, b7, b7, b7, N3, N3, N3, N3, N3, N3, N1, N1, N1, b6, b6, b6, N3, N3, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, n4, b12, b1, b1, b1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:28
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, b1, b7, b7, b7, b7, b7, b7, N3, N2, N2, N2, N2, N3, N3, N1, N1, b6, b6, b6, b6, b6, b6, N1, N1, N1, N1, b6, b6, b6, b6, b6, b6, n4, n4, b12, b1, b1, b1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:29
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, b1, b7, b7, b7, B9, B9, b7, N2, N2, I1, I1, N2, N2, N2, N1, N1, N3, b6, N3, b6, b6, N1, N2, I1, I1, N2, N2, b6, b6, b6, b6, n4, n4, n4, b12, b1, n4, n4, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:30
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, b1, b7, b7, b7, B9, B9, b7, N2, I2, I1, I1, I2, N2, N2, N2, N1, N3, b6, N3, b6, b6, N2, I2, I1, I1, I2, N2, N2, b6, b6, b6, n4, n4, n4, b12, b1, n4, n4, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:31
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, b1, b7, b7, b7, B9, B9, B9, B9, B9, B9, B9, B9, N3, B9, N2, N1, N3, b6, N3, b6, b6, b6, N1, N1, N1, N1, b6, b6, b6, b6, n4, n4, n4, n4, b12, b1, n4, n4, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:32
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, b1, b7, b7, b7, b7, b7, B9, B9, B9, B9, B9, N3, B9, B9, N2, N1, N3, b6, N3, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, n4, n4, n4, n4, b12, n4, n4, n4, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:33
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, b7, b7, b7, b7, b7, B9, B9, B9, B9, N3, N3, B9, B9, N2, N1, N3, b6, N3, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, n4, n4, n4, n4, n4, b12, n4, N3, n4, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:34
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, b7, b7, b7, B9, B9, B9, B9, B9, N3, N3, N3, B9, B9, N2, N1, N3, b6, N3, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, n4, n4, n4, n4, n4, n4, n4, N3, n4, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:35
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, b7, b7, B9, B9, B9, B9, B9, N3, N3, N3, N3, B9, B9, N2, N1, N3, b6, N3, B9, b6, b6, b6, b6, b6, b6, b6, b6, b6, n4, n4, n4, n4, n4, n4, N3, N3, n4, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:36
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, b7, b7, B9, B9, B9, B9, N3, N3, N3, N3, N3, B9, B9, N2, N1, N3, b6, N3, N3, B9, b6, b6, b6, b6, b6, b6, b6, b6, n4, n4, n4, n4, n4, n4, N3, n4, n4, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:37
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, b7, b7, B9, B9, B9, B9, N3, N3, N3, N3, N3, B9, N2, N2, N1, N1, b6, N3, N3, N3, B9, b6, b6, b6, b6, b6, b6, b6, n4, n4, n4, n4, n4, n4, N3, n4, n4, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:38
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, b7, b7, B9, B9, B9, B9, N3, N3, N3, N3, N3, B9, N2, N2, N7, N1, N3, N3, N7, N3, N3, B9, b6, b6, b6, b6, b6, b6, n4, n4, n4, n4, n4, n4, n4, n4, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:39
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, b7, b7, B9, B9, B9, B9, B9, N3, N3, N3, B9, B9, B9, B9, N1, N1, N1, N3, N3, N3, N3, N3, B9, b6, b6, b6, b6, b6, n4, B9, n4, n4, n4, n4, n4, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:40
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, b7, b7, b7, B9, B9, B9, B9, B9, B9, B9, B9, B9, B9, B9, B9, B9, N3, N3, n5, n5, n5, N3, N3, B9, B9, N3, B9, B9, B9, n4, n4, n4, n4, n4, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:41
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, b7, b7, b7, b7, b7, B9, B9, B9, B9, B9, B9, B9, B9, B9, B9, n5, n5, n5, n5, n5, n5, n5, N3, N3, N3, B9, N3, N3, B9, n4, n4, n4, n4, B9, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:42
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, b7, b7, b7, b7, b7, B9, B9, B9, B9, B9, N1, B9, B9, B9, n5, n5, n5, n5, n5, n5, n5, n5, n5, n5, N3, B9, n6, n6, B9, n4, n4, n4, n4, B9, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:43
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, b7, b7, b7, b7, b7, B9, B9, N3, B9, B9, N1, N1, M1, M2, M2, M2, M2, M2, M2, M2, M2, n5, n5, n5, N3, B9, n6, n6, B9, n4, n4, n4, B9, B9, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:44
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, b7, b7, b7, b7, b7, B9, N3, B9, B9, M1, M1, M1, T1, T2, T2, T2, T2, T2, T1, M1, M1, M1, M1, B9, n6, n6, n6, B9, n4, n4, B9, B9, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:45
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, b7, b7, b7, b7, b7, b7, B9, N3, N3, B9, B9, M1, M1, M2, M2, M2, M2, M3, M3, M3, n6, n6, n6, n6, n6, n6, B9, N3, n4, n4, B9, B9, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:46
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, b7, b7, b7, b7, b7, b7, B9, B9, B9, B9, B9, M1, M2, M2, M2, M2, M3, M3, n6, n6, n6, n6, n6, n6, B9, N3, n4, n4, B9, B9, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:47
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, b7, b7, b7, b7, b7, b7, b7, B9, B9, B9, B9, B9, b8, b8, b8, n6, n6, n6, n6, n6, n6, n6, n6, B9, n6, n4, n4, B9, B9, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:48
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, b7, b7, b7, b7, b7, b7, B9, B9, B9, B9, b8, b8, b8, b8, n6, n6, n6, n6, n6, n6, n6, n6, n6, n6, n4, B9, B9, B9, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:49
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, b7, b7, b7, b7, B9, B9, B9, b8, b8, b8, b8, b8, n6, n6, n6, n6, n6, n6, n6, n6, n6, N3, B9, B9, B9, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:50
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, b7, b7, b7, b7, B9, b8, b8, b8, b8, b8, b8, b8, n6, n6, n6, n6, n6, b8, b8, b8, B9, B9, B9, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:51
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, b7, b7, b7, b7, b8, b8, b8, b8, b8, b8, b8, b8, b8, b8, b8, b8, b8, b8, B9, B9, B9, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:52
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, b7, b7, b7, b7, B9, b8, b8, b8, b8, b8, b8, b8, b8, b8, b8, b8, B9, B9, B9, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:53
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, b7, b7, b7, b7, b7, b7, b7, b7, b7, b7, b7, b7, b7, b7, b7, B9, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:54
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, B9, B9, B9, B9, B9, B9, B9, B9, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ],


    


  ] 


  return musk_image
  




def gen_hair(normal_hair):

  if normal_hair == 'yes':
    b1 = (49,43,42)

  else:
    b1 = generate_pixel()
  
  return b1


def generate_pixel():
    rand_RGB = (randint(0,256), randint(0,256), randint(0,256))
    generate_seed()
    return rand_RGB


def generate_seed():
    seed_1 = randint(0,1000)
    seed(seed_1)



def make_image(check_background): #Makes basic elon image

  pixel_list = gen_musk() 
  pixel_array = np.array(pixel_list, dtype=np.uint8) 
  new_image = Image.fromarray(pixel_array) 

  image = new_image.resize(DIMENSIONS, resample=0)
  image.save(IMAGE_PATH + '\musk_' + str(x) + '.png')

  if check_background != '':
    image = new_image.resize(SMALL_DIMENSIONS, resample=0)
    image = Image.open(IMAGE_PATH + '\musk_' + str(x) + '.png')
    image = image.convert('RGBA')
    rgba = image.getdata()

    new_rgba = []

    for data in rgba: #make background pixels transparent
      if data[0] == bg[0] and data[1] == bg[1] and data[2] == bg[2]:
        new_rgba.append((255, 255, 255, 0))
      else:
        new_rgba.append(data)
      
    
    image.putdata(new_rgba)
    image = image.resize(DIMENSIONS, resample=0)

    add_background(check_background, image)


def add_background(type_background, image):
  foreground = image

  background = Image.open(IMAGE_PATH_ACCESSORIES + r'\background_' + type_background + '.png')
  background = background.resize(DIMENSIONS, resample=0)
  background.paste(foreground, (0, 0), foreground)
  background.save(IMAGE_PATH + '\musk_' + str(x) + '.png')





def add_eyes(eyes_type):

  background = Image.open(IMAGE_PATH + '\musk_' + str(x) + '.png')

  if eyes_type == 'demon':
    
    foreground_image = Image.open(IMAGE_PATH_ACCESSORIES + r'\red_eye.png')
    foreground = foreground_image.resize(DIMENSIONS_DEMON, resample=0)
    background.paste(foreground, (164, 286), foreground) 


  elif eyes_type == 'lizard':
      
    foreground_image = Image.open(IMAGE_PATH_ACCESSORIES + r'\lizard_eye.png')
    foreground = foreground_image.resize(DIMENSIONS_LIZARD, resample=0)
    background.paste(foreground, (170, 291), foreground) 

  background.save(IMAGE_PATH + '\musk_' + str(x) + '.png')






def add_glasses(glasses_type, glasses_size): 
  
  background = Image.open(IMAGE_PATH + '\musk_' + str(x) + '.png')

  if glasses_type == 'normal':

    foreground_image = Image.open(IMAGE_PATH_ACCESSORIES + r'\glasses.png')

    if glasses_size == 'big_glasses':

      foreground = foreground_image.resize(DIMENSIONS_BIG_GLASSES, resample=0)
      background.paste(foreground, (110, 290), foreground)

    elif glasses_size == 'grandma_glasses':

      foreground = foreground_image.resize(DIMENSIONS_GMA_GLASSES, resample=0)
      background.paste(foreground, (160, 290), foreground)
  
  elif glasses_type == 'spooderman':
    foreground_image = Image.open(IMAGE_PATH_ACCESSORIES + r'\glasses_color.png')
    
    if glasses_size == 'big_glasses':

      foreground = foreground_image.resize(DIMENSIONS_BIG_SPOODER, resample=0)
      background.paste(foreground, (100, 290), foreground)

    elif glasses_size == 'grandma_glasses':

      foreground = foreground_image.resize(DIMENSIONS_GMA_SPOODER, resample=0)
      background.paste(foreground, (150, 290), foreground)

  elif glasses_type == 'nerd':
    foreground_image = Image.open(IMAGE_PATH_ACCESSORIES + r'\nerd_glasses.png')
    
    if glasses_size == 'big_glasses':

      foreground = foreground_image.resize(DIMENSIONS_BIG_GLASSES, resample=0)
      background.paste(foreground, (110, 265), foreground)

    elif glasses_size == 'grandma_glasses':

      foreground = foreground_image.resize(DIMENSIONS_GMA_GLASSES, resample=0)
      background.paste(foreground, (160, 318), foreground)
      
  background.save(IMAGE_PATH + '\musk_' + str(x) + '.png')



def add_joint():
  background = Image.open(IMAGE_PATH + '\musk_' + str(x) + '.png')
  foreground_image = Image.open(IMAGE_PATH_ACCESSORIES + r'\blunt.png')
  foreground = foreground_image.resize(DIMENSIONS_BIG_SPOODER, resample=0)
  background.paste(foreground, (-135, 450), foreground)
  background.save(IMAGE_PATH + '\musk_' + str(x) + '.png')



def add_forehead_tatoo(forehead_tatoo):
  background = Image.open(IMAGE_PATH + '\musk_' + str(x) + '.png')

  if forehead_tatoo == 'bitcoin':
    foreground_image = Image.open(IMAGE_PATH_ACCESSORIES + r'\bitcoin.png')
    foreground = foreground_image.resize(DIMENSIONS_FOREHEAD, resample=0)
    background.paste(foreground, (210, 150), foreground)

  elif forehead_tatoo == 'doge':
    foreground_image = Image.open(IMAGE_PATH_ACCESSORIES + r'\dogecoin.png')
    foreground = foreground_image.resize(DIMENSIONS_FOREHEAD, resample=0)
    background.paste(foreground, (210, 150), foreground)

  elif forehead_tatoo == 'marijuana':
    foreground_image = Image.open(IMAGE_PATH_ACCESSORIES + r'\marijuana.png')
    foreground = foreground_image.resize(DIMENSIONS_FOREHEAD, resample=0)
    background.paste(foreground, (210, 150), foreground)
  
  background.save(IMAGE_PATH + '\musk_' + str(x) + '.png')


nb_images = 10

DIMENSIONS = 600, 600
SMALL_DIMENSIONS = 60,60
DIMENSIONS_BIG_GLASSES = 300,300 
DIMENSIONS_GMA_GLASSES = 200,200
DIMENSIONS_BIG_SPOODER = 400, 400
DIMENSIONS_GMA_SPOODER = 275, 275
DIMENSIONS_LIZARD = 36, 36 
DIMENSIONS_DEMON = 47,47
DIMENSIONS_FOREHEAD = 100, 100
IMAGE_PATH = r"c:\Users\andyc\OneDrive\Desktop\Visual Studio Code\Nft_project\Images"
IMAGE_PATH_ACCESSORIES = r"c:\Users\andyc\OneDrive\Desktop\Visual Studio Code\Nft_project\Accessories"


A1= (79,69,68)
A2= (49,43,42)
B9 = (212,181,172)
N1 = (194,160,149)
N2 = (186,152,141)
N3 = (248,212,201)
N7 = (117,106,104)
I1 = (83,85,74)
I2 = (227,227,227)
M1 = (188,102,102)
M2 = (203,135,135)
M3 = (201,147,147)
T1 = (214,214,214)
T2 = (227,227,227)

SKIN_OPTIONS = {'random_color': 85, 'human_elon': 15}
NORMAL_HAIR = {'yes': 25, '': 75}
GLASSES_TYPE_OPTIONS = {'': 75, 'normal': 10, 'spooderman': 10, 'nerd': 5}
GLASSES_SIZE_OPTIONS = {'big_glasses' : 80, 'grandma_glasses': 20}
EYES_OPTIONS = {'': 92, 'demon': 5, 'lizard': 3}
JOINT = {'yes': 10, '': 90}
FOREHEAD_OPTIONS = {'': 80, 'marijuana': 12, 'bitcoin': 5, 'doge': 3}
BACKGROUND_OPTIONS = {'': 52, 'night': 6, 'city': 6, 'car': 6, 'cinema': 6, 'bomb': 6, 'space': 1, 'abduction': 3, 'moon': 2, 'futuristic': 6, 'trees': 6}




#pick attributes

seed(42)

list_skin_options = random.choices(list(SKIN_OPTIONS.keys()), weights = SKIN_OPTIONS.values(), k = nb_images) #**verify tha glasses_size is not included in map if glasses type is ''
list_normal_hair = random.choices(list(NORMAL_HAIR.keys()), weights = NORMAL_HAIR.values(), k = nb_images)
list_glasses_type = random.choices(list(GLASSES_TYPE_OPTIONS.keys()), weights = GLASSES_TYPE_OPTIONS.values(), k = nb_images)
list_glasses_size = random.choices(list(GLASSES_SIZE_OPTIONS.keys()), weights = GLASSES_SIZE_OPTIONS.values(), k = nb_images)
list_eyes_options = random.choices(list(EYES_OPTIONS.keys()), weights = EYES_OPTIONS.values(), k = nb_images)
list_joint_option = random.choices(list(JOINT.keys()), weights = JOINT.values(), k = nb_images)
list_forehead_options = random.choices(list(FOREHEAD_OPTIONS.keys()), weights = FOREHEAD_OPTIONS.values(), k = nb_images)
list_background_options = random.choices(list(BACKGROUND_OPTIONS.keys()), weights = BACKGROUND_OPTIONS.values(), k = nb_images)


attributes_map = []

#Map attributes for all images
for i in range(nb_images): 
  attributes_dict = {
    'Skin_Type': list_skin_options[i],
    'Normal_Hair': list_normal_hair[i],
    'Glasses_type': list_glasses_type[i],
    'Glasses_size': list_glasses_size[i],
    'Eyes_Type': list_eyes_options[i],
    'Joint': list_joint_option[i],
    'Forehead type': list_forehead_options[i],
    'Background type' : list_background_options[i]
  }
  attributes_map.append(attributes_dict)

print(attributes_map)


#Make Image from Attributes
for x in range(nb_images):
  
  

  #Assign RGB value to groups of pixels

  if list_skin_options[x] == 'human_elon':   
    seed(x+21)
    bg = generate_pixel()
    b2= (154,136,131)
    b3= (165,145,140)
    b4= (212,181,172)
    b5= (248,212,201)
    b6= (255,222,214)
    b7= (194,160,149)
    b8= (242,212,201)
    b12= (158,139,136)
    n4 = (248,212,201)
    n5= (255,222,214)
    n6= (255,222,214)

    #add hair rgb value
    b1= gen_hair(list_normal_hair[x])



  
  elif list_skin_options[x] == 'random_color':
    seed(x+21)
    bg = generate_pixel()
    b2= generate_pixel()
    b3= generate_pixel()
    b4= generate_pixel()
    b5= generate_pixel()
    b6= generate_pixel()
    b7= generate_pixel()
    b8= generate_pixel()
    b12= generate_pixel()
    n4= generate_pixel()
    n5= generate_pixel()
    n6= generate_pixel()

    b1= gen_hair(list_normal_hair[x])


  
  make_image(list_background_options[x])


  if list_eyes_options[x] != '':
    add_eyes(list_eyes_options[x])

  if list_forehead_options[x] != '':
    add_forehead_tatoo(list_forehead_options[x])
  
  if list_glasses_type[x] != '':
    add_glasses(list_glasses_type[x], list_glasses_size[x])
   
  if list_joint_option[x] != '':
    add_joint()
  
  final_image = Image.open(IMAGE_PATH + '\musk_' + str(x) + '.png')
  final_image.show()

  



