"""""""""""""""""""""""""""""""""""""""""""""""
@author: duzj                                   
@contact: dzj0574@163.com                     
@software: PyCharm                    
@file: ReadAndWrite.py                             
@time: 2019/1/31 15:07                        
"""""""""""""""""""""""""""""""""""""""""""""""
#总结
#读取并写入

import cv2

img = cv2.imread('1.jpg',1)
cv2.imshow('image',img)
k = cv2.waitKey(0) & 0xFF
if k == 27:
    # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):
    # 按 s 键 保存并离开
    cv2.imwrite('1.png',img)
    cv2.destroyAllWindows()