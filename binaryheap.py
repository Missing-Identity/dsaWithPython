# Function to build binary heap
def build_heap(arr, size):
    i = int(size / 2)
    while i <= 0:
        heapify(arr, i, size)
        i -= 1


# Function to ensure Max Heap
def heapify(arr, index, size):
    left = 2 * index + 1
    right = left + 1
    max = index
    if left <= size and arr[left] > arr[max]:
        max = left
    if right <= size and arr[right] > arr[max]:
        max = right
    if index is not max:
        temp = arr[max]
        arr[max] = arr[index]
        arr[index] = temp
        heapify(arr, max, size)


# Function to delete maximum element from heap
def delete_max(arr, size):
    arr[0], arr[size] = arr[size], arr[0]
    print("Max = ", arr[size])
    arr.pop()
    heapify(arr, 0, size)


a = [12, 34, 31, 51, 11, 68, 96, 43, 56]
build_heap(a, 8)
delete_max(a, 8)
