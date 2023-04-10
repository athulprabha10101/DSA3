def max_hapify(arr, i):
    left = i*2 + 1
    right = i*2 + 2
    n = len(arr)
    if left < n and arr[left] > arr[i]:
        max = left
    else: max = i
    if right < n and arr[right] > arr[max]:
        max = right
    if i != max:
        arr[i], arr[max] = arr[max], arr[i]
        max_hapify(arr, max)

def min_hapify(arr, i):
    left = i*2 + 1
    right = i*2 + 2
    n = len(arr)
    if left < n and arr[left] < arr[i]:
        min = left
    else: max = i
    if right < n and arr[right] < arr[min]:
        min = right
    if i != min:
        arr[i], arr[min] = arr[min], arr[i]
        max_hapify(arr, min)

def build_maxheap(arr):
    for i in range((len(arr)//2)-1, -1, -1):
        max_hapify(arr, i)