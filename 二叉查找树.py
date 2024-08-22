# 生成一个二叉查找树
from 树 import BinaryTree


class TreeNode:
    """
    定义二叉查找树节点的一些性质
    """
    def __init__(self, key: int, value, parent=None, left=None, right=None):
        """
        初始化节点
        :param key: 键,用于排序
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

    # def replace_node_data(self, key, value, lt, rt):
    #     """
    #     变更节点的数据
    #     :param key: 新的键
    #     :param value:
    #     :param lt: 新的左子树
    #     :param rt: 新的右子树
    #     :return:
    #     """
    #     self.key = key
    #     self.payload = value
    #     self.left = lt
    #     self.right = rt
    #     if self.has_left():
    #         self.left.parent = self
    #     if self.has_right():
    #         self.right.parent = self

    def __iter__(self):
        """
        实现二叉树的中序遍历,按键的升序访问所有节点并逐个返回key
        :return:
        """
        if self.has_left():
            for item in self.left:  # 递归遍历左子树,递归地调用该方法
                yield item  # 逐个返回左子树的键(通过下一行)
        yield self.key  # 完成左子树的遍历后,返回当前节点(根节点)的键
        if self.has_right():
            for item in self.right:
                yield item


class BinarySearchTree:
    def __init__(self):
        """
        初始化一个二叉树
        """
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def _build(self, key, value):
        """
        检查bst的根节点是否为None.是,则将传入的key构建为root;
        否则递归调用put函数从根节点开始构建二叉树
        :param key:
        :param value:
        :return:
        """
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
        self.size += 1

    def _put(self, key, value, current_node):
        """
        使用TreeNode类来构建节点信息,并递归生成节点,根据key的大小关系构建
        :param key: 待插入的键
        :param value: 值
        :param current_node: 当前节点
        :return:
        """
        # 递归生成左子树
        if key < current_node.key:
            if current_node.has_left():
                self._put(key, value, current_node.left)
            # 若没有左子树,则key成为左子节点
            else:
                current_node.left = TreeNode(key, value, parent=current_node)
        # 递归生成右子树
        elif key > current_node.key:
            if current_node.has_right():
                self._put(key, value, current_node.right)
            else:
                current_node.right = TreeNode(key, value, parent=current_node)
        else:
            current_node.payload = value

    def __setitem__(self, key, value):
        self._build(key, value)

    def __getitem__(self, key):
        if self.root:
            # 从root节点开始查找
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def __delitem__(self, key):
        """
        用get方法得到要删除的节点,并删除
        :param key: 待删除的节点索引
        :return:
        """
        # 非根节点
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self._remove(node_to_remove)
                self.size -= 1
            else:
                raise KeyError("Invalid Key")
        # 只有一个节点,则重新初始化二叉树
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError("Invalid Key")

    def _remove(self, node):
        """
        删除掉指定的节点,并在不改变树性质的前提下更改指针朝向
        :param node: 节点
        :return:
        """
        # 叶子节点的情况
        if node.is_leaf():
            if node.is_left():
                node.parent.left = None
            elif node.is_right():
                node.parent.right = None
            else:
                # 如果是根节点且是叶子节点的情况
                self.root = None

        # 指定节点有一个子节点
        elif node.has_any_children() and not node.has_both_children():
            # 1. 只有左子节点
            if node.has_left():
                child = node.left
            else:
                child = node.right

            if node.is_left():
                node.parent.left = child
            elif node.is_right():
                node.parent.right = child
            else:
                self.root = child
            child.parent = node.parent

        # 指定节点有两个子节点
        elif node.has_both_children():
            # 找到后继节点（右子树中最小的节点）,用后继节点替代被删除的节点,并删除后继节点
            successor = self._find_min(node.right)
            node.key = successor.key
            node.payload = successor.payload
            # 递归删除后继节点
            self._remove(successor)

    @staticmethod
    def _find_min(node):
        """
        找到以node为根节点的子树中的最小节点
        :param node: 当前节点
        :return: 子树中的最小节点
        """
        current = node
        while current.has_left():
            current = current.left
        return current

    def _get(self, key, current_node):
        """
        根据输入的键找到对应的节点并返回
        :param key:需要查找的键
        :param current_node: 当前正在比对的节点,默认应该从根节点开始
        :return:需要查找的键对应的节点,没有则返回None
        """
        if not current_node:  # 若当前节点为空:
            return None
        elif current_node.key == key:  # 需要查找的节点的key与输入的key一致
            return current_node
        elif current_node.key > key:
            return self._get(key, current_node.left)
        else:
            return self._get(key, current_node.right)

    def __contains__(self, key):
        """
        判断key是否在树当中,返回bool
        :param key:需要查找的key
        :return:
        """
        if self._get(key, self.root):
            return True
        else:
            return False


if __name__ == '__main__':
    # 测试样例
    def test_bst():
        # 创建一个二叉查找树实例
        bst = BinarySearchTree()

        # 插入节点
        bst[10] = "Root"
        bst[5] = "Left Child"
        bst[15] = "Right Child"
        bst[3] = "Left Grandchild"
        bst[7] = "Right Grandchild"

        print(bst.length())

        # 测试插入和查找功能
        assert bst[10] == "Root", "Test failed: Root node"
        assert bst[5] == "Left Child", "Test failed: Left child"
        assert bst[15] == "Right Child", "Test failed: Right child"
        assert bst[3] == "Left Grandchild", "Test failed: Left grandchild"
        assert bst[7] == "Right Grandchild", "Test failed: Right grandchild"

        # 测试删除功能
        del bst[3]
        assert bst[3] is None, "Test failed: Deleting left grandchild"
        del bst[5]
        assert bst[5] is None, "Test failed: Deleting left child"
        del bst[10]
        assert bst[10] is None, "Test failed: Deleting root node"

        # 测试树的大小
        assert bst.length() == 2, "Test failed: Tree size"

        # 测试包含功能
        assert 15 in bst, "Test failed: Contains right child"
        assert 3 not in bst, "Test failed: Does not contain deleted node"

        # 测试中序遍历
        bst[10] = "Root"
        bst[5] = "Left Child"
        bst[15] = "Right Child"
        bst[3] = "Left Grandchild"
        bst[7] = "Right Grandchild"
        print(bst[7])
        inorder_keys = [key for key in bst.root]
        print(inorder_keys)
        assert inorder_keys == [3, 5, 7, 10, 15], "Test failed: Inorder traversal"


        print("All tests passed!")


    # 运行测试
    test_bst()
