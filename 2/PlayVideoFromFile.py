"""""""""""""""""""""""""""""""""""""""""""""""
@author: duzj                                   
@contact: dzj0574@163.com                     
@software: PyCharm                    
@file: PlayingVideoFromFile.py                             
@time: 2019/1/31 16:07                        
"""""""""""""""""""""""""""""""""""""""""""""""

"""
It is same as capturing from Camera, just change camera index with video file name. 
Also while displaying the frame, 
use appropriate time for cv2.waitKey(). If it is too less, 
video will be very fast and if it is too high, 
video will be slow (Well, that is how you can display videos in slow motion).
 25 milliseconds will be OK in normal cases.

它和相机拍照一样，只是用视频文件名改变相机索引。在显示帧的同时，
为cv2.waitKey()使用适当的时间。
如果它太小，视频就会很快，如果太高，视频就会很慢(这就是用慢动作显示视频的方法)。正常情况下25毫秒就可以了。
"""

import cv2
cap = cv2.VideoCapture('1.avi')

# 似乎没用了??
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 860)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 540)

while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, 1)
    cv2.imshow('frame',gray)
    # cv2.waitKey(1) 改变参数  会改变视频播放的速度  25刚刚好
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()