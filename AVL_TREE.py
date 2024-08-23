# 实现一个AVL树
# 继承之前已经实现的二叉查找树,重写_put方法,并实现调整平衡和旋转的代码
import 二叉查找树 as BST
import time


class AVLTreeNode(BST.TreeNode):
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


class AVLTree(BST.BinarySearchTree):

    def _put(self, key, value, current_node):
        """
        使用AVLTreeNode类来构建节点信息,并递归生成节点,根据key的大小关系构建
        动态地调节负载
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

    def _modify_balance(self, node: AVLTreeNode):
        """
        根据平衡因子,调整负载
        :param node: 需要调整负载的节点
        :return:
        """
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self._retrim(node)
            return
        # 对父节点的负载进行更新
        if node.parent is not None:
            if node.is_left():
                node.parent.balanceFactor += 1
            elif node.is_right():
                node.parent.balanceFactor -= 1
            # 若调整后不为0,递归更新父节点的负载
            if node.parent.balanceFactor != 0:
                self._modify_balance(node.parent)

    def _retrim(self, node):
        if node.balanceFactor < 0:
            if node.right.balanceFactor > 0:
                self._rotate_right(node.right)
                self._rotate_left(node)
            else:
                self._rotate_left(node)
        elif node.balanceFactor > 0:
            if node.left.balanceFactor < 0:
                self._rotate_left(node.left)
                self._rotate_right(node)
            else:
                self._rotate_right(node)

    def _rotate_left(self, rot_root):
        new_root = rot_root.right
        rot_root.right = new_root.left
        if new_root.left is not None:
            new_root.left.parent = rot_root
        new_root.parent = rot_root.parent
        if rot_root.is_root():
            self.root = new_root
        else:
            if rot_root.is_left():
                rot_root.parent.left = new_root
            else:
                rot_root.parent.right = new_root
        new_root.left = rot_root
        rot_root.parent = new_root
        rot_root.balanceFactor = rot_root.balanceFactor + 1 - min(new_root.balanceFactor, 0)
        new_root.balanceFactor = new_root.balanceFactor + 1 + max(rot_root.balanceFactor, 0)

    def _rotate_right(self, rot_root):
        new_root = rot_root.left
        rot_root.left = new_root.right
        if new_root.right is not None:
            new_root.right.parent = rot_root
        new_root.parent = rot_root.parent
        if rot_root.is_root():
            self.root = new_root
        else:
            if rot_root.is_right():
                rot_root.parent.right = new_root
            else:
                rot_root.parent.left = new_root
        new_root.right = rot_root
        rot_root.parent = new_root
        rot_root.balanceFactor = rot_root.balanceFactor - 1 - max(new_root.balanceFactor, 0)
        new_root.balanceFactor = new_root.balanceFactor - 1 + min(rot_root.balanceFactor, 0)

def test_avl_tree():
    # 创建一个 AVL 树实例
    avl = AVLTree()

    # 插入节点
    avl[10] = "Root"
    avl[5] = "Left Child"
    avl[15] = "Right Child"
    avl[3] = "Left Grandchild"
    avl[7] = "Right Grandchild"
    avl[13] = "Left Right Grandchild"
    avl[17] = "Right Right Grandchild"

    # 测试插入和查找功能
    assert avl[10] == "Root", "Test failed: Root node"
    assert avl[5] == "Left Child", "Test failed: Left child"
    assert avl[15] == "Right Child", "Test failed: Right child"
    assert avl[3] == "Left Grandchild", "Test failed: Left grandchild"
    assert avl[7] == "Right Grandchild", "Test failed: Right grandchild"
    assert avl[13] == "Left Right Grandchild", "Test failed: Left right grandchild"
    assert avl[17] == "Right Right Grandchild", "Test failed: Right right grandchild"

    # 测试删除功能
    del avl[3]
    assert avl[3] is None, "Test failed: Deleting left grandchild"
    del avl[5]
    assert avl[5] is None, "Test failed: Deleting left child"
    del avl[10]
    assert avl[10] is None, "Test failed: Deleting root node"

    # 测试树的大小
    assert avl.length() == 4, "Test failed: Tree size"

    # 测试包含功能
    assert 15 in avl, "Test failed: Contains right child"
    assert 3 not in avl, "Test failed: Does not contain deleted node"

    # 重新初始化树并插入节点
    avl = AVLTree()
    avl[10] = "Root"
    avl[5] = "Left Child"
    avl[15] = "Right Child"
    avl[3] = "Left Grandchild"
    avl[7] = "Right Grandchild"
    avl[13] = "Left Right Grandchild"
    avl[17] = "Right Right Grandchild"

    # 测试中序遍历
    inorder_keys = [key for key in avl.root]
    assert inorder_keys == [3, 5, 7, 10, 13, 15, 17], "Test failed: Inorder traversal"

    print("All tests passed!")
a = time.perf_counter()
# 运行测试
test_avl_tree()

b = time.perf_counter()
print(f"Time taken: {b-a}")