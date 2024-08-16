import numpy as np
import random as rd
import sys
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# 递归加深度优先遍历
sys.setrecursionlimit(10000)


class Labyrinth:
    def __init__(self, rows, cols, sparsity):
        """
        初始化一个0 1 构成的矩阵,0为路径,1为墙壁,同时为这个矩阵添加出入口,以列表表示
        :param rows: 矩阵行数
        :param cols: 列数
        :param sparsity: 稀疏程度,越大越稀疏
        """
        # 生成一个全零矩阵
        self.matrix = np.zeros((rows, cols))
        # 生成一个掩码，根据稀疏程度将部分元素置为1
        mask = np.random.rand(rows, cols) > sparsity
        self.matrix[mask] = 1
        # 为迷宫添加墙壁
        self.matrix[-1, :] = 1
        self.matrix[:, -1] = 1
        self.matrix[0, :] = 1
        self.matrix[:, 0] = 1
        # 为矩阵添加出入口
        self.enter_row = rd.randint(1, rows - 2)
        self.exit_row = rd.randint(1, rows - 2)
        self.matrix[self.enter_row, 0] = 0
        self.matrix[self.exit_row, -1] = 0
        self.enter = [self.enter_row, 0]
        self.exit = [self.exit_row, cols - 1]
        del mask, self.enter_row, self.exit_row

    def __str__(self):
        return np.array2string(self.matrix)


class Turtle:
    def __init__(self, mar):
        """
        初始化海龟的初始位置,起点,所在的位置,所在位置的值,并初始化一个记录海龟路径的栈
        :param mar: 传入的迷宫矩阵
        """
        self.mar = mar.matrix
        self.start = mar.enter
        self.exit = mar.exit
        self.current_position = self.start.copy()
        self.path = []
        del mar

    @property
    def value(self):
        return self.mar[tuple(self.current_position)]

    @value.setter
    def value(self, value=1):
        self.mar[tuple(self.current_position)] = value

    def position(self):
        return self.current_position

    def set_position(self, direction):
        row, col = self.current_position
        if direction == 0 and row > 1 and self.mar[row - 1, col] == 0:
            self.current_position = [row - 1, col]
            return True
        elif direction == 1 and row < self.mar.shape[0] - 2 and self.mar[row + 1, col] == 0:
            self.current_position = [row + 1, col]
            return True
        elif direction == 2 and col > 1 and self.mar[row, col - 1] == 0:
            self.current_position = [row, col - 1]
            return True
        elif direction == 3 and self.mar[row, col + 1] == 0:  # 这里可能涉及到迷宫的出口,需要特别注意
            self.current_position = [row, col + 1]
            return True
        return False

    # 这个海龟有点蠢
    def move(self):
        self.path.append(self.current_position.copy())  # 更新路径表
        # 碰到出口
        if self.current_position == self.exit:
            self.value = 6
            print("找到出口")
            return True
        # 标记当前位置
        if self.value == 0:
            self.value = 2
        # 依次尝试上下左右四个方向
        for direction in range(4):
            if self.set_position(direction):
                if self.move():  # 如果成功找到出口，返回True
                    return True
                else:
                    self.current_position = self.path.pop()
                    continue
        if self.current_position == self.start:
            print("寻找路径失败")
            return False

    def __str__(self):
        return np.array2string(self.mar)

def plot_labyrinth(matrix):
    # 定义颜色映射
    cmap = mcolors.ListedColormap(['white', 'black', 'red', 'blue', 'green', 'yellow'])
    bounds = [0, 1, 2, 3, 4, 5, 6]
    norm = mcolors.BoundaryNorm(bounds, cmap.N)

    plt.imshow(matrix, cmap=cmap, norm=norm)
    plt.colorbar(ticks=[0, 1, 2, 3, 4, 5, 6])
    plt.show()


if __name__ == '__main__':
    labyrinth = Labyrinth(10, 10, 0.7)
    print(labyrinth.matrix)
    turtle = Turtle(labyrinth)
    turtle.move()
    print(turtle)
    plot_labyrinth(turtle.mar)
