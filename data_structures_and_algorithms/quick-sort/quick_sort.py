def partition(arr: list, start: int, end: int) -> int:
    pivot = arr[end]
    partition_index = start

    for i in range(start, end):
        if arr[i] <= pivot:
            arr[i], arr[partition_index] = arr[partition_index], arr[i]
            partition_index += 1

    arr[partition_index], arr[end] = arr[end], arr[partition_index]

    return partition_index

def quick_sort(arr: list, start: int, end: int):
    if start < end:
        partition_index = partition(arr, start, end)
        quick_sort(arr, start, partition_index-1)
        quick_sort(arr, partition_index+1, end)


l = [7,2,1,6,8,5,3,4]
quick_sort(l, 0, len(l) - 1)
print(l)
