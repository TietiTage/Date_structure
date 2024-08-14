import collections as cl

# 判断一个词是否是回文词
def palindrome(word: str) -> bool:
    if word.isalpha() is True:
        word = word.lower()
        word_queue = cl.deque()
        word_queue.extend(word)
        for i in range(len(word_queue)):
            if len(word_queue) > 1:
                fir = word_queue.pop()
                lst = word_queue.popleft()
                if lst == fir:
                    continue
                else:
                    print("不是回文词")
                    return False
        print("是回文词")
        return True
    else:
        print("不是一个单词")
        return False

if __name__ == "__main__":
    palindrome("wow")
    palindrome("114514")
    palindrome("wuwu")