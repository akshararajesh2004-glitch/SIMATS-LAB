import heapq
n=list(map(int,input("Enter numbers: ").split()))
heapq.heapify(n)
print("Min Heap:",n)
print("Max Heap:",[-x for x in heapq.nsmallest(len(n),[-i for i in n])])
