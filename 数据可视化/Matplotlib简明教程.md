## [Matplotlib](https://github.com/2048JiaLi/PY3_privacy/blob/master/%E6%95%B0%E6%8D%AE%E5%8F%AF%E8%A7%86%E5%8C%96/matplotlib.ipynb)简介
信息可视化是数据分析中一个重要的部分。它也可能是探索数据的一部分，比如，帮助我们找到离群点或需要进行变换的数据，或帮助我们思考选择哪种模型更合适。Python有很多库能用来制作统计或动态可视化，但这里我们重点关注matplotlib pandas searborn等库。Matplotlib是一个非常强大的画图工具，对数据的可视化起着很大的作用。Maplotlib可以画图线图，散点图，等高线图，条形图，柱形图，3D图形，图形动画等。
```
import matplotlib.pyplot as plt  
import numpy as np
import pandas as pd 
```
+ ### 1 基础用法
```
x=np.linspace(-1,1,50)  #定义x
y1=2*x+1  #定义y数据范围
y2=x**2

plt.figure()  #定义图像窗口
plt.plot(x,y1)  #画出曲线
plt.plot(x,y2)
plt.show() #显示图像
```
+ ### 2 figure图像
```
x=np.linspace(-3,3,50) #在（-3,3）之间生成50个样本数
y1=2*x+1
y2=x**2

plt.figure(num=1,figsize=(8,5))                          #定义编号为1，大小为（8,5）
plt.plot(x,y1,color='red',linewidth=2,linestyle='--')    #颜色线宽及格式
plt.plot(x,y2)
plt.show()
```
+ ### 3 设置坐标轴
```
plt.figure(num=1,figsize=(8,5)) #定义编号为1，大小为（8,5）
plt.plot(x,y1,color='red',linewidth=2,linestyle='--')  
plt.plot(x,y2)
plt.xlim(-1,2) #x轴的范围
plt.ylim(-2,3) #y轴的范围
plt.xlabel("x轴")
plt.ylabel("y轴")
plt.show()
```
   
```
new_ticks=np.linspace(-1,2,5)  #-1到2分成5段，包含端点
print(new_ticks)
plt.xticks(new_ticks)  #进行替换新下标
plt.yticks([-2,-1,0,1,2,],
          [r'$really\ bad$','$bad$','$0$','$well$','$really\ well$'])
```
+ ### [作子图](https://github.com/2048JiaLi/PY3_privacy/blob/master/%E6%95%B0%E6%8D%AE%E5%8F%AF%E8%A7%86%E5%8C%96/%E7%94%BB%E5%AD%90%E5%9B%BE.py)
```
ax1 = plt.subplot(311) #建立一个3×1的图，并选择第1个图
ax2 = plt.subplot(312) #建立一个3×1的图，并选择第2个图
ax3 = plt.subplot(313) #建立一个3×1的图，并选择第3个图

# 在三个图中分布画图---
ax1.plot(·)
--图1的设置：坐标轴，线条等等--
图2、图3类似

#最后只需要一个显示即可
plt.show()
```
+ ### 设置边框--不显示/显示
```
ax=plt.gca()  #get current axis
ax.spines['right'].set_color('none') #边框属性设置为None 不显示
ax.spines['top'].set_color('none')
```
+ ### 调整移动坐标轴
```
x=np.linspace(-3,3,50) #在（-3,3）之间生成50个样本数
y1=2*x+1
y2=x**2
plt.figure(num=2,figsize=(8,5)) #定义编号为2，大小为（8,5）
plt.plot(x,y1,color='red',linewidth=2,linestyle='--')  
plt.plot(x,y2)
plt.xlim(-1,2) #x轴的范围
plt.ylim(-2,3) #y轴的范围
plt.xlabel("x轴")
plt.ylabel("y轴")

new_ticks=np.linspace(-1,2,5)  #-1到2分成5段，包含端点
print(new_ticks)
plt.xticks(new_ticks)  #进行替换新下标
plt.yticks([-2,-1,0,1,2,],
          [r'$really\ bad$','$bad$','$0$','$well$','$really\ well$'])


ax=plt.gca()  #get current axis
ax.spines['right'].set_color('none') #边框属性设置为None 不显示
ax.spines['top'].set_color('none')


ax.xaxis.set_ticks_position('bottom')  #设置x坐标刻度数字或名称的位置，所有属性为：top,bottom,both,default,none
ax.spines['bottom'].set_position(('data',0)) # 设置.spines边框x轴，设置.set_position设置边框的位置，y=0位置；位置所有属性有outward,axes,data
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0)) #坐标中心点在（0,0）位置


plt.show()
```
