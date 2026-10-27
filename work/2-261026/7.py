# 输入三个整数x, y, z 及分隔符c，按照指定的分隔符输出
#
# 例：
#
# 输入： 3 4 5 ,
#
# 输出：3,4,5
x, y, z, c = input().split()
x, y, z = map(int, (x, y, z))
print(f"{x}{c}{y}{c}{z}")
#fix:一行输入