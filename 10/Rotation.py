"""""""""""""""""""""""""""""""""""""""""""""""
@author: duzj                                   
@contact: dzj0574@163.com                     
@software: PyCharm                    
@file: Rotation.py                             
@time: 2019/2/9 15:31                        
"""""""""""""""""""""""""""""""""""""""""""""""
import cv2

img = cv2.imread('1.png',0)
rows,cols = img.shape

"""
Rotation of an image for an angle θ is achieved by the transformation matrix of the form
图像的旋转一个角度θ是通过变换矩阵的形式
                    M=[cosθ sinθ 
                      −sinθ cosθ]
But OpenCV provides scaled rotation with adjustable center of rotation so that you can rotate at any location you prefer. Modified transformation matrix is given by

但是OpenCV提供了可调旋转中心的缩放旋转，这样你可以在任何你喜欢的位置旋转。修正后的变换矩阵为

    [α β (1−α)⋅center.x−β⋅center.y
    -β α β⋅center.x+(1−α)⋅center.y]
where:
    α=scale⋅cosθ,
    β=scale⋅sinθ
    
To find this transformation matrix, OpenCV provides a function, cv2.getRotationMatrix2D. Check below example which rotates the image by 90 degree with respect to center without any scaling.

为了找到这个变换矩阵，OpenCV提供了一个函数cv2.getRotationMatrix2D。检查下面的例子，它旋转图像90度相对于中心没有任何缩放。

"""

# /2 是为了根据图片中心 旋转 90度
M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
print(M)
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()