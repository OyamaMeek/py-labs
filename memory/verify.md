# 完成标准

- 使用 PyCharm 确认的 Python 3.9.6，通过 subprocess 实际运行 `8.py`，不使用 mock。
- 修改前确认样例因 split 未调用而抛出 TypeError；修改后 7 组输入逐字符验证输出、退出码和标准错误。
- 覆盖样例、仅 0、全正数、全负数、额外空白、首个 0 后停止、较大整数。
- 运行 unittest discover，包含已有乘法表测试；项目无静态检查配置。
- 执行 `git diff --check`；仅暂存任务文件，保留 `3.py` 和 `.DS_Store` 的已有变化。
- 未访问判题系统，不能确认远端判题结果。
