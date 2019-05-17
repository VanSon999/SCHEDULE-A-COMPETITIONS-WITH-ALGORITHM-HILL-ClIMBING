import copy

class Mem:
    #id : int
    #point : int
    #count : int //so lan thi dau
    #opp : list of string  // danh sach doi thu
    #total : sum of opp point
    def __init__(self,inid,inpoint,incount ,inopp ,intotal):
        self.id = inid
        self.point = inpoint
        self.count = incount
        self.opp = inopp
        self.total = intotal
    def __str__(self):
        return str(self.id)+" list opp : [ "+','.join(str(x.id) for x in self.opp) + "]"

def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i].point < righthalf[j].point:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
def checkopp(my,opp):

    for i in range (len (my)):
        if (my[i].id == opp):

            return False
    return True

def mix(m,alt, k):
    t = 0
    for i in range ( len(m)//2):
        m[i][0] = copy.copy(alt[t%len(alt)])
        m[i][0].count += 1
        t+=1
    
    for j in range ( len(m)//2):
        while (1):
            
            if (alt[t%len(alt)].id != m[j][0].id and alt[t%len(alt)].count<k ):
                if(checkopp(alt[t%len(alt)].opp,m[j][0].id)):
                    m[j][1] = copy.copy(alt[t%len(alt)])
                    m[j][1].opp.append(m[j][0])
                    m[j][0].opp.append(m[j][1])
                    m[j][1].count +=1
                    t+=1
                    break
                else:
                    t+=1
            else:

                t+=1 
                continue
                
                    


def main(file_input, file_output):
    # read input
    infile = open(file_input)
    data = infile.readlines()
    n,k = data[0].split()
    n= int(n)
    k= int(k)
    lst = []
    i=1
    
    for x in data[1:]:
        x=int(x)
        temp = Mem(i,x,0,[],0)
        lst.append(temp)
        i=i+1
    infile.close()

    nMatch = n * k 
    matrix = [[0 for i in range(2)] for j in range(nMatch)]
    mix(matrix,lst,k)

    for i in range ( len (lst)):
        print(lst[i])


    # run algorithm
   
    
    return

main('input.txt', 'output.txt')
