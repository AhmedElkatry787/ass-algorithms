import sys

sys.setrecursionlimit(20000)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def partition(arr, p, r):
    x = arr[r]  
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


def quick_sort(arr, p=0, r=None):
    if r is None:
        r = len(arr) - 1
    if p < r:
        q = partition(arr, p, r)
        quick_sort(arr, p, q - 1)
        quick_sort(arr, q + 1, r)
    return arr


if __name__ == "__main__":
    print(merge_sort([6, 5, 3, 1, 8, 7, 2, 4]))
    print(quick_sort([2, 8, 7, 1, 3, 5, 6, 4]))


    a = [3, 8, 2, 5, 1, 4, 7, 6]
    q = partition(a, 0, len(a) - 1)
    print("partition:", a, "q =", q + 1)
