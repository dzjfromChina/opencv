"""""""""""""""""""""""""""""""""""""""""""""""
@author: duzj                                   
@contact: dzj0574@163.com                     
@software: PyCharm                    
@file: DrawingLine.py                             
@time: 2019/1/31 16:47                        
"""""""""""""""""""""""""""""""""""""""""""""""

"""
To draw a line, you need to pass starting and ending coordinates of line. 
We will create a black image and draw a blue line on it from top-left to bottom-right corners.

要绘制直线，您需要传递直线的起始坐标和结束坐标。我们将创建一个黑色的图像，并在上面画一条蓝色的线从左上角到右下角。
"""

import numpy as np
import cv2 as cv
# Create a black image
# 生成一个512*512的举证 矩阵的每一个元素是一个3*3的0矩阵
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
# 取(0,0) 和 (511,511) 两个点   (255,0,0)表示颜色  5表示粗细
cv.line(img,(0,0),(200,250),(255,255,0),1)

#显示
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()