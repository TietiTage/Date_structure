import threading
import time
from simulate_printer import Printer
from task_generator import generate_people, generate_paper

# 创建打印机实例
printer = Printer()

# 定义一个标志来控制线程运行
running = True

def generate_tasks():
    generate_people()
    while running:
        paper = generate_paper()
        printer.add_script(paper)
        time.sleep(1)  # 模拟生成任务的时间间隔

def run_printer():
    while running:
        paper = printer.buffer()
        if paper:
            printer.my_print(paper)
        time.sleep(0.1)  # 防止打印任务过于频繁

if __name__ == "__main__":
    # 创建两个线程，一个用于生成任务，一个用于运行打印机
    task_thread = threading.Thread(target=generate_tasks)
    printer_thread = threading.Thread(target=run_printer)

    # 启动线程
    task_thread.start()
    printer_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # 在接收到键盘中断（Ctrl+C）时停止运行
        running = False
        task_thread.join()
        printer_thread.join()
        print("程序已终止")
