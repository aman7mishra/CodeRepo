"""
Selection sort
"""

def selection(arr):
    """
    Sorting an array using selection sort
    """
    for index_i in range(0, len(arr)):
        small = index_i
        for index_j in range(index_i+1, len(arr)):
            if arr[index_j] < arr[small]:
                small = index_j
        temp = arr[small]
        arr[small] = arr[index_i]
        arr[index_i] = temp
    return arr

print(selection([0, 0, 0, 0, 4, 1000, 5, 7, 2, 0]))