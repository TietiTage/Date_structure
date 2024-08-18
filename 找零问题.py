# 面额兑换,如果手上有一定数量的零钱,该如何兑换使得换到手的货币的总数量最少

import numpy as np


def change(amount: int):
    denominations_list = [1, 5, 10, 20, 50, 100]  # 面额列表
    change_matrix = np.zeros((amount + 1, len(denominations_list)))  # 更新矩阵大小
    total = [float('inf')] * (amount + 1)
    total[0] = 0  # 初始化0金额所需的硬币数量为0

    for amounts in range(1, amount + 1):
        for _change in [_ for _ in denominations_list if _ <= amounts]:
            if total[amounts - _change] + 1 < total[amounts]:
                total[amounts] = total[amounts - _change] + 1
                # 将找零的规模减小后的已知最优解赋值给当前的找零问题
                change_matrix[amounts] = change_matrix[amounts - _change]
                change_matrix[amounts][denominations_list.index(_change)] += 1

    return change_matrix, total[amount]


if __name__ == '__main__':
    change_matrix, total = change(26)
    print(total)
    print(change_matrix)

