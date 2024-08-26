import heapq
import time

import 词梯问题 as Ct
# 使用最小堆和自定义的图类实现


def dijkstra(g, start, end):
    # 根据索引找到对应的节点
    start = g.get_vertex(start)
    end = g.get_vertex(end)

    # 将起始节点距离自身的距离设置为0
    start.distance = 0

    # 最小堆，优先队列
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))

    while priority_queue:
        # 取出当前距离最小的节点
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node.color == "black":
            continue

        current_node.color = "black"

        if current_node == end:
            break

        # 更新邻接节点的距离
        for key in current_node.get_neighbors():
            neighbor = g.get_vertex(key)
            new_distance = current_distance + current_node.get_weight(key)

            if new_distance < neighbor.distance:
                neighbor.distance = new_distance
                neighbor.predecessor = current_node
                heapq.heappush(priority_queue, (new_distance, neighbor))

    # 回溯路径
    path = []
    current = end
    while current:
        path.append(current)
        current = current.predecessor

    path.reverse()
    print([node.id for node in path])
    print(f"最短距离为 {end.distance}")


if __name__ == '__main__':
    # 生成一个图，添加节点和边，并赋权
    a = time.perf_counter()
    graph = Ct.WordGraph()
    graph.add_edge(5, 1, 7)
    graph.add_edge(4, 2, 5)
    graph.add_edge(1, 3, 6)
    graph.add_edge(2, 3, 2)
    graph.add_edge(3, 5, 4)
    graph.add_edge(5, 4, 6)
    graph.add_edge(2, 4, 3)
    dijkstra(graph, 1, 4)
    b = time.perf_counter()
    print(f"耗时{b-a}")
