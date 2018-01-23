#!/usr/bin/python
# -*- coding: UTF-8 -*-
#并归排序---up-bottom
def less(a,i,j):
    return a[i]<a[j]
def issorted(a,lo,hi):
    for i in range(a,lo+1,hi+1):
        if less(a[i],a[i-1]):
            return False
#merge
def merge(a,lo,mid,hi):
    aux = []
    for k in range(lo,hi+1):
        aux.append(a[k])
    i = lo
    j = mid+1
    for k in range(lo,hi+1):
        if i>mid and j<=hi:
            a[k] = aux[j]
            j += 1
        elif j>hi and i<=mid:
            a[k] = aux[i]
            i += 1
        elif j<=hi and i<=mid and less(aux,j,i):
            a[k] = aux[j]
            j += 1
        elif j<=hi and i<=mid and less(aux,i,j):
            a[k] = aux[i]
            i += 1
        else:
            break
def sort(a,lo,hi):
    if hi <= lo:
        return
    mid = lo + (hi - lo)/2
    sort(a,lo,mid)
    sort(a,mid+1,hi)
    merge(a,lo,mid,hi)
a = [9,4,3,6]
sort(a,0,len(a)-1)
print a

