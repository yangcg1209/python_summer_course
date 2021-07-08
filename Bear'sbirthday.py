# _*_ coding : UTF-8 _*_
# 开发人员  :   YangFD
# 开发时间  :   2021/7/7  15:36
# 文件名称  :   Bear'sbirthday.PY
# 开发工具  :   PyCharm
year = int(input())
month = int(input())
day = int(input())
print("My birthday is {:d}.{:0>2d}.{:0>2d}".format(year, month, day))