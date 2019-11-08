## 绘制GRR算法中概率p与域大小d的关系折线图，Epsilon=2.0

+ ***plt.xticks(range(0,100,5))***      
设置x轴刻度，range(0,100,5)表示0-100内每5格出现一次
+ ***plt.yticks([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])***     
设置y轴刻度
+ ***plt.xlabel('Domain')***            
设置x轴标签
+ ***plt.ylabel('p')***                 
设置y轴标签
+ ***plt.title('Epsilon=2.0')***        
设置标题
+ ***plt.grid()***                      
添加网格
+ ***plt.legend(loc='lower right') #loc显示位置***


`plt.plot(ts1,color='r',linestyle=':',marker='o',label='Error(default)')`
+ **color参数**
```
'b'        blue 蓝
'g'        green 绿
'r'        red 红
'c'        cyan 蓝绿
'm'        magenta 洋红
'y'        yellow 黄
'k'        black 黑
'w'        white 白
```
+ **marker**
```
'.'        point marker
','        pixel marker
'o'        circle marker
'v'        triangle_down marker
'^'        triangle_up marker
'<'        triangle_left marker
'>'        triangle_right marker
'1'        tri_down marker
'2'        tri_up marker
'3'        tri_left marker
'4'        tri_right marker
's'        square marker
'p'        pentagon marker
'*'        star marker
'h'        hexagon1 marker
'H'        hexagon2 marker
'+'        plus marker
'x'        x marker
'D'        diamond marker
'd'        thin_diamond marker
'|'        vline marker
'_'        hline marker
```
+ **linestyle**
```
'-'        solid line style 实线
'--'       dashed line style 虚线
'-.'       dash-dot line style 点画线
':'        dotted line style 点线
```

___
```
from math import exp
import pandas as pd
import matplotlib.pyplot as plt
Epsilon = 2.0

p = [exp(Epsilon) / (exp(Epsilon) + d - 1) for d in range(1,100)]
ts = pd.Series(p,index=range(1,100))
plt.plot(ts)
#或者不将p转化为Series结构，直接可视化

plt.xticks(range(0,100,5))
plt.yticks([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
plt.grid()
plt.xlabel('Domain')
plt.ylabel('p')
plt.title('Epsilon=2.0')
plt.show()
```

### 结果
![image](https://github.com/2048JiaLi/PY3_privacy/blob/master/%E6%95%B0%E6%8D%AE%E5%8F%AF%E8%A7%86%E5%8C%96/images/Pvalue_GRR.png)
