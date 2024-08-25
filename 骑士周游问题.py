# 求解国际象棋当中的骑士周游问题
# 使用深度优先遍历
import 词梯问题 as Ct
import sys

sys.setrecursionlimit(10000)

# 生成存储可能路径的图
# 存储回溯节点的栈
graph = Ct.WordGraph()
stack = []


# 生成所有可能的节点
def generate_spots():
    spots = []
    for i in range(8):
        for j in range(8):
            spots.append((i, j))
    return spots


def generate_path():
    spots = generate_spots()
    for pos1 in spots:
        for pos2 in spots:
            # 检测是否是一个合法路径,如果是,则加入图当中
            if abs(pos1[0] - pos2[0]) == 2:
                if abs(pos1[1] - pos2[1]) == 1:
                    graph.add_edge(pos1, pos2)
            if abs(pos1[1] - pos2[1]) == 2:
                if abs(pos1[0] - pos2[0]) == 1:
                    graph.add_edge(pos1, pos2)


def is_visited_all_neighbors(pos):
    """
    判断当前节点的所有邻接节点是否都已经被访问
    :param pos: 当前的节点
    :return: bool,true为都已经访问,false为还有未被访问的节点
    """
    pos_neighbors = pos.get_neighbors()
    for key in pos_neighbors:
        if graph.vertDict[key].color == "white":
            return False
        else:
            continue
    return True


def find_path(source: tuple):
    """
    寻找从起始点到所有可能点的路径,使用深度优先遍历
    :param source: 起始坐标
    :return:
    """
    global stack

    source_node = graph.vertDict[source]
    stack.append(source_node)
    source_node.color = "black"

    # 终止条件：栈中节点数达到64，即找到完整路径
    if len(stack) == 64:
        return True

    # 遍历邻接节点
    for _neighbor in source_node.get_neighbors():
        next_node = graph.vertDict[_neighbor]
        if next_node.color == "white":
            next_node.predecessor = source_node
            if find_path(next_node.id):
                return True

    # 若未能找到完整路径，进行回溯
    stack.pop()
    source_node.color = "white"
    return False

if __name__ == '__main__':
    generate_path()
    if find_path((0, 0)):
        print("找到完整路径：")
        for node in stack:
            print(node.id)
    else:
        print("未找到完整路径")




if __name__ == '__main__':
    generate_path()
    find_path((0, 0))
