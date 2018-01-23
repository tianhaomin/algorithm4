#!/usr/bin/python
# -*- coding: UTF-8 -*-
#红黑二叉树是将2,3平衡二叉树转化成红黑的二叉树基本方法与之前的BST是一样的但是插入操作不同
#构建红黑二叉树的时候需要进行反转转化
class Node(object):
    def __init__(self,k,v,s):
        self.value = v
        self.left = None
        self.right = None
        self.size = s
        self.key = k
        self.color = 'RED'#定义节点的时候多了一个颜色需要进行定义,color的颜色是指parent link
class redblackBST(object):
    #很多的基本操作基本都是一样的
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
    #检查颜色的函数
    def isRed(self,x):
        if x == None:
            return False
        return x.color == 'RED'
    #插入的过程会有所变化需要一些前期准备比如一些适当而定反转
    def rotateLeft(self,h):
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = 'RED'
        return x
    def rotateRight(self,h):
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = 'RED'
        return x
    def colorFlip(self,h):
        h.color = 'RED'
        h.left.color = 'BLACK'
        h.left.color = 'BLACK'
    def put(self,k,v):
        if v == None:
            self.delete(k)
            return
        self.root = self.put1(self.root,k,v)
        self.root.color = 'BLACK'
    #Assuming that h is red and both h.left and h.left.left
    def moveRedLeft(self,x):
        self.colorFlip(x)
        if self.isRed(x.right.left):
            x.right = self.rotateRight(x.right)
            x = self.rotateLeft(x)
            self.colorFlip(x)
        return x
    #Assuming that h is red and both h.right and h.right.left
    def moveRedRight(self,x):
        self.colorFlip(x)
        if self.isRed(x.left.left):
            x = self.rotateRight(x)
            self.flipColor(x)
        return x
    # restore red-black tree invariant
    #在需要爱翻转的时候进行翻转同时进行技术
    def balance(self,x):
        if self.isRed(x.right):
            x = self.rotateLeft(x)
        if self.isRed(x.left) and self.isRed(x.left.left):
            x = self.rotateLeft(x)
        if self.isRed(x.left) and self.isRed(x.right):
            self.colorFlip(x)
        x.size = self.size(x.left) + self.size(x.right) + 1
        return x
#查看红黑二叉树的高度
    def height(self):
        return self.height1(self.root)
    def height1(self,x):
        if x == None:
            return -1
        return 1+max(self.height(x.right),self.height(x.right))
    #插入函数差别较大需要进行翻转同时也需要函数的重写
    def put1(self,h,k,v):
        if h == None:#前半部分是在找指定的key值
            return Node(k,v,1)
        if k<h.key:
            k.left = self.put(h.left,k,v)
        elif k>h.key:
            h.right = self.put(h.right,k,v)
        else:
            h.val = v
        #赚转的原则就是右边是红左转，左边连续两个是红右转，左右两边都是红就进行颜色的翻转
        if self.isRed(h.right) and not self.isRed(h.left):
            h = self.rotateLeft(h)
        elif self.isRed(h.left) and self.isRed(h.left.left):
            h = self.rotateRight(h)
        elif self.isRed(h.left) and self.isRed(h.right):
            self.colorFilp(h)
        h.size = self.size(h.left) + self.size(h.right) + 1
        return h

    def deleteMin(self):
        if not self.isRed(self.root.left) and not self.isRed(self.root.right):
            self.root.color = 'RED'
        self.root = self.deleteMin1(self.root)
        if not self.isEmpty():
            self.root.color = 'BLACK'
    def deleteMin1(self,x):
        if x.left == None:
            return x.right#如果node x没有做节点那么就将它用右子树代替
        if not self.isRed(x.left) and not self.isRed(x.left.left):
            x = self.moveRedLeft(x)
        x.left = self.deleteMin(x.left)
        return self.balance(x)
    def deleteMax(self):
        if not self.isEmpty(self.root.left) and not self.isRed(self.root.right):
            self.root.color = 'RED'
        self.root = self.deleteMax1(self.root)
        if not self.isEmpty():
            self.root.color = 'BLACK'
    def deleteMax1(self,x):
        if self.isRed(x.left):
            x = self.rotateRight(x)
        if x.right == None:
            return x.left
        if not self.isRed(x.right) and not self.isRed(x.right.left):
            x = self.moveRedRight(x)
        x.right = self.deleteMax(x.right)
        return self.balance(x)
    def delete(self,k):
        if not self.contains(k):
            return
        if not self.isRed(self.root.left) and not self.isRed(self.root.right):
            self.root.color = 'RED'
        self.root = self.delete1(self.root,k)
        if not self.isEmpty():
            self.root.color = 'BLACK'
#删除指定的节点
    def delete1(self,x,k):

        if k<x.key:
            if not self.isRed(x.left) and not self.isRed(x.left.left):
                x = self.moveRedLeft(x)
            x.left = self.delete(x.left,k)
        else:
            if self.isRed(x.left):
                x = self.rotateRight(x)
            if k == x.key and x.right == None:
                return None
            if not self.isRed(x.right) and not self.isRed(x.right.left):
                x = self.moveRedRight(x)
            if k == x.key:
                h = self.min(x.right)
                x.key = h.key
                x.val = h.val
                x.right = self.deleteMin(x.right)
            else:
                x.right = self.delete(x.right,k)
        return self.balance(x)
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
    #找出排名为k的节点
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
#找出小于给定键值的数目，找出关键值key的排名
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
    def isBST(self):
        return self.isBST1(self.root,None,None)
    #查看红黑树是不是符合对称结构
    def isBST1(self,x,min,max):
        if x == None:
            return True
        if not min == None and x.key<=min:
            return False
        if not max == None and x.key>=max:
            return False
        return self.isBST1(x.left,min.x.key) and self.isBST1(x.right,x.key,max)
        #就是检查左右分支的节点是不是确实小于或大于词节点的键值
    #检查是不是节点尺寸计算正确
    def isSizeConsistent(self):
        return self.isSizeConsistent1(self.root)
    def isSizeConsistent1(self,x):
        if x == None:
            return True
        if not x.size == (self.size(x.left) + self.size(x.right) + 1):
            return False
        return self.isSizeConsistent1(x.left) and self.isSizeConsistent1(x.right)
    #查看节点的排名是否正确
    def isRankConcicter(self):
        for i in range(self.size()):
            if not i == self.rank(self.select(i)):
                return False
        #还有一部分

    #检查是不是没有右红连接而且最多只有一条左红连接对于一个节点也就是说没有连续的红连接在左边
    #这样的情况符合一个3node的情况
    def is23(self):
        return self.is231(self.root)
    def is231(self,x):
        if x == None:
            return True
        if self.isRed(x.right):
            return False
        if not x == self.root and self.isRed(x) and self.isrRed(x.left):
            return False
        return self.is231(x.left) and self.is231(x.right)
    #检查是不是每条路径上的黑连接的数量相等
    def isBalanced(self):
        black = 0
        x = self.root
        while x != None:
            if not self.isRed(x):
                black += 1
            x = x.left
        return self.isBalanced1(self.root,black)
    def isBalanced1(self,x,black):
        if x == None:
            return black == 0
        if not self.isRed(x):
            black -= 1
        return self.isBalanced1(x.left,black) and self.isBalanced1(x.right,black)
