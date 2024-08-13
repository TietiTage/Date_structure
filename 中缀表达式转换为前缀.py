# 运用栈
# 若要定义后缀表达式,只需要将代码当中的翻转去除,并将左右括号的作用互换一下


import functools
import stack


@functools.total_ordering
class SymbolStack(stack.Stack):
    def __ge__(self, other):
        # 当前符号栈顶元素与其他操作符的优先级比较
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        return precedence.get(self.top(), 0) >= precedence.get(other, 0)

def transform(_str: str) -> str:
    sym_stack = SymbolStack()
    output = []
    list_unprocessed = list(_str)[::-1]  # 逆转输入字符串

    for char in list_unprocessed:
        if char.isdigit():
            output.append(char)
        elif char == ')':
            sym_stack.push(char)
        elif char == '(':
            while sym_stack.top() != ')':
                output.append(sym_stack.pop())
            sym_stack.pop()  # 弹出右括号
        else:  # 操作符
            while not sym_stack.is_empty() and sym_stack >= char:
                output.append(sym_stack.pop())
            sym_stack.push(char)

    # 将剩余符号栈中元素弹出
    while not sym_stack.is_empty():
        output.append(sym_stack.pop())

    return ' '.join(output[::-1])  # 逆转输出并返回


if __name__ == '__main__':
    expression = "3+4*(2-1)"  # 输入的中缀表达式
    result = transform(expression)
    print(result)  # 输出前缀表达式
