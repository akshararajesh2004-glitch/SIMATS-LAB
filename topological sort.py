from collections import defaultdict
g=defaultdict(list)
n=int(input("No. of edges: "))
for _ in range(n):
    u,v=input("Edge (u v): ").split(); g[u].append(v)
vis=set(); st=[]
def dfs(v):
    vis.add(v)
    for i in g[v]:
        if i not in vis: dfs(i)
    st.append(v)
for v in list(g):
    if v not in vis: dfs(v)
print("Topological Order:",st[::-1])
