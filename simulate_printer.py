import queue
import sys
import time
import threading


def check(func):
    """
    装饰器,用于对函数的参数进行检查
    :param func: 传入的需检查的函数,这里应该为add_script
    :return: 装饰器
    """

    def wrapper(ins, *scripts: dict):
        for script in scripts:
            if script.keys() != {"page", "name", "quality", "creat_time", "wait_time", "owner"}:
                raise KeyError("invalid form!key shall in {page, name, quality, creat_time, wait_time, owner}")
            if not isinstance(script["page"], int) or script["page"] < 1:
                raise ValueError("page should be positive int")
            if script["quality"] not in ["nor", "draft"]:
                raise ValueError("invalid mode, use nor or draft")
            if not isinstance(script["creat_time"], float):
                raise ValueError("invalid time, use float")
            if not isinstance(script["wait_time"], float):
                raise ValueError("invalid time, use float")
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
        self.__total_wait = 0, 文件的总等待时长
        """
        self.__lock = threading.Lock()
        self.__available = True
        self.__queue = queue.Queue()
        self.__mode = {"draft": 0.1, "nor": 0.2}
        self.__current_speed = 0
        self.__res_print_info = []
        self.__total_consume = 0
        self.__total_wait = 0

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
        向队列当中加入文件,同时立刻打开打印机
        :param script: 应该为字典,
        格式:{page: int,
            quality: "nor" or "draft",
            name: str,
            creat_time: countdown,
            owner: owner_name
            wait_time: 0}
        :return: None
        """
        for item in script:
            self.__queue.put(item)
        self.my_print(self.buffer())

    def buffer(self):
        """
        从队列中获取文件,
        :return: script: 一部字典,对应一个模拟打印的对象,由buffer弹出
        """
        time.sleep(0.1)  # 防止过于频繁地访问
        with (self.__lock):  # 保持buffer对属性访问的优先权
            if self.__available and not self.__queue.empty():
                script = self.__queue.get()
                return script

    def record(self, **kwargs):
        """
        向记录的列表当中添加文件信息，支持动态字段扩展。
        :param kwargs: 动态传递的文件信息
        :return: None
        """
        # 默认字段，可以根据需要扩展
        default_fields = {
            "name": None,
            "page": None,
            "count": None,
            "quality": None,
            "owner": None,
            "wait_time": None,
            "creat_time": None,
        }

        # 使用提供的字段更新默认字段
        info_dict = {**default_fields, **kwargs}

        # 更新总耗时
        if "count" in info_dict and info_dict["count"] is not None:
            self.__total_consume += round(info_dict["count"], 2)
            info_dict["count"] = round(info_dict["count"], 2)
        # 更新总等待时间
        if "wait_time" in info_dict and info_dict["wait_time"] is not None:
            self.__total_wait += round(info_dict["wait_time"], 2)
            info_dict["wait_time"] = round(info_dict["wait_time"], 2)
        # 将信息添加到记录列表中
        self.__res_print_info.append(info_dict)

    def update_waiting_times(self, elapsed_time):
        """
        更新队列中所有文件的等待时间。
        :param elapsed_time: 当前打印任务所花费的时间（分钟）。
        :return: None
        """
        # 使用队列的queue内置属性进行原地更新
        with self.__lock: # 保持线程安全
            temp_list = list(self.__queue.queue)  # 获取队列中所有元素的副本
            for paper in temp_list:
                paper["wait_time"] += elapsed_time  # 更新等待时间

            # 将更新后的列表替换为队列内容
            self.__queue.queue.clear()  # 清空原队列
            for paper in temp_list:
                self.__queue.put(paper)  # 重新加入更新后的元素

    def my_print(self, script):
        """
        打印当前的文件,文件由buffer给出,同时调用record记录文件的打印数据信息
        :return: None
        """
        while not self.__queue.empty():
            # 记录文件的相关信息
            page, quality, name, owner, wait_time, creat_time = \
                (script[key] for key in ["page", "quality", "name", "owner", "wait_time", "creat_time"])
            self.set_mode(quality)
            count = self.__current_speed * page
            self.update_waiting_times(count)  # 更新后续队列当中的每个文件的等待时间
            if script and creat_time-wait_time > 0.01:
                self.__available = False

                # 记录打印的状态
                self.record(
                    name=name,
                    page=page,
                    count=count,
                    quality=quality,
                    owner=owner,
                    wait_time=wait_time,
                    creat_time=creat_time)

                self.__available = True
            else:
                self.end_print()

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
        return (f"打印所有文件总耗时:{self.__total_consume}\n"
                f"所有文件的总等待时间为:{self.__total_wait}\n")

    def end_print(self):
        """
        强制清空打印的队列,使得打印机回到空闲的状态,不再打印,
        :return: None
        """
        self.__available = True
        self.log()
        print("运行时长已到达上限,或打印的文件为空,日志已经保存")
        print(self)
        sys.exit()
