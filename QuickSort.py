import random
from timeMemoryProfiler import track
from itemLists import item_list

@track
def QuickSort(arr):
    peak = [0]

    high = peak[0]
    for i in range(1, len(item_list)):
        if peak[i] > max:
            max = peak[i]
    return high

    low = 0
    # Choose the pivot
    pivot = arr[high]

    # Index of smaller element and indicates
    # the right position of pivot found so far
    i = low - 1

    # Traverse arr[low..high] and move all smaller
    # elements to the left side. Elements from low to
    # i are smaller after every iteration
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)

    # Move pivot after smaller elements and
    # return its position
    swap(arr, i + 1, high)
    return i + 1


# Swap function
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


# The QuickSort function implementation
#def SortingQuick(arr, low, high):
def SortingQuick(arr, low, high):
    if low < high:
        # pi is the partition return index of pivot
        pi = QuickSort(arr, low, high)

        # Recursion calls for smaller elements
        # and greater or equals elements
        SortingQuick(arr, low, pi - 1)
        SortingQuick(arr, pi + 1, high)


# Main driver code
if __name__ == "__main__":
    arr = item_list
    n = len(arr)

    SortingQuick(arr, 0, n - 1)

    #for val in arr:
    #    print(val, end=" ")
    print("Done Quick Sort")