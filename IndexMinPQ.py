#!/usr/bin/python
# -*- coding: UTF-8 -*-
#在最小优先队列的基础上添加上索引
class IndexMinPQ(object):
    def _init__(self,x):#给定已知长度初始化
        self.maxN = x
        self.n = 0
        self.pq = []  # 存放值
        self.qp = []  #存放索引
        self.keys = [0]*(self.maxN+1) #存放值所对应的的关键值
        self.pq = [0]*(self.maxN+1)
        for i in range(x+1):
            self.qp.append(-1)
    def isEmpty(self):
        return self.n == 0
    def contains(self,i):
        return self.qp[i] != -1
    def size(self):
        return self.n
    def insert(self,i,key):
        self.n += 1
        self.qp[i] = self.n#记录索引的位置在pq的什么位置
        self.pq[self.n] = i
        self.keys[i] = key
        self.swim(self.n)
    def minIndex(self):
        return self.pq[1]
    def minKey(self):
        return self.keys[self.pq[1]]
    #将最小删除并返回
    def delMin(self):
        min = self.pq[1]
        self.exch(1,self.n)
        self.n -= 1
        self.sink(1)
        assert min == self.pq[self.n+1]
        self.qp[min] = -1 #将索引去掉
        self.keys[min] = None #将关键词去掉
        self.pq[self.n+1] = -1 #将值去掉
        return min
    #值对应的关键字
    def keyOf(self,i):
        return self.keys[i] # 键值与之是相互对应的关联的
    def changeKey(self,i,key):
        self.keys[i] = key
        self.swim(self.qp[i])
        self.sink(self.qp[i])
    def decreaseKey(self,i,key):
        self.keys[i] = key
        self.swim(self.qp[i])
    def increaseKey(self,i,key):
        self.keys[i] = key
        self.sink(self.qp[i])
    def greater(self,i,j):
        return self.keys[self.pq[i]] > self.keys[self.pq[j]]
    def exch(self,i,j):
        swap = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = swap
        self.qp[self.pq[i]] = i
        self.qp[self.pq[j]] = j
    def swim(self,k):
        while k>1 and self.greater(k/2,k):
            self.exch(k,k/2)
            k = k/2
    def sink(self,k):
        while 2*k <= self.n:
            j = 2*k
            if j<self.n and self.greater(j,j+1):
                self.j += 1
            if not self.greater(k,j):
                break
            self.exch(k,j)
            k = j
