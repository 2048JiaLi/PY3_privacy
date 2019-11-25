## 问：Python中实现二分查找的2种方法？

## 答：在Python实现二分查找法有两种方法，分别用循环和递归方式。

二分查找法：搜索过程从数组的中间元素开始，如果中间元素正好是要查找的元素，则搜索过程结束；如果某一特定元素大于或者小于中间元素，则在数组大于或小于中间元素的那一半中查找，而且跟开始一样从中间元素开始比较。如果在某一步骤数组为空，则代表找不到。这种搜索算法每一次比较都使搜索范围缩小一半。注意如果要想使用二分查找，前提必须是元素有序排列 。

![image](https://mmbiz.qpic.cn/mmbiz_png/IibUVnJ665WoYpaRs0sbroNJkGicS76pS46Hnc0LHV8R6VpJTALoOXGcMdJoEwNm92sJ5BpaLYXm232KEjXF3Oicw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

1. 循环方式
```
def binary_search_2(alist,item):
    """二分查找---循环版本"""
    n = len(alist)
    first = 0
    last = n-1
    while first <= last:
        mid = (first + last)//2
        if alist[mid] ==item:
            return True
        elif item < alist[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False

if __name__ == "__main__":
    a = [1,5,6,10,11,13,18,37,99]
    sorted_list_21 = binary_search_2(a, 18)
    print(sorted_list_21) //True
    sorted_list_22 = binary_search_2(a, 77)
    print(sorted_list_22) //Fals
```

2. 递归方式
```
def binary_search(alist,item):
    """二分查找---递归实现"""
    n = len(alist)
    if n > 0:
        mid = n//2    #数组长度的一半中间下标
        if item == alist[mid] :
            return True   #查找成功
        elif item < alist[mid]:
            return binary_search(alist[:mid],item)
        else:
            return binary_search(alist[mid+1:], item)
    else :
        return False   #失败
        
if __name__ == "__main__":
    a = [1,5,6,10,11,13,18,37,99]
    # print(a)
    sorted_list_11 = binary_search(a,37)
    print(sorted_list_11)//True
    sorted_list_12= binary_search(a, 88)
    print(sorted_list_12)//False
```