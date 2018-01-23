#!/usr/bin/python
# -*- coding: UTF-8 -*-
class DirectedEdge (object):
    def __init__(self,v,w,weight):
        self.v = v
        self.w = w
        self.weight = weight
    def from1(self):
        return self.v
    def to1(self):
        return self.w
    def weight(self):
        return self.weight
    def toString(self):
        print self.v , "->" , self.w , " " , self.weight
#测试代码
e = DirectedEdge(1,2,0.54)
e.toString()
