"""""""""""""""""""""""""""""""""""""""""""""""
@author: duzj                                   
@contact: dzj0574@163.com                     
@software: PyCharm                    
@file: MoreAdvancedDemo.py                             
@time: 2019/2/1 13:56                        
"""""""""""""""""""""""""""""""""""""""""""""""

"""
Now we go for a much better application. In this, we draw either rectangles or circles (depending on the mode we select) by dragging the mouse like we do in Paint application. So our mouse callback function has two parts, one to draw rectangle and other to draw the circles. This specific example will be really helpful in creating and understanding some interactive applications like object tracking, image segmentation etc.

现在我们来看一个更好的应用程序。
在这里，我们通过拖动鼠标来绘制矩形或圆形(这取决于我们选择的模式)，
就像在Paint应用程序中所做的那样。我们的鼠标回调函数有两部分，一部分用来画矩形，另一部分用来画圆。
这个具体的例子将非常有助于创建和理解一些交互式应用程序，如对象跟踪，图像分割等。
"""
import cv2
import numpy as np

# 创建画布
img = np.zeros((512, 512, 3), np.uint8)

drawing = False  # true if mouse is pressed
mode = True  # if True, draw rectangle. Press 'm' to toggle to curve
ix, iy = -1, -1


# mouse callback function
def draw_circle(event, x, y, flags, param):
    #声明 ix, iy, drawing, mode 是全局变量
    global ix, iy, drawing, mode
    if event == cv2.EVENT_LBUTTONDOWN:#鼠标左键按下
        drawing = True
        ix, iy = x, y
        print("ix iy:",ix, iy)
    elif event == cv2.EVENT_MOUSEMOVE:#鼠标移动
        #当项目启动的时候  鼠标只要在窗口里面  就会被捕捉
        print("x, y:",x, y)
        # 当左键按下才会触发
        if drawing == True:
            if mode == True:
                # 画矩形
                cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
            else:
                # 圆形
                cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
    elif event == cv2.EVENT_LBUTTONUP:#左键弹起
        drawing = False
        if mode == True:
            print("画矩形",ix, iy,x, y)
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
        else:
            print("画圆",x, y)
            cv2.circle(img, (x, y), 5, (0, 0, 255), -1)


# 这个就不必多说了
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)
while (1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        # 切换模式
        mode = not mode
    elif k == 27:
        break
cv2.destroyAllWindows()
