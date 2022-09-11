# Binary Tree Class
class Node:
    def __init__(self, val):
        self.key = val
        self.right = None
        self.left = None


# Inserting Node in Binary Search Tree
def insert(root, val):
    if root is None:
        return Node(val)
    elif root.key < val:
        root.right = insert(root.right, val)
    elif root.key > val:
        root.left = insert(root.left, val)
    return root


# Inorder Traversal
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.key)
    inorder(root.right)


# Searching Nodes in a Tree
def search(root, key):
    if root is None:
        return False
    if root.key == key:
        return True
    if root.key < key:
        return search(root.right, key)
    else:
        return search(root.left, key)


# Get Minimum value of Right tree (Left most leaf node of the right node from current node to be deleted)
def getRightMin(root):
    temp = root
    while temp.left is not None:
        temp = temp.left
    return temp.key


# Deleting a Node in a Tree
def removeNode(root, val):
    if root is None:
        return None
    if root.key < val:
        root.right = removeNode(root.right, val)
    elif root.key > val:
        root.left = removeNode(root.left, val)
    else:
        if root.left is None and root.right is None:
            return None
        elif root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            rightMin = getRightMin(root.right)
            root.key = rightMin
            root.right = removeNode(root.right, rightMin)  # Remove the right most leaf node by taking current root as new node.right and val = rightMin value
    return root


# Calling functions to check outputs
root = None
root = insert(root, 100)
root = insert(root, 50)
root = insert(root, 150)
root = insert(root, 175)
inorder(root)
print(search(root, 50))
print(search(root, 70))
removeNode(root, 100)
print(search(root, 100))
