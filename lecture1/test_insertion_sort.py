import random

from insertion_sort import insertion_sort


def check(arr):
    expected = sorted(arr)
    insertion_sort(arr)
    assert arr == expected, arr


check([])
check([5])
check([2, 1])
check([3, 3, 3, 3])
check([1, 2, 3, 4, 5])
check([5, 4, 3, 2, 1])
for _ in range(100):
    check([random.randint(-50, 50) for _ in range(random.randint(0, 50))])


assert insertion_sort([7, 3, 9, 2, 5]) == (8, 6)
assert insertion_sort([4, 3, 2, 1]) == (6, 6)
assert insertion_sort([1, 2, 3, 4]) == (3, 0)

print("all tests passed")
