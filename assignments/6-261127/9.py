# 斐波那契数列函数
# 描述：定义函数 fib(n)，返回前 n 项斐波那契数列（以 1、
# 1 开始）组成的列表。读入一个正整数 n，输出该列表（用 Pyth
# on 列表的默认打印格式）。
# 输入格式：一行，一个正整数 n。
# 输出格式：一行，前 n 项斐波那契数列的列表。
# 样例输入：5
# 样例输出：[1, 1, 2, 3, 5]
def fib(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]

    fib_sequence = [1, 1]
    for i in range(2, n):
        next = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next)

    return fib_sequence

n = int(input())
print(fib(n))