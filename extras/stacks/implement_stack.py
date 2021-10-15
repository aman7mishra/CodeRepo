"""
Implementing stack using linked list
"""

class Node():
    def __init__(self, data, next_address = None) -> None:
        self.data = data
        self.next = next_address
    

class Stack():
    def __init__(self) -> None:
        self._root = None
    
    def push(self, value):
        """
        Add a value to the stack
        """
        if self._root is None:
            self._root = Node(value)
        else:
            self._root = Node(value, self._root)

    def pop(self):
        """
        Pop an element from the stack
        """
        if self._root is None:
            return None
        else:
            return_val = self._root
            self._root = self._root.next
            return return_val

    def is_empty(self):
        """
        Checks if the stack is empty
        """
        return bool(self._root)

    def display(self):
        """
        Print all elements in the stack
        """
        index = self._root
        if self.is_empty() is True:
            while True:
                print(index.data)
                if index.next is not None:
                    index = index.next
                else:
                    break
        else:
            print("stack empty")


st = Stack()
st.display()
st.push(1)
st.push(2)
st.display()
print()
st.pop()
st.display()
st.pop()
st.display()