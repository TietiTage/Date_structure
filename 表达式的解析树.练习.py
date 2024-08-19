class BuildParseTree:
    def __init__(self, value=None):
        self.node = None
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

def evaluate(tree):
    if tree.left.value.isdigit() and tree.right.value.isdigit():
        res =  "".join([tree.left.value, tree.value, tree.right.value])
        return eval(res)
    else:
        return eval(''.join([evaluate(tree.left), tree.value, evaluate(tree.right)]))