import random

from heap_sort import build_max_heap, heap_insert, heap_sort

tests = [
    [],
    [1],
    [2, 1],
    [4, 4, 4, 4],
    [3, 1, 2, 3, 1],
    [1, 2, 3, 4, 5, 6],
    [6, 5, 4, 3, 2, 1],
]
for _ in range(100):
    tests.append([random.randint(-100, 100) for _ in range(random.randint(0, 100))])

for t in tests:
    assert heap_sort(t[:]) == sorted(t), t


assert build_max_heap([3, 9, 2, 1, 4, 5]) == [9, 4, 5, 1, 3, 2]
assert heap_insert([16, 14, 10, 8, 7, 9, 3], 15) == [16, 15, 10, 14, 7, 9, 3, 8]

print("all tests passed")
