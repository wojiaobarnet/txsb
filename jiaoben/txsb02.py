#!/usr/bin/env python
#  coding         : utf-8
# @Time          :2018-07-20 9:17 
# @Author      ：Nanly
# @File：       ：txsb02.py
# @Software : PyCharm
#matplotlib读取图像
import numpy as np
from matplotlib import pyplot as plt
import cv2

img = cv2.imread('\\Users\\nanly\\Pictures\\NOB.jpg', 0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
plt.show()
