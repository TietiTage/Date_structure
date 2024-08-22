# 实现一个AVL树
# 继承之前已经实现的二叉查找树,重写_put方法,并实现调整平衡的代码
import 二叉查找树 as bst


class AVLTreeNode(bst.TreeNode):
    def __init__(self, key: int, value, parent=None, left=None, right=None):
        """
        调用父类当中的初始化方法,在此基础上加上平衡因子的初始化
        :param key:
        :param value:
        :param parent:
        :param left: 左子树的第一个节点
        :param right: 右子树的第一个节点
        """
        super().__init__(key, value, parent, left, right)
        self.balanceFactor = 0


class AVLTree(bst.BinarySearchTree):

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
                current_node.left = AVLTreeNode(key, value, parent=current_node)
                self._retrim(current_node.left)
        # 递归生成右子树
        elif key > current_node.key:
            if current_node.has_right():
                self._put(key, value, current_node.right)
            else:
                current_node.right = AVLTreeNode(key, value, parent=current_node)
                self._retrim(current_node.right)
        else:
            current_node.payload = value

    def _modify_balance(self, node):
        if node.balance_factor > 1 or node.balance_factor < -1:
            self._retrim(node)
            return
        if node.parent is not None:
            if node.is_left():
                node.parent.balanceFactor += 1
            elif node.is_right():
                node.parent.balanceFactor -= 1
            if node.parent.balanceFactor != 0:
                self._modify_balance(node.parent)

    def _retrim(self,node):
        ...