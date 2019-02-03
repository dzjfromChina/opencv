"""""""""""""""""""""""""""""""""""""""""""""""
@author: duzj                                   
@contact: dzj0574@163.com                     
@software: PyCharm                    
@file: MakingBordersForImagesPadding.py                             
@time: 2019/2/1 17:23                        
"""""""""""""""""""""""""""""""""""""""""""""""

"""
If you want to create a border around the image, something like a photo frame, you can use cv2.copyMakeBorder() function. But it has more applications for convolution operation, zero padding etc. This function takes following arguments

如果您想在图像周围创建边框，比如相框，可以使用cv2.copyMakeBorder()函数。
但是它在卷积运算，零填充等方面有更多的应用。这个函数有以下参数

src - 输入的图像
top, bottom, left, right - 边框宽度以相应方向上的像素数为单位
borderType - 标志，定义要添加的边框类型。它可以是以下类型:
    cv2.BORDER_CONSTANT - 添加一个固定的彩色边框。这个值应该作为下一个参数给出。
        cv2.BORDER_REFLECT - 边框将是边框元素的镜像反射，如下所示:fedcba|abcdefgh|hgfedcb
        cv2.BORDER_REFLECT_101 or cv2.BORDER_DEFAULT - 和上面一样，但是有一点细微的变化，像这样:gfedcb|abcdefgh|gfedcba
        cv2.BORDER_REPLICATE - 最后一个元素被复制，如下所示:aaaaaa|abcdefgh|hhhhhhh
        cv2.BORDER_WRAP - 无法解释，它会是这样的:cdefgh|abcdefgh|abcdefg
value - 如果边框类型为cv2，则为边框颜色。边境常数
"""

import cv2
from matplotlib import pyplot as plt

BLUE = [255, 0, 0]
img1 = cv2.imread('1.jpg')

replicate = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=BLUE)

# 原图
# 23的意思就是 2行3列 6张图  1是第一张图  Z字型的顺序  imshow显示图片  title取标题
# https://blog.csdn.net/sunshihua12829/article/details/52786144  关于subplot的用法
plt.subplot(231), plt.imshow(img1, 'gray'), plt.title('ORIGINAL')

# 处理后
plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')

plt.show()
