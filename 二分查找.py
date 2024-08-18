def binary_search(arr: list, target):
    "arr应该从小往大排列"
    low = 0 # 初始化查找下界
    high = len(arr) - 1 # 上界
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
    print("没找到")
    return False

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(binary_search(arr, 1))