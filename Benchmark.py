import random
import time
import tracemalloc
import matplotlib.pyplot as plt

# Importing sorting algorithms
import InsertionSort
from timeMemoryProfiler import track
from itemLists import item_list
from bubbleSort import bubble_sort
from InsertionSort import Insert
from MergeSort import MergeSort
from QuickSort import SortingQuick
from SelectionSort import SelectSorting


def benchmark_sorting(sorting_function, arr):

    arr_copy = arr.copy()
    tracemalloc.start()
    start_time = time.time()
    sorting_function(arr_copy)
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return {
        "name": sorting_function.__name__,
        "time": end_time - start_time,
        "memory": peak / 1024  # Convert to KB
    }


if __name__ == "__main__":
    arr = [random.randint(0, 10000) for _ in range(10000)]

    # List of sorting algorithms to benchmark
    sorting_algorithms = [
        InsertionSort.Insert,  # Insertion Sort
        MergeSort,              # Merge Sort
        SortingQuick,           # Quick Sort
        SelectSorting,          # Selection Sort
        bubble_sort,            # Bubble Sort
    ]


    results = [benchmark_sorting(sort_func, arr) for sort_func in sorting_algorithms]

    # Sort the results by time first, then memory usage
    results.sort(key=lambda x: (x["time"], x["memory"]))

    # Print the results
    print("Sorting Algorithm Performance:")
    for result in results:
        print(f"{result['name']}: Time = {result['time']:.4f} sec, Memory = {result['memory']:.2f} KB")
        plt.plot()
        plt.ylabel('some numbers')
        plt.show()
