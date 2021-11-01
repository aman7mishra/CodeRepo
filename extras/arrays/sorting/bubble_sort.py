"""
implement bubble sort
"""

def bubble(arr):
    """
    Sorts an array using bubble sort
    """
    for index_i, _ in enumerate(arr):
        for index_j, _ in enumerate(arr):
            if arr[index_j] > arr[index_i]:
                temp = arr[index_i]
                arr[index_i] = arr[index_j]
                arr[index_j] = temp
    return arr

print(bubble([0, 3, 5, 8, 2, 1, 0]))