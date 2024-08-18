def insert_sort(_list: list):
    for boundary in range(1, len(_list)): # 逐步扩大已经排序的列表边界
        item_to_insert = _list[boundary] # 将需要插入的元素设为边界后面的一个元素
        i = boundary - 1 # 边界的索引
        while i >= 0 and _list[i] > item_to_insert: # 如果边界大于0,并且边界的元素比待插入的元素更小:
            _list[i + 1] = _list[i] # 将待插入的元素赋值为边界元素,相当于将边界向右边移动
            i -= 1 # 从右往左边检查元素和插入元素的大小关系,更新索引
        # 插入元素,若不需要排序,相当于没做任何操作
        _list[i + 1] = item_to_insert
    return _list

# 插入排序
if __name__ == '__main__':
    my_list = [1, 6, 44, 2, 8, 9, 7, 1, 2, 5, 3, 45, 84, 55]
    print(insert_sort(my_list))
