# 提取用户名与域名
# 分值：15   预估时间：10分钟
# 描述：给定一个邮箱地址（格式为 `用户名@域名`），
# 请分别输出用户名和域名。用户名可能包含字母、数字、下划线、点号，域名至少包含一个点号。
# 输入格式：一行，一个合法的邮箱地址字符串。
# 输出格式：两行，第一行为用户名，第二行为域名。
# 样例输入：zhangsan_2024@example.com
# 样例输出：zhangsan_2024
# example.com
email = input()
username = email.split('@')[0]
domain = email.split('@')[1]
print(username)
print(domain)
