for _ in range(int(input())):
    arr=list(map(int,input()))
    flag=False
    for i in range (len(arr)-1,1,-1):
        for j in range(i-1,1,-1):
            if arr[i]==arr[j]:
                print(arr[i],i+1)
                flag=True
                break
    else:
        if flag==False:
            print('-1')