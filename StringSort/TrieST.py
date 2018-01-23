#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Queue1
R = 256
class Node(object):

    def __init__(self):
        self.val = None
        self.next1 = [None] * R

class TrieST(object):

    def __init__(self):
        self.root = Node()
        self.n = 0

    def get1(self,key):
        x = self.get2(self,self.root,0)
        if x == None:
            return x.value

    def get2(self,x,key,d):
        if x == None:
            return None
        if d == len(key):
            return x
        c = key[d]
        return self.get2(x.next1[c],key,d+1)

    def contains(self,key):
        return self.get(key) != None

    def put1(self,key,val):
        if val == None:
            self.delete(key)
        else:
            self.root = self.put2(self.root,key,val,0)

    def put2(self,x,key,val,d):
        if x == None:
            x = Node()
        if d == len(key):
            if x.val == None:
                self.n += 1
                x.val = val
                return x
        c = key[d]
        x.next1[c] = self.put2(x.next1[c],key,val,d+1)
        return x

    def size(self):
        return self.n

    def isEmpty(self):
        return self.size == 0

    def keyaWithPrefix(self,prefix):
        results = Queue1
        x = self.get(self.root,prefix,0)
        self.collect(x,prefix,results)
        return results

    def collect(self,x,prefix,results):
        if x == None:
            return
        if x.val != None:
            results.enqueue(prefix)
        for c in R:
            prefix.append(c)
            self.collect(x.next1[c],prefix,results)
            prefix.deleteCharAt(prefix.length()-1)


