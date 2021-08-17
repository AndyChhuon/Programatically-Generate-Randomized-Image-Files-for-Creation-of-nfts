from random import seed
from random import randint
import numpy as np
from PIL import Image
import os
import random




def gen_musk(): #Generate musk image (60x60)
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
  



def make_image(): #Makes basic elon image
  pixel_list = gen_musk() 
  pixel_array = np.array(pixel_list, dtype=np.uint8) 

  new_image = Image.fromarray(pixel_array) 
  image = new_image.resize(DIMENSIONS, resample=0)
  image.save(IMAGE_PATH + '\musk_' + str(x) + '.png')
  image.show()






def add_glasses(glasses_type, glasses_size): 
  
  background = Image.open(IMAGE_PATH + '\musk_' + str(x) + '.png')

  if glasses_type == 'normal':

    foreground_image = Image.open(IMAGE_PATH_ACCESSORIES + r'\glasses.png')

    if glasses_size == 'big_glasses':

      foreground = foreground_image.resize(DIMENSIONS_BIG_GLASSES, resample=0)
      background.paste(foreground, (110, 290), foreground)
      background.show()

    elif glasses_size == 'grandma_glasses':

      foreground = foreground_image.resize(DIMENSIONS_GMA_GLASSES, resample=0)
      background.paste(foreground, (160, 290), foreground)
      background.show()
  
  elif glasses_type == 'spooderman':
    foreground_image = Image.open(IMAGE_PATH_ACCESSORIES + r'\glasses_color.png')
    
    if glasses_size == 'big_glasses':

      foreground = foreground_image.resize(DIMENSIONS_BIG_SPOODER, resample=0)
      background.paste(foreground, (100, 290), foreground)
      background.show()

    elif glasses_size == 'grandma_glasses':

      foreground = foreground_image.resize(DIMENSIONS_GMA_SPOODER, resample=0)
      background.paste(foreground, (150, 290), foreground)
      background.show()

  elif glasses_type == 'nerd':
    foreground_image = Image.open(IMAGE_PATH_ACCESSORIES + r'\nerd_glasses.png')
    
    if glasses_size == 'big_glasses':

      foreground = foreground_image.resize(DIMENSIONS_BIG_GLASSES, resample=0)
      background.paste(foreground, (110, 265), foreground)
      background.show()

    elif glasses_size == 'grandma_glasses':

      foreground = foreground_image.resize(DIMENSIONS_GMA_GLASSES, resample=0)
      background.paste(foreground, (160, 318), foreground)
      background.show()
      
  background.save(IMAGE_PATH + '\musk_' + str(x) + '.png')







def add_eyes(eyes_type):

  background = Image.open(IMAGE_PATH + '\musk_' + str(x) + '.png')

  if eyes_type == 'demon':
    
    foreground_image = Image.open(IMAGE_PATH_ACCESSORIES + r'\red_eye.png')
    foreground = foreground_image.resize(DIMENSIONS_DEMON, resample=0)
    background.paste(foreground, (164, 286), foreground) 
    background.show()


  elif eyes_type == 'lizard':
      
    foreground_image = Image.open(IMAGE_PATH_ACCESSORIES + r'\lizard_eye.png')
    foreground = foreground_image.resize(DIMENSIONS_LIZARD, resample=0)
    background.paste(foreground, (170, 291), foreground) 
    background.show()

  background.save(IMAGE_PATH + '\musk_' + str(x) + '.png')


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



nb_images = 5

DIMENSIONS = 600, 600
DIMENSIONS_BIG_GLASSES = 300,300 
DIMENSIONS_GMA_GLASSES = 200,200
DIMENSIONS_BIG_SPOODER = 400, 400
DIMENSIONS_GMA_SPOODER = 275, 275
DIMENSIONS_LIZARD = 36, 36 
DIMENSIONS_DEMON = 47,47
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

SKIN_OPTIONS = {'random_color' : 85, 'human_elon' : 15}
NORMAL_HAIR = {'yes': 25, 'no': 75}
GLASSES_TYPE_OPTIONS = {'' : 75, 'normal' : 10, 'spooderman' : 10, 'nerd' : 5}
GLASSES_SIZE_OPTIONS = {'big_glasses' : 80, 'grandma_glasses' : 20}
EYES_OPTIONS = {'' : 92, 'demon' : 5, 'lizard' : 3}
JOINT = {'yes': 10, 'no': 90}



#pick attributes

list_skin_options = random.choices(list(SKIN_OPTIONS.keys()), weights = SKIN_OPTIONS.values(), k = nb_images) #**verify tha glasses_size is not included in map if glasses type is ''
list_normal_hair = random.choices(list(NORMAL_HAIR.keys()), weights = NORMAL_HAIR.values(), k = nb_images)
list_glasses_type = random.choices(list(GLASSES_TYPE_OPTIONS.keys()), weights = GLASSES_TYPE_OPTIONS.values(), k = nb_images)
list_glasses_size = random.choices(list(GLASSES_SIZE_OPTIONS.keys()), weights = GLASSES_SIZE_OPTIONS.values(), k = nb_images)
list_eyes_options = random.choices(list(EYES_OPTIONS.keys()), weights = EYES_OPTIONS.values(), k = nb_images)
list_joint_option = random.choices(list(JOINT.keys()), weights = JOINT.values(), k = nb_images)

print(list_skin_options)
print (list_normal_hair)
print(list_glasses_type)
print(list_glasses_size)
print(list_eyes_options)
print(list_joint_option)



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


  #Generate basic image with colors
  make_image()

  if list_eyes_options[x] != '':
    add_eyes(list_eyes_options[x])
  
  if list_glasses_type != '':
    add_glasses(list_glasses_type[x], list_glasses_size[x])


