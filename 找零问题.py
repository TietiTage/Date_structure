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


#

def changeCoins(values):
    coinList = np.array([1, 5, 10, 20, 50, 100])
    changeList = np.zeros((len(coinList), values)) # 根据硬币列表的长度,和所兑换硬币的值创建
    changeList[1][1] = 1 # 初始化,兑换一块钱只需要一块钱的硬币一个
    for value in range(2, values+1):
        if

