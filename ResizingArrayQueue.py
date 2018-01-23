#!/usr/bin/python
# -*- coding: UTF-8 -*-
#定容的队列因为array不能动态调整但是可以设计函数进行对队列的扩充和缩小lalala
class ResizingArrayQueue(object):
    def __init__(self):
        self.q = [0]*2#存放queue元素
        self.n = 0#queue中的元素个数
        self.first = 0
        self.last = 0
    def isEmpty(self):
        return self.n == 0
    def size(self):
        return self.n
    def resize(self,capacity):
        temp = [0]*capacity
        for i in range(self.n):
            temp[i] = self.q[(self.first + i)%len(self.q)]
        self.q = temp
        self.first = 0
        self.last = self.n
    def enqueue(self,v):
        if self.n == len(self.q):
            self.resize(2*len(self.q))
        self.q[self.last] = v
        self.last += 1
        if self.last == len(self.q):
            self.last = 0
        self.n += 1
    def dequeue(self):#移除最早的元素
        v = self.q[self.first]
        self.q[self.first] = None
        self.n -= 1
        self.first += 1#first是q中的第一个元素的索引
        if self.first == len(self.q):
            self.first = 0
        if self.n>0 and self.n == len(self.q)/4 :
            self.resize(len(self.q)/2)
        return v
    def peek(self):
        return self.q[self.first]
#测试
if __name__ == "__main__":
    q = ResizingArrayQueue()
    q.enqueue(1)
    q.enqueue(2)
    print q.peek()
    print q.size()

