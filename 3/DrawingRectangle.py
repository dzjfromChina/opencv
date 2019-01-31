"""""""""""""""""""""""""""""""""""""""""""""""
@author: duzj                                   
@contact: dzj0574@163.com                     
@software: PyCharm                    
@file: DrawingRectangle.py                             
@time: 2019/1/31 17:06                        
"""""""""""""""""""""""""""""""""""""""""""""""

"""
To draw a rectangle, you need top-left corner and bottom-right corner of rectangle.
 This time we will draw a green rectangle at the top-right corner of image.

要绘制矩形，需要矩形的左上角和右下角。这次我们将在图像的右上角绘制一个绿色矩形。
"""

import numpy as np
import cv2 as cv
# Create a black image
# 生成一个512*512的举证 矩阵的每一个元素是一个3*3的0矩阵
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
# 取(384,0) 和 (510,128) 两个点   (0,255,0)表示颜色  5表示粗细
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)

#显示
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()