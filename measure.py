

import math
import random
import sys
import time


import heap_sort
from sorts import merge_sort, quick_sort


def measure(sort_function, arr):
    arr = arr[:]
    start = time.time()
    sort_function(arr)
    return round(time.time() - start, 3)


for n in [1000, 10000, 100000, 1000000]:
    arr = [random.randint(0, 1000000) for _ in range(n)]

    heap_sort.comparisons = 0
    t_heap = measure(heap_sort.heap_sort, arr)
    comps = heap_sort.comparisons

    t_merge = measure(merge_sort, arr)
    t_quick = measure(quick_sort, arr)

    print("n =", n)
    print("  heap:", t_heap, "s  merge:", t_merge, "s  quick:", t_quick, "s")
    print("  heap sort comparisons:", comps, " n log2 n:", round(n * math.log2(n)))
