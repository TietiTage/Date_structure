# 动手自己实现一个二叉堆(最小堆)
# 使用这个二叉堆进行堆排序
class BinaryHeap:
    def __init__(self):
        self.heap = [0]  # 加入0方便索引
        self.current_size = 0

    def is_empty(self):
        return self.current_size == 0

    def perc_up(self):  # 将新加入的元素上浮到合适的位置
        i = self.current_size
        while i // 2 > 0:
            if self.heap[i] < self.heap[i // 2]:
                self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2

    def min_child(self, i):
        """
        返回父节点的两个子树当中较小值对应的索引
        :param i: 当前的父节点的索引
        :return: 较小的节点的索引
        """
        # 判断当前节点是否只有一个子树
        if self.current_size < 2 * i + 1:
            return 2 * i
        else:
            if self.heap[2 * i] < self.heap[2 * i + 1]:
                return 2 * i
            else:
                return 2 * i + 1

    def perc_down(self, i):  # 下沉,在弹出堆顶的元素之后,将最小值归位
        """
        将父节点的值与其子节点的较小值进行比较,若子节点小,则交换,将原先的父节点下沉
        :param i: 父节点的索引
        :return:
        """
        while 2*i <= self.current_size:
            j = self.min_child(i)
            if self.heap[i] > self.heap[j]:
                self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            i = j

    def del_min(self):
        """
        弹出二叉堆堆顶的元素,并使用下沉对堆进行重建
        :return: 堆顶的元素
        """
        item = self.heap[1]
        # 将当前的堆顶元素替换为最大元素,对堆进行重建
        self.heap[1] = self.heap[self.current_size]
        self.perc_down(1)
        self.current_size -= 1
        # 移除重复的最大元素
        self.heap.pop()
        return item

    def get_min(self):
        return self.heap[1]

    def build_heap(self, itera: iter):
        """
        根据输入的可迭代对象创建一个新的二叉堆
        :return:None
        """
        for member in itera:
            self.current_size += 1
            self.heap.append(member)
            self.perc_up()

    def insert(self, item):
        """
        向堆当中加入元素,并调整堆的结构,使之符合二叉堆
        :param item:
        :return:
        """
        self.heap.append(item)
        self.current_size += 1
        self.perc_up()

    def get_size(self):
        return self.current_size

    def get_serial_number(self, member):
        return self.heap.index(member)

    def heap_sort(self):
        res = []
        copy = self
        while copy.heap.__len__() > 1:
            member = copy.del_min()
            res.append(member)
        return res


if __name__ == '__main__':
    heap = BinaryHeap()
    my_list = [99, 45, 78, 484, 48, 114, 1233, 15453, 12203]
    heap.build_heap(my_list)
    heap.insert(25)
    print(heap.heap_sort())
