# 每次从单词当中变化一个字母,变成另一个单词,求任意两个单词之间的最短变换路径?
# 词梯问题,将相差一个字母的单词组成一个堆,并将堆当中的单词链接
import 图 as Graph
def build_heap(output_file):
    """

    :param word_file: 存储单词的txt文件
    :return:
    """
    d = {} # 存储堆的字典,每个堆都是一个列表
    g = Graph.Graph()
    with open(output_file.txt, "r") as f:

    # 创建桶,每个桶当中的单词都只有一个字母的差异.
        for line in f:
            word = line[:-1]
            for i in range(len(word)):
                # 对单词的每个位置进行替换
                heap = word[:i] + "_" + word[i+1:]
                if heap not in d:
                    d[heap].append(word)
                else:
                    d[heap] = [word]
    # 在同一个桶当中建立边和顶点
    for heap in d.keys():
        for word1 in d[heap]:
            for word2 in d[heap]:
                if word1 != word2:
                    g.add_edge(word1, word2)
    return g
