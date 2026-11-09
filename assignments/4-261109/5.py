# n的阶乘
# 分值：10   预估时间：10分钟
# 描述：输入正整数 n，计算 n! = 1×2×...×n 的值并输出。
# 输入格式：一行，一个正整数 n（1 ≤ n ≤ 20）。
# 输出格式：一行，一个整数表示阶乘结果。
# 样例输入：5
# 样例输出：120
n=int(input())
factorial=1
for i in range(1,n+1):
    factorial*=i
print(factorial)
