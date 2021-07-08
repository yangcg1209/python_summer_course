# _*_ coding : UTF-8 _*_
# 开发人员  :   YangFD
# 开发时间  :   2021/7/6  18:23
# 文件名称  :   TerrifyingMorningClass.PY
# 开发工具  :   PyCharm
materials = input()
digits = 0
alphas = 0
for s in materials:
    if s.isdigit():
        digits = digits + 1
    elif s.isalpha():
        alphas = alphas + 1

print(digits)
print(alphas)
