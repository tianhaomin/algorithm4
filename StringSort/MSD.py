#!/usr/bin/python
# -*- coding: UTF-8 -*-

R = 256   #  因为根据ascii码每个位置的可能性有256个选择

def charAt(s,d):

    if d == len(s):
        return -1
    return s[d]

#  索引插入排序
def sortString(a,lo,hi,d,aux):

    count = {}
    for i in range(lo,hi+1):
        c = charAt(a[i],d)
        count[c+2] += 1

    for r in range(R+1):
        count[r+1] += count[r]

    for i in range(lo,hi+1):
        c = charAt(a[i],d)
        count[c+1] += 1
        aux[count[c+1]] = a[i]

    for i in range(lo,hi+1):
        a[i] = aux[i-lo]

#  插入排序
def insertionsort1(a,lo,hi,d):

    for i in range(lo,hi+1):
        j = i
        while (j>lo) and (less(a[j],a[j-1],d)):
            temp = a[j]
            a[j] = a[j-1]
            a[j-1] = temp


def less(a,b,d):

    return a[d] < b[d]


