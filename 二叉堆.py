# 实现最小二叉堆

class BinaryHeap:
    def __init__(self):
        self.heapList = [0]  # 存储完全二叉树的列表,插入0用于方便计算编号
        self.currentSize = 0

    def percup(self, i):
        """
        # 假设父节点的值小于子节点,则交换子节点和父节点的值
        :param i: 平衡二叉树节点的编号
        :return: None
        """
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                temp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = temp
            i = i // 2  # 改变当前节点的编号,循环调用

    def minChild(self, i):
        """
        返回子树当中两个节点当中较小的一个的节点编号
        :param i: 父节点编号
        :return:
        """
        if i * 2 + 1 > self.currentSize:  # 如果此时, 父节点的右子树不存在
            return i * 2  # 返回左子树的编号
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:  # 比较左右子树的值的大小
                return i * 2
            else:
                return i * 2 + 1

    def percdown(self, i):
        while i // 2 <= self.currentSize:
            mc = self.minChild(i)
            # 若父节点的元素的值大于两个子树最小的元素,与最小的元素交换位置(上浮)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            # 改变节点的编号
            i = mc

    def insert(self, item):
        self.heapList.append(item)  # 在表的末尾加入
        self.currentSize += 1  #
        self.percup(self.currentSize)

    def findMin(self):
        """
        返回最小的元素，即堆顶元素
        :return: 堆顶元素
        """
        if self.currentSize == 0:
            return None
        return self.heapList[1]

    def delMin(self):
        """
        移走堆顶的元素,保留0,将堆尾的元素移到堆顶
        并将新的顶进行下沉以保持完全二叉树的性质
        :return:
        """
        retVal = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percdown(1)
        return retVal

    def isEmpty(self):
        """
        判断堆是否为空
        :return: 布尔值，表示堆是否为空
        """
        return self.currentSize == 0

    def size(self):
        return self.currentSize

    def buildHeap(self, alist):
        """从一个无序表生成一个二叉堆"""
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0].extend(alist)

        print(len(self.heapList), i)
        # 从最后节点的父亲节点开始,逐渐下沉,使用下沉的方式生成完全二叉树
        while i // 2 > 0:
            print(self.heapList, i)
            self.percdown(i)
            i -= 1
        print(self.heapList, i)
