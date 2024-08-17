import numpy as np

def dp_make_change(coinValueList, change, mincoinList):
    counterList = np.zeros((len(coinValueList), change+1))  # 创建二维列表，行表示面值，列表示金额
    # 从1分钱到最大金额逐步计算所需的最小硬币数量
    for cents in range(1, change+1):
        coin_count = cents  # 初始化最大值（最差情况就是全用硬币）
        new_coin = 1  # 使用的硬币,初始为一块钱
        # 对每个面值的硬币，计算最小硬币数, 并将计算出来的硬币币值与数量加入矩阵
        for j in [c for c in coinValueList if c <= cents]:
            if mincoinList[cents - j] + 1 < coin_count:
                coin_count = mincoinList[cents - j] + 1
                new_coin = j # 更新所需的硬币币值
        mincoinList[cents] = coin_count # 更新所使用的硬币总数
        counterList[coinValueList.index(new_coin), cents] += 1  # 更新所使用不同币值的硬币的数量

    return mincoinList[change], counterList


result, counter = dp_make_change([1, 5, 10, 20, 50, 100], 70, [0] * 77)
print("最少硬币数量:", result)
print("硬币使用情况:\n", counter)
