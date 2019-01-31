"""""""""""""""""""""""""""""""""""""""""""""""
@author: duzj                                   
@contact: dzj0574@163.com                     
@software: PyCharm                    
@file: WriteImage.py                             
@time: 2019/1/31 14:54                        
"""""""""""""""""""""""""""""""""""""""""""""""
import cv2

img = cv2.imread("1.jpg",1)
# 写入图片
# 第一个参数 ：图片名
# 第二个参数: 要写入的图片
cv2.imwrite("2.jpg",img)