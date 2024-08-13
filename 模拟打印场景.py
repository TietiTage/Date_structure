import threading
import time
from ���ɴ�ӡ���� import generate_people, generate_paper
from simulate_printer import Printer


def main():
    # ��ʼ����ӡ��
    printer = Printer()

    # ���ɴ�ӡ������߳�
    generate_thread = threading.Thread(target=generate_paper, args=(printer,))

    # ��ӡ�������ӡ������߳�
    def printer_thread_func():
        while True:
            script = printer.buffer()
            if script:
                printer.my_print(script)
            time.sleep(0.1)  # ��ֹ����Ƶ���ط���

    printer_thread = threading.Thread(target=printer_thread_func)

    # �����߳�
    generate_thread.start()
    printer_thread.start()

    # �ȴ������߳����
    generate_thread.join()

    # ��ӡ���̼߳�������ֱ������Ϊ��
    while not printer.is_available() or not printer._Printer__queue.empty():
        time.sleep(0.01)

    # ������ӡ���߳�
    printer.end_print()


if __name__ == '__main__':
    generate_people()
    main()
