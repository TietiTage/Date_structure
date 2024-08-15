from typing import Optional
# 链表本身是一个数据结构,本身不存储值,其指向的应该是一个地址
# 不推荐在py当中使用链表
class LinkNode:
    def __init__(self, val: int = 0) -> None:
        # 初始化链表的第一个节点
        self.val = val # 链表的所处位置的索引
        self.next = None # 链表指向的下一个节点,初始为None

    def __repr__(self) -> str:
        # 别这么用,链表过长会超过递归层数
        return f'{self.val}->{repr(self.next)}'

    @staticmethod
    def make(arr: [int]) -> Optional['LinkNode']:  # 一个节点"列表",应该为一个iter
        root = LinkNode()  # 初始化根节点
        node = root  # 将当前根节点设为初始节点
        for num in arr:
            node.next = LinkNode(num) # 链接到下一个节点
            node = node.next # 将下一个节点设为初始结点
        return root.next


link = LinkNode.make([1, 2, 3, 4, 5])
print(link)

# 博客园代码,留作参考