# _*_ coding : UTF-8 _*_
# 开发人员  :   YangFD
# 开发时间  :   2021/7/6  18:28
# 文件名称  :   PerimeterofTriangle.PY
# 开发工具  :   PyCharm
import math
x, y = map(float, input().split())
v1 = [x, y]
x, y = map(float, input().split())
v2 = [x, y]
x, y = map(float, input().split())
v3 = [x, y]

peri = math.sqrt((v1[0] - v2[0]) ** 2 + (v1[1] - v2[1]) ** 2) \
       + math.sqrt((v2[0] - v3[0]) ** 2 + (v2[1] - v3[1]) ** 2) \
       + math.sqrt((v1[0] - v3[0]) ** 2 + (v1[1] - v3[1]) ** 2)
print("{:.2f}".format(peri))