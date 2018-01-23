# !/usr/bin/python
#  -*- coding: UTF-8 -*-
# 联通分量，时深度优先算法的应用就是可以利用深度优先算法找到所有联通的量
# 我们需要可以判断出两个图中的元素是不是了联通并指导有多少联通的分量并且
# 在一起相连的的元素要有统一的标识符
import graph
import Queue1
class CC(object):
    def __init__(self,g):
        self.G = g
        self.marked = [False] * self.G.V
        self.id = [0] * self.G.V  # 每个顶点都有一个ID就是代表他是哪一个联通分量中
        self.size = [0] * self.G.V  # 每个联通分量中点的个数
        self.count = 0  # 连通分量的个数（每个联通分量中都有包含了很多其他的顶点）
        for v in range(self.G.V):
            if not self.marked[v]:
                self.dfs(v)
                self.count += 1
    def dfs(self,v):
        self.marked[v] = True
        self.id[v] = self.count
        self.size[self.count] += 1  # 统计此连通分量中有多少个顶点
        for w in self.G.adj[v]:
            if not self.marked[w]:
                self.dfs(w)
    def id(self,v):
        return self.id[v]
    def size(self,v):
        return self.size[self.id[v]]
    def count(self):
        return self.count
    def connected(self,v,w):
        return self.id(v) == self.id(w)
# 测试代码
if __name__ == "__main__":
    g = graph.Graph(20)
    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(0,3)
    g.addEdge(1,6)
    g.addEdge(2,6)
    g.addEdge(3,4)
    g.addEdge(3,5)
    g.addEdge(5,6)
    g.addEdge(7,8)
    g.addEdge(7,9)
    g.addEdge(8,12)
    g.addEdge(9,12)
    g.addEdge(9,10)
    g.addEdge(12,11)
    g.addEdge(10,11)
    g.addEdge(13,14)
    g.addEdge(13,17)
    g.addEdge(13,18)
    g.addEdge(14,15)
    g.addEdge(14,16)
    g.addEdge(15,19)
    g.addEdge(16,19)
#    g.addEdge(16,20)
    g.addEdge(15,18)
#    g.addEdge(18,20)
    cc = CC(g)
    m = cc.count()
    print m + "components"
    components = Queue1.Queue()
    for i in range(m):
        components[i] = Queue1.Queue()
    for v in range(g.V()):
        components[cc.id(v)].enqueue(v)
    for i in range(m):
        for v in components[i]:
            print v + ' '