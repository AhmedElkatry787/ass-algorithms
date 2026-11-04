

import random
import time

from insertion_sort import insertion_sort

sizes = [100, 500, 1000, 2000, 3000, 4000, 5000]

print("n      input      comparisons   shifts      time (ms)")
for n in sizes:
    inputs = {
        "sorted": list(range(n)),
        "reversed": list(range(n, 0, -1)),
        "random": [random.randint(0, 10000) for _ in range(n)],
    }
    for name in inputs:
        arr = inputs[name][:]
        start = time.time()
        c, s = insertion_sort(arr)
        end = time.time()
        assert arr == sorted(inputs[name])
        print(n, "\t", name, "\t", c, "\t", s, "\t", round((end - start) * 1000, 2))
    print()
