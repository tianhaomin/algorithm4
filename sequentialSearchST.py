#!/usr/bin/python
# -*- coding: UTF-8 -*-
#基于无序情况下的查找二分查找的STlalala
class Node(object):
    def __init__(self,key,val):
        self.next1 = None
        self.key = key
        self.value = val
class SequentialSearchST(object):
    def __init__(self):
        self.first = Node(0,0)
    #索引
    def get(self,k):
        x = self.first
        while x != None:
            if k == x.key:
                return x.value
            x = x.next1
        return None
    #插入
    def put(self,k,v):
        x = self.first
        while x != None:
            if k == x.key:
                x.value = v
                return
            x = x.next1
        oldfirst = self.first
        self.first = Node(k,v)
        self.first.next1 = oldfirst
    #返回所有的键值
    def keys(self):
        x = self.first
        y = []
        while not x == None:
            y.append(x.key)
            x = x.next1
        return y
    def contains(self,k):
        return self.get(k) != None

#测试代码
if __name__ == '__main__':
    sq = SequentialSearchST()
    sq.put(2,3)
    sq.put(3,4)
    print sq.get(3)