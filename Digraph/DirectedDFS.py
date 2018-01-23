# !/usr/bin/python
# -*- coding: UTF-8 -*-
import Bag1
class DirectedDFS(object): # 用深度优先的算法对指定的点进行搜索
    def __init__(self,g,s):  # 给定已知的图和一个顶点来初始化
        self.G = g
        self.S = s
        self.marked = [False]*self.G.V
        self.dfs(s)
        self.count = 0
    '''
    def __init__(self,g,sources):  # 有多个顶点进行初始化
        self.G = g
        self.S = s
        self.marked = [False]*self.G.V
        for v in sources:
            if not self.marked[v]:
                self.dfs(v)
       '''
    def dfs(self,v):
        self.count += 1
        self.marked[v] = True
        for w in self.G.adj[v]:
            if not self.marked[w]:
                self.dfs(w)
    def count(self):
        return self.count
#测试代码
if __name__ == '__main__':
    file = open()
    sour = file[0]
    g = file[1]
    sources = Bag1.Bag()
    for i in range(1,len(sour)):
        sources.add(int(i))
    dfs = DirectedDFS(g,sources)
    for v in range(dfs.G.V):
        if dfs.marked(v):
            print v + " "
'''
注意：对于有向图进行路径的寻找，我们的方法与无向图的方法几乎一样
      就是对于无向图的DepthFirstPaths和BreadthFirstPaths的参数graph
      换成digraph就行

'''