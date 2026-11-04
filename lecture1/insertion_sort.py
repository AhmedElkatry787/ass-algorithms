

def insertion_sort(arr):
    comparisons = 0
    shifts = 0
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0:
            comparisons += 1
            if arr[i] > key:
                arr[i + 1] = arr[i]
                shifts += 1
                i -= 1
            else:
                break
        arr[i + 1] = key
    return comparisons, shifts


def insertion_sort_trace(arr):
   
    print("start:", arr)
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
        print("j =", j + 1, "key =", key, "->", arr)


if __name__ == "__main__":

    print("Exercise: trace insertion sort")
    insertion_sort_trace([6, 5, 3, 1, 8, 7, 2, 4])

    print("\nNumerical problem")
    a = [4, 3, 2, 1]
    c, s = insertion_sort(a)
    print("[4, 3, 2, 1] -> comparisons =", c, "shifts =", s)

    a = [1, 2, 3, 4]
    c, s = insertion_sort(a)
    print("[1, 2, 3, 4] -> comparisons =", c, "shifts =", s)

    print("n = 3000 -> 3 times bigger -> 9 times the time -> 2 * 9 =", 2 * 9, "ms")
