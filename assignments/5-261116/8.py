# 词频统计基础
# 描述：给定一行英文句子（单词之间用空格分隔），统计每个单词出现的次
# 数，并按插入顺序输出。
# 输入格式：一行字符串，由若干英文单词组成，单词之间用单个空格分隔。
# 输出格式：每行输出 "单词: 次数"，按首次出现顺序输出。
# 样例输入：apple banana apple cherry banana apple
# 样例输出：apple: 3
# banana: 2
# cherry: 1

sentence = input().split()
word_count = {}
for word in sentence:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for key in word_count.keys():
    print(f"{key}: {word_count[key]}")
