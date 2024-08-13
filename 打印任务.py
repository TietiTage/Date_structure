import random
import string
import simulate_printer as sp

# ��ǰ���ڳ�����,��Ӧ��ֵΪ����һСʱ�ڿ��ܵĴ�ӡ����,Ĭ��Ϊ1-4
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
        ����random�����ɴ���ӡ�ļ����������
        self.script = script ��ʼ������ӡ���ֵ�,��ʽΪscript1 = {"page": 5, "name": "Document1", "quality": "nor"}
        self.is_print = False ���ô�ӡ״̬,��ʼ��Ϊ False
        self.time = sp.current_time ��¼��ӡ��������ʱ�ĵ�ǰʱ��
        self.wait_time = 0 ��¼�ȴ�ʱ��
        self.res_wait_time = [] ��¼ÿ���ļ������ɵ���ʽ��ӡ��ʱ��
        self.owner = '' ��¼�ļ���ӡ���������
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
        ���ļ������ô�ӡʱ,������ӡ��״̬��¼ΪTrue,����¼���������ɵ���ʼ��ӡ�ȴ���ʱ��
        :return: �ļ��ľ������,��Ϊself.script
        """
        self.is_print = True
        self.wait_time = self.time - self.wait_time
        return self.script




