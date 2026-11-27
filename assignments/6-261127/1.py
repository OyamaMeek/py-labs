# 带参数的三角形打印函数
# 描述：定义函数 triangle(n)，打印一个由星号组成的直角三
# 角形，第 1 行 1 个星号，第 2 行 2 个星号，依此类推，第
#  n 行 n 个星号。
# 输入格式：一行，一个正整数 n。
# 输出格式：共 n 行，第 i 行包含 i 个星号。
# 样例输入：3
# 样例输出：*
# **
# ***
def triangle(n):
    for i in range(1, n + 1):
        print('*' * i)
n=int(input())
triangle(n)