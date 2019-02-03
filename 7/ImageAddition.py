"""""""""""""""""""""""""""""""""""""""""""""""
@author: duzj                                   
@contact: dzj0574@163.com                     
@software: PyCharm                    
@file: ImageAddition.py                             
@time: 2019/2/3 9:07                        
"""""""""""""""""""""""""""""""""""""""""""""""

"""
You can add two images by OpenCV function, cv2.add() or simply by numpy operation, res = img1 + img2. Both images should be of same depth and type, or second image can just be a scalar value.

您可以通过OpenCV函数cv2.add()或简单的numpy操作res = img1 + img2来添加两个图像。
两个图像的深度和类型应该相同，否则第二个图像只能是标量值。
"""

import numpy as np
import cv2

x = np.uint8([250])
y = np.uint8([10])

# 250+10 = 260 => 255
print( cv2.add(x,y) )

print( x+y )

