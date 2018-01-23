#!/usr/bin/python
# -*- coding: UTF-8 -*-
#是用来找图中给定两点的最短路径
#总的思路就是使用Dijkstra算法并在从优先队列取到t之后停止
import DijkstraSP
INF = float("inf")
class DijkstraAllPairsSP(object):
    def __init__(self,G):
        self.all = [0]*G.V()
        for v in range(G.V()):
            self.all[v] = DijkstraSP(G,v)  # all序列中存储的是每一个到
            # 图中所有点的最短路径
    def path(self,s,t):
        return self.all[s].pathTo(t)  # all[s]就是s到图中所有点的最短路径
    # 从中选出到t的那一条路径即可
    def hasPath(self,s,t):
        return self.dist(s,t) < INF
    def dist(self,s,t):
        return self.all[s].distTo(t)