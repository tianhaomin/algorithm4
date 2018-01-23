#!/usr/bin/python
# -*- coding: UTF-8 -*-
class ResizingArrayStack(object):
    def __init__(self):
        self.a = [0]*2
        self.n = 0
    def isEmpty(self):
        return self.n == 0
    def size(self):
        return self.n
    def resize(self,capacity):
        temp = [0]*capacity
        for i in range(self.n):
            temp[i] = self.a[i]
        self.a = temp
    def push(self,v):
        if self.n == len(self.a):
            self.resize(2*len(self.a))
        self.a[self.n] = v
        self.n += 1
    def pop(self):
        v = self.a[self.n - 1]
        self.a[self.n - 1] = None
        self.n -= 1
        if self.n>0 and self.n == len(self.a)/4:
            self.resize(len(self.a)/2)
        return v
    def peek(self):
        return self.a[self.n-1]
#测试
if __name__ == "__main__":
    s = ResizingArrayStack()
    s.push(1)
    s.push(2)
    s.push(3)
    print s.peek()
    print s.pop()