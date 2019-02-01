"""""""""""""""""""""""""""""""""""""""""""""""
@author: duzj                                   
@contact: dzj0574@163.com                     
@software: PyCharm                    
@file: AccessingImageProperties.py                             
@time: 2019/2/1 16:14                        
"""""""""""""""""""""""""""""""""""""""""""""""

"""
Image properties include number of rows, columns and channels, type of image data, number of pixels etc.

图像属性包括行数、列数和通道数、图像数据类型、像素数等。

Shape of image is accessed by img.shape. It returns a tuple of number of rows, columns and channels (if image is color)

图像的形状由img.shape访问。它返回行、列和通道数的元组(如果图像是彩色的)

If image is grayscale, tuple returned contains only number of rows and columns. So it is a good method to check if loaded image is grayscale or color image.

如果图像是灰度的，返回的元组只包含行数和列数。因此，检测加载的图像是灰度图像还是彩色图像是一个很好的方法。
"""

import cv2
import numpy as np

# 首先加载图片
img = cv2.imread('1.jpg')

#(1080, 1440, 3)   1080*1440 3个通道
print( img.shape )

#总像素数  1080*1440*3
print( img.size )

# 图片数据类型 uint8
print( img.dtype )
