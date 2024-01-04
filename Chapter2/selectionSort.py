# Find the smallest number and add it to a new array or to the beginning, to sort it
# Running time O(n^2)

def findSmallest(array):
    smallestNumber = array[0] # Stores the smallest number
    smallestIndex = 0 # Stores the smallest number index
    for i in range(1, len(array)):
        if array[i] < smallestNumber:
            smallestNumber = array[i]
            smallestIndex = i
    return smallestIndex

def selectionSort(array):
    sortedArray = []
    for i in range(len(array)):
        smallest = findSmallest(array)
        sortedArray.append(array.pop(smallest))
    return sortedArray

print(selectionSort([20, 1, 3, 12, 5, 4]))
