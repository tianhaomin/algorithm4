# !/usr/bin/python
# -*- coding: UTF-8 -*-
import Digraph
import Stack1
class DirectedCycle(object): # 这个就是为了确定是不会DAG
    def __init__(self,g):
        self.G = g
        self.marked = [False]*self.G.V  # 存放节点是不是被标记
        self.onStack = [False]*self.G.V  # 判断给定的顶点是不是在栈中
        self.edgeTo = [0]*self.G.V  # 记录某一顶点最近的一个顶点
        self.cycle = Stack1.Stack()  # 记录图中是不是存在有向环
        for v in range(self.G.V):
            if not self.marked[v] and self.cycle == None:
                self.dfs(v)  # 遍历了图中的所有点进行DFS
    def dfs(self,v):  # 寻找有向环
        self.onStack[v] = True
        self.marked[v] = True
        for w in self.G.adj(v):
            if not self.cycle == None:  # 如果有环就不做啥了没环才继续
                return
            elif not self.marked[w]:
                self.edgeTo[w] = v
                self.dfs(w)  # 体现了深度优先，找一个点往下延伸
                # 广度优先是先看望所有点再往下走
            if self.onStack[w]:
                # w在栈中说明了w可以到达v而v又回到了W
                # 找到了一个环因为在路径v->w时w也在栈中
                self.cycle = Stack1.Stack()
                x = v
                while not x == w:
                    self.cycle.push(x)  # 环中有值
                    x = self.edgeTo[x]  # 寻找环的路径
                self.cycle.push(w)  # 返回环中的所有顶点
                self.cycle.push(v)
        self.onStack[v] = False  # 找到一个环后重新进行下一次的探索
    def hasCycle(self):
        return self.cycle != None
#对于有向图判断是不是有向无环图是重要的应用，因为我们需要
#对于一些应用比如已知优先级的调度问题如果存在环的话就会发生错误
#所以这个程序是用来判断有向图中是不是存在环结构