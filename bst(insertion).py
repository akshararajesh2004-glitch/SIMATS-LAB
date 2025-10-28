class Node:
    def __init__(self, key): self.key = key; self.left = self.right = None
def insert(root, k):
    if not root: return Node(k)
    if k < root.key: root.left = insert(root.left, k)
    elif k > root.key: root.right = insert(root.right, k)
    return root
def print_tree(r, s=0):
    if r:
        print_tree(r.right, s+4)
        print(' '*s + str(r.key))
        print_tree(r.left, s+4)

root = None
while (v := input("Insert node or q: ")) != 'q':
    try: root = insert(root, int(v)); print_tree(root)
    except: print("Invalid input")
