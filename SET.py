#!/usr/bin/python
# -*- coding: UTF-8 -*-
#集合结构的实现lalala
class SET(object):
    def __init__(self):
        self.set = set()
    def add(self,k):
        self.set.add(k)
    def contains(self,k):
        return k in self.set
    def delete(self,k):
        self.set.remove(k)
    def size(self):
        return len(self.set)
    def isEmpty(self):
        return self.size() == 0
    def max1(self):
        return max(self.set)
    def min1(self):
        return min(self.set)
    def ceiling(self,k):
        temp = []
        for i in self.set:
            if i>=k:
                temp.append(i)
        return min(temp)
    def floor(self,k):
        temp = []
        for i in self.set:
            if i<=k:
                temp.append(i)
        return max(temp)
    #集合最大应用场景就是可以进行集合间的交并补运算
    def union(self,that):#并
        return self.set | that
    def intersets(self,that):#交
        return self.set&that
    #判断两个集合是否相等
    def equals(self,other):
        return self.set == other
#测试代码
if __name__ == '__main__':
    set = SET()
    set.add("www.cs.princeton.edu")
    set.add("www.cs.princeton.edu")
    set.add("www.princeton.edu")
    set.add("www.math.princeton.edu")
    set.add("www.yale.edu")
    set.add("www.amazon.com")
    set.add("www.simpsons.com")
    set.add("www.stanford.edu")
    set.add("www.google.com")
    set.add("www.ibm.com")
    set.add("www.apple.com")
    set.add("www.slashdot.com")
    set.add("www.whitehouse.gov")
    set.add("www.espn.com")
    set.add("www.snopes.com")
    set.add("www.movies.com")
    set.add("www.cnn.com")
    set.add("www.iitb.ac.in")
    print set.ceiling('www.simpsonr.com')



