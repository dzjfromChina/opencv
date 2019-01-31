"""""""""""""""""""""""""""""""""""""""""""""""
@author: duzj                                   
@contact: dzj0574@163.com                     
@software: PyCharm                    
@file: DrawingPolygon.py                             
@time: 2019/1/31 17:19                        
"""""""""""""""""""""""""""""""""""""""""""""""

"""
To draw a polygon, first you need coordinates of vertices. Make those points into an array of shape ROWSx1x2 where ROWS are number of vertices and it should be of type int32. Here we draw a small polygon of with four vertices in yellow color.

要绘制多边形，首先需要顶点的坐标。将这些点组成形状  行x1x2 数组，
其中行是顶点数，类型为int32。这里我们用黄色画一个有四个顶点的小多边形。
"""

import numpy as np
import cv2 as cv
# Create a black image
# 生成一个512*512的举证 矩阵的每一个元素是一个3*3的0矩阵
img = np.zeros((512,512,3), np.uint8)

pts = np.array([[10,5],[20,80],[70,50],[50,10],[20,1]], np.int32)
print(pts)
# (-1,1,2) 似乎是个固定值
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,255,255))
#显示
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()
