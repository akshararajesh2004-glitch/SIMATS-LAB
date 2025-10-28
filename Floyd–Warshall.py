n=int(input("No. of vertices: "))
g=[list(map(int,input().split())) for _ in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            g[i][j]=min(g[i][j],g[i][k]+g[k][j])
print("Shortest Paths:")
for r in g: print(*r)
