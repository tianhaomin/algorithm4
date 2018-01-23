#!/usr/bin/python
# -*- coding: UTF-8 -*-
#广度优先算法
#不论是广度优先还是深度优先都是在已经给定的图上进行相关性质的挖掘
#而原始的图的类中定义的是对于初始化一个图一般是通过自己设置点或者直接
#从文件中读入已经规定好的图
#深度优先算法是判断是不是有路径在两点之间但是不能找到最短的路径
#广度优先的算法就是为了可以寻找最短的路径
#原理：在寻找从起点到v的路径是先在一部可达的点中寻找是不是有v如果没有就是在
#两步中找直到找到为止
import graph
import sys
import Queue1
import Stack1
class BreadthFirstPaths(object):
#下面是给定一个起点
    def __init__(self,g,s):
        self.G = g
        self.source = s
        self.marked = [False]*self.G.V()#标记是不是联通
        self.distTo = [0]*self.G.V()#记录给定点到起点的距离
        self.edgeTo = [0]*self.G.V()#与dfs一样也是记录最后一次经过的路径
        self.bfs(g,s)#直接用广度优先的算法计算出距离1步2步...都是哪些点
    #也就是找出起点到所有点的最短路径
        assert self.check()
#下面这段代码是在给定多个起点而准备的
    '''def __init__(self,g,s):
        self.marked = [False]*g.V()
        self.distTo = [0]*g.V()
        self.edgeTo = [0]*g.V()
        for i in range(g.V()):
            self.disTo[i] = sys.maxint
        self.bfs(g,s)'''
    def bfs(self):#用广度优先的算法对各个顶点进行遍历
        q = Queue1.Queue()
        for v in range(self.G.V()):
            self.distTo[v] = sys.maxint
        self.distTo[self.source] = 0
        self.marked[self.source] = True
        q.enqueue(self.source)
        while not q.isEmpty():
            l = q.dequeue()
            for w in self.G.adj(l):
                if not self.marked[w]:
                    self.edgeTo[w] = l
                    self.distTo[w] = self.distTo[l] + 1
                    self.marked[w] = True
                    q.enqueue(w)
    def hasPathTo(self,v):
        return self.marked[v]#判断是不是可以与起点联通
    def distTo(self,v):
        return self.distTo[v]#返回起点到给定点的距离
    def pathTo(self,v):#返回起点到指定点的最短距离
        if not self.hasPathTo(v):
            return None
        path = Stack1.Stack()
        x = v
        while self.distTo[x] != 0:
            path.push(x)
            x = self.edgeTo[x]
        path.push(x)
        return path
    def check(self):
        #先检查s的距离=0
        if self.distTo[self.source] != 0:
            print "distance of source" + self.source + "to itself = " + self.distTo[self.source]
            return False
        #check that for each edge v-w dist[w] <= dist[v] + 1
