# 十进制整数转换为16进制整数
def toStr(n, base):
    convertString = "0123456789ABCDEF"  # 用于将数字转换为对应进制字符的查找表

    if n < base:
        return convertString[n]  # 基本情况：如果 n 小于 base，直接返回对应的字符
    else:
        return toStr(n // base, base) + convertString[n % base]  # 递归情况：进行整数除法和取模运算，然后递归调用


print(toStr(1453, 16))  # 调用 toStr 函数，将 1453 转换为 16 进制表示
