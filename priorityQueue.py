#!/usr/bin/python
# -*- coding: UTF-8 -*-
#优先队列可以找出优先级最高的不必完全排列lalala
class PQ(object):
    #pq = [0]
    #N  = 0
    def __init__(self,pq,N):#lalala
        self.pq = pq#python定容的方法
        self.N = N
    def isEmpty(self):#lalala
        return self.N == 0
    def insert(self,x):#lalala
        self.pq.append(x)
        self.N += 1
    def exch(self,i,j):#lalaal
        temp = self.pq[j]
        self.pq[i] = self.pq[j]
        self.pq[j] = temp
    def delMax(self):#lalaal
        max = 0
        for i in range(1,self.N):
            if self.pq[max]<self.pq[i]:
                max = i
        self.exch(max, self.N - 1)
        self.pq.pop()
        self.N -= 1
        return self.pq[self.N-1]#删除最大的元素
#测试代码
N = int(raw_input("please enter the length: "))
s = raw_input("please enter the words")
l1 = list(s)
l = l1[:N]
p = PQ(l,N)
print p.pq
p.delMax()
print p.pq


