"""""""""""""""""""""""""""""""""""""""""""""""
@author: duzj                                   
@contact: dzj0574@163.com                     
@software: PyCharm                    
@file: AccessingAndModifyingPixelValues.py                             
@time: 2019/2/1 15:35                        
"""""""""""""""""""""""""""""""""""""""""""""""

import cv2
import numpy as np

# 首先加载图片
img = cv2.imread('1.jpg')

"""
You can access a pixel value by its row and column coordinates. For BGR image, it returns an array of Blue, Green, Red values. For grayscale image, just corresponding intensity is returned. 

可以通过像素的行坐标和列坐标访问像素值。
对于BGR图像，它返回一个包含蓝色、绿色和红色值的数组。对于灰度图像，只返回相应的强度
"""

px = img[100,100]
print( px )

# 1 其实是下标   0获取B 1获取G 2获取R
blue = img[100,100,1]
print( blue )

#修改某一个点的颜色  这里修改为黑色  就会有一个黑色的点
img[100,100] = [0,0,0]
print( img[100,100] )


"""
warning 
Numpy is a optimized library for fast array calculations. So simply accessing each and every pixel values and modifying it will be very slow and it is discouraged.

警告 
Numpy是一个用于快速数组计算的优化库。因此，简单地访问每个像素值并修改它将是非常缓慢的，这是不鼓励的。
"""

"""
Better pixel accessing and editing method : 
更好的像素访问和编辑方法
"""
# 获取坐标10,10 的G
print("item:",img.item(10,10,2))
# 更改坐标10,,10 的G
img.itemset((10,10,2),100)
print("item:",img.item(10,10,2))

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()