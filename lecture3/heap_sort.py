

comparisons = 0


def heapify(arr, n, i):
    global comparisons
    while True:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n:
            comparisons += 1
            if arr[left] > arr[largest]:
                largest = left
        if right < n:
            comparisons += 1
            if arr[right] > arr[largest]:
                largest = right
        if largest == i:
            break
        arr[i], arr[largest] = arr[largest], arr[i]
        i = largest


def build_max_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    return arr


def heap_sort(arr):
    build_max_heap(arr)
    for end in range(len(arr) - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        heapify(arr, end, 0)
    return arr


def heap_insert(arr, value):
    arr.append(value)
    i = len(arr) - 1
    while i > 0 and arr[(i - 1) // 2] < arr[i]:
        parent = (i - 1) // 2
        arr[i], arr[parent] = arr[parent], arr[i]
        i = parent
    return arr


if __name__ == "__main__":
   
    print("build max heap:", build_max_heap([3, 9, 2, 1, 4, 5]))

    
    a = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    for step in range(1, 3):
        end = len(a) - step
        a[0], a[end] = a[end], a[0]
        heapify(a, end, 0)
        print("after iteration", step, ":", a)

   
    print("insert 15:", heap_insert([16, 14, 10, 8, 7, 9, 3], 15))
