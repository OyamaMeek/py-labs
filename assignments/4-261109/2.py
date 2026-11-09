# 成绩等级判定
# 分值：10   预估时间：10分钟
# 描述：输入一个百分制成绩 score（0~100 的整数），
# 按以下规则输出等级：90 及以上为 A，80~89 为 B，70~79 为 C，
# 60~69 为 D，60 以下为 E。
# 输入格式：一行，一个整数 score（0 ≤ score ≤ 100）。
# 输出格式：一行，一个大写字母等级。
# 样例输入：85
# 样例输出：B

score=int(input())
if score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")
elif score>=60:
    print("D")
else:
    print("E")