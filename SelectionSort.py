import random
from timeMemoryProfiler import track

@track
def SelectSorting(arr):
    n = len(arr)
    for i in range(n - 1):

        # Assume the current position holds
        # the minimum element
        min_idx = i

        # Iterate through the unsorted portion
        # to find the actual minimum
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                # Update min_idx if a smaller element is found
                min_idx = j

        # Move minimum element to its
        # correct position
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def PrintIt(arr):
    for val in arr:
        print(val, end=" ")
    print()


if __name__ == "__main__":
    arr = [random.randint(0,10000) for i in range(10000)]

    print("Original array: ", end="")
    PrintIt(arr)

    SelectSorting(arr)

    print("Sorted array: ", end="")
    PrintIt(arr)
    meow