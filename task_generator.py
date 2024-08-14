import random
import string
import simulate_printer as sp
import numpy as np

pre_people_dict = {}  # 当前的在场人数,对应的值为其在一小时内可能的打印次数,默认为1-4

countdown = 60.0  # 初始化第一个文件的倒计时时间,目前设置为60min
total_print_freq = 0 # 所有人可能发起的总打印需求次数


def generate_people():
    """
    根据所创建的随机人数, 修改字典pre_people_dict,{人名:发起的打印请求个数},
    计算总的打印需求数并返回到total_print_freq
    ran_amount: 生成随机人数
    :return: None
    """
    global pre_people_dict, total_print_freq
    ran_amount = random.randint(7, 13)
    for i in range(ran_amount):
        ran_name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
        ran_fre = random.randint(1, 4)
        pre_people_dict[ran_name] = ran_fre
    total_print_freq = ran_amount * sum(pre_people_dict.values())


class Paper(object):
    def __init__(self, count_down: float, owner: str):
        """
        owner = '' 记录文件打印需求提出人,
        countdown 倒计时,
        运用random库生成待打印文件的随机参数
        self.script = script 初始化待打印的字典,格式如下
        self.is_print = False 设置打印状态,初始设为 False
        creat_time = None 记录打印需求生成时的当前时间
        wait_time = 0 记录等待时间
        page = int 记录文件的的页数
        quality = 记录文件的质量
        """
        self.script = {
            "page": random.randint(1, 20),
            "quality": random.choice(["nor", "draft"]),
            "name": ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10)),
            "owner": owner,
            "creat_time": count_down,
            "wait_time": 0.0
        }
        self.is_print = False

    def set_quality(self, quality):
        if quality in ["draft", "nor"]:
            self.script["quality"] = quality
        else:
            raise ValueError("invalid input")

    def __call__(self):
        """
        当文件被调用打印时,将被打印的状态记录为True,
        :return: 文件的具体参数,即为self.script
        """
        self.is_print = True
        # print(self.script)
        return self.script


def generate_paper():
    """
    生成待打印的需求,生成后,应该立即将需求添加到待打印队列当中
    打印的需求提出的时间出现应该服从泊松分布,利用泊松过程的特性来生成概率
    :return: 生成的打印需求
    """

    global countdown, total_print_freq
    while pre_people_dict and countdown > 0.1:
        owner = random.choice(list(pre_people_dict.keys()))
        paper = Paper(countdown, owner)
        # # 若所有人会均匀的在某段时间内提出打印的要求,则应该使用泊松分布来计算概率,这里先随机选一下
        # countdown = random.uniform(0, countdown)
        # 泊松过程间隔服从指数分布,基于此更新下一次的时间
        countdown = countdown - np.random.exponential(1/total_print_freq)
        total_print_freq -= 1
        pre_people_dict[owner] -= 1
        if pre_people_dict[owner] == 0:
            del pre_people_dict[owner]
        return paper()


if __name__ == "__main__":

    printer1 = sp.Printer()  # 初始化当前的打印机
    generate_people()
    print(pre_people_dict)
    # generate_paper()
    printer1.add_script(generate_paper())
    printer1.add_script(generate_paper())
    printer1.add_script(generate_paper())