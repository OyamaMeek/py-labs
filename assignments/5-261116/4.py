# 成绩列表统计
# 描述：给定一组成绩，用列表相关的内置函数统计：总人数、总分、最高分
# 、最低分、平均分（保留两位小数）。
# 输入格式：第一行输入整数 n；第二行输入 n 个整数。
# 输出格式：第一行输出人数；第二行输出总分；第三行输出最高分；第四行
# 输出最低分；第五行输出平均分，保留两位小数。
# 样例输入：4
# 80 90 70 60
# 样例输出：4
# 300
# 90
# 60
# 75.00
num=int(input())
list = [0] * num
values = input().split()
for i in range(num):
    list[i] = int(values[i])
print(len(list))
print(sum(list))
print(max(list))
print(min(list))
print(f"{sum(list)/len(list):.2f}")