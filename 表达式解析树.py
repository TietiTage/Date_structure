# GPT生成,应该自己敲一遍


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# 全括号的中缀表达式
def build_parse_tree(expression):
    tokens = expression.split()
    stack = []
    tree = TreeNode('')
    current = tree
    stack.append(current)

    for token in tokens:
        if token == '(':  # 若token是左括号
            current.left = TreeNode('')  # 初始化当前节点的左子树
            stack.append(current)  # 当前节点入栈
            current = current.left  # 移动到当前节点的左节点
        elif token in ['+', '-', '*', '/']:  # token为运算符
            current.value = token  # 记录当前值
            current.right = TreeNode('')  # 将右子树进行初始化
            stack.append(current)  # 将当前节点入栈
            current = current.right  # 当前节点设置为右子树的根节点
        elif token.isdigit():  # 若节点为数字
            current.value = int(token)  # 将节点的值变为整数
            current = stack.pop()  # 回到父节点
        elif token == ')':
            current = stack.pop()  # 子表达式结束,回到父节点

    return tree


def evaluate(tree):
    if tree.left is None and tree.right is None:
        return tree.value
    left_val = evaluate(tree.left)
    right_val = evaluate(tree.right)
    if tree.value == '+':
        return left_val + right_val
    elif tree.value == '-':
        return left_val - right_val
    elif tree.value == '*':
        return left_val * right_val
    elif tree.value == '/':
        return left_val / right_val


if __name__ == '__main__':
    # 示例表达式
    expression = "( ( 3 + 5 ) * ( 2 - 1 ) )"
    parse_tree = build_parse_tree(expression)
    result = evaluate(parse_tree)
    print(f"表达式的结果是: {result}")
