import random
from itemLists import item_list
from bubbleSort import bubble_sort
from InsertionSort import Insert
from MergeSort import MergeSort
from QuickSort import QuickSort
from SelectionSort import SelectSorting
from timeMemoryProfiler import track



algos = [bubble_sort, Insert, MergeSort, QuickSort, SelectSorting]


for item in item_list:
    for algo in algos:
        for j in range(2):
            if j == 0:
                #time
                pass

            if j == 1:
                #memory
                pass

            algo(item)
