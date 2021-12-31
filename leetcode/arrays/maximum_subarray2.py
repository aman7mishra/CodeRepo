arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

maxi = arr[0]

for i in range(1, len(arr)-1):
    arr[i] = max(arr[i], arr[i]+arr[i-1])
    maxi = max(maxi, arr[i])

print(maxi)
