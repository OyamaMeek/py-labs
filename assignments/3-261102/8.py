# 文本词频 Top N
# 分值：15   预估时间：10分钟
# 描述：给定一段英文文本（只包含字母和空格），
# 请统计出现次数最多的前 N 个单词（不区分大小写，统一转为小写）。按出现次数从高到低输出；
# 若次数相同，按单词字典序升序输出。每行输出 `单词:次数`。
# 输入格式：第一行一个整数 N；第二行一段英文文本（可能包含多个空格）。
# 输出格式：最多 N 行，每行格式为 `单词:次数`。
# 样例输入：2
# The cat and the dog and the bird
# 样例输出：the:3
# and:2
n=int(input())
text=input()
words=text.lower().split()
word_count={}
for word in words:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1
# 按出现次数从高到低排序，若次数相同按单词字典序升序排序
sorted_words=sorted(word_count.items(),key=lambda x:(-x[1],x[0]))
for i in range(min(n,len(sorted_words))):
    print(f"{sorted_words[i][0]}:{sorted_words[i][1]}")