#!/usr/bin/python
# -*- coding: UTF-8 -*-
#node中的所有键值都可以是其他的类
class Node(object):
    def __init__(self,k,v,s):
        self.value = v
        self.left = None
        self.right = None
        self.size = s
        self.key = k
class BST(object):
    root = Node(0,0,0)
    def __init__(self):
        self.root = Node(0,0,0)
    def isEmpty(self):
        return self.size() == 0
    def size(self):
        return self.size2(self.root)
    def size2(self,x):
        if x == None:
            return 0
        else:
            return x.size
    def contains(self,k):
        return self.get(k) != None
#从root开始出发找与key对应的节点返回对应的value
    def get(self,k):#lalala
        return self.get1(self.root,k)
    def get1(self,x,k):#若想实现类的重写必须加上一些元类编程#lalala
        if x == None:
            return None
        elif k<x.key :
            return self.get1(x.left,k)
        elif k>x.key:
            return self.get1(x.right,k)
        else:
            return x.value
#实现树中节点值得替换
    def put(self,k,v):#lalala
        if v == None:
            self.delete(k)
            return
        self.root = self.put1(self.root,k,v)
    def put1(self,x,k,v):#lalala
        if x == None:
            return Node(k,v,1)
        if k<x.key:
            x.left = self.put1(x.left,k,v)
        elif k>x.key:
            x.right = self.put1(x.right,k,v)
        else:
            x.value = v
        x.size = 1+self.size2(x.left) + self.size2(x.right)
        return x
    def deleteMin(self):
        self.root = self.deleteMin1(self.root)
    def deleteMin1(self,x):
        if x.left == None:
            return x.right#如果node x没有做节点那么就将它用右子树代替
        x.left = self.deleteMin(x.left)
        x.size = self.size(x.left) + self.size(x.right) + 1
        return x
    def deleteMax(self):
        self.root = self.deleteMax1(self.root)
    def deleteMax1(self,x):
        if x.right == None:
            return x.left
        x.right = self.deleteMax(x.right)
        x.size = self.size(x.left) + self.size(x.right) + 1
        return x
    def delete(self,k):
        self.root = self.delete1(self.root,k)
#删除指定的节点
    def delete1(self,x,k):
        if x == None:
            return None
        if k<x.key:
            x.left = self.delete(x.left,k)
        elif k>x.key:
            x.right = self.delete(x.right,k)#找到与指定key相等的节点
        else:
            if x.right == None:#如果找的节点没有右子树就直接用左子树代替
                return x.left
            if x.left == None:#如果没有左子树就用右子树代替
                return x.right
            t = x#如果两个子树都有则按下列操作进行，x是我们要删除的点
            x = self.min(t.right)#用原来右节点的最小值代替x
            x.right = self.deleteMin(t.right)#右边把提上来的节点删了即可
            x.left = t.left#左边保持不变
        x.size = self.size(x.left) + self.size(x.right) + 1
        return x
    def min(self):#找出整个树的最小值
        return self.min1(self.root).key
    def min1(self,x):#找出某节点下的最小值
        if x.left == None:
            return x
        else:
            return self.min(x.left)
    def max(self):#整个的最小值
        return self.max(self.root).key
    def max(self,x):#某节点的最小值
        if x.right == None:
            return x
        else:
            return self.max(x.right)
#返回比键值小的最大的值
    def floor(self,k):#找出比给定key小的最大值#lalala
        x = self.floor1(self.root,k)
        if x == None:
            return None
        else:
            return x.key
    def floor1(self,x,k):#lalala
        if x == None:
            return None
        if k == x.key:
            return x
        elif k < x.key:
            return self.floor(x.left,k)
        t = self.floor1(x.right,k)
        if t != None:
            return t
        else :
            return x
#找出比给定key大的最小的key值
    def ceiling(self,k):#主程序直接调用从根找的函数#lalala
        x = self.ceiling1(self.root,k)#从根开始找，调用下一个重写的哈是哪壶
        if x == None:
            return None
        else:
            return x.key
    def ceiling1(self,x,k):#从某一个节点处开始找#lalala
        if x == None:
            return None
        if k == x.key:
            return x
        if k<x.key:
            t = self.ceiling(x.left,k)
            if not t == None:
                return t
            else:
                return x
        return self.ceiling1(x.right,k)
#找到第k小的键值，找到排名为k的键值
    def select(self,k):
        x = self.select1(self.root,k)#调用重写的算法从根开始找
        return x.key##
    def select1(self,x,k):#又是方法的重写找到第k小的节点
        if x == None:
            return None
        t = self.size(x.left)
        if t>k:#如果此节点处左子树的值多于k个那么说明第k小的键值就在此节点的左子树
            return self.select(x.left,k)
        elif t<k:#如果左子树的节点数目不到k个说明第k小的在右子树
            return self.select(x.right,k-t-1)
        else:#如果左子树正好有k个节点那么此节点就是第k小值
            return x
#找出小于给定键值的数目
    def rank(self,k):#检测给定的键值是不是在对的位置上
        return self.rank1(k,self.root)#调用重写函数
    def rank1(self,k,x):#
        if x == None:
            return 0
        if k<x.key:#如果给定的键值小于当前节点的键值则说明应该往左边走
            return self.rank(k,x.left)
        elif k>x.key:#如果给定键值大于当前节点的键值则往右走
            #返回此节点加上此节点的左子树再加上对此节点右子树的判断
            return 1+self.size(x.left) + self.rank(k,x.right)
        else:
            return self.size(x.left)
#返回给定区间的所有键值(需要引入新的数据结构)#新的数据结构待定义（queue）
    def keys(self,x,queue,lo,hi):#queue是自己实现的队列结构
        #queue = Queue()
        if x == None:
            return
        if lo<x.key:
            self.keys(x.left,queue,lo,hi)
        if lo<=x.key and hi>x.key:
            queue.enqueue(x.key)
        if hi>x.key:
            self.keys(x.right,queue,lo,hi)
#返回给定区间内键值的个数(如果端点值在树中则算作计数)
    def size1(self,lo,hi):
        if lo>hi:
            return 0
        if self.contains(hi):
            return self.rank(hi) - self.rank(lo) + 1
        else:
            return self.rank(hi) - self.rank(lo)
#BST的高度
    def height(self):
        return self.height1(self.root)
#计算从节点x处树的高度
    def height1(self,x):
        if x == None:
            return -1
        return 1 + max(self.height(x.left),self.height(x.right))
#判断二分查找树是不是满足对称的顺序（不懂）
    def isBST(self):
        return self.isBst1(self.root,None,None)
    def isBST1(self,x,min,max):
        if x == None:
            return True
        if not min == None and x.key<=min:
            return False
        if not max == None and x.key>=max:
            return False
        return self.isBST(x.left,min,x.key) and self.isBST(x.right,x.key,max)
#主函数
'''
if __name__ == '__main__':
    st = BST()
    for i in range(3):
        key = raw_input("Please enter the key:")
        st.put(key,i)
    print (st.ceiling('2'))
    #print (st.get('3'))

    #print st.root.right.key
    #print st.size()

#做一个词频统计的小程序
st = BST()
minLen = 2
s = raw_input()
if len(s)<minLen:
    pass
if not st.contains(s):
    st.put(s,1)
else:
    st.put(s,st.get(s)+1)
'''





