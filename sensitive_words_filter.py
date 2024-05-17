import jieba

# 定义一个函数来加载敏感词库并生成敏感词列表
def load_sensitive_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        sensitive_words = [line.strip() for line in file.readlines()]
    return sensitive_words

# 定义一个函数来检测输入文本中是否包含敏感词
def check_sensitive_words(text, sensitive_words):
    words = jieba.lcut(text)  # 适用中文的分词库
    for word in words:
        if word in sensitive_words:
            return 1  # 发现敏感词，返回1
    return 0  # 没有发现敏感词，返回0

if __name__=='__main__':
    # 敏感词库文件路径
    word_file_path = 'sensitive_words_lines.txt'

    # 加载敏感词列表
    sensitive_words_list = load_sensitive_words(word_file_path)

    # 测试样例
    test_text = "请输入内容"

    # 检测测试样例中的文本
    result = check_sensitive_words(test_text, sensitive_words_list)

    print(result)  # 输出 1 或 0