"""
Implement array from scratch
"""

class ImpArray():
    def __init__(self):
        self.length = 0
        self.data = {}
    
    def display(self):
        """
        Print the array to the STDOUT
        """
        print("Array", self.data)
        print("Length of the array", self.length)

    def push(self, value):
        """
        Append a value to the array
        """
        self.data[self.length] = value
        self.length += 1
    
    def pop(self):
        """
        Remove the last element of the array
        Returns None when the array is empty
        """
        if self.length == 0:
            return None
        else:
            returns_value = self.data.pop(self.length-1)
            self.length -= 1
            return returns_value
    
    def delete(self, index):
        """
        Removes the element at the passed index
        Returns None in case of KeyError
        """
        try:
            return_value = self.data.pop(index)
        except KeyError:
            return_value = None
        self.move_indexes(index)
        self.length -= 1 
        self.data.pop(self.length)
        return return_value

    def move_indexes(self, index):
        """
        After deletion of a value, the keys following
        the deleted key must be moved ahead by one.
        The index is then reduced by one.
        """
        for later_index in range(index+1, self.length):
            self.data[later_index-1] = self.data[later_index]

obj = ImpArray()
obj.display()
obj.push(1)
obj.display()
obj.push(2)
obj.push(3)
obj.push(4)
obj.display()
obj.delete(1)
obj.display()
obj.pop()
obj.display()