# 定义一个栈
class Stack:
    def __init__(self):
        self._stack = []
        self._size = 0

    def is_empty(self):
        if self._size == 0:
            return True
        else:
            return False

    def push(self, *item):
        self._stack.extend(list(item))
        self._size += (len(item))

    def pop(self):
        if self._size == 0:
            raise IndexError('Stack is empty')
        else:
            self._size -= 1
            return self._stack.pop(-1)

    def top(self):
        if self._size == 0:
            raise IndexError('Stack is empty')
        else:
            return self._stack[-1]

    def get_size(self):
        return self._size

    def clear(self):
        self._stack = []
        self._size = 0
        print("Stack was cleared")

    def display(self):
        print(self._stack)

if __name__ == "__main__":
    my_stack = Stack()
    my_stack.push(1, 2, 3)
    print(my_stack.pop())
    my_stack.display()
    print(my_stack.get_size())
    print(my_stack.is_empty())