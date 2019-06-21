text = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq
    ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q
    ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq()
    gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''

'''
text_translate = ''
for i in text:
    #isalpha()检测字符串是否只由字母组成
    if str.isalpha(i):
        #ord() 函数是 chr() 函数（对于 8 位的 ASCII 字符串）的配对函数，它以一个字符串（Unicode 字符）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值。
        n = ord(i)
        if i >= 'y':
            n = ord(i) + 2 - 26
        else:
            n = ord(i) + 2
        #chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符
        text_translate += chr(n)
    else:
        text_translate += i
print(text_translate)
'''


import string
#python2 的写法是string.lowercase
l = string.ascii_lowercase
#print(l)
#l是所有小写字母顺序排列，l[2:] + l[:2]是后移两位的排列顺序
#python2 写法string.maketrans()
t = str.maketrans(l, l[2:] + l[:2])
print (text.translate(t))