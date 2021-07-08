# _*_ coding : UTF-8 _*_
# 开发人员  :   YangFD
# 开发时间  :   2021/7/6  17:01
# 文件名称  :   temp.PY
# 开发工具  :   PyCharm
n, k = map(int, input().split())
a, b = 0.0, 0.0
a_count = 0
for i in range(1, n + 1):
    if i % k == 0:
        a += i
        a_count = a_count + 1
    else:
        b += i
print("{:.1f} {:.1f}".format(a / a_count, b / (n - a_count)))