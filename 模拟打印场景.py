import threading
import time
from 生成打印任务 import generate_people, generate_paper
from simulate_printer import Printer


def main():
    # 初始化打印机
    printer = Printer()

    # 生成打印需求的线程
    generate_thread = threading.Thread(target=generate_paper, args=(printer,))

    # 打印机处理打印需求的线程
    def printer_thread_func():
        while True:
            script = printer.buffer()
            if script:
                printer.my_print(script)
            time.sleep(0.1)  # 防止过于频繁地访问

    printer_thread = threading.Thread(target=printer_thread_func)

    # 启动线程
    generate_thread.start()
    printer_thread.start()

    # 等待生成线程完成
    generate_thread.join()

    # 打印机线程继续运行直到队列为空
    while not printer.is_available() or not printer._Printer__queue.empty():
        time.sleep(0.01)

    # 结束打印机线程
    printer.end_print()


if __name__ == '__main__':
    generate_people()
    main()
