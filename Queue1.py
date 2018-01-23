#!/usr/bin/python
# -*- coding: UTF-8 -*-
#链表实现，可动态处理lalala
class node(object):
    def __init__(self):
        self.item = None
        self.next = None
class Queue(object):
    first = node()
    last = node()
    def __init__(self):
        self.first = node()
        self.last = node()
        self.n = 0
    def isEmpty(self):
        return self.n
    def size(self):
        return self.n
    def peek(self):
        return self.first.item
    def enqueue(self,v):#添加
        oldlast = node()
        oldlast = self.last
        self.last = node()
        self.last.item = v
        self.last.next = None
        if self.isEmpty():
            self.first = self.last
        else:
            oldlast.next = self.last
        self.n += 1
    def dequeue(self):#删除
        v = self.first.item#因为first是最第一添加的数
        self.first = self.first.next
        self.n -= 1
        if self.isEmpty :
            self.last = None
        return v
#测试代码
if __name__ == "__main__":
    q = Queue()
    q.enqueue(2)
    q.enqueue(4)
    q.enqueue(6)
    print q.dequeue()
