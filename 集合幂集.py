def PowerSetsBinary(items):
    res = []
    N = len(items)
    for i in range(2 ** N):#子集的个数
        combo = []
        for j in range(N):#用来判断二进制数的下标为j的位置的数是否为1
            if (i >> j) % 2:
                combo.append(items[j])
        #print(combo)
        res.append(combo)
    return res
#使用itertools模块
if __name__ == '__main__':
    X = ['a','b','d','e']
    tmp = PowerSetsBinary(X)
    #print(tmp)
    from collections import defaultdict
    res = defaultdict(float)
    Y = [4,2,2,4]
    for _x,_y in zip(X,Y):
        res[_x] = _y
    
    _f = defaultdict(float)
    for _tmp in tmp:
        if len(_tmp) > 1:
            _res = 1
            for _t in _tmp:
                _res = (0.9 * res[_t] / 4) * _res
            _f[''.join(_tmp)] = _res
    #print(_f)
    
    _a = _f.keys()
    _b = _f.values()
    #print(_a,_b)
    for a_,b_ in zip(_a,_b):
        print(a_,'  : ',b_)
