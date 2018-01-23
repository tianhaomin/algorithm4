#!/usr/bin/python
# -*- coding: UTF-8 -*-
#用hashST的简单实现
'''
import hashST
class SparseVector(object):
    def __init__(self):
        self.st1 = hashST.LinearProbingHashST()
    #将向量的第i个坐标换成value
    def put(self,i,value):
        if value == 0.0:
            self.st1.delete(i)
    def size(self):
        return self.st1.size()
    def get(self,i):
        if not self.st1.contains(i):
            return 0.0
        else:
            return self.st1.get(i)
    def dot(self,that):
        sum = 0.0
        for i in self.st1.key():
            sum += that[i]*self.st1.get(i)
        return sum
#测试代码
if __name__ == '__main__':
    a = SparseVector()
    a.put(0,1)
    a.put(1,2)
    print a.st1.key()
'''
#用ST实现功能
import ST
import math
class saprseVector(object):
    def __init__(self,d):
        self.d = d
        self.st1 = ST.ST()
    def put(self,i,value):
        if value == 0.0:
            self.st1.delete1(i)
        else:
            self.st1.put(i,value)
    def get(self,i):
        if self.st1.contains(i):
            return self.st1.get(i)
        else:
            return 0.0
    def nnz(self):
        return self.st1.size()
    def dimensuon(self):
        return self.d
    def dot(self,that):
        sum = 0.0
        if self.st1.size() <= that.st.size():
            for i in self.st1.keys():
                if that.st.contains(i):
                    sum += self.get(i) *that.get(i)
        else:
            for j in self.st1.keys():
                if self.st1.contains(j):
                    sum += self.get(j) * that.get(j)
        return sum
    def magnitude(self):
        return math.sqrt(self.dot(self.st1))
    def plus(self,that):
        c = saprseVector(self.d)
        for i in self.st1.keys():
            c.put(i,self.st1.get(i))
        for i in that.st1.keys():
            c.put(i,that.st1.get(i)+c.get(i))
        return c.st1.keys()#lalaal
#测试代码
if __name__ == '__main__':
    a = saprseVector(10)
    b = saprseVector(10)
    a.put(3, 0.50)
    a.put(9, 0.75)
    a.put(6, 0.11)
    a.put(6, 0.00)
    b.put(3, 0.60)
    b.put(4, 0.90)
    print a.plus(b)
    print b.get(3)
#还有待改进
#稀疏向量就是维度很高是矩阵的存储需要特别巨大的空间但是其中的0项比较多所以用稀疏向量的处理方法可以
#处理多为的稀疏矩阵总体思路就是我们不用a[i][j]来存储一个矩阵中的值我们用的是hashST()用a[i].put()/get()
#来进行矩阵元素的添加这样一来所需的时间不是平方级别只是N加上对应的几个元素的时间而且因为是稀疏向量所以
#元素很少这个处理的方法对于举行==巨型矩阵和特别稀疏的矩阵特别好用，但是对于不那么稀疏的矩阵或是比较小型的矩阵
#就是比较费力气的