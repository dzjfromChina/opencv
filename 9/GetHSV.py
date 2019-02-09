"""""""""""""""""""""""""""""""""""""""""""""""
@author: duzj                                   
@contact: dzj0574@163.com                     
@software: PyCharm                    
@file: GetHSV.py                             
@time: 2019/2/9 14:59                        
"""""""""""""""""""""""""""""""""""""""""""""""
import cv2
import numpy as np

"""
通过BGR 
获取HSV的颜色值
"""
green = np.uint8([[[0,255,0 ]]])
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print( hsv_green )