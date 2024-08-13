# 对两个长度相同的字符串进行逐个单词比对，
def check(func):
    def wrapper(str1, str2):
        if (not isinstance(str1, str)) or (not isinstance(str2, str)):
            print("无效输入，类型应为字符串")
            raise TypeError
        elif len(str1) != len(str2):
            print("错误的输入，两个字符串的长度必须相等")
            raise Exception
        return func(str1, str2)
    return wrapper


@check
def match(str1: str, str2: str):
    """
    对两个字符串从第一个单词出开始匹配
    :param str1: 进行匹配的第一个字符串
    :param str2: 进行匹配的第二个字符串
    :return: 返回两个字符串的匹配成功的字符数，若不匹配，指出二者从何处开始不同
    """
    count = 0
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            count += 1
        else:
            print(f"在第{i+1}个字符处不匹配，字符为{str1[i]}与{str2[i]}")
            break
        if count == len(str1):
            print("字符串完全匹配")

if __name__ == '__main__':
    match("114514","114514")
    match("1214514","1314514")
    match(1214514,1314514)