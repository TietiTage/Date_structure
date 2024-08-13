import random
import string
import simulate_printer as sp

# 当前的在场人数,对应的值为其在一小时内可能的打印次数,默认为1-4
pre_people_dict = {}


def generate_people():
    """"""
    ran_amount = random.randint(1, 10)
    for i in range(ran_amount):
        ran_name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
        ran_page = random.randint(1, 4)
        global pre_people_dict
        pre_people_dict[ran_name] = ran_page

class Paper():
    def __init__(self):
        """
        运用random库生成待打印文件的随机参数
        self.script = script 初始化待打印的字典,格式为script1 = {"page": 5, "name": "Document1", "quality": "nor"}
        self.is_print = False 设置打印状态,初始设为 False
        self.time = sp.current_time 记录打印需求生成时的当前时间
        self.wait_time = 0 记录等待时间
        self.res_wait_time = [] 记录每个文件从生成到正式打印的时间
        self.owner = '' 记录文件打印需求提出人
        """
        random_name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
        random_page = random.randint(1, 20)
        random_quality = random.choice(["nor", "draft"])
        script = {"page": random_page, "quality": random_quality, "name": random_name}
        self.script = script
        del random_page, random_quality, random_name, script
        self.is_print = False
        self.time = sp.current_time
        self.wait_time = 0
        self.res_wait_time = []
        self.owner = ''

    def __call__(self):
        """
        当文件被调用打印时,将被打印的状态记录为True,并记录从需求生成到开始打印等待的时间
        :return: 文件的具体参数,即为self.script
        """
        self.is_print = True
        self.wait_time = self.time - self.wait_time
        return self.script




