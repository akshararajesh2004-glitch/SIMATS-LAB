import heapq
g={}
n=int(input("No. of edges: "))
for _ in range(n):
    u,v,w=input("u v w: ").split(); w=int(w)
    g.setdefault(u,[]).append((v,w))
s=input("Start: ")
d={x:1e9 for x in g}; d[s]=0
pq=[(0,s)]
while pq:
    du,u=heapq.heappop(pq)
    if du>d[u]: continue
    for v,w in g[u]:
        if d[v]>du+w:
            d[v]=du+w; heapq.heappush(pq,(d[v],v))
print("Shortest Distances:",d)
