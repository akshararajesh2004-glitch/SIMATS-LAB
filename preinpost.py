class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root):
    return inorder(root.left) + root.val + inorder(root.right) if root else ""

def preorder(root):
    return root.val + preorder(root.left) + preorder(root.right) if root else ""

def postorder(root):
    return postorder(root.left) + postorder(root.right) + root.val if root else ""

# Construct the expression tree for (a+b)*c
root = Node('*')
root.left = Node('+')
root.right = Node('c')
root.left.left = Node('a')
root.left.right = Node('b')

print("Inorder traversal:", inorder(root))
print("Preorder traversal:", preorder(root))
print("Postorder traversal:", postorder(root))
