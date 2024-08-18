def quicksort(arr, low, high):
    if low < high:
        # pi 是分区索引, arr[pi] 是排序后的正确位置
        pi = partition(arr, low, high)
        # 递归地对分区进行排序
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # 选择最右边的元素作为基准
    i = low - 1  # 较小元素的索引
    for j in range(low, high):
        # 如果当前元素小于或等于基准
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # 交换,将比自己小的元素都丢在身后
    # 交换基准到正确的位置
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

if __name__ == '__main__':
    arr = [3, 6, 8, 10, 1, 2, 1]
    quicksort(arr, 0, len(arr) - 1)
    print(arr)
