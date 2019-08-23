'''
利用装饰器将单个元素输入的RR扩展为多个输入的RR
'''

import random
from typing import List
def k_RR(Random_Response):
    def wrapper(X: List,P: List) -> List:
        res = [Random_Response(x_,p_) for x_,p_ in zip(X,P)]
        print(res)
    return wrapper

@k_RR
def Random_Response(x: int,p: float):
    # x = {0,1}, p=[0,1]
    tmp = x if random.uniform(0,1) <= p else 1-x
    return tmp

if __name__=='__main__':
    P = [0.5,0.6,0.7,0.8]
    T = [0,0,1,0]
    #res = [Random_Response(t_,p_) for t_,p_ in zip(T,P)]
    #print(res)
    '''
    使用装饰器扩展函数功能之后，Random_Response(0,0.1)再用单个元素运行会报错
    此时输入装饰器中的List
    '''
    Random_Response([0,1],[0.5,0.6])
