import stack
import re


class SymbolStack(stack.Stack):
    def __ge__(self, other):
        # 当前符号栈顶元素与其他操作符的优先级比较
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        return precedence.get(self.top(), 0) >= precedence.get(other, 0)

def transform(_str: str) -> str:
    symbol_stack = SymbolStack()
    output = []
    # 使用正则表达式来分割输入字符串
    unprocessed_str_list = re.findall(r'\d+|[+*/()-]', _str.replace(' ', ''))
    # print(unprocessed_str)
    for char in unprocessed_str_list:
        if char.isdigit():
            output.append(char)
        elif char == '(':
            symbol_stack.push(char)
        elif char == ')':
            while symbol_stack.top() != '(':
                output.append(symbol_stack.pop())
            symbol_stack.pop() # 弹出左括号
        else:
            while (symbol_stack.is_empty() is False) and symbol_stack >= char:
                output.append(symbol_stack.pop())
            symbol_stack.push(char)

    while symbol_stack.is_empty() is False:
        output.append(symbol_stack.pop())
        res = ' '.join(output)
    return res



import re

def solve(expression: str) -> float:
    """
    求解后缀表达式的值
    :param expression: 一个后缀表达式,符号和不同的数字当中用空格分隔
    :return: 后缀表达式的值,应该为数字
    """
    tokens = expression.split()
    stack = []

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2
            stack.append(result)

    return stack.pop()

import re

def solve(expression: str) -> float:
    """
    求解后缀表达式的值
    :param expression: 一个后缀表达式,符号和不同的数字当中用空格分隔
    :return: 后缀表达式的值,应该为数字
    """
    tokens = expression.split()
    stack = []

    for token in tokens:
        if token.isdigit():
            stack.append(token)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = str(eval(''.join([operand1, token, operand2])))
            stack.append(result)

    return stack.pop()

if __name__ == "__main__":
    my_str = input("请输入一个后缀表达式字符串（例如：'3 4 + 2 * 7 /'）：")
    print(solve(my_str))


# if __name__ == "__main__":
#     my_str = input("Enter a expression string, if a minus num precedes, add 0 in front of it: ")
#     print(transform(my_str))