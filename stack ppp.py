stack = []
while True:
    ch = input("Enter choice (1-PUSH,2-POP,3-PEEK,4-EXIT): ")
    if ch == '1':
        stack.append(input("Enter element: "))
    elif ch == '2':
        print("Popped:", stack.pop() if stack else "Empty")
    elif ch == '3':
        print("Top:", stack[-1] if stack else "Empty")
    elif ch == '4':
        break
