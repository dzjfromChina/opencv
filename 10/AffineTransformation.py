"""""""""""""""""""""""""""""""""""""""""""""""
@author: duzj                                   
@contact: dzj0574@163.com                     
@software: PyCharm                    
@file: AffineTransformation.py                             
@time: 2019/2/9 15:40                        
"""""""""""""""""""""""""""""""""""""""""""""""

"""

In affine transformation, all parallel lines in the original image will still be parallel in the output image. To find the transformation matrix, we need three points from input image and their corresponding locations in output image. Then cv2.getAffineTransform will create a 2x3 matrix which is to be passed to cv2.warpAffine. Check below example, and also look at the points I selected (which are marked in Green color)

在仿射变换中，原图像中的所有平行线在输出图像中仍然是平行的。为了找到变换矩阵，
我们需要从输入图像中得到三个点，以及它们在输出图像中的对应位置。
然后cv2。getAffineTransform将创建一个2x3矩阵，该矩阵将传递给cv2.warpAffine。

检查下面的示例，并查看我选择的点(这些点用绿色标记)
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('1.png')
rows,cols,ch = img.shape

# 我们需要从输入图像中得到三个点，以及它们在输出图像中的对应位置。
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M = cv2.getAffineTransform(pts1,pts2)
dst = cv2.warpAffine(img,M,(cols,rows))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
