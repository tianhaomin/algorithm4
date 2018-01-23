#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Graph
import Stack1
#深度优先搜索给让我们可以判断是不是存在相连的路径下面的算法是基于深度优先搜索进行路径的查找
#深度优先算法是一种基础笨拙的方法主要是找到点与点之间的连通性
#对DepthFirstSearch的扩展
class DepthFirstPaths(object):
    def __init__(self,g,s):
        #self.g = Graph.graph(10)
        self.edgeto = [0]*g.V()
        self.marked = [False]*g.V()
        self.s = s#起始点
    def dfs(self,v):
        self.marked[v] = True
        for i in self.g.adj(v):
            if not self.marked[i]:
                self.edgeto[i] = v
                self.dfs(i)
    def hasPathTo(self,v):#查看是否有到点v的路径
        return self.marked[v]
    def pathTo(self,v):
        if not self.hasPathTo(v):
            return None
        path = Stack1#就是按照最后进去最先出来的顺序排列
        x = v
        while x != self.s:
            path.push(x)
            x = self.edgeto[x]
        path.push(self.s)#s-..-..-..-v找到了这条路径
        #但是这种原始的深度优先的算法找到的也不是最短路径知识一天路径而已
        return path
