import my_queue

# 实现约瑟夫环
vic_queue = my_queue.Queue()
vic_queue.enqueue("a", "b", "c", "d", "e", "f", "g", "h", "i", "j")

def kill(_queue: my_queue.Queue):
    count = 0
    person = ''
    dead_queue = my_queue.Queue()

    while not _queue.is_empty():
        count += 1
        person = _queue.dequeue()
        if count % 7 != 0:
            _queue.enqueue(person)

        else:
            dead_queue.enqueue(person)

    print(f"最后一位留下的人是:{person}")
    print(f"受害者顺序:{str(dead_queue.queue)}")


if __name__ == '__main__':
    kill(vic_queue)
