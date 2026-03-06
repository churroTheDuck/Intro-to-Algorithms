import time
import random
import matplotlib.pyplot as plt

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
    def sort(self):
        sortedList = []
        if (self.left != -1):
            sortedList.extend(self.left.sort())
        sortedList.append(self.nodeValue)
        if (self.right != -1):
            sortedList.extend(self.right.sort())
        return sortedList
            
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

insert_x = []
insert_y = []

print("Insert timing:")
for n in range(10000,100000,1000):
    values = list(range(n))
    random.shuffle(values)
    root = Node(values[0])
    start = time.time()
    for v in values[1:]:
        root.insert(v)
    end = time.time()
    insert_x.append(n)
    insert_y.append(end - start)
    
findmin_x = []
findmin_y = []

print("\nfindMin timing:")
for n in range(10000,100000,1000):
    values = list(range(n))
    random.shuffle(values)
    root = Node(values[0])
    for v in values[1:]:
        root.insert(v)
    start = time.time()
    for v in values[1:]:
        root.findMin()
    end = time.time()
    findmin_x.append(n)
    findmin_y.append(end - start)
    
plt.plot(insert_x, insert_y, label="Insert")
plt.plot(findmin_x, findmin_y, label="FindMin")

plt.xlabel("Number of Nodes")
plt.ylabel("Time (seconds)")
plt.title("BST Performance")
plt.legend()

plt.show()

values = list(range(100))
random.shuffle(values)
root = Node(values[0])
for v in values[1:]:
    root.insert(v)
print(f"Sorted tree: {root.sort()}")