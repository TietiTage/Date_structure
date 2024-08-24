# 使用邻接表法来表示一个有向图
# 矩阵法直接调用numpy
# 创建简单有向图

class Vertex:
# 图当中的顶点
    def __init__(self, key):
        self.id = key
        self.neighbors = {}

    def add_neighbor(self, vert, weight=0):
        self.neighbors[vert.id] = weight

    def get_neighbors(self):
        return self.neighbors.keys()

    def __str__(self):
        return f"Vertex{self.id}, connects to:{[(v, w) for v, w in self.neighbors.items()]}"

    def get_id(self):
        return self.id


    def get_weight(self, key):
        if key in self.neighbors:
            return self.neighbors[key]
        else:
            raise KeyError(f"No edge from {self.id} to {key}")


class Graph:
    def __init__(self):
        """
        初始化节点列表,节点数量
        """
        self.vertDict = {}
        self.numVertices = 0

    def add_vertex(self, key):
        self.numVertices += 1
        self.vertDict[key] = Vertex(key)
        return self.vertDict[key]

    def get_vertex(self, key):
        if key in self.vertDict:
            return self.vertDict[key]
        else:
            raise IndexError("Vertex key not found")

    def __contains__(self, item):
        return item in self.vertDict


    def add_edge(self, source_key, target_key, weight=0):
        """
         在两个的节点当中插入有向边,若不存在,则加入,存在,则更改权重
        :param source_key: 原节点的key
        :param target_key: 目标节点的key
        :param weight: 权重
        :return:
        """
        # 如果原节点不存在于图中，则先添加原节点
        if source_key not in self.vertDict:
            self.add_vertex(source_key)
        # 如果目标节点不存在于图中，则先添加目标节点
        if target_key not in self.vertDict:
            self.add_vertex(target_key)
        # 将目标节点添加为原节点的邻居
        self.vertDict[source_key].add_neighbor(self.vertDict[target_key], weight)

    def get_vertices(self):
        return self.vertDict.keys()

    def __iter__(self):
        return iter(self.vertDict.values())
