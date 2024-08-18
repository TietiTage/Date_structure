# 归并排序的算法
def merge(left_list, right_list):
    # 输入的必须为已经排好序的两个子列表
    result = []  # 初始化一个空的用于存储数据的列表
    i = j = 0 # 分别为左右列表的索引
    while i < len(left_list) and j < len(right_list):
        if left_list[i] < right_list[j]:
            result.append(left_list[i])
            i += 1
        else:
            result.append(right_list[j])
            j += 1
    # 将两个列表当中剩余的元素加入结果,两个列表必定有一个为空
    result.extend(right_list[j:])
    result.extend(left_list[i:])
    return result


def merge_sorted(_list):
    # 基本结束条件:只剩下不大于一个元素的列表
    if len(_list) <= 1:
        return _list
    # 将列表分裂为两半
    mid = len(_list) // 2
    left = _list[:mid]
    right = _list[mid:]
    # 递归调用自身,进行排序
    left_sorted = merge_sorted(left)
    right_sorted = merge_sorted(right)
    return merge(left_sorted, right_sorted)




if __name__ == '__main__':
    print(merge_sorted([1, 6, 8, 8, 8, 9, 74, 51, 145, 455, 14, 111, 12]))
