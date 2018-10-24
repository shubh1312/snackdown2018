for _ in range(int(input())):
    a,b,c=map(lambda x:"{0:b}".format(int(x)),input().split())
    ac1=a.count('1')
    bc1=b.count('1')
    count=0
    c=int(c,2)
    for i in range(1,c):
        da="{0:b}".format(i)
        db="{0:b}".format(c-i)
        if ( da.count('1')==ac1) and\
                ( db.count('1') == bc1):
            count+=1
    if a==b:
        print((count*2)-1)
    else:
        print(count)