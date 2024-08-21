# 生成一个二叉查找树
class TreeNode:
    """
    定义二叉查找树节点的一些性质
    """
    def __init__(self, key, value, parent=None, left=None, right=None):
        """
        初始化节点
        :param key: 键
        :param value: 值
        :param parent: 父节点
        :param left: 左节点
        :param right: 右节点
        """
        self.key = key
        self.payload = value
        self.left = left
        self.right = right
        self.parent = parent

    def has_left(self):
        return self.left

    def has_right(self):
        return self.right

    def is_left(self):
        # 需要排除根节点的情况
        return self.parent and self.parent.left == self

    def is_right(self):
        return self.parent and self.parent.right == self

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return self.left is None and self.right is None

    def has_any_children(self):
        return self.left or self.right

    def has_both_children(self):
        return self.left and self.right

    def replace_node_data(self, key, value, lt, rt):
        self.key = key
        self.payload = value
        self.left = lt
        self.right = rt
        if self.has_left():
            self.left.parent = self
        if self.has_right():
            self.right.parent = self


class BinarySearchTree:
    def __init__(self):
        """
        初始化一个二叉树
        """
        self.root = None
        self.size = 0

    def length(self):
        return self.size
    def build(self,key, value):
        """
        检查bst是否为None.是,则将传入的key构建为root;
        否则递归调用put函数构建二叉树
        :param key:
        :param value:
        :return:
        """
        if self.root:
            self.put(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
        self.size += 1

    def put(self, key, value, current_node):


    def __iter__(self):
        ...