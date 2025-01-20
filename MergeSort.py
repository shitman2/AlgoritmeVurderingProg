import random
from timeMemoryProfiler import track
from itemLists import item_list

@track
#def MergeSort(arr, left, mid, right):
def MergeSort(arr):

    mid = len(item_list) // 2
    left = mid - 1
    right = mid + 1

    n1 = mid - left + 1
    n2 = right - mid

    # Create temp arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = left  # Initial index of merged subarray

    # Merge the temp arrays back
    # into arr[left..right]
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[],
    # if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[],
    # if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def sorting(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        sorting(arr, left, mid)
        sorting(arr, mid + 1, right)
        MergeSort(arr, left, mid, right)

def print_list(arr):
    for i in arr:
        print(i, end=" ")
    print()

# Driver code
if __name__ == "__main__":
    arr = item_list


    sorting(arr, 0, len(arr) - 1)
