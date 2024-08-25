# 每次从单词当中变化一个字母,变成另一个单词,求任意两个单词之间的最短变换路径?
# 词梯问题,将相差一个字母的单词组成一个堆,并将堆当中的单词链接
import 图 as Graph
import queue as q


class GraphNode(Graph.Vertex):
    __slots__ = ("__predecessor", "__distance", "__color")
    """
    设置广度优先遍历的节点属性和方法
    """

    def __init__(self, key):
        """
        调用父类当中的初始化方法,并设置:
        self.__predecessor = None 前驱节点
        self.__distance = 0 距离起始节点的距离
        self.__color = 'white' 白色为未发现 灰色为已经发现 黑色为已经探索
        :param key:
        """
        super().__init__(key)
        self.__predecessor = None
        self.__distance = 0
        self.__color = 'white'

    @property
    def predecessor(self):
        return self.__predecessor

    @predecessor.setter
    def predecessor(self, predecessor):
        self.__predecessor = predecessor

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        if color in ['grey', "black", "white"]:
            self.__color = color
        else:
            raise ValueError("Color must be 'grey' or 'black' or 'white' ")
    @property
    def distance(self):
        return self.__distance

    @distance.setter
    def distance(self, distance):
        self.__distance = distance


class WordGraph(Graph.Graph):
    def add_vertex(self, key):
        self.numVertices += 1
        self.vertDict[key] = GraphNode(key)
        return self.vertDict[key]


def build_graph(output_file):
    """
     利用传入的单词文件,建立图
    :param output_file: 存储单词的txt文件
    :return:
    """
    d = {}  # 存储堆的字典,每个堆都是一个列表
    g = WordGraph()
    with open(output_file, encoding="utf-8", mode="r") as f:

        # 创建桶,每个桶当中的单词都只有一个字母的差异.
        for line in f:
            word = line.strip()
            for i in range(len(word)):
                # 对单词的每个位置进行替换
                heap = word[:i] + "_" + word[i + 1:]
                if heap in d:
                    d[heap].append(word)
                else:
                    d[heap] = [word]
    # 在同一个桶当中建立边和顶点
    for heap in d.keys():
        for word1 in d[heap]:
            for word2 in d[heap]:
                if word1 != word2:
                    g.add_edge(word1, word2, weight=1)
                    # 所有相差一个字母的单词都建立了关联

    return g
def traverse(y):
    """
    从目标单词回溯到起始单词
    :param y: 目标节点
    :return:
    """
    x = y
    while x.predecessor:
        print(x.get_id())
        x = x.predecessor
    print(x.get_id())

def find_shortest_path(gr: WordGraph, source: str, target: str):
    """
    寻找两个单词之间的最短的变化路径,使用广度优先遍历
    :param gr: 存储单词的图
    :param source: 起始单词
    :param target: 目标单词
    :return:
    """
    source = source.upper()
    target = target.upper()
    # 寻找时存储需要访问节点的队列
    queue = q.Queue()
    # 找到单词对应的节点
    current_node = gr.vertDict[source]
    queue.put(current_node)
    # 将第一个元素出队,访问其邻接节点
    while not queue.empty():
        current = queue.get()
        neighbors_set = current.get_neighbors()
        for neighbor in neighbors_set:
            neighbor_gr = gr.vertDict[neighbor]
            if neighbor_gr.color == "white":
                neighbor_gr.color = "grey"
                neighbor_gr.predecessor = current
                neighbor_gr.distance = current.distance + 1
                queue.put(neighbor_gr)
        # 标记为已访问
        current.color = "black"
    traverse(gra.vertDict[target])



if __name__ == '__main__':
    gra = build_graph(output_file="output_file.txt")
    find_shortest_path(gra, "find", "holy")

