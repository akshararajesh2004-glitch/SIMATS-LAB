class BTree:
    def __init__(s,t=2):s.t=t;s.keys=[];s.c=[];s.l=True
    def insert(s,k):
        if len(s.keys)==2*s.t-1:
            n=BTree(s.t);n.c.append(s);n.l=False;n.split(0,s);n.ins_nonfull(k);return n
        s.ins_nonfull(k);return s
    def ins_nonfull(s,k):
        if s.l:s.keys.append(k);s.keys.sort()
        else:
            i=len(s.keys)-1
            while i>=0 and k<s.keys[i]:i-=1;i+=1
            if len(s.c[i].keys)==2*s.t-1:s.split(i,s.c[i]); 
            s.c[i+(k>s.keys[i])].ins_nonfull(k)
    def split(s,i,y):
        z=BTree(y.t);z.l=y.l;z.keys=y.keys[y.t:];y.keys=y.keys[:y.t-1]
        if not y.l:z.c=y.c[y.t:];z.c=z.c[:y.t]
        s.c.insert(i+1,z);s.keys.insert(i,y.keys.pop())
    def show(s,lv=0):
        print("  "*lv,s.keys)
        for c in s.c:c.show(lv+1)

t=BTree()
while True:
    c=input("1-Insert 2-Show 3-Exit: ")
    if c=='1':t=t.insert(int(input("Val: ")))
    elif c=='2':t.show()
    else:break
