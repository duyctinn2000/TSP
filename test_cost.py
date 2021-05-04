# Them cac thu vien neu can
import random
import math
import csv
import timeit
import copy
def doanhthu(motnv,cong):
    dt=0
    for i in range (len(motnv)):
        dt=dt+cong[motnv[i]]
    return dt
def khoangcach(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)
def chiphi(motnv,x1,y1,ds):
    kc=0
    for i in range (len(motnv)):
        x2=ds[motnv[i]][0]
        y2=ds[motnv[i]][1]
        kc=kc+khoangcach(x1,y1,x2,y2)
        x1=x2
        y1=y2
    return kc/40*20+10
def loinhuan(motnv,cong,x1,y1,ds):
    return doanhthu(motnv,cong)-chiphi(motnv,x1,y1,ds)
def cost(nv,cong,x1,y1,ds):
    f=0
    for i in range(len(nv)-1):
        for j in range(i+1,len(nv)):
            f=f+abs(loinhuan(nv[i],cong,x1,y1,ds)-loinhuan(nv[j],cong,x1,y1,ds))
    return f*2
def assign(file_input, file_output):
    start = timeit.default_timer()
    with open(file_input) as f:
        x, y = [int(x) for x in next(f).split()] # read first line
        n, m = [int(x) for x in next(f).split()] # read first line
        array = []
        dem=1
        for line in f: # read rest of lines
            if dem>n:
                break
            dem=dem+1
            array.append([int(x) for x in line.split()])
    ds=array
    # run algorithm
    cong=list(range(len(ds)))
    nv=list(range(m))
    for i in range(m):
        nv[i]=[]
    for i in range(len(ds)):
        cong[i]=5+ds[i][2]+(ds[i][3]*2)
    kk=[]
    with open(file_output) as f:
        for line in f: # read rest of lines
            kk.append([int(x) for x in line.split()])
    new_cost=cost(kk,cong,x,y,ds)
    s=0
    for i in range(len(kk)):
        for j in range(len(kk[i])):
            s=s+kk[i][j]
    print(s)
    print(new_cost)
#    for i in range(len(nv)):
#    print(loinhuan(nv[i],cong,x,y,ds))
assign('input.txt', 'output.txt')