"""
Insertion Sort
"""

def insertion(arr):
    """
    Sort a given array using insertion sort
    """
    length = len(arr)
    i = 0
    end = arr[0]
    while i < length:
        if arr[i] < end:
            x = arr.pop(i)
            for j in range(0, i):
                if x < arr[j]:
                    arr.insert(j,x)
                    break
        end = arr[i]
        i += 1
    return arr

print(insertion([4, 6, 3, 9, 0]))