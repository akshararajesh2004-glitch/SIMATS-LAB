import heapq
g={}
n=int(input("No. of edges: "))
for _ in range(n):
    u,v,w=input("u v w: ").split();w=int(w)
    g.setdefault(u,[]).append((w,v));g.setdefault(v,[]).append((w,u))
s=input("Start: ")
vis=set([s]); pq=g[s]; heapq.heapify(pq); mst=[]
while pq:
    w,v=heapq.heappop(pq)
    if v not in vis:
        vis.add(v); mst.append((w,v))
        for e in g[v]: 
            if e[1] not in vis: heapq.heappush(pq,e)
print("MST Edges:",mst)
