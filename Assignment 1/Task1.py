import random
import time

def insertion_sort(arr):
    steps = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            steps += 1
        arr[j + 1] = key
        steps += 1
    return steps

def merge(arr, left, right):
    steps = 0
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
        steps += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
        steps += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
        steps += 1

    return steps

def merge_sort(arr):
    steps = 0
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        steps += merge_sort(left)
        steps += merge_sort(right)

        steps += merge(arr, left, right)

    return steps

def heapify(arr, n, i):
    steps = 0
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left
    steps += 1

    if right < n and arr[largest] < arr[right]:
        largest = right
    steps += 1

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        steps += 1
        steps += heapify(arr, n, largest)

    return steps

def heapsort(arr):
    steps = 0
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        steps += heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        steps += 1
        steps += heapify(arr, i, 0)

    return steps

def partition(arr, low, high):
    steps = 0
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            steps += 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    steps += 1

    return i + 1, steps

def quicksort(arr, low, high):
    steps = 0
    if low < high:
        pi, steps_partition = partition(arr, low, high)
        steps += steps_partition
        steps += quicksort(arr, low, pi - 1)
        steps += quicksort(arr, pi + 1, high)
    return steps

# Varying input size and recording the number of steps
input_sizes = [10, 100, 1000, 10000]  # Example input sizes

for size in input_sizes:
    arr = random.sample(range(size), size)  # Generate a random array of given size
    start_time = time.time()

    # Uncomment the algorithm you want to test
    # steps = insertion_sort(arr)
    # steps = merge_sort(arr)
    # steps = heapsort(arr)
    # steps = quicksort(arr, 0, len(arr) - 1)

    end_time = time.time()
    execution_time = end_time - start_time

    print(f"Input size: {size}, Steps: {steps}, Execution time: {execution_time} seconds")
