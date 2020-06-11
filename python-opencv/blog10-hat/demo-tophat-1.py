import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 读取图片
source = cv.imread("demo_noise_white.jpg", cv.IMREAD_GRAYSCALE)

# 设置卷积核
kernel = np.ones((5, 5), np.uint8)

# 顶帽运算
dst = cv.morphologyEx(source, cv.MORPH_TOPHAT, kernel)

# 显示结果
titles = ['Source Img', 'Tophat Img']
images = [source, dst]

# matplotlib 绘图
for i in range(2):
   plt.subplot(1, 2, i+1), plt.imshow(images[i],'gray')
   plt.title(titles[i])
   plt.xticks([]),plt.yticks([])

plt.show()