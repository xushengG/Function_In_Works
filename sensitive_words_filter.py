import jieba

# 定义一个函数来加载敏感词库并生成敏感词列表
def load_sensitive_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        sensitive_words = [line.strip() for line in file.readlines()]
    return sensitive_words

# 定义一个函数来检测输入文本中是否包含敏感词
def check_sensitive_words(text, sensitive_words):
    words = jieba.lcut(text)  # 适用中文的分词库
    new_text = ""
    flag=0
    for word in words:
        if word in sensitive_words:
            new_text += '*' * len(word)  # 替换为相同长度的星号
            flag=1
        else:
            new_text += word
        new_text += " "  # 添加空格以分隔单词
    return new_text.strip(), flag

if __name__=='__main__':
    # 敏感词库文件路径
    word_file_path = 'sensitive_words_lines.txt'

    # 加载敏感词列表
    sensitive_words_list = load_sensitive_words(word_file_path)

    # 测试样例
    test_text = "今天太阳很好，我想。"

    # 检测测试样例中的文本
    new_text, result = check_sensitive_words(test_text, sensitive_words_list)

    print(new_text, result) 
