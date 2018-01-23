#!/usr/bin/python
# -*- coding: UTF-8 -*-
#用python实现链表的数据结构可以从头或尾添加或删除数据lalala
class Node(object):
    def __init__(self):
        self.next1 = None
        self.previous = None
        self.value = 0
class Deque(object):
    first = Node()
    last = Node()
    def __init__(self):
        self.first = None
        self.last = None
        self.N = 0
    def isEmpty(self):
        return self.N == 0
    def size(self):
        return self.N
    def addFirst(self,a):
        oldfirst = Node()
        oldfirst = self.first
        self.first = Node()
        self.first.value = a
        self.first.previous = None
        if self.isEmpty():
            self.last = self.first
            self.first.next1 = None
        else:
            self.first.next1 = oldfirst
            oldfirst.previous = self.first
        self.N += 1
    def addLast(self,b):
        oldlast = Node()
        oldlast = self.last
        self.last = Node()
        self.last.value = b
        self.last.nest = None
        if self.isEmpty():
            self.first = self.last
            self.last.previous = None
        else:
            self.last.previous = oldlast
            oldlast.next1 = self.last
        self.N += 1
    def removeLast(self):
        x = self.last.value
        self.last = self.last.previous
        self.N -= 1
        if self.isEmpty():
            self.last = self.first = None
        else:
            self.last.next1 = None
        return x
    def removeFirst(self):
        x = self.first.value
        self.first = self.first.next1
        self.N -= 1
        if self.isEmpty():
            self.first = self.last = None
        else:
            self.first.previous = None
#testing cooding
q = Deque()
s = raw_input("please enter the string : ")
for i in s:
    if i != '-':
        q.addFirst(i)
    elif i == '-':
        print q.removeLast()
print q.size()

