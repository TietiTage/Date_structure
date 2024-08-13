import random
import string
import simulate_printer as sp
import threading

pre_people_dict = {}  # 当前的在场人数,对应的值为其在一小时内可能的打印次数,默认为1-4
printer1 = sp.Printer()  # 初始化当前的打印机
countdown = 60.0 # 初始化第一个文件的倒计时时间,目前设置为60min


def generate_people():
    """
    根据所创建的随机人数, 修改字典pre_people_dict,{人名:发起的打印请求个数}
    ran_amount: 生成随机人数
    :return: None
    """
    ran_amount = random.randint(1, 10)
    for i in range(ran_amount):
        ran_name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
        ran_fre = random.randint(1, 4)
        global pre_people_dict
        pre_people_dict[ran_name] = ran_fre


class Paper(object):
    def __init__(self, countdown: float, owner: str):
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
            "creat_time": countdown,
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
        print(self.script)
        return self.script


def generate_paper():
    """
    生成待打印的需求,生成后,应该立即将需求添加到待打印队列当中
    :return: 生成的打印需求
    """
    global countdown, pre_people_dict
    while pre_people_dict and countdown > 0.1:
        owner = random.choice(list(pre_people_dict.keys()))
        countdown = random.uniform(0, countdown)
        paper = Paper(countdown, owner)
        pre_people_dict[owner] -= 1
        if pre_people_dict[owner] == 0:
            del pre_people_dict[owner]
        return paper()

if __name__ == "__main__":
    generate_people()
    print(pre_people_dict)
    while pre_people_dict:
        paper = generate_paper()
        if paper:
            printer1.add_script(paper)
        else:
            break
