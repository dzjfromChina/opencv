"""""""""""""""""""""""""""""""""""""""""""""""
@author: duzj                                   
@contact: dzj0574@163.com                     
@software: PyCharm                    
@file: MeasuringPerformanceWithOpenCV.py                             
@time: 2019/2/9 13:42                        
"""""""""""""""""""""""""""""""""""""""""""""""

"""
使用OpenCV测量性能

cv2.getTickCount function returns the number of clock-cycles after a reference event (like the moment machine was switched ON) to the moment this function is called. So if you call it before and after the function execution, you get number of clock-cycles used to execute a function. cv2.getTickFrequency function returns the frequency of clock-cycles, or the number of clock-cycles per second. So to find the time of execution in seconds, you can do following

cv2.getTickCount函数返回一个引用事件(比如打开力矩机)被调用时的时钟周期数。
如果在函数执行之前和之后调用它，就会得到用于执行函数的时钟周期数。


cv2.getTickFrequency函数返回时钟周期的频率，
即每秒的时钟周期数。要找到以秒为单位的执行时间，可以执行以下操作
"""
from time import sleep
import cv2

e1 = cv2.getTickCount()
# your code execution

cv2.imread('1.jpg')

e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()

print("e1:",e1," e2:",e2," time:",time," e2 - e1:",e2 - e1," cv2.getTickFrequency():",cv2.getTickFrequency())