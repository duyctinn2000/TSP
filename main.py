import random
import math
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
    return f
def fastcost_1(nv,cong,x1,y1,ds,old,ln,t,lnold):
    f=old
    lnt=doanhthu(nv[t],cong)-chiphi(nv[t],x1,y1,ds)
    for j in range(len(nv)):
        if j!=t:
            f=f-abs(lnold-ln[j])+abs(lnt-ln[j])
    return f,lnt
def fastcost_2(nv,cong,x1,y1,ds,old,ln,t1,t2,lnold1,lnold2):
    f=old
    lnnew1=doanhthu(nv[t1],cong)-chiphi(nv[t1],x1,y1,ds)
    lnnew2=doanhthu(nv[t2],cong)-chiphi(nv[t2],x1,y1,ds)
    f=f-abs(lnold1-lnold2)+abs(lnnew1-lnnew2)
    for j in range(len(nv)):
        if j!=t1 and j!=t2:
            f=f-abs(lnold1-ln[j])+abs(lnnew1-ln[j])
    for j in range(len(nv)):
        if j!=t2 and j!=t1:
            f=f-abs(lnold2-ln[j])+abs(lnnew2-ln[j])
    return f,lnnew1,lnnew2
def second_move(nv,cong,x1,y1,ds,old,ln,recur): #thay đổi với hai nhân viên ngẫu nhiên
    recur=recur+1
    if recur>990:
        return nv,old
    temp=[]
    ds_ran_2=[]
    ds_ran_1=list(range(len(nv)))
    for i in range(len(nv)):
        if len(nv[i])>1:
            ds_ran_2=ds_ran_2+[i]
    if len(ds_ran_2) > 0 and len(ds_ran_1)>1:
        u=random.choice(ds_ran_2)
        ds_ran_1.remove(u)
        v=random.choice(ds_ran_1)
        temp=nv[u]+nv[v]
        kx=0
        ky=0
        hx=0
        hy=0
        tx=0
        ty=0
        is_move=False
        step=0
        new=0
        while is_move==False and step<3:
            tg=copy.deepcopy(nv)
            random.shuffle(temp)
            l=random.randint(1,len(temp)-1)
            tg[u]=temp[:l]
            tg[v]=temp[l:]
            lnold1=ln[u]
            lnold2=ln[v]
            new,lnnew1,lnnew2 = fastcost_2(tg,cong,x1,y1,ds,old,ln,u,v,lnold1,lnold2)
            if old>new:
                nv=tg
                ln[u]=lnnew1
                ln[v]=lnnew2
                is_move=True
            else:
                tg=copy.deepcopy(nv)
                d=random.choice([u,v])
                new=old
                random.shuffle(tg[d]) 
                lnold=ln[d]
                new, lnnew1 = fastcost_1(tg,cong,x1,y1,ds,old,ln,d,lnold)
                if old>new:
                    nv=tg
                    ln[d]=lnnew1
                    is_move=True
                else:
                    if len(temp)>2:
                        tg=copy.deepcopy(nv)
                        e1 = random.randint(0,len(tg[u])-1)
                        e2 = random.randint(0,len(tg[u])-1)
                        new=old
                        lnnew1=ln[u]
                        if e1!=e2:
                            tg[u][e1],tg[u][e2]=tg[u][e2],tg[u][e1]
                            lnold=ln[u]
                            new, lnnew1 = fastcost_1(tg,cong,x1,y1,ds,old,ln,u,lnold)
                        e3 = random.randint(0,len(tg[v])-1)
                        e4 = random.randint(0,len(tg[v])-1)
                        lnnew2=ln[v]
                        if e3!=e4:
                            tg[v][e3],tg[v][e4]=tg[v][e4],tg[v][e3]
                            lnold=ln[v]
                            new, lnnew2 = fastcost_1(tg,cong,x1,y1,ds,new,ln,v,lnold)
                        if old>new:
                            nv=tg
                            ln[u]=lnnew1
                            ln[v]=lnnew2
                            is_move=True
                        else:
                            kx,hx,tx=random.sample(temp,3)
                            kt,ht,tt=False,False,False
                            for i in (u,v):
                                if (kt==True and ht==True and tt==True):
                                    break
                                for j in range(len(nv[i])):
                                    if (kx==nv[i][j] and kt==False):
                                        kx,ky=i,j
                                        kt=True
                                    elif (hx==nv[i][j] and ht==False):
                                        hx,hy=i,j
                                        ht=True
                                    elif (tx==nv[i][j] and tt==False):
                                        tx,ty=i,j
                                        tt=True
                            a=[[kx,ky]]+[[hx,hy]]+[[tx,ty]]
                            i=[kx,ky]
                            j=[hx,hy]
                            z=[tx,ty]
                            i,j,z=random.sample(a,3)
                            tg=copy.deepcopy(nv)
                            h=tg[i[0]][i[1]]
                            k=tg[j[0]][j[1]]
                            t=tg[z[0]][z[1]]
                            tg[kx][ky]=h
                            tg[hx][hy]=k      
                            tg[tx][ty]=t
                            lnold1=ln[u]
                            lnold2=ln[v]
                            new,lnnew1,lnnew2 = fastcost_2(tg,cong,x1,y1,ds,old,ln,u,v,lnold1,lnold2)
                            if old>new:
                                nv=tg
                                ln[u]=lnnew1
                                ln[v]=lnnew2
                                is_move=True
                            else:
                                i = random.randint(0,len(nv[u])-1)
                                j = random.randint(0,len(nv[v])-1)
                                tg=copy.deepcopy(nv)
                                tg[u][i],tg[v][j]=tg[v][j],tg[u][i]
                                lnold1=ln[u]
                                lnold2=ln[v]
                                new,lnnew1,lnnew2 = fastcost_2(tg,cong,x1,y1,ds,old,ln,u,v,lnold1,lnold2)
                                if old>new:
                                    nv=tg
                                    ln[u]=lnnew1
                                    ln[v]=lnnew2
                                    is_move=True
                                elif (len(nv[v])>1):
                                    tg=copy.deepcopy(nv)
                                    tg[u] = tg[u] + [tg[v][j]]
                                    tg[v].remove(tg[v][j])
                                    lnold1=ln[u]
                                    lnold2=ln[v]
                                    new,lnnew1,lnnew2 = fastcost_2(tg,cong,x1,y1,ds,old,ln,u,v,lnold1,lnold2)
                                    if old>new:
                                        nv=tg
                                        ln[u]=lnnew1
                                        ln[v]=lnnew2
                                        is_move=True
                                    elif (len(nv[u])>1):
                                        tg=copy.deepcopy(nv)
                                        tg[v] = tg[v] + [tg[u][i]]
                                        tg[u].remove(tg[u][i])
                                        lnold1=ln[u]
                                        lnold2=ln[v]
                                        new,lnnew1,lnnew2 = fastcost_2(tg,cong,x1,y1,ds,old,ln,u,v,lnold1,lnold2)
                                        if old>new:
                                            nv=tg
                                            ln[u]=lnnew1
                                            ln[v]=lnnew2
                                            is_move=True
                                        else:
                                            step=step+1
                                    else:
                                        step=step+1
                                else:
                                    step=step+1
                    else:
                        step=step+1
        if is_move==True:
            return first_move(nv,cong,x1,y1,ds,new,ln,recur)
        else:
            return nv, old
    return nv, old
def first_move(nv,cong,x1,y1,ds,old,ln,recur):   #thay đổi với nhân viên có lợi nhuận cao nhất và nhân viên có lợi nhuận thấp nhất
    recur=recur+1
    if recur>990:
        return nv,old
    lnmotnv=list(range(len(nv)))
    u=0
    v=0
    min=0
    max=0
    for i in range(len(nv)):
        lnmotnv[i]=loinhuan(nv[i],cong,x1,y1,ds)
        if i==0:
            min=lnmotnv[i]
            max=lnmotnv[i]
            u=i
            v=i
        else:
            if min>lnmotnv[i]:
                min=lnmotnv[i]
                u=i
            if max<lnmotnv[i]:
                max=lnmotnv[i]
                v=i
    if u!=v:
        temp=nv[u]+nv[v]
        kx=0
        ky=0
        hx=0
        hy=0
        tx=0
        ty=0
        is_move=False
        step=0
        new=0
        if len(temp)>2:
            while is_move==False and step<2:
                tg=copy.deepcopy(nv)
                random.shuffle(temp)
                l=int(len(temp)/2)
                tg[u]=temp[:l]
                tg[v]=temp[l:]
                lnold1=ln[u]
                lnold2=ln[v]
                new,lnnew1,lnnew2 = fastcost_2(tg,cong,x1,y1,ds,old,ln,u,v,lnold1,lnold2)
                if old>new:
                    nv=tg
                    ln[u]=lnnew1
                    ln[v]=lnnew2
                    is_move=True
                else:
                    tg=copy.deepcopy(nv)
                    d=random.choice([u,v])
                    new=old
                    random.shuffle(tg[d]) 
                    lnold=ln[d]
                    new, lnnew1 = fastcost_1(tg,cong,x1,y1,ds,old,ln,d,lnold)
                    if old>new:
                        nv=tg
                        ln[d]=lnnew1
                        is_move=True
                    else:  
                        tg=copy.deepcopy(nv)
                        e1 = random.randint(0,len(tg[u])-1)
                        e2 = random.randint(0,len(tg[u])-1)
                        new=old
                        lnnew1=ln[u]
                        if e1!=e2:
                            tg[u][e1],tg[u][e2]=tg[u][e2],tg[u][e1]
                            lnold=ln[u]
                            new, lnnew1 = fastcost_1(tg,cong,x1,y1,ds,old,ln,u,lnold)
                        e3 = random.randint(0,len(tg[v])-1)
                        e4 = random.randint(0,len(tg[v])-1)
                        lnnew2=ln[v]
                        if e3!=e4:
                            tg[v][e3],tg[v][e4]=tg[v][e4],tg[v][e3]
                            lnold=ln[v]
                            new, lnnew2 = fastcost_1(tg,cong,x1,y1,ds,new,ln,v,lnold)
                        if old>new:
                            nv=tg
                            ln[u]=lnnew1
                            ln[v]=lnnew2
                            is_move=True
                        else:
                            kx,hx,tx=random.sample(temp,3)
                            kt,ht,tt=False,False,False
                            for i in (u,v):
                                if (kt==True and ht==True and tt==True):
                                    break
                                for j in range(len(nv[i])):
                                    if (kx==nv[i][j] and kt==False):
                                        kx,ky=i,j
                                        kt=True
                                    elif (hx==nv[i][j] and ht==False):
                                        hx,hy=i,j
                                        ht=True
                                    elif (tx==nv[i][j] and tt==False):
                                        tx,ty=i,j
                                        tt=True
                            a=[[kx,ky]]+[[hx,hy]]+[[tx,ty]]
                            i=[kx,ky]
                            j=[hx,hy]
                            z=[tx,ty]
                            i,j,z=random.sample(a,3)
                            tg=copy.deepcopy(nv)
                            h=tg[i[0]][i[1]]
                            k=tg[j[0]][j[1]]
                            t=tg[z[0]][z[1]]
                            tg[kx][ky]=h
                            tg[hx][hy]=k      
                            tg[tx][ty]=t
                            lnold1=ln[u]
                            lnold2=ln[v]
                            new,lnnew1,lnnew2 = fastcost_2(tg,cong,x1,y1,ds,old,ln,u,v,lnold1,lnold2)
                            if old>new:
                                nv=tg
                                ln[u]=lnnew1
                                ln[v]=lnnew2
                                is_move=True
                            else:
                                i = random.randint(0,len(nv[u])-1)
                                j = random.randint(0,len(nv[v])-1)
                                tg=copy.deepcopy(nv)
                                tg[u][i],tg[v][j]=tg[v][j],tg[u][i]
                                lnold1=ln[u]
                                lnold2=ln[v]
                                new,lnnew1,lnnew2 = fastcost_2(tg,cong,x1,y1,ds,old,ln,u,v,lnold1,lnold2)
                                if old>new:
                                    nv=tg
                                    ln[u]=lnnew1
                                    ln[v]=lnnew2
                                    is_move=True
                                elif (len(nv[v])>1):
                                    tg=copy.deepcopy(nv)
                                    tg[u] = tg[u] + [tg[v][j]]
                                    tg[v].remove(tg[v][j])
                                    lnold1=ln[u]
                                    lnold2=ln[v]
                                    new,lnnew1,lnnew2 = fastcost_2(tg,cong,x1,y1,ds,old,ln,u,v,lnold1,lnold2)
                                    if old>new:
                                        nv=tg
                                        ln[u]=lnnew1
                                        ln[v]=lnnew2
                                        is_move=True
                                    elif (len(nv[u])>1):
                                        tg=copy.deepcopy(nv)
                                        tg[v] = tg[v] + [tg[u][i]]
                                        tg[u].remove(tg[u][i])
                                        lnold1=ln[u]
                                        lnold2=ln[v]
                                        new,lnnew1,lnnew2 = fastcost_2(tg,cong,x1,y1,ds,old,ln,u,v,lnold1,lnold2)
                                        if old>new:
                                            nv=tg
                                            ln[u]=lnnew1
                                            ln[v]=lnnew2
                                            is_move=True
                                        else:
                                            step=step+1
                                    else:
                                        step=step+1
                                else:
                                    step=step+1
        if is_move==True:
            return first_move(nv,cong,x1,y1,ds,new,ln,recur)
        else:
            return second_move(nv,cong,x1,y1,ds,old,ln,recur)
    return second_move(nv,cong,x1,y1,ds,old,ln,recur)
def assign(file_input, file_output):
    #print("Giai thuat duoc chay trong vong duoi mot phut")
    start = timeit.default_timer()
    with open(file_input) as f:
        x, y = [int(x) for x in next(f).split()] # read first line
        n, m = [int(x) for x in next(f).split()] # read second line
        array = []
        dem=1
        for line in f: # read rest of lines
            if dem>n:
                break
            dem=dem+1
            array.append([int(x) for x in line.split()])
    ds=array
    # run algorithm
    if (n<m or m<=0 or n<=0):
        print("Khong thoa dieu kien m>0, n>0 va n>=m")
    else:
        nv=list(range(m))
        if n==m:
            for i in range(m):
                nv[i]=[i]
        elif m==1:
            nv[0]=[]
            for i in range(n):
                nv[0]=nv[0]+[i]
        else:
            cong=list(range(len(ds)))
            for i in range(m):
                nv[i]=[]
            for i in range(len(ds)):
                cong[i]=5+ds[i][2]+(ds[i][3]*2)
            ds_rd=list(range(len(ds)))
            ln=list(range(m))
            while (ds_rd):
                for i in range(m):
                    if (ds_rd):
                        u=random.choice(ds_rd)
                        nv[i]=nv[i]+[u]
                        ds_rd.remove(u)
                    else:
                        break
            for i in range(m):
                ln[i]=loinhuan(nv[i],cong,x,y,ds)
            ct=0
            for i in range(len(nv)-1):
                for j in range(i+1,len(nv)):
                    ct=ct+abs(ln[i]-ln[j])
            #print(ct)
            new_cost=ct
            count=0
            for i in range(100000):
                recur=0
                old_cost = new_cost
                #print(count)
                #print(new_cost)
                nv, new_cost=first_move(nv,cong,x,y,ds,old_cost,ln,recur)        
                timeend=timeit.default_timer() - start
                if (timeend>300):
                    print(1000)
                    break
                #print('Time: ', timeend)
                if math.ceil(old_cost*1000000)/1000000 <= math.ceil(new_cost*1000000)/1000000:
                    count=count+1
                else:
                    count=0
                if count>10000:
                    break
            print(cost(nv,cong,x,y,ds))
        with open(file_output, 'w') as out_file: 
            for i in range(len(nv)):
                for j in range(len(nv[i])):
                    if (j<len(nv[i])-1):
                        out_file.write('%s ' % nv[i][j])
                    else:
                        out_file.write('%s' % nv[i][j])
                if (i<len(nv)):
                    out_file.write('\n')
        #stop = timeit.default_timer()
        #print('Time: ', stop - start)
assign('input.txt', 'output.txt')
