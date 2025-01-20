import random
from timeMemoryProfiler import track

@track
# Function to sort array using insertion sort
def Insert(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# A utility function to print array of size n
def ArrayPrint(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

# Driver method
if __name__ == "__main__":
    arr = [random.randint(0,10000) for i in range(10000)]
    Insert(arr)
    #ArrayPrint(arr)

    # This code is contributed by Hritik Shah.