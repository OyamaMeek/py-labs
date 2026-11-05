# 统计单词出现次数
# 描述：给定一行由空格分隔的英文单词（全部为小写字母），
# 请统计每个单词出现的次数，并按单词首次出现的顺序输出每个单词及其出现次数。
# 输入格式：一行，多个英文单词，单词之间用一个或多个空格分隔。
# 输出格式：多行，每行格式为 `单词:次数`。
# 样例输入：apple banana apple cherry banana apple
# 样例输出：apple:3
# banana:2
# cherry:1
s = input()
words = s.split()
for word in words:
    if words.count(word) > 0:
        print(f"{word}:{words.count(word)}")
        words = [w for w in words if w != word]