#!/usr/bin/python
# -*- coding: UTF-8 -*-
#  符号图就是实际应用中的图都是根据字符串描述顶点和边
#  而且需要我们可以双向的对图进行索引即我们应该知道顶
#  点就能找到相应的信息，给定相应的信息就能找到对应的
#  顶点即我们需要的就是沟造一个符号图
import ST
import graph
class SymbolGraph(object):
    def __init__(self,filename):
        self.st = ST.ST()  # 由符号名找到索引
        self.keys = []  # 由索引找到符号名
        self.file = open(filename)
        for i in self.file.readlines():
            # 第一遍扫描通过读入字符串来构造索引
            a = i.split(' ')
            for j in range(len(a)):
                if not self.st.contains(a[j]):
                    self.st.put(a[j], self.st.size())
        print "Done Reading " + filename

        self.keys = [0]*self.st.size()
        for stringName in self.st.keys():#把所有的keys放到
            self.keys[self.st.get(stringName)] = stringName

        self.G = graph.Graph(self.st.size())#第二次扫描
        self.file1 = open(filename)
        for i in self.file1.readlines():
            a = i.split(' ')
            v = self.st.get(a[0])
            for i in range(len(a)):
                w = self.st.get(a[i])
                self.G.addEdge(v,w)
    def contains(self,s):
        return self.st.contains(s)
    def index(self,s):
        return self.st.get(s)
    def indexOf(self,s):
        return self.st.get(s)
    def name(self,v):
        return self.keys[v]
    def nameOf(self,v):
        return self.keys[v]
    