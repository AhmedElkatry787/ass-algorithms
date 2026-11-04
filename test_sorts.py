import random

from sorts import merge_sort, quick_sort

tests = [
    [],
    [1],
    [2, 1],
    [5, 5, 5, 5],
    [3, 1, 2, 3, 1],
    [1, 2, 3, 4, 5, 6],
    [6, 5, 4, 3, 2, 1],
]
for _ in range(100):
    tests.append([random.randint(-100, 100) for _ in range(random.randint(0, 100))])

for t in tests:
    assert merge_sort(t[:]) == sorted(t), t
    assert quick_sort(t[:]) == sorted(t), t

print("all tests passed")
