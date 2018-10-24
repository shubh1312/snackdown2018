for _ in range (int(input())):
    limit=int(input())
    arr=list(map(int,input().split()))
    if arr[0]>=arr[len(arr)-1]:
        largest=arr[0]
        count=1
        for i in range(len(arr)):
            if arr[i]>=largest:
                largest=arr[i]
            elif arr[i]<largest:
                largest=arr[i]
                count+=1
                if count>2:
                    print("NO")
                    break
        else:
            print("YES")
    elif sorted(arr)==arr:
        print('YES')
    else:
        print("NO")
