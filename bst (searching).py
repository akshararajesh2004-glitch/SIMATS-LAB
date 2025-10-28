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

def search(root, key):
    if root is None:
        return False
    if key == root.k:
        return True
    elif key < root.k:
        return search(root.l, key)
    else:
        return search(root.r, key)

# Sample usage
root = None
for val in [50, 30, 70, 20, 40, 60, 80]:
    root = ins(root, val)

key_to_search = 40
print(f"Search {key_to_search}:", "Found" if search(root, key_to_search) else "Not Found")

key_to_search = 90
print(f"Search {key_to_search}:", "Found" if search(root, key_to_search) else "Not Found")
