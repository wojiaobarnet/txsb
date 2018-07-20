#!/usr/bin/env python
#  coding         : utf-8
# @Time          :2018-07-20 10:53 
# @Author      ：Nanly
# @File：       ：txsb04.py
# @Software : PyCharm


import cv2
import numpy as np
#鼠标点击事件

drawing = False
mode = True
ix,iy = -1, -1


def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x, y
    elif event ==cv2.EVENT_MOUSEMOVE and flags ==cv2.EVENT_FLAG_LBUTTON:
        if drawing == True:
            if mode ==True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv2.circle(img, (x,y), 100, (255,0,0),- 1)
    elif event==cv2.EVENT_LBUTTONUP:
        drawing==Flase

img = np.zeros((512,512,3), np.uint8)


cv2.namedWindow('mouse')
cv2.setMouseCallback('mouse', draw_circle)

while(1):
    cv2.imshow('mouse', img)
    k = cv2.waitKey(1)&0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break