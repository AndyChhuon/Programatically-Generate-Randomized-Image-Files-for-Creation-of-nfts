from random import seed
from random import randint
import numpy as np
from PIL import Image
import os




def gen_musk(): #Generate musk image (60x60)
  musk_image = [
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, a1, bg, bg, bg, a1, bg, bg, a1, b1, b1, b1, b1, b1, b1, bg, a1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, a1, bg, bg, a1, a2, a2, a2, a1, a1, b1, b1, b1, b1, b1, b1, b1, b1, b1, a1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, a1, bg, a1, a1, b1, a1, a1, a1, a1, a1, b1, b1, a1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, a1, bg, a1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, a1, bg, bg, a1, a1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, a1, bg, a1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, a1, a1, a1, b1, a1, a1, b1, b1, b1, b1, b1, b1, b1, a1, a1, a1, a1, a1, b1, b1, a1, b1, b1, a1, a1, a1, b1, b1, b1, b1, a1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, a1, bg, a1, a2, a1, a1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, a1, a1, a1, a1, a1, a1, b1, a1, a1, a1, a1, a1, b1, b1, a1, a1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, bg, a1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, a1, b1, a1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, a1, a1, a1, a1, a1, b1, b1, a1, b1, b1, b1, b1, b1, b1, b1, b1, b1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, a1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, a1, a1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ],
    [bg, bg, bg, bg, bg, bg, bg, a1, a1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ],
    [bg, bg, bg, bg, bg, a1, a1, a1, a1, a1, b1, b1, b1, b1, b1, a2, a2, a2, a1, a1, a1, a1, a1, b2, b2, b2, b2, b2, b2, b2, b3, b3, b3, b3, b3, b3, b3, b3, b3, b1, b1, b1, b1, b1, b1, b1, b1, b1, b1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ],
    [bg, bg, bg, bg, bg, bg, bg, b1, b1, b1, b1, b1, b1, b1, b1, b4, b4, b4, b5, b5, b5, b5, b5, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b12, b1, b1, b1, b1, b1, a1, b1, b1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ],
    [bg, bg, bg, bg, bg, bg, a1, b1, b1, b1, b1, b1, b1, b4, b4, b4, b4, b4, b5, b5, b5, b5, b5, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b12, b1, b1, b1, b1, b1, b1, b1, b1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ],
    [bg, bg, bg, bg, bg, bg, bg, a1, b1, b1, b1, b1, b9, b4, b4, b4, b4, b4, b5, b5, b5, b5, b5, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b12, b1, b1, b1, a1, b1, b1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ],
    [bg, bg, bg, bg, bg, bg, bg, a1, b1, b1, b1, b1, b9, b4, b4, b4, b4, b5, b5, b5, b5, b5, b5, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b12, b1, b1, b1, a1, b1, b1, b1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:16
    [bg, bg, bg, bg, bg, bg, a1, b1, b1, b1, b1, b1, b9, b4, b4, b4, b4, b5, b5, b5, b5, b5, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b12, b1, b1, b1, a1, b1, b1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:17
    [bg, bg, bg, bg, bg, bg, bg, b1, b1, b1, b1, b7, b4, b4, b4, b4, b4, b5, b5, b5, b5, b5, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b12, b1, b1, b1, a1, b1, b1, b1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:18
    [bg, bg, bg, bg, bg, bg, bg, b1, b1, b1, b1, b7, b4, b4, b4, b4, b4, b5, b5, b5, b5, b5, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b12, b1, b1, b1, a1, b1, b1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:19
    [bg, bg, bg, bg, bg, bg, bg, bg, b1, b1, b7, b7, b4, b4, b4, b4, b4, b5, b5, b5, b5, b5, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b12, b1, b1, b1, a1, b1, b1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:20
    [bg, bg, bg, bg, bg, bg, bg, bg, b1, b1, b7, b7, b4, b4, b4, b4, b4, b5, b5, b5, b5, b5, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b12, b1, b1, b1, b1, b1, b1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:21
    [bg, bg, bg, bg, bg, bg, bg, bg, b1, b1, b7, b7, b4, b4, b4, b4, b4, b5, b5, b5, b5, b5, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b12, b1, b1, b1, b1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:22
    [bg, bg, bg, bg, bg, bg, bg, bg, b1, b1, b7, b7, b7, b4, b4, b4, b4, b4, b5, b5, b5, b5, b5, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b12, b1, b1, b1, b1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:23
    [bg, bg, bg, bg, bg, bg, bg, bg, b1, b1, b7, b7, b7, b4, b4, b4, b4, b4, b5, b5, b5, b5, b5, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b12, b1, b1, b1, b1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:24
    [bg, bg, bg, bg, bg, bg, bg, bg, b1, b1, b7, b7, b7, b4, b4, b4, b4, b4, b5, b5, b5, b5, b5, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b12, b1, b1, b1, b1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:25
    [bg, bg, bg, bg, bg, bg, bg, bg, b1, b1, b7, b7, b7, a1, a1, a1, a1, a1, a1, a1, a1, n1, n1, n3, n3, n3, n3, n3, n3, n3, a1, a1, a1, a1, a1, a1, a1, b6, b6, b6, b6, b6, b6, b12, b1, b1, b1, b1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:26
    [bg, bg, bg, bg, bg, bg, bg, bg, b1, b1, b7, b7, a1, a1, a1, a1, a1, a1, a1, a1, a1, a1, n1, n1, n3, b6, b6, b6, n3, a1, a1, a1, a1, a1, a1, a1, a1, a1, b6, b6, b6, b6, b6, b12, b1, b1, b1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:27
    [bg, bg, bg, bg, bg, bg, bg, bg, b1, b1, b7, b7, b7, b7, b7, b7, n3, n3, n3, n3, n3, n3, n1, n1, n1, b6, b6, b6, n3, n3, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, n4, b12, b1, b1, b1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:28
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, b1, b7, b7, b7, b7, b7, b7, n3, n2, n2, n2, n2, n3, n3, n1, n1, b6, b6, b6, b6, b6, b6, n1, n1, n1, n1, b6, b6, b6, b6, b6, b6, n4, n4, b12, b1, b1, b1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:29
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, b1, b7, b7, b7, b9, b9, b7, n2, n2, i1, i1, n2, n2, n2, n1, n1, n3, b6, n3, b6, b6, n1, n2, i1, i1, n2, n2, b6, b6, b6, b6, n4, n4, n4, b12, b1, n4, n4, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:30
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, b1, b7, b7, b7, b9, b9, b7, n2, i2, i1, i1, i2, n2, n2, n2, n1, n3, b6, n3, b6, b6, n2, i2, i1, i1, i2, n2, n2, b6, b6, b6, n4, n4, n4, b12, b1, n4, n4, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:31
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, b1, b7, b7, b7, b9, b9, b9, b9, b9, b9, b9, b9, n3, b9, n2, n1, n3, b6, n3, b6, b6, b6, n1, n1, n1, n1, b6, b6, b6, b6, n4, n4, n4, n4, b12, b1, n4, n4, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:32
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, b1, b7, b7, b7, b7, b7, b9, b9, b9, b9, b9, n3, b9, b9, n2, n1, n3, b6, n3, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, n4, n4, n4, n4, b12, n4, n4, n4, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:33
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, b7, b7, b7, b7, b7, b9, b9, b9, b9, n3, n3, b9, b9, n2, n1, n3, b6, n3, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, n4, n4, n4, n4, n4, b12, n4, n3, n4, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:34
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, b7, b7, b7, b9, b9, b9, b9, b9, n3, n3, n3, b9, b9, n2, n1, n3, b6, n3, b6, b6, b6, b6, b6, b6, b6, b6, b6, b6, n4, n4, n4, n4, n4, n4, n4, n3, n4, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:35
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, b7, b7, b9, b9, b9, b9, b9, n3, n3, n3, n3, b9, b9, n2, n1, n3, b6, n3, b9, b6, b6, b6, b6, b6, b6, b6, b6, b6, n4, n4, n4, n4, n4, n4, n3, n3, n4, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:36
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, b7, b7, b9, b9, b9, b9, n3, n3, n3, n3, n3, b9, b9, n2, n1, n3, b6, n3, n3, b9, b6, b6, b6, b6, b6, b6, b6, b6, n4, n4, n4, n4, n4, n4, n3, n4, n4, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:37
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, b7, b7, b9, b9, b9, b9, n3, n3, n3, n3, n3, b9, n2, n2, n1, n1, b6, n3, n3, n3, b9, b6, b6, b6, b6, b6, b6, b6, n4, n4, n4, n4, n4, n4, n3, n4, n4, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:38
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, b7, b7, b9, b9, b9, b9, n3, n3, n3, n3, n3, b9, n2, n2, n4, n1, n3, n3, n4, n3, n3, b9, b6, b6, b6, b6, b6, b6, n4, n4, n4, n4, n4, n4, n4, n4, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:39
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, b7, b7, b9, b9, b9, b9, b9, n3, n3, n3, b9, b9, b9, b9, n1, n1, n1, n3, n3, n3, n3, n3, b9, b6, b6, b6, b6, b6, n4, b9, n4, n4, n4, n4, n4, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:40
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, b7, b7, b7, b9, b9, b9, b9, b9, b9, b9, b9, b9, b9, b9, b9, b9, n3, n3, n5, n5, n5, n3, n3, b9, b9, n3, b9, b9, b9, n4, n4, n4, n4, n4, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:41
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, b7, b7, b7, b7, b7, b9, b9, b9, b9, b9, b9, b9, b9, b9, b9, n5, n5, n5, n5, n5, n5, n5, n3, n3, n3, b9, n3, n3, b9, n4, n4, n4, n4, b9, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:42
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, b7, b7, b7, b7, b7, b9, b9, b9, b9, b9, n1, b9, b9, b9, n5, n5, n5, n5, n5, n5, n5, n5, n5, n5, n3, b9, n6, n6, b9, n4, n4, n4, n4, b9, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:43
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, b7, b7, b7, b7, b7, b9, b9, n3, b9, b9, n1, n1, m1, m2, m2, m2, m2, m2, m2, m2, m2, n5, n5, n5, n3, b9, n6, n6, b9, n4, n4, n4, b9, b9, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:44
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, b7, b7, b7, b7, b7, b9, n3, b9, b9, m1, m1, m1, t1, t2, t2, t2, t2, t2, t1, m1, m1, m1, m1, b9, n6, n6, n6, b9, n4, n4, b9, b9, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:45
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, b7, b7, b7, b7, b7, b7, b9, n3, n3, b9, b9, m1, m1, m2, m2, m2, m2, m3, m3, m3, n6, n6, n6, n6, n6, n6, b9, n3, n4, n4, b9, b9, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:46
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, b7, b7, b7, b7, b7, b7, b9, b9, b9, b9, b9, m1, m2, m2, m2, m2, m3, m3, n6, n6, n6, n6, n6, n6, b9, n3, n4, n4, b9, b9, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:47
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, b7, b7, b7, b7, b7, b7, b7, b9, b9, b9, b9, b9, b8, b8, b8, n6, n6, n6, n6, n6, n6, n6, n6, b9, n6, n4, n4, b9, b9, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:48
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, b7, b7, b7, b7, b7, b7, b9, b9, b9, b9, b8, b8, b8, b8, n6, n6, n6, n6, n6, n6, n6, n6, n6, n6, n4, b9, b9, b9, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:49
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, b7, b7, b7, b7, b9, b9, b9, b8, b8, b8, b8, b8, n6, n6, n6, n6, n6, n6, n6, n6, n6, n3, b9, b9, b9, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:50
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, b7, b7, b7, b7, b9, b8, b8, b8, b8, b8, b8, b8, n6, n6, n6, n6, n6, b8, b8, b8, b9, b9, b9, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:51
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, b7, b7, b7, b7, b8, b8, b8, b8, b8, b8, b8, b8, b8, b8, b8, b8, b8, b8, b9, b9, b9, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:52
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, b7, b7, b7, b7, b9, b8, b8, b8, b8, b8, b8, b8, b8, b8, b8, b8, b9, b9, b9, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:53
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, b7, b7, b7, b7, b7, b7, b7, b7, b7, b7, b7, b7, b7, b7, b7, b9, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ], #y:54
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, b9, b9, b9, b9, b9, b9, b9, b9, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg ],
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
  image = new_image.resize(dimensions, resample=0)
  image.save(image_path + '\musk_' + str(x) + '.png')

def add_glasses(glasses_type, glasses_size): 
  
  background = Image.open(image_path + '\musk_' + str(x) + '.png')

  if glasses_type == 'normal':

    foreground_image = Image.open(image_path_accessories + r'\glasses.png')

    if glasses_size == 'big_glasses':

      foreground = foreground_image.resize(dimensions_big_glasses, resample=0)
      background.paste(foreground, (110, 290), foreground)
      background.show()

    elif glasses_size == 'grandma_glasses':

      foreground = foreground_image.resize(dimensions_gma_glasses, resample=0)
      background = Image.open(image_path + '\musk_' + str(x) + '.png')
      background.paste(foreground, (160, 290), foreground)
      background.show()
  
  elif glasses_type == 'spooderman':
    foreground_image = Image.open(image_path_accessories + r'\glasses_color.png')
    
    if glasses_size == 'big_glasses':

      foreground = foreground_image.resize(dimensions_big_spooder, resample=0)
      background.paste(foreground, (100, 290), foreground)
      background.show()

    elif glasses_size == 'grandma_glasses':

      foreground = foreground_image.resize(dimensions_gma_spooder, resample=0)
      background = Image.open(image_path + '\musk_' + str(x) + '.png')
      background.paste(foreground, (150, 290), foreground)
      background.show()

  elif glasses_type == 'nerd':
    foreground_image = Image.open(image_path_accessories + r'\nerd_glasses.png')
    
    if glasses_size == 'big_glasses':

      foreground = foreground_image.resize(dimensions_big_glasses, resample=0)
      background.paste(foreground, (110, 265), foreground)
      background.show()

    elif glasses_size == 'grandma_glasses':

      foreground = foreground_image.resize(dimensions_gma_glasses, resample=0)
      background = Image.open(image_path + '\musk_' + str(x) + '.png')
      background.paste(foreground, (160, 318), foreground)
      background.show()
  
  background.save(image_path + '\musk_' + str(x) + '.png')




def generate_seed():
    seed_1 = randint(0,1000)
    seed(seed_1)

dimensions = 600, 600
dimensions_big_glasses = 300,300 
dimensions_gma_glasses = 200,200
dimensions_big_spooder = 400, 400
dimensions_gma_spooder = 275,275
image_path = r"c:\Users\andyc\OneDrive\Desktop\Visual Studio Code\Nft_project\Images"
image_path_accessories = r"c:\Users\andyc\OneDrive\Desktop\Visual Studio Code\Nft_project\Accessories"


a1= (79,69,68)
a2= (49,43,42)
b9 = (212,181,172)
n1 = (194,160,149)
n2 = (186,152,141)
n3 = (248,212,201)
n4 = (117,106,104)
i1 = (83,85,74)
i2 = (227,227,227)
m1 = (188,102,102)
m2 = (203,135,135)
m3 = (201,147,147)
t1 = (214,214,214)
t2 = (227,227,227)


for x in range(1):
  
  seed(x+21)
  bg = (randint(0,256), randint(0,256), randint(0,256))
  generate_seed()
  b1 = (randint(0,256), randint(0,256), randint(0,256))
  generate_seed()
  b2= (randint(0,256), randint(0,256), randint(0,256))
  generate_seed()
  b3= (randint(0,256), randint(0,256), randint(0,256))
  generate_seed()
  b4= (randint(0,256), randint(0,256), randint(0,256))
  generate_seed()
  b5= (randint(0,256), randint(0,256), randint(0,256))
  generate_seed()
  b6= (randint(0,256), randint(0,256), randint(0,256))
  generate_seed()
  b7= (randint(0,256), randint(0,256), randint(0,256))
  generate_seed()
  b8= (randint(0,256), randint(0,256), randint(0,256))
  generate_seed()
  b12= (randint(0,256), randint(0,256), randint(0,256))
  generate_seed()
  n5= (randint(0,256), randint(0,256), randint(0,256))
  generate_seed()
  n6= (randint(0,256), randint(0,256), randint(0,256))
  generate_seed()

  make_image()
  
  print()
  add_glasses('nerd', 'grandma_glasses')





  
