class Node:
    def __init__(self, k):
        self.k = k
        self.l = self.r = None

def ins(root, k):
    if not root:
        return Node(k)
    if k < root.k:
        root.l = ins(root.l, k)
    elif k > root.k:
        root.r = ins(root.r, k)
    return root

def find_min(root):
    while root.l:
        root = root.l
    return root

def dele(root, k):
    if not root:
        return root
    if k < root.k:
        root.l = dele(root.l, k)
    elif k > root.k:
        root.r = dele(root.r, k)
    else:
        if not root.l:
            return root.r
        elif not root.r:
            return root.l
        minNode = find_min(root.r)
        root.k = minNode.k
        root.r = dele(root.r, minNode.k)
    return root

def inorder(root):
    return inorder(root.l) + [root.k] + inorder(root.r) if root else []

# Sample usage
root = None
for val in [50, 30, 70, 20, 40, 60, 80]:
    root = ins(root, val)

print("Inorder before deletion:", inorder(root))
root = dele(root, 50 )  
root = dele(root, 30 )# delete node with key 50
print("Inorder after deletion:", inorder(root))
