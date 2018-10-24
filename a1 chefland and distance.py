for _ in range (int(input())):
    n,m=map(int,input().split())
    arr=list()
    for _ in range(n):
        arr.append(list(map(int,input())))
    buildings=list()
    for i in range(n):
        for j in range(m):
            if arr[i][j]==1:
                buildings.append((i,j))
    distance=[0]*(n+m-2)
    for i, (a, b) in enumerate(buildings,1):
        for r, c in buildings[i:]:
            dist = int(abs(a - r) + abs(b - c))
            distance[dist - 1] += 1
    print(*distance, sep=' ')