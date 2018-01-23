#!/usr/bin/python
# -*- coding: UTF-8 -*-
#就是对最小生成树进行准备，对加权边的代码实现
#对一条边的描述lalala
class Edge(object):
    def __init__(self,v,w,weight):#初始化
        self.v = v
        self.w = w
        self.weight = weight
    def weight(self):
        return self.weight
    def either(self):#返回给定点的另一个端点
        return self.v
    def other(self,vertex):#返回给定点不同的端点
        if vertex == self.v:
            return self.w
        if vertex == self.w:
            return self.v
    def compareTo(self,that):#比较两条边的权值
        if self.weight<that.weight:
            return -1
        elif self.weight>that.weight:
            return +1
        else:
            return 0
    def toString(self):#就是给出字符串的形式表示出边的权值
        print self.v,'-',self.w,':',self.weight
#测试代码
if __name__ == '__main__':
    e = Edge(12,14,2.67)
    w = Edge(13,15,2.44)
    e.toString()
    print e.compareTo(w)
    #print e.either()
    #print e.other(12)

