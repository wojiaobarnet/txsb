#!/usr/bin/env python
#  coding         : utf-8
# @Time          :2018-07-20 9:33 
# @Author      ：Nanly
# @File：       ：txsb03.py
# @Software : PyCharm

import numpy as np
import cv2

img = np.zeros((512,512,3), np.uint8)
#np.zeros((高，宽，通道)，类型)
#创建一个宽512高512的黑色画布，RGB(0,0,0)即黑色
cv2.line(img, (0,0), (511,511), (0,0,255), 5)
#画直线 cv2.line(‘图片对象’，起始坐标(x轴,y轴)，结束坐标，颜色，宽度)
cv2.rectangle(img,(30,166), (130,266),(0,255,0),3)
#画矩形cv2.rectangle(‘图片对象’, 左上角坐标，右下角坐标，颜色，宽度)
cv2.circle(img,(222,222),60,(255,111,111),-1)
#画圆形，cv2.circle('图片对象'，中心点坐标，半径，颜色，宽度)

cv2.ellipse(img, (333, 333), (50,20), 0, 0, 150, (255,222,222), -1)
#画椭圆形，cv2.ellipse(图片对象，中心点坐标，长短轴，顺时针旋转度数，开始角度（右长轴表0度，上短轴表270度），颜色，宽度)

pts=np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
# 画多边形，指定各个点坐标,array必须是int32类型

pts = pts.reshape((-1,1,2,))
# -1表示该纬度靠后面的纬度自动计算出来，实际上是4

# print(pts)

# 画多条线，False表不闭合，True表示闭合，闭合即多边形
cv2.polylines(img,[pts],True,(255,255,0),5)

#写字,字体选择
font=cv2.FONT_HERSHEY_TRIPLEX

# 图片对象，要写的内容，左边距，字的底部到画布上端的距离，字体，大小，颜色，粗细
cv2.putText(img,"TEST",(10,400),font ,3.5,(255,255,255),2)

"""
由于OpenCV原生函数putText是不支持中文字体，所以这里无法写入中文。
关于文字字体名称标识符，参见 Hershey 字体集 ，可供字体类型如下：
FONT_HERSHEY_SIMPLEX 正常大小无衬线字体
FONT_HERSHEY_PLAIN 小号无衬线字体
FONT_HERSHEY_DUPLEX 正常大小无衬线字体，比FONT_HERSHEY_SIMPLEX更复杂
FONT_HERSHEY_COMPLEX 正常大小有衬线字体
FONT_HERSHEY_TRIPLEX 正常大小有衬线字体，比FONT_HERSHEY_COMPLEX更复杂
FONT_HERSHEY_COMPLEX_SMALL 同FONT_HERSHEY_COMPLEX
FONT_HERSHEY_SCRIPT_SIMPLEX 手写风格字体
FONT_HERSHEY_SCRIPT_COMPLEX 比FONT_HERSHEY_SCRIPT_SIMPLEX 更复杂
https://www.jianshu.com/p/e99ede5103ed

"""
winname = 'example'
cv2.namedWindow(winname)
cv2.imshow(winname, img)
cv2.waitKey(0)
cv2.destroyAllWindow(winname)