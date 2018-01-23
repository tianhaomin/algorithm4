#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sequentialSearchST

INIT_CAPACITY = 4
class SeparateChainingHsahST(object):
    def __init__(self,m):
        self.m = m
        self.n = 0
        self.st = [None]*INIT_CAPACITY
        for i in range(self.m):
            self.st[i] = sequentialSearchST.SequentialSearchST()
   #将hashtable重新定容知识每一个索引对应的是一个sequentialSearchST
    def resize(self,chains):
        temp = SeparateChainingHsahST(chains)
        for i in range(self.m):
            y = self.st[i].keys()
            for i in y:
                temp.put(i,self.st[i].get(i))
        self.m = temp.m
        self.n = temp.n
        self.st = temp.st
    #python中将给定的字符转化成hashs数值
    def convert_n_bytes(self,n, b):
        bits = b * 8
        return (n + 2 ** (bits - 1)) % 2 ** bits - 2 ** (bits - 1)
    def convert_4_bytes(self,n):
        return self.convert_n_bytes(n, 4)
    def getHashCode(self,s):
        h = 0
        n = len(s)
        for i, c in enumerate(s):
            h = h + ord(c) * 31 ** (n - 1 - i)
        return self.convert_4_bytes(h)
    #将hash值转化为一个索引值
    def hash(self,k):
        return (self.getHashCode(k) & 0x7fffffff)%self.m
    def size(self):
        return self.n
    def isEmpty(self):
        return self.size() == 0
    def contains(self,k):
        return self.get(k) != None
    def get(self,k):#直接检索值
        i = self.hash(k)
        return self.st[i].get(k)
    #插入的思路是先进性哈希映射然后检查是不是存在这个值
    #查到以后再进行put
    def put(self,k,v):
        if v == None:
            self.delete(k)
            return
        if self.n>=10*self.m:
            self.resize(2*self.m)
        i = self.hash(k)
        if not self.st[i].contains(k):
            self.n += 1
        self.st[i].put(k,v)
    def delete(self,k):
         i = self.hash(k)
         if self.st[i].contains(k):
             self.n -= 1
         self.st[i].delete(k)
         if self.m>INIT_CAPACITY and self.n<= 2*self.m:
             self.resize(self.m/2)
    #将hashtable中的所有键值都提取出来
    def keys(self):
        y = []
        for i in range(self.m):
            x = self.st[i].first
            while not x == None:
                y.append(x.key)
                x = x.next1
        return y
#测试代码

a = SeparateChainingHsahST(4)
a.put('f',1)
print a.get('f')

