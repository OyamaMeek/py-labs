# 列表增删改查
# 描述：对一个列表依次执行若干操作。操作类型有：ADD x（在末尾追
# 加 x）
# INSERT i x（在下标 i 处插入 x）、REMOVE x（
# 删除第一个值为 x 的元素）、SET i x（把下标 i 处的元素
# 改为 x）。最后输出列表。
# 输入格式：第一行输入一个整数 n，表示初始元素个数；第二行输入 n
#  个整数；第三行输入整数 m，表示操作次数；接下来 m 行，每行一
# 个操作，格式如题意。
# 输出格式：输出操作完成后最终的列表。
# 样例输入：3
# 1 2 3
# 3
# ADD 4
# INSERT 0 0
# REMOVE 2
# 样例输出：[0, 1, 3, 4]
num = int(input())
#创建一个长度为num的列表
list = [0] * num
values = input().split()
for i in range(num):
    list[i] = int(values[i])
m = int(input())
for i in range(m):
    operation = input().split()
    if operation[0] == "ADD":
        list.append(int(operation[1]))
    elif operation[0] == "INSERT":
        list.insert(int(operation[1]), int(operation[2]))
    elif operation[0] == "REMOVE":
        list.remove(int(operation[1]))
    elif operation[0] == "SET":
        list[int(operation[1])] = int(operation[2])
print(list)