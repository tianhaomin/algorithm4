#!/usr/bin/python
# -*- coding: UTF-8 -*-
#lalala实现了想要的优先队列基于堆
class MinPQ(object):
    def __init__(self):
        self.pq = [0]*10
        self.N = 0
    def resize(self,x):
        n = len(self.pq)
        for i in range(n,x+1):
            self.pq.append(0)
    def isEmpty(self):
        return self.N == 0
    def insert(self,x):
        if self.N >= len(self.pq)-1:
            self.resize(len(self.pq)*2)
        self.N += 1
        self.pq[self.N] = x
        self.swim(self.N)
    def exch(self,i,j):
        temp = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = temp
    def swim(self,k):
        while k>1 and self.pq[k/2]>self.pq[k]:
            self.exch(k,k/2)
            k = k/2
    def sink(self,k):
        while 2*k<= self.N:
            j = 2*k
            if j<self.N and self.pq[j]>self.pq[j+1]:
                j += 1
            if not self.pq[k]>self.pq[j]:
                break
            self.exch(k,j)
            k = j
    def delMin(self):
        min = self.pq[1]
        self.exch(1,self.N)
        self.N -= 1
        self.sink(1)
        self.pq[self.N+1] = None
        return min
    def sort(self):#lalala解决了堆排序
        n = self.N
        for i in range(self.N/2,0,-1):
            self.sink(i)
        while self.N>1:
            self.exch(1,self.N)
            self.N -= 1
            self.sink(1)
        self.N = n
    def show(self):#把插入的元素展示出来
        print self.pq[1:self.N+1]
#测试代码
s = raw_input("please enter the words")
l = list(s)
p = MinPQ()
for i in l:
    if not i == '-':
        p.insert(i)
    #else:
        #print p.delMax()
p.sort()
print p.show()
print p.N

