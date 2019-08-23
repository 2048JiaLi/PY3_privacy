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