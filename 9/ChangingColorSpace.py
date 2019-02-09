"""""""""""""""""""""""""""""""""""""""""""""""
@author: duzj                                   
@contact: dzj0574@163.com                     
@software: PyCharm                    
@file: ChangingColorSpace.py                             
@time: 2019/2/9 14:22                        
"""""""""""""""""""""""""""""""""""""""""""""""

"""
There are more than 150 color-space conversion methods available in OpenCV. But we will look into only two which are most widely used ones, BGR Gray and BGR HSV. For color conversion, we use the function cv2.cvtColor(input image, flag) where flag determines the type of conversion. For BGR Gray conversion we use the flags cv2.COLOR BGR2GRAY. Similarly for BGR HSV, we use the flag cv2.COLOR BGR2HSV. To get other flags, just run following commands in your Python terminal

OpenCV中有150多种颜色空间转换方法。但是我们将只研究两种应用最广泛的方法，BGR Gray和BGR HSV。
对于颜色转换，我们使用函数cv2.cvtColor(输入图像，标志)其中标志决定转换的类型。
对于BGR灰度转换，我们使用标志cv2.BGR2GRAY颜色。
类似地，对于BGR HSV，我们使用标志cv2。BGR2HSV颜色。要获得其他标志，只需在Python终端中运行以下命令


For HSV, Hue range is [0,179], Saturation range is [0,255] and Value range is [0,255]. Different softwares use different scales. So if you are comparing OpenCV values with them, you need to normalize these ranges.

HSV的色相范围为[0,179]，饱和度范围为[0,255]，值范围为[0,255]。
不同的软件使用不同的规模。如果你要比较OpenCV值和它们，你需要标准化这些范围。


HSV： https://baike.baidu.com/item/HSV/547122
"""

import cv2
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print( flags )

input_image = cv2.imread('1.jpg')
cv2.cvtColor(input_image, cv2.COLOR_BGR2HSV)


cv2.imshow('input_image',input_image)
cv2.waitKey(0)
cv2.destroyAllWindows()