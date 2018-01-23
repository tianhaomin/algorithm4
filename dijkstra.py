#lalala
import math
s1 = raw_input("Please enter : ")
l1 = list(s1)
ops = []
val = []
v = 0

for i in l1:
    if i == '(':
        pass
    elif i == '+':
        ops.append(i)
    elif i == '-':
        ops.append(i)
    elif i == '*':
        ops.append(i)
    elif i == '/':
        ops.append(i)
    elif i == 'sqrt':
        ops.append(i)
    elif i == ')':
        op = ops.pop()
        v = float(val.pop())
        if op == '+':
            v += float(val.pop())
        elif op == '-':
            v -= float(val.pop())
        elif op == '*':
            v *= float(val.pop())
        elif op == '/':
            v /= float(val.pop())
        elif op == 'sqrt':
            v = math.sqrt(float(val.pop()))
        val.append(v)
    else:
        val.append(i)
print val.pop()

