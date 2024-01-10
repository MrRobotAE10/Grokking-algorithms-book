# Run time: Worst Case O(n^2), Average Case O(n log n)
def quicksort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([2,5,1,23,5,2,190,2]))

