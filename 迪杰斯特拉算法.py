# 实现迪杰斯特拉算法
# 利用之前实现的二叉堆和堆排序,以及自定义的图的相关代码来实现
# 矩阵实现更加直观
import numpy as np

def dijkstra(matrix, start):
    """ 使用Dijkstra算法计算从单一源点到所有其他节点的最短路径。
    参数:
        matrix: 图的邻接矩阵表示，二维numpy数组。
        start: 起始节点的索引。
    返回:
        列表，表示从起始节点到所有其他节点的最短路径长度。
    """
    n = len(matrix)
    visited = [False] * n
    distances = [float('inf')] * n
    distances[start] = 0

    for _ in range(n):
        # 找到未访问节点中距离最小的节点
        min_distance = float('inf')
        min_index = -1
        for i in range(n):
            if not visited[i] and distances[i] < min_distance:
                min_distance = distances[i]
                min_index = i

        # 标记该节点为已访问
        visited[min_index] = True

        # 更新相邻节点的距离
        for j in range(n):
            if matrix[min_index][j] > 0 and not visited[j]:
                new_distance = distances[min_index] + matrix[min_index][j]
                if new_distance < distances[j]:
                    distances[j] = new_distance

    return distances

# 示例图的邻接矩阵
graph_matrix = np.array([
    [0, 1, 4, 0],
    [1, 0, 2, 5],
    [4, 2, 0, 1],
    [0, 5, 1, 0]
])

# 计算从节点 0 到所有其他节点的最短路径
print(dijkstra(graph_matrix, 0))
