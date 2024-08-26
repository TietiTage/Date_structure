# 使用图，完成一个迪杰斯特拉算法
import 词梯问题 as Ct


def dijkstra(g, start, end):
    # 根据索引找到对应的节点
    start = g.get_vertex(start)
    end = g.get_vertex(end)
    # 初始化存储路径的列表
    # 初始化当前节点距离开始节点的最小距离min_distance
    path_list = []

    # 将起始节点距离自身的距离设置为0
    start.distance = 0

    def find(_g, _start, _end):
        current_node = _start
        path_list.append(current_node)
        # 结束条件
        if current_node == _end:
            print([node.id for node in path_list])
            min_distance = path_list.pop().distance
            print(f"最短距离为{min_distance}")
            return True
        else:
            current_node.color = "black"
            # 读取当前节点未访问的邻接节点,并选取其中距离最短的作为下一个节点
            neighbors_keys = current_node.get_neighbors()
            neighbors_nodes = []
            for key in neighbors_keys:
                candidate_node = _g.get_vertex(key)
                new_distance = current_node.distance + current_node.get_weight(key)

                # 更新邻接节点的距离
                if new_distance <= candidate_node.distance:
                    candidate_node.distance = new_distance
                neighbors_nodes.append(candidate_node)

                # 选择距离最短的未访问节点
                next_node = min(
                    (node for node in neighbors_nodes if node.color == "white"),
                    key=lambda node: node.distance,
                    default=None
                )
                if next_node:
                    if find(_g, next_node, _end):
                        return True
        current_node.color = "white"
        path_list.pop()
        return False

    return find(g, start, end)


if __name__ == '__main__':
    # 生成一个图，添加节点和边，并赋权
    graph = Ct.WordGraph()
    graph.add_edge(5, 1, 7)
    graph.add_edge(4, 2, 5)
    graph.add_edge(1, 3, 6)
    graph.add_edge(2, 3, 2)
    graph.add_edge(3, 5, 4)
    graph.add_edge(5, 4, 6)
    graph.add_edge(2, 4, 3)
    dijkstra(graph, 1, 4)