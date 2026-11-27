# 方差函数
# 描述：定义函数 variance(*nums)，用 sum 和 l
# en 自己计算总体方差（平方和除以个数，不除以 n-1）。空参数或
# 只有 1 个数时返回 0.0。读入一行若干个浮点数，输出方差，保留
#  2 位小数。
# 输入格式：一行，若干个浮点数，用空格分隔。
# 输出格式：一行，方差，保留 2 位小数。
# 样例输入：1 2 3
# 样例输出：0.67
def variance(*nums):
    #一个数好像自己减自己等于0了
    if len(nums) <= 1:
        return 0.0
    #平均数
    mean = sum(nums) / len(nums)
    #方差
    var = sum((x - mean) ** 2 for x in nums) / len(nums)
    return var

nums=input().split()
#转换成浮点数列表
nums = list(map(float, nums))
print(f"{variance(*nums):.2f}")