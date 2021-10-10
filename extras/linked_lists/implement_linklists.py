"""
Implement singly linked list
"""


class Node():
    def __init__(self, data, next_address=None) -> None:
        self.data = data
        self.next = next_address


class SingleLinkedList():
    def __init__(self) -> None:
        self._root = None
    
    def prepend(self, value):
        """
        Adds an element at the begining
        """
        if self._root is None:
            node_obj = Node(value)
            self._root = node_obj
        else:
            node_obj = Node(value, self._root)
            self._root = node_obj
    

    def append(self, value):
        """
        Iterates to the last element and returns the node
        """
        index = self._root
        while True:
            if index.next is None:
                break
            else:
                index = index.next
        node_obj = Node(value)
        index.next = node_obj

    def insert_at_an_index(self, value, index):
        """
        Inserts a value at a given index
        """
        current_index = 0
        current_node = self._root
        while True:
            if current_index == index - 1:
                break
            if current_node.next is None:
                print("IndexError")
                current_node = None
                break
            else:
                current_node = current_node.next
                current_index += 1
        if current_node is not None:
            node_obj = Node(value, current_node.next)
            current_node.next = node_obj

    def delete_at_an_index(self, index):
        """
        Deletes the value at a given index
        """
        current_index = 0
        current_node = self._root
        while True:
            if current_index == index - 1:
                break
            if current_node.next is None:
                print("IndexError")
                current_node = None
                break
            else:
                current_node = current_node.next
                current_index += 1
        if current_node is not None:
            current_node.next = current_node.next.next

    def delete_by_value(self, value):
        """
        Delete a given value from the list
        """
        prev_node = None
        current_node = self._root
        while True:
            if current_node.next is None:
                break
            else:
                prev_node = current_node
                current_node = prev_node.next
                if current_node.data == value:
                    prev_node.next = current_node.next
                    break

    def display(self):
        """
        Print all values in the list in the order
        """
        index = self._root
        while True:
            print(index.data)
            if index.next is None:
                break
            else:
                index = index.next

sll = SingleLinkedList()
sll.prepend(1)
sll.prepend(2)
sll.prepend(3)
sll.display()
print()
sll.append(4)
sll.display()
print()
sll.insert_at_an_index(7, 2)
sll.display()
print()
sll.delete_at_an_index(2)
sll.display()
print()

sll.delete_by_value(1)
sll.display()
print()
