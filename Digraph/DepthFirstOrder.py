# !/usr/bin/python
# -*- coding: UTF-8 -*-
import Queue1
import Stack1
# 主要是给出各种顺序的排列以后需要可以随时调用，下面的拓扑排序就调用了reversePOSTOrder
class DepthFirstOrder(object):
    def __init__(self,g):
        self.G = g
        self.marked = [False]*self.G.V
        self.post = [0]*self.G.V
        self.pre = [0]*self.G.V  # 记录顶点在preorder这个排序中排名第几
        self.postorder = Queue1.Queue()  # postorder是顶点遍历完成的顺序
        self.preorder = Queue1.Queue()  # preorder是顶点调用的顺序
        self.preCounter = 0  # preCounter是用来统计pre数组中的个数的
        self.postCounter = 0
        for v in range(self.G.V):  # 就是按照顶点标号进行遍历
            if not self.marked[v]:
                self.dfs(v)
    '''
        #还可以定义边权重图
        初始化基本一样
    '''
    def dfs(self,v):  # 实际上就是在深度优先搜索的时候进行一个顺序的添加
        # 需要按不同的要求与方式将顶点添加到相应的队列
        self.marked[v] = True
        self.pre[v] = self.preCounter  # 因为图的标号是从0开始的，数组的索引也是从0开始
        self.preCounter += 1
        self.preorder.enqueue(v)  # 每调用一个点就先将他放到序列中去
        for w in self.G.adj(v):
            if not self.marked[w]:
                self.dfs(w)
        self.postorder.enqueue(v)  # postOrder就是在对一个点完成全部的查询在将他添加
        self.post[v] = self.postCounter
        self.postCounter += 1
    def pre(self,v):
        return self.pre[v]
    def post(self,v): # 返回的是一个顶点咱postorder的序数
        return self.post[v]
    def post(self): # 按postorder的顺序返回顶点
        return self.postorder
    def pre(self): # 按preorder得顺序返回顶点
        return self.preorder
    def reversePost(self):  # 就是POSTorder的反向
        reverse = Stack1.Stack()
        for v in self.postorder:
            reverse.push(v)  # 栈是先入后出所以就将postorder倒过来了
        return reverse
#test coding
if __name__ == '__main__':
    pass