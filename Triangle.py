# _*_ coding : UTF-8 _*_
# 开发人员  :   YangFD
# 开发时间  :   2021/7/6  18:37
# 文件名称  :   Triangle.PY
# 开发工具  :   PyCharm
s = input()
for i in range(0, 3):
    for j in range(0, 5):
        if j < 2 - i:
            print(" ", end="")
        elif 2 - i <= j < 3 + i:
            print(s, end="")
        else:
            print("", end="")
    print()