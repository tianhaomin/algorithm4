#!/usr/bin/python
# -*- coding: UTF-8 -*-
#hash有两种方法实现，一个是拉链法一个是线性探测法
#线性探测法lalala
INIT_CAPACITY = 3000
class LinearProbingHashST(object):
    def __init__(self):
        self.n = 0
        self.m = INIT_CAPACITY
        self.keys = [None]*INIT_CAPACITY
        self.values = [None]*INIT_CAPACITY
    def size(self):
        return self.n
    def isEmpty(self):
        return self.size() == 0
    def contains(self,k):
        return self.get(k) != None
    #获得字符串的hash值
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
    def resize(self,capacity):
        temp = LinearProbingHashST(capacity)
        for i in range(self.m):
            if self.keys[i] != None:
                temp.put(self.keys[i],self.values[i])
        self.keys = temp.keys
        self.values = temp.values
        self.m = temp.m
    #插入函数不是直接进行插入需要检查一簇值是不是符合进行插入
    def put(self,k,v):
        if v == None:
            self.delete(k)
            return
        if self.n > self.m/2:
            self.resize(2*self.m)
        i = self.hash(k)
        while not self.keys[i] == None:
            if self.keys[i] == k:
                self.values[i] = v
                return
            if not self.keys[i] == k:
                i = (i+1)%self.m#要检查一个簇的key
        self.keys[i] = k
        self.values[i] = v
        self.n += 1
    def get(self,k):
        i = self.hash(k)
        while self.keys[i] != None:
            if self.keys[i] == k:
                return self.values[i]
            if not self.keys[i] == k:
                i = (i+1)%self.m
        return None
    def delete(self,k):
        if not self.contains(k):
            return
        i = self.hash(k)
        while not k == self.keys[i]:
            i = (i+1) %self.m
        self.keys[i] = None
        self.values[i] = None
        #删除之后需要重新将被删除元素之后同一个簇中的元素更新他的哈希值
        i = (i +1)%self.m
        while not self.keys[i] == None:
            keytoRehash = self.keys[i]
            valtoRehash = self.values[i]
            self.keys[i] = None
            self.keys[i] = None
            self.n -= 1
            self.put(keytoRehash,valtoRehash)
            i = (i+1)%self.m
            #把后面的元素往前移动
        self.n -= 1
        if self.n>0 and self.n<=self.m/8:
            self.resize(self.m/2)
    def key(self):
        #暂时先用列表代替queue
        c = []
        for i in range(self.m):
            if not self.keys[i] == None:
                c.append(self.keys[i])
        return c
#测试函数
if __name__ == '__main__':
    ht = LinearProbingHashST()
    ht.put('g',4)
    print ht.get('g')
    ht.delete('g')
    print ht.get('g')
    print ht.key()#LIST变量不可以与函数重名
#拉链法就是用array存一个链表






