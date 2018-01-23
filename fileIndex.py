#!/usr/bin/python
# -*- coding: UTF-8 -*-lalal
'''def spl(filename):
    a = open(filename)
    b = a.readlines()
    c = []
    for i in b:
        w = i.strip('\n')
        c.append(w.split(' '))
    return c
f1 = open('E:/ddd/demo1.txt')
f2 = open('E:/ddd/demo2.txt')
f3 = open('E:/ddd/demo3.txt')
f4 = open('E:/ddd/demo4.txt')
f5 = open('E:/ddd/demo5.txt')
st = {}
st[f1.name] = spl('E:/ddd/demo1.txt')
st[f2.name] = spl('E:/ddd/demo2.txt')
st[f3.name] = spl('E:/ddd/demo3.txt')
st[f4.name] = spl('E:/ddd/demo4.txt')
st[f5.name] = spl('E:/ddd/demo5.txt')
In = raw_input("Please enter what do you find: ")
if In in st:
    print st[In]
else:
    tt = []
    for i in st.keys():
        if In in st[i]:
            tt.append(i)
    print tt
'''
#用ST数据结构实现
from ST import ST
from SET import SET
st = ST()
def splitstr(filename):
    str1 = open(filename).readlines()
    words = SET()
    for i in str1:
        a = i.strip('/n')
        c = a.split(' ')
        for j in c:
            words.add(j)
    return words
f1 = splitstr('E:/ddd/demo1.txt')
f2 = splitstr('E:/ddd/demo2.txt')
f3 = splitstr('E:/ddd/demo3.txt')
f4 = splitstr('E:/ddd/demo4.txt')
f5 = splitstr('E:/ddd/demo5.txt')
st.put('E:/ddd/demo1.txt',f1)
st.put('E:/ddd/demo2.txt',f2)
st.put('E:/ddd/demo3.txt',f3)
st.put('E:/ddd/demo4.txt',f4)
st.put('E:/ddd/demo5.txt',f5)
#测试代码
if __name__ == '__main__':
    print st.get('E:/ddd/demo5.txt')
    print splitstr('E:/ddd/demo1.txt')