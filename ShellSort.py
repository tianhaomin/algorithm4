#lalala
def less(a,i,j):
    return a[i]<a[j]
def exch(a,i,j):
    temp = a[j]
    a[j] = a[i]
    a[i] = temp
def sort(a):
    N = len(a)
    h = 1
    while h<N/3:
        h = 3*h+1
    while h>=1:
        for i in range(h,N):
            j = i
            while j>=h and less(a,j,j-h):
                exch(a,j,j-h)
                j -= h
        h = h/3

a = [3,4,1,5,0,56,34,22]
sort(a)
print a