#!/usr/bin/python
# -*- coding: UTF-8 -*-
#lalala
import random
import math
class Wq(object):
    id = []
    sz = []
    count = 0 
    def __init__(self,N):
        self.count = N
        for i in range(N):
            self.id.append(i)
        for j in range(N):
            self.sz.append(1)
    def countfun(self):
        return self.count
    def findfun(self,p):
        while p != self.id[p]:
            p = self.id[p]
        return p
    def connected(self,i,j):
        if self.findfun(i) == self.findfun(j):
            return True
        else :
            return False
    def union(self, p, q):
        i = self.findfun(p)
        j = self.findfun(q)
        if(i == j):
            return
        if self.sz[i] <self.sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]
        self.count -=1


matrix = []
#global N
N = int(raw_input("Please enter the number: "))
row = N
col = N
wq = Wq((N * N + 2))
wqT = Wq(N * N + 1)
alfull = False
for i in range(N * N + 1):
    matrix.append(0)
def openFunc(i, j):
    x = (i - 1) * col + j
    matrix[x] = 1
    if i == 1:
        wq.union(x, 0)
        wqT.union(x, 0)
    if i == row:
        wq.union(x, (row * col + 1))
    l1 = [1, -1, 0, 0]
    l2 = [0, 0, 1, -1]
    for dir in range(4):
        posx = i + l1[dir]
        posy = j + l2[dir]
        if (posx <= row) and (posx >= 1) and (posy <= col) and (posy >= 1) and (isOpen(posx, posy)):
            wq.union(x, (posx - 1) * row + posy)
            wqT.union(x, (posx - 1) * row + posy)
def isOpen(i, j):
    if matrix[(i - 1) * row + j]:
        return True
    else:
        return False

def isFull():
    global alfull#若想修改全局变量必须先声明
    if alfull:
        return True
    if wq.findfun(0) == wq.findfun((row * col + 1)):
        alfull = True
        return True
    return False
#测试代码
openFunc(1,1)
openFunc(2,1)
openFunc(2,2)
print isFull()

openFunc(1,1)
openFunc(1,2)
openFunc(2,2)
print isFull()
