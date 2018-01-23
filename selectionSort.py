#lalala
def isLess(i,j):
    if i < j:
        return True
    else:
        return False

def exch(a,i,j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def selectionSort(a):
    n = len(a)
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if isLess(a[j],a[min]):
                min = j
                exch(a,i,j)

    return a
