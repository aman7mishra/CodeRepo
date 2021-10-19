"""
Implement Binary search tree
"""

class Node():
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right

class BST():
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = Node(value)
        else:
            current_node = self.root
            while True:
                if value < current_node.data:
                    if not current_node.left:
                        current_node.left = new_node
                        return
                    current_node = current_node.left

                elif value > current_node.data:
                    if not current_node.right:
                        current_node.right = new_node
                        return
                    current_node = current_node.right
    
    def lookup(self,data):
        curr_node = self.root
        while True:
            if curr_node == None:
                print("False")
                return
            if curr_node.data == data:
                print("True")
                return
            elif data < curr_node.data:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right

    def print_tree(self):
        if self.root != None:
            self.printt(self.root)
 
    def printt(self,curr_node):
        if curr_node != None:
            self.printt(curr_node.left)
            print(str(curr_node.data))
            self.printt(curr_node.right)

obj = BST()
obj.insert(3)
obj.insert(1)
obj.insert(100)
obj.print_tree()
obj.lookup(5)
obj.lookup(1)

