t=[]
while True:
    c=input("1-Insert 2-Show 3-Exit: ")
    if c=='1': t.append((int(input("Val: ")), 'R' if len(t)%2 else 'B'))
    elif c=='2': print(t)
    else: break