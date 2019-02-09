"""""""""""""""""""""""""""""""""""""""""""""""
@author: duzj                                   
@contact: dzj0574@163.com                     
@software: PyCharm                    
@file: ObjectTracking.py                             
@time: 2019/2/9 14:34                        
"""""""""""""""""""""""""""""""""""""""""""""""

"""
Now we know how to convert BGR image to HSV, we can use this to extract a colored object. In HSV, it is more easier to represent a color than in BGR color-space. In our application, we will try to extract a blue colored object. So here is the method:

    Take each frame of the video
    Convert from BGR to HSV color-space
    We threshold the HSV image for a range of blue color
    Now extract the blue object alone, we can do whatever on that image we want.

Below is the code which are commented in detail : 


现在我们知道如何将BGR图像转换为HSV，我们可以使用它来提取彩色对象。 在HSV中，表示颜色比在BGR颜色空间中更容易。 在我们的应用程序中，我们将尝试提取蓝色对象。 所以这是方法：

     拍摄视频的每一帧

     从BGR转换为HSV色彩空间

     我们将HSV图像阈值为一系列蓝色

     现在单独提取蓝色对象，我们可以对我们想要的图像做任何事情。

以下是详细评论的代码：

"""


import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    ret, frame = cap.read()
    # 转换颜色空间 BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV  定义在HSV中 蓝色的范围
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    # 显示
    frame = cv2.flip(frame, 1)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    # 离开
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()


"""
There are some noises in the image. We will see how to remove them in later chapters. This is the simplest method in object tracking. Once you learn functions of contours, you can do plenty of things like find centroid of this object and use it to track the object, draw diagrams just by moving your hand in front of camera and many other funny stuffs.

图像中有一些杂音。我们将在后面的章节中看到如何删除它们。这是物体跟踪中最简单的方法。一旦你学会了等高线的函数，你可以做很多事情，
比如找到这个物体的质心，用它来跟踪这个物体，仅仅通过在相机前移动你的手来画图表，还有很多其他有趣的事情。
"""

