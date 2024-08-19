# 实现二叉树
class BinaryTree:
    def __init__(self, value,key = "root"):
        self.parent = None # 父节点的名字
        self.left = None # 左子树
        self.right = None # 右子树
        self.value = value # 值
        self.key = key # 名字

    def left_child_insert(self, value, key):
        # 建立新的子树,并挂在父树的左边
        t = BinaryTree(value, key)
        t.parent = self.key
        self.left = t

    def right_child_insert(self, value, key):
        t = BinaryTree(value, key)
        t.parent = self.key
        self.right = t

    @property
    def key(self):
        return self.key

    @key.setter
    def key(self, value):
        self.key = value



