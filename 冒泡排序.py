# 冒泡排序
def bubble_sort(_list: list) -> list:
    sup = len(_list) - 1  # 初始上界设定为列表的长度减去1
    while sup > 1:
        swapped = False # 标记是否发生了交换
        for index in range(sup):
            # 比较前后两个元素的大小
            if _list[index] > _list[index + 1]:
                _list[index], _list[index + 1] = _list[index + 1], _list[index]
                swapped = True
        if not swapped:
            break
        sup -= 1  # 上界减去1
    return _list


if __name__ == '__main__':
    _list = [1, 6, 1, 8, 7, 9, 5, 4, 3, 7, 8, 2, 1]
    print(bubble_sort(_list))
