# !/usr/bin/python
# -*- coding: UTF-8 -*-
import Stack1
class DepthFirstDirectedPaths(object):
    def __init__(self,g,s):
        self.G = g
        self.S = s
        self.marked = [False]*self.G.V
        self.edgeTo = [0]*self.G.V
        self.dfs(s)
    def dfs(self,v):
        self.marked[v] = True
        for w in self.G.adj(v):
            if not self.marked[w]:
                self.edgeTo[w] = v
                self.dfs(w)
    def hasPathTo(self,v):
        return self.marked[v]
    def pathTo(self,v):  # 寻找从顶点到达v的路径
        if not self.hasPathTo(v):
            return None
        path = Stack1.Stack()
        x = v
        while not x == self.S:
            path.push(x)
            x = self.edgeTo[x]
        path.push(self.S)
        return path
# 起初构建图的时候就已经把原点可以到达的地方都做标记了所以有标记的地方
# 都是可以到达的，并且用edgeTo记录了到达这一点的最后一条边是什么而且可
# 以利用这个进行图路径的还原可以进行路径的查询。在寻找路径的时候首先确
# 定是不是可以到达，如果可以在进行接下来的工作，将路径用一个栈存储。一层
# 层的往上进行探索找到路径