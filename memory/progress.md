# 当前进度

## 8.py 正负数统计

- [x] 阅读代码、附件和已有用户修改，定位 split 未调用、字符串未转整数、外层循环无法结束的问题。
- [x] 通过 PyCharm 确认项目解释器为 Python 3.9.6。
- [x] 用样例回归测试复现附件中的 TypeError。
- [x] 使用 `map(int,input().split())` 和单层循环完成统计，7 组输入检查通过；包括乘法表在内的 3 项测试全部通过，`git diff --check` 通过。
- [x] 更新开发日志，提交 `63d8ce6 fix: count signed integers from one input line`，已普通推送至 `origin/main`。

## 10.py 乘法表输出

- [x] 阅读题目附件、脚本和引用，确认每行末尾多输出空格。
- [x] 通过 PyCharm 确认项目解释器为 Python 3.9.6。
- [x] 运行回归测试，确认修改前因行尾空格失败。
- [x] 仅修改输出结束符；标准库 unittest 的 2 项测试通过，覆盖样例和全部合法输入 1～9；`git diff --check` 通过。
- [x] 更新日志，提交 `e724433 fix: remove trailing spaces from multiplication table`，已普通推送至 `origin/main`。

## f-string 详细笔记

- [x] 阅读 `4.py`、现有记录和 Git 状态，核对 Python 官方文档。
- [x] 通过 PyCharm 确认项目解释器为 Python 3.9.6。
- [x] 编写 18 节详细笔记，包含输出、常见错误、速查表和 6 道练习及答案。
- [x] Python 3.9.6 doctest：126 条示例全部通过；原练习 4 组输入输出断言通过；`git diff --check` 通过。
- [x] 更新开发日志，提交 `51bc3e5 docs: add detailed f-string study notes`，已普通推送至 `origin/main`。

## 7.py 同一行输入

- [x] 检查目标脚本和引用，未发现调用方或关联测试。
- [x] 修改前输入 `3 4 5 ,`，确认抛出 `ValueError`。
- [x] 使用 `split` 和 `map` 读取同一行数据。
- [x] 使用项目解释器运行 4 组输入，输出断言通过，退出码为 0，标准错误为空；`git diff --check` 通过。
- [x] 提交 `83c276d fix: read exercise 7 input from one line`，已推送至 `origin/main`。

## 历史任务：L1

- [x] 阅读题目图片和空白 `character1/L1.py`。
- [x] 确认项目 Python 版本为 3.9.6，本地日期为 2026-10-19。
- [x] 完成五行输出和逐条注释；个人资料暂显示“待填写”。
- [ ] 收到用户的姓名、班级、学号后替换三项文字。
- [x] 实际运行脚本，五行输出、日期、解释器版本及逐条注释断言通过，标准错误为空。
- [x] 更新开发记录，创建提交 `19fd4fc feat: complete L1 information card exercise`。
- [ ] 推送到 `https://github.com/OyamaMeek/py-labs.git` 的 `main`：自动审批以缺少具体目的地授权为由拒绝，等待用户明确授权。

已有其他文件的暂存和未暂存修改，均不纳入本任务提交。
