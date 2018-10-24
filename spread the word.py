for _ in range (int(input())):
    person=int(input())
    arr=list(map(int,input().split()))
    end=arr[0]
    start=1
    sum=arr[0]
    person-=1
    day=0
    while person>0:
        for i in range(start,end):
            sum+=arr[i]
        start=end
        end=sum
        person-=sum
        day+=1
    print(day)