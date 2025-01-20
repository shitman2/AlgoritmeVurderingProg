import random
from timeMemoryProfiler import track
from itemLists import item_list

arr = item_list
# Use decorator (@) to use the imported function on the algo
@track
def bubble_sort(arr):
    for i in range(len(arr)):
        already_sorted = True
        for j in range(len(arr) -i -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                already_sorted = False
        if already_sorted:
            break
    return arr



if __name__ == "__main__":
    arr = items
