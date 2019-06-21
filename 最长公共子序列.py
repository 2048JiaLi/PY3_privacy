'''算法设计与分析
序列X={A,B,C,B,D,A,B}和Y={B,D,C,A,B,A}
最长公共子序列长度为4，{B,C,B,A}
'''
import numpy as np

def LCSLength(m:int ,n:int ,X:str ,Y:str):
    #m,n = len(X),len(Y)
    c,b = np.zeros((m+1,n+1)),np.zeros((m,n))
    for i in range(1,m+1):
        for j in range(1,n+1):
            if X[i-1] == Y[j-1]:
                c[i,j] = c[i-1,j-1] + 1
                b[i-1,j-1] = 1
                #print(c)
            else:
                if c[i-1,j] >= c[i,j-1]:
                    c[i,j] = c[i-1,j]
                    b[i-1,j-1] = 2
                    #print(c)
                else:
                    c[i,j] = c[i,j-1]
                    b[i-1,j-1] = 3
                    #print(c)
    return c,b
    #c[m,n]为最长公共子序列的长度

def LCS(i: int ,j: int, x: str,b,res):
    if i < 0 or j < 0: 
        return
    if b[i,j] == 1 :
        LCS(i-1,j-1,x,b,res)
        res.append(x[i])
        #print(x[i])
    elif b[i,j] == 2:
        LCS(i-1,j,x,b,res)
    elif b[i,j] == 3:
        LCS(i,j-1,x,b,res)

if __name__=='__main__':
    x,y = 'cdafebac','abcdefea'
    m,n = len(x),len(y)
    c,b = LCSLength(m,n,x,y)
    #print(b)
    res = []
    LCS(m-1,n-1,x,b,res)
    print('最大公共子序列长度为:',c[m,n])
    print('最大公共子序列为:',res)
    #print(b)