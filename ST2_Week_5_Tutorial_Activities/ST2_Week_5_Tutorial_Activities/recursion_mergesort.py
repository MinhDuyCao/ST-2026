import random
import timeit

# ============================
# INSERTION SORT (Inefficient)
# ============================

def insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and current < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current
    return arr


# ============================
# MERGE SORT (Efficient)
# ============================

def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


# ============================
# TEST DATA (Same for both)
# ============================

data_sizes = [100, 500, 1000, 2000]

for size in data_sizes:
    print(f"\n==============================")
    print(f"   TESTING DATA SIZE = {size}")
    print(f"==============================")

    test_data = [random.randint(1, 10000) for _ in range(size)]

    # Benchmark Insertion Sort
    insertion_time = timeit.timeit(
        lambda: insertion_sort(test_data),
        number=1
    )

    # Benchmark Merge Sort
    merge_time = timeit.timeit(
        lambda: merge_sort(test_data),
        number=1
    )

    print(f"Insertion Sort Time: {insertion_time:.6f} seconds")
    print(f"Merge Sort Time:     {merge_time:.6f} seconds")





