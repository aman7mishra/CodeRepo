"""
Merge sort
"""
import math

def merge(left, right):
    result = []
    index_l = 0
    index_r = 0
    while index_l < len(left) and index_r < len(right):
        if left[index_l] < right[index_r]:
            result.append(left[index_l])
            index_l += 1
        else:
            result.append(right[index_r])
            index_r += 1
    return result + left[index_l:] + right[index_r:]

def merge_sort(arr):
    """
    Sort an array using merge sort
    """
    if len(arr) == 1:
        return arr
    mid = math.ceil(len(arr)/2)
    left = arr[:mid]
    right = arr[mid:]
    return merge(merge_sort(left), merge_sort(right))

print(merge_sort([1, 6, 2, 8]))