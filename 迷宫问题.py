import numpy as np
import random as rd


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
        self.enter_col = rd.randint(1, rows - 2)
        self.exit_col = rd.randint(1, rows - 2)
        self.matrix[self.enter_col, 0] = 0
        self.matrix[self.exit_col, -1] = 0
        self.enter = [self.enter_col, 0]
        self.exit = [self.exit_col, -1]
        del mask, self.enter_col, self.exit_col

    def __str__(self):
        return print(self.matrix)


class Turtle:
    def __init__(self, mar):
        """
        初始化海龟的初始位置,起点,所在的位置,所在位置的值
        :param mar: 传入的迷宫矩阵
        """
        self.mar = mar.matrix
        self.start = mar.enter
        self.exit = mar.exit
        self.current_position = self.start
        del mar

    @property
    def value(self):
        return self.mar[tuple(self.current_position)]

    @value.setter
    def value(self, value=1):
        self.mar[tuple(self.current_position)] = value

    def position(self):
        return self.current_position

    def setposition(self, position):
        """
        向上下左右四个方向分别尝试探索,若可行则标记现在的地点并前进
        :param position: 0, 1 ,2, 3 四个参数代表上下左右四个方向
        :return: bool ,可行为True
        """
        row = self.current_position[0]
        col = self.current_position[1]
        if position == 0 and int(self.mar[row - 1][col]) == 0:
            self.current_position[0] -= 1  # 向指定方向移动
            return True
        elif position == 1 and int(self.mar[row + 1][col]) == 0:
            self.current_position[0] += 1
            return True
        elif position == 2 and int(self.mar[row][col - 1]) == 0:
            self.current_position[1] -= 1
            return True
        elif position == 3 and int(self.mar[row][col + 1]) == 0:
            self.current_position[1] += 1
            return True
        else:
            return False

    def move(self):
        # 碰到出口
        if self.current_position == self.exit:
            return True

        # 标记当前位置
        if self.value == 0:
            self.value = 2

        # 依次尝试上下左右四个方向
        for direction in range(4):
            if self.setposition(direction):
                if self.move():  # 如果找到出口，立刻返回True
                    return True
                else:
                    return False  # 如果所有方向都走不通，返回False

    def __str__(self):
        return print(self.mar)


if __name__ == '__main__':
    labyrinth = Labyrinth(10, 10, 0.7)
    print(labyrinth.matrix)
    turtle = Turtle(labyrinth)
    turtle.move()
    print(turtle.mar)
