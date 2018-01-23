# !/usr/bin/python
# -*- coding: UTF-8 -*-
import DepthFirstOrder
class KosarajuSharirSCC(object):
    def __init__(self,g):
        self.G = g
        self.dfs = DepthFirstOrder(self.G.reverse())  # 用图的逆序数进行排列
        #得到图的强连通的结果
        self.marked = [False]*self.G.V
        self.id = [0]*self.G.V  # 给定点标号确定是不是在同一个强连通域内
        self.count = 0
        for v in self.dfs.reversePost():
            if not self.marked[v]:
                self.dfs(v)
                self.count += 1
    def dfs(self,v):
        self.marked[v] = True
        self.id[v] = self.count
        for w in self.G.adj[v]:
            if not self.marked[w]:
                self.dfs(w)
    def count(self):  # 图中强连通分量的数量
        return self.count
    def stronglyConnected(self,v,w):  # 判断图中是不是强连通分量
        return self.id[v] == self.id[w]
# 总结：有向图的可达性有别与无向图的，无向图的可达性就是连通性就是CC
# 可是有向图不同，有向图的强连通性与可达是两个概念所以需要新的方法解
# 这个问题