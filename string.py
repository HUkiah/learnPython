#!/usr/bin/python
# -*- coding:utf-8 -*-

def triangles():
    a,b=[1],[1,1]
    yield a
    while True:
        yield b
        insertCount=len(b)-1
        temp=[]
        for x in range(insertCount):
            temp.append(b[x]+b[x+1])
        temp.insert(0,1)
        temp.append(1)
        b=temp[:]  
n=0
for t in triangles():
    print(t)
    n=n+1
    if n>=10:
        break
