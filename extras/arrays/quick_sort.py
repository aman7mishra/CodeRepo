numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0, 5]

def partition(arr,left,right):
    i = (left - 1)
    pivot = arr[right]
    for j in range(left, right):
        if arr[j] <= pivot:
            i = i+1
            arr[i],arr[j] = arr[j], arr[i]
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return (i+1)

def quick_sort(arr, left, right):
    if left < right:
        partition_index = partition(arr,left,right)
        quick_sort(arr,left, partition_index - 1)
        quick_sort(arr, partition_index + 1, right)


quick_sort(numbers,0,len(numbers)-1)
print(numbers)