# 不定长参数求和函数
# 描述：定义函数 total(*nums)，返回所有传入数字的和；不
# 传任何数字时返回 0。读入一行若干个整数，调用 total 输出它
# 们的和。
# 输入格式：一行，若干个整数，用空格分隔。
# 输出格式：一行，所有整数之和。
# 样例输入：1 2 3 4
# 样例输出：10
def total(*nums):
    sum = 0
    for num in nums:
        sum += num
    return sum


nums=input().split()
nums = list(map(int, nums))
print(total(*nums))




# numbers = list(map(int, input().split()))
# print(total(*numbers))