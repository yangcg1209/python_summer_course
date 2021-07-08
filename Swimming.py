# _*_ coding : UTF-8 _*_
# 开发人员  :   YangFD
# 开发时间  :   2021/7/7  15:40
# 文件名称  :   Swimming.PY
# 开发工具  :   PyCharm
target = float(input())
now = 0.0
step = 2.0
step_count = 0
while True:
    if now < target + 1e-8:
        now += step
        step_count += 1
    else:
        break
    step *= 0.98
print(step_count)