"""""""""""""""""""""""""""""""""""""""""""""""
@author: duzj                                   
@contact: dzj0574@163.com                     
@software: PyCharm                    
@file: UsingMatplotlib.py                             
@time: 2019/1/31 15:18                        
"""""""""""""""""""""""""""""""""""""""""""""""

"""
Matplotlib is a plotting library for Python which gives you wide variety of plotting methods. 
You will see them in coming articles. Here, you will learn how to display image with Matplotlib. 
You can zoom images, save it etc using Matplotlib.

Matplotlib是一个用于Python的绘图库，它提供了多种绘图方法。您将在接下来的文章中看到它们。
在这里，您将学习如何使用Matplotlib显示图像。你可以使用Matplotlib放大图片，保存图片等。
"""

import cv2
from matplotlib import pyplot as plt
img = cv2.imread('1.jpg',0)

#用matplotlib显示图片  如果彩色就会出现问题(前提是cv2读取的# )
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

"""
warning 
Color image loaded by OpenCV is in BGR mode. But Matplotlib displays in RGB mode.
So color images will not be displayed correctly in Matplotlib if image is read with OpenCV.
Please see the exercises for more details.

OpenCV加载的警告彩色图像处于BGR模式。但是Matplotlib以RGB模式显示。
因此，如果使用OpenCV读取图像，Matplotlib中的彩色图像将不能正确显示。
"""