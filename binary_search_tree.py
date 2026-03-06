import time
import random

class Node:
    def __init__(self, nodeValue, left = -1, right = -1):
        self.balanceFactor = 0
        self.nodeValue = nodeValue
        self.left = left
        self.right = right
    def insert(self, value):
        if value < self.nodeValue:
            self.balanceFactor -= 1
            if (self.left != -1):
                self.left.insert(value)
            else:
                self.left = Node(value)
        else:
            self.balanceFactor += 1
            if (self.right != -1):
                self.right.insert(value)
            else:
                self.right = Node(value)
    def findMin(self):
        if (self.left != -1):
            return self.left.findMin()
        else:
            return self.nodeValue
# the following code was by AI, not by me

def print_tree(node, prefix="", is_left=True):
    if node == -1:
        return
    print(prefix + ("├── " if is_left else "└── ") + str(node.nodeValue) + ("(") + str(node.balanceFactor) + (")"))
    if node.left != -1 or node.right != -1:
        if node.left != -1:
            print_tree(node.left, prefix + ("│   " if is_left else "    "), True)
        else:
            print(prefix + ("│   " if is_left else "    ") + "├── None")
        if node.right != -1:
            print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
        else:
            print(prefix + ("│   " if is_left else "    ") + "└── None")

def print_bst(root):
    if root == -1:
        print("Empty tree")
        return
    print(str(root.nodeValue) + ("(") + str(root.balanceFactor) + (")"))
    if root.left != -1 or root.right != -1:
        if root.left != -1:
            print_tree(root.left, "", True)
        else:
            print("├── None")
        if root.right != -1:
            print_tree(root.right, "", False)
        else:
            print("└── None")
            
# end AI code section

sizes = [50000, 100000, 150000, 200000, 250000]
import time
import random


print("Insert timing:")
for n in sizes:
    values = list(range(n))
    random.shuffle(values)
    root = Node(values[0])
    start = time.time()
    for v in values[1:]:
        root.insert(v)
    end = time.time()
    print(f"n = {n}, time = {end - start} seconds")
    
print("\nfindMin timing:")
for n in sizes:
    values = list(range(n))
    random.shuffle(values)
    root = Node(values[0])
    for v in values[1:]:
        root.insert(v)
    start = time.time()
    for v in values[1:]:
        root.findMin()
    end = time.time()
    print(f"n = {n}, time = {end - start} seconds")