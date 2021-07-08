# _*_ coding : UTF-8 _*_
# 开发人员  :   YangFD
# 开发时间  :   2021/7/6  18:05
# 文件名称  :   X'sStudyPlan.PY
# 开发工具  :   PyCharm
import datetime

d1 = datetime.datetime.now()
h, m = map(int, input().split())
n = int(input())
d2 = datetime.datetime(d1.year, d1.month, d1.day, h, m, 0, 0)
d3 = datetime.datetime(d1.year, d1.month, d1.day, 23, 30, 0, 0)
d4 = d2 + datetime.timedelta(minutes=n)
if d4 < d3:
    print("{:0>2d}:{:0>2d}".format(d4.hour, d4.minute))
else:
    print("23:30")