# 列表索引与切片
# 描述：给定一个列表，按要求进行索引与切片操作，
# 输出取出的元素。
# 输入格式：第一行输入一个整数 n，表示列表长度；
# 第二行输入 n 个用空格分隔的整数；第三行输入三个整数 a b c
# 表示取索引 a、切片 [b:c]。
# 输出格式：第一行输出索引 a 对应的元素；第二行输出切片 [b:c]
# 得到的新列表（用 Python 列表格式输出）。
# 样例输入：5
# 10 20 30 40 50
# 2 1 4
# 样例输出：30
# [20, 30, 40]
num = int(input())
#创建一个长度为num的列表
list = [0] * num
# for i in range(num):
#     list[i] = int(input())
values = input().split()
for i in range(num):
    list[i] = int(values[i])
a, b, c = map(int, input().split())
print(list[a])
print(list[b:c])
