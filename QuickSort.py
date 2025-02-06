import random
from timeMemoryProfiler import track
from itemLists import item_list

# Helper function to swap elements in the array
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# Partition function to partition the array and return the pivot index
def partition(arr, low, high):
    # Choose the pivot (we'll use the last element as the pivot)
    pivot = arr[high]
    i = low - 1  # Index of smaller element

    # Traverse the array and rearrange elements based on the pivot
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)

    # Move pivot element to its correct position
    swap(arr, i + 1, high)
    return i + 1  # Return the pivot index

# The main QuickSort function that applies the partitioning logic recursively
def QuickSort(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pi = partition(arr, low, high)

        # Recursively sort the subarrays before and after the pivot
        QuickSort(arr, low, pi - 1)  # Elements before pivot
        QuickSort(arr, pi + 1, high)  # Elements after pivot

# Wrapper function to allow benchmarking with just the array
@track  # Apply @track only here, to the wrapper function
def SortingQuick(arr):
    QuickSort(arr, 0, len(arr) - 1)  # Pass the whole array from 0 to len(arr)-1

from QuickSort import SortingQuick

arr = [random.randint(0, 10000) for _ in range(10000)]  # Test array

SortingQuick(arr)  # This should print memory and time stats just once
