#!/usr/bin/python
# -*- coding: UTF-8 -*-
#bag的实现就是不能删除而且元素的顺序不重要,由链表实现
#lalala
class node(object):
    def __init__(self):
        self.item = None
        self.next = None
class Bag(object):
    def __init__(self):
        self.first = None#first如果是node()那么bag就永远不会为空
        self.n = 0
    def isEmpty(self):
        return self.first == None
    def  size(self):
        return self.n
    def add(self,item):
        oldfirst = self.first
        self.first = node()
        self.first.item = item
        self.first.next = oldfirst
        self.n += 1
#测试代码
if __name__ == '__main__':
    b = Bag()
    b.add(3)
    print b.size()

