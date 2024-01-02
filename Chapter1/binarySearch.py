# The functiosn takes an ordered array and the item to find
def binary_Search(arr, item):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        if guess < item:
            low = mid + 1
    return None

array = [1,2,3,4,8,10,13,15,17,18,22]

print(binary_Search(array, 18))
print(binary_Search(array, 0))