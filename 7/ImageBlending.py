"""""""""""""""""""""""""""""""""""""""""""""""
@author: duzj                                   
@contact: dzj0574@163.com                     
@software: PyCharm                    
@file: ImageBlending.py                             
@time: 2019/2/3 9:20                        
"""""""""""""""""""""""""""""""""""""""""""""""

"""
This is also image addition, but different weights are given to images so that it gives a feeling of blending or transparency. Images are added as per the equation below

这也是图像添加，但不同的权重赋予图像，使其给人一种混合或透明的感觉。图像按下式添加

                g(x)=(1−α)f0(x)+αf1(x)
                
By varying α from 0 1, you can perform a cool transition between one image to another.

通过改变α从0 1中,您可以执行一个很酷的一个图像之间的过渡到另一个地方。


Here I took two images to blend them together. First image is given a weight of 0.7 and second image is given 0.3. cv2.addWeighted() applies following equation on the image.

这里我拍了两张照片把它们混合在一起。第一幅图像的权值为0.7，第二幅图像的权值为0.3。cv2.addWeighted()对图像应用以下方程。

                dst=α⋅img1+β⋅img2+γ
                
Here γ is taken as zero. 

γ是视为零。
"""
import  cv2

img1 = cv2.imread('1.png')
img2 = cv2.imread('2.png')
# size 要一样   也就是像素比要一样   不然会报错
dst = cv2.addWeighted(img1,0.7,img2,0.3,0)

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()