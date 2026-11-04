
import random
import time

from sorts import merge_sort, quick_sort


def measure(sort_function, arr):
    arr = arr[:]
    start = time.time()
    sort_function(arr)
    return round(time.time() - start, 3)


print("--- random data ---")
for n in [1000, 10000, 100000, 1000000]:
    arr = [random.randint(0, 1000000) for _ in range(n)]
    print("n =", n, " merge:", measure(merge_sort, arr), "s  quick:", measure(quick_sort, arr), "s")

print("--- sorted data ---")
for n in [1000, 2000, 4000]:
    arr = list(range(n))
    print("n =", n, " merge:", measure(merge_sort, arr), "s  quick:", measure(quick_sort, arr), "s")

print("--- reversed data ---")
for n in [1000, 2000, 4000]:
    arr = list(range(n, 0, -1))
    print("n =", n, " merge:", measure(merge_sort, arr), "s  quick:", measure(quick_sort, arr), "s")
