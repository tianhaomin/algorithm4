#!/usr/bin/python
# -*- coding: UTF-8 -*-
#搜索树的基本结构是平衡搜索树，红黑搜索树，二分搜索树的基本结构
class ST(object):
    def __init__(self):
        self.st = {}
    def get(self,k):
        return self.st[k]
    def put(self,k,v):
        if v == None:
            self.st.pop(k)
        else:
            self.st[k] = v
    def delete1(self,k):
        del self.st[k]
        return self.st
    def contains(self,k):
        return k in self.st
    def size(self):
        return len(self.st)
    def isEmpty(self):
        return self.size() == 0
    def min(self):#找出最小的键值
        a = self.st.keys()
        a.sort()
        return a[0]
    def max(self):
        a = self.st.keys()
        a.sort()
        return a[-1]
    def ceiling(self,k):
        k1 = self.st.keys()
        k2 = []
        for i in k1:
            if i>=k:
                k2.append(i)
        return min(k2)
    def floor(self,k):
        k1 = self.st.keys()
        k2 = []
        for i in k1:
            if i <= k:
                k2.append(i)
        return max(k2)
    def keys(self):
        return self.st.keys()

if __name__ == '__main__':
    a = ST()
    a.put('a', 1)
    a.put('b', 2)
    a.put('c', 3)
    a.put('d', 4)
    a.put('e', 5)
    a.put('f', 6)
    a.put('g', 7)
    a.put('h', 8)
    a.put('i', 9)
    a.put('j', 10)
    a.put('k', 11)
    print a.floor('z')
