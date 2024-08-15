# 运用递归去尝试求解一个二阶差分方程
# 完成杀人游戏: 600个人,每次杀掉奇数位的人,后面的人向前补位,最后一个人是初始几号的概率最大?
import matplotlib.pyplot as plt
import numpy as np

n = 600
kill = np.zeros((n+1,n+1))
kill[1,1] = 1
for n in range(2, n+1):
    for k in range(1, n+1):
        kill[n,k] = \
            kill[n - 1, k - 1]* (k // 2) / ((n+1) // 2) + \
            kill[n - 1, k] * ((n+1)//2 - (k+1) //2)/((n+1)//2)

if __name__ == '__main__':
    print(kill[600, 600])
    x = np.array(range(1, n + 1))
    y = np.array(kill[600, 0:600])

# 画图
    plt.figure(figsize=(100, 30))
    plt.plot(x, y, label='Probability of being the last person', color='b')
    plt.xlabel('Initial Position')
    plt.xticks(np.arange(0, len(x) + 1, step=20))  # 根据需要调整步长step
    plt.xlim(1, len(y))
    plt.ylabel('Probability')
    plt.title('Probability of Being the Last Person in the Game')
    plt.legend()
    plt.grid(True)
    plt.show()



