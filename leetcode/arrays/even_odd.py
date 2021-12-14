def even_odd(arr):
    i = 0
    j = len(arr) - 1
    while i < j:
        if arr[i] % 2 == 0:
            i += 1
        else:
            swap(arr, i, j)
            j -= 1
    return arr

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


print(even_odd([2,3,7,9,8,10]))