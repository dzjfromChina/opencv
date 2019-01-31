"""""""""""""""""""""""""""""""""""""""""""""""
@author: duzj                                   
@contact: dzj0574@163.com                     
@software: PyCharm                    
@file: DrawingCircle.py                             
@time: 2019/1/31 17:09                        
"""""""""""""""""""""""""""""""""""""""""""""""

"""
To draw a circle, you need its center coordinates and radius. We will draw a circle inside the rectangle drawn above.

要画一个圆，你需要它的中心坐标和半径。我们将在上面画的矩形内画一个圆。
"""

import numpy as np
import cv2 as cv
# Create a black image
# 生成一个512*512的举证 矩阵的每一个元素是一个3*3的0矩阵
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
# 取(447,63) 圆心   63为半径  (0,255,0)表示颜色  5表示粗细
cv.circle(img,(447,63), 10, (0,0,255), -1)

#显示
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()