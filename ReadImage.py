"""""""""""""""""""""""""""""""""""""""""""""""
@author: duzj                                   
@contact: dzj0574@163.com                     
@software: PyCharm                    
@file: ReadImage.py                             
@time: 2019/1/31 14:15                        
"""""""""""""""""""""""""""""""""""""""""""""""

import cv2
# 使用cv2.imread() 读取图片
# 第一个参数: 图片路径 图片必须在工作目录下
# 第二个参数: 0图片显示灰色  1是彩色   也可以是下面的3个 参数
"""
    cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
    cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
    cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel
"""
img = cv2.imread("1.jpg",cv2.IMREAD_COLOR)
# 加了这一行可以控制窗口的大小
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# cv2.imshow() 显示图片
# 第一个参数: 显示框的名字
#第二个参数:  读取到的图片
cv2.imshow("image",img)
# 按下任意键盘键  就会关闭
cv2.waitKey(0)
cv2.destroyAllWindows()