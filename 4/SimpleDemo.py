"""""""""""""""""""""""""""""""""""""""""""""""
@author: duzj                                   
@contact: dzj0574@163.com                     
@software: PyCharm                    
@file: SimpleDemo.py                             
@time: 2019/2/1 10:51                        
"""""""""""""""""""""""""""""""""""""""""""""""

"""
Here, we create a simple application which draws a circle on an image wherever we double-click on it.

在这里，我们创建一个简单的应用程序，它在我们双击的图像上画一个圆。

First we create a mouse callback function which is executed when a mouse event take place. Mouse event can be anything related to mouse like left-button down, left-button up, 
left-button double-click etc. It gives us the coordinates (x,y) for every mouse event. With this event and location, we can do whatever we like. To list all available events available, run the following code in Python terminal

首先，我们创建一个鼠标回调函数，该函数在鼠标事件发生时执行。
鼠标事件可以是任何与鼠标相关的东西，如左键向下、左键向上、左键双击等。它为每个鼠标事件提供坐标(x,y)。
有了这个事件和位置，我们可以做任何我们想做的事情。要列出所有可用的事件，请在Python终端中运行以下代码

import cv2
events = [i for i in dir(cv2) if 'EVENT' in i]
print( events )
"""



"""
Creating mouse callback function has a specific format which is same everywhere. It differs only in what the function does. So our mouse callback function does one thing, it draws a circle where we double-click. So see the code below. Code is self-explanatory from comments

创建鼠标回调函数有一种特定的格式，这种格式在任何地方都是相同的。它只在函数的作用上有所不同。
我们的鼠标回调函数会做一件事，它会在我们双击的地方画一个圆。参见下面的代码。代码是注释中自解释的
"""

import cv2
import numpy as np

#显示事件集合
# https://blog.csdn.net/qq_21033779/article/details/78365665  点击事件介绍
events = [i for i in dir(cv2) if 'EVENT' in i]
print( events )

# mouse callback function
def draw_circle(event,x,y,flags,param):
    # 捕获的事件是双击事件  x与y是捕获的
    if event == cv2.EVENT_LBUTTONDBLCLK:
        # 画圆参考 3号文件夹
        cv2.circle(img,(x,y),100,(255,0,0),-1)


# 创建一个画布
img = np.zeros((512,512,3), np.uint8)
# 取名
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.setMouseCallback('image',draw_circle)

while(1):
    #显示图片
    cv2.imshow('image',img)
    #按ESC 退出
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()