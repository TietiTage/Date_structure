# 将word文件的单词变为一行

def preprocess_file(input_file, output_file):
    with open(input_file, "r") as infile:
        content = infile.read()

    # 将空格替换为换行符
    content = content.replace(" ", "\n")

    with open(output_file, "w") as outfile:
        outfile.write(content)


# 使用示例
input_file = "word_file.txt"
output_file = "output_file.txt"
preprocess_file(input_file, output_file)