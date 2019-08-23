## 绘制GRR算法中概率p与域大小d的关系折线图，Epsilon=2.0

+ ***plt.xticks(range(0,100,5))***      
设置x轴刻度，range(0,100,5)表示0-100内每5格出现一次
+ ***plt.yticks()***     
设置y轴刻度
+ ***plt.xlabel('Domain')***            
设置x轴标签
+ ***plt.ylabel('p')***                 
设置y轴标签
+ ***plt.title('Epsilon=2.0')***        
设置标题
+ ***plt.grid()***                      
添加网格



```
from math import exp
import pandas as pd
import matplotlib.pyplot as plt
Epsilon = 2.0

p = [exp(Epsilon) / (exp(Epsilon) + d - 1) for d in range(1,100)]
ts = pd.Series(p,index=range(1,100))
plt.plot(ts)
plt.xticks(range(0,100,5))
#plt.grid()
plt.xlabel('Domain')
plt.ylabel('p')
plt.title('Epsilon=2.0')
plt.show()
```

## 可视图
![image](https://github.com/2048JiaLi/PY3_privacy/blob/master/%E6%95%B0%E6%8D%AE%E5%8F%AF%E8%A7%86%E5%8C%96/images/Pvalue_GRR.png)
