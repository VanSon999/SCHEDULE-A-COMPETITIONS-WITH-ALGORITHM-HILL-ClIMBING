import sys
import random 
def main(file_input):
    f = open(file_input ,"wb") 
    n = -1
    k = -1 
    while (True): 
        if (n%2 == 0) or (k%2 ==0): 
            break 
        k = random. randint (2 ,1000) 
        n = random.randint(k+1,1001) 
        _from = random.randint(1 ,100) 
        _to = random. randint(_from+1,100) 
        f.write(str(n) + "␣" + str(k) + '\n')
        for i in range(0,int(n)): 
            f.write(str(random. randint(int(_from) ,int(_to))) + '\n')      
                 
        f.close()
# if __name__ == '__main__' : main(sys . argv [1:])
main('input.txt')