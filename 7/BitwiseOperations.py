"""""""""""""""""""""""""""""""""""""""""""""""
@author: duzj                                   
@contact: dzj0574@163.com                     
@software: PyCharm                    
@file: BitwiseOperations.py                             
@time: 2019/2/3 9:32                        
"""""""""""""""""""""""""""""""""""""""""""""""

"""
This includes bitwise AND, OR, NOT and XOR operations. They will be highly useful while extracting any part of the image (as we will see in coming chapters), defining and working with non-rectangular ROI etc. Below we will see an example on how to change a particular region of an image. I want to put OpenCV logo above an image. If I add two images, it will change color. If I blend it, I get an transparent effect. But I want it to be opaque. If it was a rectangular region, I could use ROI as we did in last chapter. But OpenCV logo is a not a rectangular shape. So you can do it with bitwise oper
这包括位和、或、非和XOR操作。
它们在提取图像的任何部分(我们将在接下来的章节中看到)、定义和处理非矩形ROI时非常有用。
我想把OpenCV的logo放在图片上面。
如果我添加两个图像，它会改变颜色。如果我混合它，我得到一个透明的效果。
但我希望它是不透明的。如果它是一个矩形区域，我可以像上一章那样使用ROI。
但是OpenCV的logo不是一个矩形。所以你可以用bitwise oper来做

参考: https://blog.csdn.net/weixin_35732969/article/details/83748054
"""
import cv2

# Load two images
img1 = cv2.imread('1.jpg')# 底图
img2 = cv2.imread('3.jpg')# 水印图

# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
print("img2.shape:",img2.shape)

# 取底图的顶部位置  大小和水印图一样
roi = img1[0:rows, 0:cols ]

# 把图片变为灰度图片
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
cv2.imshow('img2gray',img2gray)

# https://blog.csdn.net/u012566751/article/details/77046445  threshold的用法
# 使用二值化函数cv2.threshold()将灰度图二值化：
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
# 使用“非”操作函数cv2.bitwise_not()将上图颠倒黑白：
mask_inv = cv2.bitwise_not(mask)

# 使用“与”操作函数cv2.bitwise_and()对图像遮挡：
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
cv2.imshow('img1_bg',img1_bg)
cv2.imshow('roi',roi)
cv2.imshow('mask_inv',mask_inv)
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
cv2.imshow('img2_fg',img2_fg)
cv2.imshow('img2',img2)
cv2.imshow('mask',mask)

dst = cv2.add(img1_bg,img2_fg)


img1[0:rows, 0:cols ] = dst

cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()