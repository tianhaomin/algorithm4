#!/usr/bin/python
# -*- coding: UTF-8 -*-
#任务调度问题
import EdgeWeightedDigraph
import DirectedEdge
import AcyclicLP
n = int(raw_input("Please enter the number of jobs: "))
source = 2 * n
sink = 2 * n + 1
G = EdgeWeightedDigraph(2*n+2)
# build network(构建任务调度图)
for i in range(n):
    duration = float(raw_input("Enter the time"))
    e1 = DirectedEdge(source,i,0.0)
    e2 = DirectedEdge(i+n,sink,0.0)  # 连接结束点到终点
    e3 = DirectedEdge(i,i+n,duration)  # 从任务开始到结束隔了n
    G.addEdge(e1)
    G.addEdge(e2)
    G.addEdge(e3)
    # precedence contraints优先级的设定
    m = int(raw_input("")) # 比i点优先级低的几个点
    for j in range(m):  # 对优先级低的进行连接
        precedent = int(raw_input(""))
        e4 = DirectedEdge(n+i,precedent,0.0)
        G.addEdge(e4)
lp = AcyclicLP(G,source)
print "Job start  finish"
print "-----------------"
