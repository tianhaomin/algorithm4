#!/usr/bin/python
# -*- coding: UTF-8 -*-
import insertionSort

CUTTON = 5

def exch(a,i,j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def charAt(s,d):

    if d == len(s):
        return -1
    else:
        return s[d]

def sort(s,lo,hi,d):
    if hi<lo + CUTTON:
        insertionSort(s,lo,hi,d)
        return
    lt = lo
    gt = hi
    v = charAt(s[lo],d)
    i = lo + 1
    while (i <= gt):
        t = charAt(s[i],d)
        if t<v:
            exch(s,lt,i)
            lt += 1
            i += 1
        elif t>v:
            exch(s,i,gt)
            gt -= 1
        else:
            i += 1
    sort(s,lo,lt-1,d)
    if (v>=0):
        sort(s,lt,gt,d+1)
    sort(s,gt+1,hi,d)