"""""""""""""""""""""""""""""""""""""""""""""""
@author: duzj                                   
@contact: dzj0574@163.com                     
@software: PyCharm                    
@file: ImageROI.py                             
@time: 2019/2/1 16:32                        
"""""""""""""""""""""""""""""""""""""""""""""""

"""
Sometimes, you will have to play with certain region of images. For eye detection in images, first face detection is done all over the image and when face is obtained, we select the face region alone and search for eyes inside it instead of searching whole image. It improves accuracy (because eyes are always on faces :D ) and performance (because we search for a small area)

有时，你必须处理图像的某些区域。对于图像中的眼睛检测，首先对整个图像进行人脸检测，当得到人脸时，
我们只选择人脸区域并在其中搜索眼睛，而不是搜索整个图像。它提高了准确性(因为眼睛总是盯着脸:D)和性能(因为我们寻找一个小区域)


ROI is again obtained using Numpy indexing. Here I am selecting the ball and copying it to another region in the image

ROI再次使用Numpy索引获得。这里我选择了球，并将它复制到图像的另一个区域
"""

import cv2
import numpy as np

# 首先加载图片
img = cv2.imread('roi.jpg')
"""
习惯的坐标表示 是 先 x 横坐标，再 y 纵坐标  在图像处理中，这种惯性思维尤其需要担心
因为在计算机中，图像是以矩阵的形式保存的，先行后列。所以，一张 宽×高×颜色通道＝480×256×3 
的图片会保存在一个 256×480×3 的三维张量中。
图像处理时也是按照这种思想进行计算的（其中就包括 OpenCV 下的图像处理），即 高×宽×颜色通道。
"""
print(img.shape)
# y1:y2,x1:x2  !!!!  把球取出来
ball = img[240:270, 280:315]

print(ball.shape)
print(img[0:30, 0:35].shape)

img[0:30, 0:35]= ball

"""
cv2.split() is a costly operation (in terms of time). So do it only if you need it. Otherwise go for Numpy indexing.

split()(就时间而言)是一个开销很大的操作。所以只有在你需要的时候才去做。否则就使用Numpy索引。
"""
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

cv2.line(img,(280,0),(280,280),(255,255,0),1)
cv2.line(img,(315,0),(315,315),(255,255,0),1)

cv2.line(img,(0,240),(450,240),(255,255,0),1)
cv2.line(img,(0,270),(450,270),(255,255,0),1)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
