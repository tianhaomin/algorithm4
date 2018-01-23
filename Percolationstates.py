#percolationstats
#lalala
import random
import math
from percolation1.percolation import percolation

x = []
expTimes = 0
T = input()
M = int(raw_input())
expTimes = T
ppp = percolation(M)
x = [0.0]*(T+1)
for i in range(1,T+1):
    numofLine = 0
    isEmptysiteline = [False]*(M+1)
    while True:
        posX = random.randint(0,M)
        posY = random.randint(0,M)
        ppp.openFunc(posX,posY)
        x[i]+=1
        if not isEmptysiteline[posX]:
            isEmptysiteline[posX] = True
            numofLine += 1
        if numofLine == ppp.N:
            break
    x[i] = x[i]/(float)(M*M)

def mean():
    mu = 0.0
    for i in range(1,expTimes+1):
        mu += x[i]
    return mu/((float)(expTimes))
def stdev():
    if expTimes == 1:
        return 0.0
    sigma = 0.0
    mu = mean()
    for i in range(1,expTimes+1):
        sigma += (x[i] - mu)*(x[i] - mu)
    return math.sqrt(sigma/((float)(expTimes - 1)))
def confidencelow():
    mu = mean()
    sigma = stdev()
    return mu - 1.96*sigma/math.sqrt(expTimes)
def confidencehigh():
    mu = mean()
    sigma = stdev()
    return mu + 1.96*sigma/math.sqrt(expTimes)



print mean()