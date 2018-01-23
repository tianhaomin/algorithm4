#!/usr/bin/python
# -*- coding: UTF-8 -*-
#链表实现，可动态处理lalala
class node(object):
    def __init__(self):
        self.item = None
        self.next = None
class Stack(object):
    first = node()
    def __init__(self):#初始化
        self.first = None
        self.n = 0#计数
    def isEmpty(self):
        return self.first == None
    def size(self):
        return self.n
    def push(self,v):#添加
        oldFirst = node()
        oldFirst = self.first
        self.first = node()
        self.first.item = v
        self.first.next = oldFirst
        self.n += 1
    def pop(self):#退出第一个数(remove)
        temp = self.first.item
        self.first = self.first.next
        self.n -= 1
        return temp
    def peek(self):#只是返回最早添加的数但不删除
        return self.first.item
#测试代码
if __name__ == "__main__":
    s = Stack()
    s.push(3)
    s.push(4)
    s.push(1)
    print s.pop()

