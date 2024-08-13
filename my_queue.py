class Queue:
    def __init__(self):
        super().__init__(self)
        self.queue = []
        self.size = 0

    def enqueue(self, *values):
        """

        :param values: 加入队列的元素,为可迭代的对象,按迭代顺序依次入栈
        :return: None
        """
        self.queue.extend(values)
        self.size += len(values)

    def dequeue(self):
        """

        :return: 队列的首端,并将该元素出栈
        """
        if self.size == 0:
            raise Exception("Queue is empty")
        else:
            self.size -= 1
            value = self.queue.pop(-1)
            return value

    def get_front(self):
        """

        :return: 队列的首端
        """
        if self.size != 0:
            return self.queue[-1]
        else:
            raise Exception("Queue is empty")


    def get_rear(self):
        """

        :return: 队列的末端
        """
        if self.size != 0:
            return self.queue[0]
        else:
            raise Exception("Queue is empty")

    def clear(self):
        """
        重新初始化栈
        :return:
        """
        self.__init__()

    def is_empty(self):
        """

        :return: bool
        """
        return self.size == 0

    def __str__(self):
        """

        :return: 队列的所有元素构成的字符串
        """
        return str(self.queue)


if __name__ == "__main__":
    # 测试队列
    q = Queue()
    q.enqueue(1, 2, 3)
    print(q)  # 输出: [1, 2, 3]
    print(q.get_front())  # 输出: 1
    print(q.get_rear())  # 输出: 3
    print(q.dequeue())  # 输出: 1
    print(q)  # 输出: [2, 3]
    print(q.get_front())  # 输出: 2
    print(q.get_rear())  # 输出: 3
