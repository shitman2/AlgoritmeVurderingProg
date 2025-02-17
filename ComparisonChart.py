import matplotlib.pyplot as plt

import Benchmark
from Benchmark import *
#plt.plot([4, 6, 8, 14], [1, 5, 7, 8])

#results = Benchmark.results

plt.plot(results())
plt.ylabel('some numbers')
plt.show()




'''
def revert(arr):
    array = [0:len(arr)] = arr[::-1]

nice_storing_array = [i for i in range(1000, 0, -1)]

if __name__ == "__main__":
    times_stored_nicely = [{}, {}, {}, {}, {}]
    for i in range(100):
        print(i)
        times_stored_nicely[i][0] = times_stored_nicely[i-1][0]

    fig, ax = plt.subplots()
    ax.plot(list(times[0].keys()), list(times[0].values()), label='Bubble Sort')
    ax.plot(list(times[1].keys()), list(times[1].values()), label='Insertion Sort')
    ax.plot(list(times[2].keys()), list(times[2].values()), label='Selection Sort')
    ax.plot(list(times[3].keys()), list(times[3].values()), label='Quick Sort')
    plt.grid()
    plt.legend(['Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Quick Sort'])
    plt.xlabel('Array Size')
    plt.ylabel('Time Taken')
    plt.show() 
'''