import simulate_printer as sp
import task_generator as gt
from concurrent.futures import ThreadPoolExecutor

def print_task(printer):
    printer.my_print()

def generate_task(printer):
    while True:
        new_paper = gt.generate_paper()
        printer.add_script(new_paper)

if __name__ == "__main__":
    gt.generate_people()
    printer1 = sp.Printer()

    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(print_task, printer1)
        executor.submit(generate_task, printer1)

# 代码无法正常运行
# 多线程的开发超出了我目前的能力限制,日后再试
