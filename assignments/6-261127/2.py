# 两数求和与求积函数
# 描述：定义两个函数 add(a, b) 返回 a 与 b 的和，mul(a, b)
# 返回 a 与 b 的积。读入两个整数，分别调用两
# 个函数并输出结果。
# 输入格式：一行，两个整数 a 和 b，用空格分隔。
# 输出格式：两行，第一行为和，第二行为积。
# 样例输入：2 3
# 样例输出：5
# 6
def add(a, b):
    return a + b

def mul(a, b):
    return a * b

#a, b = map(int, input().split())
#用字符串
str_input = input().split()
a=int(str_input[0])
b=int(str_input[1])

print(add(a, b))
print(mul(a, b))