#lalala
class Wq(object):
    id = []
    sz = []
    count = 0
    def __init__(self,N):
        self.count = N
        for i in range(N):
            self.id.append(i)
        for j in range(N):
            self.sz.append(j)
    def countfun(self):
        return self.count
    def findfun(self,p):
        while p != self.id[p]:
            p = self.id[p]
        return p
    def connected(self,i,j):
        if self.findfun(i) == self.findfun(j):
            return True
        else :
            return False
    def union(self, p, q):
        i = self.findfun(p)
        j = self.findfun(q)
        if(i == j):
            return
        if self.sz[i] <self.sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]
        self.count -=1
