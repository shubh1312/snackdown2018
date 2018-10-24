for _ in range(int(input())):
    dict={}
    ftime=0
    for _ in range(int(input())):
        string=input()
        if string in dict:
            time=(dict.get(string)/2)
        else:
            arr=list(string)
            time=0.2
            for i in range(1,len(arr)):
                last=arr[i-1]
                if last in {'j','k'}:
                    if arr[i]=='d' or arr[i]=='f':
                        time+=0.2
                    else:
                        time+=0.4
                elif last in {'d','f'}:
                    if arr[i]=='j' or arr[i]=='k':
                        time+=0.2
                    else:
                        time+=0.4
            dict[string]=time
        ftime+=time
    print(int(round(ftime,10)*10))
