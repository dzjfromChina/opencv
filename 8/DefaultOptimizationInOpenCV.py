"""""""""""""""""""""""""""""""""""""""""""""""
@author: duzj                                   
@contact: dzj0574@163.com                     
@software: PyCharm                    
@file: DefaultOptimizationInOpenCV.py                             
@time: 2019/2/9 13:53                        
"""""""""""""""""""""""""""""""""""""""""""""""

"""

Many of the OpenCV functions are optimized using SSE2, AVX etc. It contains unoptimized code also. So if our system support these features, we should exploit them (almost all modern day processors support them). It is enabled by default while compiling. So OpenCV runs the optimized code if it is enabled, else it runs the unoptimized code. You can use cv2.useOptimized() to check if it is enabled/disabled and cv2.setUseOptimized() to enable/disable it. Let's see a simple example. 


许多OpenCV函数是使用SSE2、AVX等进行优化的。
它还包含未优化的代码。因此，如果我们的系统支持这些功能，
我们应该利用它们(几乎所有现代处理器都支持它们)。编译时默认启用。
所以OpenCV在启用时运行优化的代码，否则运行未优化的代码。
您可以使用cv2.useOptimized ( )来检查它是否被启用/禁用，使用cv2.setUseOptimized ( )来启用/禁用它。让我们看一个简单的例子。
"""

import cv2

img = cv2.imread("2.jpg")


print(
 cv2.useOptimized()
)


e1 = cv2.getTickCount()
res = cv2.medianBlur(img,49)
e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()
print(time)

# 关闭之后
cv2.setUseOptimized(False)

print(
 cv2.useOptimized()
)


e1 = cv2.getTickCount()
res2 = cv2.medianBlur(img,49)
e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()
print(time)

