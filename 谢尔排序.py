# 谢尔排序
import numpy as np
def shell_sort(_list: list) -> list:
    gap = len(_list) // 2  # 初始的切片间隔设为列表的长度//2

    while gap > 0:
        for i in range(gap, len(_list)):
            current_value = _list[i]
            # 插入排序
            j = i
            while j >= gap and _list[j - gap] > current_value: # 依次检查间隔为gap的元素
                _list[j] = _list[j - gap] # 变更顺序
                j -= gap # 切换到下一个间隔为gap的元素,进行比较
            _list[j] = current_value
        # 缩小间隔
        gap //= 2

    return _list


if __name__ == '__main__':
    print(shell_sort([4, 7, 48, 754, 74854, 41, 44, 8, 84, 85, 444, 4562]))
