def counter(arr):
    if arr == []:
        return 0
    return 1 + counter(arr[1:])

print(counter([1,2,3,4,5]))