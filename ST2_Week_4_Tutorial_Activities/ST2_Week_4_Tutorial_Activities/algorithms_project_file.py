import random
import timeit

# ============================
# SEARCHING ALGORITHMS
# ============================

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# ============================
# SORTING ALGORITHMS
# ============================

def insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


# ============================
# COMBINED ALGORITHMS
# ============================

def insertion_linear(arr, target):
    sorted_arr = insertion_sort(arr)
    return linear_search(sorted_arr, target)


def bubble_linear(arr, target):
    sorted_arr = bubble_sort(arr)
    return linear_search(sorted_arr, target)


def insertion_binary(arr, target):
    sorted_arr = insertion_sort(arr)
    return binary_search(sorted_arr, target)


def bubble_binary(arr, target):
    sorted_arr = bubble_sort(arr)
    return binary_search(sorted_arr, target)


# ============================
# BENCHMARKING
# ============================

def benchmark():
    sizes = [1000, 3000, 5000]

    for size in sizes:
        print(f"\n==============================")
        print(f"      DATA SIZE = {size}")
        print(f"==============================")

        arr = [random.randint(1, 10000) for _ in range(size)]
        target = random.choice(arr)

        # 1. Insertion Sort + Linear Search
        t1 = timeit.timeit(lambda: insertion_linear(arr, target), number=1)

        # 2. Bubble Sort + Linear Search
        t2 = timeit.timeit(lambda: bubble_linear(arr, target), number=1)

        # 3. Insertion Sort + Binary Search
        t3 = timeit.timeit(lambda: insertion_binary(arr, target), number=1)

        # 4. Bubble Sort + Binary Search
        t4 = timeit.timeit(lambda: bubble_binary(arr, target), number=1)

        print(f"Insertion Sort + Linear Search: {t1:.6f} sec")
        print(f"Bubble Sort + Linear Search:    {t2:.6f} sec")
        print(f"Insertion Sort + Binary Search: {t3:.6f} sec")
        print(f"Bubble Sort + Binary Search:    {t4:.6f} sec")


# Run benchmarks
benchmark()