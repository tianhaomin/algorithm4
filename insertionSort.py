#!/usr/bin/python
# -*- coding: UTF-8 -*-
#lalala
def isLess(i,j):
    if i<j:
        return True
    else:
        return False
def exch(a,i,j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp
def insertionSort(a):
    n = len(a)
    for i in range(n):
        for j in range(i,0,-1):#倒序引用
            if isLess(a[j],a[j-1]):
                exch(a,j,j-1)
            else:
                continue

    return a
