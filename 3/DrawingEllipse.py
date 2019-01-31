"""""""""""""""""""""""""""""""""""""""""""""""
@author: duzj                                   
@contact: dzj0574@163.com                     
@software: PyCharm                    
@file: DrawingEllipse.py                             
@time: 2019/1/31 17:11                        
"""""""""""""""""""""""""""""""""""""""""""""""

"""
To draw the ellipse, we need to pass several arguments. One argument is the center location (x,y). Next argument is axes lengths (major axis length, minor axis length). angle is the angle of rotation of ellipse in anti-clockwise direction. startAngle and endAngle denotes the starting and ending of ellipse arc measured in clockwise direction from major axis. i.e. giving values 0 and 360 gives the full ellipse. For more details, check the documentation of cv.ellipse(). Below example draws a half ellipse at the center of the image.

要绘制椭圆，我们需要传递几个参数。
 center 参数是中心位置(x,y)  
 axes 参数是轴长(长轴，短轴)。
 angle 角度是椭圆逆时针旋转的角度。
 startAngle和endAngle表示从主轴顺时针方向测量的椭圆圆弧的起点和终点。
也就是说，给出0和360的值就得到了完整的椭圆。有关详细信息，请查看cv.ellipse()的文档。下面的示例在图像的中心绘制半个椭圆。
"""


import numpy as np
import cv2 as cv
# Create a black image
# 生成一个512*512的举证 矩阵的每一个元素是一个3*3的0矩阵
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
# 取(447,63) 中心位置
# (100,50)为(长轴,短轴)轴长
# 90这个参数控制图像的角度(90的时候垂直)
# 0-360 显示全部  不然会显示部分
# 0是线段粗细
cv.ellipse(img,(256,256),(100,50),90,0,360,255,0)
#显示
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()