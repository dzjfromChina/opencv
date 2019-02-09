"""""""""""""""""""""""""""""""""""""""""""""""
@author: duzj                                   
@contact: dzj0574@163.com                     
@software: PyCharm                    
@file: PerspectiveTransformation.py                             
@time: 2019/2/9 15:46                        
"""""""""""""""""""""""""""""""""""""""""""""""
import cv2
import numpy as np
from matplotlib import pyplot as plt

"""
For perspective transformation, you need a 3x3 transformation matrix. Straight lines will remain straight even after the transformation. To find this transformation matrix, you need 4 points on the input image and corresponding points on the output image. Among these 4 points, 3 of them should not be collinear. Then transformation matrix can be found by the function cv2.getPerspectiveTransform. Then apply cv2.warpPerspective with this 3x3 transformation matrix.

对于透视变换，你需要一个3x3变换矩阵。
即使在转换之后，直线仍然是直线。
要找到这个变换矩阵，需要输入图像上的4个点和输出图像上的对应点。
在这4个点中，有3个不应该共线。
然后可以通过函数cv2. getperspective vetransform找到变换矩阵。
然后应用cv2。用这个3x3变换矩阵的warpPerspective。

"""
img = cv2.imread('1.png')
rows,cols,ch = img.shape

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(300,300))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()