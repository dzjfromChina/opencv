"""""""""""""""""""""""""""""""""""""""""""""""
@author: duzj                                   
@contact: dzj0574@163.com                     
@software: PyCharm                    
@file: Translation.py                             
@time: 2019/2/9 15:18                        
"""""""""""""""""""""""""""""""""""""""""""""""

"""
Translation is the shifting of object's location. If you know the shift in (x,y) direction, let it be (tx,ty), you can create the transformation matrix M as follows:

                        M=[1 0 tx
                           0 1 ty]

You can take make it into a Numpy array of type np.float32 and pass it into cv2.warpAffine() function. See below example for a shift of (100,50): 



平移是物体位置的移动。如果你知道(x,y)方向的位移，就随它去吧   假设它是(tx,ty)你可以像这样创建变换矩阵M

你可以把它变成一个np类型的Numpy数组。浮点32并将其传递给cv2.warpAffine()函数。(100,50)的位移见下面的例子
"""

import cv2
import numpy as np
img = cv2.imread('1.png',0)

rows,cols = img.shape
# 向左平移10个像素  向下平移50个像素   上述1 0  0 1 表示平移
M = np.float32([[1,0,10],[0,1,10]])
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
Third argument of the cv2.warpAffine() function is the size of the output image, which should be in the form of **(width, height)**. Remember width = number of columns, and height = number of rows.

warpaffine()函数的第三个参数是输出图像的大小，它应该是**(宽度、高度)**的形式。记住宽度=列数，高度=行数。
"""