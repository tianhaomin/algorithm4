#!/usr/bin/python
# -*- coding: UTF-8 -*-
#用两种方法实现一种正常一种递归
#lalala
def exch(a,i,j):
    temp = a[j]
    a[j] = a[i]
    a[i] = temp
def subnum(j):
    j -= 1
    return j
def addnum(i):
    i += 1
    return i
def partition(a,lo,hi):
    v = a[lo]
    i = lo
    j = hi+1
    while True:
        i += 1
        while a[i] < v:
            if i==hi:
                break
        j -= 1
        while v < a[j]:
            if j==lo:
                break
        if i>=j:
            break
        exch(a,i,j)
    exch(a,lo,j)
    return j
def sort1(a,lo,hi):
    if hi<=lo:
        return 
    j = partition(a,lo,hi)
    sort1(a,lo,j-1)
    sort1(a,j+1,hi)

def sort(a):
    sort1(a,0,len(a)-1)
    return a
 
