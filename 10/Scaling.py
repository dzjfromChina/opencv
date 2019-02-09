"""""""""""""""""""""""""""""""""""""""""""""""
@author: duzj                                   
@contact: dzj0574@163.com                     
@software: PyCharm                    
@file: Scaling.py                             
@time: 2019/2/9 15:08                        
"""""""""""""""""""""""""""""""""""""""""""""""

"""
Scaling is just resizing of the image. OpenCV comes with a function cv2.resize() for this purpose. The size of the image can be specified manually, or you can specify the scaling factor. Different interpolation methods are used. Preferable interpolation methods are cv2.INTER AREA for shrinking and cv2.INTER CUBIC (slow) & cv2.INTER LINEAR for zooming. By default, interpolation method used is cv2.INTER LINEAR for all resizing purposes. You can resize an input image either of following methods

缩放就是调整图像的大小。为此，OpenCV附带了一个函数cv2.resize()。
可以手动指定图像的大小，也可以指定缩放因子。
使用不同的插值方法。较好的插值方法是cv2。收缩和cv2的中间区域。立方间(慢)& cv2。用于缩放的内线性。

默认情况下，采用的插值方法是cv2。用于所有调整大小的目的。您可以调整输入图像的大小，方法如下
"""

import cv2

img = cv2.imread('1.jpg')
res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
#OR
height, width = img.shape[:2]
# 这边(width, height)  必须是整数   所以采用// 代替/
# 参考 https://blog.csdn.net/wobuzixun/article/details/79976647
width  = width//2
height = height//2
res = cv2.resize(img,(width, height), interpolation = cv2.INTER_CUBIC)

cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows()