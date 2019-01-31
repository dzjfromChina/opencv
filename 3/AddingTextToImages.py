"""""""""""""""""""""""""""""""""""""""""""""""
@author: duzj                                   
@contact: dzj0574@163.com                     
@software: PyCharm                    
@file: AddingTextToImages.py                             
@time: 2019/1/31 17:28                        
"""""""""""""""""""""""""""""""""""""""""""""""

"""
1. Text data that you want to write
   要写入的文本数据
2. Position coordinates of where you want put it (i.e. bottom-left corner where data starts).
   位置坐标的地方，你想把它(即左下角的数据开始)。
3. Font type (Check cv.putText() docs for supported fonts)
   字体类型(检查cv.putText()文档是否支持字体)
4. Font Scale (specifies the size of font)
   字体大小(指定字体大小)
5. regular things like color, thickness, lineType etc. For better look, lineType = cv.LINE_AA is recommended.
   规则的东西，如颜色，厚度，线条类型等。为了更好看，线条类型= cv。建议行AA。
"""

import numpy as np
import cv2 as cv
# Create a black image
# 生成一个512*512的举证 矩阵的每一个元素是一个3*3的0矩阵
img = np.zeros((512,512,3), np.uint8)

#字体类型
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(1,250), font, 4,(255,255,255),2,cv.LINE_AA)
# 判断起点  按照逻辑 似乎是从左下角开始绘制
cv.line(img,(1,250),(512,250),(255,255,0),1)

#显示
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()