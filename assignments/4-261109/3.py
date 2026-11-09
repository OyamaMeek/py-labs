# 三个数最大值
# 分值：10   预估时间：10分钟
# 描述：输入三个整数 a、b、c，输出其中的最大值。
# 输入格式：一行，三个整数 a、b、c，用空格分隔
# （-1000000 ≤ a,b,c ≤ 1000000）。
# 输出格式：一行，一个整数，表示最大值。
# 样例输入：3 9 5
# 样例输出：9
a=int(input())
b=int(input())
c=int(input())
if a>=b and a>=c:
    print(a)
elif b>=a and b>=c:
    print(b)
else:
    print(c)
