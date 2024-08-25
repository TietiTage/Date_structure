# 建立深度优先遍历通用的图
import 词梯问题 as Ct


class BFSGraph(Ct.WordGraph):
    """
    通用的深度优先遍历的图,在其中实现一个普遍的深度优先遍历算法
    """
    def __init__(self):
        """
        self.time = 0 算法的步数,初始设置为0
        """
        super().__init__()
        self.time = 0

    def dfs(self):
        # 初始化所有的节点
        for _vertex in self:
            _vertex.color = "white"
            _vertex.predecessor = None
        # 开始探索
        for aVertex in self:
            if aVertex.Color == 'white':
                self.dfsvisit(aVertex)

    # 深度优先遍历的核心代码
    def dfsvisit(self, startVertex):
        startVertex.color = 'grey'
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.get_neighbors():
            if nextVertex.color == 'white':
                nextVertex.predecessor = startVertex
                self.dfsvisit(nextVertex)
        startVertex.color = "black"
        self.time += 1
        startVertex.setFinish(self.time)
