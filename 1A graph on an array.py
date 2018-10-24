from math import gcd
def coprime(a,b):
    return gcd(a,b)==1
for _ in range(int(input())):
    limit=int(input())
    arr=list(map(int,input().split()))
    count=0
    for i in range(0,len(arr)-1):
        if (coprime(arr[i],arr[i+1]))== False:
            count+=1
            for j in range(2,51):
                if (i + 2) < len(arr):
                    if (coprime(arr[i],j))==True and \
                            (coprime(j,arr[i+2]))==True:
                        arr[i + 1] = j
                        break
                else:
                    if (coprime(arr[i], j)) == True:
                        arr[i + 1] = j
                        break
    print(count)
    print(*arr,sep=' ')