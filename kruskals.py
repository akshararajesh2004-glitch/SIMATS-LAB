n=int(input("No. of edges: "))
E=[]
for _ in range(n):
    u,v,w=input("u v w: ").split();E.append((int(w),u,v))
E.sort(); p={}
def f(x): return x if p[x]==x else f(p[x])
for _,u,v in E: p[u]=u; p[v]=v
mst=[]
for w,u,v in E:
    if f(u)!=f(v):
        mst.append((u,v,w)); ru,rv=f(u),f(v)
        for k in p:
            if f(k)==rv:p[k]=ru
print("MST:",mst)
