#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 图的一种处理算法就是用graph进行图的初始化然后用
# 各种search算法对图的各种性质进行挖掘，主要是用来判断是不是存在
# 一条路径在两点之间
# 深度优先算法就是遍历所有顶点走过的顶点就做一个标记递归的访问没有
# 标记过的顶点
import graph  # lalala
class DepthFirstSearch(object):  # 找到所有与顶点相连的点，追访问与
    # 起点联通的点，深度优先算法的每条边都会访问两次
    # 而第二次就是总是发现已经访问过
    # 可以实现两个功能：1、判断两点间是不是有存在路径
    # 2、找出给定点到起点的路径
    def __init__(self,g,s):
        g = graph.Graph()
        self.G = g
        self.marked = [False]*self.G.V()
        self.count = 0
    # 深度优先搜索
    def dfs(self,v):  # 从v点进行深度优先的遍历
        self.count += 1
        self.marked[v] = True  # 先对点进行标记
        for i in self.G.adj[v]:
            if not self.marked[i]:  # 遍历所有没有标记的点进行迭代的深度优先搜索
                self.dfs(i)
    def marked1(self,v):
        return self.marked[v]  # 判断v是不是与起点相连
    def count(self):
        return self.count
# 测试算法
if __name__ == "__main__":
    pass


