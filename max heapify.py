def max_heapify(arr, i, heapsize):
    left = i * 2 + 1
    right = i * 2 + 2
    n = heapsize

    if left < n and arr[left] > arr[i]:
        max = left
    else:
        max = i
    if right < n and arr[right] > arr[max]:
        max = right
    if i != max:
        arr[i], arr[max] = arr[max], arr[i]
        max_heapify(arr, max, n)


def min_heapify(arr, i, heapsize):
    left = i * 2 + 1
    right = i * 2 + 2
    n = heapsize
    if left < n and arr[left] < arr[i]:
        min = left
    else:
        min = i
    if right < n and arr[right] < arr[min]:
        min = right
    if i != min:
        arr[i], arr[min] = arr[min], arr[i]
        min_heapify(arr, min, n)


def delete_max(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr.pop()
    else:
        max = arr[0]
        arr[0] = arr.pop()
        max_heapify(arr, 0, len(arr))
        return max


def delete_min(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr.pop(0)
    else:
        min = arr[0]
        arr[0] = arr.pop()
        min_heapify(arr, 0, len(arr))
        return min


def heapsort(arr):
    build_maxheap(arr)
    n = len(arr)
    for i in range(n - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr, 0, i)
    return arr


def heapsort_desc(arr):
    build_minheap(arr)
    n = len(arr)
    for i in range(n - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        min_heapify(arr, 0, i)
    return arr


def build_maxheap(arr):
    for i in range((len(arr) // 2) - 1, -1, -1):
        max_heapify(arr, i, len(arr))
    return arr


def build_minheap(arr):
    for i in range((len(arr) // 2) - 1, -1, -1):
        min_heapify(arr, i, len(arr))
    return arr


def insert_node(arr, val):
    arr.append(val)
    i = len(arr) - 1

    while i > 0 and arr[(i-1)//2] < arr[i]:
        arr[i], arr[(i-1)//2] = arr[(i-1)//2], arr[i]
        i = (i-1)//2
    return arr


a = [3, 5, 2, 7, 1, 8]
print("MAXHEAP -> ", build_maxheap(a))
print("MINHEAP -> ", build_minheap(a))
print(heapsort(a))
print(heapsort_desc(a))
print(insert_node(a, 20))
print(heapsort(a))
print(heapsort_desc(a))
