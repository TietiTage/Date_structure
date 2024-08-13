import queue
import sys
import time
import threading

# 打印机运行的时间,以分钟计算,为倒计时
current_time = 60


def check(func):
    """
    装饰器,用于对函数的参数进行检查
    :param func: 传入的需检查的函数,这里应该为add_script
    :return: 装饰器
    """

    def wrapper(ins, *scripts: dict):
        for script in scripts:
            if script.keys() != {"page", "name", "quality"}:
                raise KeyError("格式错误!key应为page,name,quality")
            if not isinstance(script["page"], int) or script["page"] < 1:
                raise ValueError("page 应该为正整数")
            if script["quality"] not in ["nor", "draft"]:
                raise ValueError("invalid mode, use nor or draft")
        return func(ins, *scripts)

    return wrapper


class Printer:
    def __init__(self):
        """
        属性:self.__available = True   打印机是否空闲,默认为是
        self.__queue = queue.Queue() 打印队列生成,初始为空
        self.__mode = {"draft": 0.1, "nor": 0.2} 内置的打印质量和对应的速度,单位为 min/page
        self.__current_speed = 0 当前速度,初始设置为0
        self.__res_print_info 列表,元素为字典,文件打印的信息,
                        格式为{name : ({打印耗时:}, {质量:}, {页数:},{需求提出人:}},值为元组
        self.__lock = threading.Lock() ,线程锁,确保当buffer访问打印机和队列状态时,其他方法无法修改buffer要访问的状态
        self.__total_consume = 0 ,文件打印的总耗时

        """
        self.__lock = threading.Lock()
        self.__available = True
        self.__queue = queue.Queue()
        self.__mode = {"draft": 0.1, "nor": 0.2}
        self.__current_speed = 0
        self.__res_print_info = []
        self.__total_consume = 0

    def is_available(self):
        """
        判断打印机是否处于空闲状态
        :return: bool类型,是返回True,否返回False
        """
        return self.__available

    def get_speed(self):
        """
        :return: 返回打印机当前的速度
        """
        return self.__current_speed

    def set_mode(self, mode):
        """
        设置打印机的打印模式
        :param mode: 打印模式,应为"nor"或"draft"
        :return: None
        """
        if mode in self.__mode:
            self.__current_speed = self.__mode[mode]
        else:
            raise ValueError("invalid mode, use nor or draft")

    @check
    def add_script(self, *script: dict):
        """
        向队列当中加入文件
        :param script: 应该为字典,格式:{page: int, quality: "nor" or "draft", name: str }
        :return: None
        """
        for item in script:
            self.__queue.put(item)

    def buffer(self):
        """
        从队列中获取文件
        :return: script: 一部字典,对应一个模拟打印的对象,由buffer弹出
        """
        time.sleep(0.01)
        with self.__lock:  # 保持buffer对属性访问的优先权
            if self.__available and not self.__queue.empty():
                script = self.__queue.get()
                return script

    def record(self, name: str, page: int, count: float, quality: str, demander: str, wait_time: float):
        """
        向记录的列表当中添加文件信息,格式由info_dict给出
        :param name: 文件名称
        :param page: 文件页数, int
        :param count: 打印耗时的秒数,保留2位数字
        :param quality: 为nor or draft
        :param demander: 文件打印的提出者
        :param wait_time: 文件从提出打印到打印的等待时间,保留两位数字
        :return: None
        """
        info_dict = {
            name:
                (
        {"耗时": round(count, 2)},
        {"质量": quality},
        {"页数": page},
        {"需求者": demander},
        {"等待时间": round(wait_time, 2)}
            )
        }
        self.__total_consume += count
        self.__res_print_info.append(info_dict)

    def my_print(self):
        """
        打印当前的文件,文件由buffer给出,同时调用record记录文件的打印数据信息
        :return: None
        """
        while not self.__queue.empty():
            script = self.buffer()
            if script:
                # 记录文件的相关信息
                page, quality, name, demander, wait_time = \
                    (script[key] for key in ["page", "quality", "name", "demander", "wait_time"])

                self.set_mode(quality)
                count = self.__current_speed * page
                self.__available = False
                self.record(name, page, count, quality,demander, wait_time)  # 记录打印的状态
                self.__available = True
                global current_time
                current_time -= count  # 计时器减去打印的时间

    def log(self):
        """
        将打印记录保存到日志文件中
        :return: None
        """
        timestamp = time.strftime("%Y%m%d_%H%M%S", time.localtime())
        with open(f"{timestamp}.txt", "w+", encoding="utf-8") as file:
            for item in self.__res_print_info:
                file.write(f"{item}\n", )
        print(f"本次运行的总文件日志已经保存到{file.name}当中")

    def __str__(self):
        """
        返回打印机的总耗时
        :return: str
        """
        return f"打印所有文件总耗时:{self.__total_consume}"

    def end_print(self):
        """
        强制清空打印的队列,使得打印机回到空闲的状态,不再打印
        :return: None
        """
        with self.__lock:
            while not self.__queue.empty():
                self.__queue.get()
            self.__available = True
            sys.exit()
