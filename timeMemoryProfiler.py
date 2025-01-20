import time, os, psutil
from psutil._common import bytes2human
# instead of using fx memory_profiler which is build using psutil,
# we use psutil in order to make a single function which both tracks time spent and memory usage.

def get_process_memory():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss    # rss stands for resident set size
                                        # and is the nonswapped physical memory that a task has used

def elapsed_since(start):
    return time.strftime('%H:%M:%S', time.gmtime(time.time() - start))
# strftime is a structure format. Here: %H:%M:%S which is hours, minutes and seconds
# returns a string with the elapsed time since start.

def track(func):
    def main(*args, **kwargs):
        mem_before = get_process_memory()
        start = time.time()
        result = func(*args, **kwargs)
        mem_after = get_process_memory()
        time_elapsed = elapsed_since(start)
        mem_after = get_process_memory()
        print(f"{func.__name__}: memory before: {bytes2human(mem_before)}, memory after: {bytes2human(mem_after)}, consumed: {bytes2human(mem_after - mem_before)}, execution time: {time_elapsed}")
        return result
    return main

# Credit for some of it (code tutorial): github.com/saife245
