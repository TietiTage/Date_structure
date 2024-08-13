# from collections import deque
# def match(my_str):
#
#     bracket_stack = deque([])
#
#     for char in my_str:
#         if char == "(":
#             bracket_stack.append(char)
#         elif char == ")":
#             if len(bracket_stack) == 0:
#                 print("无法匹配")
#                 return
#             else:
#                 bracket_stack.pop()
#
#     if len(bracket_stack) == 0:
#         print("匹配完成")
#     else:
#         print("无法匹配")
#
# match("()()()()()()")
# 只能适用于一种括号的情形
import stack


def check(_stackstr: str, _matchstr: str) -> bool:
    check_dic = {"(": ")", "{": "}", "[": "]"}
    return check_dic[_stackstr] == _matchstr

def match(_str: str) -> bool:
    my_stack = stack.Stack()
    index = 0
    balance = True
    while index < len(_str) and balance:
        char = _str[index]
        if char in ['[', '{', "("]:
            my_stack.push(char)
        elif char in [']', '}', ")"]:
            if my_stack.is_empty() is False:
                check_result = check(my_stack.pop(), char, )
                balance = check_result
            else:
                balance = False
        index += 1

    if balance and my_stack.is_empty():
        print("匹配完成")
        return True
    else:
        print(f"匹配失败:在第{[index]}处的字符{_str[index - 1]}不匹配")
    return False


match("[{})][][]{{_}}")
match("1510")

