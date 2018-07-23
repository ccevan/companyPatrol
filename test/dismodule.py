
import dis

# def add(a):
#     print(a)
#     return a
#
#
# def change(a,b):
#     a,b = b,a+b
#
#
# dis.dis(change)

def change():
    x = [0,1]
    i = 0
    i,x[i] = [1,2]

import dis
#
dis.dis(change)
