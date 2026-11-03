## [2026-10-19 11:32] L1 个人信息卡与环境自检

- **需求/问题描述**：
  > 根据题目图片完成 `character1/L1.py`，输出个人信息及本机 Python 环境。

- **实际实现的功能与改动**：
  - 使用五条 `print` 输出姓名、班级、学号、当前日期和 Python 版本，每条语句前有中文注释。
  - 姓名、班级、学号尚未提供，明确标为“待填写”；日期为 2026-10-19，项目解释器版本为 3.9.6。
  - 测试前确认空文件输出 0 行，五行输出断言失败；实现后使用项目解释器实际运行，五行输出、日期、版本和逐条注释断言全部通过，退出码为 0，标准错误为空。
  - `git diff --check` 通过；项目没有现成的测试或静态检查配置。

- **涉及文件**：
  - `character1/L1.py`
  - `memory/agents.md`、`memory/plan.md`、`memory/progress.md`、`memory/verify.md`、`memory/gotchas.md`
  - `docs/CHANGELOG.md`

- **Git 提交**：`19fd4fc feat: complete L1 information card exercise`。
- **推送状态**：自动审批拒绝了向 `https://github.com/OyamaMeek/py-labs.git` 的 `main` 分支执行普通推送，理由是缺少对该具体目的地的明确授权；远端未更新。

---

## [2026-10-27 23:23] 7.py 同一行输入

- **需求/问题描述**：
  > 三个整数及分隔符从同一行输入，使用 map 和 split。

- **实际实现的功能与改动**：
  - 使用 `input().split()` 拆分四项，使用 `map(int, ...)` 转换三个整数，保留指定分隔符输出。
  - 修改前题目示例触发 `ValueError`；修改后示例、负数与零、多余空白、整数格式转换共 4 组实际运行与输出断言通过，标准错误为空。
  - `git diff --check` 通过；未新增依赖或测试框架。

- **涉及文件**：
  - `work/2-261026/7.py`
  - `memory/agents.md`、`memory/plan.md`、`memory/progress.md`、`memory/verify.md`、`memory/gotchas.md`
  - `docs/CHANGELOG.md`

- **Git 提交**：`83c276d fix: read exercise 7 input from one line`，已推送至 `origin/main`。

---

## [2026-11-03 17:13] f-string 详细学习笔记

- **需求/问题描述**：
  > 结合 `work/3-261102/4.py` 整理一份 f-string 的详细笔记。

- **实际实现的功能与改动**：
  - 新增 18 节中文笔记，逐项解释原题，覆盖常用格式、表达式、转义、调试、动态格式、日期、常见错误、速查表和 6 道练习答案。
  - 说明两个 `f` 的区别、最小宽度、浮点舍入和中文显示宽度，附 Python 官方文档链接。
  - Python 3.9.6 doctest：126 条示例全部通过；原练习普通输入、中文、超宽内容和负数共 4 组输入输出断言通过，退出码为 0、标准错误为空。
  - `git diff --check` 通过；未修改练习脚本，未新增依赖，未执行视觉检查。

- **涉及文件**：
  - `docs/f-string笔记.md`
  - `memory/agents.md`、`memory/plan.md`、`memory/progress.md`、`memory/verify.md`
  - `docs/CHANGELOG.md`

- **Git 提交**：`51bc3e5 docs: add detailed f-string study notes`，已推送至 `origin/main`。

---
