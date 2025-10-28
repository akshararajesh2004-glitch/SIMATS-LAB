from collections import deque
g={}
n=int(input("No. of nodes: "))
for _ in range(n):
    v=input("Node: "); g[v]=input("Adj (space sep): ").split()
s=input("Start: ")
vis=set(); q=deque([s])
print("BFS:",end=" ")
while q:
    v=q.popleft()
    if v not in vis:
        print(v,end=" "); vis.add(v)
        q.extend(g[v])
print("\nGraph:",g)
