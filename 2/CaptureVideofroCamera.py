"""""""""""""""""""""""""""""""""""""""""""""""
@author: duzj                                   
@contact: dzj0574@163.com                     
@software: PyCharm                    
@file: CaptureVideofro Camera.py                             
@time: 2019/1/31 15:29                        
"""""""""""""""""""""""""""""""""""""""""""""""

#从摄像机捕捉视频

"""
Often, we have to capture live stream with camera. 
OpenCV provides a very simple interface to this. 
Let's capture a video from the camera (I am using the in-built webcam of my laptop), 
convert it into grayscale video and display it. Just a simple task to get started. 
To capture a video, you need to create a VideoCapture object. 
Its argument can be either the device index or the name of a video file. 
Device index is just the number to specify which camera. 
Normally one camera will be connected (as in my case). 
So I simply pass 0 (or -1). You can select the second camera by passing 1 and so on.

通常，我们必须用相机捕捉实时流。OpenCV提供了一个非常简单的接口。
让我们从相机中捕捉一个视频(我使用的是笔记本电脑内置的摄像头)，
将其转换成灰度视频并显示出来。开始只是一个简单的任务。

要捕获视频，您需要创建一个VideoCapture对象。
它的参数可以是设备索引，也可以是视频文件的名称。
设备索引只是指定哪个摄像机的编号。
通常会连接一个摄像头(就像我的情况)。所以我只传递0(或-1)您可以通过传递1来选择第二个摄像机，以此类推。
"""

import cv2
#获取一个摄像机 如果是笔记本就是笔记本的摄像头  记得开摄像头的权限
cap = cv2.VideoCapture(0)
#设置窗体   数据可以由下面的print显示
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 240)

# 原理应该是循环显示每一帧
while(True):
    # Capture frame-by-frame  开始读取
    ret, frame = cap.read()
    # 设置窗体
    # Our operations on the frame come here  设置视频的颜色 和读取照片类似  0就是灰色的
    gray = cv2.cvtColor(frame, 0)
    # 加上这一句话  就可以把图片水平翻转   0为垂直翻转   -1水平垂直翻转
    gray = cv2.flip(gray,1)
    # Display the resulting frame 显示视频流
    cv2.imshow('frame',gray)
    # 如果按 q 就是关闭  区分大小写
    print("宽度："+str(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) + "高度："+str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# When everything done, release the capture  释放cap
cap.release()
cv2.destroyAllWindows()