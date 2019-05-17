import itertools as it
import random
import sys
def random_combination(iterable, r):
    "Random selection from itertools.combinations(iterable, r)"
    pool = tuple(iterable)
    n = len(pool)
    indices = sorted(random.sample(range(n), r))
    return tuple(pool[i] for i in indices)

def check_(mt_,i,n,k): #tra ve doi thu da ghep chung va so doi thu con lai
    ls_doithu = []
    for j in range(i,n): #quet theo cot
        # print(j)
        if(mt_[i][j-i] == 1): 
            k -=1
            # print(j)
            ls_doithu.append(j)
    for j in range(0,i): #quet theo hang
        if(mt_[j][i-j] == 1):
            k -=1
            # print(j)
            ls_doithu.append(j)
    return (ls_doithu,k)

def update_matrix(mt_,list_,i):
    for j in range(len(mt_[i])):
        mt_[i][j] = 0
    for j in list_:
        if(j>i):
            mt_[i][j-i] = 1

    return mt_

def update_matrix_2(mt_, list_,i):
    #quet cot
    for j in range(len(mt_[i])):
        mt_[i][j] = 0
    for j in list_:
        if(j>i):
            mt_[i][j-i] = 1
    #quet hang
    for j in range(0,i+1):
        mt_[j][i-j] = 0
    for j in list_:
        if(j < i):
            mt_[j][i-j] = 1
    return mt_

def initial_state(k,n): #tra ve danh sach khoi tao cung nhu ma tran khoi tao tuong ung!
    #mot so truong hop dac biet:
    list_doithu = []
    mt = [[0 for i in range(n-x+1) ] for x in range(1,n+1)]
    #######################################################################
    if(k==1):
        for x in range(0,n-1):
            if(x%2 == 0):
                list_doithu.append([x+1])
            else:
                list_doithu.append([x-1])
        list_doithu.append([n-2])
        #convert to mt
        for x in range(0,n):
            mt = update_matrix(mt,list_doithu,x)
    #######################################################################
    elif(k==2):
        for x in range(0,n-1):
            if (x==0):
                list_doithu.append([1,n-1])
            else:
                # print(x)
                list_doithu.append([x-1,x+1])
        list_doithu.append([0,n-2])
        #convert to mt
        for x in range(0,n):
            mt = update_matrix(mt,list_doithu[x],x)
    #######################################################################
    elif (k == n/2 and n%2 == 0): #k = n/2 và n chẵn
        for x in range(0,n):
            if(x <= (k-1)):
                list_doithu.append([i for i in range(k,n)])
            else:
                list_doithu.append([i for i in range(0,k)])
        #convert to mt
        for x in range(0,n):
            mt = update_matrix(mt,list_doithu[x],x)
    #######################################################################
    elif (k == n-1):
        for x in range(0,n):
            list_doithu.append([i for i in range(0,n) if i!=x])
        #convert to mt
        for x in range(0,n):
            mt = update_matrix(mt,list_doithu[x],x)
    #mot so truong hop dac biet
    #######################################################################
    else:
        temp = subinitial_state(n,k)
        list_doithu = temp[0]
        mt = temp[1]
    return (list_doithu,mt)

    #cac truong hop khac! ta sinh random to hop doi thu cho tung vdv roi doi chieu nhau qua ma tran!
def subinitial_state(n,k):
    mt_1 = []
    doithu = []
    while(True):
        mt_1 = [[0 for i in range(n-x+1) ] for x in range(1,n+1)]
        # print(mt_1)
        bool1 = True
        # print(lis)
        for i in range(0,n):
            lis = [x for x in range(i,n)]
            at = check_(mt_1,i,n,k) #kiem tra doi thu da dau va da du chua
            ####
            # print("i:",i)
            # print(at[0])
            # print(at[1])
            ####
            if(at[1] == 0): 
                # print('continue')
                continue

            if(((at[1] > 0) and (i == n-1)) or (at[1] < 0)): 
                bool1 = False
                # print("break ")
                break

            for t in at[0]: #cap nhat doi thu
                if(t in lis):
                    lis.remove(t)

            lis.remove(i) #i k the la doi thu cua i!

            if(len(lis) < at[1]):
                bool1 = False
                break
            # print("danh sach: ", lis)
            doithu_of_i = random_combination(lis, at[1]) #tao doi thu random
            # print("doi thu cua i: ", doithu_of_i)
            #cap nhat vao maxtrix_
            mt_1 = update_matrix(mt_1,doithu_of_i,i)
        #dk de dung vong lap
        if(bool1):break
    
    for x in range(0,n):
        temp = check_(mt_1,x,n,k)
        doithu.append(temp[0])
    return (doithu,mt_1)

def getSum_(ls1,ls2,n): #ls1 la danh sach doi thu, ls2 so diem tuong ung 
    Sum_ = []
    for x in range(len(ls1)):
        S = 0
        for y in ls1[x]:
            S = S + ls2[y]
        # print(S)
        Sum_.append(S)
    max_ = max(Sum_)
    min_ = min(Sum_)
    for x in range(0,n):
        if Sum_[x] == min_:
            Sum_ene_min = x
            break

    for x in range(0,n):
        if Sum_[x] == max_:
            Sum_ene_max = x
            break

    return (Sum_, Sum_ene_max, Sum_ene_min)

def getMax(ls,ls_p):
    Max__ = -100
    t = 0
    for x in ls:
        if(Max__ < ls_p[x]):
            Max__ = ls_p[x]
            t = x
    return t

def getMin(ls,ls_p):
    Min__ = 1000000000
    t = 0
    for x in ls:
        if(Min__ > ls_p[x]):
            Min__ = ls_p[x]
            t = x
    return t

def process(mt_,n,k,ls,ls_p):#ls la danh sach doi thu, ls_p la danh sach diem so
    while(True):
        bool_t = True
        ls_try = [list(x) for x in ls]
        Sum_p, Ene_max, Ene_min = getSum_(ls_try,ls_p,n)
        mnt = [[i for i in x ] for x in mt_] #ma tran tam thoi de luu trang thai thay doi
        #danh sach doi thu can trao doi giua cac vđv max min:
        list_max = []#danh sach max của vận động viên Ene_max cần trao đổi
        for x in ls_try[Ene_max]:
            if((x != Ene_max) and (x != Ene_min) and (x not in list_max)):
                list_max.append(x)
        list_min = []#danh sach min của vận động viên Ene_min cần trao đổi
        for x in ls_try[Ene_min]:
            if((x != Ene_max) and (x != Ene_min) and (x not in list_min)):
                list_min.append(x)
        
        # if ((list_max ==[]) or (list_min ==[]) ):
        #     break 

        while (list_max != [] and list_min != []):
            ma = getMax(list_max,ls_p)
            mi = getMin(list_min,ls_p)
            #qua trinh trao doi max min cua hai cau thu!
            list_max.remove(ma)   
            list_min.remove(mi)
            ls_try[Ene_max].remove(ma)
            ls_try[Ene_min].remove(mi)
            ls_try[Ene_max].append(mi)
            ls_try[Ene_min].append(ma)
            update_matrix_2(mnt,ls_try[Ene_max],Ene_max) #cap nhat lai ma tran sau khi trao doi
            update_matrix_2(mnt,ls_try[Ene_min],Ene_min)
            temp_list = [] #danh sach doi thu tam thoi sau khi cap nhat!
            for x in range(0,n):
                temp = check_(mnt,x,n,k)
                temp_list.append(temp[0]) 
            Sum_p2, Ene_max2, Ene_min2 = getSum_(temp_list,ls_p,n)
            #su dung ham luon gia H = maxdt(cua i) - mindt(cua j) cang nho cang tot
            if (((Sum_p2[Ene_max2] - Sum_p2[Ene_min2]) < (Sum_p[Ene_max] - Sum_p[Ene_min])) and (Ene_max2 != Ene_max) and (Ene_min2 != Ene_min)):
                ls = [list(x) for x in temp_list]
                mt_ = mnt
                bool_t = False
                break
        if (list_max ==[]) or (list_min ==[]):
            if(bool_t):
                break
    return ls

def main(file_input, file_output):
    # read input
    f = open(file_input,'r')
    list_point = []
    list_point = [int(x) for x in f.read().split() if x.isdigit()]
    f.close()
    n = list_point.pop(0)
    k = list_point.pop(0)
    
    # run algorithm
    if((n%2 != 0 and k%2 !=0 )or (k >= n)):
        print("Khong the xep duoc lich thi dau")
        return

    #tao mot nua tren cua ma tran
    # matrix_ = [[0 for i in range(n-x+1) ] for x in range(1,n+1)] #tao mot nua tren cua ma tran
    print("Danh sach trang thai khoi tao!:")
    temp_ = initial_state(k,n)
    ds_1= temp_[0]
    print(ds_1)
    # mn = temp_[1]
    # # print(mn)
    # mn = update_matrix_2(mn,[1,3],0)
    # print(update_matrix_2(mn,[1,4],2))
    #Hill Climbing##########################################################
    ds_2 = process(temp_[1],n,k,ds_1,list_point)
    #Hill Climbing##########################################################    
    print("Danh sach trang thai toi uu!:")
    print(ds_2)
    # print("Nua tren cua ma tran trang thai khoi tao")
    # matran = temp_[1]
    # print(matran)
    # t = getSum_(ds_,list_point,n)
    # print(t[1])
    # print(t[2])
    # print(mt_)
    # print(initial_state(k,n))
    # print(list(it.combinations(list_point, k)))
    
    # write output
    f = open(file_output,'w')
    for x in range(len(ds_2)):
        for y in range(len(ds_2[x])):
            if((x == len(ds_2) - 1) and (y == len(ds_2[x]) - 1)):
                f.write(str(ds_2[x][y]))
            else:
                f.write(str(ds_2[x][y]) +'\n')
    return


main('in.txt', 'output.txt')
