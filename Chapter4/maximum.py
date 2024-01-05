def maxNumber(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    maximum = maxNumber(arr[1:])
    return arr[0] if arr[0] > maximum else maximum

print(maxNumber([2,4,1,10,2,9]))