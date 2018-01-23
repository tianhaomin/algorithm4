#!/usr/bin/python
# -*- coding: UTF-8 -*-
#lalala
#添加功能：可以返回索引位置
'''a = []
N = int(raw_input("Please enter the length of array"))
for i in range(N):
   x = int(raw_input("Please enter the number: "))
   a.append(x)
def binarysearch( key, a):
    lo = 0
    hi = len(a) - 1
    mid = 0
    a.sort()#只有排完序才能进行二分搜索
    while lo <= hi:
        mid = lo + (hi - lo)/2
        if key < a[mid]:
            hi = mid - 1
        elif key > a[mid]:
            lo = mid + 1
        else:
            return mid
    return a[0]

key = int(raw_input("Please enter the number you want to find: "))
d = binarysearch(key,a)
if a[d] == key:
    print "Yes,the index is ",d
else:
    print "No"

'''
#递归的方法进行二分搜索

def cur_binarysearch(a,lo,hi,key):
   a.sort()
   mid = lo + (hi - lo)/2
   
   if key < a[mid]:
      cur_binarysearch(a,lo,mid-1,key)
   elif key > a[mid]:
      cur_binarysearch(a,mid+1,hi,key)
   elif key == a[mid]:
      print 'True'
   if lo >= hi:
      return 'False'
      
      





      

