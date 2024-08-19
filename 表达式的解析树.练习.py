class BuildParseTree:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        if self.left is None:
            self.left = BuildParseTree(value)
        else:
            t = BuildParseTree(value)
            t.left = self.left
            self.left = t

    def insert_right(self, value):
        if self.right is None:
            self.right = BuildParseTree(value)
        else:
            t = BuildParseTree(value)
            t.right = self.right
            self.right = t


def build_tree(expression):
    t = BuildParseTree()  # 初始化一个树
    path_stack = [t]  # 初始化一个栈
    current_tree = t

    for char in expression:
        if char == '(':
            current_tree.insert_left(None)
            path_stack.append(current_tree)
            current_tree = current_tree.left
        elif char in "+-*/":
            current_tree.value = char
            current_tree.insert_right(None)
            path_stack.append(current_tree)
            current_tree = current_tree.right
        elif char.isdigit():
            current_tree.value = int(char)
            current_tree = path_stack.pop()
        elif char == ")":
            current_tree = path_stack.pop()

    return t

# def evaluate(tree):
#     if tree.left.value.isdigit() and tree.right.value.isdigit():
#         res =  "".join([tree.left.value, tree.value, tree.right.value])
#         return eval(res)
#     else:
#         return eval(''.join([evaluate(tree.left), tree.value, evaluate(tree.right)]))

 # 利用前序遍历求解表达式的值
def evaluate(tree):
    if tree.left is None and tree.right is None:
        return tree.value
    left_val = evaluate(tree.left)
    right_val = evaluate(tree.right)
    return eval(f'{left_val} {tree.value} {right_val}')

def inorder_traversal(tree):
    if tree is None:
        return ""
    left_expr = inorder_traversal(tree.left)
    right_expr = inorder_traversal(tree.right)
    if left_expr or right_expr:
        return f"({left_expr}{tree.value}{right_expr})"
    else:
        return str(tree.value)



if __name__ == '__main__':
    expression = "(3+(5*(4+5)))" # 必须是全括号表达式
    parse_tree = build_tree(expression)
    result = evaluate(parse_tree)
    print(result)
    print(inorder_traversal(parse_tree))