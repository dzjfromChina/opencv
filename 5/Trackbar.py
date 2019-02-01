"""""""""""""""""""""""""""""""""""""""""""""""
@author: duzj                                   
@contact: dzj0574@163.com                     
@software: PyCharm                    
@file: Trackbar.py                             
@time: 2019/2/1 14:28                        
"""""""""""""""""""""""""""""""""""""""""""""""

"""
Here we will create a simple application which shows the color you specify. You have a window which shows the color and three trackbars to specify each of B,G,R colors. You slide the trackbar and correspondingly window color changes. By default, initial color will be set to Black.

在这里，我们将创建一个简单的应用程序，
显示您指定的颜色。您有一个显示颜色的窗口和三个trackbar来指定每个B、G、R颜色。
你滑动轨迹条，相应的窗口颜色就会改变。默认情况下，初始颜色将设置为黑色


For cv2.getTrackbarPos() function, first argument is the trackbar name, second one is the window name to which it is attached, third argument is the default value, fourth one is the maximum value and fifth one is the callback function which is executed everytime trackbar value changes. The callback function always has a default argument which is the trackbar position. In our case, function does nothing, so we simply pass.

对于cv2.getTrackbarPos()函数，
回调函数总是有一个默认参数，即trackbar位置。
在我们的例子中，函数什么也不做，所以我们只是传递。

Another important application of trackbar is to use it as a button or switch. OpenCV, by default, doesn't have button functionality. So you can use trackbar to get such functionality. In our application, we have created one switch in which application works only if switch is ON, otherwise screen is always black.

trackbar的另一个重要应用是将其用作按钮或开关。
默认情况下，OpenCV没有按钮功能。所以你可以使用trackbar来获得这样的功能。
在我们的应用程序中，我们已经创建了一个开关，在这个开关中应用程序只在开关打开时才工作，否则屏幕总是黑色的。
"""

import cv2
import numpy as np


def nothing(x):
    pass


#Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')

"""
create trackbars for color change
第一个参数是trackbar名称，
第二个参数是它所附加的窗口名称，
第三个参数是默认值，
第四个参数是最大值，
第五个参数是回调函数，
每次trackbar值发生变化时都会执行回调函数。
"""
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)
# create switch for ON/OFF functionality
switch = '0:OFF/1:ON'
cv2.createTrackbar(switch, 'image',0,1,nothing)


while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    # get current positions of four trackbars  取值
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    s = cv2.getTrackbarPos(switch,'image')
    if s == 0:
        # 数字都为0  就是黑色
        img[:] = 0
    else:
        # 根据调色变化
        img[:] = [b,g,r]
cv2.destroyAllWindows()