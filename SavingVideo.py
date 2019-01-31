"""""""""""""""""""""""""""""""""""""""""""""""
@author: duzj                                   
@contact: dzj0574@163.com                     
@software: PyCharm                    
@file: SavingVideo.py                             
@time: 2019/1/31 16:23                        
"""""""""""""""""""""""""""""""""""""""""""""""

"""
So we capture a video, process it frame-by-frame and we want to save that video. For images, it is very simple, 
just use cv2.imwrite(). Here a little more work is required.

我们捕获一个视频，逐帧处理然后保存它。对于图像，它非常简单，只需使用cv2.imwrite()。这里还需要做一些工作。


This time we create a VideoWriter object. We should specify the output file name (eg: output.avi). 
Then we should specify the FourCC code (details in next paragraph). 
Then number of frames per second (fps) and frame size should be passed.
 And last one is isColor flag. If it is True, encoder expect color frame, otherwise it works with grayscale frame.

这次我们创建一个VideoWriter对象。我们应该指定输出文件名(例如:output.avi)。
然后我们应该指定FourCC代码(详细信息在下一段中)。然后应该传递每秒帧数(fps)和帧大小。
最后一个是isColor flag。如果是真的，编码器期望的颜色帧，否则它的工作与灰度帧。

FourCC is a 4-byte code used to specify the video codec.
 The list of available codes can be found in fourcc.org. 
 It is platform dependent. Following codecs works fine for me.

FourCC是一个4字节的代码，用于指定视频编解码器。可用代码的列表可以在fourcc.org中找到。
它依赖于平台。遵循编解码器对我来说很好
https://en.wikipedia.org/wiki/FourCC

In Fedora: DIVX, XVID, MJPG, X264, WMV1, WMV2. (XVID is more preferable. MJPG results in high size video. X264 gives very small size video)
In Windows: DIVX (More to be tested and added)
In OSX: MJPG (.mp4), DIVX (.avi), X264 (.mkv).


"""

import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
# output.avi 保存文件的名字
# 这里的20应该是 fps 码率
# (640,480) 尺寸
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        # 读取每一帧并且旋转
        frame = cv2.flip(frame, 1)
        # write the flipped frame 保存每一帧 但是并没有写入磁盘
        out.write(frame)
        # 显示
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
